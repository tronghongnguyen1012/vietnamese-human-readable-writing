# ViWrite V5 — Communication-First Experiment Report

**Nhánh thực nghiệm:** `experiment/v5-communication-first` (xuất phát từ `experiment/semantic-reconstruction`, commit `275ce12b03ca40299a65eb13166407dd893dd96c`)  
**Trạng thái:** **Prototype Research — CHƯA phát hành, CHƯA merge vào `main`** (đang chờ Independent Review & Human Blind Evaluation từ chủ sở hữu).

---

## 1. Tóm tắt Điều hành (Executive Summary)

Thí nghiệm này kiểm chứng hai hướng thiết kế **ViWrite V5 (Communication-First)** — gồm **V5-A (`E`)** (tái cấu trúc `v4.1` theo 3 bước `Understand → Communicate → Verify`) và **V5-B (`F`)** (viết lại tinh gọn tối đa từ nguyên lý gốc) — đối chứng với **`v4.1` (`B`)**, **`v4.1 + Semantic Reconstruction` (`C`)**, **`Baseline*` (`A`)**, và chuẩn tham chiếu **`GPT-6.2 Instant` (`D`, chỉ có trên `SR-01`)** trên **13 tình huống** (`7` hồi quy `SR-01..SR-07` + `6` chưa từng thấy `V5-01..V5-06`).

**Các tín hiệu thực nghiệm chính đã quan sát được:**
1. **Layer 1 (Semantic Integrity):** Cả **`V5-A (E)`** và **`V5-B (F)`** đều đạt **`13/13` `Gate 0 Pass`** với **`0` lỗi `Critical`, `0` `Major`, `0` `Minor`, và `0` `intent_leak`** trong 47 phiên audit ẩn danh ([semantic-integrity-report.md](semantic-integrity-report.md)). Trong khi đó, `C` (`v4.1+SR`) mắc `3` lỗi `Minor` (`SR-07`, `V5-03`, `V5-06`), `B_prior` mắc `1` lỗi `Major` (`có thể → sẽ`), và `A` mắc `1` lỗi `Major` (`V5-05`).
2. **Chi phí Ngữ cảnh, Độ trễ và Kích thước Instruction:**
   - **Instruction footprint:** `V5-A` giảm **`-25.7%` dung lượng** (`6,674 bytes / 63 dòng` vs `8,986 bytes / 82 dòng` của `v4.1`); **`V5-B` giảm `-50.9%`** (`4,413 bytes / 47 dòng`).
   - **Số lượt phải đọc `references/` (`refs_read`):** Giảm từ **`9/13` (`B`) và `10/13` (`C`)** xuống còn **`3/13` ở cả `E` và `F`** (chỉ đọc thêm `references/` khi gặp Business Rule phức tạp như `SR-05`, `V5-05` hoặc bảng biểu `SR-07` / `V5-06`).
   - **Chi phí token đầu vào cộng dồn (`avg_input_tokens_sum`):** **`F` giảm `-27.4%` (`12,885.9` vs `B: 17,737.4`)**; `E` giảm `-22.4%` (`13,764.4`).
   - **Độ trễ trung bình (`avg_latency_sec`):** **`F` nhanh nhất (`21.46s`, nhanh hơn `30.6%` so với `B: 30.92s`)**; `E` đạt `24.31s` (`-21.4%` vs `B`).
   - **Độ gọn đầu ra (`avg_words_all`):** **`F` ngắn gọn nhất (`443.4` từ, ngắn hơn `-19.0%` so với `B: 547.4` từ; trên bộ unseen `V5-01..06` giảm tới `-23.2%`: `486.7` vs `633.5` từ)**. `E` dài `532.7` từ (`-2.7%` vs `B`) do tự mở rộng thêm checklist hành động ở `SR-07` và bảng kiểm thử dài ở `V5-05`.
