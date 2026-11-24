# Báo cáo Kiểm thử & Ổn định Round 2 (`Skill v4`)

> [!NOTE]
> **Đính chính Đánh giá v4.1 (Evaluation Correction):**
> 1. **Phân loại Hard Fail 3 mức & Bất nhất giữa các cặp đấu:** Kết quả `0/24 HF` (`C vs A`), `1/24 HF` (`C vs B`: `H2-06`), và `2/12 HF` (`C vs C0`: `H2-12, H2-19`) của cùng tập đầu ra Group C cho thấy đánh giá cặp A/B bị ảnh hưởng bởi đối chứng ghép cặp. Kiểm định độc lập Gate 0 trước khi so sánh cặp ([standalone-hf-protocol.md](./standalone-hf-protocol.md), [v4.1-stabilization-report.md](./v4.1-stabilization-report.md)) xác định: `H2-06` là **Verified HF (`HF-2`)**, `H2-12` là **Judge-Disagreed / Unconfirmed** (`PASS_GATE_0` cả 2 lượt standalone), còn `H2-19` là **Judge-Disagreed (Boundary `Major` ở standalone nhưng xác thực có mâu thuẫn trạng thái giữa Bảng/Mermaid và Câu hỏi mở)**.
> 2. **Tách bảng theo tập mẫu trùng khớp (`n = 24` vs `n = 12`):** Không so sánh trực tiếp `2/12` của `C0` với `8/24` của `A/B` như cùng tập mẫu. Trên đúng **12 ca trùng khớp** của `C0`: Judge ghi nhận `A: 5/12`, `B: 6/12`, `C0: 2/12`, `C: 0/12` (khi ghép A/B) và `2/12` (khi ghép C0).
> 3. **Token Overhead:** Toàn bộ số token trong Mục 6.2 là **ước lượng heuristic** (`bytes / 3,8` hoặc `chars / 3,5`), không phải chỉ số billing token từ runtime.

**Nhánh thực nghiệm:** `round-2/v4-stabilization` (tách từ baseline v3 commit [`cd5bba945886222d0ebd236b3c1ba92a60dd3155`](https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/commit/cd5bba945886222d0ebd236b3c1ba92a60dd3155))  
**Nguyên tắc thực nghiệm:** Đóng băng [`SKILL.md` v4](../skills/vietnamese-human-readable-writing/SKILL.md) (SHA-256 `b418c737eef1f916bd1c3a9ce10abbd4448dd336118ddb0848f88dd9995764a5`) trước khi sinh bất kỳ đầu ra nào trên tập kiểm thử mới; bảo toàn nguyên vẹn toàn bộ dữ liệu và kết quả lịch sử v3 dưới [`evaluation/results/`](./results/); không xóa hoặc che giấu các ca thua, bất nhất vị trí hay Hard Fail.

---

## 1. Thiết kế Thực nghiệm & Chống Nhiễm dữ liệu (`FIX-01`, `FIX-06`, `FIX-09`)

Toàn bộ cấu hình chạy thực nghiệm và hàm băm SHA-256 của Skill v4, rubric, prompt và dataset được ghi cố định trong [run-manifest.json](./results-v2/run-manifest.json):

- **Hạ tầng sinh & chấm:** Toàn bộ câu trả lời (A, B, C0, C, Regression v4, Trigger Eval) được sinh trên tier `flash`; toàn bộ vòng chấm mù A/B được thực hiện bằng giám khảo độc lập [eval-blind-judge-v2](./judge-instructions-v2.md) trên tier `pro` với **2 lượt hoán đổi vị trí A/B bắt buộc** (Pass 1 xen kẽ chẵn/lẻ, Pass 2 đảo ngược vị trí 100%).
- **Hiệu chỉnh bộ dữ liệu chống leakage (`FIX-09`):**
  - 24 ca [held-out-test.jsonl](./held-out-test.jsonl) của Round 1 (đã được phân tích ở `TEST-02`, `TEST-05` để cải tiến Skill v4) được **hạ cấp thành Bộ Hồi quy (`Regression Suite v3`)**, không còn gọi là tập "chưa từng nhìn thấy".
  - Tạo mới 24 ca chưa từng thấy [held-out-v2.jsonl](./held-out-v2.jsonl) gồm 5 nhóm mục tiêu: `technical_depth` (6 ca), `ambiguity_no_fabrication` (7 ca), `natural_conversation` (3 ca), `hybrid_docs` (4 ca), và `real_world_long_docs` (4 ca dài đa phần).
  - **Cảnh báo trung thực (Section 14):** 4 ca `real_world_long_docs` (`H2-21..24`, gắn cờ `"simulated_real_world": true`) là **tài liệu nghiệp vụ/kỹ thuật đa phần được mô phỏng sát thực tế** (BRD Bundle Add-on, IDD ví + điểm POS, OpenAPI Partial Payment/Refund, Incident Runbook), **không phải tài liệu nội bộ thật lấy từ doanh nghiệp đang vận hành**.
  - Kiểm tra chống trùng lặp chéo trên 70 ca (`development` 16 + `regression_v3` 24 + `held_out_v2` 24 + `judge_calibration` 6) qua [validate_datasets.py](./scripts/validate_datasets.py): **`max_jaccard_similarity = 0.27`** (`flagged_pairs = []`, dưới ngưỡng `0.35`).
