# Ví dụ 5: Nguồn Thiếu Tham số — Không Tự Điền Quy tắc Ngoài Nguồn (`H2-10`)

- **Nguồn dữ liệu:** Ca `H2-10` ([held-out-v2.jsonl](../evaluation/held-out-v2.jsonl)), đối chiếu giữa `Group A` ([held-out-v2-gen-A.jsonl](../evaluation/results-v2/held-out-v2-gen-A.jsonl)) và `Group C Skill v4` ([held-out-v2-gen-C.jsonl](../evaluation/results-v2/held-out-v2-gen-C.jsonl)).
- **Kết quả Blind Judge (`pro`, 2 lượt hoán đổi vị trí):** **ViWrite thắng đồng thuận `2–0`** ([held-out-v2-judge-C-vs-A.jsonl](../evaluation/results-v2/held-out-v2-judge-C-vs-A.jsonl)). `Group A` mắc lỗi **Hard Fail `HF-3`** cả 2/2 lượt; `Group C` đạt `0 HF`.

## Prompt đầu vào
> Rà soát và viết lại rõ ràng quy tắc tính phí bên dưới; nếu thiếu công thức hoặc ngưỡng thì giữ trung thực và liệt kê điểm cần chốt: 'Đối tác giao trễ tiến độ cam kết sẽ bị áp dụng mức phạt hợp lý tương ứng với mức độ trễ và giá trị đơn hàng.'

## So sánh Đầu ra Thực tế

### `AI Mặc định` (`Group A` — Dính `HF-3` cả 2/2 lượt)
Ngay trong **Mục 2 (`Bản viết lại rõ ràng (giữ nguyên phần chưa có dữ liệu để chờ chốt)`)**, AI mặc định viết nguyên văn như sau:

> **Quy tắc phạt giao hàng trễ tiến độ:**
> Trường hợp Đối tác giao hàng chậm so với thời hạn cam kết được xác nhận trên đơn hàng/hợp đồng (sau khi trừ thời gian ân hạn, nếu có `[cần chốt]`), Đối tác sẽ chịu khoản phí phạt trễ tiến độ. Mức phạt được xác định căn cứ trên **thời gian giao trễ thực tế** *(tính theo `[đơn vị thời gian cần chốt]`)* và **`[toàn bộ giá trị đơn hàng / giá trị phần hàng giao trễ - cần chốt]`** theo công thức/biểu mức phạt `[công thức hoặc bảng mức phạt cần chốt]`, nhưng không vượt quá mức phạt tối đa là `[ngưỡng trần cần chốt]`.
>
> **Quy định này không áp dụng nếu việc chậm trễ phát sinh do sự kiện bất khả kháng, do lỗi từ phía Bên đặt hàng, hoặc đã được hai bên thống nhất gia hạn bằng văn bản trước thời điểm đến hạn.**

**Vì sao Giám khảo gắn lỗi `HF-3`:** Dù đặt tiêu đề *"giữ nguyên phần chưa có dữ liệu để chờ chốt"*, AI mặc định lại tự khẳng định thêm nguyên một đoạn điều khoản miễn trừ (kể cả điều kiện *"thống nhất gia hạn bằng văn bản trước thời điểm đến hạn"*) không có trong câu gốc mà không gắn nhãn `[cần chốt]` hay `[Giả định]`, mâu thuẫn với danh sách câu hỏi mở ở Mục 3.6; đồng thời mặc định tồn tại ngưỡng trần theo quy tắc chung.

---

