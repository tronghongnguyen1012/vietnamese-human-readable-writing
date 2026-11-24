# Khung và Tiêu chí Đánh giá Chất lượng (Evaluation Rubric)

Khung đánh giá này được thiết kế **độc lập hoàn toàn với hướng dẫn của Skill**, không dùng nhận xét cảm tính (*"hay hơn"*, *"mượt hơn"*, *"chuyên nghiệp hơn"*), và áp dụng cơ chế **phi bù trừ (non-compensatory)**: điểm văn phong cao tuyệt đối không thể bù đắp cho lỗi sai nghĩa, sai dữ kiện hoặc thiếu điều kiện nghiệp vụ.

---

## 1. Phản biện Chỉ số Time to Correct Understanding (TtCU) và Kiến trúc 2 Tầng

### 1.1 Giá trị của TtCU
**Time to Correct Understanding (TtCU)** là thời gian tính từ lúc người đọc bắt đầu tiếp nhận văn bản đến khi họ trả lời đúng các câu hỏi kiểm tra bản chất nghiệp vụ/kỹ thuật hoặc thực hiện đúng thao tác mục tiêu. Chỉ số này phản ánh trực tiếp mục tiêu cốt lõi của dự án: giảm công sức con người bỏ ra để hiểu đúng thông tin.

### 1.2 Ba hạn chế nếu dùng TtCU như chỉ số đơn lẻ
1. **Nhiễu theo độ phức tạp nội tại (*Intrinsic Load*) và độ dài:** Một đặc tả API phức tạp đương nhiên cần thời gian đọc lâu hơn một câu chat ngắn, kể cả khi viết rất tốt. So sánh TtCU thô giữa các bài khác nhau là vô nghĩa nếu không ghép cặp trên cùng một đầu vào gốc.
2. **Bẫy "Ảo giác dễ hiểu" (*Illusion of Understanding* & *Subconscious Disambiguation*):** Một văn bản ngắn, đọc rất lướt nhưng mập mờ hoặc cắt mất ngoại lệ sẽ cho thời gian đọc nhanh hơn, nhưng người đọc hiểu sai hoàn toàn (Berry et al., 2003). Thời gian đọc nhanh mà hiểu sai có giá trị âm.
3. **Không thể đo trực tiếp bằng LLM:** LLM không có bộ nhớ làm việc sinh học của con người; mọi đánh giá tự động chỉ đo được *ước lượng phân tích* (analytical proxy), không phải TtCU thật.

### 1.3 Giải pháp: Kiến trúc Đánh giá 2 Tầng

- **Tầng 1 — Chuẩn vàng Đánh giá trên Con người (*Accuracy-Gated Comprehension Efficiency*):**
  - *Cổng bắt buộc:* Người tham gia phải đạt ngưỡng hiểu đúng tình huống (Comprehension Gate ≥ 2/3 câu hỏi ứng dụng/ngoại lệ) trước khi tính thời gian. Bản đọc nhanh nhưng rớt cổng hiểu đúng bị xếp loại **Thất bại đọc hiểu**.
  - *Chỉ số hiệu quả ghép cặp:* $\text{TtCU Ratio} = \text{TtCU}_{\text{Experiment}} / \text{TtCU}_{\text{Baseline}}$ trên cùng một bài toán gốc, kết hợp thang đo nỗ lực nhận thức 9 mức (Paas Cognitive Load Scale) và mức cần chỉnh sửa trước khi dùng (xem chi tiết tại [human-eval-protocol.md](./human-eval-protocol.md)).
- **Tầng 2 — Chuẩn Phân tích Tự động / Chuyên gia (*Non-Compensatory MQM + Blind Rubric*):**
  - Dùng để chấm có đối chứng trong quá trình phát triển và kiểm thử LLM khi chưa thực hiện thí nghiệm người dùng thực tế, gồm: **Gate 0 (Hard Fail)** → **9 Tiêu chí neo hành vi (thang 0–4)** → **Gắn nhãn lỗi theo Error Taxonomy & MQM Severity** → **So sánh mù hoán đổi vị trí A/B**.

