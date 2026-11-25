<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" alt="ViWrite — AI viết. Con người hiểu." width="840">
  </picture>
</p>

<p align="center">
  <strong>AI viết. Con người hiểu.</strong> — <em>AI writes. Humans understand.</em>
</p>

<p align="center">
  <a href="https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/releases/tag/v4.2.0-beta"><img src="https://img.shields.io/badge/release-v4.2.0--beta-0F766E?style=flat-square" alt="Release v4.2.0-beta"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/spec-agentskills.io-1E293B?style=flat-square" alt="Agent Skills Spec"></a>
  <a href="https://skills.sh"><img src="https://img.shields.io/badge/CLI-skills.sh-0D9488?style=flat-square" alt="skills.sh"></a>
  <img src="https://img.shields.io/badge/skill_id-vietnamese--human--readable--writing-334155?style=flat-square" alt="Skill ID">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-0F766E?style=flat-square" alt="MIT License"></a>
</p>

<p align="center">
  <strong>Tiếng Việt</strong> · <a href="./README.en.md">English</a> · <a href="./INSTALL.md">Cài đặt chi tiết</a> · <a href="./examples/README.md">Ví dụ thực tế</a> · <a href="./docs/compatibility-and-smoke-test.md">Kiểm thử &amp; Tương thích</a>
</p>

---

**ViWrite** (tên gói cài đặt: [`vietnamese-human-readable-writing`](./skills/vietnamese-human-readable-writing/SKILL.md)) là một bộ quy tắc cài trực tiếp vào AI Coding Agent (Antigravity, Claude Code, Codex, Cursor). Sau khi cài, AI vẫn giữ nguyên thuật ngữ và logic kỹ thuật, nhưng viết tiếng Việt tự nhiên, đi thẳng vào việc cần làm và biết hỏi lại khi đề bài thiếu dữ kiện thay vì tự đoán bù.

---

## Vì sao cần ViWrite?

Khi nhờ AI viết tài liệu hay trả lời bằng tiếng Việt, bạn thường gặp cảnh **mình hiểu rõ chuyên môn, đọc không vướng thuật ngữ nào, nhưng vẫn phải đọc lại 2–3 lần mới hiểu AI đang nói gì**:

1. **Câu viết theo kiểu dịch từ tiếng Anh:** Dồn hết điều kiện và ngoại lệ vào một câu dài 80–100 chữ, lặp nhiều cụm trang trọng rỗng (*"thực hiện việc..."*, *"tiến hành..."*, *"nhằm đảm bảo..."*).
2. **Giấu ý chính xuống cuối bài:** Tin nhắn hay báo cáo mở đầu bằng vài dòng rào đón chung chung, khiến đồng nghiệp phải đọc hết mới thấy quyết định hoặc phần việc của mình.
3. **Tự điền cho mượt khi đề bài còn thiếu ý:** Khi bạn đưa một câu yêu cầu còn bỏ ngỏ con số, đối tượng áp dụng hay trường hợp ngoại lệ, AI dễ tự viết thêm quy tắc cho câu nghe trôi chảy. Nếu không để ý, người đọc sẽ tưởng những chi tiết tự thêm đó đã được chốt.

### Khác gì với các công cụ chỉnh giọng văn (Humanizer)?

Các công cụ chỉnh văn phong thường tập trung làm câu chữ trôi chảy hơn hoặc tự nhiên hơn trong giao tiếp. Với tài liệu kỹ thuật và sản phẩm, **nghe mượt chưa đủ — người đọc cần hiểu đúng để bắt tay vào làm ngay**.

