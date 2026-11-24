# Hướng dẫn Chấm điểm Độc lập v2 (`judge-instructions-v2.md`)

Tài liệu này quy định quy trình làm việc của Giám khảo mù (Blind A/B Evaluator v2) dựa trên [rubric-v2.md](./rubric-v2.md). Giám khảo **không biết** đầu ra nào được tạo bởi mô hình hay Skill nào.

---

## 1. Quy tắc Chống Thiên lệch và Phân định Nghiêm ngặt

1. **Chống Position Bias & Verbosity Bias:** Đánh giá độc lập Output A và Output B trước khi so sánh; không mặc định Output A hay Output B tốt hơn; không thưởng độ dài nếu chỉ là chữ đệm hoặc lặp ý, nhưng **KHÔNG** phạt độ dài nếu dùng để giải thích đầy đủ mọi trục kỹ thuật mà chuyên gia yêu cầu hoặc giữ hội thoại sâu đúng mạch trao đổi.
2. **Phân biệt rạch ròi `Major` vs `Critical (Hard Fail)`:**
   - **KHÔNG gắn `HF-3` quá nhạy** cho các câu nối mục đích vô hại (*"để phục vụ tra cứu nhanh"*, lời chào xã giao, placeholder `[Tên]`). Chỉ gắn `HF-3` khi có **bịa đặt trọng yếu** (số liệu, SLA, quy tắc nghiệp vụ, hợp đồng API/field JSON, nguyên nhân log khẳng định như sự thật đã đo) HOẶC khi nguồn cố ý thiếu chủ thể/điều kiện/giao thức mà output **tự bịa để tạo độ rõ giả tạo (False Clarity)**.
   - **BẮT BUỘC gắn `HF-6`** nếu output đưa **lệnh thao tác có rủi ro phá hủy/stage xóa sai ngữ cảnh** trái mục tiêu an toàn (ví dụ: dùng `git rm --cached` cho Git bản cũ khi file có thể đã commit) hoặc đưa **khuyến nghị kỹ thuật tự mâu thuẫn phá vỡ bất biến cam kết** (ví dụ: dùng DLX để "giữ thứ tự nghiêm ngặt" trong khi message kế tiếp cùng key vẫn chạy).
   - **KHÔNG tự động gắn Hard Fail** cho lỗi `Major` thiếu chiều sâu ở một khía cạnh phụ (`D2=2`) nếu các phần đã viết không sai sự thật gây hại hay phá vỡ cơ chế.
3. **Quy tắc đối xứng bắt buộc:** Mọi lỗi đánh dấu `severity = "Critical"` phải đi kèm mã `HF-*` trong `hard_fails`, và mỗi mã trong `hard_fails` phải có lỗi `Critical` tương ứng trong `errors`.
4. **Cấm nhận xét cảm tính:** Không viết *"mượt hơn, hay hơn, chuyên nghiệp hơn"* nếu không chỉ ra bằng chứng cụ thể.

---

## 2. Trình tự Chấm 4 Bước

1. **Kiểm tra Gate 0 độc lập từng Output (`A` riêng, `B` riêng):** So trực tiếp với `input`, `purpose`, `audience` và `must_preserve` để gán `hard_fails` (`HF-1..HF-6` hoặc `[]`).
2. **Chấm 9 tiêu chí `D1..D9` (thang 0–4; `D9 = null` nếu `actionability_applicable == false`):**
   - Đặc biệt kiểm tra **Trường hợp B (nguồn thiếu thông tin / mâu thuẫn)**: nếu nguồn thiếu chủ thể, điều kiện, kết quả hoặc có 2 mục mâu thuẫn, output chỉ rõ chỗ thiếu/mâu thuẫn được điểm cao ở `D1, D4, D9`; output tự đoán bừa để viết cho trôi chảy bị gắn `HF-3` (`D1=0`).
   - Đặc biệt kiểm tra **chiều sâu đa trục**: nếu đề bài hỏi nhiều khía cạnh kỹ thuật (ví dụ cả lưu trữ lẫn thứ tự), kiểm tra từng khía cạnh có được phân tích đầy đủ không (`D2`).
3. **Gắn nhãn lỗi `S-01..R-04` hoặc `HF-1..HF-6` với `severity` (`Minor | Major | Critical`) và trích dẫn bằng chứng cụ thể.**
4. **Ra phán quyết `winner` (`"A"`, `"B"`, hoặc `"TIE"`):** Bên qua Gate 0 thắng bên dính Hard Fail; nếu cả hai qua Gate 0, ưu tiên `D1, D2, D4, D5, D8, D9` trước `D7`.

---

## 3. Định dạng JSON Đầu ra Bắt buộc

Trả về duy nhất 1 JSON hợp lệ:

```json
{
  "case_id": "string",
  "output_a": {
    "hard_fails": [],
    "scores": {"D1": 4, "D2": 4, "D3": 4, "D4": 4, "D5": 4, "D6": 4, "D7": 4, "D8": 4, "D9": 4},
    "errors": []
  },
  "output_b": {
    "hard_fails": ["HF-3"],
    "scores": {"D1": 0, "D2": 3, "D3": 4, "D4": 1, "D5": 3, "D6": 3, "D7": 4, "D8": 3, "D9": 1},
    "errors": [{"code": "HF-3", "severity": "Critical", "evidence": "Tự bịa tên hệ thống PAY gửi OMS qua webhook dù nguồn không cung cấp."}]
  },
  "winner": "A",
  "rationale": "Output B mắc HF-3 (False Clarity) khi tự bịa hệ thống và giao thức không có trong nguồn; Output A giữ nguyên sự thật và chỉ rõ thông tin cần xác nhận."
}
```
