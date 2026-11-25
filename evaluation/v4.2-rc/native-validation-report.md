# Báo cáo Kiểm thử Native Activation & Đối chứng Cuối (`ViWrite v4.2-rc`)

Báo cáo này ghi nhận kết quả kiểm thử **native runtime activation** trực tiếp trong môi trường Antigravity (không dùng chiêu tiêm `SKILL.md` vào system prompt) cho bản **`v4.2-rc`** trên nhánh `release/v4.2-rc`, đối chứng cùng **`v4.1` (cài global)** trên cùng model (`gemini-4-hydrogen-high`), cùng subagent trung tính (`v42-native-runner`), cùng cấu hình và cùng bộ prompt nguồn.

- **Dữ liệu đầu vào (7 ca):** [`native-validation-dataset.jsonl`](./native-validation-dataset.jsonl)
- **Kết quả smoke test:** [`smoke-test-results.json`](./smoke-test-results.json)
- **Toàn bộ 14 output nguyên văn + log nạp file + verdict audit:** [`native-validation-outputs.jsonl`](./native-validation-outputs.jsonl)

---

## 1. Native Activation Smoke Test (Xác minh Tách biệt Phiên bản & Điều kiện Kích hoạt)

Thử nghiệm được thực hiện theo 2 giai đoạn, xác minh đường dẫn tuyệt đối của mọi lệnh `read_file` trong `transcript_full.jsonl`:

| Smoke Test | Trạng thái workspace | Prompt kiểm thử | Skill nạp thực tế (xác minh từ log) | Reference nạp thực tế | Kết quả |
|---|---|---|---|---|---|
| **`Smoke1_Pos`** (`v4.1` global) | Không có `.agents/skills/` | Viết lại câu *"Sau 3 lần vi phạm liên tiếp, thực hiện khóa tạm thời trong 24 giờ và gửi cảnh báo."* | `C:\Users\Ztayrong440z\.gemini\config\skills\vietnamese-human-readable-writing\SKILL.md` (`v4.1`) | `...\references\vietnamese-clarity-and-style.md` | **PASS** — Tách phần chắc chắn + chỉ rõ 3 điểm khuyết Trường hợp B. |
| **`Smoke1_Neg`** (`v4.1` global) | Không có `.agents/skills/` | `"Write a Python pytest unit test for binary search"` | **Không nạp** (`all_read_paths: []`) | Không | **PASS** — Không kích hoạt nhầm vào tác vụ code thuần tiếng Anh. |
| **`Smoke2_Pos`** (`v4.2-rc` override) | Có `.agents/skills/vietnamese-human-readable-writing/` (`v4.2-rc`) | Cùng prompt tiếng Việt như `Smoke1_Pos` | `c:\...\Vi Writer\.agents\skills\vietnamese-human-readable-writing\SKILL.md` (`v4.2-rc`) | `...\Vi Writer\.agents\skills\...\vietnamese-clarity-and-style.md` | **PASS** — Antigravity nạp đúng bản project-local `v4.2-rc` (Priority 1), ghi đè sạch bản global `v4.1` (Priority 3). |
| **`Smoke2_Neg`** (`v4.2-rc` override) | Có `.agents/skills/vietnamese-human-readable-writing/` (`v4.2-rc`) | `"Write a Python pytest unit test for binary search"` | **Không nạp** (`all_read_paths: []`) | Không | **PASS** — Không kích hoạt nhầm. |

> *(Lưu ý phụ minh bạch: cả `Smoke1_Pos` lẫn `Smoke2_Pos` đều ghi nhận thêm lời gọi đọc skill built-in `using-superpowers/SKILL.md` của hệ thống trước khi hoàn tất bước đọc skill chuyên môn; ở các ca `NV-01..NV-07-REG`, chúng tôi kiểm tra chính xác trường `viwrite_skill_path` và `viwrite_refs_paths` cho từng lượt.)*

---

