# Bộ Đánh giá Đọc hiểu Ẩn danh cho Người dùng (`human-blind-eval-pack.md`)

Bộ tài liệu này chứa **7 tình huống (`SR-01`..`SR-07`)** với các phương án viết lại đã được **ẩn danh hoàn toàn** và **đảo ngẫu nhiên thứ tự** giữa các nhóm đối chứng.

**Cách chấm gợi ý (không xem khóa đối chiếu trước khi chấm):**

Với mỗi mẫu trong từng tình huống, đánh giá theo 5 câu hỏi nhanh:

1. **Hiểu ngay lần đầu (1–5):** Đọc một lượt có nắm trọn việc gì xảy ra không?

2. **Tự nhiên tiếng Việt (1–5):** Nghe giống người Việt viết cho nhau đọc hay giống dịch/văn hành chính?

3. **Rõ tác động & việc cần làm (1–5):** Người đọc biết ngay mình bị ảnh hưởng gì và phải làm gì không?

4. **Trung thực dữ kiện (`Đạt` / `Không đạt`):** Có giữ đúng số liệu, ngoại lệ và không tự bịa chi tiết ngoài bản gốc không?

5. **Xếp hạng chọn bản tốt nhất:** Chọn `Mẫu` bạn muốn gửi cho người đọc thật nhất.


---

## SR-01 — Thông báo dịch vụ: Thông báo tối ưu hóa cơ chế vận hành và đồng bộ tài khoản (Seed Case)

- **Người đọc mục tiêu:** Người dùng cuối của nền tảng
- **Mục đích:** Hiểu ngay sắp có thay đổi gì về gia hạn & đồng bộ tài khoản, tác động khi thanh toán liên kết chưa đồng bộ, ngoại lệ cho tài khoản cũ và việc người dùng cần kiểm tra ngay.

### Văn bản gốc

```text
Thông báo về việc tối ưu hóa cơ chế vận hành và nâng cấp trải nghiệm đồng bộ hóa tài khoản

Trong bối cảnh không ngừng nỗ lực nâng cao chất lượng dịch vụ nhằm kiến tạo một hệ sinh thái tương tác liền mạch và tối ưu hóa giá trị dài hạn cho người dùng, chúng tôi trân trọng thông báo về việc triển khai lộ trình tái cấu trúc cơ chế quản trị phiên truy cập và luồng xử lý gia hạn tự động trên nền tảng.

Theo đó, kể từ chu kỳ chuyển đổi sắp tới, việc duy trì tính liên tục của các gói dịch vụ đang ở trạng thái kích hoạt sẽ không còn được thực thi thông qua phương thức ghi nhận mặc định trước đây, mà sẽ được điều phối chuyển sang mô hình xác thực đa tầng có điều kiện. Trong trường hợp các thiết lập liên quan đến phương thức thanh toán liên kết chưa đạt được trạng thái đồng bộ hóa đầy đủ tại thời điểm hệ thống tiến hành đối soát định kỳ, quá trình kích hoạt lại quyền truy cập có thể ghi nhận sự gián đoạn cục bộ hoặc phát sinh trạng thái tạm treo đối với một số tính năng nâng cao cho đến khi các điều kiện tiên quyết được hoàn tất xác minh lại.

Đồng thời, đối với các tài khoản thuộc diện chuyển tiếp từ phiên bản lưu trữ cũ, dữ liệu phát sinh trong khoảng thời gian giao thoa giữa hai cơ chế vận hành sẽ được xử lý theo quy tắc ưu tiên bất đồng bộ nhằm giảm thiểu rủi ro xung đột thông tin, ngoại trừ các trường hợp đã chủ động thiết lập giới hạn truy xuất thủ công trước mốc triển khai. Để đảm bảo hành trình trải nghiệm không bị ảnh hưởng ngoài mong muốn, khuyến nghị quý người dùng chủ động rà soát tính tương thích của cấu hình hiện tại và thực hiện các điều chỉnh phù hợp theo định hướng mới trong thời gian sớm nhất.
```

### Mẫu 1

Thông báo thay đổi cơ chế gia hạn dịch vụ và đồng bộ tài khoản
Trong thời gian tới, chúng tôi sẽ cập nhật cách quản lý phiên truy cập, gia hạn dịch vụ tự động và xử lý dữ liệu tài khoản. Những thay đổi cụ thể như sau:

1. Gia hạn dịch vụ và quyền truy cập

Hệ thống sẽ thay thế cơ chế duy trì gói dịch vụ hiện tại bằng cơ chế xác thực nhiều lớp dựa trên các điều kiện nhất định.

Khi hệ thống kiểm tra định kỳ, nếu thông tin thiết lập phương thức thanh toán chưa được đồng bộ đầy đủ, việc khôi phục quyền truy cập có thể bị gián đoạn hoặc một số tính năng nâng cao có thể tạm thời không sử dụng được. Tình trạng này có thể kéo dài cho đến khi các điều kiện cần thiết được xác minh lại.

2. Xử lý dữ liệu trong giai đoạn chuyển đổi

Đối với tài khoản chuyển từ hệ thống lưu trữ cũ, dữ liệu phát sinh trong giai đoạn chuyển đổi sẽ được xử lý theo quy tắc ưu tiên bất đồng bộ để hạn chế xung đột dữ liệu.

Quy tắc này không áp dụng cho các tài khoản đã thiết lập giới hạn truy xuất thủ công trước thời điểm triển khai.

3. Người dùng cần chuẩn bị gì?

Để hạn chế gián đoạn dịch vụ, bạn nên sớm kiểm tra các thiết lập tài khoản hiện tại, bao gồm phương thức thanh toán đã liên kết, và thực hiện những điều chỉnh cần thiết để phù hợp với cơ chế mới.

### Mẫu 2

**Thông báo cập nhật cơ chế vận hành và đồng bộ tài khoản**

Để nâng cao chất lượng dịch vụ, mang lại trải nghiệm liền mạch và tối ưu giá trị lâu dài cho bạn, chúng tôi sẽ thay đổi cơ chế quản lý phiên truy cập và quy trình gia hạn tự động trên nền tảng.

Từ chu kỳ chuyển đổi sắp tới, các gói dịch vụ đang hoạt động sẽ không còn được duy trì theo cách ghi nhận mặc định như trước. Thay vào đó, hệ thống sẽ chuyển sang áp dụng mô hình xác thực đa tầng có điều kiện.

Lưu ý về thanh toán: Nếu các thiết lập liên quan đến phương thức thanh toán liên kết chưa được đồng bộ đầy đủ tại thời điểm hệ thống đối soát định kỳ, quá trình kích hoạt lại quyền truy cập có thể bị gián đoạn cục bộ, hoặc một số tính năng nâng cao có thể bị tạm treo cho đến khi các điều kiện yêu cầu được xác minh lại hoàn tất.

Ngoài ra, đối với các tài khoản chuyển tiếp từ phiên bản lưu trữ cũ, dữ liệu phát sinh trong thời gian chuyển giao giữa hai cơ chế vận hành sẽ được xử lý theo quy tắc ưu tiên bất đồng bộ để giảm nguy cơ xung đột thông tin — ngoại trừ các trường hợp đã chủ động thiết lập giới hạn truy xuất thủ công trước mốc triển khai.

Để tránh ảnh hưởng ngoài ý muốn đến quá trình sử dụng, chúng tôi khuyến nghị bạn chủ động kiểm tra tính tương thích của cấu hình hiện tại và điều chỉnh cho phù hợp với cơ chế mới trong thời gian sớm nhất.

### Mẫu 3

**Thông báo cập nhật cơ chế quản lý phiên truy cập, gia hạn tự động và đồng bộ tài khoản**

Nhằm nâng cao chất lượng dịch vụ và mang lại trải nghiệm liền mạch lâu dài, chúng tôi thông báo triển khai lộ trình thay đổi cơ chế quản lý phiên truy cập và quy trình gia hạn tự động trên nền tảng.

**1. Thay đổi về duy trì và gia hạn gói dịch vụ**
- **Cơ chế mới:** Kể từ chu kỳ chuyển đổi sắp tới, các gói dịch vụ đang kích hoạt sẽ không còn được duy trì liên tục theo cách ghi nhận mặc định như trước, mà sẽ chuyển sang mô hình xác thực đa tầng có điều kiện.
- **Rủi ro gián đoạn có thể xảy ra:** Nếu thiết lập của phương thức thanh toán liên kết chưa được đồng bộ đầy đủ tại thời điểm hệ thống đối soát định kỳ, quá trình kích hoạt lại quyền truy cập **có thể** bị gián đoạn cục bộ hoặc một số tính năng nâng cao **có thể** bị tạm treo, cho đến khi các điều kiện tiên quyết được xác minh lại hoàn tất.

**2. Xử lý dữ liệu cho tài khoản chuyển tiếp từ phiên bản lưu trữ cũ**
- Dữ liệu phát sinh trong thời gian giao thoa giữa hai cơ chế vận hành sẽ được xử lý theo quy tắc ưu tiên bất đồng bộ nhằm giảm rủi ro xung đột thông tin.
- **Ngoại lệ:** Quy tắc này không áp dụng cho các trường hợp đã chủ động cài đặt giới hạn truy xuất thủ công trước mốc triển khai.

**3. Khuyến nghị dành cho bạn**
Để tránh ảnh hưởng ngoài mong muốn đến trải nghiệm sử dụng, chúng tôi khuyến nghị bạn chủ động kiểm tra tính tương thích của cấu hình hiện tại và sớm thực hiện các điều chỉnh phù hợp theo định hướng mới.

---
**Điểm bản gốc chưa nêu cụ thể (nên bổ sung trước khi phát hành cho người dùng cuối):**
- Thời điểm cụ thể của *"chu kỳ chuyển đổi sắp tới"* và *"mốc triển khai"*.
- Chi tiết *"mô hình xác thực đa tầng có điều kiện"* và *"các điều kiện tiên quyết"* cần xác minh lại (người dùng cần thao tác gì hay hệ thống tự thực hiện).
- Danh sách *"một số tính năng nâng cao"* có thể bị tạm treo và hướng dẫn để người dùng kiểm tra, điều chỉnh *"tính tương thích của cấu hình hiện tại"*.

### Mẫu 4

**Thông báo tối ưu hóa cơ chế vận hành và nâng cấp trải nghiệm đồng bộ tài khoản**

Để nâng cao chất lượng dịch vụ, giúp bạn có trải nghiệm tương tác liền mạch và tối ưu hóa giá trị lâu dài, chúng tôi trân trọng thông báo về lộ trình thay đổi cơ chế quản lý phiên truy cập và quy trình gia hạn tự động trên nền tảng.

