# Chuẩn Viết Tài liệu Kỹ thuật (IDD, SAD, API Spec, System Design, Runbook) (v4.1)

Dùng tài liệu này khi soạn thảo, giải thích hoặc rà soát tài liệu kỹ thuật dành cho lập trình viên, kiến trúc sư hệ thống hoặc đội vận hành.

---

## 1. Register Kỹ thuật, Thuật ngữ và Không Bịa Hợp đồng

- **Register chuẩn (tránh lỗi dịch máy):**
  - Tài liệu đặc tả hệ thống (**IDD, SAD, API Spec, RFC, System Design, Postmortem**): ưu tiên giọng khách quan, **vô nhân xưng** (*"Hệ thống ghi nhận..."*, *"Worker đẩy sự kiện..."*; tránh dùng đại từ `bạn` lặp đi lặp lại trong spec chính thức).
  - Tài liệu hướng dẫn thao tác / onboarding (**Runbook, How-to**): có thể dùng `bạn` hoặc câu mệnh lệnh rõ ràng (*"Chạy lệnh..."*, *"Kiểm tra..."*).
- **Giữ nguyên tên định danh & thuật ngữ chuẩn ngành:** Không dịch sang tiếng Việt các tên endpoint, header, trường JSON, enum, lệnh CLI, bảng/topic hay khái niệm kỹ thuật phổ biến (`Idempotency-Key`, `HMAC-SHA256`, `ZSET`, `at-least-once`, `Presigned URL`, `rollback`, `Stop-The-World`). Chỉ bọc backtick tên tham số/lệnh/biến thật; không bọc backtick khái niệm mô tả chung như tên biến giả.
- **Không tự bịa chi tiết hợp đồng kỹ thuật chưa chốt:** Giữ đúng 100% path, header, field, mã HTTP và enum từ đầu vào. Nếu cung cấp payload minh họa hoặc gợi ý cơ chế còn thiếu (như xử lý timeout ở bước cuối giữa nhiều hệ thống), **tách riêng và gắn nhãn rõ** `Ví dụ minh họa (chưa chốt schema chính thức)` hoặc `Điểm cần thống nhất giữa các đội`.

---

## 2. Kiểm chứng Khẳng định Kỹ thuật & An toàn Vận hành

1. **Xác minh khẳng định có rủi ro dữ liệu / vận hành:** Với tên lệnh CLI có rủi ro xóa/sửa trạng thái, lock mode của CSDL (ví dụ thao tác DDL trên bảng tải cao), cú pháp tham số hoặc bất biến thứ tự/nguyên tử:
   - Ưu tiên đối chiếu mã nguồn, tài liệu chính thức hoặc công cụ kiểm thử nếu môi trường cho phép; **không bắt buộc tra cứu với câu hỏi khái niệm thông thường**.
   - Tách bạch rõ **phần đã kiểm chứng** với **giả định cần kiểm tra ở staging/tài liệu hãng**; nếu chưa xác minh được chính xác tên flag hoặc lock mode, **không khẳng định chắc chắn tuyệt đối**.
2. **Bảo toàn điều kiện biên & bất biến cơ chế:** Kiểm tra không gộp lệnh có rủi ro xóa dữ liệu/lịch sử vào hướng dẫn hoàn tác an toàn, và không mô tả một cơ chế tách luồng lỗi là giữ nguyên thứ tự nghiêm ngặt nếu các thông điệp kế tiếp cùng khóa vẫn được xử lý.
3. **Giải thích code / thuật toán / RFC:** Đi thẳng qua từng bước thực thi hoặc từng pha rollout/rollback, nêu rõ điều kiện biên (concurrency, `clock skew`, lock queue ở QPS cao, OOM/leak reference).

---

## 3. Cấu trúc Khuyến nghị, Đồng nhất Trạng thái & Tài liệu Lai

- **Giữ nguyên trạng thái xác nhận giữa các khối kiến trúc:** Mọi luồng hoặc thành phần còn ở trạng thái *"chưa chốt"* **phải để trung tính** *(hoặc ghi rõ `[Chưa chốt — xem Mục Câu hỏi mở]`)* đồng bộ trên **Bảng trách nhiệm thành phần, Sơ đồ Sequence/Flowchart, API Contract, Ma trận trạng thái, Trình tự luồng và Open Questions** — tuyệt đối không gán cứng vào thành phần cụ thể ở bảng/sơ đồ rồi lại hỏi ở cuối tài liệu.

- **API Spec / IDD:** Tóm tắt Endpoint/Event → Bảng Request (Header/Path/Body) → Bảng Response & Mã lỗi + Retry/Idempotency → Payload minh họa (nếu cần, đặt sát bảng tránh Split-Attention) → Điểm cần thống nhất (nếu nguồn thiếu). Không lặp lại bằng văn xuôi những gì bảng đã thể hiện đủ.
- **SAD / System Design / IDD đa hệ thống:** Mục tiêu & Ràng buộc → Thành phần & Ranh giới trách nhiệm → Luồng tương tác đánh số theo đúng thứ tự (gồm nhánh bù trừ khi bước sau lỗi) → Đánh đổi thiết kế & Các bước chưa chốt.
- **IDD kèm Business Rule/AC hoặc SAD kèm luồng nghiệp vụ:** Đọc kết hợp `business-specs.md` để giữ nhất quán tên trạng thái, biên `< / <=` và kịch bản QA xuyên suốt cả phần kỹ thuật lẫn nghiệp vụ.
- **Runbook sự cố:** Đặt **Điều kiện kích hoạt** và **Cảnh báo cấm làm** lên đầu trang; tách nhánh rẽ theo kết quả kiểm tra thật rõ ràng; giữ Runbook thuần túy phục vụ trực sự cố.
