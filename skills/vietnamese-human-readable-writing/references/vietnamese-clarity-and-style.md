# Rõ Nghĩa Ngữ Nghĩa, Biên Tập An Toàn và Chống Độ Rõ Giả Tạo (v4.1)

Dùng tài liệu này khi biên tập văn bản tiếng Việt mắc lỗi câu nặng nề, dịch sát, danh từ hóa rỗng, hoặc khi **tài liệu nguồn thiếu dữ kiện / mơ hồ / mâu thuẫn**.

---

## 1. Xử lý Trường hợp A vs Trường hợp B (Trọng tâm Làm rõ Ngữ nghĩa)

Xác định từng ý hoặc mệnh đề thuộc trường hợp nào. Một đoạn có thể chứa cả ý đã rõ lẫn thuật ngữ chưa rõ; không để phần mơ hồ làm cả đoạn trở nên cứng nhắc.

### Trường hợp A — Nguồn đủ dữ kiện nhưng diễn đạt khó hiểu
Nguồn đã cung cấp đủ tác thể, hành động, đối tượng, điều kiện và kết quả (hoặc có thể suy ra chắc chắn từ các câu xung quanh trong cùng tài liệu).
- **Cách xử lý:** Hiểu ý rồi viết lại theo cách người Việt thường diễn đạt, không bám cấu trúc nguồn. Đưa hành động ra khỏi danh từ hóa rỗng, đặt đúng Đề–Thuyết, trả lại chủ thể–đối tượng rõ ràng nếu nguồn xác định được, tách nhánh điều kiện `và/hoặc` cho đơn nghĩa.

### Trường hợp B — Bản thân nguồn thiếu thông tin hoặc tự mâu thuẫn
Nguồn thiếu tác thể thực hiện, đối tượng chịu tác động, điều kiện kích hoạt, quy tắc tính kết quả, chứa đại từ quy chiếu đa nghĩa không phân giải được từ ngữ cảnh, hoặc hai mục trong cùng tài liệu mâu thuẫn nhau.
- **Điều cấm tuyệt đối (False Clarity):** Không tự điền tên phân hệ, giao thức, ngưỡng số hay âm thầm chọn một phía để viết thành câu có vẻ rõ ràng trơn tru.
  - *Ví dụ sai:* Nguồn ghi `"Hệ thống thực hiện đồng bộ trạng thái giao dịch giữa các phân hệ liên quan nhằm đảm bảo tính nhất quán."` → Viết lại thành `"PAY gửi trạng thái thanh toán cho OMS qua webhook."` (tự bịa phân hệ, hướng truyền và giao thức).
- **4 chế độ xử lý cho Trường hợp B:**
  1. **Giữ nguyên phần chắc chắn + Gắn Gap Marker / Câu hỏi chốt:** Viết tự nhiên phần đã xác định được từ nguồn, chỉ giữ thuật ngữ chưa thể giải nghĩa ở phạm vi cần thiết. Với thông báo/email, đặt câu hỏi xác nhận có ảnh hưởng thực tế sau bản viết lại, không chen vào nội dung gửi người nhận; với đặc tả, đánh dấu đúng vị trí và đồng bộ trạng thái. Liệt kê ngắn gọn đúng các tham số còn khuyết (`Ai gửi cho ai? Khi nào kích hoạt? Giao thức gì? Lỗi xử lý ra sao?`).
  2. **Nêu các cách hiểu có điều kiện (khi có 2–3 hướng rõ ràng):** Trình bày tách bạch `Phương án hiểu 1 (nếu ...) → ...` và `Phương án hiểu 2 (nếu ...) → ...` để BA/PO/Kinh doanh chọn thay vì tự chọn ngầm.
  3. **Báo cáo trực diện mâu thuẫn:** Khi Mục A và Mục B xung đột số liệu/thời hạn/quy tắc, chỉ rõ chính xác hai câu mâu thuẫn và không tự xóa một vế.
  4. **Giữ đúng phạm vi & không hỏi vặn thừa:** Không mở rộng phân tích mọi khía cạnh chỉ vì nguồn thiếu dữ kiện; tách rõ *điểm chưa rõ ảnh hưởng trực tiếp mục đích hiện tại* vs *điểm cần chốt trước khi triển khai* vs *câu hỏi mở rộng tùy chọn*. Nếu ngữ cảnh đã có sẵn đáp án hoặc chi tiết không ảnh hưởng công việc, xử lý trực tiếp luôn.

---

## 2. Cấu trúc Đề–Thuyết, Tác thể & Chế độ Biên tập Nhẹ (Light Edit)

- **Giữ "được" và "bị" đúng sắc thái:** Dùng *"được"* cho kết quả tích cực/được duyệt; *"bị"* cho sự cố/bất lợi; loại bỏ *"được [V] bởi [Tác thể vô tri]"* kiểu dịch sát tiếng Anh.
- **Tách phạm vi phủ định `"không ... và ..."`:** Không nối thẳng vế phủ định với vế khẳng định bằng `"và"` — tách thành `, đồng thời giới hạn...` hoặc tách câu riêng.
- **Chế độ Biên tập Nhẹ (Light Edit):** Khi câu gốc đã rõ tác thể, đúng ngữ pháp, tự nhiên và đúng giọng tác giả, **không sửa chỉ để đổi từ đồng nghĩa**. Mỗi thay đổi phải nhắm vào một lỗi cụ thể (mơ hồ, danh từ hóa rỗng, lặp ý, sai quy chiếu, lệch trình tự).

### Chế độ Viết lại sâu (Deep Rewrite)

