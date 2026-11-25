# Nhật ký Quyết định Thiết kế & Lộ trình Kế thừa (`DESIGN_DECISIONS.md`)

Tài liệu ghi lại các quyết định kiến trúc qua hai vòng phát triển (**Round 1: v1–v3** và **Round 2: v4 Stabilization**), bằng chứng thực nghiệm đối chứng và các điểm tồn đọng thực tế cho phiên bản kế tiếp.

---

## 1. Các Quyết định Thiết kế Cốt lõi (Từ v1 đến v4)

| Hạng mục | Giả định / Thiết kế cũ (v3) | Quyết định hiện tại (v4) | Lý do & Bằng chứng |
|---|---|---|---|
| **Cấu trúc Skill** | `skills/vietnamese-human-readable-writing/SKILL.md` (90 dòng, `10.069 bytes`) | Giữ vị trí chuẩn `agentskills.io`, tinh gọn `SKILL.md` còn **78 dòng (`9.132 bytes`)** | Tách sạch Skill cài đặt khỏi nghiên cứu/eval; giảm kích thước thân ~13,7% nhưng bổ sung quy tắc Trường hợp B và phân lớp chiều sâu kỹ thuật. |
| **Progressive Disclosure (`FIX-05`)** | Hardcode *"Chỉ dùng `read_file` mở đúng 1 file"* | Cơ chế **`0 → 1 → tối đa 2 file`**, **không nhắc tên tool `read_file`**, có fallback nếu host không có tool | Tài liệu lai (`H2-17..20`, `TEST-19`) cần phối hợp 2 mảng (ví dụ `business-specs.md` + `technical-specs.md`). Thực tế trên Held-Out v2: `2/24` ca đọc 0 file, `13/24` đọc 1 file, `9/24` đọc 2 file. |
| **Chế độ Nhẹ & Hội thoại (`FIX-04`)** | Ép cứng *"2–6 câu, hoặc tối đa 3 gạch đầu dòng"* | Gỡ trần câu/bullet; điều chỉnh độ dài theo ý định, mạch nhiều lượt và tôn trọng yêu cầu phong cách riêng của người dùng | Ngăn gãy mạch hội thoại sâu (`H2-15`) và không phá vỡ yêu cầu viết đoạn văn xuôi liền mạch (`H2-16`). |
| **Bảo toàn chiều sâu kỹ thuật (`FIX-02`)** | Dễ nén mỏng một trục khi câu hỏi kỹ thuật yêu cầu đa khía cạnh (`TEST-05`) | Phân biệt rõ 4 lớp nội dung; buộc giữ đủ chiều sâu trên **từng trục** và kiểm chứng tính nhất quán cơ chế | Trên Regression `v4 vs v3`, điểm `D2` (Đầy đủ) tăng từ `3,375` lên **`3,750`** (`+0,375`) và xóa hoàn toàn `HF-6` trên `TEST-05` & `TEST-02`. |
| **Chống *False Clarity* (`FIX-03`)** | Mới có quy tắc chung *"không bịa JSON/SLA"* | Tách rạch ròi **Trường hợp A** (nguồn đủ dữ kiện, rối văn -> làm rõ không thêm ý) vs **Trường hợp B** (nguồn thiếu chủ thể/điều kiện/giao thức hoặc mâu thuẫn -> lộ diện lỗ hổng/câu hỏi mở) | Trong Held-Out v2 `C vs A` và `C vs B`, nhóm Neutral A và Simple Prompt B đều mắc `8/24 (33,3%)` HF (chủ yếu `HF-3` ở nhóm nguồn thiếu dữ kiện), trong khi C giảm xuống **`0/24`** (vs A) và **`1/24`** (vs B). |
| **Kiểm định chất lượng & Judge (`FIX-01`, `FIX-09`)** | Rubric v1 (chỉ 1 tập held-out 24 ca, chưa hiệu chuẩn Judge) | Hạ cấp 24 ca cũ thành Regression; tạo **Held-Out v2 (`n=24`)**, hiệu chuẩn **Judge v2 (`5/6`)** và tách rạch ròi `Major` vs `Critical HF` | Tái chấm v3 dưới Rubric v2 phơi bày `2/24 HF-6` ẩn trên v3 (`TEST-02`, `TEST-05`) và gỡ lỗi `HF-3` thổi phồng trên Baseline (`TEST-12`), giúp kết quả đáng tin cậy và không bảo vệ thành tích ảo. |

---

## 2. Giá trị của Ablation (`C0`) & So sánh với Simple Prompt (`B`) (`FIX-06`)

Thử nghiệm 4 nhóm (`A`, `B`, `C0`, `C`) trả lời thẳng hai câu hỏi thiết kế quan trọng nhất:
1. **Prompt ngắn 6 nguyên tắc (`Group B`, `609 bytes`) có thay thế được Skill không?**  
   - **Không trên tác vụ đặc tả / tài liệu / phân tích thiếu dữ kiện.** Dù B chỉ tốn ~`160 tokens` prompt và viết mượt ở hội thoại hài hước (`H2-14` thắng C `2–0`), B vẫn mắc **`8/24 (33,3%)` Hard Fail** (giống hệt Group A!) khi gặp nguồn mơ hồ hoặc tài liệu lai vì mô hình không tự biết quy trình phân tách *Đã biết / Chưa xác định / Câu hỏi mở*. C thắng B **`17–1`** (`6` bất nhất).
