# Layer 1 Report: Semantic Integrity & Hard-Fail Audit (ViWrite V5)

Báo cáo này tổng hợp kết quả kiểm định **Layer 1 (Semantic Integrity Gate)** cho thí nghiệm `V5 — Communication-First Prototype` trên **47 phiên audit đơn lẻ, ẩn danh** bằng subagent `v5-integrity-auditor` (`gemini-4-hydrogen-high`), kết hợp đối chiếu dữ liệu lịch sử từ nhánh `experiment/semantic-reconstruction`.

> **Lưu ý phương pháp:** Trong 47 bản audit mới này, `v5-integrity-auditor` chỉ nhận **1 cặp (nguồn gốc + 1 output ứng viên)** tại một thời điểm, hoàn toàn **không biết tên nhóm (`A/B/C/E/F/D/B_prior`) hay tên model**, và chấm độc lập theo thang 4 mức tác động thực tế (`None` / `Minor` / `Major` / `Critical`) cùng cơ chế chặn `Gate 0` (`HF-1..HF-6`, `modality_shifts`, `scope_narrowing`, `intent_leak`).

---

## 1. Bảng Tổng hợp Kết quả Layer 1 theo Nhánh (47 Fresh Audits + Historical Context)

| Nhánh | Mô tả | Số bản mới được audit (`n`) | `Gate 0 Pass` | `Critical` | `Major` | `Minor` | `intent_leak` | Ngữ cảnh lịch sử (`SR-01..07 run1`) |
|---|---|---:|---:|---:|---:|---:|---:|---|
| **A** (`Baseline*`) | Gemini 4 Neon (nhưng tự kích hoạt skill `v4.1` qua `<skills>` trong IDE) | 6 (`V5-01..06`) | **5 / 6** | 0 | **1** (`V5-05`) | 0 | 0 | `7 / 7` pass (`hf-audit.jsonl`, binary Gate 0) |
| **B** (`v4.1`) | Gemini 4 Neon + `SKILL.md` v4.1 (system prompt) | 6 (`V5-01..06`) | **6 / 6** | 0 | 0 | 0 | 0 | `7 / 7` pass (`hf-audit.jsonl`, binary Gate 0) |
| **C** (`v4.1+SR`) | Gemini 4 Neon + `v4.1` + Semantic Reconstruction | 7 (`SR-07` + `V5-01..06`) | **7 / 7** | 0 | 0 | **3** (`SR-07`, `V5-03`, `V5-06`) | 0 | `7 / 7` pass (`hf-audit.jsonl`); `SR-07 C` re-audited = `Minor` |
| **E** (`V5-A`) | Gemini 4 Neon + Prototype V5-A (Refactor `Understand → Communicate → Verify`) | 13 (`SR-01..07` + `V5-01..06`) | **13 / 13** | 0 | 0 | 0 | 0 | *(Không chạy ở nhánh cũ)* |
| **F** (`V5-B`) | Gemini 4 Neon + Prototype V5-B (Minimalist Communication-First Core) | 13 (`SR-01..07` + `V5-01..06`) | **13 / 13** | 0 | 0 | 0 | 0 | *(Không chạy ở nhánh cũ)* |
| **D** (`GPT-6.2`) | GPT-6.2 Instant mặc định (user-provided, chỉ có `SR-01`) | 1 (`SR-01`) | **1 / 1** | 0 | 0 | **1** (`SR-01`) | 0 | Re-audit xác nhận `Minor`, giữ đúng tình thái & ngoại lệ |
| **B_prior** (`v4.1_prior`) | Gemini + `v4.1` chạy trước đây trên `SR-01` (user-provided) | 1 (`SR-01`) | **0 / 1** | 0 | **1** (`SR-01`) | 0 | 0 | Re-audit xác nhận `Major` (`có thể → sẽ`) |

**Nhận xét tổng quát Layer 1:**
- Cả **V5-A (`E`)** và **V5-B (`F`)** đạt **13/13 `Gate 0 Pass`** với **0 lỗi `Critical`, 0 `Major`, 0 `Minor` và 0 `intent_leak`** trên cả 7 case hồi quy (`SR-01..07`) lẫn 6 case mới (`V5-01..06`).
- Cả hai prototype V5 đều loại bỏ hoàn toàn hiện tượng rò rỉ nội dung rà soát nội bộ (`"Điểm chưa xác định trong bản gốc"`) vào các thông báo/email dành cho người dùng cuối (`SR-01`, `SR-02`, `SR-03`, `V5-02`, `V5-03`) mà không đánh đổi độ chính xác quy tắc nghiệp vụ ở `SR-05` và `V5-05`.
- Ngược lại, **nhánh `C` (`v4.1+SR`)** tuy đạt `7/7` `Gate 0 Pass`, lại phát sinh **3 lỗi mức `Minor`** liên quan đến việc thu hẹp nhẹ phạm vi hoặc diễn giải thêm chi tiết ngầm định trong quá trình tái cấu trúc tự do (`SR-07`, `V5-03`, `V5-06`).

