# Chuẩn Viết Tài liệu Nghiệp vụ (PRD, BRD, User Story, AC, Business Rule) (v4.1)

Dùng tài liệu này khi soạn thảo hoặc chuẩn hóa tài liệu nghiệp vụ để PO, BA, Dev và QA đọc hiểu thống nhất, triển khai và viết test case chính xác.

---

## 1. Bốn Thuộc tính Bắt buộc (ISO/IEC/IEEE 29148)

1. **Đơn nghĩa (Unambiguous):** Mọi bên chỉ rút ra **một** cách hiểu duy nhất về điều kiện kích hoạt, công thức tính và biên giá trị.
2. **Kiểm chứng được (Verifiable):** QA viết được test Pass/Fail từ điều kiện cụ thể; tránh tính từ mơ hồ (*"hợp lý", "bất thường", "phù hợp"*) trừ khi đánh dấu là lỗ hổng cần PO chốt.
3. **Đầy đủ (Complete):** Bảo toàn trọn vẹn phạm vi áp dụng, ngoại lệ và chuyển đổi trạng thái.
4. **Nhất quán (Consistent):** Một thực thể/trạng thái giữ đúng một tên gọi từ Scope, Business Rule tới AC và API contract đi kèm.

---

## 2. Xử lý Lỗ hổng & Mâu thuẫn trong Tài liệu Nghiệp vụ (Trường hợp B)

Khi ghi chú họp hoặc tài liệu nguồn thiếu thông số hay có mâu thuẫn:
- **Không tự bịa ngưỡng hoặc chọn ngầm một phía:** Tuyệt đối không tự đặt tỷ lệ % phạt, ngưỡng tiền/ngày hay tự xóa bỏ một quy định khi hai phần tài liệu mâu thuẫn nhau (ví dụ Mục 1 ghi hoàn 3 ngày làm việc, Mục 3 ghi 5–7 ngày làm việc).
- **Tách riêng và giới hạn theo phạm vi:** Đặt câu hỏi mở ảnh hưởng trực tiếp mục tiêu/triển khai vào mục **`Điểm cần xác nhận / Mâu thuẫn cần PO chốt trước khi dev`**. Không mở rộng hỏi lan man ngoài phạm vi yêu cầu, và giữ nguyên trạng thái *"chưa chốt"* ở mọi phần Scope, BR, AC, State transition hoặc API đi kèm cho tới khi được xác nhận.
- **Câu quy tắc đa nghĩa logic (`và/hoặc`, phạm vi loại trừ):** Nếu câu gốc có từ 2 cách hiểu hợp lý (ví dụ loại trừ cả đơn vs chỉ loại trừ dòng sản phẩm thuộc danh mục), trình bày tường minh cả hai phương án hiểu để Kinh doanh/PO chốt.

---

## 3. Cấu trúc Đặc tả Gọn, Sạch và Kết hợp Tài liệu Lai

1. **Phạm vi (Scope):** Tách rõ **In-Scope** vs **Out-of-Scope** (ví dụ kênh Web/App vs POS, Phase 1 vs Phase sau).
2. **Quy tắc nghiệp vụ (`BR-01, BR-02...`):** Nêu rõ **Chủ thể / Điều kiện kích hoạt → Hành vi hệ thống**. Với phân tầng hạn mức nhiều mức, dùng bảng lộ rõ dấu `<`, `<=`, `>`, `>=`. Khóa chặt từ khóa nghĩa vụ (`Phải / Bắt buộc / Chặn`, `Không áp dụng / Ngoại trừ`, `Được phép`).
3. **User Story & Acceptance Criteria (`AC-01, AC-02...`):**
   - Dùng **một định dạng đồng nhất** cho toàn bộ AC (hoặc `Given–When–Then` phân nhóm *Hợp lệ / Biên / Lỗi–Ngoại lệ*, hoặc bảng kịch bản cho các ca cùng mẫu — không trộn nửa bảng nửa bullet).
   - Không lặp dài dòng cùng một mệnh đề `Given` ở nhiều AC liên tiếp nếu chỉ khác một biến số.
4. **Khi PRD gắn kèm API Contract (Tài liệu lai):** Đối chiếu chéo để tên trạng thái hệ thống (`CANCELLED`, `PARTIAL_PAID`), điều kiện chặn (`409 Conflict`) và ràng buộc dữ liệu khớp tuyệt đối giữa phần Business Rule và phần API; đồng thời đọc thêm `technical-specs.md` khi cần trình bày chi tiết hợp đồng API.
