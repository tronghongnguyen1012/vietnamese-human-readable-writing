# Báo cáo Tương thích 6 Tầng, Smoke Test Windows & Đề xuất Giấy phép (`compatibility-and-smoke-test.md`)

Tài liệu ghi nhận kết quả thực tế (chỉ báo cáo những gì đã kiểm chứng trực tiếp trên môi trường test, không suy đoán phần chưa chạy live):
1. Phân tích 4 repository tham chiếu.
2. Ma trận tương thích **6 tầng độc lập** trên các runtime AI.
3. Kết quả kiểm tra schema/cấu trúc của 6 tệp plugin manifest.
4. Nhật ký smoke test thực tế trên Windows (project-local, cập nhật `-p`, global cô lập `-g`, cài thủ công lặp lại).
5. Kiểm toán quyền sở hữu nội dung & đề xuất **MIT License** chờ chủ repository xác nhận.

---

## 1. Phân tích 4 Repository Tham chiếu

| Repository | Giấy phép | Điểm học hỏi về đóng gói & DX | Phần chủ động KHÔNG sao chép |
|---|---|---|---|
| `vercel-labs/skills` (`skills.sh`) | MIT | Cấu trúc chuẩn `skills/<name>/SKILL.md` để `npx skills add <owner>/<repo>` quét tự động; lệnh `--list`, `--copy`, `-g`, `-p`, `update`, `remove`. | Monorepo TypeScript & CLI source code. |
| `obra/superpowers` | MIT | Phân tách mục cài đặt gọn theo từng runtime (`Claude Code`, `Codex`, `Cursor`); manifest tối giản theo chuẩn từng hãng. | Thư viện đa skill, lifecycle `hooks`, tài sản nhận diện thương hiệu. |
| `tronghongnguyen1012/ponytail` | MIT | Hero branding gọn (logo + tagline ngắn + banner Light/Dark qua `<picture>`); bảng so sánh trực diện và tách riêng `INSTALL.md`. | Bộ `hooks`, telemetry CSV, script đa IDE phức tạp. |
| `cloudflare/security-audit-skill` | MIT | Giải thích cơ chế theo pha ngắn gọn cho kỹ sư, giữ cấu trúc repo dễ quét. | Kiến trúc đa tác nhân audit bảo mật đặc thù. |

**Phạm vi giữ nguyên của ViWrite:** Chỉ đóng gói skill thuần túy trong [`skills/vietnamese-human-readable-writing/`](../skills/vietnamese-human-readable-writing/) + các tệp manifest JSON tối giản — **không** tạo custom installer, hook, MCP server hay background service.

---

## 2. Ma trận Tương thích 6 Tầng (Tách bạch Trung thực)

Để tránh nhầm lẫn giữa việc *có tệp manifest / đã chạy thử qua subagent* với *runtime gốc đã tự nạp và tự kích hoạt ngoài thực tế*, toàn bộ khả năng tương thích được tách rõ thành **6 tầng độc lập**:

