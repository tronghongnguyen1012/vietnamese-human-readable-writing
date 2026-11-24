# Khung và Tiêu chí Đánh giá Chất lượng v2 (`rubric-v2.md`)

Tài liệu này hiệu chỉnh [rubric.md](./rubric.md) (bản lịch sử giữ nguyên cho đối chiếu v3) nhằm giải quyết các bất nhất Gate 0 phát hiện trong Round 2 Audit: phân định ranh giới khách quan giữa lỗi **Minor / Major / Critical (Hard Fail)** dựa trên **tác động thực tế lên người đọc và hệ thống**, đồng thời ngăn cả tình trạng bỏ sót lỗi kỹ thuật nguy hiểm lẫn bắt lỗi `HF-3` quá nhạy cho các cụm từ đệm vô hại.

---

## 1. Phân loại Mức độ Nghiêm trọng theo Tác động Thực tế

| Mức độ | Tác động lên người đọc & hệ thống | Ảnh hưởng tới điểm & Gate 0 |
|---|---|---|
| **Minor** | Câu chữ hơi gượng, lặp nhẹ, thiếu đồng bộ trình bày nhỏ, hoặc mất thêm chút công đọc; người đọc vẫn hiểu đúng và làm đúng. | Trừ 1 điểm ở tiêu chí liên quan (`3/4`), **KHÔNG** Hard Fail. |
| **Major** | Người đọc phải đọc lại mới hiểu, phải tự giải mã câu mơ hồ, thiếu một khía cạnh kỹ thuật/ngữ cảnh phụ làm giảm độ đầy đủ (`D2=2`), hoặc có cụm từ mục đích chung chung vô hại không có trong nguồn (`"để phục vụ tra cứu nhanh"`). Không gây hiểu sai ngược bản chất hay thiệt hại triển khai/dữ liệu. | Hạ điểm tiêu chí (`<= 2/4`), **KHÔNG** tự động Hard Fail trừ khi vi phạm Gate 0 bên dưới. |
| **Critical (Hard Fail)** | Gây hiểu sai bản chất nghiệp vụ/kỹ thuật, phá vỡ bất biến hệ thống, mất dữ kiện/điều kiện biên quan trọng, tự bịa đặt hợp đồng/số liệu/nguyên nhân kỹ thuật trọng yếu, tạo "độ rõ giả tạo" khi nguồn thiếu dữ kiện, hoặc hướng dẫn lệnh/cơ chế sai có rủi ro mất dữ liệu/phá cam kết. | Kích hoạt **Gate 0 (`HARD_FAIL`)**; trần `D1`/`D2`/`D4`/`D9` hạ về `<= 1` (`0` ở chiều vi phạm trực tiếp), **không thể bù trừ** bằng văn phong. |

**Quy tắc đối xứng bắt buộc:** Mọi lỗi được gắn `severity = "Critical"` BẮT BUỘC phải xuất hiện mã `HF-1..HF-6` tương ứng trong `hard_fails`, và ngược lại mỗi mã trong `hard_fails` BẮT BUỘC phải có ít nhất 1 lỗi `Critical` làm bằng chứng.

---

## 2. Gate 0 — Định nghĩa Chi tiết 6 Nhóm Hard Fail (`HF-1`..`HF-6`)

