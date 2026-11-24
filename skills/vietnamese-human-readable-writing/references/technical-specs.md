# Chuẩn Viết Tài liệu Kỹ thuật (IDD, SAD, API Spec, System Design, Runbook)

Dùng tài liệu này ở chế độ **Chặt** khi viết hoặc rà soát tài liệu kỹ thuật cho lập trình viên, kiến trúc sư hệ thống hoặc đội vận hành kỹ thuật.

---

## 1. Thuật ngữ và Cách Giữ Chuẩn Kỹ thuật

- **Giữ nguyên tên định danh và thuật ngữ chuẩn ngành:** Không dịch sang tiếng Việt các tên endpoint, header, trường JSON, trạng thái enum, lệnh CLI, tên bảng/topic hay khái niệm phổ biến như `Idempotency-Key`, `HMAC-SHA256`, `at-least-once`, `ZSET`, `ZCARD`, `409 Conflict`, `Presigned URL`, `rollback`, `timeout`.
- **Không viết hoa hoặc tự đặt tên mới cho field chưa có trong đề:** Khi viết IDD/API Spec từ yêu cầu tóm tắt:
  - Giữ chính xác 100% tên path, header, tham số, mã trạng thái HTTP và tên enum có trong đầu vào.
  - Nếu cần trình bày khung JSON request/response minh họa có thêm trường phụ trợ chưa được đề bài chốt (như `refund_id`, `created_at`, cấu trúc `error.code`), **bắt buộc ghi nhãn rõ**: *"Khung JSON minh họa — các trường ngoài đặc tả gốc cần thống nhất với backend"* để tránh biến đề xuất của AI thành hợp đồng API giả.

---

## 2. Cấu trúc Chuẩn theo Loại Tài liệu Kỹ thuật

### A. Đặc tả API / Webhook (IDD / API Spec)
1. **Tóm tắt Endpoint / Event:** Method, Path (hoặc Webhook Event Name), mục đích 1 câu, yêu cầu xác thực/chữ ký/idempotency nếu có.
2. **Đầu vào (Request):** Bảng gọn gồm `Vị trí (Header/Path/Body)`, `Tên trường`, `Kiểu`, `Bắt buộc`, `Ràng buộc & Validation` — không diễn giải lại bằng văn xuôi những gì bảng đã thể hiện đủ (*chống Redundancy Effect*).
3. **Đầu ra & Mã lỗi (Response & Error Handling):** Bảng mã HTTP / trạng thái trả về kèm điều kiện kích hoạt chính xác; chính sách retry/timeout nếu là webhook hoặc giao dịch idempotent.
4. **Ví dụ Payload (nếu cần thiết cho tích hợp):** Đặt ngay sau bảng thông số để giảm *Split-Attention*.

### B. Thiết kế Hệ thống / Kiến trúc (SAD / System Design)
1. **Mục tiêu & Ràng buộc:** Nêu ngắn gọn bài toán, giới hạn tải/thời gian (ví dụ 500.000 dòng, tránh HTTP timeout 30s) và giả định phạm vi.
2. **Luồng xử lý & Thành phần (Data Flow & Responsibilities):** Trình bày theo đúng trình tự chạy từ Client → Ingestion → Queue/Storage → Worker/DB → Phản hồi, nêu rõ trách nhiệm từng thành phần và ngữ nghĩa truyền tin (*at-least-once*, *idempotent*). Có thể dùng sơ đồ ngắn hoặc danh sách đánh số rõ từng bước.
3. **Xử lý lỗi cục bộ & Điểm đánh đổi:** Nêu chính xác cơ chế retry, trạng thái lỗi từng phần (không rollback cả lô nếu đề bài quy định vậy), và tách rõ **Lựa chọn đề xuất thêm** khỏi **Ràng buộc đã chốt trong đề**.

### C. Technical Spec Thuật toán / Cơ chế (ví dụ Rate Limit, Outbox)
- Trình bày trực tiếp theo **Cấu trúc dữ liệu/Key** → **Các bước thực thi nguyên tử theo nhánh điều kiện** (`nếu < ngưỡng` vs `nếu >= ngưỡng`) → **Đầu ra trả về**.
- Tránh giảng lại khái niệm cơ bản (*Redis là gì, Kafka là gì*) cho đối tượng kỹ sư.

### D. Runbook Vận hành Sự cố Kỹ thuật
- Đặt **Điều kiện kích hoạt** và **Cảnh báo cấm làm** lên đầu trang bằng định dạng nổi bật.
- Tách nhánh `Nếu kết quả A → Làm X` vs `Nếu kết quả B → KHÔNG làm X, chuyển Y kèm bằng chứng Z` thật rõ để người trực sự cố dưới áp lực không bấm nhầm nút.
- Giữ Runbook thuần túy phục vụ người đang trực sự cố; chỉ tách câu hỏi mở cho đội kỹ thuật nếu đầu vào có khoảng trống vận hành thực sự gây rủi ro bấm nhầm, không gắn các ghi chú tiền phát hành thừa vào cuối hướng dẫn thao tác.

---

## 3. Tự rà Ngữ nghĩa & Tải Nhận thức cho Tài liệu Kỹ thuật

- [ ] Mọi con số, timeout, chu kỳ polling, ngưỡng HTTP code và tên trường kỹ thuật đã khớp 100% đầu vào chưa?
- [ ] Có bỏ qua được phần giải thích khái niệm sơ đẳng thừa với trình độ kỹ sư mục tiêu không?
- [ ] Văn xuôi có lặp lại nguyên văn các dòng trong bảng thông số / đoạn mã không (nếu có → cắt phần văn xuôi lặp)?
- [ ] Các chi tiết do AI gợi ý thêm (nếu có) đã được gắn nhãn *Đề xuất / Ví dụ minh họa* tách khỏi phần đặc tả gốc chưa?
