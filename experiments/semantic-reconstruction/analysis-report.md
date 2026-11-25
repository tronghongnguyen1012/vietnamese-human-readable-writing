# Báo cáo Thực nghiệm: Giả thuyết Semantic Reconstruction & Khoảng cách Chất lượng Diễn đạt (`experiment/semantic-reconstruction`)

- **Phiên bản đối chứng Skill:** `ViWrite v4.1.0-beta` (`main` tại `a63c39ce`, giữ nguyên không sửa)
- **Model chạy nhóm A, B, C:** `Gemini 4 Neon` (cấu hình đồng nhất giữa 3 nhóm, subagent độc lập không chia sẻ ngữ cảnh chéo)
- **Nhóm tham chiếu D (`GPT-6.2 Instant mặc định`):** Sử dụng duy nhất output thực tế do người dùng cung cấp ở ca `SR-01` (không tự sinh hay bịa output GPT-6.2 cho `SR-02..SR-07`)
- **Tài liệu liên quan trong nhánh thí nghiệm:**
  - Bộ 7 ca kiểm thử: [`dataset.jsonl`](./dataset.jsonl)
  - Toàn bộ 32 output nguyên văn: [`raw-outputs.jsonl`](./raw-outputs.jsonl)
  - Kết quả kiểm định Gate 0 độc lập (32 lượt): [`hf-audit.jsonl`](./hf-audit.jsonl)
  - Số liệu ngôn ngữ học (n-gram overlap, độ dài câu): [`linguistic-metrics.json`](./linguistic-metrics.json)
  - Bộ chấm mù ẩn danh cho người dùng: [`human-blind-eval-pack.md`](./human-blind-eval-pack.md) *(khóa giải mã tại [`human-blind-key.json`](./human-blind-key.json))*
  - Bộ prompt lấy thêm output GPT-6.2 cho `SR-02..SR-07`: [`prompts-for-gpt62.md`](./prompts-for-gpt62.md)

---

## 1. Kết luận Nhanh (BLUF)

Khoảng cách về độ tự nhiên tiếng Việt giữa **Gemini + ViWrite v4.1** và **GPT-6.2 Instant** không chỉ do một nguyên nhân đơn lẻ, mà là **tổng hợp của 3 yếu tố có bằng chứng trực tiếp**:

1. **Nguyên nhân từ Nền model (`Gemini 4 Neon` bám câu nguồn gấp ~3 lần `GPT-6.2 Instant`):** Ngay cả ở **Group A (Gemini mặc định, không cài Skill)** trên ca `SR-01`, tỷ lệ trùng cụm 3 từ với văn bản nguồn là **`49,1%` – `53,9%`**, so với **`16,9%`** ở **GPT-6.2 Instant**. Model có xu hướng mặc định chỉnh sửa cục bộ theo khung câu nguồn thay vì giải mã rồi viết lại từ đầu.
2. **Nguyên nhân từ Thiết kế Skill v4.1 (Gây tâm lý dè dặt & leo thang nhầm Chế độ B):**
   - Các quy tắc bất biến chống bịa trong `SKILL.md` v4.1 không phân biệt **thuật ngữ kỹ thuật/định danh bắt buộc giữ** (ví dụ `RPO > 0`, `split-brain`) với **cụm từ hành chính/trừu tượng giả chuyên môn** (ví dụ `"chu kỳ chuyển đổi sắp tới"`, `"đối soát định kỳ"`, `"gián đoạn cục bộ"`, `"trạng thái tạm treo"`, `"tính tương thích của cấu hình hiện tại"`). Hệ quả là `Group B` giữ nguyên các cụm nặng nề này với tỷ lệ gần tương đương `Group A`.
   - Quy tắc **Trường hợp B** khiến `Group B` (2/2 lượt `SR-01` và `SR-07`) và `Group C` (lượt 2 `SR-01`) tự động gắn thêm khối `"Điểm chưa xác định trong bản gốc..."` (`100–170` từ) vào cuối một **thông báo phát hành cho người dùng cuối**, khiến văn bản dài lên **`419–496` từ** (so với **`277` từ** của GPT-6.2).
   - Trong toàn bộ `20` lượt chạy `Group B` và `Group C`, **không một lượt nào chủ động gọi đọc file trong `references/`** (`refs_read = []`), nghĩa là toàn bộ hành vi thực tế chỉ đến từ `SKILL.md` 82 dòng.