## 2. Giới hạn về Nhánh "Gemini không có ViWrite" (0-Skill Baseline)

**Ghi nhận trung thực về môi trường:** Trong phiên kiểm thử này, máy đang cài sẵn `v4.1.0-beta` ở đường dẫn global `C:\Users\Ztayrong440z\.gemini\config\skills\vietnamese-human-readable-writing\`. Theo đặc tả cấu hình của Antigravity (`agy-customizations/docs/json_configs.md`), các luật `exclude` trong `.agents/skills.json` **không thể lọc bỏ skill đã nạp từ môi trường global của người dùng**; đồng thời chúng tôi không chỉnh sửa thư mục `~/.gemini/config/` bên ngoài repo và không giả lập baseline bằng cách tiêm prompt "bỏ qua skill".

Do đó, vòng đối chứng native thực hiện so sánh trực tiếp **hai nhánh native sạch (`v4.1 native` vs `v4.2-rc native`)** và **không báo cáo một baseline 0-skill giả tạo**. Để chạy bổ sung nhánh `Gemini không có ViWrite` độc lập hoàn toàn, chỉ cần tạm di chuyển hoặc gỡ skill global theo hướng dẫn tại [install-and-rollback-v4.2-rc.md](./install-and-rollback-v4.2-rc.md) rồi chạy lại 6 prompt trong `native-validation-dataset.jsonl`.

---

## 3. Kết quả Vòng Đối chứng Cuối (`v4.1 native` vs `v4.2-rc native`)

### 3.1. Bảng Tổng hợp Log Nạp File, Độ dài, Độ trễ & Audit Ngữ nghĩa Độc lập (Layer 1)

| Ca kiểm thử | Vai trò / Nguồn gốc | `v4.1 native` (`words / lat / refs / audit`) | `v4.2-rc native` (`words / lat / refs / audit`) | Ghi chú so sánh |
|---|---|---|---|---|
| **`NV-01`** (`SR-01`) | Thông báo dịch vụ (đối chứng `GPT-6.2`: `277w`) | `359w` / `38.0s` / `[clarity]` / **`PASS (None)`** | `338w` / `37.0s` / `[clarity]` / **`PASS (None)`** | Cả 2 đều sạch, bỏ hoàn toàn phụ lục `"Điểm chưa xác định"`, giữ `"có thể"`. Xem thêm mục hạn chế bên dưới. |
| **`NV-02`** (`V5-03`) | Email PM chốt phương án (re-test lỗi `V5-03 C`) | `347w` / `26.0s` / `[clarity]` / **`PASS (None)`** | `358w` / `29.0s` / `[clarity]` / **`PASS (None)`** | `v4.2-rc` giữ nguyên `"team Sản phẩm và Vận hành"` (không bịa nhãn `"(Sản phẩm)"` cho anh Minh) và không thu hẹp mốc giải đáp. |
| **`NV-03`** (`V5-04`) | Giải thích kỹ thuật `Rate Limiting vs Circuit Breaker` | `703w` / `33.0s` / `[clarity, ia]` / **`PASS (None)`** | `764w` / `37.0s` / `[clarity, ia]` / **`PASS (None)`** | `v4.2-rc` áp dụng tự nhiên trình tự so sánh (bản chất trước → tình huống `15s` → bảng → phối hợp), giữ nguyên độ sâu kỹ thuật. |
| **`NV-04`** (`V5-05`) | Business Rule B2B phức tạp (lỗ hổng ẩn) | `1567w` / `41.0s` / `[business-specs]` / **`PASS (Minor — 2 missing_must_preserve)`** | `2183w` / `56.0s` / `[business-specs]` / **`PASS (None — 0 errors)`** | **`v4.1` chốt cứng theo từng đơn hàng**, bỏ sót câu hỏi *đơn lẻ vs cộng dồn* và mốc *chưa xuất hóa đơn* khỏi Mục 5, đồng thời chèn pseudocode (`ROUND_HALF_UP`). **`v4.2-rc` giữ đủ 100% điểm chưa chốt & sạch hoàn toàn.** |
| **`NV-05`** (`SR-07`) | Quy trình CSKH / Kho / Quản lý ca (re-test lỗi `SR-07 C`) | `606w` / `26.0s` / `[clarity]` / **`PASS (None)`** | `624w` / `43.0s` / `[clarity, ia]` / **`PASS (None)`** | `v4.2-rc` giữ nguyên **`Phiếu giao hàng đi kèm`** (không thu hẹp thành `"Ảnh chụp phiếu giao hàng"`), không lộ phụ lục nội bộ, tách rõ bảng + từng bộ phận. |
| **`NV-06`** *(Unseen mới)* | Quy định **đối soát** cuối ngày đa kênh & sự cố máy POS | `705w` / `38.0s` / `[clarity]` / **`PASS (None)`** | `592w` / `49.0s` / `[clarity, ia]` / **`PASS (Minor)`** | Cả hai giữ chính xác thuật ngữ `"đối soát"`, `"Chờ đối soát"`, tách đúng phạm vi toàn kênh vs POS-only và `"có thể"`. `v4.2-rc` gọn hơn 16%, nhưng đổi `"như"` → `"gồm:"` trước 3 lỗi POS (`Minor`). |
| **`NV-07-REG`** (`V5-06`) | Quy định làm việc từ xa (re-test lỗi `V5-06 C`) | *(Đã chạy ở `V5`: `620w`, xem lưu ý `Group A`)* | `531w` / `126.0s` / `[clarity, ia]` / **`PASS (None)`** | **`v4.2-rc` sửa triệt để lỗi `V5-06 C`**: câu mở đầu ghi *"áp dụng cho toàn thể nhân sự khi làm việc bên ngoài văn phòng"*, không thu hẹp sai thành chỉ trên *"thiết bị cấp phát"*. |

**Xác minh Progressive Disclosure:** Tất cả **`7/7` lượt `v4.2-rc`** và **`6/6` lượt `v4.1`** đều đọc đúng file `SKILL.md` thuộc nhánh tương ứng và mở **`1–2` tệp `references/*.md`** đúng giới hạn `0 → 1 → tối đa 2 file` (không nạp thừa).

---

## 4. Kiểm tra lại Các Lỗi Đã Xác nhận & Các Hạn chế Ngữ nghĩa Còn Tồn tại

### 4.1. Kết quả kiểm tra các lỗi đã xác nhận trước đây (`SR-07`, `V5-03`, `V5-06`) + bài test thuật ngữ `"đối soát"` (`NV-06`)
- **`SR-07` (`NV-05`):** Khắc phục sạch (`v4.2-rc` giữ nguyên `3. Phiếu giao hàng đi kèm`, không thu hẹp thành `"Ảnh chụp phiếu giao hàng"`, và không chèn phụ lục `"Điểm chưa xác định"` vào SOP).
- **`V5-03` (`NV-02`):** Khắc phục sạch (không tự gán `"(Sản phẩm)"` sau `"anh Minh"`, giữ nguyên trách nhiệm phối hợp của CSKH/Vận hành tới khi đối soát khớp sau thứ Ba).
- **`V5-06` (`NV-07-REG`):** Khắc phục sạch (không thu hẹp phạm vi toàn văn bản sang `"trên thiết bị cấp phát"` ở câu dẫn nhập như `V5-06 C`).
- **`NV-06` (Case mới kiểm tra rule bảo toàn thuật ngữ nghiệp vụ):** `v4.2-rc` giữ nguyên vẹn **`đối soát`** và **`Chờ đối soát`** xuyên suốt cả câu dẫn, bảng quy tắc và cảnh báo — không thay máy móc bằng `"kiểm tra"` — đồng thời đặt **Cảnh báo cấm tự điều chỉnh số dư sổ sách** lên trước bảng xử lý.

### 4.2. Báo cáo trung thực lỗi / hạn chế ngữ nghĩa còn tồn tại sau kiểm định
1. **Lỗi `Minor` duy nhất trên `v4.2-rc native` (`NV-06`, Audit `NVAUD-06`):** Ở Mục `2.1`, nguồn ghi *"lỗi phần cứng **như** không đọc được thẻ, kẹt giấy in hóa đơn hoặc mất kết nối mạng"* (dạng ví dụ mở), bản `v4.2-rc` viết *"lỗi phần cứng hoặc kết nối, **gồm:** Không đọc được thẻ; Kẹt giấy in hóa đơn; Mất kết nối mạng."* Đánh giá độc lập xếp mức **`Minor`** vì vẫn giữ cụm bao quát phía trước nhưng chữ *"gồm:"* mang sắc thái liệt kê đóng hơn *"như"*. Không có lỗi `Major` hay `Critical` nào ở cả `7/7` ca `v4.2-rc native`.
2. **Lỗi `Minor` phát hiện trên `v4.1 native` (`NV-04`, Audit `NVAUD-11`):** Khi chạy native trên `v4.1`, ở Mục 1 và mã giả, `v4.1` tự chốt logic tính chiết khấu theo **từng đơn hàng** mà bỏ sót câu hỏi *đơn lẻ vs cộng dồn tháng/quý* khỏi Mục 5 Open Questions, đồng thời thu hẹp trường hợp chuyển tiếp *"chưa xuất hóa đơn"* thành *"duyệt đơn"* (và chèn tên hàm/biến tự đặt như `ROUND_HALF_UP`, `customer_segment`). `v4.2-rc native` khắc phục hoàn toàn cả 2 điểm này (`0` lỗi ở `NV-04`).
3. **Hạn chế văn phong trên `NV-01` (`SR-01` vs `GPT-6.2 Instant`):** Dù `v4.2-rc native` đã bỏ sạch phụ lục `"Điểm chưa xác định"` (`338w`, giữ nguyên `có thể`), trên nền `gemini-4-hydrogen-high` đầu ra vẫn giữ lại nhiều cụm Hán–Việt/hành chính từ bản gốc (như *"chu kỳ chuyển đổi sắp tới"*, *"mô hình xác thực đa tầng có điều kiện"*, *"đối soát định kỳ"*, *"điều kiện tiên quyết"*) thay vì diễn giải đời thường như `GPT-6.2 Instant` (`277w`: *"Trong thời gian tới"*, *"xác thực nhiều lớp"*, *"kiểm tra định kỳ"*). Chúng tôi ghi nhận trung thực hiện tượng này thay vì chỉnh quá tay trên một ca đơn lẻ.

---

## 5. Kết luận cho Vòng Kiểm thử Cuối `v4.2-rc`

- `validate_datasets.py --check-skill` đạt **PASS** (`91` dòng, `12.809` bytes, `0` lỗi cấu trúc/liên kết).
- Smoke Test xác nhận ghi đè **project-local `.agents/skills/`** hoạt động chính xác trên Antigravity và không kích hoạt nhầm trên tác vụ code tiếng Anh.
- Toàn bộ **`7/7` ca `v4.2-rc native`** đạt **`Gate 0 PASS`** (`0` Critical, `0` Major, `6/7` `None`, `1` `Minor`), đồng thời vượt qua sạch cả 3 lỗi hồi quy đã xác nhận (`SR-07`, `V5-03`, `V5-06`), ca `NV-04` (nơi `v4.1 native` bị `2 missing_must_preserve` mức `Minor`), và ca mới chưa từng thấy `NV-06`.
- Đủ điều kiện trình chủ sở hữu **cài thử nghiệm thực tế** theo [install-and-rollback-v4.2-rc.md](./install-and-rollback-v4.2-rc.md) trước khi quyết định có phát hành chính thức hay không.
