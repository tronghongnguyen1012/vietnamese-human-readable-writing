# Hướng dẫn Cài đặt, Cập nhật & Gỡ bỏ (`INSTALL.md`)

Hướng dẫn chi tiết cài đặt **ViWrite** (Skill ID: `vietnamese-human-readable-writing`, bản phát hành **`v4.2.0-beta`**) theo từng runtime, không dùng custom installer, hook hay dịch vụ nền.

> **Phương thức khuyến nghị trên mọi runtime:** Dùng **Universal Skills CLI (`skills.sh`)** — đã kiểm thử thực tế trên Windows (cả project-local lẫn sandbox global `-g`). Các cách nạp **Native Plugin** bên dưới đang đánh dấu **`experimental`** vì máy kiểm thử chưa cài sẵn CLI/app gốc của từng hãng để xác minh live.

---

## 1. Universal Skills CLI (`skills.sh`) — Khuyến nghị

Yêu cầu **Node.js ≥ 22.20** (đã test trên Windows 11 với Node `v24.18.0`, `npx.cmd` `11.16.0`).

> [!NOTE]
> Trên **Windows PowerShell**, nếu hệ thống chặn `npx.ps1` (`PSSecurityException`), chạy **`npx.cmd`** thay cho `npx`. Khi máy Windows chưa bật Developer Mode để tạo symlink, thêm **`--copy`** để copy file trực tiếp.

### Xem trước & Cài đặt

```powershell
# Kiểm tra skill tìm thấy từ GitHub (không ghi file)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --list

# Cài Project-local (chia sẻ theo repo dự án)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --copy -y

# Cài Global (dùng cho mọi dự án của bạn)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing -g --copy -y

# Ghim đúng tag phát hành Beta hiện tại (v4.2.0-beta)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing@v4.2.0-beta --skill vietnamese-human-readable-writing -g --copy -y

# Cài một lúc cho cả Antigravity, Claude Code, Codex và Cursor (Project-local)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a antigravity claude-code codex cursor --copy -y
```

### Liệt kê, Cập nhật lên `v4.2.0-beta`, Rollback về `v4.1.0-beta` & Gỡ bỏ

```powershell
# Liệt kê skill đã cài (project-local và global)
npx.cmd --yes skills list
npx.cmd --yes skills list -g

# Cập nhật bản đã cài lên mới nhất (Project-local -p hoặc Global -g)
npx.cmd --yes skills update -p -y
npx.cmd --yes skills update -g -y

# Hoặc cài đè ghim đúng bản v4.2.0-beta (Global Antigravity)
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing@v4.2.0-beta --skill vietnamese-human-readable-writing -a antigravity -g --copy -y

# Rollback về bản ổn định trước đó (v4.1.0-beta) qua skills.sh
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing@v4.1.0-beta --skill vietnamese-human-readable-writing -a antigravity -g --copy -y

# Gỡ bỏ hoàn toàn khỏi Project-local hoặc Global
npx.cmd --yes skills remove vietnamese-human-readable-writing -y
npx.cmd --yes skills remove vietnamese-human-readable-writing -g -y
```

*(Nếu rollback **thủ công** không dùng Node.js: clone/checkout đúng tag `git checkout v4.1.0-beta`, xóa thư mục đích rồi copy lại `.\skills\vietnamese-human-readable-writing`; kiểm tra dòng tiêu đề đầu `SKILL.md` hiển thị `# Viết Tiếng Việt Rõ Nghĩa và Khả Dụng (v4.1)`.)*

---

## 2. Claude Code & Claude Code Desktop

- **Đường dẫn Skill chính thức:**
  - Project-local: `.claude/skills/vietnamese-human-readable-writing/`
  - Global: `~/.claude/skills/vietnamese-human-readable-writing/`

### Cách khuyên dùng (`skills.sh`)
```powershell
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a claude-code --copy -y
# Thêm -g để cài Global:
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a claude-code -g --copy -y
```

