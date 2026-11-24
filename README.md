# Vietnamese Human-Readable Writing Skill

Skill chuẩn [`agentskills.io`](https://agentskills.io) giúp AI truyền tải thông tin bằng tiếng Việt **rõ nghĩa ngay từ lần đọc đầu**, **đúng trình tự tiếp nhận của con người**, **giữ nguyên 100% dữ kiện/điều kiện nghiệp vụ** và **phù hợp từng ngữ cảnh** (từ chat hằng ngày đến PRD, BRD, API Spec, System Design và biên tập tài liệu).

---

## 1. Cấu trúc Dự án

Phần **Skill cài đặt vào runtime** được tách biệt hoàn toàn khỏi phần **Nghiên cứu** và **Kiểm thử**:

```text
Vi Writer/
├── README.md                                  # Hướng dẫn cài đặt và sử dụng
├── DESIGN_DECISIONS.md                        # Nhật ký quyết định thiết kế & việc tồn đọng
├── skills/
│   └── vietnamese-human-readable-writing/     # <-- CHỈ COPY THƯ MỤC NÀY ĐỂ CÀI ĐẶT
│       ├── SKILL.md                           # Instruction cốt lõi (90 dòng)
│       └── references/                        # Progressive Disclosure (chỉ đọc khi cần)
│           ├── vietnamese-clarity-and-style.md
│           ├── information-architecture.md
│           ├── business-specs.md
│           └── technical-specs.md
├── research/                                  # Cơ sở nghiên cứu & phân loại lỗi
│   ├── research-report.md
│   ├── sources.md
│   └── error-taxonomy.md
└── evaluation/                                # Bộ dữ liệu, rubric & báo cáo kiểm thử
    ├── rubric.md
    ├── human-eval-protocol.md
    ├── judge-instructions.md
    ├── development.jsonl                      # 16 test cases phát triển
    ├── held-out-test.jsonl                    # 24 test cases kiểm thử độc lập
    ├── evaluation-report.md                   # Báo cáo kết quả & giới hạn thực nghiệm
    ├── scripts/
    │   ├── validate_datasets.py
    │   └── analyze_results.py
    └── results/                               # Dữ liệu thô, nhật ký lặp & thống kê
```

---

## 2. Hướng dẫn Cài đặt & Sử dụng

Chỉ cần sao chép thư mục `skills/vietnamese-human-readable-writing/` vào thư mục `skills/` của công cụ AI bạn đang dùng (tên thư mục khớp chính xác với trường `name` trong `SKILL.md`):

- **Antigravity (theo dự án):** Copy vào `<project-root>/.agents/skills/vietnamese-human-readable-writing/`
- **Antigravity (toàn cục trên máy):** Copy vào `~/.gemini/config/skills/vietnamese-human-readable-writing/`
- **Claude Code:** Copy vào `~/.claude/skills/vietnamese-human-readable-writing/` hoặc `.claude/skills/vietnamese-human-readable-writing/`
- **Cursor / Codex / các runtime hỗ trợ `agentskills.io`:** Đặt vào thư mục skills tương ứng của workspace hoặc cấu hình toàn cục.

Sau khi cài đặt:
- Ở trạng thái chờ (**Discovery**), runtime chỉ nạp `name` và `description` (297 ký tự).
- Khi bạn hỏi đáp nhanh hoặc nhắn tin ngắn bằng tiếng Việt, Skill chỉ dùng `SKILL.md` (**chế độ Nhẹ**, không đọc thêm file tham chiếu).
- Khi bạn soạn thảo/review PRD, BRD, User Story, AC, API Spec, SAD, báo cáo hoặc biên tập văn bản nặng dịch máy, Skill tự đọc đúng **1 file** tương ứng trong `references/` (**Progressive Disclosure**).

---

## 3. Tóm tắt Kết quả Kiểm thử Độc lập (Held-Out `n = 24`)

Trên tập kiểm thử độc lập gồm **24 ca hoàn toàn tách biệt** thuộc 8 ngữ cảnh (cùng mức model sinh `flash`, đánh giá mù 2 lượt hoán đổi vị trí A/B bằng giám khảo `pro` và kiểm tra độ biến động Run 2 trên 8 ca đại diện):

| Chỉ số | Baseline (Không Skill) | Skill v3 (Đóng băng) |
|---|---:|---:|
| **Thắng đồng thuận cả 2 lượt hoán đổi A/B** | 1 / 24 (4,17%) | **20 / 24 (83,33%)** |
| **Bất nhất vị trí giữa Pass 1 & Pass 2** | — | 3 / 24 (12,50%) |
| **Số ca dính Hard Fail (bịa dữ kiện/lệch logic)** | **11 / 24 (45,83%)** | **0 / 24 (0,00%)** |
| **Độ dài trung bình** | 794,29 từ | **573,21 từ** (tỷ số 0,78) |
| **Nhóm sạch không Hard Fail (`n = 13`)** | 1 thắng | **10 thắng** (`D6 +0,846`, `D5 +0,654`, `D7 +0,615`) |
| **Variance Check Run 2 (`n = 8`)** | 3/8 Hard Fail | **8/8 thắng**, 0/8 Hard Fail |

**Giới hạn quan trọng:** Kết quả trên dựa vào đánh giá tự động bằng LLM Judge trong một họ mô hình; **chưa thực thi đo thời gian hiểu đúng (TtCU) trực tiếp trên người đọc Việt Nam** (quy trình đã chuẩn bị sẵn trong [evaluation/human-eval-protocol.md](./evaluation/human-eval-protocol.md)). Xem đầy đủ phân tích ca thua (`TEST-05`), 3 ca bất nhất vị trí và giới hạn tại [evaluation/evaluation-report.md](./evaluation/evaluation-report.md).

---

## 4. Kiểm định & Chạy lại Đánh giá

Kiểm tra tính toàn vẹn bộ dữ liệu và chuẩn `SKILL.md`:

```bash
python evaluation/scripts/validate_datasets.py --check-skill
```

Tính lại toàn bộ thống kê từ kết quả kiểm thử thô:

```bash
python evaluation/scripts/analyze_results.py
```

Khi cập nhật Skill, luôn chạy vòng thay đổi trên [development.jsonl](./evaluation/development.jsonl), kiểm tra lại với `validate_datasets.py --check-skill`, sau đó mới chạy lại kiểm chứng mù trên [held-out-test.jsonl](./evaluation/held-out-test.jsonl).