---

## 2. Gate 0 — Các Lỗi Hard Fail (Không Bù Trừ)

Trước khi tính bất kỳ điểm chất lượng nào, phải đối chiếu từng đầu ra với `input` và danh sách `must_preserve` của test case. Nếu vi phạm **bất kỳ** lỗi nào dưới đây → gán nhãn **`HARD_FAIL`** ngay lập tức:

| Mã | Tên lỗi Hard Fail | Định nghĩa nhận diện khách quan |
|---|---|---|
| `HF-1` | **Làm sai ý nghĩa** | Đảo ngược, bóp méo hoặc làm sai lệch thông điệp chính hay quan hệ nhân–quả của nguồn. |
| `HF-2` | **Làm sai dữ kiện / số liệu** | Sai lệch con số, đơn vị, mốc thời gian, tên API/biến/trạng thái, định danh hoặc đối tượng áp dụng. |
| `HF-3` | **Tự bổ sung thông tin không có căn cứ** | Tự bịa thêm quy tắc nghiệp vụ, số liệu giả định, tham số kỹ thuật hoặc cam kết không có trong đề bài / không được đánh dấu rõ là ví dụ hoặc giả định đề xuất. |
| `HF-4` | **Thay đổi logic nghiệp vụ / mức bắt buộc** | Đổi `và` ↔ `hoặc`, đổi `phải` (mandatory) ↔ `nên`/`có thể` (optional), đảo điều kiện kích hoạt hoặc phạm vi loại trừ. |
| `HF-5` | **Làm mất điều kiện xử lý quan trọng** | Bỏ sót điều kiện biên, ngoại lệ, cảnh báo an toàn không thể hoàn tác hoặc dữ kiện trong `must_preserve`. |
| `HF-6` | **Đơn giản hóa đến mức gây hiểu nhầm** | Rút gọn quá mức khiến người đọc hiểu sai bản chất cơ chế kỹ thuật hoặc hiểu quy tắc cục bộ thành quy tắc toàn phần. |

**Quy tắc xử lý Hard Fail:**
- Trong so sánh cặp A/B: một đầu ra **không** Hard Fail mặc định thắng một đầu ra bị Hard Fail (trừ khi cả hai đều Hard Fail, khi đó chấm hòa thua hoặc bên ít lỗi nghiêm trọng hơn và ghi rõ cả hai không đạt).
- Đầu ra có điểm văn phong 4/4 nhưng dính `HF-1..HF-6` vẫn bị kết luận **KHÔNG ĐẠT**.

---

## 3. Bộ 9 Tiêu chí Chấm điểm Neo Hành vi (Thang 0–4)

Mọi điểm số dưới **4** BẮT BUỘC phải kèm trích dẫn đoạn lỗi thực tế, mã lỗi trong [error-taxonomy.md](../research/error-taxonomy.md) (`S-01`..`R-04`) và mức độ MQM (`Minor` / `Major` / `Critical`).

### Nhóm A: Trung thực Nội dung & Dữ kiện (Nhóm Cổng Chất lượng)

#### `D1`: Semantic Accuracy (Độ chính xác ngữ nghĩa)
- **4:** Giữ đúng 100% ý nghĩa gốc, quan hệ logic, mức độ bắt buộc và dữ kiện; không sai sót dù nhỏ.
- **3:** Ý chính và dữ kiện cốt lõi đúng, nhưng có 1 chi tiết phụ hơi lệch sắc thái (*Minor*), không ảnh hưởng quyết định hoặc thực thi.
- **2:** Có 1–2 chỗ diễn đạt gây hiểu nhầm quan hệ giữa các ý hoặc làm mờ mức bắt buộc (*Major*).
- **1:** Sai lệch rõ rệt nhiều mệnh đề quan trọng hoặc xuyên tạc mục tiêu gốc.
- **0:** Sai hoàn toàn ý nghĩa nguồn hoặc vi phạm Hard Fail `HF-1`/`HF-2`/`HF-3`/`HF-4`.