**1. Thay đổi cơ chế gia hạn và duy trì gói dịch vụ**
- Kể từ chu kỳ chuyển đổi sắp tới, việc duy trì liên tục các gói dịch vụ đang hoạt động sẽ không còn thực hiện theo cách ghi nhận mặc định như trước đây, mà chuyển sang mô hình xác thực nhiều lớp có điều kiện.
- Nếu các cài đặt liên quan đến phương thức thanh toán liên kết chưa được đồng bộ đầy đủ tại thời điểm hệ thống đối soát định kỳ, quá trình kích hoạt lại quyền truy cập **có thể** bị gián đoạn cục bộ hoặc một số tính năng nâng cao **có thể** bị tạm ngưng cho đến khi các điều kiện tiên quyết được xác minh lại hoàn tất.

**2. Xử lý dữ liệu cho tài khoản chuyển tiếp từ phiên bản lưu trữ cũ**
- Với các tài khoản thuộc diện chuyển tiếp từ phiên bản lưu trữ cũ, dữ liệu phát sinh trong giai đoạn chuyển giao giữa hai cơ chế vận hành sẽ được xử lý theo quy tắc ưu tiên bất đồng bộ nhằm giảm rủi ro xung đột thông tin.
- **Ngoại lệ:** Quy tắc này không áp dụng cho các trường hợp đã chủ động cài đặt giới hạn truy xuất thủ công trước thời điểm triển khai.

**3. Khuyến nghị dành cho bạn**
Để trải nghiệm sử dụng không bị ảnh hưởng ngoài ý muốn, chúng tôi khuyến nghị bạn chủ động kiểm tra tính tương thích của cấu hình hiện tại và điều chỉnh cho phù hợp với định hướng mới trong thời gian sớm nhất.

### Phiếu chấm nhanh của bạn

- Mẫu tự nhiên & dễ hiểu nhất: `...`
- Mẫu giữ đúng ý nhưng còn cứng / nặng từ ngữ gốc: `...`
- Ghi chú cảm nhận: `...`

---

## SR-02 — Thông báo dịch vụ: Thông báo điều chỉnh chính sách dọn dẹp tệp đính kèm không phát sinh truy cập

- **Người đọc mục tiêu:** Người dùng nền tảng quản lý công việc
- **Mục đích:** Nắm được quy tắc tự động xóa tệp đính kèm sau 180 ngày không truy cập, mốc nhắc trước 15 ngày, trường hợp ngoại lệ được giữ lại và việc cần làm để không mất dữ liệu.

### Văn bản gốc

```text
Thông báo về việc áp dụng cơ chế chuẩn hóa vòng đời lưu trữ đối với các tệp đính kèm không phát sinh hoạt động truy xuất

Nhằm mục tiêu nâng cao hiệu suất vận hành tài nguyên hạ tầng cũng như tối ưu hóa dung lượng lưu trữ khả dụng cho toàn bộ người dùng thuộc gói miễn phí và gói tiêu chuẩn, kể từ tháng tới hệ thống sẽ tiến hành kích hoạt quy trình tự động điều chuyển vòng đời đối với các tệp tin đính kèm không ghi nhận tương tác. Cụ thể, những tệp tin không phát sinh bất kỳ lượt mở xem hay tải xuống nào trong khoảng thời gian 180 ngày liên tiếp sẽ được tự động đưa vào khu vực thùng rác hệ thống, trước khi bị tiến hành thanh lọc vĩnh viễn sau 30 ngày tiếp theo nếu chủ sở hữu không thực hiện thao tác khôi phục.

Trước thời điểm chuyển trạng thái vào thùng rác 15 ngày, hệ thống sẽ thực hiện gửi thư điện tử cảnh báo tới địa chỉ liên hệ đã đăng ký. Tuy nhiên, quy định tự động xử lý nêu trên sẽ không áp dụng đối với các tệp được sắp xếp trong thư mục gắn nhãn Lưu trữ cố định (Pinned Archive) hoặc thuộc phạm vi tài khoản đang kích hoạt chế độ khóa bảo toàn pháp lý (Legal Hold). Khuyến nghị người dùng chủ động kiểm tra lại các tệp dữ liệu quan trọng và thực hiện thao tác phân loại phù hợp nhằm hạn chế nguy cơ thất thoát dữ liệu ngoài ý muốn.
```

### Mẫu 1

**Thông báo: Tự động chuyển vào thùng rác và xóa tệp đính kèm không truy cập từ tháng tới**

Từ tháng tới, hệ thống sẽ áp dụng quy trình tự động xử lý các tệp đính kèm không có tương tác đối với **toàn bộ người dùng gói miễn phí và gói tiêu chuẩn**, nhằm nâng cao hiệu suất vận hành hạ tầng và tối ưu dung lượng lưu trữ khả dụng.

### 1. Điều gì sắp thay đổi?
Cơ chế tự động áp dụng cho các tệp đính kèm không phát sinh **bất kỳ lượt mở xem hay tải xuống nào trong 180 ngày liên tiếp**:
- **Trước khi chuyển vào thùng rác 15 ngày:** Hệ thống gửi email cảnh báo tới địa chỉ liên hệ đã đăng ký.
- **Đủ 180 ngày liên tiếp không mở xem hay tải xuống:** Hệ thống tự động chuyển tệp vào thùng rác.
- **Sau 30 ngày tiếp theo trong thùng rác:** Nếu chủ sở hữu không khôi phục, tệp sẽ bị xóa vĩnh viễn.

### 2. Ngoại lệ được giữ lại
Quy định tự động xử lý trên **không áp dụng** cho các tệp:
- Được sắp xếp trong thư mục gắn nhãn **Lưu trữ cố định (Pinned Archive)**; hoặc
- Thuộc tài khoản đang bật chế độ **khóa bảo toàn pháp lý (Legal Hold)**.

### 3. Cần làm gì để tránh mất tệp?
- Chủ động kiểm tra lại các tệp dữ liệu quan trọng và phân loại phù hợp để tránh mất dữ liệu ngoài ý muốn (các tệp sắp xếp trong thư mục **Lưu trữ cố định (Pinned Archive)** sẽ không bị xử lý tự động).
- Lưu ý email cảnh báo gửi tới địa chỉ liên hệ đã đăng ký (**15 ngày** trước khi tệp chuyển vào thùng rác) và khôi phục trong vòng **30 ngày** nếu tệp đã vào thùng rác.

### Mẫu 2

**Thông báo: Tự động chuyển và xóa tệp đính kèm không có tương tác (từ tháng tới)**

Nhằm nâng cao hiệu suất vận hành hạ tầng và tối ưu dung lượng lưu trữ khả dụng cho người dùng **gói miễn phí** và **gói tiêu chuẩn**, **kể từ tháng tới**, hệ thống sẽ áp dụng quy trình tự động xử lý đối với các tệp đính kèm không có lượt truy cập.

### 1. Điều gì sắp thay đổi?
- **Điều kiện áp dụng:** Tệp đính kèm không có bất kỳ lượt **mở xem** hay **tải xuống** nào trong **180 ngày liên tiếp**.
- **15 ngày trước khi chuyển vào thùng rác:** Hệ thống gửi email cảnh báo tới địa chỉ liên hệ đã đăng ký.
- **Đủ 180 ngày không tương tác:** Tệp tự động được chuyển vào **thùng rác** hệ thống.
- **Sau 30 ngày tiếp theo:** Tệp bị **xóa vĩnh viễn** nếu chủ sở hữu không khôi phục.

### 2. Ngoại lệ được giữ lại
Quy định tự động xử lý trên **không áp dụng** đối với:
- Các tệp được sắp xếp trong thư mục gắn nhãn **Lưu trữ cố định (Pinned Archive)**; **hoặc**
- Các tệp thuộc phạm vi tài khoản đang kích hoạt chế độ **khóa bảo toàn pháp lý (Legal Hold)**.

### 3. Cần làm gì để tránh mất tệp?
- Chủ động **kiểm tra lại các tệp dữ liệu quan trọng** và **phân loại phù hợp** (như sắp xếp vào thư mục **Lưu trữ cố định (Pinned Archive)**) để tránh mất dữ liệu ngoài ý muốn.
- Theo dõi **email cảnh báo** được gửi **15 ngày trước khi** tệp bị chuyển vào thùng rác.
- Nếu tệp đã vào thùng rác, hãy **khôi phục trong vòng 30 ngày** trước khi hệ thống xóa vĩnh viễn.

### Mẫu 3

**Thông báo: Tự động dọn dẹp tệp đính kèm không có lượt truy cập từ tháng tới**

Để nâng cao hiệu suất hạ tầng và tối ưu dung lượng lưu trữ, **từ tháng tới**, hệ thống sẽ tự động đưa vào thùng rác và xóa vĩnh viễn các tệp đính kèm không có tương tác của toàn bộ người dùng thuộc **gói miễn phí** và **gói tiêu chuẩn**.

**1. Điều gì sắp thay đổi?**
Với các tệp đính kèm **không có bất kỳ lượt mở xem hay tải xuống nào trong 180 ngày liên tiếp**, hệ thống sẽ xử lý theo lộ trình sau:
- **Trước khi chuyển vào thùng rác 15 ngày:** Hệ thống gửi email cảnh báo tới địa chỉ liên hệ đã đăng ký.
- **Sau 180 ngày liên tiếp không truy cập:** Hệ thống tự động chuyển tệp vào **thùng rác hệ thống**.
- **Sau 30 ngày tiếp theo trong thùng rác:** Tệp bị **xóa vĩnh viễn** nếu chủ sở hữu không khôi phục.

**2. Ngoại lệ nào được giữ lại?**
Quy định tự động xử lý nêu trên **không áp dụng** đối với các tệp:
- Được sắp xếp trong thư mục gắn nhãn **Lưu trữ cố định (Pinned Archive)**; **hoặc**
- Thuộc tài khoản đang bật chế độ **khóa bảo toàn pháp lý (Legal Hold)**.

**3. Cần làm gì để tránh mất tệp?**
- **Kiểm tra và phân loại tệp quan trọng:** Chủ động rà soát các tệp dữ liệu quan trọng và phân loại phù hợp (như sắp xếp vào thư mục **Lưu trữ cố định (Pinned Archive)**) để hạn chế nguy cơ mất dữ liệu ngoài ý muốn.
- **Theo dõi email cảnh báo:** Chú ý email thông báo được gửi trước 15 ngày để kịp thời xử lý.
- **Khôi phục kịp thời:** Nếu tệp đã chuyển vào thùng rác, chủ sở hữu cần thực hiện khôi phục trước khi hết **30 ngày** lưu tại thùng rác để tránh bị xóa vĩnh viễn.

