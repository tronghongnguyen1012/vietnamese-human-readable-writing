# Nhật ký Quyết định Thiết kế & Lộ trình Kế thừa (`DESIGN_DECISIONS.md`)

Tài liệu này ghi lại các quyết định kiến trúc, phản biện cơ sở lý thuyết và các hạng mục còn tồn đọng để bất kỳ Agent hoặc kỹ sư nào tiếp quản dự án đều có thể tiếp tục phát triển mà không phải thử–sai lại từ đầu.

---

## 1. Các Quyết định Thiết kế Chính và Lý do

| Hạng mục | Phương án tham khảo / giả định đầu | Quyết định thực tế | Lý do (kèm cơ sở) |
|---|---|---|---|
| **Cấu trúc thư mục Skill** | `skill/SKILL.md` | `skills/vietnamese-human-readable-writing/SKILL.md` | Chuẩn `agentskills.io` và `agy-customizations` bắt buộc tên thư mục cha khớp chính xác trường `name` trong frontmatter (`[a-z0-9-]`). Đặt dưới `skills/` thay vì `.agents/skills/` giúp cài đặt bằng cách copy 1 thư mục, đồng thời giữ môi trường chạy Baseline hoàn toàn sạch không bị runtime tự nạp Skill. |
| **Số lượng file trong `references/`** | 6 file (`semantic-clarity`, `information-architecture`/`structure`, `natural-vietnamese`, `technical-writing`, `business-writing`, `anti-patterns`) | Gộp còn **4 file định tuyến theo tác vụ** (`vietnamese-clarity-and-style.md`, `information-architecture.md`, `business-specs.md`, `technical-specs.md`) | Trong `SKILL.md`, mỗi chế độ Trung bình/Chặt chỉ cần gọi `read_file` **1 lần** là đủ cả lý thuyết câu–phong cách–lỗi thường gặp hoặc trọn bộ quy chuẩn nghiệp vụ/kỹ thuật, giảm số vòng gọi tool và độ trễ. |
| **Kích thước & ngôn ngữ `SKILL.md`** | Có thể viết dài hoặc viết toàn tiếng Anh | Thân `SKILL.md` tiếng Việt **90 dòng (~1.509 từ)**; `description` tiếng Anh chuẩn trigger `Use when...` (297 ký tự) | Thân tiếng Việt khớp trực tiếp với đầu ra mục tiêu và thuật ngữ Đề–Thuyết/ngữ dụng Việt Nam; `description` ngắn không tóm tắt quy trình giúp tối ưu kích hoạt đa runtime (theo hướng dẫn `writing-skills` về SDO). |
| **Cơ chế phân tầng tải ngữ cảnh** | Áp dụng chung quy trình 9 bước mọi lúc | **Context Triage 3 chế độ (`Nhẹ / Trung bình / Chặt`)** | Kiểm chứng thực nghiệm trên 24 ca Held-Out cho thấy `casual_chat` (3/3) và tin nhắn Teams ngắn (`TEST-10`) giữ `refs=[]` (0 lần đọc reference), trong khi 100% ca đặc tả nạp đúng file chuyên sâu. |
| **Kiến trúc kiểm định chất lượng** | TtCU làm chỉ số chính duy nhất + chấm điểm 9 tiêu chí cộng tổng | **Kiến trúc 2 tầng** + **Gate 0 Hard Fail phi bù trừ** + **Blind Position-Swapped A/B** | TtCU không đo được trên LLM và dễ bị đánh lừa bởi câu văn ngắn nhưng hiểu sai (*Subconscious Disambiguation*, Berry et al., 2003). Gate 0 phi bù trừ ngăn văn phong mượt che giấu lỗi bịa dữ kiện (`HF-3`), vốn xảy ra ở **11/24 ca Baseline Held-Out**. |
| **Cấm từ & ép độ dài câu** | Danh sách từ cấm / quy tắc câu ngắn kiểu CNL | **Ranh giới chống máy móc dựa trên điều kiện quan sát được** | Tuân theo kết luận Việt ngữ học (Cao Xuân Hạo, Nguyễn Đức Dân): *"việc, sự, được, bị"* tự nhiên khi đúng vai Đề ngữ hoặc sắc thái lợi/hại; công thức đếm câu/từ không dùng được cho tiếng Việt (Luong et al., 2020). |

---

## 2. Bài học Thực nghiệm từ Vòng Lặp Phát triển (`v1 → v2 → v3`)

