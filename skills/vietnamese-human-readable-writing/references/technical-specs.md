# Chuẩn Viết Tài liệu Kỹ thuật (IDD, SAD, API Spec, System Design, Runbook) (v4)

Dùng tài liệu này khi soạn thảo, giải thích hoặc rà soát tài liệu kỹ thuật dành cho lập trình viên, kiến trúc sư hệ thống hoặc đội vận hành.

---

## 1. Register Kỹ thuật, Thuật ngữ và Không Bịa Hợp đồng

- **Register chuẩn (tránh lỗi dịch máy):**
  - Tài liệu đặc tả hệ thống (**IDD, SAD, API Spec, RFC, System Design, Postmortem**): ưu tiên giọng khách quan, **vô nhân xưng** (*"Hệ thống ghi nhận..."*, *"Worker đẩy sự kiện..."*; tránh dùng đại từ `bạn` lặp đi lặp lại trong spec chính thức).
  - Tài liệu hướng dẫn thao tác / onboarding (**Runbook, How-to**): có thể dùng `bạn` hoặc câu mệnh lệnh rõ ràng (*"Chạy lệnh..."*, *"Kiểm tra..."*).
- **Giữ nguyên tên định danh & thuật ngữ chuẩn ngành:** Không dịch sang tiếng Việt các tên endpoint, header, trường JSON, enum, lệnh CLI, bảng/topic hay khái niệm kỹ thuật phổ biến (`Idempotency-Key`, `HMAC-SHA256`, `ZSET`, `at-least-once`, `Presigned URL`, `rollback`, `Stop-The-World`). Chỉ bọc backtick tên tham số/lệnh/biến thật; không bọc backtick khái niệm mô tả chung như tên biến giả.
- **Không tự bịa chi tiết hợp đồng kỹ thuật chưa chốt (`HF-3`):** Giữ đúng 100% path, header, field, mã HTTP và enum từ đầu vào. Nếu cung cấp payload minh họa hoặc gợi ý cơ chế còn thiếu (như xử lý timeout ở bước cuối giữa nhiều hệ thống), **tách riêng và gắn nhãn rõ** `Ví dụ minh họa (chưa chốt schema chính thức)` hoặc `Điểm cần thống nhất giữa các đội`.

---

## 2. Kiểm chứng An toàn Lệnh & Bất biến Cơ chế (FIX-01, FIX-02)

1. **Lệnh CLI / thao tác có rủi ro dữ liệu:** Phân biệt rạch ròi giữa lệnh chỉ sửa staging vs lệnh xóa/stage xóa khỏi repo hoặc ghi đè working tree. Ví dụ trong Git:
   - `git restore --staged <file>` (Git ≥ 2.23) và `git reset HEAD <file>` (Git cũ hơn, repo đã có commit): chỉ gỡ khỏi staging, giữ nguyên file trên máy.
   - `git rm --cached <file>`: chỉ dùng để bỏ theo dõi nếu chấp nhận **xóa file khỏi repo ở commit tiếp theo** (hoặc dùng khi repo hoàn toàn chưa có commit nào chưa có `HEAD`); tuyệt đối không gộp chung cho "Git bản cũ" với file đã từng commit.
   - Luôn nêu cảnh báo ngắn phân biệt với lệnh nguy hiểm (`git restore <file>` thiếu `--staged`, `git rm -f`, `git reset --hard`) khi an toàn file trên máy là yêu cầu cốt lõi.
2. **Bất biến thứ tự & nguyên tử trong hệ thống phân tán:** Không khẳng định một cơ chế xử lý lỗi giữ được bất biến nếu nó tự mâu thuẫn về mặt logic (ví dụ: không viết *"đẩy message lỗi M1 sang DLX để giữ thứ tự nghiêm ngặt"* nếu message `M2` cùng key tiếp tục được xử lý trên queue chính; phải phân tách *retry tại chỗ / head-of-line blocking* vs *cách ly cả key*).
3. **Giải thích code / thuật toán / RFC:** Đi thẳng qua từng bước thực thi của code hoặc từng pha rollout/rollback, nêu rõ điều kiện biên (concurrency, `clock skew`, lock queue ở QPS cao, OOM/leak reference).

---

## 3. Cấu trúc Khuyến nghị & Kết hợp Tài liệu Lai

- **API Spec / IDD:** Tóm tắt Endpoint/Event → Bảng Request (Header/Path/Body) → Bảng Response & Mã lỗi + Retry/Idempotency → Payload minh họa (nếu cần, đặt sát bảng tránh Split-Attention) → Điểm cần thống nhất (nếu nguồn thiếu). Không lặp lại bằng văn xuôi những gì bảng đã thể hiện đủ.
- **SAD / System Design / IDD đa hệ thống:** Mục tiêu & Ràng buộc → Thành phần & Ranh giới trách nhiệm → Luồng tương tác đánh số theo đúng thứ tự (gồm nhánh bù trừ khi bước sau lỗi) → Đánh đổi thiết kế & Các bước chưa chốt.
- **IDD kèm Business Rule/AC hoặc SAD kèm luồng nghiệp vụ:** Đọc kết hợp `business-specs.md` để giữ nhất quán tên trạng thái, biên `< / <=` và kịch bản QA xuyên suốt cả phần kỹ thuật lẫn nghiệp vụ.
- **Runbook sự cố:** Đặt **Điều kiện kích hoạt** và **Cảnh báo cấm làm** lên đầu trang; tách nhánh rẽ theo kết quả kiểm tra thật rõ ràng; giữ Runbook thuần túy phục vụ trực sự cố.
