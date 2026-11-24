# Quy trình Đánh giá trên Người đọc Thực tế (Human Evaluation Protocol)

**Trạng thái hiện tại:** Đã thiết kế quy trình chuẩn để triển khai kiểm chứng độc lập, **CHƯA thực thi** trong phạm vi dự án hiện tại vì không sử dụng dịch vụ tuyển người tham gia hay hạ tầng thu thập dữ liệu ngoài. Mọi báo cáo kết quả hiện tại không được phép tuyên bố đã hoàn tất human evaluation.

---

## 1. Mục tiêu Kiểm chứng

Kiểm chứng trực tiếp trên người đọc bản ngữ tiếng Việt có chuyên môn phù hợp 4 chỉ số mà LLM Judge không thể đo trực tiếp:
1. **Độ hiểu đúng thực tế** (*Accuracy-Gated Comprehension* — không mắc *Subconscious Disambiguation*).
2. **Time to Correct Understanding (TtCU)** — thời gian đọc và trả lời đúng các câu hỏi ứng dụng/ngoại lệ.
3. **Công sức nhận thức chủ quan** (*Paas 9-point Mental Effort Scale*).
4. **Mức độ cần chỉnh sửa & sẵn sàng sử dụng trong công việc** (*Edit-to-Use* & *Readiness-to-Use*).

---

## 2. Thiết kế Thí nghiệm (Blind Within-Subjects Latin Square)

- **Người tham gia mục tiêu:** Tối thiểu 12–16 người Việt làm việc chuyên môn thật (chia nhóm tương ứng loại tài liệu: BA/PM cho `business_docs`, Kỹ sư phần mềm cho `technical_docs`, nhân sự văn phòng/vận hành cho `workplace_communication` và `reports_guides_training`).
- **Làm mù hoàn toàn (Double-Blind):** Không hiển thị nhãn `Baseline` hay `Experiment`; ký hiệu mẫu là `Phiên bản M` và `Phiên bản N`.
- **Phân phối Latin Square:** Mỗi người tham gia đọc một nửa số bài ở bản Baseline và nửa còn lại ở bản Experiment (chỉ đọc **1 phiên bản** cho mỗi đầu vào gốc nhằm loại bỏ hiệu ứng học thuộc khi đọc lại cùng nội dung hai lần). Thứ tự trình bày các ngữ cảnh được xáo ngẫu nhiên.

---

## 3. Quy trình Đo cho Mỗi Mẫu Thử

Với mỗi bài kiểm thử:
1. **Bước 1 — Đọc và bấm giờ (`Reading Time`):** Người tham gia đọc văn bản ở tốc độ tự nhiên để phục vụ công việc rồi bấm "Đã đọc xong". Ghi lại `T_read` (giây). Cho phép xem lại văn bản ở Bước 2 nếu là tài liệu tra cứu (ghi nhận tách biệt `T_read_only` và `T_total_with_lookup`).
2. **Bước 2 — Cổng Kiểm tra Hiểu đúng (3 câu hỏi tình huống):**
   - Không hỏi câu nhớ mặt chữ (như *"Câu đầu tiên nói gì?"*).
   - Hỏi 3 câu dựa trên **Situation Model** và **điều kiện biên** (ví dụ: *"Nếu đơn hàng 350.000đ, nặng 16 kg và khách hàng là hạng Vàng thì phí ship tính thế nào?"*).
   - Tính `T_answer` đến khi hoàn tất trả lời.
   - **Ngưỡng vượt cổng (*Comprehension Gate*):** Đạt tối thiểu **2/3 câu đúng** (và đúng 100% ở câu hỏi điều kiện cốt lõi).
3. **Bước 3 — Tự đánh giá Tải nhận thức & Tính khả dụng:**
   - **Paas Mental Effort Scale (1–9):** *"Bạn đã tốn bao nhiêu công sức trí óc để đọc và hiểu đúng văn bản này?"* (`1 = Cực kỳ ít công sức` ... `9 = Cực kỳ tốn công sức`).
   - **Mức cần chỉnh sửa trước khi dùng thực tế (1–4):**
     - `1`: Dùng ngay được, không cần sửa.
     - `2`: Sửa nhẹ câu chữ (< 20% nội dung).
     - `3`: Phải cấu trúc lại hoặc hỏi thêm thông tin.
     - `4`: Không thể dùng, phải viết lại từ đầu.
   - **Mức độ sẵn sàng đọc và áp dụng (1–5):** Từ `1 (Không muốn đọc/không tin dùng)` đến `5 (Sẵn sàng áp dụng ngay)`.

---

## 4. Chỉ số Tổng hợp Báo cáo

- **Tỷ lệ vượt cổng hiểu đúng (*Comprehension Pass Rate*):** So sánh trực tiếp `% Pass` giữa Baseline và Experiment (kiểm định McNemar hoặc Fisher exact nếu mẫu nhỏ).
- **Tỷ số TtCU ghép cặp (*Paired TtCU Ratio*):** Chỉ tính trên các bài đạt Comprehension Gate:
  $$\text{TtCU Ratio} = \frac{\text{Median}(\text{TtCU}_{\text{Experiment}})}{\text{Median}(\text{TtCU}_{\text{Baseline}})}$$
  Giá trị `< 1.0` đồng thời Comprehension Pass Rate không giảm nghĩa là Skill thực sự giảm thời gian để hiểu đúng.
- **Chênh lệch Paas Mental Effort & Edit-to-Use Score:** Đánh giá qua Wilcoxon signed-rank test trên cặp mẫu cùng đầu vào.

---

## 5. Giới hạn Nhận thức khi Chưa Thực thi Tầng Này

Khi chưa chạy quy trình trên người Việt thật, mọi kết luận từ LLM Judge ở Tầng 2 chỉ chứng minh được **sự tuân thủ tiêu chí phân tích văn bản** và **giảm lỗi cấu trúc/ngữ nghĩa có thể quan sát được**; chưa đủ cơ sở để khẳng định định lượng mức giảm TtCU (tính bằng giây) trong môi trường làm việc thực tế.
