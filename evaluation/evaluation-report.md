# Báo cáo Kết quả Kiểm thử và Đánh giá v3 (Bản Lịch sử & Đính chính Round 2)

> [!WARNING]
> **Đính chính (Errata — Round 2 Audit, 25/11/2026):**
> Kiểm tra độc lập dữ liệu thô [held-out-raw-results.jsonl](./results/held-out-raw-results.jsonl) đã phát hiện các điểm cần đính chính trong bản báo cáo v3 dưới đây (toàn văn gốc vẫn được giữ nguyên bên dưới để bảo toàn lịch sử thực nghiệm):
> 1. **Số liệu vị trí A/B ở 3 ca bất nhất (Mục 5.2):** Báo cáo gốc viết nhầm rằng cả 3 ca `TEST-02, TEST-21, TEST-24` đều chọn `Output B`. Thực tế dữ liệu thô 48 lượt chấm là **`A = 23`, `B = 25`**, cụ thể: `TEST-02` (`Pass 1 = B`, `Pass 2 = B`), **`TEST-21` (`Pass 1 = A`, `Pass 2 = A`)**, `TEST-24` (`Pass 1 = B`, `Pass 2 = B`). Không có đủ bằng chứng kết luận Judge thiên lệch hệ thống về vị trí B; sự khác biệt giữa 2 lượt trên 3 ca này phản ánh **bất nhất vị trí (position inconsistency)** / **dao động chấm điểm ở các ca sát nút (near-tie / judge variance)**.
> 2. **Phân biệt hai phép tính tỷ số độ dài (Mục 2.1):** Giá trị `0,78` (`0,7799`) là **trung bình của 24 tỷ số từng cặp** ($\frac{1}{n}\sum \text{exp\_words}_i / \text{base\_words}_i$), khác với **tỷ số giữa hai độ dài trung bình** ($573,208 / 794,292 = 0,7217$).
> 3. **Diễn đạt về Hard Fail và tính bảo toàn:** Kết quả `0/24 Hard Fail` của Skill v3 phụ thuộc vào định nghĩa Rubric v1 tại thời điểm chấm. Khi hiệu chỉnh sang Rubric v2 để xử lý các lỗi kỹ thuật nghiêm trọng bị sót như `TEST-05` (`DLX` phá thứ tự) hay `TEST-02` (`git rm --cached`) và tránh quá nhạy với sáo ngữ vô hại, kết quả đối chứng lại được công bố tách riêng tại [evaluation-report-v2.md](./evaluation-report-v2.md). Không khẳng định Skill "bảo toàn 100% dữ kiện" hay "xóa sạch mọi lỗi".
> 4. **Trạng thái bộ `held-out-test.jsonl` sau v3:** Vì 24 ca này đã được dùng để phân tích lỗi cho vòng sửa sang v4, chúng không còn là *unseen held-out* đối với phiên bản v4 mà được chuyển thành **Regression Suite (`regression-v3`)**. Kết quả đánh giá độc lập mới của v4 nằm tại [evaluation-report-v2.md](./evaluation-report-v2.md).

Báo cáo này trình bày kết quả thực nghiệm có đối chứng giữa **Baseline** (AI không dùng Skill) và **Experiment** (AI dùng Skill `vietnamese-human-readable-writing` phiên bản đóng băng v3), cùng đầy đủ các giới hạn chưa được kiểm chứng. Toàn bộ số liệu định lượng được trích xuất trực tiếp từ [summary-stats.json](./results/summary-stats.json).

---

## 1. Thiết lập Kiểm soát Thực nghiệm