| Khía cạnh | Công cụ chỉnh văn phong thông thường | ViWrite |
|---|---|---|
| **Mục tiêu chính** | Làm câu chữ tự nhiên, bớt sượng. | Giúp người đọc **hiểu đúng ngay lần đọc đầu** và dùng được ngay cho công việc. |
| **Cách sắp xếp ý** | Thường chỉ sửa từng câu hoặc từng đoạn. | Đảo ý quan trọng lên đầu (tin nhắn, báo cáo) hoặc tách nhánh điều kiện–ngoại lệ rõ ràng (spec). |
| **Giữ chi tiết kỹ thuật** | Dễ vô tình làm mờ ranh giới số (`>` hay `>=`), toán tử `và/hoặc` hoặc ngoại lệ. | Giữ nguyên thông số, điều kiện, API contract và đối chiếu nhất quán giữa chữ, bảng và sơ đồ. |
| **Khi đầu vào thiếu dữ kiện** | Tùy công cụ; đôi khi đoán thêm để câu nghe liền mạch. | Tách rõ phần đã chắc chắn khỏi danh sách điểm cần chốt, **không tự bịa** chi tiết ngoài nguồn. |

---

## AI thay đổi gì sau khi cài?

*(Các trích đoạn `TEST-23` và `H2-10` dưới đây lấy nguyên văn từ kết quả chạy thử đã lưu; ví dụ gọt câu ngắn ngay bên dưới chỉ dùng để minh họa cách viết.)*

### 1. Gọn ý, tự nhiên nhưng không rơi thông số (`TEST-23`)

Trích nguyên văn từ [held-out-test.jsonl](./evaluation/held-out-test.jsonl) và bản chạy `Skill v4` trong [regression-v4-raw.jsonl](./evaluation/results-v2/regression-v4-raw.jsonl):

- **Đầu vào gốc (câu ghép 108 chữ, dịch sát tiếng Anh):**
  > *"Cơ chế tự động mở rộng theo chiều ngang (HPA) được cấu hình để kích hoạt việc tăng số lượng pod khi mức sử dụng CPU trung bình vượt qua ngưỡng 75% được duy trì trong một cửa sổ thời gian là 3 phút. Tuy nhiên, việc thu hẹp quy mô (scale-in) bị trì hoãn bởi một khoảng thời gian ổn định mặc định là 5 phút nhằm ngăn chặn sự dao động liên tục của các pod (flapping), và số lượng bản sao không bao giờ được giảm xuống dưới mức tối thiểu là 2 hoặc vượt quá mức tối đa là 12."*
- **Sau khi dùng ViWrite (`Skill v4` nguyên văn — tách 3 câu chủ động, giữ nguyên `75%`, `3 phút`, `5 phút`, `2`, `12`):**
  > *"HPA (cơ chế tự động mở rộng theo chiều ngang) được cấu hình để tăng số lượng pod khi mức sử dụng CPU trung bình vượt ngưỡng 75% và duy trì trong 3 phút. Tuy nhiên, HPA trì hoãn quá trình thu hẹp quy mô (scale-in) theo khoảng thời gian ổn định mặc định 5 phút nhằm ngăn tình trạng pod dao động liên tục (flapping). Ngoài ra, số lượng bản sao không bao giờ giảm xuống dưới mức tối thiểu 2 và không vượt quá mức tối đa 12."*

*(Ví dụ minh họa ngắn ngoài bộ kiểm thử: thay vì viết "Hệ thống tiến hành việc thực hiện gửi thông báo đến người dùng sau khi có sự hoàn tất của giao dịch", AI viết thẳng "Hệ thống gửi thông báo cho người dùng sau khi giao dịch hoàn tất.")*

### 2. Giữ trung thực khi yêu cầu còn thiếu tham số (`H2-10`)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/before-after-dark.svg">
    <img src="assets/before-after.svg" alt="So sánh nguyên văn ca H2-10" width="840">
  </picture>
</p>

Xem đủ 5 ca đối chiếu nguyên văn (hội thoại tự nhiên, tin nhắn Teams, Business Rule đa nghĩa, RFC PostgreSQL + Mermaid và ca `H2-10`) tại **[examples/](./examples/README.md)**.

---

## Khi nào nên dùng?