### `ViWrite` (`Skill v4`, `Group C` — `0 HF`, thắng `2–0`)
> ### 1. Rà soát câu quy tắc gốc
>
> Câu gốc (*"Đối tác giao trễ tiến độ cam kết sẽ bị áp dụng mức phạt hợp lý tương ứng với mức độ trễ và giá trị đơn hàng."*) chưa đủ điều kiện để triển khai hệ thống hoặc viết ca kiểm thử (test case) vì các lý do sau:
> - **Tính từ mơ hồ, không kiểm chứng được:** Cụm *"mức phạt hợp lý"* không nêu công thức, tỷ lệ hay bảng ngưỡng cụ thể.
> - **Thiếu định nghĩa biến đầu vào và biên áp dụng:** Chưa xác định cách đo *"mức độ trễ"* (mốc đối chiếu, đơn vị tính, thời gian ân hạn nếu có) và cơ sở tính *"giá trị đơn hàng"*.
> - **Thiếu chủ thể thực thi và ngoại lệ:** Chưa rõ bên/hệ thống nào tính và khấu trừ phạt, cũng như các trường hợp miễn trừ khi trễ không do lỗi đối tác.
>
> ---
>
> ### 2. Viết lại rõ ràng phần đã xác định từ nguồn
>
> > **Quy tắc áp dụng phạt giao trễ (Bản nháp — chưa đủ tham số tính toán):**
> > - **Điều kiện kích hoạt:** Đối tác giao hàng muộn hơn tiến độ đã cam kết.
> > - **Hệ quả:** Đối tác bị tính phí phạt dựa trên **mức độ trễ** và **giá trị đơn hàng**, theo công thức và bảng ngưỡng **[Điểm chưa xác định / cần chốt]**.
>
> *(Lưu ý: Phần định lượng mức phạt hiện bỏ trống có chủ đích để tránh tạo thông số giả ngoài tài liệu nguồn.)*
>
> ---
>
> ### 3. Các điểm chưa xác định / cần chốt trước khi triển khai
>
> 1. **Cách xác định "mức độ trễ":**
>    - Thời gian trễ được tính từ mốc cam kết nào (mốc ban đầu trên đơn hay mốc gia hạn đã được duyệt)?
>    - Đơn vị tính độ trễ là phút, giờ hay ngày; làm tròn như thế nào?
>    - Có thời gian ân hạn (grace period) trước khi bắt đầu tính phạt không, và biên điều kiện là `>` hay `>=` ngưỡng quy định?
> 2. **Cơ sở xác định "giá trị đơn hàng":**
>    - Tính trên giá trị hàng hóa trước hay sau khuyến mãi/thuế, có bao gồm phí vận chuyển hoặc phụ phí khác không?
>    - Trường hợp đơn giao làm nhiều đợt và chỉ trễ một phần, mức phạt áp dụng trên toàn đơn hay chỉ phần hàng giao trễ?
> 3. **Công thức tính và giới hạn mức phạt:**
>    - Phạt tính theo số tiền cố định, theo phần trăm (`%`) giá trị đơn hàng, hay lũy tiến theo từng bậc trễ (cần bảng phân tầng cụ thể)?
>    - Có mức phạt tối thiểu (sàn) hoặc tối đa (trần) cho mỗi đơn hàng không?
> 4. **Cơ chế xử lý và trường hợp ngoại lệ:**
>    - Phí phạt do hệ thống tự động tính hay cần nhân sự vận hành duyệt; khấu trừ trực tiếp vào kỳ đối soát công nợ của đối tác hay thu riêng?
>    - Các tình huống nào được miễn phạt (ví dụ: bất khả kháng, khách hàng hẹn lại giờ nhận, hoặc lỗi từ phía đơn vị đặt hàng/điều phối)?

---

### Tham chiếu thêm trong cùng nhóm Trường hợp B
- **`H2-09` (Quy định chống spam `3 lần vi phạm liên tiếp`):** `Group A` cũng mắc `HF-3` (tự điền chủ thể `"Hệ thống"` vào luồng và chốt `"đồng thời gửi cảnh báo"` dù mục câu hỏi mở vẫn đang hỏi thứ tự thực hiện), còn `Skill v4` thắng `2–0` và đạt `0 HF`. Xem nguyên văn tại [`held-out-v2-gen-A.jsonl`](../evaluation/results-v2/held-out-v2-gen-A.jsonl) và [`held-out-v2-gen-C.jsonl`](../evaluation/results-v2/held-out-v2-gen-C.jsonl).
- **`H2-07` (Đồng bộ trạng thái giao dịch giữa các phân hệ):** Cả hai nhóm không bịa tên hệ thống cụ thể vì prompt gốc ghi lệnh cấm tường minh (`TUYỆT ĐỐI không tự bịa thêm tên hệ thống`), nhưng `Group A` mắc lỗi **Hard Fail `HF-5`** vì bỏ sót yếu tố `"cách truyền"` (cơ chế/giao thức giao tiếp), còn `Skill v4` chỉ rõ đủ 5 tham số khuyết và thắng `2–0`.