### Native Plugin (`experimental` — chưa kiểm chứng live)
Repository đã kèm [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) (khớp SchemaStore) và [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json). Trong phiên tương tác Claude Code, chạy 2 lệnh:
```text
/plugin marketplace add tronghongnguyen1012/vietnamese-human-readable-writing
/plugin install vietnamese-human-readable-writing@vietnamese-human-readable-writing
```
*(Skill chưa phát hành lên danh mục Official Plugins của Anthropic; chỉ mới xác minh manifest & copy file, chưa chạy live trên `claude` CLI/Desktop.)*

---

## 3. OpenAI Codex (CLI, App & IDE Extension)

- **Đường dẫn Skill chính thức theo tài liệu OpenAI Codex:**
  - Project-local: `.agents/skills/vietnamese-human-readable-writing/`
  - Global: `~/.agents/skills/vietnamese-human-readable-writing/`
  - *(Lưu ý: `$CODEX_HOME/skills/` hay `~/.codex/skills/` vẫn tồn tại làm đường dẫn tương thích cho cấu hình Codex cũ, nhưng đường dẫn chuẩn ưu tiên là `.agents/skills/` và `~/.agents/skills/`.)*

### Cách khuyên dùng (`skills.sh`)
```powershell
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a codex --copy -y
# Thêm -g để cài Global:
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a codex -g --copy -y
```

### Native Plugin (`experimental` — chưa kiểm chứng live)
Repository đã kèm [`.codex-plugin/plugin.json`](./.codex-plugin/plugin.json) và [`.agents/plugins/marketplace.json`](./.agents/plugins/marketplace.json) với `"source": { "source": "local", "path": "./" }`. Khi clone hoặc mở repository trong Codex:
1. Đảm bảo thư mục repo chứa `.agents/plugins/marketplace.json` đang mở hoặc có mặt trong cấu hình workspace.
2. Mở bộ quản lý plugin bằng lệnh `/plugins` trong Codex và cài `vietnamese-human-readable-writing` (**ViWrite**).
*(Chưa có `codex` CLI/App trên máy kiểm thử nên luồng `/plugins` mới kiểm chứng ở mức cấu trúc manifest, chưa xác minh runtime loader trực tiếp.)*

---

## 4. Antigravity (IDE, App & CLI)

- **Đường dẫn Skill chính thức:**
  - Project-local: `.agents/skills/vietnamese-human-readable-writing/`
  - Global: `~/.gemini/config/skills/vietnamese-human-readable-writing/`

### Cách khuyên dùng (`skills.sh`)
```powershell
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a antigravity --copy -y
# Thêm -g để cài Global:
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a antigravity -g --copy -y
```

### Native Plugin (`experimental` — chưa kiểm chứng live)
Repository đã kèm [`.antigravity-plugin/plugin.json`](./.antigravity-plugin/plugin.json) (đã kiểm tra khớp schema `https://antigravity.google/schemas/v1/plugin.json`). Theo tài liệu chính thức của Antigravity (`antigravity.google/docs/plugins`):
```bash
agy plugin install https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing
```
*(Chưa có binary `agy` trên máy kiểm thử nên chưa chạy kiểm tra lệnh `agy plugin validate` / `agy plugin install` live.)*

---

## 5. Cursor

- **Đường dẫn Skill chính thức:**
  - Project-local: `.agents/skills/vietnamese-human-readable-writing/`
  - Global: `~/.cursor/skills/vietnamese-human-readable-writing/`

### Cách khuyên dùng (`skills.sh`)
```powershell
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a cursor --copy -y
# Thêm -g để cài Global:
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing --skill vietnamese-human-readable-writing -a cursor -g --copy -y
```

### Native Plugin (`experimental` — chưa kiểm chứng live)
Repository có sẵn [`.cursor-plugin/plugin.json`](./.cursor-plugin/plugin.json) khai báo `"skills": "./skills/"` để nạp từ repo trong phần mở rộng/tùy chỉnh plugin của Cursor (chưa kiểm chứng live trong Cursor IDE).