| Mã | Tên lỗi | Kích hoạt `HARD_FAIL` (Critical) | KHÔNG kích hoạt `HARD_FAIL` (Chỉ xét Minor/Major) |
|---|---|---|---|
| `HF-1` | **Làm sai ý nghĩa** | Đảo ngược thông điệp, quan hệ nhân–quả hoặc tự mâu thuẫn nội tại trực tiếp về dữ kiện cốt lõi (ví dụ đoạn trên nói trừ tồn kho vật lý vĩnh viễn, đoạn dưới nói chỉ giữ chỗ tạm). | Diễn đạt hơi khác từ nhưng giữ đúng nghĩa mệnh đề gốc. |
| `HF-2` | **Làm sai dữ kiện / số liệu** | Sai con số, đơn vị, mốc thời gian, tên endpoint/header/biến/trạng thái, lệnh CLI hoặc ngưỡng định lượng. | Quy đổi định dạng hiển thị tương đương không đổi giá trị (ví dụ `00:00 – 02:30` vs `00:00 đến 02:30`). |
| `HF-3` | **Bịa đặt trọng yếu / Độ rõ giả tạo** | Tự bổ sung **dữ kiện trọng yếu** như sự thật đã chốt: số liệu/SLA/tỷ lệ chưa đo, hợp đồng API/field JSON/mã lỗi, quy tắc nghiệp vụ/phạt, nguyên nhân kỹ thuật từ log chưa có trong nguồn, HOẶC tự điền **chủ thể/giao thức/điều kiện/kết quả** khi văn bản nguồn cố ý mơ hồ (*False Clarity*). *(Chỉ hợp lệ nếu gắn nhãn rõ ràng là `Ví dụ minh họa`, `Giả định cần xác nhận` hoặc `Câu hỏi mở`).* | Câu dẫn/mục đích chung chung vô hại mang tính tổ chức văn phong (ví dụ `"để phục vụ tra cứu nhanh"`, `"trân trọng thông báo"`, placeholder `[Tên người gửi]`) hoặc gợi ý hướng kiểm tra có ghi rõ là cần xác minh/ví dụ. |
| `HF-4` | **Thay đổi logic / mức bắt buộc** | Đảo `và` ↔ `hoặc`, đảo `phải` ↔ `nên`/`có thể`, đổi biên `<` ↔ `<=`, `>` ↔ `>=`, đổi logic cửa sổ thời gian hoặc điều kiện phủ định. | Tách một câu ghép đúng logic thành gạch đầu dòng dễ đọc hơn mà giữ nguyên toán tử. |
| `HF-5` | **Mất điều kiện / cảnh báo trọng yếu** | Bỏ sót phần tử trong `must_preserve`, mất ngoại lệ loại trừ, hoặc bỏ cảnh báo an toàn không thể hoàn tác / phân biệt lệnh phá hủy khi nhiệm vụ yêu cầu an toàn thao tác. | Thiếu 1 chi tiết phụ hoặc mẹo tối ưu thêm không nằm trong điều kiện bắt buộc của đề bài. |
| `HF-6` | **Đơn giản hóa sai / Khuyến nghị kỹ thuật phá hủy hoặc phản tác dụng** | (a) Rút gọn làm hiểu sai bản chất nghiệp vụ/kỹ thuật; (b) Hướng dẫn **lệnh thao tác có rủi ro phá hủy/xóa/ghi đè sai ngữ cảnh** trái với an toàn mục tiêu (ví dụ chỉ dẫn `git rm --cached` chung cho Git cũ trên file đã commit làm stage xóa file khỏi repo); (c) Đưa **khuyến nghị kỹ thuật tự mâu thuẫn phá vỡ bất biến đã cam kết** (ví dụ khẳng định đẩy message lỗi sang DLX để *"giữ thứ tự nghiêm ngặt"* trong khi `M2` cùng key vẫn chạy tiếp). | Thiếu chiều sâu phân tích ở một khía cạnh phụ (ví dụ giải thích chưa sâu cấu trúc compaction của Quorum Queue nhưng không phát biểu sai sự thật gây phá vỡ cơ chế) → chấm `Major` ở `D2`/`D3`, **không** gắn `HF-6`. |

---

## 3. Bộ 9 Tiêu chí Chấm điểm (Thang 0–4)

