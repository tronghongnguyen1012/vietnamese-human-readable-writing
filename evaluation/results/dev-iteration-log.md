# Nhật ký Lặp Phát triển Skill trên Tập Dev (`RED → GREEN → REFACTOR`)

Tài liệu này ghi nhận trung thực toàn bộ quá trình kiểm định và tinh chỉnh `SKILL.md` cùng các tệp tham chiếu trên **16 ca phát triển** (`evaluation/development.jsonl`), sử dụng cùng một mức mô hình sinh đầu ra (`flash`) và giám khảo mù độc lập (`pro`). Các ca kiểm thử độc lập (`evaluation/held-out-test.jsonl`) không được đọc hay dùng để tinh chỉnh trong suốt quá trình này.

---

## 1. Pha RED — Baseline (Không có Skill)

- **Agent:** `eval-baseline` (`flash`), không có hướng dẫn Skill.
- **Tệp dữ liệu thô:** `evaluation/results/dev-baseline-raw.jsonl`
- **Vấn đề thực tế quan sát được từ đầu ra Baseline:**
  1. **Tự bịa thông số/quy tắc chưa có căn cứ (`HF-3` — 7/16 ca bị Blind Judge gắn Hard Fail khi chấm đối chứng):** Đặc biệt nặng ở đặc tả kỹ thuật (`DEV-11` 1.341 từ — tự thêm header `Authorization`, schema JSON 8 trường, các mã HTTP `400/401/404`, quy tắc trim chuỗi client; `DEV-12` — tự thêm API `POST /orders`, `FOR UPDATE SKIP LOCKED`, trạng thái `PENDING/SENT`; `DEV-13` Runbook — tự thêm mốc đếm giờ và tên biến; `DEV-10` — tự thêm quy tắc không gia hạn khóa và giải thích sai cửa sổ trượt thành `HF-4`; `DEV-14` — tự khẳng định quy tắc hoàn tiền/tồn kho dẫn tới `HF-3` và `HF-6`; `DEV-07`, `DEV-08` — tự thêm cam kết ngoài input).
  2. **Lạm dụng tiêu đề và mở rộng quá phạm vi ở hội thoại ngắn (`D-04`, `R-01`):** `DEV-01` (hỏi nhanh `useEffect` chạy 2 lần lúc dev) bị Baseline kéo thành bài hướng dẫn 326 từ với nhiều `### Heading`, gạch ngang `---`, 2 đoạn code dài và khuyến nghị thư viện ngoài câu hỏi.
  3. **Rào đón, lặp ý và sáo ngữ (`P-01`, `P-04`, `S-01`):** `DEV-08` mở bài hành chính dài, `DEV-16` giữ lời dẫn sáo rỗng, `DEV-15` vẫn giữ *"đáp ứng các nghiệp vụ tại điểm bán"*.

---

## 2. Pha GREEN — Skill v1 (`eval-experiment`)

- **Thiết kế v1:** `SKILL.md` (89 dòng, 1.438 từ) với Context Triage 3 chế độ (`Nhẹ / Trung bình / Chặt`), 4 bất biến bảo toàn nội dung (tách rạch `Đề xuất bổ sung (cần xác nhận)` / `Ví dụ minh họa`), quy trình 9 bước, ranh giới chống máy móc và bảng điều hướng tới 4 tệp trong `references/`.
- **Kết quả Blind Judge (`dev-v1-judge.jsonl`):**
  - **Thắng / Thua / Hòa:** **15 thắng / 1 thua (`DEV-15`) / 0 hòa**.
  - **Hard Fail:** Baseline có **7/16 ca** (`DEV-07, 08, 10, 11, 12, 13, 14`), **Skill v1 có 0/16 ca**.
  - **Progressive Disclosure thực tế:** `DEV-01, 02, 03, 07` chạy với `refs=[]`; `DEV-01` giảm từ 326 xuống 109 từ; `DEV-11` giảm từ 1.341 xuống 613 từ; `DEV-13` giảm từ 534 xuống 302 từ.
- **Chẩn đoán lỗi còn sót ở v1:**
  - `DEV-15` (thua): v1 tách một đoạn văn mô tả 2 giới hạn thành câu dẫn đệm + 2 gạch đầu dòng in đậm lặp lại nhãn (`P-04`, `D-04`), ẩn chủ thể ở gạch đầu dòng (`S-02`), và sót các vỏ dịch sát (*"các kịch bản nghiệp vụ"*, *"dưới mức sàn"*, *"mỗi đơn hàng đơn lẻ"*).
  - Các lỗi nhỏ ở các ca thắng: lặp nội dung giữa bảng và phần chữ (`DEV-14`), trộn bảng và bullet trong phần AC (`DEV-10`), đính kèm ghi chú tiền phát hành vào cuối Runbook (`DEV-13`), cụm `"Các webhook sẽ tạm hoãn"` hơi cứng (`DEV-16`).

---

## 3. Pha REFACTOR 1 — Skill v2 (`eval-experiment-v2`)