- **Hiệu chuẩn Giám khảo v2 trước khi chấm ([judge-calibration-results.jsonl](./results-v2/judge-calibration-results.jsonl)):**
  - Chấm thử 6 ca gài lỗi biết trước (`CAL-01..06`), đạt **`6/6` chọn đúng output chuẩn ở cả 2 lượt hoán đổi** và **`5/6` khớp chính xác nhãn Hard Fail kỳ vọng**:
    - `CAL-01` (DLX phá vỡ thứ tự): Pass (`HF-1, HF-5, HF-6`).
    - `CAL-02` (False Clarity tự bịa `PAY`/`OMS`/webhook): Pass (`HF-3, HF-5`).
    - `CAL-03` (Đảo biên tài chính `<` / `>=` & `VÀ` / `HOẶC`): Pass (`HF-4`).
    - `CAL-04` (Anti-overtrigger câu mục đích vô hại): Pass (`hard_fails = []`).
    - `CAL-06` (Hội thoại tự nhiên không ép khuôn): Pass (`hard_fails = []`).
    - `CAL-05` (Ranh giới thiếu 1 khía cạnh phụ vs HF-5): Judge thắng đúng bên chuẩn nhưng vẫn bật `HF-5` cho bản gài lỗi vì prompt kiểm thử có ghi `fsync` và `file lớn` trong `must_preserve` (chặt hơn kỳ vọng giả định `[]`). Kết quả `5/6` đạt ngưỡng `>= 5/6` để mở khóa vòng chấm chính thức.

---

## 2. Kiểm toán Lịch sử v3: Đính chính Rubric v1 & Tái chấm dưới Rubric v2 (`FIX-01`, `FIX-08`)

### 2.1. Đính chính số liệu báo cáo v3 (`FIX-08`)
Kiểm toán trực tiếp 48 lượt chấm trong [held-out-raw-results.jsonl](./results/held-out-raw-results.jsonl) cho thấy 3 điểm cần đính chính ở [evaluation-report.md](./evaluation-report.md) (đã thêm khối *Errata* ở đầu file gốc mà không sửa phần lịch sử bên dưới):
1. Tổng thắng raw trên 48 lượt là **`A = 23`, `B = 25`** (chênh lệch nhẹ trong vùng dao động ngẫu nhiên), và trong 3 ca bất nhất vị trí: `TEST-02` chọn `(B, B)`, **`TEST-21` chọn `(A, A)`**, `TEST-24` chọn `(B, B)` — không phải cả 3 ca đều chọn B như bản v3 từng nêu.
2. **Trung bình 24 tỷ số độ dài từng cặp** (`exp_words / base_words`) là **`0,7799` (`0,780`)**, khác với **tỷ số của hai trung bình** (`13.757 / 19.063 = 0,7217` hay `0,722`).
3. Không giữ các diễn đạt tuyệt đối hóa như *"xóa sạch mọi lỗi bịa chi tiết"*.

### 2.2. Kết quả Tái chấm 24 cặp lịch sử v3 dưới Rubric v2 ([v3-reaudit-rubric-v2.jsonl](./results-v2/v3-reaudit-rubric-v2.jsonl))

Áp dụng [rubric-v2.md](./rubric-v2.md) và [judge-instructions-v2.md](./judge-instructions-v2.md) lên nguyên văn `baseline_output` và `experiment_output` (v3) cho thấy:

