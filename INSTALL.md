# Hướng dẫn Cài đặt, Cập nhật & Gỡ bỏ (`INSTALL.md`)

Tài liệu hướng dẫn chi tiết 3 cách cài đặt Skill **`vietnamese-human-readable-writing`** (bản phát hành `v4.1.0-beta`, tên thương hiệu đề xuất: **ViWrite**) trên Windows và macOS/Linux.

---

## Cách 1: Cài nhanh qua Skills CLI (`skills.sh`) — Khuyên dùng

Yêu cầu: **Node.js ≥ 22.20** (đã kiểm thử thực tế trên Windows 11 với Node `v24.18.0`).

> [!NOTE]
> **Mẹo quan trọng trên Windows PowerShell:** Nếu PowerShell chặn chạy `npx` với lỗi `npx.ps1 cannot be loaded because running scripts is disabled`, hãy dùng **`npx.cmd`** thay cho `npx`. Khi máy Windows chưa bật Developer Mode để tạo symlink, thêm cờ **`--copy`** để sao chép file trực tiếp.

### 1. Xem trước và cài đặt

```powershell
# Kiểm tra danh sách skill tìm thấy từ GitHub (không cài)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --list

# Cài cho dự án hiện tại (mặc định tạo trong .agents/skills/ hoặc thư mục agent tương ứng)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --copy

# Cài toàn cục (Global - dùng cho mọi dự án trên máy)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing -g --copy

# Ghim đúng tag phát hành Beta (khuyến nghị khi chia sẻ cho team)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing@v4.1.0-beta --skill vietnamese-human-readable-writing -g --copy -y
```

### 2. Chọn AI IDE / Agent cụ thể (`--agent`)

| Agent | Cờ `--agent` | Thư mục Project-local | Thư mục Global |
|---|---|---|---|
| **Antigravity IDE / CLI** | `-a antigravity` | `.agents/skills/` | `~/.gemini/config/skills/` |
| **Claude Code / Desktop** | `-a claude-code` | `.claude/skills/` | `~/.claude/skills/` |
| **OpenAI Codex (CLI / App)** | `-a codex` | `.agents/skills/` | `~/.agents/skills/` |
| **Cursor** | `-a cursor` | `.agents/skills/` | `~/.cursor/skills/` |
| **Tất cả agent đã phát hiện** | `-a *` | Theo từng agent | Theo từng agent |

Ví dụ cài cùng lúc cho cả Antigravity, Claude Code, Codex và Cursor vào thư mục dự án:

```powershell
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a antigravity claude-code codex cursor --copy -y
```

### 3. Liệt kê, Cập nhật và Gỡ bỏ

```powershell
# Liệt kê skill đã cài trong dự án hiện tại (thêm -g để xem danh sách global)
npx.cmd --yes skills list
npx.cmd --yes skills list -g

# Cập nhật phiên bản mới nhất (bỏ -g nếu chỉ cập nhật cho dự án)
npx.cmd --yes skills update -g -y

# Gỡ bỏ skill khỏi dự án hoặc global
npx.cmd --yes skills remove vietnamese-human-readable-writing -y
npx.cmd --yes skills remove vietnamese-human-readable-writing -g -y
```

*(Tham khảo thêm nhật ký smoke test từng lệnh trên Windows tại [docs/compatibility-and-smoke-test.md](./docs/compatibility-and-smoke-test.md).)*

---

## Cách 2: Plugin Manifest Cấp Repository

Repository đã đính kèm các manifest tối giản (không chứa `hooks`, không cài `MCP Server`) để hỗ trợ nạp trực tiếp dưới dạng plugin từ GitHub URL/repository:
- **Claude Code:** Hỗ trợ `.claude-plugin/marketplace.json` và `.claude-plugin/plugin.json` (cài từ repo bằng `/plugin marketplace add tronghongnguyen1012/vietnamese-human-readable-writing` trong Claude Code nếu bật plugin repository).
- **Codex:** Có sẵn `.codex-plugin/plugin.json` và `.agents/plugins/marketplace.json` trỏ tới `./skills/`.
- **Cursor / Antigravity:** Có sẵn `.cursor-plugin/plugin.json` và `.antigravity-plugin/plugin.json`.