| Runtime | 1. Manifest / Schema hợp lệ | 2. Skills CLI Discovery (`--list`) | 3. File Installation (`--copy`) | 4. Native Runtime Discovery | 5. Native Auto Activation | 6. Đánh giá Chất lượng Model |
|---|---|---|---|---|---|---|
| **Antigravity (IDE / App / CLI)** | **Đạt Schema chính thức** (`antigravity.google/schemas/v1/plugin.json`) | **Đã xác minh** (`1 skill`) | **Đã kiểm thử Windows** (project-local & sandbox `-g` vào `.gemini\config\skills\`) | Chưa kiểm chứng live (`agy` CLI/App chưa cài trên máy test) | **Chưa kiểm chứng live** | **Đã đánh giá qua Antigravity Subagent** (Round 1, Round 2 & v4.1 trên `flash`/`pro`)\* |
| **Claude Code & Claude Code Desktop** | `marketplace.json` **đạt SchemaStore**; `plugin.json` hợp lệ cấu trúc | **Đã xác minh** (`1 skill`) | **Đã kiểm thử Windows** (project-local & sandbox `-g` vào `.claude\skills\`) | Chưa kiểm chứng live (`claude` CLI/Desktop chưa cài trên máy test) | Chưa kiểm chứng live | Chưa đánh giá trên model Claude |
| **OpenAI Codex (CLI / App / IDE Ext)** | **Hợp lệ cấu trúc** (`.agents/plugins/marketplace.json` dùng `source: local, path: "./"`) | **Đã xác minh** (`1 skill`) | **Đã kiểm thử Windows** (project-local & sandbox `-g` vào `.agents\skills\`) | Chưa kiểm chứng live (`codex` CLI/App chưa cài trên máy test) | Chưa kiểm chứng live | Chưa đánh giá trên model GPT/Codex |
| **Cursor** | **Hợp lệ cấu trúc** (`.cursor-plugin/plugin.json`) | **Đã xác minh** (`1 skill`) | **Đã kiểm thử Windows** (project-local & sandbox `-g` vào `.agents\skills\` & manual `.cursor\skills\`) | Chưa kiểm chứng live (Cursor chưa cài trên máy test) | Chưa kiểm chứng live | Chưa đánh giá trong Cursor Agent |

> [!IMPORTANT]
> **Ghi chú minh bạch về Antigravity (Tầng 4–5 vs Tầng 6):** Các đánh giá chất lượng văn bản (`eval-experiment-v4b`, `eval-trigger-tester`, `v4.1` targeted regression) được chạy qua **Antigravity subagent** với prompt test kiểm soát — tức chỉ là bằng chứng cho **Tầng 6 (Model Quality Evaluation)**, **KHÔNG** dùng để kết luận **Tầng 4 (Native Runtime Discovery)** hay **Tầng 5 (Native Automatic Activation)** trên Antigravity App/CLI thật. Skill cũng chưa đăng ký trên các curated marketplace chính thức của các hãng.

---

## 3. Kiểm tra Schema & Cấu trúc 6 Tệp Manifest

Máy kiểm thử hiện tại **không cài sẵn** `claude`, `codex`, `cursor` hay `agy` binary nên chưa chạy được `claude plugin validate` hay `agy plugin validate` trực tiếp. Tuy nhiên, đã chạy script Python kiểm tra từng tệp với các schema JSON công khai truy cập được và bộ quy tắc cấu trúc tài liệu chính thức:

| Tệp Manifest | Nguồn đối chiếu & Phương pháp | Kết quả kiểm tra |
|---|---|---|
| `.antigravity-plugin/plugin.json` | Fetch trực tiếp schema chính thức `https://antigravity.google/schemas/v1/plugin.json` (`additionalProperties: false`) | **Đạt** — đủ trường `name`, chỉ chứa trường hợp lệ (`displayName`, `version`, `description`, `logo`, `suggestedPrompts` gồm 3 câu, `author`, `homepage`, `repository`), `assets/logo.svg` tồn tại. |
| `.claude-plugin/marketplace.json` | Fetch trực tiếp SchemaStore `https://json.schemastore.org/claude-code-marketplace.json` | **Đạt** — đủ `name`, `owner.name`, `plugins[].source` khớp regex `^\.\/.*` (`"./"`). |
| `.claude-plugin/plugin.json` | Kiểm tra cấu trúc JSON (SchemaStore URL tạm trả `503 Service Unavailable` lúc test) | Hợp lệ cấu trúc (`name` kebab-case, `version` semver, `author`, không `hooks`/`mcpServers`). |
| `.agents/plugins/marketplace.json` | Đối chiếu cấu trúc tài liệu OpenAI Codex (`plugins`) | **Đã sửa lỗi P0** — đổi từ `"source": "url"` sang `"source": { "source": "local", "path": "./" }` trỏ đúng gốc repo chứa `skills/`. |
| `.codex-plugin/plugin.json` | Đối chiếu cấu trúc tài liệu OpenAI Codex (`skills`, `interface`) | Hợp lệ cấu trúc (`skills: "./skills/"`, `interface.displayName: "ViWrite"`, đủ `defaultPrompt`). |
| `.cursor-plugin/plugin.json` | Đối chiếu cấu trúc tài liệu Cursor (`skills` relative path; URL `cursor.com/schemas/plugin.schema.json` không trả JSON lúc test) | Hợp lệ cấu trúc (`name`, `displayName: "ViWrite"`, `version`, `skills: "./skills/"`). |

---

## 4. Nhật ký Smoke Test Thực tế trên Windows

- **Môi trường:** Windows 11 · Node `v24.18.0` · `npx.cmd` `11.16.0` · Thư mục cô lập trong `%TEMP%` (đã dọn sạch sau khi test).
- **Xác minh an toàn profile thật:** Đã chụp snapshot trước & sau test toàn bộ 4 đường dẫn trong `%USERPROFILE%` thật (`C:\Users\Ztayrong440z\...`) — tất cả đều giữ nguyên trạng thái `exists=False`, không ghi chạm vào cấu hình thật của máy.

| Hạng mục kiểm thử | Lệnh & Phạm vi | Kết quả thực tế quan sát được |
|---|---|---|
| **1. Discovery local & remote** | `npx.cmd --yes skills add . --list` và `... tronghongnguyen1012/vietnamese-human-readable-writing --list` | Exit `0` · Tìm thấy đúng **1 skill** (`vietnamese-human-readable-writing`), không trùng lặp do 6 tệp manifest. |
| **2. Cài Project-local đa agent (`--copy`) & kiểm tra SHA-256** | `npx.cmd --yes skills add <repo> -a antigravity claude-code codex cursor --copy -y` | Exit `0` · Copy đủ 5 file vào `.agents\skills\...` và `.claude\skills\...` · SHA-256 khớp 100% `v4.1.0-beta`. |
| **3. Cập nhật riêng Project-local (`-p`) từ GitHub** | Cài từ GitHub remote vào sandbox dự án → `npx.cmd --yes skills update -p -y` → `skills remove ... -y` | Exit `0` · `skills.sh` đánh giá repo `Gen: Safe`, `Socket: 0 alerts`, `Snyk: Low Risk`; `update -p -y` báo `✓ All project skills are up to date`. |
| **4. Cài Global cô lập (`-g --copy`)** | Đặt tạm `USERPROFILE`/`HOME`/`XDG_*`/`CODEX_HOME` vào `%TEMP%\viwrite-global-sandbox` → `npx.cmd --yes skills add <repo> -a antigravity claude-code codex cursor -g --copy -y` → `skills list -g --json` → `remove -g -y` | `add -g` Exit `0`, ghi đủ 15 file (5 file × 3 thư mục `~\.agents\skills\`, `~\.claude\skills\`, `~\.gemini\config\skills\`); `list -g --json` trả `status: "tracked"`. *(Ghi nhận trung thực: lệnh `remove -a ... -g -y` báo `Successfully removed 1 skill(s)` nhưng còn sót 1 thư mục `SKILL.md` trong sandbox — người dùng muốn gỡ sạch global hoàn toàn trên Windows có thể chạy `skills remove vietnamese-human-readable-writing -g -y` không giới hạn `-a` hoặc xóa thư mục thủ công).* |
| **5. Copy thủ công PowerShell lặp lại 2 lần (`idempotent reinstall`)** | Chạy vòng lặp xóa thư mục đích nếu tồn tại rồi `Copy-Item -Recurse -Force` từ `INSTALL.md` **2 lần liên tiếp** cho cả 4 đích Global trong `%TEMP%\viwrite-manual-sandbox` | Cả 4 đích đều đạt `files=5`, `nested=False` (không lồng `vietnamese-human-readable-writing\vietnamese-human-readable-writing\`), `SKILL.md` SHA-256 khớp `77e02eb0...c3911c`. |

---

## 5. Kiểm toán Nguồn Gốc Tài sản & Đề xuất Giấy phép (`MIT License`)

Theo yêu cầu chỉ áp dụng giấy phép khi chủ repository xác nhận, **tệp `LICENSE` cố ý chưa được tạo**. Kết quả kiểm toán quyền sử dụng toàn bộ tệp hiện có trong repository:

| Thành phần trong Repository | Nguồn gốc & Tình trạng Bản quyền | Khả năng áp dụng MIT License |
|---|---|---|
| `skills/vietnamese-human-readable-writing/*` (`SKILL.md` + 4 `references/*.md`) | Tự thiết kế & biên soạn 100% cho dự án; các thuật ngữ chuyên môn chung và tham chiếu tài liệu công khai được diễn giải độc lập, không copy nguyên văn nội dung có bản quyền hạn chế. | Sẵn sàng |
| `research/*.md`, `docs/*.md`, `INSTALL.md`, `README*.md`, `examples/*.md` | Tự biên soạn cho dự án; `4` repo tham chiếu (`vercel-labs/skills`, `obra/superpowers`, `tronghongnguyen1012/ponytail`, `cloudflare/security-audit-skill`) đều dùng **MIT License** và dự án chỉ tham khảo cách tổ chức cấu trúc phân phối, không sao chép mã nguồn hay nhận diện thương hiệu. | Sẵn sàng |
| `evaluation/*` (`datasets`, `scripts/*.py`, `results*`, `reports`) | Dữ liệu ca kiểm thử mô phỏng và kịch bản tự viết cho dự án, cùng log benchmark tự sinh trong các vòng R&D. | Sẵn sàng |
| `assets/*.svg` (`logo`, `banner*`, `before-after*`, `benchmark-chart*`) | Đồ họa SVG vector tự tạo mới 100%, chỉ dùng bảng màu tự chọn và font hệ thống (`system-ui`, `Segoe UI`, `Roboto`, `Helvetica`, `Arial`), không nhúng font hay icon thương mại bên thứ ba. | Sẵn sàng |
| `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/`, `.cursor-plugin/`, `.antigravity-plugin/` | Manifest JSON tự viết theo đặc tả cấu trúc công khai của từng nền tảng. | Sẵn sàng |

**Đề xuất cho chủ repository:** **MIT License** phù hợp nhất vì toàn bộ tài sản đều là nội dung tự biên soạn, tương thích đồng bộ với cả 4 repository tham chiếu và giữ rào cản thấp nhất cho người cài đặt vào IDE/CI nội bộ. Sau khi chủ repository xác nhận, chỉ cần tạo tệp `LICENSE` ở gốc repo (năm bản quyền + tên chủ sở hữu) và bổ sung `"license": "MIT"` vào các manifest tương ứng nếu muốn.