### Phiếu chấm nhanh của bạn

- Mẫu tự nhiên & dễ hiểu nhất: `...`
- Mẫu giữ đúng ý nhưng còn cứng / nặng từ ngữ gốc: `...`
- Ghi chú cảm nhận: `...`

---

## SR-03 — Giao tiếp công việc: Tin nhắn nhóm dự án báo dời lịch phát hành và phân công FE/BE/QA

- **Người đọc mục tiêu:** Đội kỹ thuật FE, BE, QA trên Slack/Teams
- **Mục đích:** Nắm ngay kết luận dời lịch release từ 14:00 thứ Năm sang 10:00 thứ Hai tuần sau, hiểu lý do ngắn gọn và biết rõ từng team phải làm gì trước mốc mới.

### Văn bản gốc

```text
Chào mọi người trong nhóm dự án 2.4, lời đầu tiên mình xin cảm ơn sự cố gắng của tất cả anh chị em trong sprint vừa qua để kịp hoàn thành phần lớn các hạng mục đúng tiến độ đề ra. Tuy nhiên, do một số vướng mắc khách quan phát sinh từ phía đối tác ngân hàng trong việc bàn giao môi trường sandbox cho API đối soát thanh toán bị chậm sang tận chiều thứ Sáu nên sau khi trao đổi nhanh với anh lead kỹ thuật và team sản phẩm, tụi mình nhận thấy nếu vẫn giữ kế hoạch phát hành vào 14:00 thứ Năm tuần này sẽ tiềm ẩn rất nhiều rủi ro cho luồng thanh toán thực tế. Vì vậy, lịch phát hành phiên bản 2.4 dự kiến sẽ được điều chỉnh lùi sang 10:00 sáng thứ Hai tuần sau. Để tận dụng khoảng thời gian đệm này một cách hiệu quả nhất, nhờ phía Backend hỗ trợ hoàn thiện phần tích hợp mock fallback và triển khai lên môi trường staging chậm nhất trước 17:00 thứ Sáu; trong khi đó, bên Frontend vẫn giữ nguyên nhánh giao diện hiện tại và vui lòng thực hiện đóng băng code (không merge thêm bất kỳ tính năng mới nào sau 18:00 tối nay), chỉ xử lý các lỗi chặn luồng nếu có phản hồi từ đội kiểm thử. Về phía QA, ngay sau khi Backend cập nhật hoàn chỉnh môi trường staging thì nhờ các bạn thực hiện chạy lại toàn bộ bộ kiểm thử hồi quy cho luồng thanh toán vào sáng thứ Bảy để chúng ta kịp rà soát và chốt việc đưa bản 2.4 lên production vào đúng 10:00 thứ Hai tuần sau trong trường hợp không còn phát sinh lỗi blocker nào.
```

### Mẫu 1

**[Thông báo] Dự kiến lùi lịch phát hành phiên bản 2.4 sang 10:00 sáng thứ Hai tuần sau**

Sau khi trao đổi với lead kỹ thuật và team sản phẩm, chúng ta **dự kiến lùi lịch phát hành phiên bản 2.4 từ 14:00 thứ Năm tuần này sang 10:00 sáng thứ Hai tuần sau** (trong trường hợp không còn phát sinh lỗi blocker nào).

**Lý do:** Đối tác ngân hàng bàn giao môi trường sandbox cho API đối soát thanh toán bị chậm sang chiều thứ Sáu. Nếu vẫn giữ lịch phát hành 14:00 thứ Năm tuần này sẽ tiềm ẩn nhiều rủi ro cho luồng thanh toán thực tế.

**Phân việc cho từng team:**

- **FE:**
  - Giữ nguyên nhánh giao diện hiện tại và đóng băng code: **không merge thêm bất kỳ tính năng mới nào sau 18:00 tối nay**.
  - Chỉ xử lý các lỗi chặn luồng nếu có phản hồi từ QA.

- **BE:**
  - Hoàn thiện phần tích hợp mock fallback và triển khai lên môi trường staging **chậm nhất trước 17:00 thứ Sáu**.

- **QA:**
  - Ngay sau khi BE cập nhật hoàn chỉnh môi trường staging, chạy lại toàn bộ bộ kiểm thử hồi quy cho luồng thanh toán vào **sáng thứ Bảy** để kịp rà soát và chốt đưa bản 2.4 lên production vào đúng **10:00 thứ Hai tuần sau** (nếu không còn phát sinh lỗi blocker nào).

### Mẫu 2

**[Thông báo] Dời lịch phát hành phiên bản 2.4 sang 10:00 sáng thứ Hai tuần sau**

Chào nhóm dự án 2.4,

**1. Quyết định & Lý do**
- **Lịch phát hành dự kiến mới:** Điều chỉnh lùi từ **14:00 thứ Năm tuần này** sang **10:00 sáng thứ Hai tuần sau** (chốt đưa lên production đúng mốc này nếu không còn phát sinh lỗi blocker nào).
- **Lý do:** Đối tác ngân hàng bàn giao chậm môi trường sandbox cho API đối soát thanh toán sang tận chiều thứ Sáu. Sau khi trao đổi nhanh với anh lead kỹ thuật và team sản phẩm, việc giữ kế hoạch cũ tiềm ẩn rất nhiều rủi ro cho luồng thanh toán thực tế.

*(Cảm ơn anh chị em đã cố gắng hoàn thành phần lớn các hạng mục đúng tiến độ trong sprint vừa qua.)*

**2. Phân việc cụ thể trong thời gian đệm**
- **FE:**
  - Giữ nguyên nhánh giao diện hiện tại và đóng băng code (**không merge thêm bất kỳ tính năng mới nào sau 18:00 tối nay**).
  - Chỉ xử lý các lỗi chặn luồng nếu có phản hồi từ đội kiểm thử.
- **BE:**
  - Hoàn thiện phần tích hợp mock fallback và triển khai lên môi trường staging **chậm nhất trước 17:00 thứ Sáu**.
- **QA:**
  - Ngay sau khi BE cập nhật hoàn chỉnh môi trường staging, chạy lại toàn bộ bộ kiểm thử hồi quy cho luồng thanh toán vào **sáng thứ Bảy** để kịp rà soát và chốt đưa bản 2.4 lên production vào đúng **10:00 thứ Hai tuần sau** (trường hợp không còn phát sinh lỗi blocker nào).

### Mẫu 3

**THÔNG BÁO ĐIỀU CHỈNH LỊCH PHÁT HÀNH PHIÊN BẢN 2.4**

Lịch phát hành phiên bản 2.4 **dự kiến lùi từ 14:00 thứ Năm tuần này sang 10:00 sáng thứ Hai tuần sau**.

**Lý do:** Đối tác ngân hàng bàn giao môi trường sandbox cho API đối soát thanh toán chậm sang tận **chiều thứ Sáu**. Sau khi trao đổi với anh lead kỹ thuật và team sản phẩm, việc giữ kế hoạch phát hành vào 14:00 thứ Năm tuần này sẽ tiềm ẩn nhiều rủi ro cho luồng thanh toán thực tế.

**Phân việc cho các team:**
- **Team FE:**
  - Giữ nguyên nhánh giao diện hiện tại và đóng băng code: **không merge thêm bất kỳ tính năng mới nào sau 18:00 tối nay**.
  - Chỉ xử lý các lỗi chặn luồng nếu có phản hồi từ đội kiểm thử.
- **Team BE:**
  - Hoàn thiện phần tích hợp mock fallback.
  - Triển khai lên môi trường staging **chậm nhất trước 17:00 thứ Sáu**.
- **Team QA:**
  - Ngay sau khi BE cập nhật hoàn chỉnh môi trường staging, chạy lại toàn bộ bộ kiểm thử hồi quy cho luồng thanh toán vào **sáng thứ Bảy** để cả nhóm kịp rà soát.

**Điều kiện chốt phát hành:** Đưa bản 2.4 lên production vào đúng **10:00 thứ Hai tuần sau** trong trường hợp không còn phát sinh lỗi blocker nào.

Cảm ơn sự cố gắng của tất cả anh chị em trong sprint vừa qua để hoàn thành phần lớn các hạng mục đúng tiến độ.

### Phiếu chấm nhanh của bạn

- Mẫu tự nhiên & dễ hiểu nhất: `...`
- Mẫu giữ đúng ý nhưng còn cứng / nặng từ ngữ gốc: `...`
- Ghi chú cảm nhận: `...`

---

## SR-04 — Giải thích khái niệm: Giải thích cơ chế Idempotency Key kết hợp Exponential Backoff khi thanh toán

- **Người đọc mục tiêu:** Product Manager, BA và kỹ sư mới vào nhóm ví điện tử
- **Mục đích:** Hiểu rõ Idempotency Key là gì, Exponential Backoff giải quyết vấn đề gì, hai cơ chế phối hợp ra sao để vừa thử lại khi rớt mạng vừa không trừ tiền hai lần.

### Văn bản gốc

```text
Trong thiết kế hệ thống phân tán phục vụ thanh toán, việc kết hợp cơ chế khóa định danh bất biến (Idempotency Key) với chiến lược giãn cách thời gian thử lại theo hàm mũ (Exponential Backoff) đóng vai trò mang tính nền tảng trong việc đảm bảo sự an toàn của giao dịch trước các sự cố gián đoạn kết nối mạng. Khi một yêu cầu thanh toán từ phía ứng dụng gửi đi gặp phải tình trạng rớt mạng hoặc hết thời gian chờ phản hồi (timeout), phía gọi sẽ rơi vào trạng thái không thể xác định được liệu máy chủ đã thực hiện việc ghi nhận trừ tiền hay chưa, dẫn đến nhu cầu bắt buộc phải tiến hành gửi lại yêu cầu. Nếu chỉ thực hiện việc thử lại một cách tuần tự thông thường, sự việc sẽ làm gia tăng nguy cơ phát sinh hiện tượng trừ tiền trùng lặp trên tài khoản người dùng; do đó, Idempotency Key được sử dụng như một mã định danh duy nhất đại diện cho mỗi giao dịch nhằm giúp máy chủ nhận diện các yêu cầu lặp lại và trả về kết quả đã xử lý trước đó thay vì thực thi lại thao tác tài chính. Song song với việc bảo vệ tính duy nhất đó, chiến lược Exponential Backoff thực hiện việc kéo dài khoảng thời gian chờ giữa các lần thử lại liên tiếp theo cấp số nhân, kết hợp cùng biên độ dao động ngẫu nhiên (jitter), với mục đích ngăn chặn tình trạng hàng loạt ứng dụng đồng loạt gửi lại yêu cầu tại cùng một thời điểm gây quá tải dây chuyền lên máy chủ đang gặp sự cố. Như vậy, hai cơ chế giải quyết hai vấn đề hoàn toàn bổ trợ lẫn nhau: Backoff kiểm soát tần suất và thời điểm gửi lại để bảo vệ năng lực chịu tải của hệ thống, trong khi Idempotency Key đảm bảo tính đúng đắn rằng giao dịch chỉ được thực thi tối đa một lần. Tuy nhiên, cần lưu ý rằng Idempotency Key chỉ phát huy hiệu lực trong khoảng thời gian máy chủ còn lưu trữ mã khóa này, đồng thời cũng không thể ngăn chặn việc trừ tiền hai lần nếu phía ứng dụng vô tình sinh ra một mã khóa hoàn toàn mới cho cùng một giao dịch đang thanh toán.
```