| Chỉ số (cùng 24 cặp lịch sử `v3` vs `Baseline`) | Rubric v1 (Lịch sử cũ) | Rubric v2 (Tái chấm Round 2) | Thay đổi & Ý nghĩa |
|---|---:|---:|---|
| **v3 thắng đồng thuận 2 lượt** | 20 / 24 | **18 / 24 (75,00%)** | `TEST-06`, `TEST-22` chuyển sang `position_inconsistent` |
| **Baseline thắng đồng thuận 2 lượt** | 1 / 24 (`TEST-05`) | **2 / 24 (8,33%)** (`TEST-02`, `TEST-05`) | `TEST-02` từ `position_inconsistent` thành `baseline` thắng |
| **Bất nhất vị trí (Position Inconsistent)** | 3 / 24 | **4 / 24 (16,67%)** | `TEST-06`, `TEST-21`, `TEST-22`, `TEST-24` |
| **Tổng 48 lượt (mapped)** | v3 `43` / Base `5` / Tie `0` | **v3 `38` / Base `8` / Tie `2`** | Nhất quán vị trí: `20/24 (83,33%)` |
| **Baseline dính Hard Fail (HF union)** | 11 / 24 | **8 / 24 (33,33%)** | Hết bịa HF-3 cho sáo ngữ vô hại (`TEST-12`, v.v.) |
| **Skill v3 dính Hard Fail (HF union)** | 0 / 24 | **2 / 24 (8,33%)** (`TEST-02`, `TEST-05`) | **Cả 2 ca P0 đều bị bắt đúng `HF-6`** |
| **Nhóm sạch không HF (`n = 15` dưới v2)** | 10 / 13 thắng v3 | **11 / 15 thắng v3**, `4` bất nhất, `0` thua | Chênh lệch điểm chất lượng `D1..D9` vẫn nghiêng mạnh về v3 |

- **Điểm trung bình `D1..D9` của v3 vs Baseline dưới Rubric v2:**  
  `v3`: `D1=3,396 | D2=3,542 | D3=3,438 | D4=3,604 | D5=3,708 | D6=3,792 | D7=3,771 | D8=3,875 | D9=3,438`  
  `Baseline`: `D1=2,542 | D2=3,354 | D3=2,979 | D4=2,562 | D5=3,104 | D6=3,000 | D7=3,208 | D8=3,083 | D9=2,625`
- **Xác nhận `FIX-01`:** Khi bỏ thiên lệch quá nhạy với sáo ngữ vô hại của Baseline (`TEST-12`: từ `HF-3` xuống `0 HF`, v3 vẫn thắng cả 2 lượt) và áp dụng nghiêm `HF-6` cho lỗi kỹ thuật phá vỡ cam kết/nguy cơ xóa file, tỷ lệ HF của Skill v3 thực tế là **`2/24` (`TEST-02` và `TEST-05`)**, không phải `0/24`.

---

## 3. Bộ Hồi quy (`Regression v4 vs v3`, 24 ca `held-out-test.jsonl`)

So sánh đối đầu trực tiếp giữa **Skill v4** ([regression-v4-raw.jsonl](./results-v2/regression-v4-raw.jsonl)) và **Skill v3 lịch sử** dưới cùng `eval-blind-judge-v2` (`pro`):

| Chỉ số (`n = 24`) | Skill v3 | Skill v4 | Nhận xét |
|---|---:|---:|---|
| **Thắng đồng thuận 2 lượt** | **8 / 24 (33,33%)** | **9 / 24 (37,50%)** | `7 / 24` bất nhất vị trí (`position_consistency = 70,83%`) |
| **Tổng 48 lượt (mapped)** | 22 lượt thắng (`+2 TIE`) | **24 lượt thắng** (`+2 TIE`) | Hai bản đều đạt chất lượng cao ở nhóm ca ngắn nên cận hòa nhiều |
| **Số ca dính Hard Fail (HF union)** | **3 / 24 (12,50%)** | **0 / 24 (0,00%)** | `v3` mắc `HF-6` (`TEST-02`, `TEST-05`) và `HF-2` (`TEST-17`); `v4` xóa sạch cả 3 |
| **Lỗi `Critical` / `Major` / `Minor` (48 lượt)** | `6 / 22 / 135` | **`0 / 21 / 134`** | Giảm `Critical` từ 6 lượt xuống **0** |
| **Nhóm sạch không HF (`n = 21`)** | **8 / 21** | **6 / 21** (+`7` bất nhất) | `v3` nhỉnh hơn ở độ súc tích `D6`/`D7` trên một số ca nghiệp vụ ngắn |
| **Độ dài trung bình (`words`)** | `573,21` (`sum=13.757`) | `767,88` (`sum=18.429`) | `v4` dài hơn ~34% vì hết nén mỏng chiều sâu đa trục |

**Điểm trung bình `D1..D9` (`v3` vs `v4` trên Regression):**
- `v4` **vượt rõ rệt ở trục cốt lõi:** `D1` (**3,312** vs 3,104), `D2` (**3,750** vs 3,375, `+0,375`), `D4` (**3,417** vs 3,250), `D5` (**3,729** vs 3,458), `D9` (**3,562** vs 3,125, `+0,437`).
- `v3` **nhỉnh nhẹ ở mật độ & tự nhiên bề mặt:** `D3` (3,333 vs 3,188), `D6` (3,583 vs 3,396), `D7` (3,604 vs 3,479), `D8` (3,750 vs 3,667).

