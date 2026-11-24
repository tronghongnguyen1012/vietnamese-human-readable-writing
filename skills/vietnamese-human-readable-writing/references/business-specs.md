# Chuẩn Viết Tài liệu Nghiệp vụ (PRD, BRD, User Story, AC, Business Rule)

Dùng tài liệu này ở chế độ **Chặt** khi soạn hoặc chuẩn hóa tài liệu nghiệp vụ để BA, Product, Dev và QA đọc hiểu thống nhất và triển khai/kiểm thử được ngay.

---

## 1. Nguyên tắc Cốt lõi của Đặc tả Nghiệp vụ

Một tài liệu nghiệp vụ đạt chuẩn (ISO/IEC/IEEE 29148) phải đạt đồng thời 4 tính chất:
1. **Đơn nghĩa (Unambiguous):** Mọi người đọc (PO, Dev, QA) chỉ suy ra **một** cách hiểu duy nhất về logic và biên giá trị.
2. **Kiểm chứng được (Verifiable):** QA viết được test case Pass/Fail ngay từ tài liệu, không dùng tính từ mơ hồ (*"nhanh", "phù hợp", "hợp lý", "nhiều lần"* nếu đề đã cho ngưỡng hoặc thiếu ngưỡng).
3. **Đầy đủ (Complete):** Không rơi điều kiện kích hoạt, phạm vi loại trừ, xử lý lỗi hay chuyển đổi trạng thái.
4. **Nhất quán (Consistent):** Một khái niệm nghiệp vụ giữ đúng một tên gọi xuyên suốt (`đơn hàng` không tự đổi thành `phiếu đặt`; giữ nguyên tên trạng thái hệ thống như `PARTIAL_PAID`).

---

## 2. Cấu trúc Khuyến nghị (Gọn, Không Bịa Thêm Luật)

Tùy yêu cầu đầu vào, sắp xếp rõ theo các khối sau:

1. **Phạm vi áp dụng (Scope):**
   - Tách rõ **Áp dụng (In-Scope)** và **Không áp dụng (Out-of-Scope)** nếu có ranh giới giai đoạn hoặc kênh (ví dụ: chỉ tại quầy POS, chưa hỗ trợ ngoại tệ ở Phase 1).
2. **Quy tắc nghiệp vụ (Business Rules — `BR-01, BR-02...`):**
   - Mỗi quy tắc viết ngắn gọn, rõ **Chủ thể / Điều kiện kích hoạt → Hành vi hệ thống / Giới hạn**.
   - Với phân cấp hạn mức hoặc điều kiện đa nhánh (ví dụ hạn mức duyệt chi `< 10 triệu`, `10–50 triệu`, `> 50 triệu`), trình bày bằng **bảng** hoặc gạch đầu dòng phân tầng để lộ rõ từng dấu `<`, `<=`, `>`.
   - Khóa chặt mức bắt buộc bằng từ khóa rõ ràng:
     - **Phải / Bắt buộc / Từ chối / Chặn:** Hành vi bắt buộc của hệ thống.
     - **Không áp dụng / Ngoại trừ:** Điều kiện loại trừ.
     - **Được phép / Có thể:** Quyền lựa chọn hợp lệ.
3. **User Story & Tiêu chí Chấp nhận (Acceptance Criteria — `AC-01, AC-02...`):**
   - User Story theo mẫu gọn: *Với vai trò `[Ai]`, tôi muốn `[Làm gì]` để `[Đạt kết quả gì]`.*
   - Viết AC theo nhóm kịch bản rõ rệt: **(a) Luồng hợp lệ**, **(b) Điều kiện biên**, **(c) Luồng lỗi / Ngoại lệ / Hủy giữa chừng**.
   - Dùng **một định dạng đồng nhất** cho toàn bộ danh sách AC (chọn hoặc `Given – When – Then` gọn theo từng AC, hoặc bảng kịch bản cho các ca cùng mẫu — không trộn nửa bảng nửa bullet giữa các AC ngang hàng). Không lặp dài dòng cùng một mệnh đề `Given` ở nhiều AC liên tiếp khi chỉ khác một biến số.
4. **Điểm cần xác nhận / Giả định mở (chỉ thêm khi thực sự phát hiện kẽ hở trong đề bài):**
   - Nếu đầu vào có điểm chưa chốt (ví dụ: quy định *"Không áp dụng đồng thời với sản phẩm Flash Sale"* chưa rõ là chặn áp voucher cho cả đơn hàng hay chỉ loại trừ dòng sản phẩm Flash Sale đó, hoặc chưa quy định cách hoàn tiền khi thanh toán lần 2 lỗi mà khách bỏ luôn), **tuyệt đối không tự bịa rule lấp vào làm thành quy tắc chính thức**. Liệt kê ngắn gọn ở mục riêng cuối bài: `Câu hỏi mở cần PO/BA chốt trước khi dev`.

---

## 3. Danh sách Tự rà Trước khi Xuất Spec Nghiệp vụ

- [ ] Tất cả mốc số, tiền tệ, thời gian (`100.000đ`, `5 lần`, `10 phút`, `15 phút`, `<= 3 phương thức`) đã giữ chính xác và rõ dấu biên `<` / `<=` / `>` / `>=` chưa?
- [ ] Có trường hợp nào chữ `và` / `hoặc` có thể hiểu theo 2 cách gom ngoặc logic không? Nếu có, tách thành từng dòng đánh số.
- [ ] Mỗi chuyển đổi trạng thái đã nêu rõ trạng thái đích và ai/hệ thống nào kích hoạt chưa?
- [ ] Văn phong đã gọn trực diện (loại bỏ `"tiến hành thực hiện việc..."`, `"nhằm đáp ứng các kịch bản..."`), không dài dòng thừa chữ nhưng vẫn đủ điều kiện để QA test ngay?