3. **Sửa triệt để lỗi rò rỉ nội bộ & mở khóa diễn đạt cho người dùng cuối:** Cả `V5-A` và `V5-B` đều **không còn in mục `"Điểm bản gốc chưa nêu cụ thể"`** vào thông báo gửi người dùng cuối hoặc email giao tiếp nội bộ (`SR-01`, `SR-02`, `SR-03`, `V5-02`, `V5-03`), đồng thời giữ lại đầy đủ `[Chưa chốt]` khi viết Business Rule (`SR-05`, `V5-05`).
4. **Phát hiện phương pháp luận quan trọng về Nhánh `A`:** Kiểm tra log `transcript_full.jsonl` cho thấy **13/13 lượt chạy của Nhánh `A` (`sr-group-a`) đã tự động kích hoạt skill `v4.1` cài sẵn trên máy thông qua `<skills>` của Antigravity IDE (`read_file` trên `SKILL.md` v4.1)**. Do đó, Nhánh `A` trong dữ liệu này thực chất phản ánh *Gemini 4 Neon + kích hoạt tự nhiên `v4.1`*, không phải *Gemini thuần không có skill*.
5. **Chưa kết luận người thắng Layer 2:** Đánh giá mù thực sự của con người (Layer 2) đang chờ chủ sở hữu thực hiện qua [human-blind-eval-pack.md](human-blind-eval-pack.md).

---

## 2. Thiết kế Thí nghiệm & Minh bạch Phương pháp

### 2.1. Các nhánh đối chứng (Arms) & Cách kích hoạt

| Nhánh | Tên cấu hình | Cách đưa instruction vào subagent | Model thực tế ghi trong log | Ghi chú kích hoạt thực tế |
|---|---|---|---|---|
| **A** | `Baseline*` (Native Auto-Discovery `v4.1`) | System prompt trung tính (~190 bytes), không chèn skill | `gemini-4-hydrogen-high` | **13/13 lượt tự gọi `read_file` đọc `SKILL.md` v4.1** từ global skill (`Tầng 4/5`); 8/13 lượt đọc thêm `references/`. Trên `V5-05` gửi 2 tin nhắn (bản đầu + bản hiệu đính sau 16s). |
| **B** | `v4.1` (Injected) | Tiêm nguyên văn `SKILL.md` v4.1 (`8,986 bytes`) vào system prompt | `gemini-4-hydrogen-high` | 0 lượt cần đọc `SKILL.md`; 9/13 lượt đọc thêm `references/`. |
| **C** | `v4.1 + SR` (Injected) | Tiêm `SKILL.md` v4.1 + chỉ dẫn Semantic Reconstruction (`10,422 bytes`) | `gemini-4-hydrogen-high` | 0 lượt đọc `SKILL.md`; 10/13 lượt đọc thêm `references/`. |
| **E** | **`V5-A`** (Refactored) | Tiêm [prototypes/v5-a/SKILL.md](prototypes/v5-a/SKILL.md) (`6,674 bytes`) | `gemini-4-hydrogen-high` | Chỉ 3/13 lượt đọc thêm `references/` (`SR-05`, `V5-05`, `V5-06`). |
| **F** | **`V5-B`** (Minimalist Core) | Tiêm [prototypes/v5-b/SKILL.md](prototypes/v5-b/SKILL.md) (`4,413 bytes`) | `gemini-4-hydrogen-high` | Chỉ 3/13 lượt đọc thêm `references/` (`SR-05`, `SR-07`, `V5-05`). |
| **D** | `GPT-6.2 Instant` | Tham chiếu thực tế do người dùng cung cấp (`SR-01`) | `GPT-6.2 Instant` | `n = 1` (`SR-01`, 277 từ). Không ngoại suy cho các ca còn lại. |
| **B_prior** | `v4.1_prior` | Output chạy trước đây do người dùng cung cấp (`SR-01`) | Gemini + `v4.1` (prior) | `n = 1` (`SR-01`, 255 từ), tái kiểm định riêng lỗi tình thái. |

> **Giới hạn phương pháp cần ghi nhận:** Các nhánh `B, C, E, F` được kiểm thử bằng **tiêm trực tiếp `SKILL.md` vào system prompt của subagent** (`subagent injection`), khác với **cơ chế native skill activation** ngoài phiên chính (nơi model chỉ thấy mô tả ngắn và tự `read_file` khi kích hoạt, như đã xảy ra với Nhánh `A`). Ngoài ra, dữ liệu `SR-01..SR-07` cho `A, B, C` được tái sử dụng nguyên văn từ `run1` của [experiments/semantic-reconstruction/raw-outputs.jsonl](../semantic-reconstruction/raw-outputs.jsonl) (cùng model và cùng prompt).

### 2.2. Bộ dữ liệu kiểm thử (13 ca)