| Thành phần | Thiết lập Baseline | Thiết lập Experiment |
|---|---|---|
| **Mô hình sinh đầu ra** | Subagent `eval-baseline` (model `flash`) | Subagent `eval-experiment-v3` (model `flash`) |
| **System Prompt** | Trợ lý AI tiếng Việt trung tính, trả lời trực tiếp | Cùng nền trung tính + `SKILL.md` v3 + quyền `read_file` tới `references/*.md` |
| **Tập dữ liệu tách biệt** | 16 ca Dev (`development.jsonl`) để phát triển; **24 ca Held-Out (`held-out-test.jsonl`) hoàn toàn tách biệt** để kiểm thử độc lập sau khi đóng băng Skill v3 |
| **Phương pháp chấm** | Blind Position-Swapped Pairwise A/B (`eval-blind-judge`, model `pro`, độc lập hoàn toàn với `SKILL.md`). Toàn bộ 24 ca Held-Out được chấm **2 lượt hoán đổi vị trí A/B** (Pass 1 và Pass 2). |
| **Quy tắc chốt kết quả** | Chỉ tính thắng/thua khi cả Pass 1 và Pass 2 đồng thuận; nếu lệch giữa hai lượt, ghi nhận là `position_inconsistent`. |
| **Kiểm tra độ biến động** | Sinh và chấm lại lượt độc lập thứ 2 (Run 2) trên **8 ca đại diện** thuộc đủ 8 ngữ cảnh (`TEST-01, 04, 07, 10, 13, 16, 19, 22`). |

*(Nhật ký quá trình tinh chỉnh v1 → v2 → v3 trên tập Dev xem chi tiết tại [dev-iteration-log.md](./results/dev-iteration-log.md): `DEV v1: 15W/1L/0T` → `DEV v2: 12W/3L/1T` → `DEV v3: 13W/2L/1T`, 0/16 Hard Fail so với 7/16 Hard Fail của Baseline).*

---

## 2. Kết quả Tổng quan trên Tập Kiểm thử Độc lập (24 ca Held-Out)

### 2.1 Tỷ lệ Thắng / Thua / Bất nhất và Gate 0 (Hard Fail)

| Chỉ số | Baseline | Experiment (Skill v3) | Ghi chú |
|---|---:|---:|---|
| **Thắng đồng thuận 2 lượt** (`Pass 1 & Pass 2`) | **1 / 24** (4,17%) | **20 / 24** (83,33%) | Ca Baseline thắng: `TEST-05` |
| **Hòa đồng thuận** (`TIE`) | 0 / 24 (0%) | 0 / 24 (0%) | — |
| **Bất nhất vị trí** (`position_inconsistent`) | — | **3 / 24** (12,50%) | `TEST-02, TEST-21, TEST-24` (P1=Base, P2=Exp) |
| **Độ đồng thuận vị trí** (`Pass 1 == Pass 2`) | — | **21 / 24** (87,50%) | Cho thấy mức độ tồn tại của Position Bias ở ca sát nút |
| **Số ca dính Hard Fail (Gate 0)** | **11 / 24** (45,83%) | **0 / 24** (0,00%) | Baseline: `HF-3` (10 ca), `HF-4` (2), `HF-1` (1), `HF-2` (1), `HF-5` (1) |
| **Độ dài trung bình (số từ)** | 794,29 từ | **573,21 từ** | Tỷ số trung bình `exp / base = 0,78` |

**Phân tích ý nghĩa Gate 0:** Trong 24 ca kiểm thử độc lập, Baseline mắc Hard Fail ở **11/24 ca**, chủ yếu là lỗi `HF-3` (10 ca — tự bịa trường API, quy tắc hoàn tiền, ràng buộc hệ thống hoặc cam kết vận hành như sự thật đã chốt mà không gắn nhãn ví dụ/điểm cần xác nhận) và `HF-4` (2 ca — làm lệch logic nghiệp vụ ở `TEST-13` và `TEST-17`). Experiment v3 đạt **0/24 Hard Fail** nhờ tách biệt rạch ròi giữa dữ kiện gốc và phần *Đề xuất bổ sung / Câu hỏi mở*.

### 2.2 Kiểm chứng Phân nhóm Không Hard Fail (`n = 13` ca cả hai bên đều qua Gate 0)

Để kiểm chứng xem Skill có thực sự cải thiện chất lượng truyền tải ngay cả khi Baseline *không* mắc Hard Fail hay không, nhóm 13 ca sạch được tách riêng:

- **Tỷ lệ kết quả (`n = 13`):** Experiment thắng **10/13** (76,92%), Baseline thắng **1/13** (`TEST-05`), Bất nhất vị trí **2/13** (`TEST-21`, `TEST-24`).
- **Điểm trung bình 9 tiêu chí (thang 0–4, trung bình Pass 1 & Pass 2):**

| Tiêu chí | Toàn bộ 24 ca (Base → Exp) | $\Delta$ (24 ca) | Nhóm sạch 13 ca (Base → Exp) | $\Delta$ (13 ca) |
|---|---:|---:|---:|---:|
| **D1** Semantic Accuracy | 2,000 → 3,708 | **+1,708** | 3,269 → 3,654 | **+0,385** |
| **D2** Completeness | 3,542 → 3,750 | +0,208 | 3,692 → 3,808 | +0,116 |
| **D3** Terminology Consistency | 3,083 → 3,542 | +0,459 | 3,231 → 3,462 | +0,231 |
| **D4** Semantic Clarity | 3,146 → 3,708 | +0,562 | 3,346 → 3,769 | +0,423 |
| **D5** Coherence | 3,229 → 3,875 | +0,646 | 3,308 → 3,962 | **+0,654** |
| **D6** Information Density | 2,792 → 3,729 | **+0,937** | 2,923 → 3,769 | **+0,846** |
| **D7** Naturalness | 3,104 → 3,667 | +0,563 | 3,077 → 3,692 | **+0,615** |
| **D8** Context Appropriateness | 2,917 → 3,688 | **+0,771** | 3,192 → 3,731 | +0,539 |
| **D9** Actionability *(chỉ tính ca áp dụng)* | 2,625 → 3,406 | **+0,781** | 3,417 → 3,750 | +0,333 |

Ngay cả trên 13 ca Baseline hoàn toàn không dính Hard Fail, Skill vẫn nâng đồng loạt cả 9 chiều chất lượng, mạnh nhất ở **Mật độ thông tin (`+0,846`)**, **Mạch lạc (`+0,654`)** và **Độ tự nhiên tiếng Việt (`+0,615`)**.

---

## 3. Phân rã theo 8 Ngữ cảnh & Kiểm chứng Progressive Disclosure

| Ngữ cảnh (`n=3`/nhóm) | Thắng / Thua / Bất nhất | Baseline HF | Exp HF | Từ TB (Base → Exp) | Tỷ số độ dài | Nạp Reference thực tế |
|---|---|---|---|---:|---:|---|
| `casual_chat` | 2 / 0 / 1 | 1 | 0 | 154,0 → 137,3 | 0,914 | **0/3 (0%)** (`[]`) |
| `concept_explanation` | 2 / 1 / 0 | 0 | 0 | 647,0 → 533,0 | 0,869 | 3/3 (`information-architecture.md`) |
| `problem_analysis` | **3 / 0 / 0** | 2 | 0 | 1314,0 → 1107,3 | 0,860 | 3/3 (`information-architecture.md`) |
| `workplace_communication` | **3 / 0 / 0** | 1 | 0 | 276,0 → 173,0 | 0,614 | 2/3 (`information-architecture.md`; `TEST-10` Teams ngắn giữ `[]`) |
| `business_docs` | **3 / 0 / 0** | 3 | 0 | 1900,3 → 1403,0 | 0,850 | 3/3 (`business-specs.md`) |
| `technical_docs` | **3 / 0 / 0** | 3 | 0 | 1446,0 → 837,0 | **0,576** | 3/3 (`technical-specs.md`) |
| `reports_guides_training` | 2 / 0 / 1 | 1 | 0 | 504,7 → 291,0 | 0,640 | 3/3 (`information-architecture.md`) |
| `editing_rewriting` | 2 / 0 / 1 | 0 | 0 | 112,3 → 104,0 | 0,917 | 3/3 (`vietnamese-clarity-and-style.md`) |