3. **Nguyên nhân từ Phương pháp Đánh giá (`rubric-v2.md` + Gate 0 thiên vị giữ sát nguồn):** Toàn bộ **32/32** output đạt Gate 0 (`0 Hard Fail`, `0 Major`), kể cả `Group B` còn nguyên 10–13 cụm từ hành chính. Ngược lại, chính `sr-hf-auditor` lại ghi chú `minor_notes` lên bản mượt mà nhất của **GPT-6.2 (`SR-01`)** chỉ vì đổi `"chu kỳ chuyển đổi sắp tới"` → `"Trong thời gian tới"` và `"đối soát định kỳ"` → `"kiểm tra định kỳ"`. Nếu thước đo phạt việc diễn giải sang tiếng Việt đời thường nhiều hơn việc để nguyên từ sáo rỗng, LLM Judge sẽ chọn bản "đọc cứng nhưng an toàn".

**Đánh giá giả thuyết Semantic Reconstruction (`Group C`):**
- Bổ sung instruction **Semantic Reconstruction** **có ích rõ rệt về bố cục và độ cô đọng**: trên `SR-01..SR-07`, `Group C` cho văn bản gọn nhất (`369,1` từ TB vs `412,4` của A và `460,6` của B), tách được cấu trúc đoạn mạch lạc hơn (`SR-04`, `SR-07`), **không làm tăng Hard Fail** (`0/10` HF ngay cả trên bẫy thiếu dữ kiện `SR-05`).
- Tuy nhiên, **chỉ gắn thêm đoạn instruction Semantic Reconstruction ở cuối Skill v4.1 CHƯA đủ** để Gemini đạt mức tự nhiên từ vựng như GPT-6.2 trên `SR-01` (trùng 3-gram của `Group C` vẫn ở mức **`49,0%`** ở lượt 1 và **`36,7%`** ở lượt 2), vì xung đột ngầm với thái độ "sợ sai nên giữ nguyên chữ nguồn" của `SKILL.md` v4.1 và thói quen mặc định của model.

---

## 2. Tổng hợp Số liệu Thực nghiệm

### A. So sánh Trực tiếp trên Ca Trọng tâm `SR-01` (Có đối chứng thực tế GPT-6.2 Instant)

| Nhóm / Lượt | Model / Cấu hình | Số từ | Từ / câu | Trùng 3-gram nguồn | Trùng 4-gram nguồn | Số cụm hành chính giữ lại\* | Gắn thêm mục "Điểm chưa xác định" | Gate 0 HF |
|---|---|---|---|---|---|---|---|---|
| **Group D (Chuẩn tham chiếu)** | **GPT-6.2 Instant (user cung cấp)** | **277** | **23,1** | **16,9%** | **10,9%** | **1** | Không | **Đạt (`0 HF`)** |
| Group A — Lượt 1 | Gemini 4 Neon mặc định | 341 | 34,1 | 49,1% | 40,2% | 8 | Không | Đạt (`0 HF`) |
| Group A — Lượt 2 | Gemini 4 Neon mặc định | 330 | 47,1 | 53,9% | 44,9% | 8 | Không | Đạt (`0 HF`) |
| Group B — Lượt 1 | Gemini + ViWrite v4.1 | 419 | 29,9 | 38,7% | 30,7% | 13 | **Có** | Đạt (`0 HF`) |
| Group B — Lượt 2 | Gemini + ViWrite v4.1 | 496 | 31,0 | 31,7% | 25,4% | 10 | **Có** | Đạt (`0 HF`) |
| Group B (`prior`) | Gemini + ViWrite v4.1 (user cung cấp) | 250 | 25,0 | 39,5% | 28,5% | 6 | Không | Đạt (`0 HF`) |
| **Group C — Lượt 1** | Gemini + ViWrite v4.1 + SR | 292 | 41,7 | 49,0% | 40,3% | 7 | Không | **Đạt (`0 HF`)** |
| **Group C — Lượt 2** | Gemini + ViWrite v4.1 + SR | 458 | 30,5 | 36,7% | 29,1% | 8 | **Có** | **Đạt (`0 HF`)** |