- **7 ca hồi quy (`SR-01..SR-07`):** Thông báo dịch vụ (`SR-01`, `SR-02`), giao tiếp công việc (`SR-03`), giải thích khái niệm kỹ thuật (`SR-04`), Business Rule hoàn tiền (`SR-05`), tài liệu kỹ thuật DB failover (`SR-06`), quy trình nhiều thông tin CSKH/Kho (`SR-07`).
- **6 ca mới chưa từng thấy (`V5-01..V5-06`):**
  - `V5-01`: Hội thoại tự nhiên với đồng nghiệp đang bị stress vì 18 comment PR + đổi requirement phút chót.
  - `V5-02`: Thông báo bảo trì app ngân hàng tối ưu để đọc nhanh trên điện thoại.
  - `V5-03`: Email ra quyết định trong 30 giây cho PM & Trưởng nhóm Vận hành (giữa 2 phương án chuyển đổi dữ liệu).
  - `V5-04`: Giải thích kỹ thuật phân biệt và phối hợp `Rate Limiting` vs `Circuit Breaker`.
  - `V5-05`: Đặc tả Business Rule phức tạp (chiết khấu thương mại B2B kèm khóa công nợ quá hạn `> 15 ngày` + nhiều lỗ hổng ẩn).
  - `V5-06`: Quy định nội bộ 3 đoạn dài bị lặp/nhảy ý cần sắp xếp lại cho dễ tra cứu.

Toàn bộ dữ liệu thô (`67` bản ghi) lưu tại [raw-outputs-v5.jsonl](raw-outputs-v5.jsonl) và [dataset-v5.jsonl](dataset-v5.jsonl).

---

## 3. Đo lường Chi phí Ngữ cảnh, Độ trễ & Độ gọn

Số liệu trích xuất trực tiếp từ [metrics-v5.json](metrics-v5.json):

| Chỉ số | Nhánh A (`Baseline*`) | Nhánh B (`v4.1`) | Nhánh C (`v4.1+SR`) | Nhánh E (`V5-A`) | Nhánh F (`V5-B`) | Tham chiếu D (`GPT-6.2`, `n=1`) |
|---|---:|---:|---:|---:|---:|---:|
| Dung lượng `SKILL.md` | *(tự đọc 8,986 B)* | 8,986 B (82 dòng) | 10,422 B *(kèm SR)* | **6,674 B (63 dòng)** | **4,413 B (47 dòng)** | — |
| Số ca kiểm thử (`n`) | 13 | 13 | 13 | 13 | 13 | 1 (`SR-01`) |
| Số lượt gọi `read_file` (`refs_read`) | **13 / 13** *(SKILL+refs)* | 9 / 13 | 10 / 13 | **3 / 13** | **3 / 13** | — |
| `avg_input_tokens_sum` | 18,123.1 | 17,737.4 | 16,108.2 | **13,764.4** (`-22.4%` vs B) | **12,885.9** (`-27.4%` vs B) | — |
| `avg_output_tokens_sum` | 5,621.1 | 5,382.6 | 4,374.8 | 4,307.2 | **3,739.7** | — |
| `avg_latency_sec` (min–max) | 32.15s (14–69s) | 30.92s (9–54s) | 26.77s (10–46s) | 24.31s (11–68s) | **21.46s (9–40s)** | — |
| `avg_words_all` (13 ca) | 503.0 từ | 547.4 từ | 468.8 từ | 532.7 từ | **443.4 từ** | — |
| `avg_words_sr` (`SR-01..07`) | 423.1 từ | 473.6 từ | **377.4 từ** | 442.1 từ | 406.3 từ | 277.0 từ (`SR-01`) |
| `avg_words_unseen` (`V5-01..06`) | 596.2 từ | 633.5 từ | 575.3 từ | 638.3 từ | **486.7 từ** | — |

**Phân tích chi phí – hiệu năng:**
- **`V5-B (F)` vượt trội về hiệu suất vận hành:** Giảm một nửa kích thước `SKILL.md` (`-50.9%`), giảm tỷ lệ phải tra thêm file tham chiếu từ ~70% (`9/13` ở B, `10/13` ở C) xuống `23%` (`3/13`), rút tổng token đầu vào trung bình gần `4,850` token/lượt (`-27.4%` vs B), phản hồi nhanh nhất (`21.46s`), và tạo văn bản cô đọng nhất (`443.4` từ).
- **`V5-A (E)` tiết kiệm ngữ cảnh & độ trễ tốt (`-22.4%` token đầu vào, `-21.4%` latency)** nhưng **vẫn giữ xu hướng viết dài trên các ca tài liệu nghiệp vụ nhiều tầng** (`SR-07`: `569` từ; `V5-05`: `2,202` từ) do vẫn giữ danh sách câu trúc định dạng tương đối đầy đủ từ `v4.1`.