### Mẫu 1

Trong hệ thống thanh toán phân tán, khi ứng dụng gửi yêu cầu thanh toán đi nhưng bị rớt mạng hoặc quá thời gian chờ phản hồi (timeout), ứng dụng sẽ không biết máy chủ đã trừ tiền hay chưa. Lúc này, ứng dụng buộc phải gửi lại yêu cầu.

Tuy nhiên, nếu chỉ thử lại theo cách thông thường, giao dịch dễ bị trừ tiền trùng lặp trên tài khoản người dùng; đồng thời, nếu nhiều ứng dụng đồng loạt gửi lại yêu cầu vào cùng một thời điểm, máy chủ đang gặp sự cố có thể bị quá tải dây chuyền.

Để giải quyết cả hai vấn đề này, hệ thống kết hợp hai cơ chế bổ trợ lẫn nhau:

- **Idempotency Key — Đảm bảo mỗi giao dịch chỉ thực hiện tối đa một lần:** Ứng dụng gắn cho mỗi giao dịch một mã định danh duy nhất. Khi nhận được yêu cầu gửi lại mang cùng mã khóa này, máy chủ nhận diện đây là yêu cầu lặp lại và trả về kết quả đã xử lý trước đó, thay vì trừ tiền thêm lần nữa.
- **Exponential Backoff kèm jitter — Bảo vệ năng lực chịu tải của hệ thống:** Cơ chế này kiểm soát tần suất và thời điểm gửi lại. Ứng dụng sẽ kéo dài dần khoảng thời gian chờ giữa các lần thử lại liên tiếp theo cấp số nhân, kết hợp thêm một khoảng dao động ngẫu nhiên (jitter). Nhờ vậy, các yêu cầu thử lại được giãn ra, tránh tình trạng hàng loạt ứng dụng dội yêu cầu về máy chủ cùng lúc khi hệ thống đang gặp sự cố.

Tóm lại, hai cơ chế giải quyết hai bài toán tách bạch nhưng phối hợp chặt chẽ: **Exponential Backoff** điều tiết nhịp gửi lại để hệ thống không bị quá tải, còn **Idempotency Key** đảm bảo tính đúng đắn để giao dịch chỉ được thực thi tối đa một lần.

**Hai giới hạn quan trọng cần lưu ý:**
1. **Giới hạn về thời gian lưu trữ:** Idempotency Key chỉ còn tác dụng trong khoảng thời gian máy chủ vẫn lưu trữ mã khóa này.
2. **Rủi ro từ phía ứng dụng:** Cơ chế này không thể ngăn việc trừ tiền hai lần nếu ứng dụng vô tình tạo ra một mã khóa hoàn toàn mới cho cùng một giao dịch đang thanh toán.

### Mẫu 2

Trong hệ thống thanh toán phân tán, việc kết hợp **Idempotency Key** (khóa định danh bất biến) và **Exponential Backoff** (giãn cách thời gian thử lại theo hàm mũ) là nền tảng giúp giao dịch an toàn khi kết nối mạng bị gián đoạn.

### 1. Vì sao gửi lại yêu cầu thanh toán lại tiềm ẩn rủi ro?
Khi ứng dụng gửi yêu cầu thanh toán nhưng bị rớt mạng hoặc hết thời gian chờ phản hồi (**timeout**), phía gọi không thể biết máy chủ đã ghi nhận trừ tiền hay chưa, nên buộc phải gửi lại yêu cầu. Nếu chỉ thử lại theo cách thông thường, hệ thống dễ đối mặt với hai vấn đề:
- **Nguy cơ trừ tiền trùng lặp:** Nếu không có cách nhận diện giao dịch cũ, việc gửi lại tuần tự thông thường sẽ làm tăng nguy cơ tài khoản người dùng bị trừ tiền nhiều lần cho cùng một giao dịch.
- **Nguy cơ quá tải dây chuyền:** Khi nhiều ứng dụng đồng loạt gửi lại yêu cầu tại cùng một thời điểm, máy chủ đang gặp sự cố sẽ bị quá tải dây chuyền.

### 2. Hai cơ chế phối hợp giải quyết bài toán như thế nào?
Hai cơ chế này xử lý hai vấn đề khác nhau nhưng bổ trợ chặt chẽ cho nhau:

- **Idempotency Key — Đảm bảo tính đúng đắn (chỉ thực thi tối đa một lần):**
  Mỗi giao dịch được gán một mã định danh duy nhất. Khi nhận lại yêu cầu mang cùng mã khóa, máy chủ nhận diện được đây là yêu cầu lặp lại và trả về kết quả đã xử lý trước đó, thay vì thực hiện lại thao tác tài chính.
- **Exponential Backoff kết hợp Jitter — Bảo vệ năng lực chịu tải của hệ thống:**
  Ứng dụng kéo dài thời gian chờ giữa các lần thử lại liên tiếp theo cấp số nhân (**Exponential Backoff**), đồng thời cộng thêm một biên độ dao động ngẫu nhiên (**jitter**). Cách này giúp kiểm soát tần suất và thời điểm gửi lại, ngăn tình trạng hàng loạt ứng dụng cùng lúc dồn yêu cầu lên máy chủ đang gặp sự cố.

Nói ngắn gọn: **Backoff** kiểm soát *tần suất và thời điểm gửi lại* để bảo vệ năng lực chịu tải của hệ thống, còn **Idempotency Key** đảm bảo *giao dịch chỉ được thực thi tối đa một lần*.

### 3. Hai giới hạn quan trọng cần lưu ý
Khi áp dụng **Idempotency Key**, đội ngũ sản phẩm và kỹ thuật cần lưu ý hai điểm giới hạn sau:
1. **Hiệu lực phụ thuộc vào thời gian lưu trữ trên máy chủ:** Idempotency Key chỉ phát huy tác dụng trong khoảng thời gian máy chủ còn lưu trữ mã khóa này.
2. **Không tự động bảo vệ nếu ứng dụng tạo mã khóa mới:** Nếu phía ứng dụng vô tình sinh ra một mã khóa hoàn toàn mới cho cùng một giao dịch đang thanh toán, Idempotency Key không thể ngăn việc trừ tiền hai lần.

### Mẫu 3

Trong hệ thống thanh toán phân tán, việc kết hợp **Idempotency Key** (khóa định danh bất biến) và **Exponential Backoff** (giãn cách thời gian thử lại theo hàm mũ) đóng vai trò nền tảng để giữ an toàn cho giao dịch khi kết nối mạng bị gián đoạn.

### 1. Vì sao gửi lại yêu cầu thanh toán lại tiềm ẩn rủi ro?
Khi ứng dụng gửi yêu cầu thanh toán nhưng gặp sự cố rớt mạng hoặc hết thời gian chờ phản hồi (**timeout**), ứng dụng không thể xác định được máy chủ đã ghi nhận trừ tiền hay chưa nên buộc phải gửi lại yêu cầu.

Tuy nhiên, nếu chỉ thử lại theo cách tuần tự thông thường, người dùng sẽ đối mặt với nguy cơ bị trừ tiền trùng lặp trên tài khoản. Đồng thời, nếu nhiều ứng dụng cùng đồng loạt gửi lại yêu cầu tại một thời điểm, máy chủ đang gặp sự cố sẽ bị quá tải dây chuyền.

### 2. Hai cơ chế phối hợp với nhau như thế nào?
Hai cơ chế này giải quyết hai khía cạnh khác nhau nhưng bổ trợ chặt chẽ cho nhau:

* **Idempotency Key — Đảm bảo tính đúng đắn (giao dịch chỉ thực hiện tối đa một lần):**
  Mỗi giao dịch được gắn một mã định danh duy nhất. Khi nhận được các yêu cầu gửi lại, máy chủ dựa vào mã này để nhận diện đây là yêu cầu lặp lại và trả về kết quả đã xử lý trước đó, thay vì thực hiện lại thao tác tài chính.
* **Exponential Backoff kèm Jitter — Bảo vệ sức chịu tải của hệ thống:**
  Thay vì gửi lại liên tiếp ngay lập tức, ứng dụng sẽ kéo dài thời gian chờ giữa các lần thử lại theo cấp số nhân, kết hợp thêm một khoảng dao động ngẫu nhiên (**jitter**). Cách này giúp ngăn tình trạng hàng loạt ứng dụng đồng loạt gửi lại yêu cầu cùng lúc gây quá tải dây chuyền lên máy chủ đang gặp sự cố.

Tóm lại, **Exponential Backoff** kiểm soát *tần suất và thời điểm* gửi lại để bảo vệ năng lực chịu tải của hệ thống, trong khi **Idempotency Key** đảm bảo *tính đúng đắn* để giao dịch chỉ được thực thi tối đa một lần.

### 3. Hai giới hạn quan trọng cần lưu ý
Khi áp dụng, cần lưu ý hai giới hạn sau của **Idempotency Key**:

* **Phụ thuộc vào thời gian lưu trữ trên máy chủ:** Idempotency Key chỉ phát huy hiệu lực trong khoảng thời gian máy chủ còn lưu trữ mã khóa này.
* **Không chống được trùng lặp nếu ứng dụng tạo mã mới:** Nếu phía ứng dụng vô tình sinh ra một mã khóa hoàn toàn mới cho cùng một giao dịch đang thanh toán, cơ chế này không thể ngăn chặn việc trừ tiền hai lần.

