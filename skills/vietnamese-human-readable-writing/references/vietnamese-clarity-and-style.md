# Rõ Nghĩa Ngữ Nghĩa, Văn Phong Tiếng Việt Tự Nhiên và Biên Tập An Toàn

Dùng tài liệu này khi viết hoặc biên tập lại văn bản tiếng Việt mắc lỗi câu nặng nề, dịch sát tiếng Anh, danh từ hóa rỗng hoặc mơ hồ logic.

---

## 1. Cấu trúc Đề–Thuyết & Tác thể–Hành động

Trong tiếng Việt tự nhiên, mỗi câu nên đặt rõ **Đề** (phạm vi ngữ cảnh, điều kiện, hoặc đối tượng đang bàn) trước **Thuyết** (hành động hoặc trạng thái mới về đối tượng đó), rồi lấy thông tin mới ở câu trước làm Đề cho câu sau.

- **Đưa hành động ra khỏi danh từ hóa rỗng:** Khi thấy chuỗi `động từ hình thức + việc/sự/quá trình/năng lực + [Động từ thật]`, lôi động từ thật ra làm vị ngữ chính và trả lại đúng tác thể/đối tượng cụ thể.
- **Giữ "được" và "bị" đúng sắc thái:**
  - Dùng *"được"* cho kết quả có lợi hoặc sự chấp thuận tự nhiên (*"Hồ sơ đã được duyệt"*).
  - Dùng *"bị"* cho kết quả bất lợi/sự cố (*"Giao dịch bị timeout"*).
  - Loại bỏ *"được [V] bởi [Tác thể]"* cho chủ thể kỹ thuật vô tri → đổi thành câu chủ động (*"Worker gửi sự kiện..."*) hoặc câu Đề–Thuyết (*"Với đơn dưới 100.000đ, hệ thống không cho tách..."*).

### Bảng Chữa nhanh Các Mẫu Câu Phổ biến

| Mẫu lỗi hay gặp | Hướng sửa trực tiếp | Vì sao dễ hiểu hơn |
|---|---|---|
| `Phân hệ X cung cấp năng lực xử lý việc Y nhằm đáp ứng Z` | `Khi [tình huống Z], [đối tượng] có thể [hành động Y]...` | Hiện rõ tác thể, đối tượng và hành động thật thay vì 3 lớp danh ngữ rỗng. |
| `hỗ trợ phân bổ giá trị thanh toán... cho các kịch bản nghiệp vụ... dưới mức sàn... mỗi đơn hàng đơn lẻ` | `cho phép chia thành nhiều lần thanh toán khi bán tại quầy... không áp dụng cho đơn dưới [X]... tối đa 3 phương thức mỗi đơn.` | Gỡ sạch vỏ danh từ dịch sát (`phân bổ giá trị`, `kịch bản nghiệp vụ`, `mức sàn`, `đơn lẻ`), giữ tác thể chủ động xuyên suốt. |
| `Các webhook sẽ tạm hoãn` | `Hệ thống tạm hoãn gửi webhook trong lúc bảo trì và sẽ gửi lại sau khi hoàn tất.` | Trả lại chủ thể thực hiện (`Hệ thống`) thay vì để sự kiện tự hành động gượng ngữ pháp. |
| `Lỗi này được gây ra bởi token đã bị hết hạn một cách bất ngờ` | `Lỗi xảy ra vì token hết hạn giữa chừng.` | Bỏ ghép sai sắc thái `"được gây ra"`, bỏ phó từ dịch sát `"một cách bất ngờ"`. |
| `Việc áp dụng cơ chế này không được hỗ trợ đối với các đơn có giá trị nhỏ hơn mức sàn...` | `Không áp dụng cơ chế này cho đơn dưới [X]...` | Cắt danh từ đệm `"Việc áp dụng"`, đặt thẳng đối tượng loại trừ. |
| `Trong một cửa sổ thời gian là 3 phút` / `bị trì hoãn bởi khoảng thời gian ổn định` | `duy trì liên tục trong 3 phút` / `chờ hết stabilization window 5 phút trước khi scale-in` | Thay cụm dịch sát từng chữ tiếng Anh bằng cách nói tự nhiên hoặc giữ đúng tên tham số kỹ thuật. |
| `Tối ưu hóa trải nghiệm người dùng một cách toàn diện / vượt trội` | Thay bằng tác động thực tế đã có trong dữ liệu (hoặc bỏ nếu không có dữ kiện) | Loại bỏ sáo ngữ không mang thông tin (`S-05`). |

