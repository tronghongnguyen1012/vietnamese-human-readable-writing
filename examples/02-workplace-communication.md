# Ví dụ 2: Giao tiếp Công việc trên Teams (`TEST-10`)

- **Nguồn dữ liệu:** Ca `TEST-10` ([held-out-test.jsonl](../evaluation/held-out-test.jsonl)), đối chiếu giữa `baseline_output` ([held-out-raw-results.jsonl](../evaluation/results/held-out-raw-results.jsonl)) và `v4_output` ([regression-v4-raw.jsonl](../evaluation/results-v2/regression-v4-raw.jsonl)).
- **Mục tiêu kiểm chứng:** Tin nhắn công việc cần đi thẳng trọng tâm (BLUF), gom việc theo đúng người nhận (`FE` vs `BE`) và bỏ rào đón dư thừa.

## Prompt đầu vào
> Viết tin nhắn gửi nhóm dự án trên Teams báo thay đổi scope gấp: khách hàng vừa chốt dời tính năng 'Xuất báo cáo Excel theo chi nhánh' sang Phase 2 (tuần sau), giữ nguyên bản web view cho release thứ Năm tuần này (04/12); các bạn FE bỏ qua phần nút Export Excel nhưng BE vẫn giữ nguyên schema API hiện tại để tuần sau nối tiếp.

## Trước (`AI Mặc định Baseline` — `152` từ)
> Chào cả team,
>
> Mình xin cập nhật gấp một thay đổi về scope cho đợt release tuần này để mọi người kịp điều chỉnh:
>
> **[CẬP NHẬT SCOPE GẤP - RELEASE THỨ NĂM (04/12)]**
>
> * **Nội dung thay đổi:** Khách hàng vừa chốt dời tính năng **"Xuất báo cáo Excel theo chi nhánh"** sang **Phase 2 (tuần sau)**.
> * **Phạm vi release tuần này (thứ Năm, 04/12):** Vẫn giữ nguyên bản **web view** như kế hoạch.
> * **Action cho từng team:**
>   * **@FE:** Tạm bỏ qua phần nút **Export Excel** trong đợt release này.
>   * **@BE:** Vẫn **giữ nguyên schema API hiện tại**, không cần chỉnh sửa hay gỡ bỏ để tuần sau team tiếp tục nối tiếp cho Phase 2.
>
> Mọi người nắm thông tin và điều chỉnh giúp mình nhé. Nếu có vướng mắc gì báo lại mình ngay để xử lý kịp tiến độ thứ Năm. Cảm ơn cả team!

## Sau (`Skill v4` — `100` từ, `refs = []`, giảm ~34% độ dài)
> **[Cập nhật gấp – Thay đổi scope release thứ Năm (04/12)]**
>
> Chào cả team, khách hàng vừa chốt dời tính năng **"Xuất báo cáo Excel theo chi nhánh"** sang **Phase 2 (tuần sau)**. Đợt release **thứ Năm tuần này (04/12)** sẽ chỉ giữ nguyên phần **web view**.
>
> Nhờ các bạn điều chỉnh công việc theo phạm vi mới:
> - **FE:** Bỏ qua phần nút Export Excel cho đợt release này.
> - **BE:** Giữ nguyên schema API hiện tại để tuần sau nối tiếp cho Phase 2.
>
> Mọi người cập nhật giúp mình để kịp tiến độ release thứ Năm nhé!

## Nhận xét nhanh
- Cả hai đều bảo toàn đầy đủ dữ kiện (`0 HF`). Bản Skill bỏ câu mở bài khuôn mẫu và danh sách 2 cấp lồng nhãn dư thừa (*"Nội dung thay đổi"*, *"Action cho từng team"*), giúp đồng nghiệp nắm trọn phạm vi mới trong vài giây đầu mà không sót việc của FE/BE.