> **Lưu ý trung thực:** Skill hiện **chưa được xuất bản lên các curated marketplace chính thức** của Anthropic, OpenAI Codex, Cursor hay Antigravity. Trên các nền tảng chưa kiểm chứng live plugin loader, nên dùng **Cách 1 (`skills.sh`)** hoặc **Cách 3 (Copy thủ công)** bên dưới để bảo đảm ổn định.

---

## Cách 3: Cài Thủ công (Fallback Không Cần Node.js)

Clone repository và **chỉ copy thư mục `skills/vietnamese-human-readable-writing/`** (tên thư mục đích bắt buộc là `vietnamese-human-readable-writing` khớp với trường `name` trong `SKILL.md`).

### Windows PowerShell

```powershell
git clone https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing.git
cd vietnamese-human-readable-writing
$src = ".\skills\vietnamese-human-readable-writing"

# Antigravity (Global)
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.gemini\config\skills" | Out-Null
Copy-Item -Recurse -Force $src "$env:USERPROFILE\.gemini\config\skills\vietnamese-human-readable-writing"

# Claude Code (Global)
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse -Force $src "$env:USERPROFILE\.claude\skills\vietnamese-human-readable-writing"

# OpenAI Codex (Global — hỗ trợ cả .agents\skills và .codex\skills)
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force $src "$env:USERPROFILE\.codex\skills\vietnamese-human-readable-writing"

# Cursor (Project hoặc Global)
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills" | Out-Null
Copy-Item -Recurse -Force $src "$env:USERPROFILE\.cursor\skills\vietnamese-human-readable-writing"
```

*(Nếu cài Project-local, copy vào `<project-root>\.agents\skills\vietnamese-human-readable-writing\` cho Antigravity/Codex/Cursor hoặc `<project-root>\.claude\skills\vietnamese-human-readable-writing\` cho Claude Code.)*

### macOS / Linux

```bash
git clone https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing.git
cd vietnamese-human-readable-writing
SRC="./skills/vietnamese-human-readable-writing"

# Antigravity (Global)
mkdir -p ~/.gemini/config/skills && cp -R "$SRC" ~/.gemini/config/skills/

# Claude Code (Global)
mkdir -p ~/.claude/skills && cp -R "$SRC" ~/.claude/skills/

# OpenAI Codex (Global)
mkdir -p ~/.agents/skills && cp -R "$SRC" ~/.agents/skills/

# Cursor (Global)
mkdir -p ~/.cursor/skills && cp -R "$SRC" ~/.cursor/skills/
```

---

## Kiểm tra Sau khi Cài đặt

1. **Đủ đúng 5 tệp trong thư mục đích** (không copy nhầm `research/` hay `evaluation/`):
   ```text
   vietnamese-human-readable-writing/
   ├── SKILL.md
   └── references/
       ├── business-specs.md
       ├── information-architecture.md
       ├── technical-specs.md
       └── vietnamese-clarity-and-style.md
   ```
2. **Mở một phiên làm việc mới** trên IDE/CLI để runtime nạp lại danh sách skill.
3. **Xác nhận Discovery:** Gõ `/skills` trong Codex hoặc Claude Code (hoặc kiểm tra danh sách available skills trong Antigravity) và thấy `vietnamese-human-readable-writing`.
4. **Kiểm tra kích hoạt thực tế (2 câu thử nhanh):**
   - *Nên kích hoạt:* *"Biên tập câu Business Rule sau cho rõ nghĩa hơn mà không tự thêm dữ kiện: Sau 3 lần vi phạm liên tiếp, thực hiện khóa tạm thời tài khoản và gửi thông báo cho quản trị viên."* → Skill kích hoạt sẽ tách phần đã biết và chỉ rõ các điểm khuyết (`thời hạn khóa`, `kênh gửi thông báo`) thay vì tự đoán bừa.
   - *Không nên kích hoạt:* *"Write a Python pytest unit test for binary search"* → Câu lệnh code tiếng Anh thuần không bị Skill can thiệp.
