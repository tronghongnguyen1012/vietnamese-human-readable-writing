# Vietnamese Human-Readable Writing Skill (`v4.1.0-beta`)

Skill chuẩn [`agentskills.io`](https://agentskills.io) giúp AI truyền tải thông tin bằng tiếng Việt **rõ nghĩa ngay từ lần đọc đầu**, **đúng trình tự tiếp nhận của con người**, **giữ nguyên dữ kiện/điều kiện nghiệp vụ**, **đồng nhất trạng thái xác nhận xuyên suốt tài liệu**, **không tự bịa để tạo độ rõ giả tạo (False Clarity)** và **thích ứng đúng ngữ cảnh** — từ hội thoại tự nhiên đến PRD, BRD, IDD, API Spec, SAD và biên tập tài liệu kỹ thuật.

> [!NOTE]
> Phiên bản phát hành chính thức trên `main` là **Skill v4.1 Beta** (tag `v4.1.0-beta`), đã hoàn tất Independent Review và sẵn sàng cài đặt thử nghiệm thực tế có kiểm soát. Xem chi tiết bản vá tại [v4.1-stabilization-report.md](./evaluation/v4.1-stabilization-report.md) và lịch sử phiên bản tại [CHANGELOG.md](./CHANGELOG.md).

---

## 1. Cấu trúc Dự án

Phần **Skill cài đặt vào runtime** tách biệt hoàn toàn với phần **Nghiên cứu**, **Kiểm toán** và **Kiểm thử**:

```text
Vi Writer/
├── README.md                                  # Hướng dẫn cài đặt Beta, lựa chọn phương án & tổng quan kết quả
├── CHANGELOG.md                               # Lịch sử thay đổi v1 -> v2 -> v3 -> v4 -> v4.1
├── REVIEW-FINDINGS.md                         # Xác minh 10 finding độc lập FIX-01..FIX-10
├── DESIGN_DECISIONS.md                        # Quyết định thiết kế, đối chứng Ablation & việc tồn đọng
├── skills/
│   └── vietnamese-human-readable-writing/     # <-- CHỈ COPY THƯ MỤC NÀY ĐỂ CÀI ĐẶT
│       ├── SKILL.md                           # Instruction cốt lõi (82 dòng, 8.904 bytes)
│       └── references/                        # Progressive Disclosure linh hoạt (0, 1 hoặc tối đa 2 file)
│           ├── vietnamese-clarity-and-style.md
│           ├── information-architecture.md
│           ├── business-specs.md
│           └── technical-specs.md
├── research/
│   ├── research-report.md                     # Cơ sở Việt ngữ học & Thiết kế thông tin
│   ├── sources.md
│   ├── error-taxonomy.md
│   └── competitive-research-report.md         # Đối chiếu trực tiếp 8 GitHub repo công khai
└── evaluation/
    ├── rubric.md / rubric-v2.md               # Rubric v1 (lịch sử) & Rubric v2 (Round 2)
    ├── judge-instructions.md / ...-v2.md      # Hướng dẫn Judge mù 2 lượt hoán đổi
    ├── human-eval-protocol.md                 # Quy trình đo TtCU trên người thật (CHƯA thực thi)
    ├── development.jsonl                      # 16 ca phát triển
    ├── held-out-test.jsonl                    # Bộ Regression v3 (24 ca, hạ cấp từ Round 1)
    ├── held-out-v2.jsonl                      # Bộ kiểm thử mới 24 ca (gồm 4 ca dài mô phỏng)
    ├── judge-calibration.jsonl                # 6 ca kiểm chuẩn Judge v2
    ├── trigger-eval.jsonl                     # 16 truy vấn kiểm thử kích hoạt
    ├── evaluation-report.md                   # Báo cáo v3 lịch sử (kèm Errata Round 2)
    ├── evaluation-report-v2.md                # Báo cáo Round 2 đầy đủ (4 nhóm A/B/C0/C + Đính chính v4.1)
    ├── standalone-hf-protocol.md              # Quy trình Gate 0 độc lập 1 output/lượt & HF 3 mức
    ├── v4.1-stabilization-report.md           # Báo cáo bản vá v4.1 & kiểm thử hồi quy tập trung (n=9)
    ├── scripts/
    │   ├── validate_datasets.py               # Kiểm tra schema, chống leakage (Jaccard) & Skill v4.1
    │   ├── analyze_results.py                 # Thống kê Round 1 (lịch sử)
    │   └── analyze_results_v2.py              # Thống kê Round 2 -> results-v2/summary-stats-v2.json
    ├── results/                               # Dữ liệu thô v3 lịch sử (giữ nguyên)
    ├── results-v2/                            # Run manifest, calibration, re-audit v3 & kết quả 4 nhóm v4
    └── results-v4.1/                          # Audit Gate 0 độc lập & hồi quy tập trung v4.1 (n=9)
```

---

## 2. Hướng dẫn Cài đặt & Chọn Phương án Sử dụng

### Cài đặt Skill v4.1 Beta trên Windows
Chỉ cần sao chép thư mục `skills\vietnamese-human-readable-writing\` vào đúng thư mục skills của runtime bạn sử dụng (tên thư mục đích bắt buộc là `vietnamese-human-readable-writing` khớp trường `name` trong `SKILL.md`):

| Công cụ AI | Cài cho từng dự án (Project-local) | Cài toàn cục (Global trên Windows) |
|---|---|---|
| **Antigravity** | `<project-root>\.agents\skills\vietnamese-human-readable-writing\` | `%USERPROFILE%\.gemini\config\skills\vietnamese-human-readable-writing\` |
| **Claude Code** | `<project-root>\.claude\skills\vietnamese-human-readable-writing\` | `%USERPROFILE%\.claude\skills\vietnamese-human-readable-writing\` |
| **OpenAI Codex** | `<project-root>\.agents\skills\vietnamese-human-readable-writing\` *(hoặc `.\.codex\skills\...`)* | `%USERPROFILE%\.agents\skills\vietnamese-human-readable-writing\` *(hoặc `%USERPROFILE%\.codex\skills\...`)* |

**Lệnh PowerShell cài đặt nhanh từ thư mục gốc của repo:**

```powershell
# Chạy tại thư mục gốc của repo (nơi chứa thư mục skills\)
$src = ".\skills\vietnamese-human-readable-writing"

# 1. Antigravity (Global trên Windows)
$destAgy = "$env:USERPROFILE\.gemini\config\skills\vietnamese-human-readable-writing"
New-Item -ItemType Directory -Force -Path (Split-Path $destAgy) | Out-Null
Copy-Item -Recurse -Force $src $destAgy

# 2. Claude Code (Global trên Windows)
$destClaude = "$env:USERPROFILE\.claude\skills\vietnamese-human-readable-writing"
New-Item -ItemType Directory -Force -Path (Split-Path $destClaude) | Out-Null
Copy-Item -Recurse -Force $src $destClaude

# 3. OpenAI Codex (Global trên Windows — có thể dùng .codex\skills thay cho .agents\skills)
$destCodex = "$env:USERPROFILE\.codex\skills\vietnamese-human-readable-writing"
New-Item -ItemType Directory -Force -Path (Split-Path $destCodex) | Out-Null
Copy-Item -Recurse -Force $src $destCodex
```

*(Nếu cài theo từng dự án, thay biến `$dest...` bằng `<project-root>\.agents\skills\vietnamese-human-readable-writing` cho Antigravity/Codex hoặc `<project-root>\.claude\skills\vietnamese-human-readable-writing` cho Claude Code.)*

### Xác minh Cấu trúc & Kiểm tra Kích hoạt Runtime
1. **Kiểm tra cấu trúc gói đã copy** gồm đủ 5 file (không copy nhầm `research/` hay `evaluation/`):
   ```text
   vietnamese-human-readable-writing\
   ├── SKILL.md
   └── references\
       ├── business-specs.md
       ├── information-architecture.md
       ├── technical-specs.md
       └── vietnamese-clarity-and-style.md
   ```
   Có thể kiểm tra nhanh trong PowerShell: `Get-ChildItem -Recurse -File "<đường-dẫn-đích>"`.
2. **Mở phiên làm việc mới** trên Antigravity / Claude Code / Codex để runtime nạp lại danh sách skill.
3. **Kiểm tra Discovery:** Gõ `/skills` trong Codex hoặc Claude Code (hoặc kiểm tra danh sách available skills trong Antigravity) và xác nhận `vietnamese-human-readable-writing` xuất hiện đúng với `description`.
4. **Kiểm tra kích hoạt thực tế (2 câu test nhanh):**
   - *Nên kích hoạt (Positive):* Thử yêu cầu *"Viết lại câu quy tắc nghiệp vụ tiếng Việt sau cho rõ nghĩa mà không tự bịa thêm dữ kiện: Sau 3 lần vi phạm liên tiếp, thực hiện khóa tạm thời tài khoản và gửi thông báo cho quản trị viên."* → Skill kích hoạt sẽ tách rõ phần đã biết và liệt kê điểm chưa xác định (`thời hạn khóa`, `kênh/nội dung thông báo`).
   - *Không nên kích hoạt (Negative):* Thử yêu cầu lập trình thuần tiếng Anh như *"Write a Python pytest unit test for binary search"* → Skill giữ nguyên không can thiệp.

### Khi nào chỉ cần Simple Prompt vs `SKILL.md` độc lập vs Full Skill (`v4.1.0-beta`)?
Thực nghiệm đối chứng Round 2 trên `held-out-v2.jsonl` (`v4.0`, trước bản vá `v4.1`) cho thấy rõ đánh đổi chi phí – chất lượng (tách riêng tập `n = 24` và tập `n = 12` trùng khớp của `C0`; mọi số token là **ước lượng heuristic theo `bytes / 3,8`** vì runtime không cung cấp billing token usage thực tế):

**Bảng A — Trên trọn bộ `held-out-v2.jsonl` (`n = 24`):**

| Lựa chọn | Kích thước / Ước lượng token hệ thống | Độ trễ TB (`flash`) | Hard Fail (Judge cặp đấu `pro`) | Phù hợp nhất cho |
|---|---:|---:|---:|---|
| **Simple Prompt 6 ý** (`Group B`) | `609 bytes` *(~160 tokens ước lượng)* | `23,80s` | **`8 / 24 (33,3%)`** *(vs C)* | Hỏi đáp nhanh, trò chuyện tự nhiên không có rủi ro nghiệp vụ/kỹ thuật. |
| **Full Skill** (`Group C`, bản v4 + `0–2` ref) | `8.694 → 19.019 bytes` *(TB ~3.814 tokens ước lượng)* | `39,11s` | **`0 / 24`** *(vs A)* \| **`1 / 24`** *(vs B: `H2-06`)* | Đặc tả PRD/BRD/IDD/API/SAD, phân tích kỹ thuật đa trục, biên tập nguồn thiếu chi tiết. |

**Bảng B — Trên đúng 12 ca phức tạp trùng khớp của nhóm Ablation (`n = 12`):**
`A: 5/12` HF \| `B: 6/12` HF \| `C0 (SKILL.md-only, 8.694 bytes / ~2.288 tokens ước lượng, 29,06s): 2/12` HF \| `C (Full Skill v4): 0/12` *(khi ghép vs A/B)* và `2/12` *(khi ghép vs C0 — `H2-12, H2-19`)*. Khi dùng kết hợp quy chuẩn kiểm định độc lập trong [standalone-hf-protocol.md](./evaluation/standalone-hf-protocol.md) trên bản phát hành **v4.1 Beta** cho 9 ca hồi quy tập trung, **v4.1 đạt `0/9` Hard Fail**.

> [!TIP]
> Trong **chế độ Nhẹ**, Skill **không nạp thêm file tham chiếu** (`refs = []`), chỉ nạp phần `SKILL.md` (`~2.288 tokens` ước lượng) khi được kích hoạt (`trigger` `16/16`, `F1 = 1,00`). Chi tiết đánh giá bản vá xem [v4.1-stabilization-report.md](./evaluation/v4.1-stabilization-report.md).

---

## 3. Tóm tắt Kết quả Kiểm thử (`v4.0` Round 2 & Bản vá `v4.1 Beta`)

Toàn bộ kết quả chấm mù thực hiện trên `flash` (sinh) và `pro` (giám khảo [eval-blind-judge-v2](./evaluation/judge-instructions-v2.md) đã hiệu chuẩn `5/6`, hoán đổi 2 lượt vị trí A/B). Chi tiết xem [evaluation-report-v2.md](./evaluation/evaluation-report-v2.md) và [v4.1-stabilization-report.md](./evaluation/v4.1-stabilization-report.md).

1. **Kiểm toán lại dữ liệu lịch sử v3 dưới Rubric v2 (`n = 24`, [held-out-test.jsonl](./evaluation/held-out-test.jsonl)):**
   - Kết quả lịch sử v3 điều chỉnh từ `20W/1L/3 Inc` (`0/24 HF`) thành **`18` thắng v3 / `2` thua Baseline (`TEST-02`, `TEST-05`) / `4` bất nhất**, trong đó **Skill v3 dính `2/24` HF (`HF-6`: `TEST-02`, `TEST-05`)** và **Baseline dính `8/24` HF**.
   - Xem thêm Errata số liệu Báo cáo v3 tại [evaluation-report.md](./evaluation/evaluation-report.md).
2. **Bộ Hồi quy (`Regression v4 vs v3`, `n = 24`):**
   - `v4` xóa sạch toàn bộ 3 ca HF của `v3` (`TEST-02, 05, 17`: **`0/24` HF** vs `3/24`), thắng **`9` vs `8`** (`7` bất nhất vị trí), tăng mạnh điểm **Đầy đủ `D2` (`3,750` vs `3,375`)**, **Tính sử dụng được `D9` (`3,562` vs `3,125`)** và **Trung thực `D1` (`3,312` vs `3,104`)** dù văn bản dài hơn (`767,9` vs `573,2` từ).
3. **Bộ Kiểm thử Mới `held-out-v2.jsonl` (`n = 24`, gồm `technical_depth`, `ambiguity_no_fabrication`, `natural_conversation`, `hybrid_docs`, `real_world_long_docs` mô phỏng):**
   - **`C (Full v4)` vs `A (Neutral)`:** **`20 / 24 (83,3%)`** thắng đồng thuận (`3` thua `A`, `1` bất nhất), **`0/24` vs `8/24` HF**, nhóm sạch (`n=16`) thắng **`12/16` (`75%`)**.
   - **`C (Full v4)` vs `B (Simple Prompt)`:** **`17 / 24 (70,8%)`** thắng đồng thuận (`1` thua `B` tại `H2-14`, `6` bất nhất), **`1/24` (`H2-06: HF-2`) vs `8/24` HF**, nhóm sạch (`n=15`) thắng **`9/15`**.
   - **`C (Full v4)` vs `C0 (SKILL-only Ablation, n = 12)`:** **`7 / 12` thắng `C`** vs `3` thắng `C0` (`H2-12, 19, 22`), `2` bất nhất *(trên đúng 12 ca này: `C0` và `C` cùng ghi nhận `2/12` HF theo Judge cặp đấu)*.
4. **Bản vá `v4.1.0-beta` & Kiểm thử Hồi quy Tập trung (`n = 9` ca đã biết, KHÔNG phải held-out benchmark mới):**
   - Kiểm định Gate 0 độc lập 1 output/lượt ([standalone-hf-protocol.md](./evaluation/standalone-hf-protocol.md)) xác nhận `H2-06` là `Verified HF` (`2/2` lượt standalone) ở bản `v4`, còn `H2-12` và `H2-19` `PASS_GATE_0` ở standalone (`H2-19` có mâu thuẫn xác nhận giữa Bảng/Mermaid và Câu hỏi mở).
   - Trên 9 ca hồi quy tập trung (`v4.1 vs v4`), **Skill v4.1 đạt `0/9` Hard Fail** ở cả Standalone Gate 0 lẫn Blind A/B (`v4.1` thắng **`4`** gồm `H2-06, H2-12, H2-19, TEST-05`; `v4` thắng **`3`**; `2` bất nhất; điểm `D1 +0,556`, `D4 +0,334`, `D9 +0,700`).
5. **Hạn chế chưa kiểm chứng:** Chưa chạy thực nghiệm đo thời gian hiểu đúng trên người đọc Việt Nam thật (`TtCU`, xem [human-eval-protocol.md](./evaluation/human-eval-protocol.md)); 4 ca `real_world_long_docs` là tài liệu mô phỏng sát thực tế; mới kiểm thử trong 1 họ mô hình (`flash` / `pro`) nên chưa kết luận độ ổn định chéo Claude/GPT/model khác.

---

## 4. Kiểm định Toàn vẹn & Tái chạy Thống kê

```bash
python evaluation/scripts/validate_datasets.py --check-skill
python evaluation/scripts/analyze_results_v2.py
```
