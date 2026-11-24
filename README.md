# Vietnamese Human-Readable Writing Skill (`Skill v4`)

Skill chuẩn [`agentskills.io`](https://agentskills.io) giúp AI truyền tải thông tin bằng tiếng Việt **rõ nghĩa ngay từ lần đọc đầu**, **đúng trình tự tiếp nhận của con người**, **giữ nguyên dữ kiện/điều kiện nghiệp vụ**, **không tự bịa để tạo độ rõ giả tạo (False Clarity)** và **thích ứng đúng ngữ cảnh** — từ hội thoại tự nhiên đến PRD, BRD, IDD, API Spec, SAD và biên tập tài liệu kỹ thuật.

> [!NOTE]
> Phiên bản hiện tại trên nhánh `round-2/v4-stabilization` là **Skill v4**, được nâng cấp và kiểm chứng độc lập sau vòng ổn định Round 2 đối chiếu với bản v3 lịch sử tại commit `cd5bba945886222d0ebd236b3c1ba92a60dd3155`.

---

## 1. Cấu trúc Dự án

Phần **Skill cài đặt vào runtime** tách biệt hoàn toàn với phần **Nghiên cứu**, **Kiểm toán** và **Kiểm thử**:

```text
Vi Writer/
├── README.md                                  # Hướng dẫn cài đặt, lựa chọn phương án & tổng quan kết quả
├── CHANGELOG.md                               # Lịch sử thay đổi v1 -> v2 -> v3 -> v4
├── REVIEW-FINDINGS.md                         # Xác minh 10 finding độc lập FIX-01..FIX-10
├── DESIGN_DECISIONS.md                        # Quyết định thiết kế, đối chứng Ablation & việc tồn đọng
├── skills/
│   └── vietnamese-human-readable-writing/     # <-- CHỈ COPY THƯ MỤC NÀY ĐỂ CÀI ĐẶT
│       ├── SKILL.md                           # Instruction cốt lõi (78 dòng, 9.132 bytes)
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
    ├── evaluation-report-v2.md                # Báo cáo Round 2 đầy đủ (4 nhóm A/B/C0/C + Overhead)
    ├── scripts/
    │   ├── validate_datasets.py               # Kiểm tra schema, chống leakage (Jaccard) & Skill v4
    │   ├── analyze_results.py                 # Thống kê Round 1 (lịch sử)
    │   └── analyze_results_v2.py              # Thống kê Round 2 -> results-v2/summary-stats-v2.json
    ├── results/                               # Dữ liệu thô v3 lịch sử (giữ nguyên)
    └── results-v2/                            # Run manifest, calibration, re-audit v3 & kết quả 4 nhóm v4
```

---

## 2. Hướng dẫn Cài đặt & Chọn Phương án Sử dụng

### Cài đặt Skill v4
Sao chép nguyên thư mục `skills/vietnamese-human-readable-writing/` vào thư mục `skills/` của công cụ AI bạn sử dụng:
- **Antigravity (theo dự án):** `<project-root>/.agents/skills/vietnamese-human-readable-writing/`
- **Antigravity (toàn cục):** `~/.gemini/config/skills/vietnamese-human-readable-writing/`
- **Claude Code:** `~/.claude/skills/vietnamese-human-readable-writing/` hoặc `.claude/skills/vietnamese-human-readable-writing/`
- **Cursor / Codex / harness chuẩn `agentskills.io`:** Đặt vào thư mục skills tương ứng của workspace hoặc cấu hình toàn cục.

### Khi nào chỉ cần Simple Prompt vs `SKILL.md` độc lập vs Full Skill v4?
Thực nghiệm đối chứng 4 nhóm trên `held-out-v2.jsonl` (`n = 24`) cho thấy rõ đánh đổi chi phí – chất lượng giữa 3 lựa chọn:

| Lựa chọn | Chi phí Prompt hệ thống | Tỷ lệ Hard Fail (`held-out-v2`) | Phù hợp nhất cho |
|---|---:|---:|---|
| **Simple Prompt 6 ý** (`Group B`) | `609 bytes` (`~160 tokens`), trễ TB `23,80s` | **`8 / 24 (33,3%)`** *(không giảm HF so với Neutral A)* | Hỏi đáp nhanh, trò chuyện tự nhiên đời thường không có rủi ro nghiệp vụ/kỹ thuật, cần phản hồi nhanh nhất. |
| **Chỉ `SKILL.md` v4** (`Group C0`, host không đọc được `references/`) | `8.694 bytes` (`~2.288 tokens`), trễ TB `29,06s` | `2 / 12 (16,7%)` trên 12 ca khó | Harness giới hạn tool đọc file hoặc cần giảm mạnh bịa dữ kiện (`HF-3`) mà vẫn giữ 1 vòng gọi mô hình. |
| **Full Skill v4** (`Group C`, `0–2` references) | `8.694 → 19.019 bytes` (TB `~3.814 tokens`), trễ TB `39,11s` | **`0 / 24 (0,0%)`** vs A; **`1 / 24 (4,2%)`** vs B *(17–1 thắng B)* | Đặc tả PRD/BRD/IDD/API/SAD, phân tích đánh đổi kỹ thuật đa trục, biên tập quy tắc/luồng dữ liệu nguồn thiếu chi tiết (*Trường hợp B*). |

> [!TIP]
> Trong **chế độ Nhẹ**, Full Skill v4 **không nạp thêm file tham chiếu** (`refs = []`), tránh tốn chi phí đọc file khi hội thoại ngắn, nhưng vẫn nạp cơ bản `SKILL.md` (`~2.288 tokens`) khi kích hoạt — vì vậy nếu cuộc trò chuyện thuần túy tán gẫu không liên quan kỹ thuật/tài liệu, `trigger` của Skill giữ kích hoạt đúng ngữ cảnh (`16/16`, `F1 = 1,00`).

---

## 3. Tóm tắt Kết quả Kiểm thử Round 2 (Skill v4)

Toàn bộ kết quả chấm mù thực hiện trên `flash` (sinh) và `pro` (giám khảo [eval-blind-judge-v2](./evaluation/judge-instructions-v2.md) đã hiệu chuẩn `5/6`, hoán đổi 2 lượt vị trí A/B). Chi tiết xem [evaluation-report-v2.md](./evaluation/evaluation-report-v2.md).

1. **Kiểm toán lại dữ liệu lịch sử v3 dưới Rubric v2 (`n = 24`, [held-out-test.jsonl](./evaluation/held-out-test.jsonl)):**
   - Khi bắt nghiêm lỗi `HF-6` và bỏ phạt `HF-3` quá nhạy ở sáo ngữ vô hại, kết quả lịch sử v3 điều chỉnh từ `20W/1L/3 Inc` (`0/24 HF`) thành **`18` thắng v3 / `2` thua Baseline (`TEST-02`, `TEST-05`) / `4` bất nhất**, trong đó **Skill v3 dính `2/24` HF (`HF-6`: `TEST-02`, `TEST-05`)** và **Baseline dính `8/24` HF**.
   - Xem thêm Errata số liệu Báo cáo v3 tại [evaluation-report.md](./evaluation/evaluation-report.md).
2. **Bộ Hồi quy (`Regression v4 vs v3`, `n = 24`):**
   - `v4` xóa sạch toàn bộ 3 ca HF của `v3` (`TEST-02, 05, 17`: **`0/24` HF** vs `3/24`), thắng **`9` vs `8`** (`7` bất nhất vị trí), tăng mạnh điểm **Đầy đủ `D2` (`3,750` vs `3,375`)**, **Tính sử dụng được `D9` (`3,562` vs `3,125`)** và **Trung thực `D1` (`3,312` vs `3,104`)** dù văn bản dài hơn (`767,9` vs `573,2` từ).
3. **Bộ Kiểm thử Mới `held-out-v2.jsonl` (`n = 24`, gồm `technical_depth`, `ambiguity_no_fabrication`, `natural_conversation`, `hybrid_docs`, `real_world_long_docs` mô phỏng):**
   - **`C (Full v4)` vs `A (Neutral)`:** **`20 / 24 (83,3%)`** thắng đồng thuận (`3` thua `A`, `1` bất nhất), **`0/24` vs `8/24` HF**, nhóm sạch (`n=16`) thắng **`12/16` (`75%`)**.
   - **`C (Full v4)` vs `B (Simple Prompt)`:** **`17 / 24 (70,8%)`** thắng đồng thuận (`1` thua `B` tại `H2-14`, `6` bất nhất), **`1/24` (`H2-06: HF-2`) vs `8/24` HF**, nhóm sạch (`n=15`) thắng **`9/15`**.
   - **`C (Full v4)` vs `C0 (SKILL-only Ablation, n = 12)`:** **`7 / 12` thắng `C`** vs `3` thắng `C0` (`H2-12, 19, 22`), `2` bất nhất.
4. **Hạn chế chưa kiểm chứng:** Chưa chạy thực nghiệm đo thời gian hiểu đúng trên người đọc Việt Nam thật (`TtCU`, xem [human-eval-protocol.md](./evaluation/human-eval-protocol.md)); 4 ca `real_world_long_docs` là tài liệu mô phỏng sát thực tế; mới kiểm thử trong 1 họ mô hình (`flash` / `pro`) nên chưa kết luận độ ổn định chéo Claude/GPT/model khác.

---

## 4. Kiểm định Toàn vẹn & Tái chạy Thống kê

```bash
python evaluation/scripts/validate_datasets.py --check-skill
python evaluation/scripts/analyze_results_v2.py
```
