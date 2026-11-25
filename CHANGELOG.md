# Lịch sử Phiên bản (`CHANGELOG.md`)

Tài liệu ghi nhận quá trình tiến hóa của **Vietnamese Human-Readable Writing Skill** qua các vòng nghiên cứu, kiểm thử và ổn định độc lập.

---

## `v4.2-rc` — Communication-First Refinement on `v4.1` Core (Nhánh `release/v4.2-rc`, từ `main` `a63c39ce`)

Bản tích hợp có chọn lọc các cải tiến đã chứng minh hiệu quả từ hai nhánh thực nghiệm **Semantic Reconstruction** ([`275ce12b`](https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/commit/275ce12b03ca40299a65eb13166407dd893dd96c)) và **V5 Communication-First** ([`3f1c3d5c`](https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/commit/3f1c3d5c95f6290bc4c9fdb47450db1825589389)) trực tiếp trên nền `SKILL.md` v4.1 (không sử dụng nguyên mẫu tối giản V5-A/V5-B làm bản phát hành chính thức nhằm giữ trọn chiều sâu và độ linh hoạt ngữ cảnh của v4.1):

- **Tích hợp Semantic Reconstruction vào quy trình lõi (`SKILL.md` Mục 2.1, Mục 4.1 & 4.3):** Yêu cầu hiểu trọn vẹn thông điệp và tái tổ chức theo nhu cầu tiếp nhận của người đọc thay vì sửa từng câu trên khung văn bản gốc. *Bằng chứng:* Trong Human Evaluation vòng SR (`SR-03, SR-04, SR-07`), `Group C` (v4.1 + SR) được ưu tiên ở cả `3/3` ca so với `Group B` dài dòng.
- **Tách rạch ròi 5 chế độ tác vụ & cách xử lý nguồn thiếu dữ kiện (`SKILL.md` Mục 1 & Mục 2.2):** Phân biệt *Hội thoại tự nhiên*, *Viết thành phẩm cho người đọc cuối*, *Đặc tả để triển khai*, *Review & phân tích* và *Giải thích kiến thức/kỹ thuật*. Chặn thói quen tự động gắn khối `"Điểm bản gốc chưa nêu cụ thể"` vào thông báo/email/SOP cho người đọc cuối (từng xảy ra ở `Group B` trên `SR-01`, `SR-02`, `SR-03`, `SR-07`), nhưng giữ chặt câu hỏi `[Chưa chốt]` ở đặc tả triển khai (`SR-05`, `V5-05`) và không che giấu lỗ hổng gây rủi ro vận hành.
- **Trình tự truyền đạt linh hoạt không ép ngắn (`SKILL.md` Mục 1 & Mục 4.2):** Bỏ một khuôn sắp xếp cứng duy nhất; cho phép mở bằng quyết định/tác động (email/quyết định), bằng vấn đề thực tế (giải thích lý do cần cơ chế), bằng phân biệt bản chất trước tình huống (so sánh cơ chế), hoặc bối cảnh–điều kiện–trình tự (hướng dẫn vận hành). *Bằng chứng:* Trong Human Evaluation vòng V5 (`V5-01..V5-06`), `v4.1` (kích hoạt dưới nhãn `Group A`) được ưu tiên ở `V5-01`, `V5-03`, `V5-04`, ngang bằng ở `V5-05`, trong khi `Group C` thắng ở `V5-02`, `V5-06` — cho thấy nền v4.1 vẫn có lợi thế về độ dày thông tin và trình tự giải thích.
- **Khóa chặt bảo toàn ngữ nghĩa & phân biệt thuật ngữ thật vs từ hành chính (`SKILL.md` Mục 2.3–2.4 & Mục 4.4):** Bổ sung kiểm tra tường minh `có thể` vs `sẽ` (từ lỗi `SR-01 B_prior`), `phải` vs `nên`, chống thu hẹp/mở rộng phạm vi ngoài nguồn (từ các lỗi `Minor` ở `SR-07 C`, `V5-03 C`, `V5-06 C`), cấm trình bày định danh/trạng thái/kiến trúc tự đề xuất như thiết kế đã chốt, và phân biệt thuật ngữ nghiệp vụ chính xác (như `"đối soát"` trong tài chính) với chữ hành chính sáo rỗng.
- **Giữ hệ thống `references/` & chỉnh sửa xung đột tối thiểu (`vietnamese-clarity-and-style.md`):** Chỉ hiệu đính quy tắc Trường hợp B cho thành phẩm cuối và bổ sung ví dụ tái cấu trúc theo nghĩa ở mục Light Edit; giữ nguyên `business-specs.md`, `technical-specs.md` và `information-architecture.md`.