### Phiếu chấm nhanh của bạn

- Mẫu tự nhiên & dễ hiểu nhất: `...`
- Mẫu giữ đúng ý nhưng còn cứng / nặng từ ngữ gốc: `...`
- Ghi chú cảm nhận: `...`

---

## SR-05 — Business Rule: Quy tắc hoàn tiền từng phần và xử lý mã giảm giá (có chi tiết chưa chốt)

- **Người đọc mục tiêu:** Đội Sản phẩm (BA/PO) và Kỹ sư Thanh toán
- **Mục đích:** Làm rõ quy tắc hoàn tiền khi khách trả một phần đơn hàng đã áp mã giảm giá, đồng thời chỉ rõ các điểm quy tắc gốc chưa chốt (phí ship và số ngày hoàn tiền) để không tự đoán khi code.

### Văn bản gốc

```text
Quy định về việc thực hiện hoàn trả tài chính từng phần đối với đơn hàng đa sản phẩm có áp dụng mã ưu đãi

Trong trường hợp người mua tiến hành yêu cầu hoàn trả đối với một hoặc một số hạng mục sản phẩm nằm trong cùng một đơn hàng có sự áp dụng của mã giảm giá tính trên tổng giá trị đơn, giá trị khoản tiền thực hiện hoàn trả cho từng sản phẩm sẽ không được căn cứ theo đơn giá niêm yết ban đầu của sản phẩm đó, mà phải được xác định trên cơ sở số tiền thực tế đã thanh toán sau khi đã thực hiện việc phân bổ phần giá trị được khấu trừ từ mã giảm giá theo tỷ lệ giá trị của từng mặt hàng cấu thành nên đơn hàng. Tuy nhiên, đối với tình huống việc hoàn trả một phần nêu trên dẫn đến hệ quả là tổng giá trị của phần hàng hóa còn lại mà người mua giữ lại bị rơi xuống dưới mức ngưỡng tối thiểu cần thiết để đủ điều kiện hưởng ưu đãi của mã giảm giá đã áp dụng, hệ thống sẽ tiến hành khấu trừ hồi tố phần giá trị ưu đãi tương ứng trước khi xác định khoản tiền hoàn trả cuối cùng. Đồng thời, mã giảm giá đã được kích hoạt sử dụng cho đơn hàng có phát sinh trả hàng một phần sẽ không thuộc diện được hoàn trả lại vào tài khoản của người mua để tái sử dụng cho các giao dịch kế tiếp.
```

### Mẫu 1

# Quy định nghiệp vụ: Hoàn tiền khi trả một phần đơn hàng đa sản phẩm có áp dụng mã giảm giá

## 1. Phạm vi áp dụng
Áp dụng cho **đơn hàng đa sản phẩm** đã sử dụng **mã giảm giá tính trên tổng giá trị đơn hàng**, khi người mua yêu cầu hoàn trả **một hoặc một số** sản phẩm trong đơn (trả hàng một phần).

---

## 2. Quy tắc nghiệp vụ

### BR-01: Nguyên tắc xác định tiền hoàn trả theo tỷ lệ phân bổ mã giảm giá
- **Điều kiện kích hoạt:** Người mua yêu cầu hoàn trả một phần đơn hàng thỏa phạm vi áp dụng tại Mục 1.
- **Quy định bắt buộc:**
  - Hệ thống **không** tính tiền hoàn trả dựa trên đơn giá niêm yết ban đầu của sản phẩm trả lại.
  - Tiền hoàn trả cho từng sản phẩm được xác định theo **số tiền thực tế người mua đã thanh toán** cho sản phẩm đó, sau khi đã trừ đi phần giá trị ưu đãi của mã giảm giá được phân bổ theo **tỷ lệ giá trị của từng mặt hàng** trong đơn hàng.

### BR-02: Khấu trừ hồi tố khi phần hàng giữ lại không còn đạt ngưỡng ưu đãi
- **Điều kiện kích hoạt:** Sau khi loại trừ các sản phẩm yêu cầu trả lại, tổng giá trị phần hàng hóa còn lại mà người mua giữ lại giảm xuống **dưới mức ngưỡng tối thiểu** (`< ngưỡng tối thiểu`) để đủ điều kiện hưởng ưu đãi của mã giảm giá đã áp dụng.
- **Quy định bắt buộc:** Trước khi xác định số tiền hoàn trả cuối cùng, hệ thống **phải khấu trừ hồi tố phần giá trị ưu đãi tương ứng** vào khoản tiền hoàn trả dự kiến.

### BR-03: Không hoàn lại mã giảm giá đã sử dụng
- **Điều kiện kích hoạt:** Đơn hàng có áp dụng mã giảm giá và phát sinh giao dịch trả hàng một phần.
- **Quy định bắt buộc:** Hệ thống **không hoàn lại** mã giảm giá đã kích hoạt cho đơn hàng vào tài khoản của người mua; người mua không được tái sử dụng mã này cho các giao dịch tiếp theo.

---

## 3. Điểm chưa xác định cần PO chốt trước khi triển khai
Văn bản nguồn hiện còn các điểm bỏ ngỏ sau đây cần làm rõ để BA hoàn thiện Acceptance Criteria và Kỹ sư viết công thức tính chính xác:

1. **Công thức "khấu trừ hồi tố phần giá trị ưu đãi tương ứng" và trường hợp biên (BR-02):**
   - Cần xác định cụ thể phần ưu đãi bị khấu trừ hồi tố là **phần giảm giá đã phân bổ cho các sản phẩm người mua giữ lại** (tránh trừ trùng phần giảm giá đã trừ sẵn trên sản phẩm trả lại theo BR-01), hay **toàn bộ giá trị mã giảm giá** của đơn hàng.
   - Cần chốt hướng xử lý nếu số tiền khấu trừ hồi tố lớn hơn số tiền dự kiến hoàn trả (ví dụ: chốt tiền hoàn = 0 hay chặn hoàn trả).
2. **Cơ sở tính "giá trị mặt hàng" và quy tắc làm tròn phân bổ (BR-01, BR-02):**
   - Cần làm rõ giá trị dùng để chia tỷ lệ phân bổ và kiểm tra ngưỡng tối thiểu là **đơn giá niêm yết** hay **giá bán thực tế của sản phẩm trước khi áp mã**.
   - Cần chốt quy tắc **làm tròn và xử lý số dư** khi phân bổ giá trị mã giảm giá cho từng sản phẩm để tổng phần phân bổ khớp với giá trị mã đã giảm.
3. **Kịch bản trả hàng một phần nhiều lần trên cùng một đơn:**
   - Cần xác nhận hệ thống có hỗ trợ trả hàng một phần nhiều đợt cho cùng một đơn hàng hay không; nếu có, cần quy định cách tính lũy kế phần hàng giữ lại và phần ưu đãi đã khấu trừ hồi tố từ các lần trước.

### Mẫu 2

# Quy định hoàn tiền khi trả hàng một phần đối với đơn hàng đa sản phẩm có áp dụng mã giảm giá

## 1. Phạm vi áp dụng
- **Áp dụng cho:** Yêu cầu trả hàng và hoàn tiền một phần (trả một hoặc một số sản phẩm) thuộc đơn hàng có nhiều sản phẩm và có áp dụng **mã giảm giá tính trên tổng giá trị đơn hàng**.
- **Chưa quy định trong phạm vi tài liệu này:** Trả toàn bộ đơn hàng, mã giảm giá áp dụng riêng theo từng sản phẩm/danh mục, phí vận chuyển và thời hạn hoàn tiền.

---

## 2. Quy tắc nghiệp vụ (Business Rules)

### BR-01: Tính tiền hoàn trả theo số tiền thực tế đã thanh toán sau phân bổ ưu đãi
- **Điều kiện áp dụng:** Người mua yêu cầu trả một hoặc một số sản phẩm trong đơn hàng thuộc phạm vi trên.
- **Hành vi hệ thống:**
  - Hệ thống **không** tính tiền hoàn dựa trên đơn giá niêm yết ban đầu của sản phẩm được trả.
  - Hệ thống **phải** tính tiền hoàn cho từng sản phẩm dựa trên **số tiền thực tế người mua đã thanh toán** cho sản phẩm đó, sau khi phân bổ số tiền được giảm từ mã giảm giá theo **tỷ lệ giá trị của từng mặt hàng** trong đơn hàng.

### BR-02: Khấu trừ hồi tố ưu đãi khi phần hàng giữ lại không đủ ngưỡng tối thiểu
- **Điều kiện áp dụng:** Sau khi trừ các sản phẩm yêu cầu trả, **tổng giá trị phần hàng hóa người mua giữ lại** nhỏ hơn (`<`) **ngưỡng tối thiểu** để đủ điều kiện hưởng ưu đãi của mã giảm giá đã áp dụng.
- **Hành vi hệ thống:**
  - Hệ thống **phải** khấu trừ hồi tố phần giá trị ưu đãi tương ứng trước khi chốt số tiền hoàn trả cuối cùng cho người mua.
  - Nếu tổng giá trị phần hàng hóa giữ lại lớn hơn hoặc bằng (`>=`) ngưỡng tối thiểu, hệ thống không áp dụng khấu trừ hồi tố và tính tiền hoàn theo **BR-01**.

### BR-03: Không hoàn lại mã giảm giá đã sử dụng
- **Điều kiện áp dụng:** Đơn hàng có áp dụng mã giảm giá và phát sinh trả hàng một phần.
- **Hành vi hệ thống:** Hệ thống **không** hoàn lại mã giảm giá đó vào tài khoản của người mua để tái sử dụng cho các giao dịch sau.

---

## 3. Điểm chưa xác định — Cần PO/Nghiệp vụ chốt trước khi lập trình

Văn bản quy định gốc hiện thiếu các thông số và quy tắc chi tiết dưới đây, chưa đủ điều kiện để kỹ sư viết công thức xử lý đơn nghĩa:

1. **Cơ sở tính "tỷ lệ giá trị từng mặt hàng" và quy tắc làm tròn (BR-01):**
   - Tỷ lệ phân bổ giá trị mã giảm giá được tính theo **giá niêm yết ban đầu** hay **giá bán sau khuyến mãi riêng của từng sản phẩm** (nếu có)?
   - Khi phân bổ tiền giảm giá phát sinh số lẻ (hoặc khi người mua chỉ trả một phần số lượng của cùng một sản phẩm có số lượng > 1), hệ thống làm tròn và dồn phần chênh lệch vào sản phẩm nào?