2. **`references/` (`17.804 bytes` tổng cộng) có thực sự mang lại giá trị vượt trên `SKILL.md` (`Group C0`) không?**  
   - **Có, ở độ đầy đủ và cấu trúc đặc tả, nhưng đi kèm đánh đổi độ trễ.** Chỉ riêng `SKILL.md` (`C0`) đã đủ giữ phần lớn bất biến chống bịa (`HF` giảm xuống `2/12`), giúp `C0` thắng `C` ở 3 ca (`H2-12, 19, 22`). Tuy nhiên trên toàn bộ 12 ca khó, việc nạp có chọn lọc `references/` giúp Full Skill `C` thắng **`7–3`**, đặc biệt nâng `D2` (`3,708` vs `3,417`) và `D4` (`3,458` vs `3,250`). Ngược lại, **tổng độ trễ trung bình tăng từ `29,06s` (`C0`) lên `39,11s` (`C`)** và tổng prompt tĩnh+tham chiếu tăng từ `8.694 bytes` lên trung bình `14.491 bytes`.

---

## 3. Bảng Trạng thái Nhận thức luận (Cập nhật sau Round 2)

| Nhận định / Giả thuyết | Trạng thái sau Round 2 | Bằng chứng & Phạm vi áp dụng |
|---|---|---|
| Cách tiếp cận Việt ngữ học (Đề–Thuyết, phân biệt `được`/`bị`, gỡ danh từ hóa rỗng, tránh mơ hồ phạm vi logic) phù hợp lý thuyết cho tiếng Việt | **Có cơ sở lý thuyết vững** | Cao Xuân Hạo (1991), Trần Ngọc Thêm (1985), Đỗ Hữu Châu, Nguyễn Đức Dân, Berry et al. (2003). |
| Skill v4 vượt trội rõ rệt cả Neutral Baseline (`20–3`) lẫn Simple Prompt (`17–1`) và giảm mạnh Hard Fail trên nhiều ngữ cảnh mới | **Đã kiểm chứng trong phạm vi 1 họ mô hình (`flash` / `pro`)** | `held-out-v2.jsonl` (`n=24`): `C vs A = 20/3/1 inc` (`0` vs `8` HF); `C vs B = 17/1/6 inc` (`1` vs `8` HF). |
| Không thể đánh đồng "viết gọn đầu ra hơn" với "tốn ít token / nhanh hơn" | **Đã kiểm chứng bằng số liệu đo** | `C` tốn TB `14.491 bytes` prompt đầu vào & `39,11s` độ trễ (vs `295 bytes` & `22,36s` ở A), nhưng đổi lấy giảm HF từ `33,3%` xuống `0–4%`. |
| Khả năng kích hoạt đúng lúc (`trigger`) đạt chuẩn cao | **Đã kiểm chứng ở mức mô phỏng (`16/16`, `F1 = 1,00`)** | Bộ `trigger-eval.jsonl` (`flash`); chưa thu telemetry trên Claude Code/Cursor/Codex thật. |
| Skill giảm thời gian hiểu đúng (**TtCU**) và giảm công sức trên người Việt thật | **Giả thuyết CHƯA kiểm chứng** | Chưa thực thi `evaluation/human-eval-protocol.md` trên người dùng thật. |
| Hiệu quả giữ ổn định trên các họ LLM khác (Claude, GPT/Codex, model tiếng Việt nội địa) | **Giả thuyết CHƯA kiểm chứng** | Chỉ mới chạy thực nghiệm trên tier `flash` & `pro` của Antigravity. |

---

## 4. Hạng mục Đã Xử lý ở `v4.1` & Tồn đọng cho Round 3

- **Đã xử lý ở `v4.1` (xem [v4.1-stabilization-report.md](../evaluation/v4.1-stabilization-report.md)):**
  1. Đồng bộ hóa trạng thái xác nhận giữa Bảng, Sơ đồ Mermaid, Trình tự và Open Questions (`H2-19` từ bất nhất HF xuống `0 HF`, thắng `2–0` trước `v4`).
  2. Quy tắc *Scope & Proportion* cho nguồn thiếu dữ kiện (`H2-12` đạt `0 HF`, `0 Major`, thắng `2–0` trước `v4`).
  3. Thay kho lệnh cụ thể trong Skill bằng quy tắc *Technical Claim Verification* tách dữ kiện kiểm chứng vs giả định (`H2-06` sửa sạch khẳng định sai `SHARE ROW EXCLUSIVE`, đạt `0 HF`, `0 Major`, thắng `2–0`).
  4. Audit sửa 4 ví dụ bảng trong `vietnamese-clarity-and-style.md` và tách Gate 0 standalone ([standalone-hf-protocol.md](../evaluation/standalone-hf-protocol.md)) trước khi so sánh cặp A/B.
- **Còn tồn đọng cho tương lai:**
  1. **Siết nhẹ ký hiệu bảng giao tiếp và nhánh timeout (`H2-22`, `H2-19`):** Kiểm tra quy ước chiều mũi tên trong bảng IDD khớp tiêu đề cột và nhắc xác minh trạng thái `capture` trước khi `rollback` điểm; không gán nhánh chưa chốt vào cột trách nhiệm xác nhận của bảng thành phần.
  2. **Trau chuốt độ mượt câu văn ở hội thoại ẩn dụ (`H2-16`):** Giữ nhất quán từ khóa (`mã định danh`) khi kể chuyện hài hước không dùng bullet.
  3. **Thực thi Human Evaluation (`evaluation/human-eval-protocol.md`) & Kiểm thử chéo đa họ mô hình.**