---

## 4. Kết quả Layer 1: Bảo toàn Ngữ nghĩa (Semantic Integrity)

Chi tiết xem tại [semantic-integrity-report.md](semantic-integrity-report.md) và [semantic-integrity-audit.jsonl](semantic-integrity-audit.jsonl):

- **`V5-A (E)` & `V5-B (F)`:** **`13/13` `Gate 0 Pass`**, **`0` lỗi ở mọi cấp độ** (`Critical = 0`, `Major = 0`, `Minor = 0`, `intent_leak = 0`).
- **`v4.1 (B)`:** `6/6` mới pass sạch (`+ 7/7 SR run1` trước đó pass), nhưng `B_prior` trên `SR-01` xác nhận `Major` (`có thể → sẽ`).
- **`v4.1+SR (C)`:** `7/7` mới `Gate 0 Pass`, nhưng phát sinh **`3` lỗi `Minor`** (`SR-07 C`: thu hẹp `"phiếu giao hàng"` → `"Ảnh chụp phiếu giao hàng"`; `V5-03 C`: thêm `"(Sản phẩm)"` + thu hẹp mốc hỗ trợ ở PA2; `V5-06 C`: câu mở đầu gắn toàn bộ hướng dẫn với `"trên thiết bị do công ty cấp phát"`).
- **`Baseline* (A)`:** `5/6` mới pass; **`1` lỗi `Major` trên `V5-05`** (đóng khung `$V$` là giá trị từng đơn hàng mà bỏ sót câu hỏi chưa chốt *đơn lẻ vs cộng dồn tháng/quý*, đồng thời lọt 1 dòng meta `"Bản hiệu đính thống nhất số mục tham chiếu..."` ở đầu văn bản).

---

## 5. So sánh Chất lượng Truyền đạt Sơ bộ (Layer 2 — Chờ Human Blind Eval Xác nhận)

> **Cảnh báo:** Phần nhận xét dưới đây là **quan sát định tính đối chiếu văn bản trước khi chấm mù**, không thay thế cho điểm số Layer 2 trong [human-blind-eval-pack.md](human-blind-eval-pack.md).

### 5.1. Giải mã ngôn ngữ tự nhiên vs "Dịch giữ vỏ" (`SR-01` — Thông báo người dùng cuối)
- **`v4.1 (B)` (`427` từ, `54s`)** vẫn mắc kẹt hai vấn đề: (1) chèn một phụ lục rà soát nội bộ ở cuối thư người dùng (`"Điểm bản gốc chưa nêu cụ thể (nên bổ sung trước khi phát hành cho người dùng cuối)"`), và (2) giữ nguyên cụm hành chính `"phương thức ghi nhận mặc định"`, `"xác thực đa tầng có điều kiện"`.
- **`V5-A (E)` (`281` từ, `33s`)** bỏ sạch phụ lục rà soát nội bộ và rút độ dài tương đương `GPT-6.2 (D: 277 từ)`, nhưng **vẫn giữ nhiều cụm Hán-Việt/kỹ thuật nguyên khối** như `"mô hình xác thực đa tầng có điều kiện"`, `"đối soát định kỳ"`, `"các điều kiện tiên quyết"`.
- **`V5-B (F)` (`314` từ, `22s`)** tiến gần nhất tới cách diễn đạt dễ tiếp thu của **`D` (`GPT-6.2`)**: chia 3 tiểu mục rõ cho người đọc (`"Thay đổi chính và ảnh hưởng có thể gặp"`, `"Lưu ý cho tài khoản chuyển tiếp..."`, `"Việc bạn nên làm"`), đồng thời chuyển ngữ tự nhiên hơn (`"xác thực nhiều lớp có điều kiện"`, `"tạm ngưng"`, `"các điều kiện bắt buộc"` — gần với `"xác thực nhiều lớp"`, `"tạm thời không sử dụng được"`, `"các điều kiện cần thiết"` của `D`).