**Nhận xét về Progressive Disclosure:** Cơ chế điều hướng 3 chế độ hoạt động đúng thiết kế trên cả 24 ca chưa từng thấy:
- Toàn bộ `casual_chat` (3/3) và tin nhắn Teams ngắn (`TEST-10`) không đọc thêm tệp tham chiếu (`refs=[]`), giữ độ dài gọn và không phình token.
- 100% các ca `business_docs`, `technical_docs` và `editing_rewriting` đọc đúng duy nhất 1 tệp chuyên sâu tương ứng. Đặc biệt ở `technical_docs`, độ dài trung bình giảm từ 1.446 xuống 837 từ (tỷ số 0,576) trong khi xóa sạch toàn bộ 3/3 Hard Fail `HF-3`/`HF-4` của Baseline.

---

## 4. Độ Biến động giữa Các Lượt Sinh (Variance Check — `n = 8`)

Kết quả đối chiếu Run 2 độc lập trên 8 ca đại diện ([held-out-variance-results.jsonl](./results/held-out-variance-results.jsonl)):
- **Tính nhất quán kết quả thắng/thua:** **8/8 (100%)** giữ nguyên kết quả `experiment` thắng như Run 1.
- **Hard Fail ở Run 2:** Baseline mắc Hard Fail ở **3/8 ca** (`TEST-13`: `HF-2, HF-3, HF-4`; `TEST-16`: `HF-3`; `TEST-19`: `HF-3`); Experiment tiếp tục giữ **0/8 ca**.
- **Độ dài trung bình Run 2:** Baseline 823,5 từ vs Experiment 499,25 từ (ổn định so với Run 1).

---

## 5. Phân tích Ca Thua và Các Ca Bất nhất Vị trí

### 5.1 Ca Experiment thua: `TEST-05` (*Kafka Partition Key vs RabbitMQ Consistent Hash cho Staff Engineer*)
- **Kết quả:** Pass 1 = Baseline, Pass 2 = Baseline; cả hai đều `0 Hard Fail` (`Base 1053 từ`, `Exp 741 từ`).
- **Nguyên nhân thực chất:**
  1. Đề bài yêu cầu so sánh **hai trục kỹ thuật sâu** cho Staff Engineer: *(a) cơ chế lưu trữ* và *(b) bảo đảm thứ tự*. Experiment nén phần cơ chế lưu trữ xuống quá mỏng (chỉ 1 câu mở đầu và 1 dòng trong bảng), bỏ qua phân tích lưu trữ Classic Queue vs Quorum Queue (Raft log và compaction), hành vi drop/Alternate Exchange khi không có queue khớp và quy tắc binding key số nguyên dương (`D-03`, `Major`).
  2. Do ép gọn bảng so sánh, Experiment đơn giản hóa sai chi tiết Quorum Queue (*"bị xóa ngay khi `basic.ack`"*) và khẳng định đẩy message lỗi sang DLX vẫn *"giữ thứ tự nghiêm ngặt"* (thực tế đẩy `M1` sang DLX khiến `M2` cùng key chạy vượt trước `M1` — `R-04`, `Major`).
  3. Dùng backtick cho `` `binding weight` `` như tên tham số cấu hình AMQP (`S-06`).
- **Bài học cải tiến:** Với bài giải thích kỹ thuật cho chuyên gia yêu cầu đối chiếu nhiều trục cụ thể, không được nén quá tay phần cơ chế nội tại trên một trục khiến thiếu chiều sâu và phát sinh đơn giản hóa sai (`R-04`).