*\*Đếm các cụm hành chính/trừu tượng từ danh sách kiểm soát (như `thực hiện`, `tiến hành`, `gián đoạn cục bộ`, `tạm treo`, `tiên quyết`, `ưu tiên bất đồng bộ`, `tính tương thích`, `khuyến nghị`, `chuyển tiếp`). Lưu ý ở `Group B` Lượt 1–2 và `Group C` Lượt 2, tỷ lệ `%` 3-gram bị pha loãng do có thêm 100–170 từ phần `"Điểm chưa xác định"`; phần thân thông báo vẫn bám sát từ ngữ gốc.*

### B. Trung bình trên Toàn bộ 7 Tình huống (`SR-01`..`SR-07`, Lượt 1)

| Nhóm (`n = 7`) | Từ trung bình | Từ / câu TB | Trùng 3-gram nguồn TB | Trùng 4-gram nguồn TB | Tổng cụm hành chính | Gate 0 HF (cả Run 1 & Run 2) |
|---|---|---|---|---|---|---|
| **Group A** (Gemini mặc định) | 412,4 | 25,6 | 46,0% | 37,8% | 19 | `0/10` |
| **Group B** (Gemini + ViWrite v4.1) | 460,6 | 25,8 | 39,5% | 31,2% | 22 | `0/10` |
| **Group C** (Gemini + ViWrite v4.1 + SR) | **369,1** | 29,0 | 41,6% | 32,4% | **16** | `0/10` |

### C. Kiểm tra Độ Ổn định qua Chạy Lặp (`Run 1` vs `Run 2` trên `SR-01`, `SR-05`, `SR-06`)

- **`SR-05` (Business Rule) & `SR-06` (CSDL Failover):** Cả 3 nhóm **ổn định cao** giữa Run 1 và Run 2: giữ đủ 100% bất biến kỹ thuật/nghiệp vụ, không mắc `HF-3` hay `HF-6`, cấu trúc tương đồng (xê dịch độ dài & n-gram nhẹ `< 3%`–`5%`).
- **`SR-01` (Thông báo dịch vụ mơ hồ nhiều thuật ngữ hành chính):**
  - **Group A** ổn định theo hướng *bảo thủ*: cả 2 lượt đều chép sát ~50% cụm 3-gram nguồn và đều **không** gắn khối hỏi ngược.
  - **Group B** ổn định ở việc *gắn khối hỏi ngược* (2/2 lượt đều thêm mục `"Điểm bản gốc chưa nêu cụ thể"` dù đang viết thông báo cho người dùng cuối), nhưng tỷ lệ bám chữ vẫn cao.
  - **Group C dao động rõ rệt nhất ở `SR-01`:** Lượt 1 ra văn xuôi gọn `292` từ (không tiêu đề con, không khối hỏi ngược, nhưng trùng 3-gram `49,0%`); Lượt 2 lại chuyển sang bố cục đánh số + gắn khối `"Điểm chưa xác định"` dài `458` từ giống hệt Group B. Nguyên nhân: `Group C` đang nhận hai tín hiệu kéo về hai phía (`SKILL.md` kéo về *Trường hợp B* gắn danh sách điểm thiếu; *Semantic Reconstruction* kéo về viết lại trôi chảy cho người dùng cuối).

---

## 3. Phân tích Chuyên sâu theo 7 Tiêu chí Yêu cầu

