# Báo cáo Tương thích, Cài đặt Thực tế & Đề xuất Giấy phép (`compatibility-and-smoke-test.md`)

Tài liệu tổng hợp: (1) phân tích 4 repository tham chiếu, (2) ma trận tương thích 4 tầng trên các runtime AI phổ biến, (3) nhật ký smoke test thực tế trên Windows với `skills` CLI (`skills.sh`), và (4) đề xuất giấy phép mã nguồn mở cho chủ repository lựa chọn.

---

## 1. Kết quả Phân tích 4 Repository Tham chiếu

| Repository | Giấy phép | Mô hình trình bày & phân phối áp dụng | Phần chủ động KHÔNG sao chép |
|---|---|---|---|
| `vercel-labs/skills` (`skills.sh`) | MIT | Cấu trúc chuẩn `skills/<name>/SKILL.md` để `npx skills add <owner>/<repo>` quét tự động; hỗ trợ bảng `--agent`, `--copy`, `list`, `update`, `remove`. | Hệ thống monorepo workspace TypeScript phức tạp (`bin/`, `src/`, telemetry). |
| `obra/superpowers` | MIT | Bố cục rõ ràng cho người dùng cuối; tách manifest tối giản cho `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/marketplace.json`, `.cursor-plugin/`, `.antigravity-plugin/`. | Bộ thư viện đa skill lớn, `hooks` tự động inject, logo thương hiệu riêng. |
| `tronghongnguyen1012/ponytail` | MIT | Hero branding gọn (logo + tagline + badge tối giản + banner Dark/Light qua `<picture>`); tách riêng `INSTALL.md` gọn gàng. | Bộ `hooks` / telemetry CSV / script đa IDE (>15 thư mục plugin) không cần thiết cho Writing Skill thuần túy. |
| `cloudflare/security-audit-skill` | MIT | Phong cách giải thích cơ chế theo pha ngắn gọn, trực diện cho kỹ sư; gắn chặt `skills/<name>/SKILL.md` + `LICENSE` ở root. | Cấu trúc đặc thù audit bảo mật đa tác nhân (`coverage-ledger`). |

**Nguyên tắc áp dụng cho `vietnamese-human-readable-writing`:** Giữ trọn gói thực thi gọn nhẹ ở `skills/vietnamese-human-readable-writing/`, không thêm `hooks`, `MCP server`, daemon hay gói npm riêng, chỉ thêm các file manifest JSON tối giản tương thích các plugin/repository loader chính.

---

## 2. Ma trận Tương thích Native 4 Tầng (Phân tách Trung thực)

> **Lưu ý quan trọng:** Skill hiện tại **chưa được nộp hoặc xuất bản trên các curated marketplace chính thức của bên thứ ba** (như Anthropic Official Directory, OpenAI Codex Official Catalog, Cursor Directory hay Antigravity Public Marketplace). Việc cài qua GitHub/CLI hoạt động trực tiếp từ repository này.

