# Lịch sử Phiên bản (`CHANGELOG.md`)

Tài liệu ghi nhận quá trình tiến hóa của **Vietnamese Human-Readable Writing Skill** qua các vòng nghiên cứu, kiểm thử và ổn định độc lập.

---

## `v4.0` — Round 2 Stabilization & Multi-Arm Validation (Nhánh `round-2/v4-stabilization`)

**Cơ sở đối chiếu:** Tách nhánh từ bản đóng băng v3 tại commit [`cd5bba945886222d0ebd236b3c1ba92a60dd3155`](https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/commit/cd5bba945886222d0ebd236b3c1ba92a60dd3155) trên `main`.

### Thay đổi chính trên Skill (`FIX-01..FIX-05`)
- **Bảo toàn chiều sâu kỹ thuật (`FIX-02`):** Phân tách rõ 4 lớp nội dung trong `SKILL.md` (dư thừa hình thức vs giải thích cần thiết vs chi tiết kỹ thuật cốt lõi vs chi tiết bổ trợ); bắt buộc giữ đủ chiều sâu trên **từng trục** khi câu hỏi kỹ thuật yêu cầu đa khía cạnh và không gộp/lược bỏ cơ chế làm sai bản chất lưu trữ hay thứ tự xử lý.
- **Tách Trường hợp A vs Trường hợp B chống *False Clarity* (`FIX-03`):** Bổ sung quy tắc tường minh phân biệt nguồn đủ ý nhưng viết rối (**Trường hợp A**) với nguồn thiếu tác thể/điều kiện/giao thức hoặc tự mâu thuẫn (**Trường hợp B** — cấm tự điền để viết cho trôi; phải chỉ rõ điểm thiếu bằng câu hỏi mở hoặc tách giả định kèm cảnh báo). Cập nhật đồng bộ vào `vietnamese-clarity-and-style.md` và `business-specs.md`.
- **Hội thoại tự nhiên & quyền ưu tiên ràng buộc người dùng (`FIX-04`):** Gỡ giới hạn cứng *"2–6 câu / tối đa 3 gạch đầu dòng"* ở chế độ Nhẹ; hỗ trợ hội thoại nhiều lượt sâu, sắc thái hài hước/cảm xúc tự nhiên và tuân thủ ưu tiên chỉ dẫn văn phong của người dùng.
- **Progressive Disclosure linh hoạt & độc lập runtime (`FIX-05`):** Mở rộng từ đọc cứng đúng 1 file sang cơ chế linh hoạt **`0 → 1 → tối đa 2 file`** trong `references/` cho tài liệu lai (PRD kèm API, IDD kèm BR/AC); gỡ tên tool `read_file` đặc thù runtime khỏi `SKILL.md` (giảm từ `90` dòng / `10.069 bytes` xuống **`78` dòng / `9.132 bytes`**) và thêm hướng dẫn fallback khi host không có tool đọc file.

### Thay đổi về Kiểm toán, Nghiên cứu & Kiểm thử (`FIX-01, FIX-06..FIX-10`)
- **Kiểm toán & Đính chính Báo cáo v3 (`FIX-01`, `FIX-08`):** Thêm mục *Round 2 Errata* ở đầu [evaluation-report.md](./evaluation/evaluation-report.md) đính chính `TEST-21` (`A, A`), tỷ lệ 48 lượt (`A=23, B=25`), trung bình tỷ số cặp (`0,780`) vs tỷ số trung bình (`0,722`), và bỏ nhận định tuyệt đối. Giữ nguyên vẹn toàn bộ file lịch sử v3.
- **Rubric v2 & Re-audit v3 (`FIX-01`):** Ban hành [rubric-v2.md](./evaluation/rubric-v2.md) và [judge-instructions-v2.md](./evaluation/judge-instructions-v2.md), hiệu chuẩn trước trên 6 ca [judge-calibration.jsonl](./evaluation/judge-calibration.jsonl) (đạt `6/6` winner, `5/6` khớp HF chính xác), và tái chấm 24 cặp v3 lịch sử (`v3` thắng `18/24`, `Baseline` thắng `2/24`, `4` bất nhất; `v3 HF = 2/24` tại `TEST-02` & `TEST-05`, `Baseline HF = 8/24`).
- **Bộ dữ liệu chống leakage & Thực nghiệm 4 nhóm (`FIX-06`, `FIX-09`, Section 14):** Hạ cấp 24 ca v3 cũ thành Regression Suite (`v4` đạt `0/24 HF`, thắng `9` vs `8` ở cặp `v4 vs v3`, `7` bất nhất); tạo 24 ca mới [held-out-v2.jsonl](./evaluation/held-out-v2.jsonl) (gồm cả 4 ca tài liệu dài mô phỏng `simulated_real_world = true`); đối chứng 4 nhóm A (Neutral), B (Simple Prompt), C0 (`SKILL.md`-only Ablation), C (Full Skill v4).
- **Nghiên cứu đối chứng 8 repo (`FIX-07`):** Hoàn thành phân tích primary-source 8 GitHub repo công khai tại [competitive-research-report.md](./research/competitive-research-report.md).
- **Chi phí Runtime & Trigger Eval (`FIX-10`):** Đo kích thước, prompt overhead, phân bố đọc `references/` (`0/1/2` file), độ trễ từng arm và kiểm thử kích hoạt 16 truy vấn [trigger-eval.jsonl](./evaluation/trigger-eval.jsonl) (`16/16`, `F1 = 1,00`).

---

## `v3.0` — Round 1 Held-Out Frozen Baseline (`cd5bba945886222d0ebd236b3c1ba92a60dd3155`)
- Tách bạch 2 nhánh điều kiện hiển thị văn xuôi vs danh sách có cấu trúc sau bẫy `DEV-16`.
- Đóng băng `SKILL.md` 90 dòng (~1.509 từ / `10.069 bytes`) + 4 file trong `references/`.
- Kiểm thử 24 ca `held-out-test.jsonl` (8 ngữ cảnh, `flash` gen / `pro` judge, Rubric v1): `20` thắng đồng thuận, `1` thua (`TEST-05`), `3` bất nhất; tái kiểm định lại dưới Rubric v2 ở Round 2 xác định 2 ca `HF-6` ẩn (`TEST-02`, `TEST-05`).

## `v2.0` — Dev Iteration 2
- Điều chỉnh ranh giới chế độ Nhẹ và quy tắc định dạng bảng/đoạn sau phản hồi trên 16 ca `development.jsonl` (`DEV-16` mail bảo trì B2B).

## `v1.0` — Initial Research-Grounded Prototype
- Xây dựng từ báo cáo nghiên cứu Việt ngữ học + Thiết kế thông tin ([research-report.md](./research/research-report.md)) và [error-taxonomy.md](./research/error-taxonomy.md) với quy trình 3 chế độ (Nhẹ / Trung bình / Chặt) và bất biến chống bịa chi tiết (`HF-3`).
