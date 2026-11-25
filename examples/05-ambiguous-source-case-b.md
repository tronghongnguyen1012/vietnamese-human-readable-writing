# Ví dụ 5: Nguồn Thiếu Dữ kiện — Chống "Độ Rõ Giả Tạo" (`H2-07`)

- **Nguồn dữ liệu:** Ca `H2-07` ([held-out-v2.jsonl](../evaluation/held-out-v2.jsonl)), đối chiếu giữa `Group A` ([held-out-v2-gen-A.jsonl](../evaluation/results-v2/held-out-v2-gen-A.jsonl)) và `Group C Skill v4` ([held-out-v2-gen-C.jsonl](../evaluation/results-v2/held-out-v2-gen-C.jsonl)).
- **Mục tiêu kiểm chứng:** Khi văn bản nguồn mơ hồ hoặc khuyết tác thể/giao thức (**Trường hợp B**), Skill **không** tự bịa tên phân hệ hay cơ chế truyền dẫn mà tách phần đã biết khỏi danh sách câu hỏi chốt trước khi viết đặc tả.

## Prompt đầu vào
> Biên tập hoặc làm rõ câu tài liệu sau để kỹ sư và BA không hiểu nhầm (TUYỆT ĐỐI không tự bịa thêm tên hệ thống hay cơ chế không có trong câu gốc): 'Hệ thống thực hiện đồng bộ trạng thái giao dịch giữa các phân hệ liên quan nhằm đảm bảo tính nhất quán.'

## So sánh Đầu ra Thực tế

- **`AI Mặc định` (`Group A` — bị Blind Judge gắn `HF-5`):**
  Trong Mục 1 có liệt kê các điểm dễ hiểu nhầm, nhưng tới **Phương án B** lại không chỉ rõ câu gốc còn khuyết điều kiện gì và đặt mẫu điền khuyết lẫn lộn với bản viết lại tổng quát khiến người đọc thiếu bức tranh tách bạch phần an toàn vs phần chặn triển khai (`[...]` trong [held-out-v2-gen-A.jsonl](../evaluation/results-v2/held-out-v2-gen-A.jsonl)).
  *(Lưu ý: ở các ca thiếu dữ kiện tự nhiên không có cảnh báo `TUYỆT ĐỐI` trong prompt như `H2-09`, `H2-10`, `H2-17`, `H2-18`, `H2-19`, cả AI mặc định lẫn Simple Prompt đều tự bịa thẳng tên hệ thống/giao thức/field API — lỗi `HF-3`.)*

- **`ViWrite` (`Skill v4`, thắng `2–0` trước cả Group A, B và C0):**
> Câu gốc đang **thiếu dữ kiện cốt lõi**, không chỉ là vấn đề diễn đạt. Dù có chỉnh lại câu chữ mượt hơn, kỹ sư và BA vẫn chưa thể dựa vào đây để chốt đặc tả hay thiết kế nếu chưa xác định rõ các tham số còn khuyết.
>
> ### 1. Bản rút gọn an toàn (giữ đúng phạm vi câu gốc)
> > *"Hệ thống đồng bộ trạng thái giao dịch giữa các phân hệ liên quan để giữ dữ liệu nhất quán."*
>
> ### 2. Điểm chưa xác định / cần chốt trước khi đưa vào tài liệu đặc tả
> 1. **Tác thể và hướng đồng bộ:** `"Hệ thống"` và `"các phân hệ liên quan"` là những phân hệ cụ thể nào? Phân hệ nào giữ dữ liệu chuẩn (nguồn phát), phân hệ nào nhận cập nhật, hay đồng bộ hai chiều?
> 2. **Phạm vi dữ liệu:** Áp dụng cho loại giao dịch nào, và đồng bộ toàn bộ vòng đời trạng thái hay chỉ một số trạng thái nhất định?
> 3. **Điều kiện kích hoạt:** Đồng bộ ngay khi trạng thái giao dịch thay đổi, theo một sự kiện cụ thể khác, hay chạy gom định kỳ?
> 4. **Mức độ "nhất quán":** Yêu cầu đồng bộ tức thời ngay trong cùng luồng xử lý, hay chấp nhận độ trễ (nếu có thì độ trễ tối đa cho phép là bao nhiêu)?
> 5. **Cơ chế và xử lý ngoại lệ:** Các phân hệ giao tiếp qua giao thức/cơ chế nào? Khi đồng bộ thất bại hoặc lệch dữ liệu thì hệ thống xử lý ra sao (thử lại, đối soát bù, ghi nhận lỗi hay hoàn tác)?
>
> ### 3. Khung câu chuẩn hóa (điền sau khi chốt thông tin)
> > *"Khi `[điều kiện kích hoạt]`, `[phân hệ nguồn]` gửi trạng thái `[phạm vi trạng thái]` của `[loại giao dịch]` sang `[phân hệ đích]` qua `[giao thức/cơ chế]`, đảm bảo dữ liệu khớp nhau trong `[ngưỡng thời gian / yêu cầu nhất quán]`. Nếu đồng bộ thất bại, hệ thống thực hiện `[cơ chế xử lý lỗi / đối soát]`."*