2. **Cách xác định "tổng giá trị phần hàng hóa còn lại" khi so với ngưỡng tối thiểu (BR-02):**
   - Giá trị dùng để so sánh với ngưỡng tối thiểu của mã giảm giá là **giá trị trước khi trừ mã giảm giá** hay **số tiền thực trả sau khi trừ mã giảm giá**?
3. **Công thức "khấu trừ hồi tố phần giá trị ưu đãi tương ứng" và trường hợp tiền hoàn bị âm (BR-02):**
   - *"Phần giá trị ưu đãi tương ứng"* được hiểu theo phương án nào:
     - *Phương án hiểu 1:* Thu hồi **toàn bộ phần tiền giảm giá đã phân bổ cho các sản phẩm người mua giữ lại** (vì phần hàng giữ lại không còn đủ điều kiện hưởng ưu đãi; phần giảm giá gắn với sản phẩm trả lại đã được trừ sẵn theo BR-01).
     - *Phương án hiểu 2:* Tính theo một tỷ lệ hoặc mức chênh lệch khác.
   - **Trường hợp biên:** Nếu số tiền khấu trừ hồi tố lớn hơn số tiền dự kiến hoàn của sản phẩm được trả (dẫn đến số tiền hoàn cuối cùng `< 0`), hệ thống xử lý thế nào (trả về `0`, chặn không cho trả hàng một phần, hay yêu cầu thu thêm từ người mua)?
4. **Hành vi khi trả hàng một phần nhiều lần trên cùng một đơn hàng:**
   - Hệ thống có cho phép tách nhiều lần yêu cầu trả hàng một phần trên cùng một đơn hàng hay chỉ cho phép 1 lần? Nếu cho phép nhiều lần và đến lần trả sau mới bị tụt xuống dưới ngưỡng tối thiểu, phần ưu đãi đã xử lý ở lần trả trước có bị khấu trừ hồi tố hay không?

### Mẫu 3

# Quy định nghiệp vụ: Hoàn tiền khi trả hàng một phần đối với đơn hàng đa sản phẩm có áp dụng mã giảm giá toàn đơn

## 1. Điều kiện áp dụng
Quy định này áp dụng khi đồng thời thỏa mãn các điều kiện sau:
- Đơn hàng gồm nhiều sản phẩm và có áp dụng mã giảm giá tính trên **tổng giá trị đơn hàng**.
- Người mua yêu cầu trả hàng và hoàn tiền cho **một hoặc một số sản phẩm** trong đơn hàng đó (trả hàng một phần).

## 2. Quy tắc nghiệp vụ

- **BR-01 — Tính tiền hoàn theo giá trị thực trả đã phân bổ giảm giá**
  - Hệ thống **không** tính tiền hoàn theo đơn giá niêm yết ban đầu của sản phẩm được trả.
  - Tiền hoàn cho từng sản phẩm **phải** dựa trên **số tiền người mua thực tế đã thanh toán** cho sản phẩm đó, sau khi đã phân bổ phần tiền giảm giá của mã ưu đãi theo tỷ lệ giá trị của từng sản phẩm trong đơn hàng.

- **BR-02 — Ngoại lệ: Khấu trừ hồi tố khi phần hàng giữ lại không đạt ngưỡng ưu đãi**
  - Nếu việc trả hàng một phần khiến tổng giá trị của **các sản phẩm còn lại** (người mua giữ lại) **thấp hơn ngưỡng tối thiểu** để đủ điều kiện hưởng ưu đãi của mã giảm giá đã dùng:
  - Hệ thống **phải khấu trừ hồi tố** phần giá trị ưu đãi tương ứng trước khi xác định số tiền hoàn trả cuối cùng.

- **BR-03 — Không hoàn lại mã giảm giá**
  - Mã giảm giá đã dùng cho đơn hàng có phát sinh trả hàng một phần **không được hoàn lại** vào tài khoản của người mua để tái sử dụng cho các giao dịch sau.

## 3. Điểm bỏ ngỏ cần chốt trước khi lập trình

Tài liệu gốc chưa đủ chi tiết ở các điểm sau (cần PO/Kinh doanh xác nhận để tránh suy diễn khi thiết kế và lập trình):

1. **Công thức khấu trừ hồi tố ở BR-02:**
   - Chưa chốt rõ *"phần giá trị ưu đãi tương ứng"* cần khấu trừ là:
     - **Phương án 1:** Thu hồi toàn bộ phần tiền giảm giá đã phân bổ cho các sản phẩm người mua **giữ lại** (do phần hàng giữ lại không còn đạt ngưỡng hưởng mã; khi đó tiền hoàn cuối = tiền thực trả của phần hàng trả − tiền giảm giá đã phân bổ cho phần hàng giữ lại, tương đương tổng tiền thực trả cả đơn − giá trị chưa áp mã của phần hàng giữ lại).
     - **Phương án 2:** Áp dụng mức ưu đãi thấp hơn theo bậc (nếu mã giảm giá có nhiều mức ngưỡng) hoặc quy tắc thu hồi khác.
2. **Giá trị làm căn cứ tính tỷ lệ phân bổ (BR-01) và kiểm tra ngưỡng tối thiểu (BR-02):**
   - Chưa làm rõ *"giá trị"* sản phẩm ở đây là **đơn giá niêm yết ban đầu** hay **giá bán thực tế trước khi áp mã toàn đơn** (trường hợp sản phẩm có chương trình giảm giá riêng).
3. **Trường hợp số tiền hoàn sau khấu trừ hồi tố ≤ 0:**
   - Chưa quy định hành vi hệ thống khi tiền ưu đãi bị khấu trừ hồi tố lớn hơn hoặc bằng số tiền thực trả của các sản phẩm yêu cầu hoàn: hoàn **0 đồng**, thu bù từ người mua, hay **chặn** yêu cầu trả hàng một phần.
4. **Quy tắc làm tròn và xử lý phần dư khi phân bổ giảm giá:**
   - Chưa quy định cách làm tròn số tiền lẻ khi chia tỷ lệ theo sản phẩm (hoặc theo từng đơn vị số lượng nếu một mặt hàng mua nhiều cái nhưng chỉ trả một phần) và cách phân bổ phần chênh lệch (nếu có) để khớp tổng giá trị mã giảm giá.
5. **Trường hợp trả hàng một phần nhiều lần trên cùng một đơn:**
   - Chưa quy định cách kiểm tra ngưỡng tối thiểu và khấu trừ hồi tố lũy kế nếu người mua thực hiện trả hàng một phần qua nhiều lần tách biệt trên cùng một đơn hàng.
6. **Các nội dung chưa có trong quy định gốc:**
   - Nguồn hiện tại **không quy định** về thời hạn hoàn tiền (số ngày xử lý), phương thức hoàn tiền và quy tắc xử lý phí vận chuyển (hoàn hay không hoàn phí vận chuyển, có tính phí vận chuyển vào ngưỡng tối thiểu của mã hay không). Nếu phạm vi triển khai cần các quy tắc này, phải bổ sung xác nhận riêng.

### Phiếu chấm nhanh của bạn

- Mẫu tự nhiên & dễ hiểu nhất: `...`
- Mẫu giữ đúng ý nhưng còn cứng / nặng từ ngữ gốc: `...`
- Ghi chú cảm nhận: `...`

---

## SR-06 — Tài liệu kỹ thuật: Chuyển đổi dự phòng CSDL (Failover) khi dùng sao chép bất đồng bộ

- **Người đọc mục tiêu:** Kỹ sư Backend & SRE / Vận hành hệ thống
- **Mục đích:** Trình bày rõ cơ chế, rủi ro mất dữ liệu (RPO > 0) khi failover từ Primary sang Replica chạy bất đồng bộ, cách xử lý transaction đang chạy dở và trạng thái kết nối ứng dụng.

### Văn bản gốc

```text
Trong kiến trúc cơ sở dữ liệu quan hệ triển khai theo mô hình một máy chủ chính (Primary) kết hợp với bản sao (Replica) sử dụng cơ chế sao chép bất đồng bộ (asynchronous replication), quá trình chuyển đổi dự phòng (failover) khi nút Primary gặp sự cố đòi hỏi sự đánh đổi trực tiếp giữa thời gian khôi phục khả năng ghi và tính toàn vẹn của dữ liệu phát sinh gần thời điểm sự cố. Do đặc thù của sao chép bất đồng bộ là nút Primary sẽ xác nhận hoàn tất giao dịch (commit) với ứng dụng ngay sau khi ghi nhận cục bộ mà không chờ nút Replica phản hồi đã lưu trữ nhật ký thay đổi (WAL/binlog), sự tồn tại của độ trễ sao chép (replication lag) dẫn đến hệ quả là những giao dịch đã được xác nhận thành công trên Primary ngay trước lúc xảy ra sự cố nhưng chưa kịp truyền sang Replica có thể bị thất thoát khi hệ thống tiến hành thăng cấp (promote) Replica lên đảm nhiệm vai trò Primary mới, đồng nghĩa với việc mục tiêu điểm khôi phục (RPO) lớn hơn 0. Song song đó, toàn bộ các giao dịch đang thực thi dở dang ở trạng thái chưa hoàn tất xác nhận (uncommitted) tại thời điểm chuyển đổi sẽ bị hệ thống thực hiện hoàn tác (rollback). Ngoài ra, trong khoảng thời gian diễn ra quá trình thăng cấp nút mới và cập nhật định tuyến kết nối hoặc connection pool, lớp ứng dụng có thể ghi nhận khoảng gián đoạn quyền ghi hoặc trạng thái chỉ đọc tạm thời. Cuối cùng, tại thời điểm máy chủ Primary ban đầu được khắc phục và khởi động lại, hệ thống tuyệt đối không được phép để máy chủ này tự động tiếp nhận lưu lượng ghi trở lại ngay trước khi thực hiện đồng bộ hoặc tái lập lại đúng vai trò nhằm ngăn chặn tình trạng phân mảnh quyền ghi đồng thời trên hai nút (split-brain) gây xung đột dữ liệu nghiêm trọng.
```

### Mẫu 1

**Failover trên mô hình Primary–Replica (Sao chép bất đồng bộ): Đánh đổi và Rủi ro vận hành**

Trong kiến trúc cơ sở dữ liệu quan hệ gồm một **Primary** và **Replica** dùng cơ chế sao chép bất đồng bộ (asynchronous replication), quá trình failover khi Primary gặp sự cố luôn đòi hỏi đánh đổi trực tiếp giữa thời gian khôi phục khả năng ghi và tính toàn vẹn của dữ liệu phát sinh gần thời điểm sự cố.