---

## 2. Xử lý 4 Loại Mơ hồ Ngữ nghĩa Nguy hiểm

1. **Mơ hồ phạm vi logic (`và`, `hoặc`, `không`, `ngoại trừ`):**
   - *Không đạt (`và/hoặc`):* `Không cho hủy đơn đối với tài khoản chưa xác thực hoặc đơn đã đóng gói và giao vận chuyển.`
   - *Sửa:* Chia nhánh đánh số: `Từ chối hủy đơn nếu rơi vào một trong hai trường hợp: (1) Tài khoản chưa xác thực; (2) Đơn đã đóng gói VÀ đã giao cho đơn vị vận chuyển.`
   - *Không đạt (`không ... và ...`):* `Không hỗ trợ tách thanh toán cho đơn dưới 100.000đ và giới hạn tối đa 3 phương thức.` (dễ hiểu nhầm chữ *không* bao trùm cả vế *giới hạn*).
   - *Sửa:* Tách rõ bằng dấu phẩy + từ chuyển hoặc tách câu: `...không áp dụng cơ chế này cho đơn dưới 100.000đ, đồng thời giới hạn mỗi đơn chỉ dùng tối đa 3 phương thức thanh toán.`
2. **Mơ hồ quy chiếu (`nó`, `điều này`, `việc đó`):**
   - Sau một câu có từ 2 mệnh đề hoặc 2 thực thể trở lên, **không** mở câu sau bằng *"Điều này giúp..."* hay *"Nó sẽ..."*; lặp lại đúng danh từ cụ thể (*"Cơ chế giữ chỗ 15 phút này giúp..."*).
3. **Ẩn tác thể thực thi:**
   - Trong quy trình nhiều bên (Khách hàng, POS, Cổng thanh toán, CSKH), mỗi hành động phải gắn rõ chủ thể (*"Thu ngân bấm..."*, *"Hệ thống POS gửi..."*).
4. **Mơ hồ biên độ và mốc thời gian:**
   - Khi nguồn ghi rõ con số, đơn vị, mốc giờ (`<= 15 phút`, `tối đa thêm 10 ngày làm việc`, `ngày 1–28`), giữ nguyên ký hiệu/cụm phân định chính xác. Cẩn thận phân biệt **"thêm X ngày"** (cộng dồn) với **"tối đa X ngày"** (tổng trần).

---

## 3. Quy trình 3 Lượt khi Biên tập / Viết lại Văn bản Có sẵn

1. **Lượt 1 — Trích khóa bất biến:** Gạch ra mọi con số, đơn vị, mốc ngày/giờ, thuật ngữ bắt buộc, điều kiện áp dụng và ngoại lệ từ văn bản gốc.
2. **Lượt 2 — Dọn cấu trúc & câu chữ:**
   - Nếu ý chính bị chôn sau lời chào/mở bài sáo rỗng → đưa thông báo/quyết định chính, mốc thời gian và hành động người đọc cần làm lên đầu.
   - Gỡ danh từ hóa nhiều lớp, bị động `"được... bởi"`, từ nối giả (`Tuy nhiên, Hơn nữa, Do đó` khi ý không đối lập/nhân quả) và câu lặp ý.
   - **Chọn khung giữ nguyên hay tách nhánh:** Với đoạn văn mô tả thuần túy chỉ có 2–4 câu và 1–2 điều kiện đơn giản (không phải email thông báo vận hành, hướng dẫn hay chuỗi `và/hoặc` lồng nhau), giữ dưới dạng **văn xuôi chủ động liền mạch** — tránh tách câu dẫn đệm + gạch đầu dòng lặp nhãn in đậm. Với email thông báo sự cố/bảo trì hoặc văn bản có ≥ 3 mốc điều kiện/thời hạn, tách dòng/danh sách rõ mục Thời gian, Tác động và Hành động để người đọc quét nhanh.
3. **Lượt 3 — Đối chiếu ngược với Lượt 1:** Kiểm tra từng con số, từng từ phủ định, từng ngoại lệ và quan hệ mục đích/phạm vi đã trích ở Lượt 1; không tự ý thu hẹp đại từ thay thế (*"cơ chế này"*) hoặc biến quan hệ mục đích (*"để..."*) thành điều kiện địa điểm nếu bản gốc không khẳng định vậy.
