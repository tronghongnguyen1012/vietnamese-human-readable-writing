# Kiến trúc Thông tin và Thích ứng Người đọc

Dùng tài liệu này khi trình bày bài giải thích khái niệm, phân tích vấn đề, đề xuất giải pháp, báo cáo sự cố, email quan trọng hoặc tài liệu hướng dẫn/đào tạo.

---

## 1. Cấu trúc Đưa Trọng tâm lên Đầu (BLUF / Pyramid)

- **Phân tích vấn đề & Báo cáo sự cố:** Câu/đoạn đầu tiên phải trả lời ngay: *Chuyện gì đang xảy ra, tác động bao nhiêu, nguyên nhân khả dĩ chính là gì?* Sau đó mới đi vào phân rã nguyên nhân và phương án xử lý theo thứ tự ưu tiên (Ngắn hạn/Cấp cứu → Dài hạn/Phòng ngừa).
- **Email & Giao tiếp công việc:**
  - *Tiêu đề:* Nêu thẳng hành động/chủ đề + mốc thời gian (ví dụ: `[Đề xuất dời lịch] Xuất hóa đơn tự động sang 02/12`).
  - *Đoạn mở đầu:* 1–2 câu nêu ngay đề xuất/quyết định cần phê duyệt, rồi mới đến lý do ngắn gọn và cam kết phạm vi ảnh hưởng. Bỏ đoạn hỏi thăm/rào đón chung chung.
- **Hướng dẫn thao tác (How-to / Runbook):**
  - Thứ tự bắt buộc: **(1) Phạm vi & Điều kiện tiên quyết** → **(2) Cảnh báo không thể hoàn tác / Việc cấm làm** → **(3) Từng bước thực hiện đánh số** → **(4) Cách kiểm tra kết quả**.

---

## 2. Tách 4 Chế độ Tài liệu (Diátaxis)

Không trộn các mục đích sau trong cùng một khối văn bản:
- **Giải thích (Explanation):** Giúp hiểu *tại sao* và *bản chất khác biệt* (dùng tương tự đời thực nếu người đọc không chuyên; dùng cơ chế và đánh đổi nếu người đọc là chuyên gia).
- **Hướng dẫn theo mục tiêu (How-to / Runbook):** Giúp hoàn thành việc ngay — chỉ giữ bước làm, điều kiện rẽ nhánh và cảnh báo lỗi; cắt bỏ phần giảng lý thuyết nền.
- **Đào tạo người mới (Tutorial / Onboarding):** Dẫn theo lộ trình từng bước kèm mốc giải thích ngắn *vì sao cần bước đó* và lỗi hay đụng ngày đầu.
- **Tra cứu (Reference):** Bảng thông số, mã lỗi, quy tắc ngắn gọn, đồng nhất.

---

## 3. Thích ứng theo Trình độ Người đọc (Chống Expertise Reversal)

| Đối tượng | Cách viết phù hợp | Lỗi cần tránh |
|---|---|---|
| **Chuyên gia / Kỹ sư có kinh nghiệm** | Đi thẳng vào cơ chế nội tại, điều kiện biên, điểm đánh đổi (*trade-off*), lệnh/chỉ số kiểm chứng thực tế. | Giảng lại khái niệm nền (*API là gì, transaction là gì*), viết giáo trình dài dòng lặp lại ý ở phần kết. |
| **PM / Vận hành / CSKH / Chủ shop** | Giữ thuật ngữ cần thiết nhưng giải thích theo **tác động nghiệp vụ và trải nghiệm thực tế**; dùng bảng so sánh khi cần ra quyết định nhanh. | Ném thuật ngữ hạ tầng sâu (*WAL, MVCC, Redis ZSET TTL*) không gắn với tình huống công việc của họ. |
| **Người đọc hỗn hợp** | Đặt tóm tắt điều hành/checklist 5 dòng lên đầu cho người đã biết; đặt giải thích nền vào mục phụ bên dưới. | Bắt người đã rành phải đọc qua 2 trang định nghĩa mới thấy bước hành động. |

---

## 4. Chọn Hình thức Trình bày Theo Chức năng

- **Văn xuôi ngắn (2–5 câu):** Dùng cho câu trả lời chat đơn giản, kết nối lập luận nguyên nhân–hệ quả gồm 1–2 ý chính.
- **Danh sách đánh số (`1, 2, 3`):** Dùng cho chuỗi thao tác tuần tự theo thời gian hoặc các bước ưu tiên phải làm theo thứ tự.
- **Danh sách gạch đầu dòng (`-`):** Dùng cho các điều kiện song song, trường hợp rẽ nhánh hoặc hành động ngang hàng (giữ mỗi dòng ngắn gọn, 1 ý rõ ràng).
- **Bảng biểu:** Dùng khi so sánh từ 2–3 đối tượng/trạng thái trên nhiều tiêu chí (ví dụ: *Hủy đơn vs Hoàn trả*, *Phân quyền duyệt chi theo hạn mức*, *Ma trận HTTP Status*).
- **Chống lặp giữa bảng và văn bản:** Khi bảng đã tóm tắt đủ các mốc điều kiện, thời gian hoặc tác động, phần văn xuôi/mục bên dưới **chỉ nêu quy trình thao tác hoặc ngoại lệ chưa có trong bảng** — tuyệt đối không lặp lại cùng nội dung vừa đặt trong bảng.
- **Chống lặp nhãn trong danh sách:** Khi dùng gạch đầu dòng có nhãn in đậm (`- **Nhãn:** Nội dung`), không lặp lại các từ của nhãn vào đầu câu nội dung phía sau.

---

## 5. Trung thực Dữ kiện khi Phân tích Vấn đề

- Phân biệt rạch ròi giữa **Sự kiện đã quan sát trong đề bài** (số liệu log, triệu chứng) và **Giả thuyết nguyên nhân / Đề xuất cần kiểm chứng**.
- Không tự gán nguyên nhân chưa xác minh thành khẳng định chắc chắn; kèm câu lệnh hoặc bước kiểm tra để xác nhận giả thuyết trước khi sửa diện rộng.
- Không bịa thêm số liệu benchmark hoặc con số cam kết ngoài dữ liệu đầu vào.