**Chi tiết các ca v4 thắng lại HF của v3 vs các ca v4 thua (`8/24`):**
- **v4 khắc phục triệt để 3 ca HF của v3:** `TEST-02` (`v4` tách rõ `git reset HEAD` cho Git < 2.23 và cảnh báo không dùng `git rm --cached` khi file đã commit), `TEST-05` (`v4` không khuyên đẩy `M1` sang DLX khi giữ thứ tự nghiêm ngặt và giải thích sâu cả lưu trữ lẫn Quorum/Classic Queue), `TEST-17` (`v4` giữ đúng cú pháp Redis `ZREMRANGEBYSCORE ... -inf (now - 60000` thay vì `(<now - 60000)` bị `HF-2` ở `v3`).
- **8 ca v3 thắng v4 (`TEST-03, 08, 10, 12, 14, 15, 19, 23`):** Không ca nào của v4 bị HF (`v4_HF = []`), nhưng khi đầu vào thuộc dạng rõ ý sẵn hoặc cần cô đọng (như phân biệt 2 thông báo lỗi ở `TEST-03`, tin nhắn Slack/Teams ở `TEST-10`, biên bản nửa trang `TEST-12`, viết lại 1 đoạn HPA `TEST-23`), v4 có xu hướng triển khai thêm bảng biểu/phân rã quy tắc phụ hoặc mở ngoặc giải thích làm giảm độ cô đọng (`D6`) và tính tự nhiên ngắn gọn (`D7`) so với v3.

---

## 4. Kết quả Thực nghiệm Chính 4 Nhóm trên `held-out-v2.jsonl` (`FIX-06`, `FIX-09`)

Thử nghiệm trên **24 ca mới hoàn toàn** chia thành 4 nhóm đối chứng:
- **Group A (`Neutral Baseline`):** Trợ lý tiếng Việt trung tính (`295 bytes` prompt).
- **Group B (`Simple Prompt`):** Prompt 6 quy tắc súc tích (`609 bytes` prompt — đối chứng chi phí/hiệu quả tối giản).
- **Group C0 (`Ablation SKILL.md-only`):** Chỉ nạp thân `SKILL.md` v4 (`8.694 bytes`), **cấm đọc `references/`**, chạy trên 12 ca đại diện phức tạp (`H2-01, 02, 07, 09, 12, 17, 18, 19, 21, 22, 23, 24`).
- **Group C (`Full Skill v4`):** Nạp `SKILL.md` v4 + Progressive Disclosure linh hoạt `0–2` file từ `references/`.

### 4.1. Bảng Tổng hợp So sánh Cặp (`Blind Judge v2`, 2 lượt hoán đổi)

| Cặp đấu | Số ca (`n`) | C thắng (v4 Full) | Đối thủ thắng | Bất nhất vị trí (`TIE=0`) | 48 / 24 lượt (mapped) | HF của C | HF của Đối thủ | Nhóm sạch không HF |
|---|---:|---:|---:|---:|---|---:|---:|---|
| **`C vs A` (`Full v4` vs `Neutral`)** | 24 | **20 (83,33%)** | 3 (`A`) | 1 (`cons = 95,83%`) | `C: 41 / A: 7` | **0 / 24 (0,0%)** | **8 / 24 (33,3%)** | `n=16`: **C thắng 12**, A 3, inc 1 |
| **`C vs B` (`Full v4` vs `Simple Prompt`)** | 24 | **17 (70,83%)** | 1 (`B`) | 6 (`cons = 75,00%`) | `C: 38 / B: 7 / TIE: 3` | **1 / 24 (4,2%)** | **8 / 24 (33,3%)** | `n=15`: **C thắng 9**, B 1, inc 5 |
| **`C vs C0` (`Full v4` vs `SKILL-only`)** | 12 | **7 (58,33%)** | 3 (`C0`) | 2 (`cons = 83,33%`) | `C: 16 / C0: 7 / TIE: 1` | **2 / 12 (16,7%)** | **2 / 12 (16,7%)** | `n=9`: **C thắng 6**, C0 1, inc 2 |

> [!IMPORTANT]
> **Giải đáp `FIX-06` ("Simple Prompt 6 dòng có đủ thay Skill không?"):**
> Câu trả lời là **KHÔNG đủ trên tác vụ đòi hỏi tính chính xác nghiêm ngặt.** Dù **Group B (Simple Prompt)** cải thiện nhẹ độ chỉn chu bề mặt so với Group A ở vài ca `casual`/`natural_conversation` (thắng C ở `H2-14`), **Group B vẫn mắc `8 / 24 (33,3%)` Hard Fail** — bằng hệt tỷ lệ HF của Neutral Baseline A (`6 HF-3`, `1 HF-5`, `1 HF-2`, và `3 HF-1` ở tổng lỗi). Nói cách khác, nhắc chung chung *"không tự bịa thông tin chưa có căn cứ"* không ngăn được model rơi vào bẫy *False Clarity* khi xử lý nguồn thiếu dữ kiện (`H2-07, 09, 10, 13`) hoặc tài liệu lai (`H2-17, 18, 19`).  
> Ngược lại, **Ablation (`C vs C0`)** chứng minh thân `SKILL.md` v4 (C0) tự nó đã giảm mạnh Hard Fail so với A/B (`2/12` vs `8/24` trên đúng 12 ca khó), còn `references/` giúp Full Skill C tăng chất lượng cấu trúc, độ đầy đủ `D2` (`3,708` vs `3,417`) và rõ nghĩa `D4` (`3,458` vs `3,250`) để thắng **7–3** chung cuộc và **6–1** trong nhóm sạch không HF.

