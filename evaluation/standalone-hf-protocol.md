# Quy trình Kiểm định Hard Fail Độc lập (`standalone-hf-protocol.md`)

Tài liệu này bổ sung cho [rubric-v2.md](./rubric-v2.md) nhằm khắc phục hiện tượng **bất nhất Hard Fail giữa các cặp đấu A/B** (ví dụ cùng một bản đầu ra `C` ở `H2-06`, `H2-12`, `H2-19` nhận phán quyết HF khác nhau khi ghép cặp với A, B hay C0).

---

## 1. Nguyên tắc Đánh giá Gate 0 Độc lập Trước Khi So sánh Cặp

1. **Một bản đầu ra mỗi lần chấm (Single-Output Gate 0 Audit):** Giám khảo kiểm tra độc lập **duy nhất 1 output** trực tiếp với `input`, `purpose`, `audience` và `must_preserve` — hoàn toàn **không nhìn thấy output đối thủ**. Điều này ngăn hiệu ứng lu mờ cặp đấu (*pairwise overshadowing*, khi đối thủ A/B tự bịa quá nặng khiến lỗi nội tại của C bị bỏ qua hoặc ngược lại).
2. **Kiểm tra chéo bằng chứng nguyên văn & tài liệu gốc:** Mọi cờ Hard Fail do LLM Judge bật đều phải trích nguyên văn câu/dòng vi phạm và kiểm tra xem có thật sự tồn tại lỗi không.

---

## 2. Phân loại 3 Mức Độ Hard Fail (Thay thế Nhãn Gộp)

| Nhãn phân loại | Định nghĩa | Cách dùng trong báo cáo |
|---|---|---|
| **1. Judge-Detected HF** | Cờ `HF-1..HF-6` bật lên trong ít nhất 1 lượt chấm (Standalone hoặc Pairwise). | Ghi nhận làm tín hiệu rà soát sơ bộ; không mặc định là sự thật tuyệt đối nếu các lượt khác bác bỏ. |
| **2. Verified HF** | Lỗi Hard Fail đã được xác minh trực tiếp trên nguyên văn output (và kiểm chứng kỹ thuật/logic nguồn nếu là lỗi kỹ thuật), thực sự vi phạm `HF-1..HF-6`. | Dùng để tính tỷ lệ Hard Fail xác thực của phiên bản Skill và đưa vào backlog sửa lỗi. |
| **3. Judge-Disagreed / Unconfirmed** | Giám khảo bất đồng giữa các lượt chấm (hoặc giữa standalone và pairwise) và đối chiếu nguyên văn cho thấy chỉ là lỗi `Major` diễn đạt/biên tập ranh giới chứ không đủ căn cứ `Critical HF`. | Báo cáo tách riêng là bất đồng giám khảo / lỗi `Major` ranh giới; không phóng đại hay che giấu. |

---

## 3. Quy tắc Báo cáo Tương đương Tập mẫu & Token

1. **Không so sánh chéo tỷ lệ HF trên các tập mẫu khác cỡ như thể cùng tập mẫu:** Mọi bảng so sánh có `Group C0` (`n = 12`) **phải** tách riêng bảng trên đúng **12 ca trùng khớp (`H2-01, 02, 07, 09, 12, 17, 18, 19, 21, 22, 23, 24`)**, tách biệt khỏi bảng toàn tập `n = 24` của `A`, `B`, `C`.
2. **Nhãn Token Ước lượng:** Khi runtime không cung cấp billing/API token count thực tế, mọi số token phải ghi rõ là **ước lượng heuristic (`bytes / 3,8` hoặc `chars / 3,5`)**.
