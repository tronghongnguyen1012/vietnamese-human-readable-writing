# Ví dụ 1: Hội thoại Tự nhiên (`H2-14`)

- **Nguồn dữ liệu:** Ca `H2-14` ([held-out-v2.jsonl](../evaluation/held-out-v2.jsonl)), bản sinh [targeted-regression-v41-gen.jsonl](../evaluation/results-v4.1/targeted-regression-v41-gen.jsonl).
- **Mục tiêu kiểm chứng:** Khi người dùng trò chuyện ngắn cần hài hước/đồng cảm, Skill giữ nguyên chế độ Nhẹ (`refs = []`), **không** ép khung đề mục hay giảng bài học về Auto Save.

## Prompt đầu vào
> Đang debug cả buổi sáng tới giờ mới phát hiện lỗi nằm ở việc quên lưu file trước khi chạy test, cay quá. Nói câu gì an ủi nhẹ nhàng pha chút hài hước mà đừng giảng đạo lý nghe.

## Đầu ra `AI Mặc định` (`Group A` — `57` từ)
> Thôi đừng cay nữa, nghĩ tích cực lên: hoá ra cả buổi sáng nay bạn code chuẩn đét từ đầu rồi, chỉ là chiếc máy tính chưa được cấp quyền biết thôi. Chúc mừng bạn vừa có màn lội ngược dòng đầy kịch tính trước phiên bản quá khứ của chính mình chỉ bằng một cú Ctrl+S!

## Đầu ra `ViWrite` (`Skill v4.1` — `56` từ, `refs = []`, `7,4s`)
> Chia buồn sâu sắc với buổi sáng của bạn! Nhưng nhìn theo hướng tích cực thì ít ra giờ cũng có bằng chứng thép: code bạn viết không hề sai, chỉ là cái ổ cứng chưa kịp biết đến sự xuất sắc đó thôi. Đúng là cú plot twist tốn năng lượng nhất hệ mặt trời.

## Nhận xét nhanh
- Cả hai bản đều đạt Gate 0 (`0 HF`, không giảng đạo lý). Trong lượt chấm mù `pro`, `Skill v4.1` giữ tự nhiên, gọn hơn cả bản v4 trước đó (từng bị trừ điểm ở cụm *"tập bài khởi động não bộ miễn phí"* hơi sách vở) và không tốn chi phí đọc bất kỳ reference nào (`refs = []`).