- **Thay đổi v1 → v2:**
  - Thêm vào `SKILL.md` và `vietnamese-clarity-and-style.md` quy tắc giữ văn xuôi cho *"đoạn biên tập ngắn (2–4 câu, tối đa 2–3 điều kiện đơn giản)"*, cấm lặp nhãn in đậm, và bổ sung mẫu sửa cho *"các kịch bản nghiệp vụ / mức sàn / đơn lẻ / Các webhook sẽ tạm hoãn"*.
  - Bổ sung quy tắc chống lặp bảng–chữ (`information-architecture.md`), đồng nhất định dạng AC (`business-specs.md`) và giữ Runbook thuần túy cho người trực (`technical-specs.md`).
- **Kết quả Blind Judge (`dev-v2-judge.jsonl`):**
  - **Thắng / Thua / Hòa:** **12 thắng / 3 thua (`DEV-03, DEV-15, DEV-16`) / 1 hòa (`DEV-05`)**.
  - **Hard Fail:** Baseline có 7/16 ca (hoặc tương đương), **Skill v2 vẫn đạt 0/16 ca**.
- **Phát hiện thoái lui quan trọng:**
  - `DEV-16` bị **thoái lui từ Thắng (v1) → Thua (v2)** do quy tắc giữ văn xuôi cho *"đoạn biên tập ngắn"* viết quá rộng, làm v2 gộp toàn bộ email thông báo bảo trì B2B thành đoạn văn xuôi dày khó quét nhanh!
  - `DEV-15` vẫn thua sát vì v2 tạo ra lỗi mơ hồ phạm vi phủ định `"không hỗ trợ ... và giới hạn tối đa 3 phương thức"` (`S-03`) và chuyển mục đích *"tại điểm bán"* thành khung địa điểm đầu câu.
  - `DEV-03` thua do 1 lỗi nhầm kỹ thuật ngẫu nhiên của mô hình sinh (*"độ trễ tối thiểu bằng chu kỳ hỏi"* thay vì *tối đa*).

---

## 4. Pha REFACTOR 2 — Skill v3 (`eval-experiment-v3`, Phiên bản Đóng băng)

- **Thay đổi v2 → v3:**
  - Hẹp hóa điều kiện định dạng trong `SKILL.md` (90 dòng, 1.509 từ): tách rõ thành 2 điều kiện quan sát được — giữ văn xuôi cho *hội thoại chat ngắn hoặc đoạn văn mô tả 1–2 ý đơn giản*, còn *email thông báo vận hành hoặc quy tắc nhiều điều kiện* tách dòng ngắn để quét nhanh.
  - Bổ sung vào `vietnamese-clarity-and-style.md` quy tắc tách vế phủ định `"không ... và ..."` (chống tràn phạm vi chữ *không*) và nguyên tắc Lượt 3 không thu hẹp đại từ thay thế hoặc đổi quan hệ mục đích thành địa điểm.
- **Kết quả Blind Judge (`dev-v3-judge.jsonl`):**
  - **Thắng / Thua / Hòa:** **13 thắng / 2 thua (`DEV-04`, `DEV-15`) / 1 hòa (`DEV-01`)**.
  - **Hard Fail:** **0/16 ca** trên Skill v3.
  - **Kiểm chứng phục hồi:** `DEV-16` trở lại **Thắng** (cấu trúc email quét nhanh sạch sẽ, giữ nguyên phạm vi webhook). `DEV-13` rút còn 172 từ (so với 534 từ Baseline) và **Thắng**; `DEV-14` rút còn 475 từ (so với 842 từ Baseline) và **Thắng**; `DEV-03` trở lại **Thắng**.
  - **Phân tích 2 ca thua & 1 ca hòa ở v3:**
    - `DEV-01` (Hòa): Skill giữ đúng phong cách `casual_chat` gọn nhẹ (136 vs 326 từ, `refs=[]`), nhưng bị trừ điểm D1 do rút gọn chuỗi chu trình bỏ chữ `unmount` rõ ràng ở một câu so với Baseline.
    - `DEV-04` (Thua): Cả hai đều 0 Hard Fail và chuyên sâu ngang tầm kỹ sư 5 năm, nhưng ở lượt này Experiment v3 nhầm chi tiết nội bộ `FOR UPDATE` ghi vào Lock Manager khi không tranh chấp và bỏ qua phần Write Skew/Anchor Lock so với Baseline.
    - `DEV-15` (Thua): Skill v3 đã hết lỗi tách bullet thừa và hết lỗi phạm vi `không... và...`, nhưng vẫn còn nhẹ cụm `"cho phép xử lý... nhằm đáp ứng... thấp hơn... riêng lẻ"` so với bản Baseline rất súc tích (`"xử lý... dưới... mỗi đơn hàng"`).

---

## 5. Quyết định Chốt Kiểm thử Độc lập

Với tỷ lệ **13/16 thắng**, **0/16 Hard Fail** (giảm tuyệt đối so với 7/16 ca dính Hard Fail ở Baseline), khắc phục thành công thoái lui bố cục ở `DEV-16` và giữ `casual_chat` / `workplace_communication` gọn gàng (`DEV-01` 136w, `DEV-02` 111w, `DEV-07` 65w), **Skill v3 chính thức được đóng băng** để đưa vào kiểm thử độc lập trên 24 ca `held-out-test.jsonl`.