### 4.2. Điểm Trung bình `D1..D9` (thang 0–4, `D9` chỉ tính trên `actionability_applicable = true`)

| Tiêu chí | `C vs A`: **A** | `C vs A`: **C** | `C vs B`: **B** | `C vs B`: **C** | `C vs C0`: **C0** | `C vs C0`: **C** |
|---|---:|---:|---:|---:|---:|---:|
| **D1. Trung thực dữ kiện & logic** | 2,458 | **3,625** (`+1,167`) | 2,625 | **3,708** (`+1,083`) | 3,208 | **3,292** (`+0,084`) |
| **D2. Đầy đủ & chiều sâu đúng trọng tâm** | 3,125 | **3,708** (`+0,583`) | 3,292 | **3,688** (`+0,396`) | 3,417 | **3,708** (`+0,291`) |
| **D3. Thuật ngữ & nhất quán ký hiệu** | 3,083 | **3,417** (`+0,334`) | 3,208 | **3,458** (`+0,250`) | 3,292 | **3,375** (`+0,083`) |
| **D4. Rõ nghĩa ngay lần đọc đầu** | 2,583 | **3,812** (`+1,229`) | 2,688 | **3,812** (`+1,124`) | 3,250 | **3,458** (`+0,208`) |
| **D5. Tổ chức thông tin (BLUF/trình tự)** | 3,083 | **3,729** (`+0,646`) | 3,125 | **3,729** (`+0,604`) | 3,417 | **3,542** (`+0,125`) |
| **D6. Mật độ thông tin & không dư thừa** | 3,375 | **3,667** (`+0,292`) | 3,354 | **3,708** (`+0,354`) | 3,583 | **3,667** (`+0,084`) |
| **D7. Văn phong tiếng Việt tự nhiên** | 3,417 | **3,750** (`+0,333`) | 3,625 | **3,812** (`+0,187`) | 3,750 | 3,750 (`0,000`) |
| **D8. Phù hợp ngữ cảnh & đối tượng** | 3,354 | **3,875** (`+0,521`) | 3,604 | **3,896** (`+0,292`) | 3,792 | **3,875** (`+0,083`) |
| **D9. Tính sử dụng được / hành động hóa** | 2,529 | **3,765** (`+1,236`) | 2,618 | **3,735** (`+1,117`) | 3,389 | 3,389 (`0,000`) |

### 4.3. Phân tích theo 5 Ngữ cảnh & Nhóm Tài liệu Dài Mô phỏng (`Section 14`)

| Ngữ cảnh (`held-out-v2.jsonl`) | Số ca | `C vs A` | `C vs B` | `C vs C0` (`n=12`) |
|---|---:|---|---|---|
| `technical_depth` (`H2-01..06`) | 6 | **C: 5**, A: 1 (`H2-06`) | **C: 4**, inc: 2 (`H2-03, 06`) | **C: 2 / 2** (`H2-01, 02`) |
| `ambiguity_no_fabrication` (`H2-07..13`) | 7 | **C: 5**, A: 2 (`H2-08, 12`) | **C: 5**, inc: 2 (`H2-08, 12`) | **C: 2**, C0: 1 (`H2-12`) |
| `natural_conversation` (`H2-14..16`) | 3 | **C: 2**, inc: 1 (`H2-14`) | **B: 1** (`H2-14`), C: 1, inc: 1 | *(chưa chạy C0)* |
| `hybrid_docs` (`H2-17..20`) | 4 | **C: 4 / 4** (`100%`) | **C: 4 / 4** (`100%`) | **C: 2**, C0: 1 (`H2-19`) |
| `real_world_long_docs` (`H2-21..24`, **mô phỏng**) | 4 | **C: 4 / 4** (`100%`) | **C: 3**, inc: 1 (`H2-23`) | **C: 1**, C0: 1 (`H2-22`), inc: 2 |