Giữ nguyên 9 chiều chất lượng từ [rubric.md](./rubric.md) nhưng đồng bộ hóa cách xử lý **Trường hợp B (nguồn thiếu thông tin)** và **chiều sâu kỹ thuật**:
- **`D1` Semantic Accuracy (0–4):** `4` = đúng 100% ý nghĩa, logic, cơ chế kỹ thuật và phân biệt rõ sự thật vs giả định; `3` = 1 lệch sắc thái nhỏ; `2` = có lỗi `Major` kỹ thuật hoặc mơ hồ quan hệ nhưng không gây rủi ro Critical; `0–1` = vi phạm `HF-1..HF-4` hoặc `HF-6`.
- **`D2` Completeness (0–4):** `4` = đủ 100% `must_preserve` và **đủ mọi trục/khía cạnh người dùng hỏi** (kể cả phân tích chiều sâu cho chuyên gia); `3` = thiếu 1 chi tiết phụ; `2` = bỏ sót/nén quá mỏng một khía cạnh chính của câu hỏi (`Major`, ví dụ nén trục lưu trữ trong câu hỏi so sánh lưu trữ & thứ tự); `0–1` = vi phạm `HF-5`.
- **`D3` Terminology Consistency (0–4):** Giữ thuật ngữ chuẩn đối tượng, nhất quán 1 khái niệm = 1 tên gọi (đặt backtick đúng cho định danh thật, không bọc backtick tên khái niệm giả như tham số cấu hình).
- **`D4` Semantic Clarity (0–4):**
  - *Nếu nguồn đủ dữ kiện (Trường hợp A):* Rõ tác thể, hành động, đối tượng, điều kiện.
  - *Nếu nguồn thiếu dữ kiện hoặc mâu thuẫn (Trường hợp B):* Điểm `4` dành cho bản **nhận diện và chỉ rõ thông tin thiếu/mâu thuẫn hoặc tách các cách hiểu có điều kiện**; bản tự đoán bừa để viết cho "có vẻ rõ" bị đánh `HF-3` (`D1=0`, `D4<=1`).
- **`D5` Coherence (0–4):** Trình tự thuận tiếp nhận (BLUF, cảnh báo trước thao tác, nối tiếp Cũ→Mới), liên kết xuyên suốt tài liệu dài nhiều phần.
- **`D6` Information Density (0–4):** Mật độ thông tin hữu ích tương xứng ngữ cảnh — không phạt chiều dài cần thiết cho giải thích kỹ thuật chuyên sâu hoặc hội thoại sâu nhiều lượt; phạt rào đón, lặp ý giữa bảng và chữ, sáo ngữ rỗng.
- **`D7` Naturalness (0–4):** Tiếng Việt tự nhiên, Đề–Thuyết trôi chảy, đúng sắc thái `được/bị`, không dịch sát cú pháp Anh; giữ sắc thái thân mật/hài hước nếu hội thoại tự nhiên yêu cầu.
- **`D8` Context Appropriateness (0–4):** Đúng register (vô nhân xưng cho RFC/Spec/Postmortem, tự nhiên cho chat, tôn trọng chỉ định văn phong riêng của người dùng), không áp đặt 1 giọng cho mọi ngữ cảnh.
- **`D9` Actionability (0–4 hoặc `null`):** Dùng được ngay cho công việc/kiểm thử (hoặc chỉ rõ điểm cần chốt để tránh code sai trong Trường hợp B). Đặt `null` nếu `actionability_applicable == false`.

---

## 4. Quy tắc Tổng hợp Phi bù trừ & Quyết định Cặp A/B

1. **Gate 0 ưu tiên tuyệt đối:** Bên không có `hard_fails` thắng bên có `hard_fails`. Nếu cả hai đều có `hard_fails`, bên ít lỗi `Critical` hơn thắng (hoặc `TIE` nếu mức nghiêm trọng tương đương), và ghi rõ cả hai đều **KHÔNG ĐẠT**.
2. **Ưu tiên nội dung khi cả hai qua Gate 0:** Xét nhóm Trung thực, Đầy đủ & Rõ nghĩa (`D1, D2, D4, D5`) và Khớp ngữ cảnh/Khả dụng (`D8, D9`) trước nhóm bề mặt (`D7`).
3. **Chống lạm dụng `TIE` nhưng chấp nhận `TIE` thật sự:** Chỉ chọn `TIE` khi hai bản có chất lượng thực chất tương đương (chênh lệch không rõ ràng hoặc mỗi bên mạnh ngang trọng số).
