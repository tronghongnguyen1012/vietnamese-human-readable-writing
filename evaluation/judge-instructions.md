# Hướng dẫn Chấm điểm Độc lập cho Blind A/B Judge (`judge-instructions.md`)

Tài liệu này quy định quy trình làm việc của Giám khảo đánh giá mù (Blind Evaluator). Giám khảo **không biết** và **không được suy đoán** đầu ra nào được tạo bằng Skill hay Baseline. Mọi đánh giá phải bám chặt nguồn đầu vào và bằng chứng văn bản.

---

## 1. Quy tắc Chống Thiên lệch Bắt buộc

1. **Chống Thiên lệch Vị trí (*Position Bias*, Zheng et al., 2023):** Không mặc định `Output A` tốt hơn `Output B` hay ngược lại. Đánh giá độc lập từng bản trên các tiêu chí trước khi ra phán quyết thắng/thua. (Hệ thống chạy kiểm thử sẽ hoán đổi ngẫu nhiên và chạy 2 lượt ngược vị trí A/B).
2. **Chống Thiên lệch Độ dài (*Verbosity Bias*, Zheng et al., 2023):** Văn bản dài hơn **KHÔNG** tốt hơn. Chỉ thưởng độ dài nếu nó chứa thêm **dữ kiện đúng, điều kiện biên hoặc bước thao tác cần thiết**. Phạt nặng ở `D6` (Information Density) nếu độ dài tăng do mở bài vòng vo, lặp ý, lời rào đón lịch sự thừa hoặc giải thích kiến thức nền không đúng đối tượng.
3. **Chống Nhận xét Cảm tính:** Cấm sử dụng các nhận xét mơ hồ như *"hay hơn"*, *"mượt hơn"*, *"chuyên nghiệp hơn"* mà không kèm dẫn chứng cụ thể về tác thể, điều kiện, trình tự hay cấu trúc tiếng Việt.
4. **Quy tắc Phi Bù trừ (*Non-Compensatory*):** Văn phong trôi chảy ở `D7` tuyệt đối không thể bù cho bất kỳ lỗi sai nghĩa, thiếu dữ kiện, sai số liệu hay bịa thêm thông tin nào ở Gate 0 (`HF-1..HF-6`) hoặc `D1`, `D2`.

---

## 2. Trình tự Chấm điểm Từng Bước (Chain-of-Thought G-Eval)

### Bước 1: Kiểm tra Độc lập Dữ kiện & Hard Fail cho từng Output (Gate 0)
Đọc kỹ `input`, `purpose`, `audience` và danh sách `must_preserve`. So sánh **từng** output (`Output A` riêng, `Output B` riêng) để phát hiện 6 lỗi Hard Fail:
- `HF-1`: Làm sai ý nghĩa gốc.
- `HF-2`: Làm sai dữ kiện, số liệu, đơn vị, tên định danh/API.
- `HF-3`: Tự bổ sung thông tin/quy tắc/con số không có căn cứ trong input (trừ khi ghi rõ là ví dụ minh họa hoặc giả định đề xuất theo yêu cầu phân tích).
- `HF-4`: Thay đổi logic nghiệp vụ hoặc mức bắt buộc (`và`/`hoặc`, `phải`/`nên`/`có thể`, điều kiện phủ định).
- `HF-5`: Làm mất điều kiện xử lý quan trọng hoặc bỏ sót phần tử trong `must_preserve`.
- `HF-6`: Đơn giản hóa đến mức gây hiểu nhầm bản chất.

Ghi rõ danh sách mã `HF-*` cho `A` và `B` (mảng rỗng `[]` nếu không vi phạm).

### Bước 2: Chấm điểm 9 Tiêu chí Neo Hành vi (Thang 0–4)
Chấm điểm độc lập cho `Output A` và `Output B` trên từng chiều `D1..D9` (nếu `actionability_applicable` là `false`, đặt `D9 = null` cho cả hai):
- **D1 Semantic Accuracy:** Độ chính xác ngữ nghĩa.
- **D2 Completeness:** Độ đầy đủ theo `must_preserve` và ngữ cảnh.
- **D3 Terminology Consistency:** Độ chính xác & nhất quán thuật ngữ.
- **D4 Semantic Clarity:** Tác thể–hành động–đối tượng–điều kiện rõ nghĩa ngay lần đọc đầu.
- **D5 Coherence:** Mạch lạc Đề–Thuyết, trình tự thông tin, từ nối đúng logic.
- **D6 Information Density:** Mật độ thông tin hữu ích / độ dài (không rỗng nghĩa, không lặp, không thừa).
- **D7 Naturalness:** Độ tự nhiên tiếng Việt (không dịch sát tiếng Anh, không lạm dụng danh từ hóa/bị động máy móc, không giọng AI sáo rỗng).
- **D8 Context Appropriateness:** Phù hợp ngữ cảnh (chat ngắn vs báo cáo vs spec), trình độ người đọc (không quá sơ đẳng với chuyên gia), và không làm lộ quy trình tự kiểm nội bộ.
- **D9 Actionability:** Dùng được ngay cho công việc/kiểm thử (hoặc `null` nếu không áp dụng).

### Bước 3: Gắn nhãn Lỗi Thực tế theo Taxonomy (`S-01`..`R-04`)
Với mọi tiêu chí bị chấm `< 4` hoặc đáng chú ý, liệt kê lỗi quan sát được gồm:
- `code`: mã lỗi (`S-01`..`S-06`, `P-01`..`P-04`, `D-01`..`D-04`, `R-01`..`R-04`).
- `severity`: `Minor` | `Major` | `Critical`.
- `evidence`: trích nguyên văn cụm từ/câu bị lỗi hoặc chỉ rõ thông tin bị thiếu.

### Bước 4: Ra Phán quyết Thắng / Hòa / Thua (`winner`)
- Xét Gate 0 trước: bên không có `HF-*` thắng bên có `HF-*`.
- Nếu cả hai đều qua Gate 0: ưu tiên nhóm Trung thực & Rõ nghĩa (`D1, D2, D4, D5`) và Khả dụng/Ngữ cảnh (`D8, D9`) trước nhóm bề mặt (`D7`).
- Giá trị bắt buộc của `winner`: `"A"`, `"B"`, hoặc `"TIE"`. Chỉ chọn `"TIE"` khi chất lượng thực chất tương đương hoặc mỗi bản hơn một mặt ngang trọng số.

---

## 3. Định dạng JSON Đầu ra Bắt buộc

Giám khảo trả về **duy nhất 1 khối JSON hợp lệ** đúng cấu trúc sau:

```json
{
  "case_id": "string",
  "output_a": {
    "hard_fails": ["HF-5"],
    "scores": {
      "D1": 2,
      "D2": 1,
      "D3": 4,
      "D4": 3,
      "D5": 3,
      "D6": 3,
      "D7": 4,
      "D8": 3,
      "D9": 2
    },
    "errors": [
      {
        "code": "R-04",
        "severity": "Critical",
        "evidence": "Trích dẫn đoạn lỗi hoặc thông tin bị mất..."
      }
    ]
  },
  "output_b": {
    "hard_fails": [],
    "scores": {
      "D1": 4,
      "D2": 4,
      "D3": 4,
      "D4": 4,
      "D5": 4,
      "D6": 4,
      "D7": 4,
      "D8": 4,
      "D9": 4
    },
    "errors": []
  },
  "winner": "B",
  "rationale": "Giải thích súc tích 2-4 câu dựa trên bằng chứng cụ thể ở Gate 0 và các tiêu chí D1..D9, không dùng từ cảm tính."
}
```
