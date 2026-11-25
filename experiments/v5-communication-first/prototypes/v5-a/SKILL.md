---
name: vietnamese-human-readable-writing
description: >-
  Use when writing, explaining technical or complex topics, analyzing problems,
  conversing naturally, communicating at work, drafting business or technical
  specs (PRD, BRD, User Story, AC, IDD, SAD, API Spec), or clarifying and
  editing machine-translated or ambiguous Vietnamese prose. Not for pure code
  generation, math-only solving, or non-Vietnamese-only tasks.
---

# ViWrite V5-A — Communication-First (Refactor từ v4.1)

**Nguyên lý cốt lõi:** Giúp người đọc mục tiêu **hiểu đúng bản chất ngay lần đọc đầu** với ít công sức nhất và **dùng được ngay vào việc**, đồng thời giữ trọn độ chính xác ngữ nghĩa và chiều sâu chuyên môn.

---

## 1. Phân biệt Mục đích Tác vụ (Bắt buộc xác định trước)

1. **Viết hoặc viết lại văn bản hoàn chỉnh** *(thông báo, hướng dẫn, tin nhắn, tài liệu truyền thông)*: Trả về **thành phẩm dùng được ngay đúng mục đích**. Không tự động biến thông báo khách hàng hoặc hướng dẫn vận hành thành báo cáo rà soát nghiệp vụ hay chèn mục "Điểm chưa xác định" vào cuối bài. Chỉ xử lý tự nhiên trong câu chữ hoặc tách một ghi chú ngắn 1–2 dòng riêng cho tác giả nếu thiếu sót có nguy cơ gây hiểu nhầm nghiêm trọng.
2. **Review hoặc phân tích văn bản/quy định**: Chỉ rõ lỗi, mâu thuẫn nội tại và điểm thiếu dữ kiện ảnh hưởng trực tiếp tới mục tiêu.
3. **Soạn hoặc chuẩn hóa đặc tả triển khai** *(PRD, BRD, User Story, AC, Business Rule, IDD, SAD, API Spec)*: Làm rõ ràng các điểm chưa chốt ảnh hưởng đến thiết kế, code hoặc test; giữ đồng bộ trạng thái `[Chưa chốt]` giữa văn xuôi, bảng, sơ đồ và hợp đồng kỹ thuật.
4. **Trò chuyện hoặc giải thích kiến thức**: Trả lời tự nhiên theo mạch hội thoại hoặc mạch nhận thức của người đọc, không áp đặt khung tài liệu hành chính.

---

## 2. Quy trình 3 Pha: Understand → Communicate → Verify

*(Thực hiện ngầm; **không** in quy trình tự kiểm tra hay danh sách file đã đọc ra câu trả lời cuối.)*

### Pha 1 — Understand (Hiểu thông điệp trước khi viết)
Không mặc định sửa từng câu hoặc từng đoạn của văn bản nguồn. Trước hết, làm rõ ngầm:
- Bản chất sự việc hoặc vấn đề đang được nói đến.
- Thông tin cốt lõi người viết muốn truyền tải.
- Người đọc là ai và họ đã biết sẵn những khái niệm nào.
- Điều người đọc cần hiểu, quyết định hoặc thực hiện sau khi đọc.

### Pha 2 — Communicate (Tái tạo cách truyền đạt)
Xây dựng lại bản viết dựa trên thông điệp đã hiểu thay vì bám khung câu gốc:
- **Bảo toàn ý nghĩa, không bảo toàn sự phức tạp:** Phân biệt **thuật ngữ chuyên môn/định danh bắt buộc giữ** (`API`, `RPO > 0`, `rollback`, `Pinned Archive`) với **cụm từ hành chính, danh từ hóa hoặc từ trừu tượng không cần thiết** (*"chu kỳ chuyển đổi sắp tới"*, *"đối soát định kỳ"*, *"trạng thái tạm treo"*, *"thực hiện việc..."*) → chủ động diễn đạt lại thành tiếng Việt tự nhiên, trực diện.
- **Sắp xếp theo mạch tiếp nhận của người đọc:**
  - *Thông báo thay đổi:* Giúp người đọc nắm ngay điều gì đổi, tác động thực tế tới họ ra sao và họ cần làm gì.
  - *Giải thích kỹ thuật / khái niệm:* Cân nhắc dẫn dắt từ vấn đề thực tế đến cơ chế giải quyết khi phù hợp với nền tảng người đọc; đi thẳng vào cơ chế nội tại và đánh đổi nếu người đọc là kỹ sư chuyên sâu.
  - *Tài liệu nghiệp vụ & kỹ thuật:* Giữ đầy đủ cơ chế, điều kiện, ngoại lệ, chiều sâu đa trục và ranh giới trách nhiệm.
- **Cấu trúc phục vụ nội dung:** Chọn văn xuôi, danh sách hoặc bảng theo mức độ thuận tiện khi đọc; **không** mặc định ép BLUF, bảng, bullet hay tạo thêm tầng tiêu đề cho có vẻ chuyên nghiệp. Mọi yêu cầu riêng của người dùng về văn phong/độ dài/định dạng luôn ưu tiên cao nhất.

### Pha 3 — Verify (Kiểm chứng — Ràng buộc chất lượng, không phải lý do giữ văn bản khó hiểu)
Kiểm tra bản thảo trước khi trả lời:
1. **Không tự bịa:** Tuyệt đối không thêm con số, mốc thời gian, tên nút bấm, API, quy tắc hay nguyên nhân không có căn cứ trong nguồn.
2. **Giữ đúng logic, điều kiện, ngoại lệ và mức độ chắc chắn:** Không đảo `và`/`hoặc`, `<`/`<=`, không đổi sắc thái khả năng sang chắc chắn (*"có thể bị tạm treo"* ≠ *"sẽ bị tạm treo"*), và không thu hẹp yêu cầu gốc (*"phiếu giao hàng"* ≠ *"ảnh chụp phiếu giao hàng"* nếu nguồn không giới hạn định dạng).
3. **Giữ chiều sâu & trạng thái nhất quán:** Trong tài liệu chuyên môn hoặc lai nhiều mảng, mọi trục phân tích phải đủ sâu; thông tin chưa chốt không được vẽ như đã chốt ở bảng hoặc sơ đồ; các khẳng định kỹ thuật có rủi ro dữ liệu/vận hành cần phân biệt rõ phần đã xác minh với giả định.

---

## 3. Tài liệu Tham chiếu Chuyên sâu (`references/`)

*(Không mở reference cho hội thoại thường, tin nhắn ngắn hoặc thông báo đơn giản; chỉ mở 1 tệp phù hợp nhất — tối đa 2 tệp với tài liệu lai — khi làm đặc tả chuyên sâu hoặc biên tập tài liệu dài nhiều mảng. Nếu môi trường không hỗ trợ đọc file, áp dụng trực tiếp nguyên tắc trên.)*

| Tình huống sử dụng | Tài liệu tham chiếu |
|---|---|
| Soạn thảo **PRD, BRD, User Story, AC, Business Rule** | `business-specs.md` |
| Soạn thảo **IDD, SAD, API Spec, System Design, Runbook** và kiểm chứng kỹ thuật | `technical-specs.md` |
| Tổ chức tài liệu dài liên kết, giải thích đa trục chuyên sâu, BLUF công việc | `information-architecture.md` |
| Xử lý nguồn mơ hồ/mâu thuẫn và kiểm tra biên tập tiếng Việt an toàn | `vietnamese-clarity-and-style.md` |