---

## 2. Đánh giá lại các ca ranh giới: `SR-01 B_prior`, `SR-07 C` và `SR-01 D` (Theo Tác động Thực tế)

Theo yêu cầu thiết kế Layer 1 mới, việc phân loại phải dựa vào **mức độ tác động lên quyết định hoặc nghĩa vụ ngoài đời thực**, thay vì gộp mọi biến đổi câu chữ vào một nhãn lỗi chung:

| Ca & Nhánh | Audit Code | Bản gốc / `must_preserve` | Output ứng viên | Phán quyết Audit (Judge) | Đối chiếu thủ công (`Verified`) | Lý do & Tác động thực tế |
|---|---|---|---|---|---|---|
| **`SR-01 B_prior`** | `AUD-15` | *"...quá trình kích hoạt lại quyền truy cập **có thể** ghi nhận sự gián đoạn cục bộ hoặc phát sinh trạng thái tạm treo đối với một số tính năng nâng cao..."* | *"...việc kích hoạt lại quyền truy cập có thể bị gián đoạn cục bộ hoặc một số tính năng nâng cao **sẽ bị tạm treo**..."* | `Gate 0 FAIL` — **`Major`** (`modality_shift`) | **Verified (`Major`)** | Đảo tình thái từ **khả năng có điều kiện (`có thể`)** sang **chắc chắn xảy ra (`sẽ`)** trên hệ quả ảnh hưởng trực tiếp tới quyền lợi tính năng của người dùng trả phí. Làm sai lệch cam kết vận hành của thông báo. |
| **`SR-07 C`** (`v4.1+SR`) | `AUD-17` | *"...cung cấp đầy đủ hình ảnh chụp rõ tình trạng bên ngoài lẫn bên trong kiện hàng **cùng với phiếu giao hàng đi kèm**."* | *"- Ảnh chụp rõ tình trạng bên ngoài kiện hàng.<br>- Ảnh chụp rõ tình trạng bên trong kiện hàng.<br>- **Ảnh chụp phiếu giao hàng đi kèm.**"* | `Gate 0 PASS` — **`Minor`** (`scope_narrowing`) | **Verified (`Minor`)** | Thu hẹp định dạng từ `"phiếu giao hàng đi kèm"` (có thể là bản scan PDF hoặc chứng từ đính kèm) thành `"Ảnh chụp phiếu giao hàng đi kèm"`. Trên thực tế có thể gây khước từ nhầm nếu khách nộp file PDF/chứng từ điện tử, nhưng không đảo ngưỡng tiền (`< 500.000đ`), không đổi hạn `48 giờ` / `24 giờ làm việc` và không thay đổi điều kiện hợp lệ cốt lõi. Đáng lưu ý: cả **`SR-07 E` (`V5-A`)** giữ nguyên tách bạch `"Phiếu giao hàng đi kèm"` mà không thu hẹp thành `"Ảnh chụp"`. |
| **`SR-01 D`** (`GPT-6.2`) | `AUD-16` | *"kể từ chu kỳ chuyển đổi sắp tới... gói dịch vụ đang ở trạng thái kích hoạt... gián đoạn cục bộ... không còn thực thi qua phương thức ghi nhận mặc định trước đây"* | *"Trong thời gian tới... các gói dịch vụ hiện tại... quá trình kích hoạt lại quyền truy cập có thể bị gián đoạn hoặc một số tính năng nâng cao có thể tạm thời không sử dụng được..."* | `Gate 0 PASS` — **`Minor`** | **Verified (`Minor`)** | Lược bỏ một số chi tiết phụ (`"cục bộ"`, `"mặc định trước đây"`, `"chu kỳ chuyển đổi"` → `"thời gian tới"`), nhưng **giữ nguyên toàn bộ tình thái `"có thể"`**, giữ đúng ngoại lệ giới hạn truy xuất thủ công và giữ mức độ bất định (không bịa ngày/nút bấm). Lược giản làm văn phong tự nhiên hơn mà không sai logic vận hành. |

---

## 3. Phân tích chi tiết mọi lỗi `Major` và `Minor` phát hiện trên 47 bản audit