#### `D2`: Completeness (Độ đầy đủ thông tin cần thiết)
- **4:** Bảo toàn 100% ý nghĩa/dữ kiện trong `must_preserve` và đủ thông tin để đạt mục đích truyền tải mà không thiếu ngữ cảnh hay điều kiện biên.
- **3:** Đủ toàn bộ `must_preserve` cốt lõi, nhưng thiếu 1 ngữ cảnh phụ hoặc giả định nhỏ khiến người đọc phải suy đoán nhẹ (*Minor*).
- **2:** Thiếu ít nhất 1 thông tin hữu ích quan trọng hoặc bỏ qua 1 trường hợp biên cần thiết (*Major*).
- **1:** Thiếu nhiều phần cốt lõi, người đọc không thể dùng được nếu không hỏi lại.
- **0:** Bỏ sót điều kiện/dữ kiện bắt buộc thuộc Hard Fail `HF-5`.

#### `D3`: Terminology Consistency (Độ chính xác và nhất quán thuật ngữ)
- **4:** Dùng đúng thuật ngữ chuyên ngành theo ngữ cảnh và đối tượng đọc (giữ nguyên thuật ngữ Anh phổ biến khi cần, chú thích hợp lý nếu người đọc rộng); 1 khái niệm = 1 tên gọi xuyên suốt.
- **3:** Thuật ngữ đúng nhưng có 1 chỗ dùng chưa thật đồng nhất hoặc giải thích hơi thừa/hơi thiếu cho đối tượng (*Minor*).
- **2:** Dịch cưỡng ép gây khó nhận diện khái niệm gốc (`S-06`), hoặc dùng 2–3 tên gọi khác nhau cho cùng một thực thể gây nghi ngờ là đối tượng khác (*Major*).
- **1:** Nhầm lẫn thuật ngữ kỹ thuật/nghiệp vụ cốt lõi gây hiểu sai khái niệm.
- **0:** Dùng sai thuật ngữ nghiêm trọng dẫn tới sai bản chất kỹ thuật/nghiệp vụ.

---

### Nhóm B: Rõ Nghĩa & Giảm Tải Nhận thức

#### `D4`: Semantic Clarity (Độ rõ ràng ngữ nghĩa)
- **4:** Tác thể, hành động, đối tượng và phạm vi điều kiện hiện rõ ngay ở lần đọc đầu; không phải tự đặt dấu ngoặc logic hay giải mã câu chồng chéo danh từ hóa (`S-01`..`S-03`).
- **3:** Phần lớn câu rõ nghĩa, còn tối đa 1–2 câu hơi nặng danh từ hóa hoặc hơi trừu tượng nhưng vẫn đoán đúng được từ ngữ cảnh (*Minor*).
- **2:** Nhiều câu ẩn tác thể, danh từ hóa nhiều lớp hoặc chứa mơ hồ phạm vi `và/hoặc`, mơ hồ quy chiếu buộc người đọc phải đọc lại (*Major*).
- **1:** Đọc đúng ngữ pháp bề mặt nhưng người hiểu lĩnh vực vẫn không xác định được hệ thống/ai làm gì trong điều kiện nào.
- **0:** Mơ hồ nghiêm trọng hoặc rút gọn gây hiểu nhầm thành `HF-6`.