### 5.2. Tôn trọng ngữ cảnh giao tiếp tự nhiên (`V5-01`, `V5-02`, `V5-03`)
- **`V5-01` (Trả lời đồng nghiệp stress vì 18 comment PR + đổi req phút chót):**
  - `C` (`v4.1+SR`) viết tới `273` từ theo cấu trúc lý do đánh số `1. 2.` hơi giống bài phân tích hơn là tin nhắn chat đồng nghiệp.
  - **`F` (`V5-B`, `157` từ, `11s`)** ngắn và đời nhất (*"Thôi dẹp máy đi nghỉ đi ông ơi. Đầu đang mụ mị mà cố ngồi sửa tiếp giữa lúc vừa ăn 18 comment vừa bị đổi requirement thì dễ đẻ thêm bug lắm..."*), hợp đúng ngữ cảnh rủ ra làm ly nước nghỉ ngơi. `E` (`178` từ) và `B` (`181` từ) cũng giữ giọng đồng nghiệp tốt.
- **`V5-02` (Thông báo bảo trì đọc trên điện thoại):**
  - Cả **`E` (`159` từ, `11s`)** và **`F` (`162` từ, `9s`)** đều đưa thẳng khung giờ **`01:00 – 03:30 rạng sáng Chủ nhật tới`** lên ngay dòng tiêu đề (*"Thông báo bảo trì hệ thống: 01:00 – 03:30 rạng sáng Chủ nhật tới"* / *"Bảo trì hệ thống chuyển tiền nhanh 24/7 (01:00 – 03:30 rạng sáng Chủ nhật tới)"*) — giúp người mở app nhìn lướt 2 giây là nắm được ngay khung giờ ảnh hưởng, điều mà `B` và `C` chưa đưa lên tiêu đề.
- **`V5-03` (Email cần PM chốt trong 30 giây):**
  - Cả `B, C, E, F` đều tóm bằng bảng so sánh 2 phương án rất rõ. Điểm cộng riêng của `E` (`340` từ, `12s`) và `F` (`360` từ, `19s`) là đưa luôn dòng **`Cần chốt trước 17:00 thứ Tư`** vào Subject email và giữ nguyên phạm vi hỗ trợ của Phương án 2 mà không tự gán nhãn `"(Sản phẩm)"` hay thu hẹp mốc hỗ trợ như `C`.

### 5.3. Quy trình dài & Business Rule phức tạp (`SR-07`, `V5-05`, `V5-06`)
- **`SR-07` (CSKH / Kho / Quản lý ca):**
  - `B` (`627` từ) thêm mục `"Điểm chưa quy định trong tài liệu gốc"` không thực sự phù hợp với vai trò một SOP vận hành; `C` (`392` từ) gọn nhưng bị lỗi `Minor` (`"Ảnh chụp phiếu giao hàng"`).
  - `E` (`569` từ, `14s`) bổ sung hẳn mục **"4. Việc cần làm theo từng bộ phận"** (tốt cho nhân viên tra theo vai trò), trong khi `F` (`416` từ, `34s`) giữ cấu trúc bảng gọn hơn `27%` — cả hai đều giữ nguyên `"Phiếu giao hàng đi kèm"` (`0` lỗi).
- **`V5-05` (Business Rule B2B phức tạp):**
  - Cả `E` (`2,202` từ) và `F` (`1,455` từ) đều bắt trọn toàn bộ 3 bậc chiết khấu, điều kiện biên `<= 15 ngày` vs `> 15 ngày`, thứ tự ưu tiên khóa công nợ, bảng kiểm thử/chuyển trạng thái và toàn bộ nhóm điểm `[Chưa chốt]` (bao gồm cả điểm `đơn lẻ vs cộng dồn tháng/quý` mà `A` làm rơi). Tuy nhiên `F` biểu đạt chặt chẽ hơn **`-33.9%` độ dài so với `E`** và **`-28.7%` so với `B` (`2,041` từ)** với thời gian phản hồi chỉ `40s`.

---

## 6. Đánh đổi & Khuyến nghị Prototype Dựa trên Bằng chứng

