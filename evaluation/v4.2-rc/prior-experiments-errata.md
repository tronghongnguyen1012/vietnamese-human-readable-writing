# Đính chính Metadata Kích hoạt & Đọc `references/` ở Các Thí nghiệm Trước (`Errata`)

Tài liệu này **không ghi đè dữ liệu thô lịch sử** trên các nhánh `experiment/semantic-reconstruction` (`275ce12b`) hay `experiment/v5-communication-first` (`3f1c3d5c`), mà ghi nhận kết quả **đối soát trực tiếp trên `transcript_full.jsonl` gốc** của từng subagent đã lưu trong runtime Antigravity.

---

## 1. Đính chính cho `experiment/semantic-reconstruction` (`275ce12b`)

### Sai sót đã phát hiện trong báo cáo gốc
Trong [analysis-report.md](https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/blob/experiment/semantic-reconstruction/experiments/semantic-reconstruction/analysis-report.md) (trên nhánh `experiment/semantic-reconstruction`), `raw-outputs.jsonl` ghi nhận `"refs_read": []` cho toàn bộ `30/30` lượt chạy Gemini (`Group A, B, C`), dẫn tới hai nhận định không chính xác về telemetry:
1. Coi `Group A` là *"Gemini mặc định, không cài Skill"*.
2. Kết luận `20/20` lượt `Group B` và `Group C` *"không một lượt nào chủ động gọi đọc file trong `references/`"*.

### Sự thật xác minh trực tiếp từ `transcript_full.jsonl` (`30/30` runs)
Nguyên nhân sai lệch kỹ thuật là script thu thập ban đầu chỉ đọc khóa `tc.get("arguments")` trong khi log runtime của Antigravity lưu tham số tool call dưới khóa `tc.get("args")`. Khi trích xuất lại trực tiếp trường `args["Path"]` của tất cả lệnh `read_file` trong 30 file `transcript_full.jsonl` tương ứng với các `subagent_id` lưu trong `raw-outputs.jsonl`:

| Nhánh | Số lượt gọi `read_file` / Tổng lượt | Tệp thực tế đã nạp (`actual_reads`) | Hệ quả phương pháp |
|---|---:|---|---|
| **Group A** | **10 / 10** (`100%`) | `10/10` lượt tự gọi `read_file` đọc `SKILL.md` (`v4.1` cài global tại `~/.gemini/config/skills/...`) qua `<skills>` auto-discovery; `9/10` lượt đọc thêm `references/*.md` (trừ `SR-03 run1` chỉ đọc `SKILL.md`). | **Group A trong vòng SR không phải Gemini thuần không có Skill**, mà là *Gemini + kích hoạt tự nhiên `v4.1`*. |
| **Group B** (`v4.1` injected) | **9 / 10** (`90%`) | `9/10` lượt gọi `read_file` đọc `references/*.md` (`vietnamese-clarity-and-style.md`, `business-specs.md`, `technical-specs.md`, `information-architecture.md`); chỉ `SR-03 B run1` không mở reference. | `SKILL.md` v4.1 đã kích hoạt progressive disclosure đọc `references/` ở `90%` tác vụ. |
| **Group C** (`v4.1 + SR` injected) | **9 / 10** (`90%`) | `9/10` lượt gọi `read_file` đọc `references/*.md`; chỉ `SR-03 C run1` không mở reference. | `Group C` cũng đọc `references/` ở `90%` tác vụ, đúng theo cấu trúc đa tệp của `v4.1`. |

### Kết luận nào vẫn giữ giá trị, kết luận nào cần rút lại?
- **Vẫn giữ giá trị:** Chênh lệch quan sát được giữa `Group C` vs `Group B` (tách cấu trúc tốt hơn, không chèn thừa câu dẫn giáo khoa ở `SR-04`, cô đọng ở `SR-07`), cũng như nhận xét đối chiếu văn phong giữa các bản Gemini và bản `Group D (GPT-6.2 Instant)` trên `SR-01`.
- **Cần rút lại / đính chính:** Không được diễn giải `Group A` trong vòng SR là "Gemini không có ViWrite", và không được tuyên bố `v4.1` không kích hoạt `references/` (thực tế đã kích hoạt `9/10` lượt).

---

## 2. Xác nhận lại cho `experiment/v5-communication-first` (`3f1c3d5c`)

Trong `metrics-v5.json` và `v5-experiment-report.md` của nhánh `experiment/v5-communication-first`:
- **Đã phát hiện và công bố minh bạch ngay trong báo cáo:** `Group A` tự kích hoạt `SKILL.md` v4.1 ở **`13/13` lượt chạy** (và đọc thêm `references/` ở `8/13` lượt), do cùng cơ chế `<skills>` auto-discovery của Antigravity.
- **Tỷ lệ đọc `references/` xác minh chuẩn (`args.Path`):** `B = 9/13`, `C = 10/13`, `E (V5-A) = 3/13`, `F (V5-B) = 3/13`.
- **Ý nghĩa cho `v4.2-rc`:** Chính sự cố "rò rỉ skill global vào nhánh Baseline" ở hai vòng trước là lý do vòng kiểm thử `v4.2-rc` bắt buộc phải thực hiện **Native Activation Smoke Test có log đường dẫn tuyệt đối** và ghi rõ giới hạn nếu môi trường vẫn còn bản global `v4.1` chưa tháo bỏ.