**Các rủi ro kỹ thuật cần kiểm soát khi vận hành:**

- **Thất thoát dữ liệu đã commit (`RPO > 0`):** Primary xác nhận hoàn tất giao dịch (`commit`) với ứng dụng ngay sau khi ghi cục bộ, không chờ Replica phản hồi đã lưu nhật ký thay đổi (WAL/binlog). Do tồn tại độ trễ sao chép (replication lag), các giao dịch đã `commit` trên Primary ngay trước sự cố nhưng chưa kịp truyền sang Replica có thể bị mất khi thăng cấp (`promote`) Replica lên làm Primary mới.
- **Hoàn tác giao dịch đang chạy (`rollback`):** Toàn bộ các giao dịch đang thực thi dở dang ở trạng thái chưa xác nhận (`uncommitted`) tại thời điểm chuyển đổi đều bị hệ thống `rollback`.
- **Gián đoạn quyền ghi hoặc chỉ đọc tạm thời:** Trong khoảng thời gian hệ thống thăng cấp nút mới và cập nhật định tuyến kết nối hoặc connection pool, lớp ứng dụng có thể ghi nhận tình trạng gián đoạn quyền ghi hoặc chuyển sang trạng thái chỉ đọc tạm thời.
- **Xung đột dữ liệu do `split-brain` khi khôi phục nút cũ:** Khi máy chủ Primary ban đầu được khắc phục và khởi động lại, hệ thống tuyệt đối không được để máy chủ này tự động tiếp nhận lưu lượng ghi trở lại trước khi thực hiện đồng bộ hoặc tái lập đúng vai trò. Quy định này nhằm ngăn tình trạng phân mảnh quyền ghi đồng thời trên hai nút (`split-brain`), gây xung đột dữ liệu nghiêm trọng.

### Mẫu 2

**Bối cảnh & Đánh đổi cốt lõi**
Trong kiến trúc cơ sở dữ liệu quan hệ gồm một nút **Primary** và **Replica** sử dụng cơ chế sao chép bất đồng bộ (asynchronous replication), khi Primary gặp sự cố, quá trình chuyển đổi dự phòng (failover) buộc phải đánh đổi trực tiếp giữa **thời gian khôi phục quyền ghi** và **tính toàn vẹn của dữ liệu** phát sinh sát thời điểm sự cố.

**Rủi ro và tác động khi failover**
- **Mất dữ liệu đã commit (RPO > 0):** Primary xác nhận hoàn tất giao dịch (commit) với ứng dụng ngay sau khi ghi cục bộ mà không chờ Replica phản hồi đã lưu nhật ký thay đổi (WAL/binlog). Do độ trễ sao chép (replication lag), các giao dịch vừa commit trên Primary ngay trước sự cố nhưng chưa kịp truyền sang Replica có thể bị mất khi promote Replica lên làm Primary mới.
- **Hủy giao dịch chưa hoàn tất (rollback):** Toàn bộ các giao dịch đang chạy dở dang ở trạng thái chưa xác nhận hoàn tất (uncommitted) tại thời điểm chuyển đổi đều bị hệ thống rollback.
- **Gián đoạn quyền ghi tạm thời ở lớp ứng dụng:** Trong thời gian promote Primary mới và cập nhật định tuyến kết nối hoặc connection pool, ứng dụng có thể gặp gián đoạn quyền ghi hoặc trạng thái chỉ đọc tạm thời.

**Yêu cầu bắt buộc khi khôi phục Primary cũ**
- **Phòng tránh split-brain:** Khi máy chủ Primary ban đầu được khắc phục và khởi động lại, tuyệt đối không để nút này tự động tiếp nhận lưu lượng ghi trở lại ngay. Phải đồng bộ dữ liệu hoặc tái lập lại đúng vai trò của nút này trước nhằm ngăn tình trạng hai nút cùng nhận quyền ghi đồng thời (split-brain) gây xung đột dữ liệu nghiêm trọng.

### Mẫu 3

Trong kiến trúc cơ sở dữ liệu quan hệ gồm một máy chủ **Primary** và bản sao (**Replica**) dùng cơ chế sao chép bất đồng bộ (asynchronous replication), quá trình **failover** khi Primary gặp sự cố luôn đòi hỏi đánh đổi trực tiếp giữa thời gian khôi phục quyền ghi và tính toàn vẹn dữ liệu phát sinh sát thời điểm lỗi.

Dưới đây là các tác động và rủi ro vận hành cần nắm khi failover diễn ra:

- **Mất dữ liệu đã xác nhận (RPO > 0):** Primary xác nhận hoàn tất giao dịch (commit) cho ứng dụng ngay sau khi ghi cục bộ mà không chờ Replica lưu xong nhật ký thay đổi (WAL/binlog). Do tồn tại độ trễ sao chép (replication lag), các giao dịch đã commit trên Primary ngay trước lúc gặp sự cố nhưng chưa kịp truyền sang Replica có thể bị mất khi Replica được thăng cấp (promote) lên làm Primary mới.
- **Hoàn tác giao dịch dở dang (rollback):** Toàn bộ các giao dịch đang thực thi nhưng chưa hoàn tất xác nhận (uncommitted) tại thời điểm chuyển đổi sẽ bị hệ thống thực hiện rollback.
- **Gián đoạn quyền ghi ở tầng ứng dụng:** Trong thời gian promote nút mới và cập nhật định tuyến kết nối hoặc connection pool, ứng dụng có thể gặp khoảng gián đoạn quyền ghi hoặc rơi vào trạng thái chỉ đọc tạm thời.
- **Nguy cơ split-brain khi Primary cũ hoạt động lại:** Khi máy chủ Primary ban đầu được khắc phục và khởi động lại, hệ thống tuyệt đối không được để nút này tự động nhận lưu lượng ghi trước khi đồng bộ dữ liệu hoặc tái lập đúng vai trò. Nếu không chặn bước này, cả hai nút sẽ cùng tiếp nhận ghi đồng thời (split-brain), gây xung đột dữ liệu nghiêm trọng.

### Phiếu chấm nhanh của bạn

- Mẫu tự nhiên & dễ hiểu nhất: `...`
- Mẫu giữ đúng ý nhưng còn cứng / nặng từ ngữ gốc: `...`
- Ghi chú cảm nhận: `...`

---

## SR-07 — Văn bản dài nhiều thông tin liên quan: Quy trình tiếp nhận và duyệt hoàn tiền khiếu nại giao thiếu/hư hỏng (4 đoạn liên kết)

- **Người đọc mục tiêu:** Nhân viên CSKH, Bộ phận Kho và Quản lý ca trực
- **Mục đích:** Biến một tài liệu vận hành 4 đoạn dài dòng thành hướng dẫn dễ tra cứu theo bước, tách rõ điều kiện thời hạn, phân quyền duyệt < 500.000đ vs >= 500.000đ và ngoại lệ hàng tươi sống/dễ vỡ.

### Văn bản gốc

```text
Tài liệu hướng dẫn quy trình tiếp nhận và giải quyết các yêu cầu khiếu nại phát sinh đối với đơn hàng gặp sự cố giao thiếu sản phẩm hoặc hư hỏng hàng hóa trong quá trình vận chuyển

Về điều kiện tiếp nhận ban đầu, khách hàng có nhu cầu thực hiện khiếu nại liên quan đến tình trạng thiếu hụt số lượng hoặc hư hỏng vật lý đối với đơn hàng cần phải tiến hành gửi yêu cầu lên hệ thống trong khoảng thời gian giới hạn không vượt quá 48 giờ kể từ thời điểm đơn hàng được hệ thống ghi nhận chuyển sang trạng thái Đã giao thành công. Mọi hồ sơ khiếu nại gửi sau mốc thời gian 48 giờ nêu trên sẽ bị hệ thống thực hiện từ chối tiếp nhận một cách tự động, ngoại trừ trường hợp ngoại lệ có văn bản hoặc ghi nhận xác nhận từ phía đơn vị vận chuyển về việc đã xảy ra sai sót trong khâu cập nhật trạng thái giao hàng thực tế lên hệ thống.

Về thành phần chứng từ bắt buộc đính kèm theo yêu cầu, người gửi khiếu nại phải thực hiện cung cấp đầy đủ hình ảnh chụp rõ tình trạng bên ngoài lẫn bên trong kiện hàng cùng với phiếu giao hàng đi kèm. Riêng đối với các đơn hàng có chứa sản phẩm thuộc nhóm danh mục hàng tươi sống hoặc hàng hóa có tính chất dễ vỡ, quy trình quy định điều kiện bắt buộc bổ sung là khách hàng phải đính kèm thêm đoạn video ghi lại toàn bộ quá trình mở hộp một cách liền mạch và không có dấu hiệu cắt ghép chỉnh sửa.

Về phân cấp thẩm quyền kiểm tra và phê duyệt chi trả khoản tiền hoàn, quy trình được phân chia theo ngưỡng giá trị của yêu cầu khiếu nại cụ thể. Đối với các yêu cầu có giá trị đề nghị hoàn trả ở mức dưới 500.000đ, nhân viên thuộc bộ phận Chăm sóc khách hàng (CSKH) được quyền trực tiếp tiến hành rà soát tính hợp lệ của bộ chứng từ bằng chứng đã nộp và thực hiện phê duyệt lệnh hoàn tiền ngay trong ca làm việc hiện tại. Ngược lại, đối với các yêu cầu có giá trị đề nghị hoàn trả từ 500.000đ trở lên, nhân viên CSKH không tự ý phê duyệt mà phải tiến hành chuyển tiếp hồ sơ sang Bộ phận Kho để bộ phận này thực hiện việc kiểm tra đối chiếu lại dữ liệu camera tại khâu đóng gói đơn hàng làm căn cứ trình lên Quản lý ca xem xét phê duyệt cuối cùng.

Về thời hạn phối hợp xử lý giữa các bộ phận liên quan trong trường hợp phải chuyển tiếp hồ sơ giá trị cao, Bộ phận Kho có trách nhiệm hoàn tất quá trình kiểm tra dữ liệu camera đóng gói và gửi phản hồi kết quả xác minh về cho luồng xử lý trong khoảng thời gian tối đa không vượt quá 24 giờ làm việc tính từ thời điểm tiếp nhận thông tin chuyển tiếp từ phía nhân viên CSKH.
```

### Mẫu 1

# Quy trình tiếp nhận và xử lý khiếu nại giao thiếu hoặc hư hỏng hàng hóa