- Tách cờ `simulated_real_world`: Trên 20 ca chuẩn (`simulated_real_world = false`), C đạt **`16/20` thắng vs A** và **`14/20` thắng vs B**; trên 4 ca dài mô phỏng (`simulated_real_world = true`), C đạt **`4/4` vs A**, **`3/4` vs B** (`1` bất nhất), **`1/4` vs C0** (`1` C0 thắng ở `H2-22`, `2` bất nhất — cho thấy ngay cả khi chỉ dùng `SKILL.md` v4, mô hình cũng xử lý tốt cấu trúc đặc tả dài nếu không cần tham khảo quá sâu bảng tra phụ).

---

## 5. Phân tích Trung thực Mọi Ca Thua, Bất nhất và Hard Fail của Skill v4

Theo nguyên tắc đóng băng trước khi chấm, toàn bộ các ca lỗi/thua của Skill v4 được giữ nguyên trạng để báo cáo trung thực:

1. **`H2-06` (`technical_depth` — PostgreSQL 15 Zero-Downtime Migration):**
   - **Kết quả:** Thua `A` (0–2 trong `C vs A`), bất nhất trong `C vs B` (C thắng Pass 1, **dính `HF-2` ở Pass 2**).
   - **Nguyên nhân gốc rễ:** Trong Mục 5 của Group C, output viết nhầm rằng lệnh `ALTER TABLE ... ADD CONSTRAINT CHECK (...) NOT VALID` giữ lock `SHARE ROW EXCLUSIVE` ngắn; thực tế trên PostgreSQL 15, lệnh này vẫn xin `ACCESS EXCLUSIVE` ngắn (chặn cả `SELECT`), trong khi `SHARE ROW EXCLUSIVE` là chế độ khóa của `ADD FOREIGN KEY`. Đây là lỗi kiến thức hệ quản trị cơ sở dữ liệu thật cần lưu ý (Skill giúp cấu trúc RFC tốt nhưng không tự sửa được lỗi nhớ nhầm lock mode của mô hình sinh `flash`).
2. **`H2-19` (`hybrid_docs` — Payout SAD + Business Rule > 50 triệu):**
   - **Kết quả:** C thắng A (`2–0`) và B (`2–0`) vì A và B đều bịa hàng loạt trường API/giao thức (`HF-3`); **nhưng trong `C vs C0`, C0 thắng `2–0` và bắt trúng `HF-1` + `HF-3` của C ở cả 2 lượt** (riêng C0 sạch Gate 0 ở Pass 1 và bị gắn `HF-1, HF-3` ở Pass 2).
   - **Nguyên nhân gốc rễ:** Output của C tự mâu thuẫn nội tại giữa các phần: ở bảng Mục 2 và sơ đồ Mermaid Mục 4.1, C gán luôn nhánh `> 50.000.000đ` sau duyệt cho `Payout Worker`; nhưng tới Mục 4.2 bước 5 và Mục 6.1, chính C lại liệt kê việc đẩy qua `Payout Worker` hay gọi đồng bộ là **"chưa chốt"**. Bài học rõ rệt cho v4.1/Round 3: **cần bước kiểm tra nhất quán chéo giữa Bảng, Sơ đồ Mermaid và danh sách Điểm chưa chốt** trong `hybrid_docs`.
3. **`H2-12` (`ambiguity_no_fabrication` — Voucher Freeship tối đa 30.000đ / Điện máy):**
   - **Kết quả:** Thua A (`0–2`), bất nhất trong `C vs B`, thua C0 (`0–2`, dính **`HF-3` ở Pass 2 `C vs C0`**).
   - **Nguyên nhân gốc rễ:** Khi đề bài nguồn có 2 cụm mơ hồ lồng nhau (*"tối đa 30.000đ"* vs *"không áp dụng kèm mã khác hoặc sản phẩm Điện máy"*), trong phần "Phương án viết lại 1", output C viết *"giảm 30.000đ nếu phí vận chuyển > 30.000đ"* mà chưa đưa câu hỏi chốt cách xử lý khi phí > 30.000đ vào mục câu hỏi xác nhận với Kinh doanh, dẫn đến một lượt Judge kết luận *False Clarity* (`HF-3`), đồng thời mâu thuẫn nhẹ giữa *"bất kỳ mã nào"* và *"theo danh sách"*.
4. **`H2-08` (`ambiguity_no_fabrication`):** C thua A (`0–2`), bất nhất trong `C vs B` (`0 HF` ở cả hai bên) vì Group A trình bày trực diện và hỏi cụ thể hơn về quy trình xử lý hàng hóa/vận đơn đã xuất kho khi đơn hủy tự động.
5. **`H2-14` (`natural_conversation` — Hài hước đồng cảm quên `Ctrl+S`):** C bất nhất với A và **thua B (`0–2`)** (đều `0 HF`) vì cụm *"tập bài khởi động não bộ miễn phí còn gì!"* của C mang sắc thái hơi "sách vở" so với câu đùa tự nhiên sát tâm lý dev của Simple Prompt B (*"thốn tới tận linh hồn luôn... cái file nó thích chơi trốn tìm trên RAM một chút thôi"*).
6. **`H2-22` (`real_world_long_docs` mô phỏng):** C thắng A (`2–0`), thắng B (`2–0`), nhưng thua C0 (`0–2`) ở nhóm sạch không HF do C0 đặt tên/sơ đồ tuần tự đồng nhất nhẹ hơn giữa `hold_id` và bước hoàn tất giao dịch POS.