---

## 6. Cài Thủ công Không Cần Node.js (An toàn khi Cài lại)

Clone repo và **chỉ copy duy nhất thư mục `skills/vietnamese-human-readable-writing/`** (tuyệt đối không copy `research/` hay `evaluation/` vào thư mục Skill).

> [!IMPORTANT]
> Khi cài lại bằng `Copy-Item -Recurse` trên PowerShell nếu thư mục đích đã tồn tại, PowerShell sẽ chép lồng thêm một lớp `...\vietnamese-human-readable-writing\vietnamese-human-readable-writing\`. **Luôn xóa thư mục đích cũ trước khi copy** như đoạn lệnh chuẩn dưới đây.

### Windows PowerShell (Global — chạy cài lại nhiều lần vẫn sạch)

```powershell
git clone https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing.git
cd vietnamese-human-readable-writing
$src = ".\skills\vietnamese-human-readable-writing"

# Giữ hoặc bỏ bớt dòng ứng với các Agent bạn đang dùng:
$targets = @(
    "$env:USERPROFILE\.gemini\config\skills\vietnamese-human-readable-writing", # Antigravity
    "$env:USERPROFILE\.claude\skills\vietnamese-human-readable-writing",        # Claude Code
    "$env:USERPROFILE\.agents\skills\vietnamese-human-readable-writing",        # OpenAI Codex (chuẩn chính thức)
    "$env:USERPROFILE\.cursor\skills\vietnamese-human-readable-writing"         # Cursor
)

foreach ($dest in $targets) {
    New-Item -ItemType Directory -Force -Path (Split-Path $dest -Parent) | Out-Null
    if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
    Copy-Item -Recurse -Force $src $dest
}
```

*(Nếu cài **Project-local** trong thư mục dự án `<project-root>`, đặt `$targets` thành `<project-root>\.agents\skills\vietnamese-human-readable-writing` cho Antigravity/Codex/Cursor và `<project-root>\.claude\skills\vietnamese-human-readable-writing` cho Claude Code.)*

### macOS / Linux

```bash
git clone https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing.git
cd vietnamese-human-readable-writing
SRC="./skills/vietnamese-human-readable-writing"

for DEST in \
  "$HOME/.gemini/config/skills/vietnamese-human-readable-writing" \
  "$HOME/.claude/skills/vietnamese-human-readable-writing" \
  "$HOME/.agents/skills/vietnamese-human-readable-writing" \
  "$HOME/.cursor/skills/vietnamese-human-readable-writing"; do
  mkdir -p "$(dirname "$DEST")"
  rm -rf "$DEST"
  cp -R "$SRC" "$DEST"
done
```

---

## 7. Kiểm tra Sau khi Cài đặt

1. **Đủ đúng 5 tệp trong thư mục đích** (không lồng thư mục, không lẫn file ngoài):
   ```text
   vietnamese-human-readable-writing/
   ├── SKILL.md
   └── references/
       ├── business-specs.md
       ├── information-architecture.md
       ├── technical-specs.md
       └── vietnamese-clarity-and-style.md
   ```
2. **Mở phiên mới** trên IDE/CLI để runtime nạp lại danh sách skill (Level 4 — *Native Runtime Discovery*).
3. **Thử kích hoạt thực tế (2 câu kiểm tra nhanh trên runtime của bạn):**
   - *Nên kích hoạt:* `"Biên tập câu Business Rule sau cho rõ nghĩa hơn mà không tự thêm dữ kiện: Sau 3 lần vi phạm liên tiếp, thực hiện khóa tạm thời trong 24 giờ và gửi cảnh báo."` → Kỳ vọng agent tách phần chắc chắn và chỉ rõ điểm khuyết (`đối tượng bị khóa`, `người nhận cảnh báo`, `cách tính liên tiếp`).
   - *Không nên kích hoạt:* `"Write a Python pytest unit test for binary search"` → Lệnh code tiếng Anh thuần không bị Skill can thiệp.