### 3.1. Mức độ phụ thuộc vào cấu trúc văn bản nguồn
- **GPT-6.2 Instant (`SR-01` Group D):** Phá vỡ cấu trúc 3 đoạn rườm rà của nguồn tốt nhất. Câu mở đầu tóm gọn toàn bộ phạm vi thay đổi trong 1 câu (`cách quản lý phiên truy cập, gia hạn tự động và xử lý dữ liệu`), tách riêng hệ quả, tách riêng ngoại lệ và biến đoạn cuối thành hành động cụ thể (`bao gồm phương thức thanh toán đã liên kết`).
- **Gemini A & B:** Chủ yếu sửa cục bộ từng đoạn theo đúng thứ tự nguồn: đoạn 1 bỏ câu dẫn `"Trong bối cảnh..."`, đoạn 2 giữ nguyên cặp nguyên nhân–kết quả, đoạn 3 giữ nguyên `"Đồng thời..."` + `"Để đảm bảo..."`.
- **Gemini + SR (Group C):** Đã phá được khung câu ở các ca có cấu trúc rõ để gom lại:
  - Ở `SR-04` (`Idempotency Key`), Group C bỏ toàn bộ câu mở đầu mang tính định nghĩa giáo khoa dài dòng của A & B, mở thẳng bằng **tình huống sự cố người dùng gặp** (*"khi ứng dụng gửi yêu cầu thanh toán đi nhưng bị rớt mạng..."*) rồi mới kéo hai cơ chế vào giải quyết — tự nhiên hơn rõ rệt.
  - Ở `SR-07` (quy trình 4 đoạn CSKH/Kho), Group C cô đọng còn `363` từ (so với `425` ở A và `591` ở B), gom toàn bộ phân quyền & SLA vào một bảng đọc trong 10 giây.
  - Tuy nhiên ở `SR-01` (đoạn văn gốc nhiều cụm từ trừu tượng nhưng thiếu hành động cụ thể), Group C vẫn đi đúng thứ tự đoạn nguồn.

### 3.2. Khả năng nhận diện thông điệp chính
- Cả A, B, C, D đều nhận diện đúng 4 ý lõi của `SR-01`, 6 ý của `SR-03`, 5 ý của `SR-04` và các ngưỡng `< 500.000đ` / `>= 500.000đ` ở `SR-07`.
- Khác biệt nằm ở **tính phân cấp thông điệp**: ở `SR-01`, GPT-6.2 rút ra thông điệp cấp 1 ngay ở câu đầu (sắp đổi 3 thứ: *phiên truy cập, gia hạn tự động, dữ liệu tài khoản*) và nhấn vào *phương thức thanh toán* ở mục chuẩn bị; còn Gemini A/B/C vẫn lặp lại câu mở *"nâng cao chất lượng dịch vụ, trải nghiệm liền mạch, tối ưu giá trị lâu dài"* (cả `Group C Run 1` cũng giữ nguyên cụm sáo ngữ mở bài này dù Skill đã dặn cắt rào đón!).

### 3.3. Khả năng lựa chọn từ ngữ tiếng Việt tự nhiên
Đây là **khoảng cách lớn nhất** quan sát được trên `SR-01`:

| Cụm từ trong bản gốc (`SR-01`) | GPT-6.2 Instant (`Group D`) | Gemini + ViWrite v4.1 (`Group B`) | Gemini + ViWrite + SR (`Group C`) |
|---|---|---|---|
| `kể từ chu kỳ chuyển đổi sắp tới` | `Trong thời gian tới` | Giữ nguyên `từ chu kỳ chuyển đổi sắp tới` | Giữ nguyên `từ chu kỳ chuyển đổi sắp tới` |
| `mô hình xác thực đa tầng có điều kiện` | `cơ chế xác thực nhiều lớp dựa trên các điều kiện nhất định` | Giữ nguyên `xác thực đa tầng có điều kiện` | `xác thực đa tầng` (R1) / `nhiều lớp có điều kiện` (R2) |
| `đối soát định kỳ` | `kiểm tra định kỳ` | Giữ nguyên `đối soát định kỳ` | Giữ nguyên `đối soát định kỳ` |
| `gián đoạn cục bộ hoặc phát sinh trạng thái tạm treo` | `bị gián đoạn hoặc ... tạm thời không sử dụng được` | Giữ nguyên `gián đoạn cục bộ ... tạm treo` | Giữ nguyên `gián đoạn cục bộ ... tạm treo` |
| `các điều kiện tiên quyết` | `các điều kiện cần thiết` | Giữ nguyên `các điều kiện tiên quyết` | `các điều kiện yêu cầu` (R1) / `tiên quyết` (R2) |
| `tính tương thích của cấu hình hiện tại` | `các thiết lập tài khoản hiện tại, bao gồm phương thức thanh toán đã liên kết` | Giữ nguyên `tính tương thích của cấu hình hiện tại` | Giữ nguyên `tính tương thích của cấu hình hiện tại` |

