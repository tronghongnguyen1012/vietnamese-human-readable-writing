# Bảng Đối chiếu Nguyên tắc: `v4.1` vs `V5-A` vs `V5-B`

## 1. So sánh Kích thước & Mức Tải Context Tĩnh (`SKILL.md`)

| Phiên bản | Định hướng thiết kế | Số dòng | Số từ | Kích thước (bytes) | Ước lượng token (`bytes / 3,8`) | Chênh lệch vs `v4.1` |
|---|---|---:|---:|---:|---:|---|
| **`v4.1` (Group B)** | Tài liệu chuẩn hóa ngữ nghĩa + bảo toàn đặc tả | 82 | 1.333 | 8.986 | ~2.365 | Baseline |
| **`v4.1 + SR` (Group C)** | `v4.1` nối thêm khối Semantic Reconstruction | 102 | 1.564 | 10.422 | ~2.743 | +16,0% |
| **`V5-A` (Group E)** | Tái cấu trúc `v4.1` theo *Understand → Communicate → Verify* | 63 | 1.028 | 6.674 | ~1.756 | **−25,7%** |
| **`V5-B` (Group F)** | Viết lại từ đầu theo khung tối giản *Communication-First* | 47 | 665 | 4.413 | ~1.161 | **−50,9%** |

*(Cả 4 biến thể dùng chung nguyên trạng 4 tệp trong `references/` để cô lập tác động của thiết kế `SKILL.md`.)*

---

## 2. Đối chiếu Từng Nguyên tắc: Giữ lại · Loại bỏ · Thay đổi

| Nhóm quy tắc / Thành phần | Trong `v4.1` | Trong `V5-A` | Trong `V5-B` | Lý do dựa trên bằng chứng `SR` |
|---|---|---|---|---|
| **Phân biệt mục đích tác vụ (4 chế độ)** | Trộn *viết lại thông báo* vào **Trường hợp B** cùng nhóm *soạn đặc tả thiếu thông tin*. | **Thêm bắt buộc (Mục 1):** Tách 4 chế độ (*Thành phẩm dùng ngay* / *Review* / *Đặc tả triển khai* / *Hội thoại–Giải thích*). | **Thêm gọn (Mục 2):** Nêu thẳng không tự biến thông báo/SOP thành báo cáo rà soát. | `SR-01` & `SR-07` Group B tự gắn khối *"Điểm chưa xác định"* vào thành phẩm gửi người đọc cuối. |
| **Quy trình Understand → Communicate** | Nằm rải rác ở Mục 1 và Mục 4 (*"tác thể–hành động"*, *"Đề–Thuyết"*). | **Tái cấu trúc (Mục 2):** Đưa *Understand* lên trước (hiểu sự việc, người đọc, mục đích) → *Communicate* (tái tạo toàn mạch). | **Cốt lõi (Mục 1):** Mô hình 2 bước trực diện, nhấn mạnh viết lại từ đầu thay vì tỉa từng câu. | Giúp phá vỡ cấu trúc câu dài/lộn xộn tốt hơn (`SR-04`, `SR-06`, `SR-07`). |
| **Giải mã từ hành chính vs giữ thuật ngữ thật** | Gộp chung *"Giữ chính xác định danh/API/trạng thái"* → model giữ luôn từ hành chính như `"tạm treo"`, `"đối soát định kỳ"`. | **Thay đổi rõ:** Tách **thuật ngữ chuyên môn/định danh thật** vs **cụm hành chính sáo rỗng** để chủ động đổi sang tiếng Việt tự nhiên. | **Thay đổi ngắn gọn:** Nêu nguyên tắc *"giữ thuật ngữ thật, đổi từ hành chính sang tác động thực tế"* kèm 3 ví dụ ngắn. | Khoảng cách lớn nhất trên `SR-01` giữa Gemini (`39–49%` trùng 3-gram) và GPT-6.2 (`16,9%`). |
| **Linh hoạt cấu trúc (không ép BLUF/bảng)** | Khuyến nghị *BLUF trước* dễ bị hiểu thành luôn dùng heading/bullet/bảng. | **Nêu rõ:** Cấu trúc phục vụ nội dung; **không** mặc định BLUF/bảng/bullet hay tạo thêm tầng tiêu đề làm màu. | **Nêu rõ:** Chọn cấu trúc tự nhiên cho từng việc; cấm thêm tầng tiêu đề chỉ để trông chuyên nghiệp. | Ngăn over-formatting ở thông báo ngắn và hội thoại tự nhiên. |
| **Chống bịa & giữ nguyên mức bất định** | Mục 2.2 & 2.4 đầy đủ nhưng lặp ý giữa Trường hợp B, giữ nguyên trạng thái, bất biến bảo toàn. | **Giữ đủ ở Pha 3 (Verify):** Gộp gọn còn 3 gạch đầu dòng rõ ràng, nhấn thêm không đổi `có thể ↔ sẽ` và không thu hẹp định dạng yêu cầu. | **Giữ cốt lõi ở Mục 3:** Rút gọn thành 3 ràng buộc trực tiếp + câu chuyển *"kiểm chứng không phải cớ giữ văn khó hiểu"*. | Vá 2 phát hiện ở Lớp 1: `SR-01 B_prior` (`có thể → sẽ`) và `SR-07 C` (`phiếu giao hàng → ảnh chụp`). |
| **Kiểm chứng khẳng định kỹ thuật & chiều sâu đa trục** | Chiếm trọn Mục 3 + Mục 4.4 (checklist 6 câu tự kiểm tra). | **Giữ nguyên bản chất** trong Pha 3.3 (bỏ checklist 6 câu lặp lại để giảm độ dài). | **Giữ ngắn gọn 1 câu** về chiều sâu & phân biệt dữ kiện đã kiểm chứng với giả định; giao chi tiết cho `technical-specs.md`. | Giữ an toàn kỹ thuật (`RPO > 0`, `split-brain`, lock mode) mà không gây quá tải prompt nền. |
| **Thuật ngữ ngôn ngữ học nội bộ (*Đề–Thuyết, 4 lớp nội dung, Gate/Semantic Check*)** | Dùng nhiều thuật ngữ phân tích (*Đề–Thuyết*, *4 lớp nội dung*, *Kiểm tra Ngữ nghĩa Cuối*). | **Loại bỏ hầu hết** tên nhãn nội bộ; đổi thành hành động cụ thể. | **Loại bỏ 100%** thuật ngữ ngôn ngữ học nội bộ. | Model thực tế tuân thủ tốt hơn khi hướng dẫn bằng hành động giao tiếp rõ ràng thay vì lý thuyết ngôn ngữ học. |
| **Progressive Disclosure (`references/`)** | Chiếm ~9 dòng chi tiết cơ chế Tool / Fallback trong Mục 1. | **Rút gọn còn 2 dòng** ngay đầu bảng `references/`. | **Rút gọn còn 1 dòng chú thích** ở cuối `SKILL.md`. | Trong `experiment/semantic-reconstruction`, 20/20 lượt B & C không đọc file ngoài nên `SKILL.md` phải tự đủ lực cho tác vụ phổ thông. |