*(Lưu ý về phương pháp luận: Việc cùng một bản sinh Group C của `H2-12` và `H2-19` không bị gắn HF trong cặp `C vs A` nhưng bị gắn HF ở 1–2 lượt trong cặp `C vs C0` phản ánh dao động biên của LLM Judge `pro` khi đánh giá lỗi ranh giới giữa tài liệu dài. Dù vậy, rà soát nguyên văn cho thấy các lỗi mà Judge chỉ ra tại `H2-06`, `H2-12` và `H2-19` đều là khiếm khuyết có thật trong văn bản C.)*

---

## 6. Kiểm thử Kích hoạt (`Trigger Eval`), Chi phí Runtime (`Overhead`) & Tương thích (`FIX-10`)

### 6.1. Độ chính xác Kích hoạt (`trigger-eval.jsonl`, `n = 16`)
Đánh giá mô phỏng khả năng phân tuyến kỹ năng (*skill routing*) trên 16 truy vấn bằng `eval-trigger-tester` (`flash`):
- **True Positive (nên kích hoạt & kích hoạt đúng):** `10 / 10` (`TRG-01..10`: giải thích kỹ thuật, biên tập dịch máy, User Story/AC, API Spec, Slack, phân tích lỗi, kiểm tra mơ hồ, Runbook, chọn DB, tài liệu lai).
- **True Negative (không kích hoạt & bỏ qua đúng):** `6 / 6` (`TRG-11..16`: viết code Python/Tailwind thuần, sửa bug off-by-one + chạy pytest, viết cover letter tiếng Anh, giải phương trình tiếng Anh, chạy `git status`).
- **Kết quả:** **`Precision = 1,00` | `Recall = 1,00` | `F1 = 1,00` | `Accuracy = 16 / 16 (100%)`**.  
  *Lưu ý:* Đây là phép thử mô phỏng định tuyến dựa trên `name` + `description` trên tier `flash`, chưa phải log kích hoạt trực tiếp từ nhiều IDE/harness bên ngoài.

### 6.2. Kích thước Tệp, Overhead Đầu vào, Mức độ Đọc Reference & Độ trễ (`summary-stats-v2.json`)

| Thành phần / Nhóm thực nghiệm | Kích thước tĩnh (`bytes`) | Chữ / Từ / Dòng | Ước lượng token hệ thống (`bytes / 3,8`) | Đầu ra TB (`words`) | Đầu ra TB (`bytes` / `~tokens`) | Độ trễ TB (`s`) / Trung vị (`s`) |
|---|---:|---:|---:|---:|---:|---:|
| `SKILL.md` (đầy đủ / thân bỏ frontmatter) | `9.132` / `8.694` | `7.235` chars / `1.367` words / `78` lines | `2.403` / **`2.288`** *(từ chars: `2.067`)* | — | — | — |
| `references/business-specs.md` | `3.484` | `552` words / `32` lines | `917` | — | — | — |
| `references/information-architecture.md` | `3.995` | `631` words / `35` lines | `1.051` | — | — | — |
| `references/technical-specs.md` | `4.689` | `735` words / `33` lines | `1.234` | — | — | — |
| `references/vietnamese-clarity-and-style.md` | `5.636` | `921` words / `48` lines | `1.483` | — | — | — |
| **Tổng cộng cả Skill + 4 references** | **`26.936`** | `4.206` words | `~7.088` *(tối đa nạp thực tế mỗi ca ≤ ~5.005t)* | — | — | — |
| **Group A (`Neutral`, `n=24`)** | `295` | — | `~78` | `1.083,5` | `6.929` (`~1.824`) | `22,36s` / `23,46s` |
| **Group B (`Simple Prompt`, `n=24`)** | `609` | — | `~160` | `1.113,3` | `7.128` (`~1.876`) | `23,80s` / `22,68s` |
| **Group C0 (`SKILL-only`, `n=12`)** | `8.694` | — | `~2.288` | `1.356,2` | `8.476` (`~2.231`) | `29,06s` / `30,50s` |
| **Group C (`Full Skill v4`, `n=24`)** | `8.694 → 19.019` (`TB 14.491`) | — | **`~3.814`** (`2.288 → 5.005`) | **`1.203,8`** | `7.659` (`~2.016`) | **`39,11s` / `40,60s`** |