---

## `v4.1` — Targeted Stabilization Patch (Nhánh `round-2/v4-stabilization`, từ `cf5f4e9`)

Bản vá tập trung giải quyết 6 nhóm lỗi/bất nhất phát hiện sau Round 2 trước khi đưa Skill vào thử nghiệm sử dụng thực tế, giữ nguyên kiến trúc lõi v4 (`validate_datasets.py --check-skill` PASS, `82` dòng / `8.904 bytes`):

- **Audit toàn bộ ví dụ trong Skill & `references/`:** Sửa 4 dòng ví dụ trước/sau trong bảng của `vietnamese-clarity-and-style.md` (đặc biệt sửa `"Các webhook sẽ tạm hoãn"` từ câu viết lại tự bịa *"trong lúc bảo trì và gửi lại sau khi hoàn tất"* sang diễn đạt giữ nguyên độ bất định cần xác nhận); gỡ các nhãn đánh dấu nội bộ (`FIX-*`, `HF-3`, `R-04`).
- **Final Semantic & Consistency Check:** Thêm bước rà soát 6 điểm ở cuối `SKILL.md` Mục 4 cho tác vụ chuyên môn phức tạp / tài liệu nhiều phần (chủ đích **bỏ qua** cho hội thoại thường).
- **Preserve Confirmation Status Across Documents (`H2-19`):** Bổ sung ràng buộc đồng bộ trạng thái *"chưa chốt / trung tính"* giữa văn xuôi, Business Rule, AC, bảng trách nhiệm, sơ đồ Sequence/Flowchart, API contract, chuyển trạng thái và Open Questions trong `SKILL.md`, `business-specs.md`, `technical-specs.md`.
- **Scope & Proportion (`H2-12`):** Tách 3 mức khi nguồn thiếu dữ kiện (*ảnh hưởng trực tiếp mục đích* vs *cần chốt trước triển khai* vs *mở rộng tùy chọn*); chống lặp nội dung giữa phân tích–bảng–ví dụ–kết luận; không tối ưu số từ cứng.
- **Technical Claim Verification (`H2-06`):** Thu gọn hướng dẫn Git/RabbitMQ chi tiết thành quy tắc kiểm chứng khẳng định có rủi ro dữ liệu/vận hành (ưu tiên kiểm tra mã nguồn/tài liệu hãng/công cụ nếu có; tách dữ kiện đã kiểm chứng vs giả định; không khẳng định chắc chắn quá mức khi chưa xác minh), tránh biến Writing Skill thành kho kiến thức công nghệ.
- **Evaluation Correction & Kiểm thử Hồi quy Tập trung (`n = 9`):** Ban hành [standalone-hf-protocol.md](./evaluation/standalone-hf-protocol.md) (Gate 0 độc lập 1 output/lượt + phân loại HF 3 mức *Judge-Detected / Verified / Judge-Disagreed*); tách rạch ròi bảng so sánh tập `n = 12` trùng khớp khỏi `n = 24`; ghi rõ token là ước lượng heuristic; kiểm thử hồi quy tập trung trên 9 ca đã biết cho `0/9` HF (cả Standalone lẫn Blind A/B `v4.1 vs v4`, thắng `4` vs `3`, `2` bất nhất, khắc phục toàn bộ `H2-06, H2-12, H2-19`). Xem [v4.1-stabilization-report.md](./evaluation/v4.1-stabilization-report.md).

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