Nhìn bảng đối chiếu trên có thể thấy: **GPT-6.2 thực hiện giải mã nghĩa (*semantic paraphrasing*)** biến từ Hán–Việt hành chính thành ngôn ngữ giao diện đời thường, trong khi Gemini (cả A, B lẫn C) hầu như **chép lại nguyên khối danh từ gốc**. Ở các ca có sẵn từ gốc rõ hơn (`SR-02`, `SR-03`, `SR-04`, `SR-06`), khoảng cách từ vựng giữa A, B, C thu hẹp lại rất nhiều.

### 3.4. Khả năng tổ chức lại thông tin theo nhu cầu người đọc
- Ở `SR-03` (Teams dời lịch release), cả B và C đều đảo quyết định `lùi sang 10:00 sáng thứ Hai` lên dòng đầu (tốt hơn bản gốc giấu ở giữa đoạn văn, và C còn gọn hơn B khi không lặp điều kiện blocker tới 2 lần).
- Ở `SR-05` (Business Rule hoàn tiền), cả 3 nhóm đều tách rạch ròi `Phạm vi -> BR-01 / BR-02 / BR-03 -> Điểm chưa xác định`, cho kết quả hữu ích ngang nhau cho BA/Dev.
- Tuy nhiên ở `SR-01` và `SR-07`, `Group B` tự động chèn thêm một **mục phê bình bản gốc (`Điểm chưa xác định`)** vào thẳng văn bản đầu ra dành cho người dùng cuối/nhân viên vận hành. Việc trộn *bản thảo gửi người đọc cuối* với *checklist phản biện dành cho tác giả* làm giảm tính khả dụng ngay (người dùng phải tự xóa đoạn cuối mới gửi đi được).

### 3.5. Khả năng diễn đạt tác động thực tế thay cho mô tả trừu tượng
- **GPT-6.2 (`SR-01`):** Biến mô tả hệ thống (`"các thiết lập liên quan đến phương thức thanh toán liên kết chưa đạt được trạng thái đồng bộ hóa đầy đủ"`, `"rà soát tính tương thích của cấu hình hiện tại"`) thành tác động người dùng dễ hình dung (`"tạm thời không sử dụng được"`, `"kiểm tra các thiết lập tài khoản hiện tại, bao gồm phương thức thanh toán đã liên kết"`).
- **Gemini C (`SR-01`):** Dù được yêu cầu ưu tiên diễn đạt tác động thực tế, vẫn viết `"kích hoạt lại quyền truy cập có thể bị gián đoạn cục bộ, hoặc một số tính năng nâng cao có thể bị tạm treo"`, người đọc phổ thông vẫn phải tự hỏi *"cục bộ là sao?"*, *"cấu hình hiện tại là chỗ nào?"*.
- Ngược lại ở `SR-06` (`Failover CSDL` — độc giả là kỹ sư SRE), `Group C` viết rất trúng tác động thực tế (`Mất dữ liệu đã commit (RPO > 0)`, `Rollback giao dịch chưa hoàn tất`, `Nguy cơ split-brain`) với giọng văn kỹ thuật sắc gọn.

### 3.6. Khả năng bảo toàn ý nghĩa, mức độ chắc chắn và chiều sâu chuyên môn
- **Không có đánh đổi an toàn:** `Group C` đạt **`0/10` Hard Fail** trên cả hai lượt chạy. Trên `SR-05` (cố ý thiếu ngày hoàn tiền và phí ship) và `SR-06` (`Primary`, `Replica`, `RPO > 0`, `rollback`, `split-brain`), `Group C` không hề tự bịa thông số hay đơn giản hóa sai cơ chế.
- **Một đánh đổi tinh tế cần chú ý ở GPT-6.2 (`SR-01` Group D):** GPT-6.2 viết mượt hơn một phần nhờ **nới nhẹ chi tiết nguồn** (`"chu kỳ chuyển đổi sắp tới"` → `"thời gian tới"`, lược chữ `"cục bộ"` trong `"gián đoạn cục bộ"`). Với thông báo người dùng cuối, sự giản lược này hợp lý và không sai bản chất; nhưng nếu áp dụng cùng thói quen đó vào Business Rule hay RFC kỹ thuật thì có thể làm mờ ranh giới quy định. Đây chính là lý do phải **tách ngữ cảnh viết thông báo/giao tiếp khỏi ngữ cảnh đặc tả hợp đồng/kỹ thuật**.

