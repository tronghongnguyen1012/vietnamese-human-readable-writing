# Ví dụ 3: Business Rule & Phạm vi (`H2-12`)

- **Nguồn dữ liệu:** Ca `H2-12` ([held-out-v2.jsonl](../evaluation/held-out-v2.jsonl)), bản sinh [targeted-regression-v41-gen.jsonl](../evaluation/results-v4.1/targeted-regression-v41-gen.jsonl).
- **Mục tiêu kiểm chứng:** Khi câu quy tắc nghiệp vụ có nhiều cụm đa nghĩa lồng nhau (*"tối đa 30.000đ"*, *"không áp dụng kèm mã giảm giá khác hoặc sản phẩm thuộc danh mục Điện máy"*), Skill phân tách đúng phạm vi ảnh hưởng và đưa ra các phương án viết lại có điều kiện mà không chọn ngầm thay bộ phận Kinh doanh.

## Prompt đầu vào
> Phân tích và đề xuất cách viết lại (có điều kiện) cho quy tắc khuyến mãi sau mà không tự chọn một cách hiểu thay cho bộ phận Kinh doanh: 'Miễn phí vận chuyển tối đa 30.000đ cho khách hàng thân thiết mua đơn hàng từ 500.000đ không áp dụng kèm mã giảm giá khác hoặc sản phẩm thuộc danh mục Điện máy.'

## Trích đoạn Đầu ra `ViWrite` (`Skill v4.1` — `0 HF`, `0 Major`, thắng `2–0` trước `v4`)
> Câu quy tắc gốc đang có **nhiều điểm đa nghĩa về phạm vi loại trừ và cách tính ngưỡng**, nên chưa thể viết lại thành một quy tắc đơn nghĩa duy nhất nếu bộ phận Kinh doanh chưa chốt hướng xử lý.
>
> ### 1. Dữ kiện bất biến từ câu gốc
> - **Đối tượng hưởng ưu đãi:** Khách hàng thân thiết.
> - **Mức ưu đãi:** Miễn phí vận chuyển tối đa `30.000đ`.
> - **Điều kiện giá trị đơn hàng:** Từ `500.000đ` (`>= 500.000đ`).
> - **Yếu tố loại trừ:** `"mã giảm giá khác"` và `"sản phẩm thuộc danh mục Điện máy"`.
>
> ### 2. Phân tích các điểm chưa xác định / đa nghĩa cần Kinh doanh chốt
> #### (a) Điểm chưa rõ ảnh hưởng trực tiếp đến cách viết lại
> 1. **Phạm vi loại trừ đối với `"sản phẩm thuộc danh mục Điện máy"`:**
>    - **Cách hiểu A1 (Loại trừ cả đơn hàng):** Nếu đơn hàng có chứa ít nhất 1 sản phẩm thuộc danh mục Điện máy thì **toàn bộ đơn hàng** không được hưởng ưu đãi.
>    - **Cách hiểu A2 (Chỉ loại trừ dòng sản phẩm Điện máy):** Sản phẩm Điện máy không được tính vào điều kiện hoặc ưu đãi, nhưng phần sản phẩm thuộc danh mục khác trong cùng đơn vẫn được xét miễn phí vận chuyển.
> 2. **Phạm vi của `"không áp dụng kèm mã giảm giá khác"`:** B1 (chặn mọi mã giảm giá) vs B2 (chỉ chặn mã vận chuyển khác).
> 3. **Cơ chế xử lý của `"Miễn phí vận chuyển tối đa 30.000đ"`:**
>    - **Cách hiểu C1 (Trần hỗ trợ):** Giảm tối đa `30.000đ` trên phí vận chuyển; nếu phí vận chuyển `> 30.000đ`, khách hàng trả phần chênh lệch.
>    - **Cách hiểu C2 (Ngưỡng đủ điều kiện):** Chỉ miễn phí vận chuyển cho đơn có phí vận chuyển `<= 30.000đ`; nếu phí vận chuyển `> 30.000đ` thì không áp dụng ưu đãi.
>
> `[...]` *(Phần 2(b) tách riêng điểm cần chốt trước triển khai, Phần 2(c) tách câu hỏi mở rộng tùy chọn, Phần 3 cung cấp phương án viết lại có điều kiện và Phần 4 là bảng checkbox chốt nhanh cho Kinh doanh — xem nguyên văn trong [targeted-regression-v41-gen.jsonl](../evaluation/results-v4.1/targeted-regression-v41-gen.jsonl).)*

*(Tham khảo thêm ví dụ PRD lai API Contract ở ca `H2-17` trong [`held-out-v2-gen-C.jsonl`](../evaluation/results-v2/held-out-v2-gen-C.jsonl), nơi Skill thắng `2–0` trước cả Neutral Baseline A lẫn Simple Prompt B nhờ không bịa trường HTTP response hay rule chưa chốt.)*