- **Nên dùng:** Trò chuyện tiếng Việt hằng ngày; giải thích kiến thức và đánh đổi kiến trúc; nhắn tin Slack/Teams/Email công việc; viết PRD, BRD, User Story, Acceptance Criteria, Business Rule; soạn IDD, SAD, API Spec, RFC, Runbook; biên tập tài liệu tiếng Việt dịch sát tiếng Anh.
- **Không dùng:** Yêu cầu chỉ viết code, giải toán thuần túy, hoặc hội thoại hoàn toàn bằng ngôn ngữ khác tiếng Việt.

---

## Cài đặt nhanh

> **Khuyên dùng:** Cài qua [Skills CLI (`skills.sh`)](https://skills.sh) vì đã chạy thử thành công trên Windows. Các gói native plugin đi kèm trong repo đang ở trạng thái **`experimental`** do chưa kiểm chứng trực tiếp trên ứng dụng thật của từng hãng. Xem hướng dẫn đầy đủ, cập nhật, gỡ bỏ và copy thủ công tại **[INSTALL.md](./INSTALL.md)**.

```bash
# macOS / Linux (chọn agent tương tác)
npx skills add tronghongnguyen1012/vietnamese-human-readable-writing
```

Trên **Windows PowerShell** (dùng `npx.cmd` nếu bị chặn `npx.ps1`, thêm `--copy` nếu chưa bật Developer Mode):

```powershell
# Cài cho dự án hiện tại
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --copy -y

# Cài toàn cục (Global — dùng cho mọi dự án)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing -g --copy -y

# Cập nhật riêng dự án (-p) hoặc toàn cục (-g)
npx.cmd --yes skills update -p -y
npx.cmd --yes skills update -g -y
```

### Tóm tắt theo từng AI IDE / CLI

| Nền tảng | Lệnh khuyên dùng (`skills.sh`) | Thư mục lưu Skill | Native Plugin (`experimental` — chưa test live) |
|---|---|---|---|
| **Claude Code / Desktop** | Thêm `-a claude-code` | `.claude/skills/` · `~/.claude/skills/` | `/plugin marketplace add tronghongnguyen1012/vietnamese-human-readable-writing` → `/plugin install vietnamese-human-readable-writing@vietnamese-human-readable-writing` |
| **OpenAI Codex (CLI / App / IDE)** | Thêm `-a codex` | `.agents/skills/` · `~/.agents/skills/` | Mở repo trong Codex và chọn plugin qua `/plugins` (`.codex-plugin/`, `.agents/plugins/marketplace.json`) |
| **Antigravity (IDE / App / CLI)** | Thêm `-a antigravity` | `.agents/skills/` · `~/.gemini/config/skills/` | `agy plugin install https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing` |
| **Cursor** | Thêm `-a cursor` | `.agents/skills/` · `~/.cursor/skills/` | Có sẵn [`.cursor-plugin/plugin.json`](./.cursor-plugin/plugin.json) |

---

## Đã kiểm chứng tới đâu?

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/benchmark-chart-dark.svg">
    <img src="assets/benchmark-chart.svg" alt="Kết quả Kiểm thử — ViWrite" width="840">
  </picture>
</p>

- **Kết quả chấm mù tự động (lịch sử `v4` / `v4.1.0-beta`):** Trên 24 tình huống mới ([held-out-v2.jsonl](./evaluation/held-out-v2.jsonl), sinh bằng `flash`, chấm chéo 2 lượt bởi `pro`), `Skill v4` thắng **`20/24 (83,3%)`** trước AI mặc định (`0/24` vs `8/24` lỗi nghiêm trọng) và thắng **`17/24 (70,8%)`** trước prompt 6 quy tắc (`1/24*` vs `8/24` lỗi nghiêm trọng). Bản vá **`v4.1.0-beta`** đạt **`0/9` lỗi nghiêm trọng** trên 9 ca hồi quy tập trung.
- **Cập nhật & Kiểm chứng Native ở `v4.2.0-beta` ([chi tiết báo cáo](./evaluation/v4.2-rc/native-validation-report.md)):** Tinh chỉnh quy trình viết trên nền `v4.1` (tách 5 chế độ tác vụ để không lộ danh sách điểm thiếu vào thông báo/email cho người đọc cuối, cho phép tái cấu trúc theo nghĩa và trình tự linh hoạt hơn, siết kiểm tra `có thể`/`sẽ`, phạm vi áp dụng và thuật ngữ nghiệp vụ). Smoke test native trên Antigravity xác nhận override project-local `.agents/skills/` nạp đúng `SKILL.md` v4.2 và không kích hoạt nhầm với `pytest`. Trên 7 ca đối chứng tập trung (`Gemini 4 Neon`), `v4.2` đạt **`7/7` Gate 0 PASS** (`0` Critical/Major, `1` Minor ở ca mới `NV-06`) so với `6/6` `v4.1 native` (`1` Minor / thiếu `2` mục bảo toàn trạng thái chưa chốt ở `NV-04`).
- **Những gì đã kiểm chứng về cài đặt:** Đã xác minh manifest/schema, chạy thành công `skills.sh` trên Windows (tìm thấy đúng 1 skill, cài project-local, cài global cô lập, cập nhật `-p` và copy thủ công lặp lại không bị lồng thư mục). Đánh giá chất lượng diện rộng `v4`/`v4.1` chạy qua subagent; smoke test `v4.2` đã xác minh native workspace override trên Antigravity.
- **Giới hạn & Minh bạch dữ liệu:** Các vòng thử nghiệm dẫn tới `v4.2.0-beta` chỉ mang tính **định hướng thiết kế** trên mẫu nhỏ (`7` ca đối chứng + [nhật ký chấm mù 1 người dùng](./evaluation/v4.2-rc/human-evaluation-log.md)), **không phải bằng chứng thống kê** rằng `v4.2.0-beta` vượt trội tuyệt đối; trong môi trường Antigravity vẫn cài global `v4.1` nên chưa tách được một baseline Gemini 0-skill thuần túy ([đính chính log thí nghiệm cũ](./evaluation/v4.2-rc/prior-experiments-errata.md)). Ngoài Antigravity, chưa chạy thử live trên **Claude Code, Codex, Cursor** hay binary `agy` CLI độc lập; chưa đo tốc độ đọc hiểu thực tế (*Time to Correct Understanding*) trên nhóm người đọc Việt Nam độc lập ([quy trình dự kiến](./evaluation/human-eval-protocol.md)). Xem bảng 6 tầng tại **[docs/compatibility-and-smoke-test.md](./docs/compatibility-and-smoke-test.md)**.

---

## Tài liệu Chi tiết & Giấy phép

- **Cài đặt & Ví dụ:** [INSTALL.md](./INSTALL.md) · [examples/README.md](./examples/README.md) · [CHANGELOG.md](./CHANGELOG.md)
- **Bộ Skill cài đặt:** [`skills/vietnamese-human-readable-writing/SKILL.md`](./skills/vietnamese-human-readable-writing/SKILL.md) (91 dòng) và [`references/`](./skills/vietnamese-human-readable-writing/references/)
- **Nghiên cứu & Kiểm thử:** [docs/compatibility-and-smoke-test.md](./docs/compatibility-and-smoke-test.md) · [docs/DESIGN_DECISIONS.md](./docs/DESIGN_DECISIONS.md) · [docs/REVIEW-FINDINGS.md](./docs/REVIEW-FINDINGS.md) · [research/research-report.md](./research/research-report.md) · [evaluation/v4.1-stabilization-report.md](./evaluation/v4.1-stabilization-report.md) · [evaluation/v4.2-rc/native-validation-report.md](./evaluation/v4.2-rc/native-validation-report.md) · Archive tags: [`archive/experiment-semantic-reconstruction`](https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/tree/archive/experiment-semantic-reconstruction) & [`archive/experiment-v5-communication-first`](https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/tree/archive/experiment-v5-communication-first)
- **Giấy phép:** Phân phối theo **[MIT License](./LICENSE)** (`Copyright (c) 2026 Trong Nguyen (tronghongnguyen1012)`).
- **Báo lỗi / Góp ý:** Mở [GitHub Issues](https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/issues) kèm câu hỏi gốc và đoạn trả lời gặp lỗi.