- **Phân bố đọc `references/` (Cơ chế Progressive Disclosure linh hoạt `0 / 1 / 2` file):**
  - Trên **Held-Out v2 (`n=24`, Group C)**: **`0` file: `2/24`** (`H2-14, H2-16` hội thoại đời thường) | **`1` file: `13/24`** | **`2` file: `9/24`** (các ca lai `hybrid_docs` & ca đa tầng). Tần suất đọc: `technical-specs.md` (`9`), `vietnamese-clarity-and-style.md` (`8`), `business-specs.md` (`8`), `information-architecture.md` (`6`).
  - Trên **Regression v4 (`n=24`)**: **`0` file: `7/24`** (`TEST-01, 02, 03, 06, 10, 11, 12`) | **`1` file: `16/24`** | **`2` file: `1/24`** (`TEST-19` Post-Incident).
- **Cảnh báo trung thực về chi phí token:** Việc rút gọn chữ đầu ra trên một số ca ngắn **KHÔNG** đồng nghĩa giảm tổng chi phí token hay chi phí thời gian chạy! Trái lại, trên 24 ca Held-Out v2, Group C có prompt đầu vào trung bình cao gấp ~49 lần Group A (`14.491 bytes` vs `295 bytes`), đầu ra dài hơn nhẹ (`1.203,8` vs `1.083,5` từ vì bảo toàn chiều sâu đa trục và tách mục làm rõ `Trường hợp B`), và độ trễ trung bình tăng **+74,9%** (`39,11s` vs `22,36s`). Giá trị của Skill v4 không phải "rẻ token hơn", mà là **giảm Hard Fail từ 33,3% xuống `0–4%` và tăng độ trung thực/rõ nghĩa +1,1 đến +1,2 điểm trên thang 4 điểm**.

### 6.3. Ma trận Tương thích Runtime 4 Tầng (`FIX-10`)

| Tầng kiểm chứng | Trạng thái cho Skill v4 | Bằng chứng / Giới hạn |
|---|---|---|
| **1. Tuân thủ đặc tả định dạng (`agentskills.io`)** | **Đạt (Verified)** | Tên thư mục khớp `name`, frontmatter YAML hợp lệ, `SKILL.md` 78 dòng (`< 500`), 4 liên kết tương đối hợp lệ, không còn hardcode tên tool `read_file` trong [validate_datasets.py](./scripts/validate_datasets.py). |
| **2. Khả năng cài đặt & đường dẫn nạp trên các harness** | **Cơ sở đặc tả đạt (Chưa cài thử thực tế trên Claude Code / Cursor / Codex)** | Tách thành gói cài độc lập `skills/vietnamese-human-readable-writing/`; có hướng dẫn fallback cho host không có tool đọc file tham chiếu. |
| **3. Độ chính xác kích hoạt từ `description`** | **Đạt trên bộ thử mô phỏng (`16/16`, `F1 = 1,00`)** | Kiểm thử qua [trigger-eval.jsonl](./trigger-eval.jsonl) trên tier `flash`; chưa đo trên telemetry thật của nhiều IDE khác nhau. |
| **4. Hiệu quả chất lượng đầu ra đa họ mô hình** | **Chỉ mới kiểm chứng trong 1 họ mô hình Antigravity (`flash` / `pro`)** | Chưa chạy đối chứng đa họ mô hình (Claude, GPT/Codex, model mở nội địa) nên **chưa khẳng định độ ổn định hiệu năng chéo model**. |

---

## 7. Những gì CHƯA được Chứng minh (`What Is NOT Proven Yet`)

1. **Chưa đo trên người đọc Việt Nam thật (`TtCU` & Comprehension Gate):** Quy trình [human-eval-protocol.md](./human-eval-protocol.md) chưa được thực thi. Chưa có bằng chứng trực tiếp rằng con người đọc bản đầu ra v4 mất ít thời gian hơn hoặc hỏi lại ít hơn ngoài thực tế; toàn bộ điểm chất lượng hiện nay vẫn dựa vào **LLM Blind Judge (`pro`)**.
2. **Chưa kiểm thử trên nhiều họ mô hình (Cross-Model):** Toàn bộ Round 1 và Round 2 chạy trên tier `flash` (sinh) và `pro` (giám khảo) trong môi trường Antigravity, chưa kiểm chứng Self-Enhancement Bias giữa các họ LLM khác nhau.
3. **4 ca tài liệu dài (`H2-21..24`) mới là mô phỏng sát thực tế (`simulated_real_world = true`):** Cần thử nghiệm thêm trên tài liệu sản phẩm/kỹ thuật thật có lịch sử sửa đổi phức tạp trong doanh nghiệp trước khi kết luận tổng quát.