| Runtime / Hệ sinh thái | 1. Tương thích định dạng (`Spec`) | 2. Cài đặt thử nghiệm (`Install`) | 3. Nạp danh sách (`Discovery`) | 4. Kích hoạt sinh (`Activation`) | Cơ chế phân phối hiện có |
|---|---|---|---|---|---|
| **Antigravity IDE / CLI** | Đạt (`SKILL.md` 82 dòng + `references/`) + `.antigravity-plugin/plugin.json` | **Đã kiểm thử thực tế trên Windows** (`npx.cmd skills add --copy`) | **Đã xác minh** (`skills add --list` + `skills list --json`) | **Đã kiểm thử toàn bộ Round 2 & v4.1** trên tier `flash` / `pro` | `skills.sh`, `.antigravity-plugin/plugin.json`, copy vào `.agents\skills\` hoặc `%USERPROFILE%\.gemini\config\skills\` |
| **Claude Code & Claude Code Desktop** | Đạt (`SKILL.md` chuẩn YAML + `.claude-plugin/{plugin,marketplace}.json`) | **Đã kiểm thử copy file trên Windows** vào `.claude\skills\` qua `skills` CLI (`SHA-256` khớp 100%) | Chưa kiểm chứng live trong ứng dụng Claude Code CLI/Desktop | **Chưa kiểm chứng trên model Claude** | `skills.sh` (`-a claude-code`), `/plugin marketplace add`, hoặc copy vào `.claude\skills\` |
| **OpenAI Codex CLI, App & IDE Extension** | Đạt (`SKILL.md` + `.codex-plugin/plugin.json` + `.agents/plugins/marketplace.json`) | **Đã kiểm thử copy file trên Windows** vào `.agents\skills\` (`SHA-256` khớp 100%) | Chưa kiểm chứng live trong app Codex / `/skills` | **Chưa kiểm chứng trên model GPT/Codex** | `skills.sh` (`-a codex`), `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, hoặc copy vào `.codex\skills\` |
| **Cursor** | Đạt (`SKILL.md` + `.cursor-plugin/plugin.json`) | **Đã kiểm thử copy file trên Windows** vào `.agents\skills\` (`SHA-256` khớp 100%) | Chưa kiểm chứng live trong Cursor IDE | **Chưa kiểm chứng live trong Cursor** | `skills.sh` (`-a cursor`), `.cursor-plugin/plugin.json`, copy vào `.agents\skills\` |
| **Agent Skills CLI (`skills.sh`)** | Đạt (quét 1 skill duy nhất ở `skills/`, không trùng lặp khi có plugin manifest) | **Đã kiểm thử đầy đủ** (cài mới, cài lại, `list`, `update`, `remove`) | **Đã kiểm thử cả local lẫn GitHub remote** | Tùy runtime đích | `npx skills add tronghongnguyen1012/vietnamese-human-readable-writing` |

---

## 3. Nhật ký Smoke Test Thực tế trên Windows

- **Môi trường test:** Windows 11, Node `v24.18.0`, `npx.cmd` (`11.16.0`), thư mục cô lập `%TEMP%\viwrite-smoke-test` (đã dọn sạch sau khi test, không đụng cấu hình toàn cục của người dùng).
- **Phát hiện môi trường Windows thực tế:** Khi `PowerShell ExecutionPolicy` mặc định chặn chạy `npx.ps1` (`PSSecurityException`), dùng **`npx.cmd`** chạy trơn tru 100%.

| Bước kiểm tra | Lệnh thực thi (`%TEMP%\viwrite-smoke-test`) | Kết quả thực tế |
|---|---|---|
| **1. Discovery từ GitHub remote** | `npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --list` | Exit `0` · Tìm thấy `1 skill`: `vietnamese-human-readable-writing` |
| **2. Discovery từ repo local (sau khi thêm 6 plugin manifest)** | `npx.cmd --yes skills add . --list` | Exit `0` · Tìm thấy đúng `1 skill` (xác nhận không bị trùng lặp do `.claude-plugin/marketplace.json`) |
| **3. Cài project-local đa agent (`--copy`)** | `npx.cmd --yes skills add <repo> --skill vietnamese-human-readable-writing -a antigravity claude-code codex cursor --copy -y` | Exit `0` · Tạo đủ `.agents\skills\vietnamese-human-readable-writing\` và `.claude\skills\vietnamese-human-readable-writing\` |
| **4. Đối chiếu SHA-256 trọn gói 5 file** | `Get-FileHash -Algorithm SHA256` trên cả 10 file đã copy ở 2 thư mục | **Khớp 100%** với `v4.1.0-beta`: `SKILL.md` (`77e02eb...`), `business-specs.md` (`3190ce2...`), `information-architecture.md` (`d57d2fe...`), `technical-specs.md` (`056a22e...`), `vietnamese-clarity-and-style.md` (`1c7972f...`) |
| **5. Liệt kê (`list`) & Cài lại idempotent** | `npx.cmd --yes skills list --json` · chạy lại lệnh `add ... --copy -y` | Exit `0` · Báo `status: "tracked"`; cài lại hiển thị `overwrites: Antigravity, Claude Code`, exit `0` |
| **6. Gỡ bỏ (`remove`)** | `npx.cmd --yes skills remove vietnamese-human-readable-writing -y` | Exit `0` · Xóa sạch cả `.agents\skills\...` và `.claude\skills\...` (giữ `skills-lock.json` ở project root) |
| **7. Cài từ GitHub remote & Kiểm tra `update`** | `npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a antigravity --copy -y` → `npx.cmd --yes skills update -p -y` → `remove -y` | Exit `0` cả 3 bước · `update -p -y` kiểm tra remote và báo `✓ All project skills are up to date` |

---

## 4. Đề xuất Giấy phép Mã nguồn mở (`LICENSE` Proposal)

Kiểm tra tại nhánh hiện tại: **repository hiện chưa có tệp `LICENSE`**. Theo chuẩn pháp lý mã nguồn mở và yêu cầu chủ động không tự ý quyết định thay chủ sở hữu, dưới đây là 3 phương án đề xuất để chủ repository xem xét chọn khi tạo tệp `LICENSE`:

| Giấy phép | Điểm mạnh | Hạn chế cần cân nhắc | Mức khuyến nghị |
|---|---|---|---|
| **MIT License** | Cực kỳ ngắn gọn; cho phép cá nhân/doanh nghiệp cài đặt vào IDE nội bộ, fork, sửa và dùng thương mại với rào cản pháp lý thấp nhất; **khớp cả 4/4 repo tham chiếu** (`ponytail`, `superpowers`, `security-audit-skill`, `skills.sh`). | Không có điều khoản cấp quyền bằng sáng chế tường minh như Apache-2.0. | **Khuyên dùng (Phù hợp nhất cho Agent Skill)** |
| **Apache-2.0** | Bảo vệ mạnh hơn về bằng sáng chế (*explicit patent grant*) và bắt buộc giữ thông báo sửa đổi khi phân phối lại. | Dài và nặng tính pháp lý hơn mức cần thiết cho bộ prompt/markdown nhỏ. | Tốt nếu dự án nhắm tới chuẩn doanh nghiệp lớn |
| **CC-BY-4.0** | Phù hợp cho tài liệu nghiên cứu/báo cáo văn bản thuần túy. | Không khuyến nghị dùng chung cho mã nguồn (`evaluation/scripts/*.py`, JSON manifests) vì quy định tương thích phần mềm kém thuận tiện. | Chỉ nên cân nhắc riêng cho thư mục `research/` |

*Khi chủ repository chốt giấy phép (ví dụ MIT), chỉ cần thêm tệp `LICENSE` ở gốc repo và điền trường `"license"` tương ứng vào các tệp `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`.*