1. **Bẫy "Nuance / Over-broad Rule" trong `SKILL.md` (v1 → v2):** Khi mở rộng quy tắc giữ văn xuôi sang *"đoạn biên tập ngắn (2–4 câu, tối đa 2–3 điều kiện đơn giản)"*, model đã gom cả email thông báo bảo trì B2B (`DEV-16`) thành đoạn văn xuôi liền làm giảm khả năng quét nhanh. Khắc phục ở v3 bằng cách tách thành 2 điều kiện quan sát được rạch ròi (mô tả 1–2 ý thuần túy vs email thông báo vận hành).
2. **Sức mạnh của Bất biến chống bịa chi tiết (`HF-3`):** Chỉ cần một quy tắc rõ ràng *"không tự bịa trường JSON/mã lỗi/quy tắc như sự thật đã chốt; tách riêng vào mục `Đề xuất bổ sung (cần xác nhận)` hoặc `Ví dụ minh họa`"*, tỷ lệ ca mắc Hard Fail giảm từ **7/16 (Dev Baseline)** và **11/24 (Held-Out Baseline)** xuống **0/16 (Dev v1, v2, v3)** và **0/24 (Held-Out)**.
3. **Điểm cân bằng khó ở Chế độ Chuyên gia (`TEST-05`, `DEV-04`):** Khi thúc đẩy cô đọng thông tin (`D6`), model có xu hướng nén quá mức một trong các nhánh kỹ thuật nếu câu hỏi yêu cầu so sánh sâu nhiều trục (*lưu trữ* + *thứ tự* ở `TEST-05`), dẫn tới mất độ sâu hoặc đơn giản hóa chi tiết nội tại (`R-04`).

---

## 3. Bảng Theo dõi Trạng thái Nhận thức luận (Đã kiểm chứng vs Giả thuyết)

| Nhận định / Giả thuyết | Trạng thái hiện tại | Bằng chứng / Ghi chú |
|---|---|---|
| Cấu trúc Đề–Thuyết, giữ "được/bị" đúng sắc thái, chống danh từ hóa rỗng và mơ hồ phạm vi logic có cơ sở ngôn ngữ học cho tiếng Việt | **Có cơ sở lý thuyết vững** | Cao Xuân Hạo (1991), Trần Ngọc Thêm (1985), Đỗ Hữu Châu, Nguyễn Đức Dân, Berry et al. (2003). |
| Skill giảm mạnh lỗi tự bịa dữ kiện (`HF-3/4`) và tăng mật độ thông tin/mạch lạc trên phân tích LLM mù hoán đổi vị trí | **Đã kiểm chứng trong phạm vi 1 họ model (`flash` / `pro`)** | Held-Out `n=24`: `20W / 1L / 3 Inconsistent`; `0/24` vs `11/24` HF; nhóm sạch `n=13` vẫn thắng `10/13` (`D6 +0.846`, `D5 +0.654`). |
| Cơ chế Progressive Disclosure giữ nhẹ hội thoại hằng ngày (`refs=[]`) và chỉ nạp 1 reference cho tác vụ sâu | **Đã kiểm chứng thực tế trên runtime Antigravity** | `casual_chat` `0/3` nạp ref, `avg_words = 137,3`; `business_docs`/`technical_docs`/`editing_rewriting` `3/3` nạp đúng 1 ref. |
| Skill giảm **Time to Correct Understanding (TtCU)** và giảm số lần phải hỏi lại trên người Việt thực tế | **Giả thuyết chưa kiểm chứng** | Đã thiết kế quy trình đo chuẩn tại `evaluation/human-eval-protocol.md`, chưa thực thi thực nghiệm trên người dùng. |
| Hiệu quả của Skill giữ ổn định trên các họ LLM khác (GPT, Claude, model tiếng Việt nội địa) | **Giả thuyết chưa kiểm chứng** | Chưa chạy kiểm thử đa model để tránh phát sinh chi phí API ngoài. |

---

## 4. Hạng mục Tồn đọng cho Phiên bản Tiếp theo (v3.1 / v4)

1. **Thực thi Human Evaluation (`evaluation/human-eval-protocol.md`):** Chạy thí nghiệm mù Latin Square trên 12–16 người Việt (BA, Dev, CSKH/Vận hành) để đo TtCU có cổng kiểm chứng hiểu đúng và đối chiếu xem kết quả có khớp với phán quyết của LLM Judge hay không.
2. **Bổ sung hướng dẫn cân bằng chiều sâu đa trục cho Chế độ Chuyên gia (`information-architecture.md`):** Khắc phục bài học từ `TEST-05` — khi người dùng chuyên sâu hỏi so sánh ≥ 2 trụ cột kỹ thuật (ví dụ *cơ chế lưu trữ* và *bảo đảm thứ tự*), yêu cầu giữ đủ độ sâu cho **từng trục được nêu** và kiểm tra lại các trường hợp biên khi viết ngắn trong bảng (`R-04`).
3. **Bổ sung nguyên tắc kiểm chứng lệnh thực thi phổ biến trong `casual_chat` (`TEST-02`):** Nhắc kiểm tra không gộp trường hợp *"Git bản cũ"* với *"repo chưa có commit"* khi đưa mẹo lệnh thao tác nhanh (`git reset HEAD` vs `git rm --cached`).
4. **Kiểm thử chéo đa model & đa giám khảo:** Đánh giá lại 24 ca `held-out-test.jsonl` trên tối thiểu 2 họ mô hình sinh khác nhau và sử dụng giám khảo độc lập khác họ mô hình sinh để loại trừ Self-Enhancement Bias.
