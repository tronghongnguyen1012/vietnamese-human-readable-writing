# Hướng dẫn Cài thử `ViWrite v4.2-rc` trên Antigravity & Rollback về `v4.1.0-beta`

> **Cập nhật phát hành:** Phiên bản RC này đã được nghiệm thu, merge vào `main` và phát hành dưới tag **`v4.2.0-beta`** (nhánh `release/v4.2-rc` đã được dọn sau khi merge). Với người dùng cài mới hoặc cập nhật bản phát hành chính thức, xem **[INSTALL.md](../../INSTALL.md)**. Tài liệu dưới đây được giữ lại làm hồ sơ thử nghiệm của giai đoạn RC.

Tài liệu này mô tả quy trình **cài thử nghiệm trong giai đoạn `v4.2-rc`** trên Antigravity và **khôi phục nhanh về bản ổn định `v4.1.0-beta`**. Cấu trúc Skill giữ nguyên 5 tệp chuẩn (`SKILL.md` + `references/*.md`).

---

## Cách 1: Cài thử **Project-local** (Khuyên dùng để test an toàn, không đụng Global `v4.1`)

Theo tài liệu ưu tiên nạp của Antigravity (`Workspace .agents/skills/` đứng **tầng 1**, ghi đè **Global `~/.gemini/config/skills/`** ở tầng 3), bạn có thể đặt `v4.2-rc` vào thư mục dự án test mà vẫn giữ nguyên `v4.1.0-beta` ở global cho các dự án khác:

### Windows PowerShell
```powershell
# Đứng tại thư mục gốc của repo đang checkout nhánh release/v4.2-rc (hoặc trỏ $src về đó)
$src = ".\skills\vietnamese-human-readable-writing"
$dest = ".\.agents\skills\vietnamese-human-readable-writing"

New-Item -ItemType Directory -Force -Path (Split-Path $dest -Parent) | Out-Null
if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
Copy-Item -Recurse -Force $src $dest
```

### Kiểm tra sau khi cài Project-local
1. Mở một **phiên chat mới** trong Antigravity tại workspace đó.
2. Kiểm tra đủ 5 tệp trong `.agents\skills\vietnamese-human-readable-writing\` và xác nhận dòng tiêu đề `# Viết Tiếng Việt Rõ Nghĩa và Khả Dụng (v4.2-rc)` ở đầu `SKILL.md`.
3. Gửi thử một yêu cầu tiếng Việt: trong log công cụ, agent phải đọc `.agents/skills/vietnamese-human-readable-writing/SKILL.md` chứ không đọc từ `~/.gemini/config/skills/...`.

### Rollback Project-local về Global `v4.1.0-beta`
```powershell
Remove-Item -Recurse -Force ".\.agents\skills\vietnamese-human-readable-writing"
```
Mở phiên mới — Antigravity sẽ tự nạp lại bản `v4.1.0-beta` từ `~/.gemini/config/skills/vietnamese-human-readable-writing`.

---

## Cách 2: Cài thử **Global** từ nhánh `release/v4.2-rc`

Chỉ dùng nếu bạn muốn thử `v4.2-rc` trên mọi workspace trên máy:

### Windows PowerShell (Copy trực tiếp từ tag `v4.2.0-beta` hoặc nhánh `main`)
```powershell
git fetch origin --tags
git checkout v4.2.0-beta

$src = ".\skills\vietnamese-human-readable-writing"
$dest = "$env:USERPROFILE\.gemini\config\skills\vietnamese-human-readable-writing"

New-Item -ItemType Directory -Force -Path (Split-Path $dest -Parent) | Out-Null
if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
Copy-Item -Recurse -Force $src $dest
```

### Hoặc qua `skills.sh` từ GitHub tag `v4.2.0-beta`
```powershell
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing@v4.2.0-beta --skill vietnamese-human-readable-writing -a antigravity -g --copy -y
```

### Rollback Global về `v4.1.0-beta`
```powershell
# Cách A: Qua skills.sh ghim đúng tag phát hành chính thức v4.1.0-beta
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing@v4.1.0-beta --skill vietnamese-human-readable-writing -a antigravity -g --copy -y

# Cách B: Thủ công từ nhánh main của repo (nếu không dùng Node.js)
git checkout main
$src = ".\skills\vietnamese-human-readable-writing"
$dest = "$env:USERPROFILE\.gemini\config\skills\vietnamese-human-readable-writing"
if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
Copy-Item -Recurse -Force $src $dest
```

Kiểm tra lại rollback thành công trên PowerShell:
```powershell
(Get-Content "$env:USERPROFILE\.gemini\config\skills\vietnamese-human-readable-writing\SKILL.md" -TotalCount 12) -join "`n"
# Kết quả phải hiển thị: # Viết Tiếng Việt Rõ Nghĩa và Khả Dụng (v4.1)
```