Khi văn bản khó hiểu do nhiều lớp danh từ hóa, lặp ý, dịch sát hoặc văn phong hành chính, mặc định viết lại sâu thay vì Light Edit. Không cần xin phép để thay đổi câu chữ nếu người dùng đã yêu cầu viết lại. Giữ bố cục nếu người dùng yêu cầu; nếu không, chọn bố cục phù hợp với mục đích đọc.

- Đọc hết đoạn để hiểu sự kiện, điều kiện, tác động và ngoại lệ trước khi viết. Không thay từng cụm từ một cách cơ học.
- Viết từ ý đã hiểu, ưu tiên động từ cụ thể, câu thuận tai, từ thông dụng đúng nghĩa. Chia câu khi nhiều điều kiện làm người đọc mất mạch; không ép mọi câu ngắn hoặc mọi đoạn thành danh sách.
- Giữ thuật ngữ chuẩn ngành hoặc cụm chưa thể giải nghĩa chính xác. Thay được từ khó bằng từ dễ mà không mất nghĩa thì thay ngay; không giữ từ chỉ vì có trong nguồn.
- Sau khi viết, đọc độc lập như người nhận rồi đối chiếu ngược từng ý. Nếu bản mới chỉ dễ nhìn hơn nhờ tiêu đề/bullet nhưng câu chữ vẫn khó hiểu, viết lại tiếp. Nếu câu trôi chảy nhưng đổi hành vi hoặc điều kiện, sửa về đúng nghĩa.

### Ví dụ đối chiếu

**Nguồn:** Khi hệ thống tiến hành đối soát định kỳ, trong trường hợp các thiết lập liên quan đến phương thức thanh toán liên kết chưa đạt trạng thái đồng bộ hóa đầy đủ, quá trình kích hoạt lại quyền truy cập có thể ghi nhận sự gián đoạn cục bộ hoặc phát sinh trạng thái tạm treo đối với một số tính năng nâng cao cho đến khi các điều kiện tiên quyết được hoàn tất xác minh lại.

**Chưa đạt — chỉ dọn câu chữ:** Nếu thiết lập phương thức thanh toán liên kết chưa đồng bộ đầy đủ khi đối soát, việc kích hoạt lại quyền truy cập có thể bị gián đoạn cục bộ hoặc tính năng nâng cao bị tạm treo cho đến khi xác minh lại điều kiện tiên quyết.

**Sai nghĩa — quá mạnh tay:** Nếu thanh toán thất bại, gói dịch vụ sẽ không được gia hạn.

**Đạt:** Khi hệ thống đối soát định kỳ, nếu thiết lập phương thức thanh toán đã liên kết chưa được đồng bộ đầy đủ, việc khôi phục quyền truy cập có thể bị gián đoạn hoặc một số tính năng nâng cao có thể tạm thời không sử dụng được. Tình trạng này có thể kéo dài cho đến khi các điều kiện cần thiết được xác minh lại.

**Lý do:** Bản đạt bảo toàn khả năng xảy ra, hai hệ quả, điều kiện và thời điểm xác minh lại; không biến đồng bộ thanh toán thành thanh toán thất bại hoặc khôi phục quyền truy cập thành gia hạn. Phạm vi gián đoạn cụ thể vẫn chưa rõ, không tự khẳng định toàn bộ dịch vụ bị khóa. Nếu cần phát hành thông báo, hỏi riêng về các điều kiện và phạm vi ảnh hưởng.

### Bảng Chữa nhanh Các Mẫu Câu Phổ biến

| Mẫu lỗi hay gặp | Hướng sửa trực tiếp |
|---|---|
| `Phân hệ X cung cấp năng lực xử lý việc Y nhằm đáp ứng Z` | `Phân hệ X xử lý [hành động Y] để đáp ứng [mục tiêu Z].` |
| `Hỗ trợ phân bổ giá trị thanh toán bằng tối đa 3 phương thức cho một đơn hàng đơn lẻ, trừ đơn dưới mức sàn` | `Cho phép thanh toán một đơn hàng bằng tối đa 3 phương thức; không áp dụng cho đơn dưới mức sàn.` |
| `Lỗi được gây ra bởi token đã bị hết hạn một cách bất ngờ` | `Lỗi xảy ra do token hết hạn đột ngột.` |
| `Các webhook sẽ tạm hoãn.` *(nguồn thiếu bối cảnh)* | `Hệ thống tạm hoãn gửi webhook *(chưa rõ thời điểm, nguyên nhân và việc có tự gửi lại hay không — cần xác nhận)*.` |

---

## 3. Quy trình 3 Lượt khi Biên tập Tài liệu Dài Có sẵn

1. **Lượt 1 — Trích khóa bất biến:** Ghi nhận mọi con số, đơn vị, mốc thời gian, thuật ngữ chuẩn (`Sev1, P1, SLA...`), vai trò, điều kiện và kiểm tra xem có chỗ nào thiếu/mâu thuẫn (Trường hợp B) không.
2. **Lượt 2 — Viết lại theo ý & tổ chức cấu trúc:** Chọn Light Edit hoặc Deep Rewrite theo độ khó và yêu cầu, không mặc định sửa ít. Đưa trọng tâm/cảnh báo lên trước; giữ nhất quán thuật ngữ từ Phần 1 đến Phần cuối; với đoạn mô tả thuần túy 2–4 câu chỉ có 1–2 điều kiện đơn giản thì giữ văn xuôi liền mạch, còn email thông báo vận hành hoặc quy định ≥ 3 mốc điều kiện thì tách danh sách/bảng quét nhanh.
3. **Lượt 3 — Đối chiếu ngược:** Kiểm tra không rơi mốc giờ, dấu `< / <=`, phủ định, ngoại lệ, URL/code/số liệu, không thu hẹp đại từ thay thế và không biến quan hệ mục đích thành điều kiện địa điểm ngoài nguồn.