### 3.7. Những điểm trong ViWrite v4.1 vô tình khiến model quá dè dặt khi viết lại
Đối chiếu trực tiếp [`SKILL.md`](../../skills/vietnamese-human-readable-writing/SKILL.md) và [`vietnamese-clarity-and-style.md`](../../skills/vietnamese-human-readable-writing/references/vietnamese-clarity-and-style.md) giải thích chính xác vì sao `Group B` và `Group C` bị "khớp":

1. **Bất biến bảo toàn không phân biệt *thuật ngữ thật* vs *từ hành chính sáo rỗng*:** `SKILL.md` Mục 2.4 viết *"Giữ chính xác số liệu, đơn vị, mốc giờ, định danh/API/trạng thái..."* nhưng **chưa có câu nào cho phép thay thế cụm từ sáo rỗng bằng từ phổ thông khi đối tượng đọc là người dùng cuối**. Khi gặp từ lạ trong thông báo sản phẩm (`"tạm treo"`, `"đối soát định kỳ"`, `"giới hạn truy xuất thủ công"`), model không dám đổi sang `"tạm ngừng hoạt động"`, `"kiểm tra định kỳ"` vì sợ vi phạm quy tắc giữ thuật ngữ.
2. **Định nghĩa `Trường hợp B` đang kích hoạt quá rộng cho cả văn bản truyền thông:** `SKILL.md` Mục 2.2 yêu cầu dùng nhãn `Điểm chưa xác định / cần chốt` khi nguồn thiếu chi tiết, và không nói rõ: **khi người dùng yêu cầu viết lại một thông báo hoàn chỉnh (chỉ dặn "giữ nguyên mức độ bất định"), hãy giữ nguyên câu chữ ở mức độ khái quát của nguồn chứ KHÔNG tự nối thêm một báo cáo "Điểm bản gốc chưa nêu cụ thể" vào cuối văn bản thành phẩm**. (Nếu chỉ gắn thêm ghi chú ngắn chỉ khi có thiếu sót chặn việc hiểu hay làm ngay, hoặc đặt riêng khi được hỏi rà soát spec).
3. **Rule `Light Edit` và ví dụ sửa câu giữ nguyên khung cũ:** Trong `vietnamese-clarity-and-style.md`, bảng *"Chữa nhanh các mẫu câu phổ biến"* sửa câu ở cấp độ thay 2–3 từ trong cùng một khung câu (`"Phân hệ X cung cấp năng lực xử lý việc Y"` → `"Phân hệ X xử lý Y"`), khiến model mặc định nghĩ "biên tập rõ nghĩa = tỉa chữ trên bộ khung gốc" thay vì đọc hiểu hết rồi diễn đạt lại từ đầu.
4. **Cơ chế `references/` không tự kích hoạt trong thực tế trên tác vụ viết lại:** Cả 20/20 lượt chạy `Group B` & `Group C` đều có `refs_read = []` (kể cả `SR-05` và `SR-06`), cho thấy mọi thay đổi hành vi viết lại phải nằm **trực tiếp trong `SKILL.md`** mới có tác động ổn định.

---

## 4. Kết luận về Giả thuyết Semantic Reconstruction & Đề xuất Cải tiến Skill