| Tiêu chí so sánh | Giữ `v4.1` | Chọn hướng **V5-A** (`E`) | Chọn hướng **V5-B** (`F`) |
|---|---|---|---|
| **Độ an toàn ngữ nghĩa (Layer 1)** | Tốt (nhưng từng lộ phụ lục nội bộ ra end-user & cần sửa prompt tránh `B_prior`) | **13/13 sạch hoàn toàn (`0 Minor/Major`)** | **13/13 sạch hoàn toàn (`0 Minor/Major`)** |
| **Chặn rò rỉ ghi chú nội bộ (`[Chưa chốt]`)** | Kém trên thông báo/email (`B` vẫn in ra ở `SR-01`, `SR-02`, `SR-03`, `SR-07`) | **Triệt để** (chỉ dùng `[Chưa chốt]` cho spec kỹ thuật/BR) | **Triệt để** |
| **Giải mã văn phong hành chính -> dễ hiểu (`SR-01`, `V5-01`)** | Khá thụ động | Cải thiện cấu trúc, nhưng đôi chỗ còn giữ từ gốc hơi cứng (`đa tầng`, `tiên quyết`) | **Tốt nhất trong 5 nhánh Gemini** — chủ động hạ tầng từ vựng sang tiếng Việt đời thực (`nhiều lớp`, `tạm ngưng`, chat tự nhiên) |
| **Chi phí context & Tốc độ** | Nặng (`8,986 B`, `30.92s`, `9/13` `refs_read`) | Nhẹ hơn (`-25.7% B`, `24.31s`, `3/13` `refs_read`) | **Nhẹ và nhanh nhất (`-50.9% B`, `21.46s`, `3/13` `refs_read`, `-27.4%` token)** |
| **Độ chi tiết sẵn sàng cho BA/Dev (`V5-05`, `SR-07`)** | Dài (`547.4` từ TB) | Rất chi tiết (có mục việc theo từng vai trò ở `SR-07`, `AC-01..11` ở `V5-05`), nhưng dễ phình độ dài (`2,202` từ ở `V5-05`) | Cân bằng giữa đủ ý và gọn (`1,455` từ ở `V5-05`, `-34%` so với `E`), ít rủi ro thừa chữ |

### Khuyến nghị sơ bộ (Chờ xác nhận qua Human Blind Evaluation)
1. **Ứng viên sáng giá nhất cho nền tảng V5 là `V5-B` (hoặc kiến trúc lấy `V5-B` làm lõi + mượn 1–2 chi tiết hay từ `V5-A`):**
   - `V5-B` chứng minh trong thực nghiệm rằng một instruction tinh gọn **chỉ còn `4,413 bytes` (`47` dòng)** **không hề làm giảm độ an toàn ngữ nghĩa** (`13/13` sạch ở Layer 1, thậm chí sạch hơn `v4.1+SR` vốn bị `3 Minor`), trong khi **nhanh hơn 30.6%**, **tiết kiệm 27.4% token đầu vào**, **ngắn gọn hơn 19.0%**, và **linh hoạt giải mã câu chữ tự nhiên nhất** ở cả thông báo người dùng lẫn chat đồng nghiệp.
   - Điểm duy nhất có thể cân nhắc bổ sung từ `V5-A` (sau khi người dùng chấm mù xong) là thói quen **chốt theo vai trò hành động** ở các SOP đa phòng ban (như mục `"Việc cần làm theo từng bộ phận"` của `V5-A` trên `SR-07`, nếu Human Eval đánh giá cao mục này hơn bản gọn của `V5-B`).
2. **Không giữ cấu trúc thêm đoạn `"Điểm bản gốc chưa nêu cụ thể"` mặc định cho mọi thể loại của `v4.1`:** Thực nghiệm khẳng định việc tách rõ ranh giới *Spec/Business Rule (cần `[Chưa chốt]`)* vs *Thông báo/Email/Chat (tuyệt đối không lộ ghi chú rà soát nội bộ)* của V5 đã giải quyết triệt để phàn nàn `"dài dòng"` từ Human Evaluation đợt trước mà không ảnh hưởng tới `SR-05` hay `V5-05`.

---

## 7. Bước tiếp theo cần Phê duyệt từ Người dùng

Trước khi quyết định có phát hành ViWrite V5 hay nâng cấp bất kỳ file nào trên `main`:
1. **Thực hiện Human Blind Evaluation (Layer 2):** Chấm điểm mù trên 13 ca tại [human-blind-eval-pack.md](human-blind-eval-pack.md) (sau khi chấm xong mới đối chiếu với [human-blind-key.json](human-blind-key.json)).
2. **Quyết định định hướng phiên bản tiếp theo (sau khi có kết quả chấm mù):**
   - Chọn **V5-B**, **V5-A**, hay **phương án kết hợp (V5-B core + chọn lọc quy tắc tốt từ V5-A)**;
   - Nếu cần thêm **0-skill Baseline thuần** đúng nghĩa (tắt hẳn global skill `v4.1` trước khi chạy `Group A`) hay mở rộng mẫu `GPT-6.2 Instant` trên `V5-01..06` để làm mốc đối chứng chéo.
3. **Giữ nguyên `v4.1.0-beta` trên `main`** cho tới khi hoàn tất Independent Review & Human Evaluation.