**Phạm vi áp dụng:** Các đơn hàng bị giao thiếu sản phẩm hoặc hư hỏng hàng hóa trong quá trình vận chuyển.

## 1. Điều kiện và thời hạn tiếp nhận

- **Thời hạn gửi yêu cầu:** Khách hàng phải gửi khiếu nại trên hệ thống trong vòng **48 giờ** kể từ thời điểm hệ thống ghi nhận đơn hàng chuyển sang trạng thái **Đã giao thành công**.
- **Quá thời hạn 48 giờ:** Hệ thống tự động từ chối tiếp nhận yêu cầu.
- **Trường hợp ngoại lệ:** Vẫn xem xét tiếp nhận nếu có văn bản hoặc ghi nhận xác nhận từ đơn vị vận chuyển về việc cập nhật sai trạng thái giao hàng thực tế lên hệ thống.

## 2. Bằng chứng bắt buộc khách hàng phải đính kèm

- **Với mọi đơn hàng khiếu nại:**
  - Ảnh chụp rõ tình trạng bên ngoài kiện hàng.
  - Ảnh chụp rõ tình trạng bên trong kiện hàng.
  - Ảnh chụp phiếu giao hàng đi kèm.
- **Bổ sung với đơn hàng có sản phẩm tươi sống hoặc hàng dễ vỡ:**
  - Video quay toàn bộ quá trình mở hộp liền mạch, không có dấu hiệu cắt ghép hoặc chỉnh sửa.

## 3. Phân cấp kiểm tra, phê duyệt và thời hạn xử lý

| Giá trị đề nghị hoàn tiền | Bộ phận CSKH | Bộ phận Kho | Quản lý ca | Thời hạn xử lý |
|---|---|---|---|---|
| **Dưới 500.000đ (`< 500.000đ`)** | Kiểm tra tính hợp lệ của bộ chứng từ/bằng chứng đã nộp và trực tiếp phê duyệt lệnh hoàn tiền. | Không tham gia | Không tham gia | Hoàn tất ngay trong ca làm việc hiện tại. |
| **Từ 500.000đ trở lên (`>= 500.000đ`)** | **Không tự phê duyệt.** Chuyển tiếp hồ sơ sang Bộ phận Kho. | Kiểm tra, đối chiếu dữ liệu camera tại khâu đóng gói đơn hàng và gửi kết quả xác minh về luồng xử lý. | Căn cứ kết quả xác minh của Bộ phận Kho để xem xét, phê duyệt cuối cùng. | Bộ phận Kho phản hồi kết quả xác minh trong tối đa **24 giờ làm việc** kể từ lúc nhận chuyển tiếp từ CSKH. |

### Mẫu 2

# Quy trình tiếp nhận và giải quyết khiếu nại giao thiếu hoặc hư hỏng hàng hóa

**Phạm vi áp dụng:** Yêu cầu khiếu nại của khách hàng đối với đơn hàng gặp sự cố **giao thiếu sản phẩm** hoặc **hư hỏng vật lý hàng hóa** trong quá trình vận chuyển.

---

## 1. Điều kiện tiếp nhận và ngoại lệ quá hạn

- **Thời hạn gửi khiếu nại:** Khách hàng phải gửi yêu cầu lên hệ thống trong vòng **không quá 48 giờ** (`<= 48 giờ`) kể từ thời điểm hệ thống ghi nhận đơn hàng chuyển sang trạng thái **Đã giao thành công**.
- **Từ chối tự động:** Mọi hồ sơ khiếu nại gửi sau mốc 48 giờ bị hệ thống tự động từ chối tiếp nhận.
- **Ngoại lệ:** Không bị từ chối theo mốc 48 giờ nếu có **văn bản hoặc ghi nhận xác nhận từ đơn vị vận chuyển** về việc xảy ra sai sót khi cập nhật trạng thái giao hàng thực tế lên hệ thống.

---

## 2. Chứng từ bắt buộc đính kèm

| Nhóm đơn hàng | Chứng từ khách hàng phải cung cấp |
|---|---|
| **Mọi đơn hàng khiếu nại** | 1. Ảnh chụp rõ tình trạng **bên ngoài** kiện hàng.<br>2. Ảnh chụp rõ tình trạng **bên trong** kiện hàng.<br>3. **Phiếu giao hàng** đi kèm. |
| **Đơn hàng có sản phẩm tươi sống hoặc dễ vỡ** *(bổ sung bắt buộc)* | Toàn bộ chứng từ trên **và** **video quay toàn bộ quá trình mở hộp** (liền mạch, không có dấu hiệu cắt ghép hay chỉnh sửa). |

---

## 3. Phân quyền xử lý, phê duyệt hoàn tiền và thời hạn phối hợp

> **Lưu ý phân quyền:** Đối với khiếu nại có giá trị đề nghị hoàn trả **từ 500.000đ trở lên**, nhân viên CSKH **không tự ý phê duyệt** mà phải chuyển tiếp hồ sơ sang Bộ phận Kho.

| Giá trị đề nghị hoàn trả | Nhân viên CSKH | Bộ phận Kho | Quản lý ca | Thời hạn xử lý |
|---|---|---|---|---|
| **Dưới 500.000đ**<br>(`< 500.000đ`) | Rà soát tính hợp lệ của bộ chứng từ bằng chứng đã nộp và trực tiếp phê duyệt lệnh hoàn tiền. | — | — | Thực hiện ngay trong **ca làm việc hiện tại**. |
| **Từ 500.000đ trở lên**<br>(`>= 500.000đ`) | Tiếp nhận yêu cầu và chuyển tiếp hồ sơ sang Bộ phận Kho. | Kiểm tra, đối chiếu dữ liệu **camera tại khâu đóng gói** đơn hàng; gửi phản hồi kết quả xác minh về luồng xử lý làm căn cứ trình Quản lý ca. | Xem xét căn cứ xác minh từ Bộ phận Kho và **phê duyệt cuối cùng**. | Bộ phận Kho hoàn tất kiểm tra và gửi phản hồi trong tối đa **24 giờ làm việc** (`<= 24 giờ làm việc`) kể từ thời điểm tiếp nhận thông tin chuyển tiếp từ CSKH. |

---

## 4. Điểm chưa quy định trong tài liệu gốc (cần làm rõ khi triển khai)

- **Cách tiếp nhận hồ sơ ngoại lệ quá 48 giờ:** Tài liệu chưa nêu quy trình tiếp nhận thủ công hoặc mở lại luồng trên hệ thống khi khách có xác nhận sai sót từ đơn vị vận chuyển nhưng hồ sơ đã qua mốc 48 giờ.
- **Bước sau phản hồi của Kho (hồ sơ `>= 500.000đ`) và phương án từ chối/bổ sung:** Tài liệu chưa quy định thời hạn xem xét của Quản lý ca, đầu mối thao tác lệnh hoàn tiền sau khi Quản lý ca phê duyệt, cũng như cách xử lý khi bộ chứng từ không hợp lệ hoặc dữ liệu camera đóng gói không khớp với khiếu nại.

### Mẫu 3

# Quy trình tiếp nhận và xử lý khiếu nại giao thiếu hoặc hư hỏng hàng hóa

**Phạm vi áp dụng:** Đơn hàng gặp sự cố **giao thiếu sản phẩm** hoặc **hư hỏng hàng hóa trong quá trình vận chuyển**.  
**Đối tượng thực hiện:** Nhân viên Chăm sóc khách hàng (CSKH), Bộ phận Kho và Quản lý ca.

---

## 1. Điều kiện tiếp nhận khiếu nại

- **Thời hạn gửi yêu cầu:** Không quá **48 giờ** kể từ thời điểm hệ thống ghi nhận đơn hàng chuyển sang trạng thái **Đã giao thành công**.
- **Quá thời hạn:** Hệ thống tự động từ chối tiếp nhận mọi hồ sơ khiếu nại gửi sau mốc **48 giờ**.
- **Ngoại lệ:** Không từ chối tiếp nhận nếu có **văn bản hoặc ghi nhận xác nhận từ đơn vị vận chuyển** về việc đã xảy ra sai sót khi cập nhật trạng thái giao hàng thực tế lên hệ thống.

---

## 2. Chứng từ bắt buộc đính kèm

| Loại đơn hàng | Chứng từ khách hàng phải cung cấp |
|---|---|
| **Mọi đơn hàng** | - Hình ảnh chụp rõ tình trạng **bên ngoài** kiện hàng<br>- Hình ảnh chụp rõ tình trạng **bên trong** kiện hàng<br>- **Phiếu giao hàng** đi kèm |
| **Đơn có sản phẩm thuộc nhóm hàng tươi sống hoặc hàng dễ vỡ** *(bổ sung thêm ngoài các mục trên)* | - **Video** ghi lại toàn bộ quá trình mở hộp, đảm bảo **liền mạch** và **không có dấu hiệu cắt ghép, chỉnh sửa** |

---

## 3. Phân cấp kiểm tra, phê duyệt hoàn tiền và thời hạn phối hợp

> **Lưu ý cho CSKH:** Không tự ý phê duyệt các yêu cầu có giá trị đề nghị hoàn trả từ **500.000đ trở lên**.

| Giá trị đề nghị hoàn trả | Quy trình & Trách nhiệm xử lý | Thời hạn xử lý |
|---|---|---|
| **Dưới 500.000đ** (`< 500.000đ`) | **CSKH:** Trực tiếp rà soát tính hợp lệ của bộ chứng từ bằng chứng đã nộp và phê duyệt lệnh hoàn tiền. | **Ngay trong ca làm việc hiện tại** |
| **Từ 500.000đ trở lên** (`>= 500.000đ`) | **1. CSKH:** Chuyển tiếp hồ sơ sang Bộ phận Kho.<br>**2. Bộ phận Kho:** Kiểm tra, đối chiếu dữ liệu camera tại khâu đóng gói đơn hàng và gửi phản hồi kết quả xác minh về luồng xử lý làm căn cứ trình duyệt.<br>**3. Quản lý ca:** Căn cứ kết quả xác minh từ Bộ phận Kho để xem xét và phê duyệt cuối cùng. | **Bộ phận Kho:** Tối đa **24 giờ làm việc** kể từ thời điểm tiếp nhận thông tin chuyển tiếp từ CSKH |

### Phiếu chấm nhanh của bạn

- Mẫu tự nhiên & dễ hiểu nhất: `...`
- Mẫu giữ đúng ý nhưng còn cứng / nặng từ ngữ gốc: `...`
- Ghi chú cảm nhận: `...`

---