| Audit Code | Case & Nhánh | Mức độ | Phân loại | Bằng chứng trích từ nguồn vs output | Trạng thái xác minh |
|---|---|---|---|---|---|
| **`AUD-38`** | `V5-05` — Nhánh **A** (`Baseline*`) | **`Major`** (`Gate 0 FAIL`) | `HF-3`, `HF-5`, `scope_narrowing` + meta leak | **Nguồn:** *"Theo chính sách ưu đãi doanh số, các đơn hàng... có giá trị đạt từ 100 triệu..."* (`must_preserve` yêu cầu giữ trạng thái chưa chốt giữa **từng đơn lẻ vs cộng dồn tháng/quý**).<br>**Output A:** Mục 1 định nghĩa cứng *"Giá trị đơn hàng ($V$): Giá trị của từng đơn hàng"*, không đưa câu hỏi `đơn lẻ hay cộng dồn` vào Mục 4 `[Chưa chốt]`. Ngoài ra dòng 1 còn sót meta hội thoại: `"Bản hiệu đính thống nhất số mục tham chiếu (thay thế bản gửi ngay trước đó):"` | **Verified (`Major`)** |
| **`AUD-15`** | `SR-01` — **`B_prior`** | **`Major`** (`Gate 0 FAIL`) | `modality_shift` | Đổi *"có thể ... phát sinh trạng thái tạm treo"* → *"sẽ bị tạm treo"*. | **Verified (`Major`)** |
| **`AUD-17`** | `SR-07` — Nhánh **C** (`v4.1+SR`) | **`Minor`** (`Gate 0 PASS`) | `scope_narrowing` | *"phiếu giao hàng đi kèm"* → *"Ảnh chụp phiếu giao hàng đi kèm"*. | **Verified (`Minor`)** |
| **`AUD-30`** | `V5-03` — Nhánh **C** (`v4.1+SR`) | **`Minor`** (`Gate 0 PASS`) | `scope_narrowing` | Thêm chú thích suy luận `"(Sản phẩm)"` sau `"anh Minh"`; và ghi phần việc hỗ trợ của Phương án 2 là *"trong thời gian chạy song song"* (nguồn nói tới mốc đối soát khớp lại *"sau ngày thứ Ba"*). | **Verified (`Minor`)** |
| **`AUD-45`** | `V5-06` — Nhánh **C** (`v4.1+SR`) | **`Minor`** (`Gate 0 PASS`) | `scope_narrowing` | Câu mở đầu viết *"áp dụng cho toàn thể nhân viên khi làm việc ngoài văn phòng trên thiết bị do công ty cấp phát"*, vô tình thu hẹp cả quy định xin phép và Wi-Fi/VPN thành chỉ gắn với thiết bị cấp phát (trong nguồn, `"thiết bị cấp phát"` gắn ở tiêu đề và mục báo mất thiết bị). | **Verified (`Minor`)** |
| **`AUD-16`** | `SR-01` — **`D` (`GPT-6.2`)** | **`Minor`** (`Gate 0 PASS`) | Lược giản phụ | Lược bỏ `"cục bộ"`, `"mặc định trước đây"`, rút gọn `"chu kỳ chuyển đổi sắp tới"` → `"Trong thời gian tới"`. | **Verified (`Minor`)** |

---

## 4. Kết luận ngắn cho Layer 1

1. **Tách `Gate 0` thành 4 mức độ tác động có hiệu quả thực tế rõ rệt:** Bộ tiêu chí mới phân biệt được lỗi làm thay đổi nghĩa vụ/tình thái nghiêm trọng (`SR-01 B_prior` = `Major`; `V5-05 A` = `Major`) khỏi các điều chỉnh diễn đạt nhẹ (`SR-07 C` = `Minor`; `SR-01 D` = `Minor`).
2. **Không có dấu hiệu đánh đổi an toàn ngữ nghĩa khi chuyển sang V5:** Cả **V5-A (`E`)** và **V5-B (`F`)** đều đạt **`13/13` pass sạch hoàn toàn (`0 Minor`, `0 Major`, `0 Critical`)**, vượt trội hơn nhánh **`C` (`v4.1+SR`)** vốn bị `3` lỗi `Minor` do xu hướng tự diễn giải thêm khi tái cấu trúc.
3. **Điểm lưu ý về Nhánh `A`:** Như ghi nhận trong [metrics-v5.json](metrics-v5.json) và [v5-experiment-report.md](v5-experiment-report.md), toàn bộ 13 lượt chạy của Nhánh `A` đã tự gọi `read_file` đọc `SKILL.md` v4.1 thông qua cơ chế auto-discovery của IDE — và dù đọc `v4.1`, ở `V5-05`, Nhánh `A` vẫn mắc lỗi `HF-3 / HF-5` (cộng thêm lỗi sót 1 dòng meta tự hiệu đính). Nhánh `E` (`V5-A`) và `F` (`V5-B`) chạy ổn định ngay trong một lượt mà không mắc bất kỳ lỗi nào.
