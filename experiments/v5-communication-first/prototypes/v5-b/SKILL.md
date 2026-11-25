---
name: vietnamese-human-readable-writing
description: >-
  Use when writing, explaining technical or complex topics, analyzing problems,
  conversing naturally, communicating at work, drafting business or technical
  specs (PRD, BRD, User Story, AC, IDD, SAD, API Spec), or clarifying and
  editing machine-translated or ambiguous Vietnamese prose. Not for pure code
  generation, math-only solving, or non-Vietnamese-only tasks.
---

# ViWrite V5-B — Communication-First (Core Tối giản)

Giúp AI truyền đạt tiếng Việt **dễ hiểu ngay lần đọc đầu, đúng bản chất và dùng được ngay**, không bắt người đọc tự giải mã văn phong hành chính hay dịch máy.

---

## 1. Hiểu đúng ý trước, viết lại từ đầu (Understand → Communicate)

Khi viết mới hoặc viết lại một văn bản, **đừng sửa lắt nhắt từng câu trên khung chữ cũ**. Hãy làm ngầm 2 bước sau:

1. **Hiểu trọn thông điệp & người đọc:** Chuyện gì đang xảy ra? Người đọc mục tiêu đã biết gì, cần nắm điều gì, chịu tác động ra sao và cần làm gì tiếp theo?
2. **Viết lại bằng tiếng Việt tự nhiên cho đúng mục đích:**
   - **Đổi ngôn ngữ nặng nề sang tác động thực tế:** Giữ nguyên các **thuật ngữ chuyên môn thật** (`Idempotency Key`, `RPO > 0`, `rollback`, `Pinned Archive`), con số, mốc giờ và định danh hệ thống; nhưng chủ động chuyển các **cụm từ hành chính, danh từ hóa rỗng** (*"đối soát định kỳ"*, *"trạng thái tạm treo"*, *"thực hiện việc..."*) thành cách nói trực diện dễ hiểu.
   - **Chọn cấu trúc tự nhiên cho từng việc:**
     - *Thông báo người dùng:* Cho biết ngay thay đổi gì, ảnh hưởng gì, ngoại lệ và việc cần làm.
     - *Giải thích khái niệm / kỹ thuật:* Đi từ vấn đề thực tế dẫn sang cơ chế giải quyết nếu phù hợp người đọc; giữ trọn cơ chế nội tại cho kỹ sư.
     - *Hội thoại / trao đổi:* Tự nhiên theo mạch trò chuyện, không tự đóng khung báo cáo.
     - Không mặc định dùng BLUF, bảng hay bullet cho mọi bài; không thêm tầng tiêu đề chỉ để trông chuyên nghiệp; ưu tiên mọi chỉ định riêng của người dùng.

---

## 2. Phân biệt Mục đích Tác vụ

- **Viết / viết lại thành phẩm (thông báo, tin nhắn, hướng dẫn):** Chỉ trả về văn bản hoàn chỉnh dùng được ngay. Không tự biến thông báo gửi khách hàng hay SOP thành báo cáo rà soát nghiệp vụ. Chỉ kèm ghi chú 1–2 dòng tách riêng cho tác giả nếu thiếu sót thực sự gây hiểu nhầm nghiêm trọng.
- **Review / phân tích:** Chỉ thẳng lỗi, mâu thuẫn và khoảng trống dữ kiện.
- **Soạn đặc tả triển khai (PRD, BRD, AC, Business Rule, IDD, API Spec):** Làm rõ các điểm chưa chốt ảnh hưởng thiết kế/code; giữ nguyên trạng thái `[Chưa chốt]` đồng bộ giữa văn bản, bảng và sơ đồ.

---

## 3. Kiểm chứng Ràng buộc (Verify)

Kiểm chứng để đảm bảo an toàn nội dung, **không** dùng làm cớ bám nguyên văn phong khó hiểu của bản gốc:
- Không tự bịa số liệu, ngày giờ, tên nút bấm, quy tắc hoặc nguyên nhân chưa có căn cứ.
- Bảo toàn chính xác logic `và`/`hoặc`, biên `<`/`<=`, mức độ bắt buộc (`phải` vs `nên`), sắc thái chắc chắn (`có thể` vs `sẽ`) và toàn bộ ngoại lệ/điều kiện gốc (không tự thu hẹp định dạng yêu cầu nếu nguồn không giới hạn).
- Không làm mỏng chiều sâu kỹ thuật khi người đọc chuyên môn cần cơ chế chi tiết; phân biệt dữ kiện đã kiểm chứng với giả định khi đưa ra khẳng định kỹ thuật có rủi ro vận hành.

*(Với tác vụ đặc tả nghiệp vụ/kỹ thuật chuyên sâu hoặc tài liệu dài nhiều mảng, chỉ mở 1–2 tài liệu cần thiết trong `references/`: `business-specs.md`, `technical-specs.md`, `information-architecture.md`, `vietnamese-clarity-and-style.md`. Không in quy trình tự kiểm tra hay danh sách file đã đọc ra câu trả lời cuối.)*