#### `D5`: Coherence (Tính mạch lạc và trình tự tiếp nhận)
- **4:** Đi thẳng vào trọng tâm phù hợp mục đích (BLUF/Pyramid khi cần); trình tự thông tin thuận logic tiếp nhận (điều kiện/cảnh báo đặt trước bước làm); chuỗi Đề–Thuyết liền mạch, từ nối dùng đúng quan hệ logic.
- **3:** Trình tự tổng thể hợp lý, có 1 đoạn chuyển ý hơi gượng hoặc 1 câu mở rào đón nhẹ chưa thực sự cần thiết (*Minor*).
- **2:** Chôn vùi ý chính dưới mở bài dài (`P-01`), đảo lộn điều kiện tiên quyết xuống cuối (`D-02`), hoặc dùng từ nối giả/nhảy tiêu điểm liên tục (`P-02`, `P-03`) (*Major*).
- **1:** Ý rời rạc, trộn lẫn chế độ tài liệu (`D-01`), người đọc phải tự ghép lại cấu trúc.
- **0:** Rối loạn trình tự nghiêm trọng, các phần mâu thuẫn hoặc đứt gãy hoàn toàn.

#### `D6`: Information Density (Mật độ thông tin hữu ích trên độ dài)
- **4:** Mọi câu và phần cấu trúc đều đóng góp giá trị thông tin hoặc giúp định hướng tiếp nhận phù hợp trình độ người đọc; không có rào đón sáo rỗng, lặp diễn giải hay giải thích sơ đẳng thừa.
- **3:** Thông tin gọn và có ích, còn khoảng ≤ 10–15% chữ đệm nhẹ hoặc câu kết tóm tắt hơi thừa (*Minor*).
- **2:** Dài dòng rõ rệt do lặp ý (`P-04`), mở/kết bài sáo rỗng, mỹ từ rỗng (`S-05`) hoặc giải thích quá sơ đẳng với chuyên gia (`R-01`) (*Major*).
- **1:** Lượng thông tin thật quá thấp so với độ dài; người đọc mất nhiều công lọc chữ mới nhặt được vài dữ kiện.
- **0:** Hầu hết là chữ đệm hình thức, gần như không truyền tải thông tin thực chất.

---

### Nhóm C: Tự nhiên Tiếng Việt & Khả dụng Thực tế

#### `D7`: Naturalness (Độ tự nhiên của văn phong tiếng Việt)
- **4:** Đọc tự nhiên như người Việt chuyên môn giao tiếp/viết tài liệu chuẩn mực: cấu trúc Đề–Thuyết trôi chảy, chọn đúng *"được/bị"* hoặc câu chủ động, không lộ dấu vết dịch sát từ tiếng Anh hay khuôn mẫu "văn AI".
- **3:** Tự nhiên ở mức đọc tốt, còn 1–2 vết nhẹ kiểu dịch sát hoặc nhịp từ nối hơi quen tay của AI (*Minor*).
- **2:** Mang rõ dấu vết cú pháp tiếng Anh (*"được ... bởi"*, *"một cách [Adj]"*, *"những cái mà"*) hoặc công thức danh từ hóa hành chính dày đặc (`S-01`, `S-04`) (*Major*).
- **1:** Văn dịch máy nặng nề, ngắt nhịp gượng gạo xuyên suốt văn bản.
- **0:** Câu tiếng Việt sai cấu trúc hoặc không thể đọc trôi chảy như tiếng Việt tự nhiên.

#### `D8`: Context Appropriateness (Sự phù hợp ngữ cảnh và đối tượng)
- **4:** Văn phong, mức độ trang trọng, độ chi tiết và định dạng (văn xuôi vs danh sách vs bảng) khớp hoàn toàn với mục đích, ngữ cảnh (chat hằng ngày vs tài liệu spec) và trình độ người đọc; không lộ quy trình kiểm tra nội bộ của AI.
- **3:** Nhìn chung phù hợp, có 1 điểm lệch nhẹ về định dạng hoặc sắc thái hơi cứng/hơi suồng sã (*Minor*).
- **2:** Lệch rõ ngữ cảnh: biến chat thường ngày thành báo cáo nhiều heading (`D-04`, `R-02`), hoặc dùng giọng hội thoại thiếu chuẩn mực trong đặc tả chính thức, hoặc vi phạm rõ *Expertise Reversal* (`R-01`) (*Major*).
- **1:** Hoàn toàn sai đối tượng/ngữ cảnh (ví dụ viết spec kỹ thuật thành bài quảng cáo marketing).
- **0:** Định dạng và văn phong phá hỏng hoàn toàn mục đích giao tiếp ban đầu.