### Kết luận giả thuyết
- **Semantic Reconstruction đi đúng hướng nhưng chưa đủ một mình:** Thêm khối hướng dẫn tái tạo thông điệp giúp Gemini **gọn hơn (`-11%` số từ vs A, `-20%` vs B), sắp xếp lại cấu trúc tốt hơn ở bài giải thích kỹ thuật & SOP (`SR-04`, `SR-07`), và an toàn (`0/10` HF)**.
- **Vì sao chưa thắng được thói quen bám câu nguồn ở `SR-01`?** Vì hai lý do đồng thời:
  1. Ở tầng **Skill**, phần lệnh *"giữ nguyên/bảo toàn/không tự điền"* ở nửa trên `SKILL.md` chi phối mạnh hơn đoạn Semantic Reconstruction ở nửa dưới, đồng thời không cho phép tường minh việc **dịch từ hành chính/Hán–Việt trừu tượng sang tiếng Việt thông dụng**.
  2. Ở tầng **Model**, Gemini 4 Neon mặc định (Group A) có thiên hướng bảo thủ giữ chữ nguồn cao hơn rõ rệt so với GPT-6.2 Instant (`~50%` vs `16,9%` trùng 3-gram).
  3. Ở tầng **Evaluation**, Gate 0 và `rubric-v2.md` cần tách tiêu chí **Bảo toàn dữ kiện cốt lõi (không bịa)** khỏi **Giải mã từ ngữ hành chính sang tác động đời thường** cho nhóm giao tiếp người dùng cuối, nếu không bản viết mượt kiểu GPT-6.2 sẽ bị phạt oan bằng `minor_notes`.

### Đề xuất thay đổi Skill có kiểm soát (Chỉ đề xuất — chưa áp dụng)

Trước khi thử nghiệm chỉnh sửa Skill tiếp theo, chỉ cần **3 thay đổi nhỏ, tách bạch** để đo tác động:

1. **Thêm quyền "Giải mã ngôn ngữ hành chính sang ngôn ngữ đời thường" theo đối tượng đọc (vào `SKILL.md` Mục 4.3):**
   - Phân biệt rõ: **Giữ nguyên** con số, ngày giờ, điều kiện/ngoại lệ và *thuật ngữ kỹ thuật chuyên ngành* (`API`, `RPO`, `rollback`, `Pinned Archive`); **Chủ động thay thế** cụm từ hành chính/trừu tượng nặng nề (`"đối soát định kỳ"`, `"trạng thái tạm treo"`, `"tính tương thích của cấu hình"`, `"tiên quyết"`) bằng cách nói tự nhiên tương đương ý cho người dùng cuối (`"kiểm tra định kỳ"`, `"tạm thời không dùng được"`, `"cài đặt hiện tại"`, `"cần thiết"`).
2. **Tách chế độ đầu ra khi viết lại cho người dùng cuối vs rà soát đặc tả (`SKILL.md` Mục 2.2):**
   - Khi người dùng yêu cầu viết lại thông báo/bài truyền thông hoàn chỉnh **và không yêu cầu rà soát lỗ hổng**, **không tự gắn mục `Điểm chưa xác định / cần chốt`** vào cuối văn bản thành phẩm; chỉ giữ nguyên độ bất định trong lời văn (trừ đặc tả BA/Dev như Business Rule, PRD, API Spec).
3. **Thay thế định hướng "sửa từng câu" bằng bước "tái tạo từ ý hiểu" trong Quy trình Tư duy (`SKILL.md` Mục 4.1–4.3):**
   - Với văn bản nguồn viết rối hoặc nặng dịch máy (**Trường hợp A** và văn bản truyền thông), tóm tắt ngầm 4 ý (*chuyện gì xảy ra → ai bị ảnh hưởng → ngoại lệ → cần làm gì*) rồi viết lại mạch văn từ đầu thay vì biên tập từng câu gốc.

---

## 5. Khuyến nghị Bước Tiếp theo cho Bạn

1. Mở [`human-blind-eval-pack.md`](./human-blind-eval-pack.md) để tự chấm cảm nhận đọc hiểu trên `Mẫu 1..4` (tất cả đã đảo ngẫu nhiên và ẩn tên nhóm).
2. Nếu muốn đối chiếu đầy đủ hơn với GPT-6.2 Instant ở các nhóm *Giao tiếp công việc, Giải thích khái niệm, Business Rule, Tài liệu kỹ thuật*, chạy thêm 6 prompt có sẵn trong [`prompts-for-gpt62.md`](./prompts-for-gpt62.md) và gửi lại output thực tế.
3. Sau khi có kết quả chấm tay của bạn (đặc biệt để kiểm chứng xem `Mẫu 1` vs `Mẫu 2/3/4` ở `SR-01` và sự khác biệt giữa A/B/C ở `SR-02..SR-07` khớp cảm nhận thực tế tới đâu), mới chốt thiết kế vòng thử nghiệm tiếp theo cho Skill.