### 5.2 Ba ca bất nhất vị trí (`position_inconsistent` — cả 3 ca đều có `Pass 1 = Baseline`, `Pass 2 = Experiment`)
Lưu ý đáng chú ý: Trong dữ liệu của ta, `TEST-02`, `TEST-21` và `TEST-24` đều có chỉ số lẻ (`idx = 1, 20, 23` — tức Pass 1 đặt `A=Exp, B=Base` và Pass 2 đặt `A=Base, B=Exp`). Cả 3 lần giám khảo đều chọn **Output B** — cho thấy ở các ca chất lượng hai bên tương đương sát nút, **Position Bias thiên về vị trí B** xuất hiện rõ. Phân tích thực chất từng ca:
- **`TEST-02` (`casual_chat` — lệnh Git gỡ `.env` khỏi staging):** Baseline mắc `HF-5` ở Pass 2 (thiếu cảnh báo phân biệt với lệnh xóa file trên máy) nhưng thắng ở Pass 1 về độ chuẩn kỹ thuật câu lệnh; ngược lại, Experiment v3 giữ văn phong chat rất gọn (`108 từ`, `refs=[]`) nhưng mắc lỗi kỹ thuật Git ở một câu: gộp Git bản cũ với repo chưa có commit để dùng `git rm --cached .env` (nếu `.env` từng được commit trước đó, `git rm --cached` sẽ stage lệnh xóa file khỏi repo thay vì chỉ gỡ khỏi staging) và dùng từ *"rút file"* hơi gượng.
- **`TEST-21` (`reports_guides_training` — Onboarding Docker local):** Experiment v3 đưa cảnh báo *"Không sửa `docker-compose.yml`"* và quy tắc cổng `5432` lên trước các bước chạy (tốt ở trình tự an toàn `D5`), nhưng bị trừ điểm do lặp ý giữa Mục 2 và Mục 3 (`P-04`), viết *"Migrate dữ liệu"* cho `npm run db:migrate` (`S-06`), và thiếu bước chạy lại `docker compose up -d` nếu lỗi cổng mới phát hiện ở Bước 3; trong khi Baseline viết mượt và đủ lệnh hơn nhưng lại đẩy cảnh báo cổng `5432` xuống Mục 4 cuối bài (`D-02`).
- **`TEST-24` (`editing_rewriting` — Biên tập chính sách hoàn học phí):** Hai bản có chất lượng rất gần nhau (`Base 135 từ`, `Exp 139 từ`, cả hai `0 HF`). Baseline xếp 3 đầu mục song hành theo mốc thời gian mượt hơn, nhưng dùng *"học viên vui lòng nộp đơn"* chưa nhất quán cụm *"học phí đã đóng"* ở mức 70%; Experiment giữ rõ *"học phí đã đóng"* ở cả hai mức nhưng dùng cụm *"đề nghị giải quyết"* hơi nặng hành chính và làm gãy song hành giữa 2 đầu mục mở bằng *"Nộp đơn..."* với mục thứ 3 mở bằng *"Sau khi..."*.

---

## 6. Giới hạn Kiểm thử và Hạng mục Chưa được Kiểm chứng

1. **Chưa thực hiện Human Evaluation với người Việt và chuyên gia thật:** Do giới hạn không tuyển người tham gia và không phát sinh chi phí ngoài, chỉ số cốt lõi **Time to Correct Understanding (TtCU)**, điểm nỗ lực nhận thức Paas (1–9) và tỷ lệ trả lời đúng câu hỏi tình huống thực tế trên người đọc thật **chưa được đo**. Hiện mới hoàn tất thiết kế quy trình chuẩn tại [human-eval-protocol.md](./human-eval-protocol.md).
2. **Kiểm thử trên một họ mô hình duy nhất:** Cả Baseline và Experiment đều sinh trên model tier `flash` và chấm bằng model tier `pro` trong hệ sinh thái Antigravity. Chưa kiểm chứng mức độ tổng quát của Skill khi chạy trên các họ LLM khác (như GPT, Claude hay các mô hình tiếng Việt mã nguồn mở).
3. **Giới hạn của LLM-as-a-Judge:** Mặc dù đã làm mù hoàn toàn, tách `SKILL.md` khỏi prompt giám khảo, dùng rubric phi bù trừ và chạy hoán đổi vị trí 2 lượt trên 100% mẫu Held-Out, việc dùng LLM cùng họ để chấm vẫn có rủi ro thiên lệch hệ thống (Self-Enhancement Bias, Zheng et al., 2023) và đòi hỏi xác thực chéo bằng chuyên gia người Việt trước khi công bố hiệu quả định lượng cuối cùng.
4. **Cỡ mẫu còn khiêm tốn ở từng ngữ cảnh:** Tập Held-Out có 24 ca (`n = 3` mỗi ngữ cảnh) — đủ cho đánh giá thăm dò đa ngữ cảnh nhưng chưa đủ cỡ mẫu lớn để kiểm định ý nghĩa thống kê riêng cho từng thể loại đơn lẻ.