#### `D9`: Actionability (Tính khả dụng để thực hiện công việc)
*(Chỉ chấm khi test case có `actionability_applicable == true`. Nếu `false` — ví dụ hội thoại giải thích thuần túy hoặc hỏi đáp khái niệm — ghi `N/A` / `null` và không đưa vào mẫu số).*
- **4:** Người đọc thực hiện được ngay mục tiêu công việc (code/test được AC, chạy được bước xử lý sự cố, ra được quyết định hoặc biên tập xong để dùng ngay) mà không cần hỏi lại các ngưỡng hay tác thể cơ bản.
- **3:** Dùng được ngay cho phần lớn công việc, chỉ cần tự làm rõ 1 chi tiết vận hành thứ yếu (*Minor*).
- **2:** Hiểu đại ý nhưng thiếu ngưỡng kiểm chứng, thiếu tác thể chịu trách nhiệm hoặc thiếu bước thực hiện cụ thể khiến chưa thể áp dụng ngay (`R-03`) (*Major*).
- **1:** Quá chung chung, chỉ dừng ở khuyến nghị khẩu hiệu, không thể triển khai hay kiểm thử.
- **0:** Gây hành động sai hoặc tê liệt khả năng thực thi.

---

## 4. Quy tắc Tổng hợp Phi bù trừ & Gắn nhãn MQM

1. **Phân loại mức lỗi MQM (dùng để trích dẫn giải trình):**
   - **Minor:** Gây gượng nhẹ hoặc tốn thêm ít công đọc, không ảnh hưởng nghĩa và khả năng dùng.
   - **Major:** Bắt buộc người đọc phải đọc lại, tự diễn giải lại hoặc phải hỏi thêm mới dùng được; hoặc sai lệch văn phong/cấu trúc đáng kể.
   - **Critical:** Làm sai/mất dữ kiện, điều kiện nghiệp vụ, logic bắt buộc hoặc dẫn tới hành động sai (tương ứng các lỗi Hard Fail).
2. **Xếp hạng đầu ra đơn lẻ (Outcome Tier):**
   - Có bất kỳ `HF-1..HF-6` → **`HARD_FAIL` (Không đạt tuyệt đối)**.
   - Không Hard Fail, nhưng `D1 < 3` hoặc `D2 < 3` hoặc có tiêu chí khác `<= 1` → **`NEEDS_REVISION` (Không đạt chuẩn sử dụng ngay)** — bất kể `D7` (Naturalness) đạt 4/4.
   - Mọi tiêu chí áp dụng `>= 3` và trung bình nhóm B–C `>= 3.25` → **`PASS_USABLE` (Đạt chuẩn sử dụng thực tế)**.
3. **Quy tắc quyết định thắng thua khi so sánh mù A/B:**
   - So **Gate 0 (Hard Fail)** trước tiên.
   - Nếu cả hai đều qua Gate 0, ưu tiên nhóm **Trung thực & Rõ nghĩa (`D1, D2, D4, D5`)** và **Tính phù hợp ngữ cảnh / Khả dụng (`D8, D9`)** cao hơn nhóm **Hình thức bề mặt**; điểm văn phong (`D7`) cao không bù cho bất kỳ suy giảm nào ở `D1` hoặc `D2`.
   - Phải chỉ ra **bằng chứng câu chữ cụ thể** nếu chấm một bản thắng; nếu chênh lệch không rõ ràng hoặc mỗi bản mạnh một chiều ngang nhau, chọn **`TIE`**.
