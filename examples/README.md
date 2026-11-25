# Ví dụ Thực tế từ Bộ Kiểm thử (`examples/`)

> **Nguồn gốc dữ liệu:** Toàn bộ 5 ví dụ dưới đây được trích **nguyên văn** từ kết quả benchmark thực tế đã lưu trong [`evaluation/results/`](../evaluation/results/), [`evaluation/results-v2/`](../evaluation/results-v2/) và [`evaluation/results-v4.1/`](../evaluation/results-v4.1/) (tier sinh `flash`, chấm mù `pro`). Những đoạn dài có lược bớt đều ghi rõ `[...]` kèm liên kết tới tệp nguồn đầy đủ — không tự chế số liệu hay ví dụ giả làm kết quả benchmark.

| Tài liệu | Ngữ cảnh | Mã ca thực tế | Điểm minh họa cốt lõi |
|---|---|---|---|
| [01-natural-conversation.md](./01-natural-conversation.md) | Hội thoại tự nhiên | `H2-14` (`v4.1`) | Không bị biến thành báo cáo, không giảng đạo lý, không mở reference (`refs=[]`, 56 từ). |
| [02-workplace-communication.md](./02-workplace-communication.md) | Giao tiếp công việc (Teams) | `TEST-10` (`v4`) | BLUF 3 giây đầu, giảm từ 152 xuống 100 từ, chia việc FE/BE sắc nét. |
| [03-business-rule-and-prd.md](./03-business-rule-and-prd.md) | Business Rule & Phạm vi | `H2-12` (`v4.1`) | Phân tách Scope & Proportion (3 tầng), không tự chốt ngầm ngưỡng `30.000đ` / `Điện máy`. |
| [04-technical-and-sad.md](./04-technical-and-sad.md) | RFC Kỹ thuật & SAD + BR | `H2-06`, `H2-19` (`v4.1`) | Kiểm chứng lock mode PostgreSQL (`H2-06`) và đồng bộ trạng thái `[Chưa chốt]` trên sơ đồ Mermaid (`H2-19`). |
| [05-ambiguous-source-case-b.md](./05-ambiguous-source-case-b.md) | Nguồn thiếu dữ kiện (Trường hợp B) | `H2-10` (`v4`, cùng tham chiếu `H2-09`, `H2-07`) | Giữ phạm vi nguồn & tách rõ điểm cần chốt thay vì tự khẳng định điều khoản miễn trừ ngoài nguồn (`HF-3`). |
