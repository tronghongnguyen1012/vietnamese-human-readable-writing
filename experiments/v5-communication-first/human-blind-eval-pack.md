# Gói Đánh giá Mù Chiều Hiểu & Truyền đạt — ViWrite V5 (Layer 2 Human Blind Evaluation)

Tài liệu này dùng để đánh giá mù hoàn toàn (Human Blind Evaluation) chất lượng truyền đạt (Layer 2) trên **13 tình huống** (`SR-01..SR-07` hồi quy + `V5-01..V5-06` mới chưa từng thấy).

## Hướng dẫn chấm điểm (Anti-bias & 2-Layer Protocol)

1. **Không có nhãn nhánh hay model:** Tên các mẫu (`Mẫu 1..Mẫu 5` hoặc `Mẫu 6`) đã được **xáo trộn cân bằng theo vị trí** giữa các ca (không có phương án nào luôn nằm ở `Mẫu 1`). Bảng giải mã được niêm phong riêng tại [human-blind-key.json](human-blind-key.json) — chỉ mở sau khi chấm xong.
2. **Cách đọc khuyến nghị:** Đọc **Ngữ cảnh gốc** -> đọc **Câu hỏi kiểm tra khả năng hiểu (Comprehension Check)** -> đọc từng `Mẫu` như một người nhận thực thụ (end-user / Dev / PM / CSKH / nhân viên).
3. **Thang tiêu chí Layer 2 (1–5 điểm, 5 = xuất sắc):**
   - **C1. Hiểu nhanh ý chính:** Mở ra đọc là nắm ngay việc gì xảy ra / cần làm gì?
   - **C2. Tự nhiên như người viết:** Trôi chảy, đúng giọng tiếng Việt bản ngữ, không có mùi dịch word-by-word hay văn phong hành chính sáo rỗng.
   - **C3. Tổ chức thông tin hợp lý:** Ý quan trọng/hành động đặt đúng chỗ, dễ quét bằng mắt, không nhảy ý.
   - **C4. Đúng đối tượng & mục đích:** Hợp người đọc (end-user không bị nhồi thuật ngữ hệ thống hay ghi chú nội bộ; BA/Dev đủ edge case & `[Chưa chốt]`).
   - **C5. Gọn nhưng không mất ý:** Bỏ được chữ thừa nhưng vẫn trả lời trọn vẹn các câu hỏi Comprehension Check.
   - **C6. Ít phải đọc lại để hiểu:** Đọc một lượt là thông suốt ngay, không vấp.

---

## Ca SR-01 — Thông báo dịch vụ

- **Tiêu đề / Chủ đề:** Thông báo tối ưu hóa cơ chế vận hành và đồng bộ tài khoản (Seed Case)
- **Đối tượng đọc:** Người dùng cuối của nền tảng
- **Mục đích giao tiếp:** Hiểu ngay sắp có thay đổi gì về gia hạn & đồng bộ tài khoản, tác động khi thanh toán liên kết chưa đồng bộ, ngoại lệ cho tài khoản cũ và việc người dùng cần kiểm tra ngay.

### Yêu cầu & Văn bản nguồn

```text
Viết lại đoạn thông báo sau sang tiếng Việt rõ ràng, dễ hiểu cho người dùng cuối, giữ nguyên toàn bộ ý nghĩa, ngoại lệ và mức độ chắc chắn của bản gốc (không tự thêm thông tin không có trong nguồn):

Thông báo về việc tối ưu hóa cơ chế vận hành và nâng cấp trải nghiệm đồng bộ hóa tài khoản

Trong bối cảnh không ngừng nỗ lực nâng cao chất lượng dịch vụ nhằm kiến tạo một hệ sinh thái tương tác liền mạch và tối ưu hóa giá trị dài hạn cho người dùng, chúng tôi trân trọng thông báo về việc triển khai lộ trình tái cấu trúc cơ chế quản trị phiên truy cập và luồng xử lý gia hạn tự động trên nền tảng.

Theo đó, kể từ chu kỳ chuyển đổi sắp tới, việc duy trì tính liên tục của các gói dịch vụ đang ở trạng thái kích hoạt sẽ không còn được thực thi thông qua phương thức ghi nhận mặc định trước đây, mà sẽ được điều phối chuyển sang mô hình xác thực đa tầng có điều kiện. Trong trường hợp các thiết lập liên quan đến phương thức thanh toán liên kết chưa đạt được trạng thái đồng bộ hóa đầy đủ tại thời điểm hệ thống tiến hành đối soát định kỳ, quá trình kích hoạt lại quyền truy cập có thể ghi nhận sự gián đoạn cục bộ hoặc phát sinh trạng thái tạm treo đối với một số tính năng nâng cao cho đến khi các điều kiện tiên quyết được hoàn tất xác minh lại.

Đồng thời, đối với các tài khoản thuộc diện chuyển tiếp từ phiên bản lưu trữ cũ, dữ liệu phát sinh trong khoảng thời gian giao thoa giữa hai cơ chế vận hành sẽ được xử lý theo quy tắc ưu tiên bất đồng bộ nhằm giảm thiểu rủi ro xung đột thông tin, ngoại trừ các trường hợp đã chủ động thiết lập giới hạn truy xuất thủ công trước mốc triển khai. Để đảm bảo hành trình trải nghiệm không bị ảnh hưởng ngoài mong muốn, khuyến nghị quý người dùng chủ động rà soát tính tương thích của cấu hình hiện tại và thực hiện các điều chỉnh phù hợp theo định hướng mới trong thời gian sớm nhất.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Sau thay đổi sắp tới, gói dịch vụ đang kích hoạt sẽ duy trì bằng cơ chế nào thay cho cách mặc định cũ?
- 2. Nếu phương thức thanh toán liên kết chưa đồng bộ đủ lúc hệ thống đối soát định kỳ, điều gì **có thể** xảy ra — chắc chắn mất hoàn toàn quyền truy cập hay có thể gián đoạn cục bộ / tạm treo một số tính năng nâng cao?
- 3. Nhóm tài khoản chuyển từ bản lưu trữ cũ nào được miễn áp dụng quy tắc ưu tiên bất đồng bộ?

### SR-01 — Mẫu 1

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

---

### SR-01 — Mẫu 2

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

---

### SR-01 — Mẫu 3

**Thông báo cập nhật cơ chế vận hành và đồng bộ tài khoản**

Để nâng cao chất lượng dịch vụ, mang lại trải nghiệm liền mạch và tối ưu giá trị lâu dài cho bạn, chúng tôi sẽ thay đổi cơ chế quản lý phiên truy cập và quy trình gia hạn tự động trên nền tảng.

Từ chu kỳ chuyển đổi sắp tới, các gói dịch vụ đang hoạt động sẽ không còn được duy trì theo cách ghi nhận mặc định như trước. Thay vào đó, hệ thống sẽ chuyển sang áp dụng mô hình xác thực đa tầng có điều kiện.

Lưu ý về thanh toán: Nếu các thiết lập liên quan đến phương thức thanh toán liên kết chưa được đồng bộ đầy đủ tại thời điểm hệ thống đối soát định kỳ, quá trình kích hoạt lại quyền truy cập có thể bị gián đoạn cục bộ, hoặc một số tính năng nâng cao có thể bị tạm treo cho đến khi các điều kiện yêu cầu được xác minh lại hoàn tất.

Ngoài ra, đối với các tài khoản chuyển tiếp từ phiên bản lưu trữ cũ, dữ liệu phát sinh trong thời gian chuyển giao giữa hai cơ chế vận hành sẽ được xử lý theo quy tắc ưu tiên bất đồng bộ để giảm nguy cơ xung đột thông tin — ngoại trừ các trường hợp đã chủ động thiết lập giới hạn truy xuất thủ công trước mốc triển khai.

Để tránh ảnh hưởng ngoài ý muốn đến quá trình sử dụng, chúng tôi khuyến nghị bạn chủ động kiểm tra tính tương thích của cấu hình hiện tại và điều chỉnh cho phù hợp với cơ chế mới trong thời gian sớm nhất.

---

### SR-01 — Mẫu 4

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

---

### SR-01 — Mẫu 5

**Thông báo cập nhật cơ chế vận hành, gia hạn tự động và đồng bộ hóa tài khoản**

Để nâng cao chất lượng dịch vụ và mang lại trải nghiệm liền mạch, lâu dài hơn, chúng tôi xin thông báo kế hoạch điều chỉnh cơ chế quản lý phiên truy cập và quy trình gia hạn tự động trên nền tảng.

Từ chu kỳ chuyển đổi sắp tới, việc duy trì liên tục các gói dịch vụ đang hoạt động sẽ không còn áp dụng cách ghi nhận mặc định như trước, mà chuyển sang mô hình xác thực đa tầng có điều kiện.

Nếu các thiết lập liên quan đến phương thức thanh toán liên kết chưa được đồng bộ đầy đủ tại thời điểm hệ thống đối soát định kỳ, quá trình kích hoạt lại quyền truy cập có thể bị gián đoạn cục bộ hoặc một số tính năng nâng cao có thể bị tạm ngưng cho đến khi các điều kiện tiên quyết được xác minh lại hoàn tất.

Đồng thời, với các tài khoản thuộc diện chuyển tiếp từ phiên bản lưu trữ cũ, dữ liệu phát sinh trong thời gian giao thoa giữa hai cơ chế vận hành sẽ được xử lý theo quy tắc ưu tiên bất đồng bộ nhằm giảm rủi ro xung đột thông tin, ngoại trừ các trường hợp đã chủ động thiết lập giới hạn truy xuất thủ công trước mốc triển khai.

Để tránh trải nghiệm bị ảnh hưởng ngoài ý muốn, bạn nên sớm kiểm tra lại mức độ tương thích của cấu hình hiện tại và thực hiện các điều chỉnh phù hợp theo cơ chế mới.

---

### SR-01 — Mẫu 6

**Thông báo cập nhật cơ chế đồng bộ tài khoản, phiên truy cập và gia hạn tự động**

Nhằm nâng cao chất lượng dịch vụ, giữ trải nghiệm tương tác liền mạch và mang lại giá trị lâu dài, chúng tôi thông báo triển khai lộ trình thay đổi cách quản lý phiên truy cập và quy trình gia hạn tự động trên nền tảng.

**Thay đổi chính và ảnh hưởng có thể gặp**

Từ chu kỳ chuyển đổi sắp tới, để duy trì liên tục các gói dịch vụ đang kích hoạt, hệ thống sẽ không còn dùng phương thức ghi nhận mặc định như trước mà chuyển sang mô hình xác thực nhiều lớp có điều kiện.

Nếu các thiết lập liên quan đến phương thức thanh toán liên kết chưa đồng bộ đầy đủ tại thời điểm hệ thống đối soát định kỳ, quá trình kích hoạt lại quyền truy cập có thể bị gián đoạn cục bộ hoặc một số tính năng nâng cao có thể bị tạm ngưng cho đến khi các điều kiện bắt buộc được xác minh lại hoàn tất.

**Lưu ý cho tài khoản chuyển tiếp từ phiên bản lưu trữ cũ**

Với các tài khoản thuộc diện chuyển tiếp từ phiên bản lưu trữ cũ, dữ liệu phát sinh trong thời gian chuyển giao giữa hai cơ chế vận hành sẽ được xử lý theo quy tắc ưu tiên bất đồng bộ nhằm giảm rủi ro xung đột thông tin — ngoại trừ những trường hợp đã chủ động thiết lập giới hạn truy xuất thủ công trước mốc triển khai.

**Việc bạn nên làm**

Để tránh ảnh hưởng ngoài ý muốn đến quá trình sử dụng, chúng tôi khuyến nghị bạn chủ động kiểm tra tính tương thích của cấu hình hiện tại và sớm điều chỉnh cho phù hợp với cơ chế mới.

---

### Phiếu chấm nhanh SR-01

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |
| Mẫu 6 | | | | | | | |

- **Lựa chọn tốt nhất cho SR-01:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca SR-02 — Thông báo dịch vụ

- **Tiêu đề / Chủ đề:** Thông báo điều chỉnh chính sách dọn dẹp tệp đính kèm không phát sinh truy cập
- **Đối tượng đọc:** Người dùng nền tảng quản lý công việc
- **Mục đích giao tiếp:** Nắm được quy tắc tự động xóa tệp đính kèm sau 180 ngày không truy cập, mốc nhắc trước 15 ngày, trường hợp ngoại lệ được giữ lại và việc cần làm để không mất dữ liệu.

### Yêu cầu & Văn bản nguồn

```text
Viết lại thông báo dịch vụ dưới đây bằng tiếng Việt tự nhiên, rõ ràng để người dùng đọc lướt vẫn nắm ngay được điều gì sắp thay đổi, ngoại lệ nào được giữ lại và cần làm gì để tránh mất tệp (giữ nguyên toàn bộ số ngày, điều kiện và không tự thêm thông tin ngoài nguồn):

Thông báo về việc áp dụng cơ chế chuẩn hóa vòng đời lưu trữ đối với các tệp đính kèm không phát sinh hoạt động truy xuất

Nhằm mục tiêu nâng cao hiệu suất vận hành tài nguyên hạ tầng cũng như tối ưu hóa dung lượng lưu trữ khả dụng cho toàn bộ người dùng thuộc gói miễn phí và gói tiêu chuẩn, kể từ tháng tới hệ thống sẽ tiến hành kích hoạt quy trình tự động điều chuyển vòng đời đối với các tệp tin đính kèm không ghi nhận tương tác. Cụ thể, những tệp tin không phát sinh bất kỳ lượt mở xem hay tải xuống nào trong khoảng thời gian 180 ngày liên tiếp sẽ được tự động đưa vào khu vực thùng rác hệ thống, trước khi bị tiến hành thanh lọc vĩnh viễn sau 30 ngày tiếp theo nếu chủ sở hữu không thực hiện thao tác khôi phục.

Trước thời điểm chuyển trạng thái vào thùng rác 15 ngày, hệ thống sẽ thực hiện gửi thư điện tử cảnh báo tới địa chỉ liên hệ đã đăng ký. Tuy nhiên, quy định tự động xử lý nêu trên sẽ không áp dụng đối với các tệp được sắp xếp trong thư mục gắn nhãn Lưu trữ cố định (Pinned Archive) hoặc thuộc phạm vi tài khoản đang kích hoạt chế độ khóa bảo toàn pháp lý (Legal Hold). Khuyến nghị người dùng chủ động kiểm tra lại các tệp dữ liệu quan trọng và thực hiện thao tác phân loại phù hợp nhằm hạn chế nguy cơ thất thoát dữ liệu ngoài ý muốn.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Gói nào bị áp dụng quy tắc tự động dọn dẹp sau 180 ngày không hoạt động?
- 2. Người dùng được báo trước bao nhiêu ngày trước khi chuyển vào thùng rác, và có bao nhiêu ngày để khôi phục trước khi bị xóa vĩnh viễn?
- 3. Hai ngoại lệ nào giúp dữ liệu không bị chuyển sang trạng thái chờ xóa tự động?

### SR-02 — Mẫu 1

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

---

### SR-02 — Mẫu 2

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

---

### SR-02 — Mẫu 3

**Thông báo: Tự động dọn dẹp tệp đính kèm không sử dụng từ tháng tới**

Để tối ưu dung lượng lưu trữ khả dụng và nâng cao hiệu suất vận hành, từ tháng tới, hệ thống sẽ tự động xử lý các tệp đính kèm không có tương tác đối với người dùng thuộc **gói miễn phí** và **gói tiêu chuẩn**.

**Điều gì sắp thay đổi?**
- **Sau 180 ngày liên tiếp** không có bất kỳ lượt mở xem hay tải xuống nào, tệp đính kèm sẽ tự động được chuyển vào thùng rác.
- **Trước khi chuyển vào thùng rác 15 ngày**, hệ thống sẽ gửi email cảnh báo đến địa chỉ liên hệ đã đăng ký.
- **Sau 30 ngày tiếp theo** trong thùng rác, nếu chủ sở hữu không khôi phục, tệp sẽ bị xóa vĩnh viễn.

**Ngoại lệ được giữ lại (không bị tự động xử lý)**
Quy định trên không áp dụng nếu tệp thuộc một trong các trường hợp sau:
- Được sắp xếp trong thư mục gắn nhãn **Lưu trữ cố định (Pinned Archive)**; hoặc
- Thuộc tài khoản đang bật chế độ **khóa bảo toàn pháp lý (Legal Hold)**.

**Cần làm gì để tránh mất tệp?**
- Chủ động kiểm tra lại các tệp dữ liệu quan trọng và phân loại phù hợp (chẳng hạn đưa vào thư mục **Lưu trữ cố định (Pinned Archive)**).
- Theo dõi email cảnh báo tại địa chỉ liên hệ đã đăng ký; nếu tệp đã vào thùng rác, cần thực hiện khôi phục trước khi hết 30 ngày để tránh bị xóa vĩnh viễn.

---

### SR-02 — Mẫu 4

**Thông báo: Tự động dọn dẹp tệp đính kèm không dùng đến từ tháng tới**

Từ **tháng tới**, hệ thống sẽ tự động đưa vào thùng rác và xóa vĩnh viễn các tệp đính kèm lâu ngày không có tương tác đối với người dùng **gói miễn phí** và **gói tiêu chuẩn**, nhằm nâng cao hiệu suất vận hành và tối ưu dung lượng lưu trữ khả dụng.

**Những thay đổi sắp áp dụng**
- **Sau 180 ngày liên tiếp** không có bất kỳ lượt mở xem hay tải xuống nào, tệp đính kèm sẽ tự động được chuyển vào thùng rác hệ thống.
- **Trước khi chuyển vào thùng rác 15 ngày**, hệ thống sẽ gửi email cảnh báo đến địa chỉ liên hệ bạn đã đăng ký.
- **Sau 30 ngày tiếp theo** trong thùng rác, nếu bạn không khôi phục, tệp sẽ bị xóa vĩnh viễn.

**Các trường hợp được giữ lại (không áp dụng quy định này)**
- Tệp nằm trong thư mục gắn nhãn **Lưu trữ cố định (Pinned Archive)**; hoặc
- Tệp thuộc tài khoản đang bật chế độ **khóa bảo toàn pháp lý (Legal Hold)**.

**Bạn cần làm gì để tránh mất tệp?**
- Chủ động kiểm tra lại các tệp dữ liệu quan trọng và phân loại phù hợp (chẳng hạn đưa vào thư mục **Lưu trữ cố định (Pinned Archive)**) để tránh mất dữ liệu ngoài ý muốn.
- Theo dõi email cảnh báo gửi trước 15 ngày và khôi phục tệp trong vòng 30 ngày nếu tệp đã được chuyển vào thùng rác.

---

### SR-02 — Mẫu 5

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

---

### Phiếu chấm nhanh SR-02

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho SR-02:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca SR-03 — Giao tiếp công việc

- **Tiêu đề / Chủ đề:** Tin nhắn nhóm dự án báo dời lịch phát hành và phân công FE/BE/QA
- **Đối tượng đọc:** Đội kỹ thuật FE, BE, QA trên Slack/Teams
- **Mục đích giao tiếp:** Nắm ngay kết luận dời lịch release từ 14:00 thứ Năm sang 10:00 thứ Hai tuần sau, hiểu lý do ngắn gọn và biết rõ từng team phải làm gì trước mốc mới.

### Yêu cầu & Văn bản nguồn

```text
Viết lại tin nhắn dưới đây thành thông báo rõ ràng, đi thẳng vào quyết định và phân việc rạch ròi cho từng team FE, BE, QA khi gửi lên nhóm Teams/Slack (giữ nguyên toàn bộ mốc giờ, điều kiện và nội dung việc, không tự bịa thêm tên người hay kênh phụ):

Chào mọi người trong nhóm dự án 2.4, lời đầu tiên mình xin cảm ơn sự cố gắng của tất cả anh chị em trong sprint vừa qua để kịp hoàn thành phần lớn các hạng mục đúng tiến độ đề ra. Tuy nhiên, do một số vướng mắc khách quan phát sinh từ phía đối tác ngân hàng trong việc bàn giao môi trường sandbox cho API đối soát thanh toán bị chậm sang tận chiều thứ Sáu nên sau khi trao đổi nhanh với anh lead kỹ thuật và team sản phẩm, tụi mình nhận thấy nếu vẫn giữ kế hoạch phát hành vào 14:00 thứ Năm tuần này sẽ tiềm ẩn rất nhiều rủi ro cho luồng thanh toán thực tế. Vì vậy, lịch phát hành phiên bản 2.4 dự kiến sẽ được điều chỉnh lùi sang 10:00 sáng thứ Hai tuần sau. Để tận dụng khoảng thời gian đệm này một cách hiệu quả nhất, nhờ phía Backend hỗ trợ hoàn thiện phần tích hợp mock fallback và triển khai lên môi trường staging chậm nhất trước 17:00 thứ Sáu; trong khi đó, bên Frontend vẫn giữ nguyên nhánh giao diện hiện tại và vui lòng thực hiện đóng băng code (không merge thêm bất kỳ tính năng mới nào sau 18:00 tối nay), chỉ xử lý các lỗi chặn luồng nếu có phản hồi từ đội kiểm thử. Về phía QA, ngay sau khi Backend cập nhật hoàn chỉnh môi trường staging thì nhờ các bạn thực hiện chạy lại toàn bộ bộ kiểm thử hồi quy cho luồng thanh toán vào sáng thứ Bảy để chúng ta kịp rà soát và chốt việc đưa bản 2.4 lên production vào đúng 10:00 thứ Hai tuần sau trong trường hợp không còn phát sinh lỗi blocker nào.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Lý do chính khiến lịch go-live bản 2.4 phải dời từ 14:00 thứ Năm sang 10:00 sáng thứ Hai tuần sau là gì?
- 2. Hạn chót của BE (fix lỗi) và FE (merge bản vá nếu có) trước khi QA kiểm thử lại là khi nào?
- 3. Ai sẽ chốt đi production vào sáng thứ Bảy nếu không còn lỗi chặn luồng?

### SR-03 — Mẫu 1

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

---

### SR-03 — Mẫu 2

**Thông báo điều chỉnh lịch phát hành bản 2.4**

Chào cả nhóm dự án 2.4, cảm ơn mọi người đã cố gắng hoàn thành phần lớn hạng mục đúng tiến độ trong sprint vừa qua.

**Quyết định:** Lịch phát hành bản 2.4 **dự kiến lùi từ 14:00 thứ Năm tuần này sang 10:00 sáng thứ Hai tuần sau**.
*Lý do:* Đối tác ngân hàng bàn giao môi trường sandbox cho API đối soát thanh toán chậm sang chiều thứ Sáu. Sau khi trao đổi với lead kỹ thuật và team sản phẩm, việc giữ lịch phát hành cũ sẽ tiềm ẩn nhiều rủi ro cho luồng thanh toán thực tế.

**Phân việc cho từng team trong thời gian đệm:**
- **FE:** Giữ nguyên nhánh giao diện hiện tại và đóng băng code (**không merge thêm bất kỳ tính năng mới nào sau 18:00 tối nay**); chỉ xử lý các lỗi chặn luồng nếu có phản hồi từ đội kiểm thử.
- **BE:** Hoàn thiện phần tích hợp mock fallback và triển khai lên môi trường staging chậm nhất **trước 17:00 thứ Sáu**.
- **QA:** Ngay sau khi BE cập nhật hoàn chỉnh môi trường staging, chạy lại toàn bộ bộ kiểm thử hồi quy cho luồng thanh toán vào **sáng thứ Bảy** để cả nhóm kịp rà soát và chốt đưa bản 2.4 lên production đúng **10:00 thứ Hai tuần sau** (trong trường hợp không còn phát sinh lỗi blocker nào).

---

### SR-03 — Mẫu 3

Chào cả nhóm dự án 2.4,

Lịch phát hành bản **2.4** dự kiến sẽ lùi từ **14:00 thứ Năm tuần này** sang **10:00 sáng thứ Hai tuần sau** (lên production vào đúng giờ này nếu không còn phát sinh lỗi blocker nào).

**Lý do:** Đối tác ngân hàng bàn giao chậm môi trường sandbox cho API đối soát thanh toán sang chiều thứ Sáu. Sau khi trao đổi với lead kỹ thuật và team sản phẩm, tụi mình quyết định điều chỉnh lịch để tránh rủi ro cho luồng thanh toán thực tế. Cảm ơn mọi người trong sprint vừa qua đã cố gắng hoàn thành phần lớn hạng mục đúng tiến độ.

**Phân việc cho từng team:**
- **BE:** Hoàn thiện phần tích hợp mock fallback và triển khai lên môi trường staging chậm nhất **trước 17:00 thứ Sáu**.
- **FE:** Giữ nguyên nhánh giao diện hiện tại và đóng băng code (không merge thêm bất kỳ tính năng mới nào **sau 18:00 tối nay**); chỉ xử lý các lỗi chặn luồng nếu có phản hồi từ QA.
- **QA:** Ngay sau khi BE cập nhật hoàn chỉnh môi trường staging, chạy lại toàn bộ bộ kiểm thử hồi quy cho luồng thanh toán vào **sáng thứ Bảy** để kịp rà soát và chốt đưa bản 2.4 lên production lúc **10:00 thứ Hai tuần sau** (nếu không còn lỗi blocker nào).

---

### SR-03 — Mẫu 4

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

---

### SR-03 — Mẫu 5

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

---

### Phiếu chấm nhanh SR-03

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho SR-03:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca SR-04 — Giải thích khái niệm

- **Tiêu đề / Chủ đề:** Giải thích cơ chế Idempotency Key kết hợp Exponential Backoff khi thanh toán
- **Đối tượng đọc:** Product Manager, BA và kỹ sư mới vào nhóm ví điện tử
- **Mục đích giao tiếp:** Hiểu rõ Idempotency Key là gì, Exponential Backoff giải quyết vấn đề gì, hai cơ chế phối hợp ra sao để vừa thử lại khi rớt mạng vừa không trừ tiền hai lần.

### Yêu cầu & Văn bản nguồn

```text
Viết lại phần giải thích kỹ thuật dưới đây sang tiếng Việt tự nhiên, dễ hiểu cho PM, BA và lập trình viên mới làm quen hệ thống thanh toán; giữ trọn cơ chế phối hợp và giới hạn quan trọng trong đoạn gốc (không tự bịa thêm thời hạn TTL cụ thể hay mã lỗi HTTP không có trong nguồn):

Trong thiết kế hệ thống phân tán phục vụ thanh toán, việc kết hợp cơ chế khóa định danh bất biến (Idempotency Key) với chiến lược giãn cách thời gian thử lại theo hàm mũ (Exponential Backoff) đóng vai trò mang tính nền tảng trong việc đảm bảo sự an toàn của giao dịch trước các sự cố gián đoạn kết nối mạng. Khi một yêu cầu thanh toán từ phía ứng dụng gửi đi gặp phải tình trạng rớt mạng hoặc hết thời gian chờ phản hồi (timeout), phía gọi sẽ rơi vào trạng thái không thể xác định được liệu máy chủ đã thực hiện việc ghi nhận trừ tiền hay chưa, dẫn đến nhu cầu bắt buộc phải tiến hành gửi lại yêu cầu. Nếu chỉ thực hiện việc thử lại một cách tuần tự thông thường, sự việc sẽ làm gia tăng nguy cơ phát sinh hiện tượng trừ tiền trùng lặp trên tài khoản người dùng; do đó, Idempotency Key được sử dụng như một mã định danh duy nhất đại diện cho mỗi giao dịch nhằm giúp máy chủ nhận diện các yêu cầu lặp lại và trả về kết quả đã xử lý trước đó thay vì thực thi lại thao tác tài chính. Song song với việc bảo vệ tính duy nhất đó, chiến lược Exponential Backoff thực hiện việc kéo dài khoảng thời gian chờ giữa các lần thử lại liên tiếp theo cấp số nhân, kết hợp cùng biên độ dao động ngẫu nhiên (jitter), với mục đích ngăn chặn tình trạng hàng loạt ứng dụng đồng loạt gửi lại yêu cầu tại cùng một thời điểm gây quá tải dây chuyền lên máy chủ đang gặp sự cố. Như vậy, hai cơ chế giải quyết hai vấn đề hoàn toàn bổ trợ lẫn nhau: Backoff kiểm soát tần suất và thời điểm gửi lại để bảo vệ năng lực chịu tải của hệ thống, trong khi Idempotency Key đảm bảo tính đúng đắn rằng giao dịch chỉ được thực thi tối đa một lần. Tuy nhiên, cần lưu ý rằng Idempotency Key chỉ phát huy hiệu lực trong khoảng thời gian máy chủ còn lưu trữ mã khóa này, đồng thời cũng không thể ngăn chặn việc trừ tiền hai lần nếu phía ứng dụng vô tình sinh ra một mã khóa hoàn toàn mới cho cùng một giao dịch đang thanh toán.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Nếu chỉ dùng Exponential Backoff mà thiếu Idempotency Key khi gọi API thanh toán, rủi ro thực tế gì xảy ra?
- 2. Nếu chỉ dùng Idempotency Key mà thiếu Exponential Backoff + jitter khi server thanh toán quá tải, hệ quả gì xảy ra?
- 3. Trong nguồn, hệ thống có quy định TTL của key hay mã lỗi HTTP cụ thể để thử lại không?

### SR-04 — Mẫu 1

Khi xây dựng hệ thống thanh toán, có một tình huống rất dễ gặp: ứng dụng gửi yêu cầu thanh toán đi nhưng bị rớt mạng hoặc hết thời gian chờ phản hồi (`timeout`). Lúc này, phía gọi không thể biết máy chủ đã kịp ghi nhận trừ tiền hay chưa, nên buộc phải gửi lại yêu cầu.

Nếu chỉ thử lại một cách thông thường, hệ thống sẽ đối mặt với rủi ro trừ tiền trùng lặp trên tài khoản người dùng và nguy cơ quá tải dây chuyền lên máy chủ đang gặp sự cố. Để xử lý trọn vẹn, hai cơ chế **Idempotency Key** và **Exponential Backoff** luôn được dùng kết hợp để bổ trợ cho nhau:

* **Idempotency Key — Đảm bảo giao dịch chỉ thực hiện tối đa một lần:** Mỗi giao dịch được gắn một mã định danh duy nhất gọi là *Idempotency Key*. Khi nhận được yêu cầu gửi lại kèm mã khóa này, máy chủ sẽ nhận diện được đây là yêu cầu lặp lại và trả về kết quả đã xử lý trước đó, thay vì thực thi lại thao tác tài chính.
* **Exponential Backoff kèm Jitter — Bảo vệ khả năng chịu tải của hệ thống:** Nếu hàng loạt ứng dụng đồng loạt gửi lại yêu cầu vào cùng một thời điểm, máy chủ đang gặp sự cố sẽ bị quá tải dây chuyền. Chiến lược *Exponential Backoff* giải quyết việc này bằng cách kéo dài khoảng thời gian chờ giữa các lần thử lại liên tiếp theo cấp số nhân, kết hợp với một biên độ dao động ngẫu nhiên (*jitter*) để phân tán thời điểm gửi lại.

Như vậy, hai cơ chế giải quyết hai bài toán bổ trợ lẫn nhau: **Exponential Backoff** kiểm soát tần suất và thời điểm gửi lại để bảo vệ năng lực chịu tải của hệ thống, trong khi **Idempotency Key** đảm bảo tính đúng đắn rằng giao dịch chỉ được thực thi tối đa một lần.

**Hai giới hạn quan trọng cần lưu ý:**
1. **Phụ thuộc vào thời gian lưu trữ khóa:** Idempotency Key chỉ phát huy hiệu lực trong khoảng thời gian máy chủ còn lưu trữ mã khóa này.
2. **Không chống được lỗi sinh nhầm mã từ phía ứng dụng:** Cơ chế này không thể ngăn chặn việc trừ tiền hai lần nếu phía ứng dụng vô tình tạo ra một mã khóa hoàn toàn mới cho cùng một giao dịch đang thanh toán.

---

### SR-04 — Mẫu 2

Trong hệ thống thanh toán phân tán, một tình huống rất dễ gặp là ứng dụng vừa gửi yêu cầu trừ tiền thì bị rớt mạng hoặc hết thời gian chờ (`timeout`). Lúc này, phía ứng dụng không thể biết máy chủ đã ghi nhận trừ tiền hay chưa nên buộc phải gửi lại yêu cầu.

Tuy nhiên, nếu chỉ gửi lại theo cách thông thường, hệ thống sẽ đối mặt với nguy cơ trừ tiền trùng lặp trên tài khoản người dùng; đồng thời, nếu nhiều ứng dụng cùng dồn dập gửi lại cùng lúc, máy chủ đang gặp sự cố có thể bị quá tải dây chuyền. Để xử lý trọn vẹn tình huống này, hệ thống kết hợp hai cơ chế bổ trợ cho nhau:

- **Idempotency Key (khóa định danh bất biến):** Ứng dụng gắn cho mỗi giao dịch một mã định danh duy nhất ngay từ đầu. Khi nhận được yêu cầu gửi lại có cùng mã này, máy chủ sẽ nhận diện đây là yêu cầu lặp lại và trả về kết quả đã xử lý trước đó, thay vì thực hiện trừ tiền thêm lần nữa.
- **Exponential Backoff kèm `jitter`:** Thay vì thử lại ngay và đều đặn, ứng dụng sẽ tăng dần thời gian chờ giữa các lần gửi lại theo cấp số nhân, kết hợp thêm một khoảng dao động ngẫu nhiên (`jitter`). Cách này giúp tránh tình trạng hàng loạt ứng dụng đồng loạt gửi lại yêu cầu vào cùng một thời điểm, bảo vệ máy chủ đang yếu khỏi bị quá tải dây chuyền.

Nói ngắn gọn, **Exponential Backoff** kiểm soát tần suất và thời điểm gửi lại để bảo vệ sức chịu tải của hệ thống, còn **Idempotency Key** bảo đảm tính đúng đắn rằng mỗi giao dịch chỉ được thực thi tối đa một lần.

**Hai giới hạn quan trọng cần lưu ý:**
- Idempotency Key chỉ có hiệu lực trong khoảng thời gian máy chủ còn lưu trữ mã khóa này.
- Cơ chế này cũng không thể ngăn chặn việc trừ tiền hai lần nếu phía ứng dụng vô tình tạo ra một mã khóa mới cho cùng một giao dịch đang thanh toán.

---

### SR-04 — Mẫu 3

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

---

### SR-04 — Mẫu 4

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

---

### SR-04 — Mẫu 5

Trong hệ thống thanh toán phân tán, khi ứng dụng gửi yêu cầu thanh toán đi nhưng bị rớt mạng hoặc quá thời gian chờ phản hồi (timeout), ứng dụng sẽ không biết máy chủ đã trừ tiền hay chưa. Lúc này, ứng dụng buộc phải gửi lại yêu cầu.

Tuy nhiên, nếu chỉ thử lại theo cách thông thường, giao dịch dễ bị trừ tiền trùng lặp trên tài khoản người dùng; đồng thời, nếu nhiều ứng dụng đồng loạt gửi lại yêu cầu vào cùng một thời điểm, máy chủ đang gặp sự cố có thể bị quá tải dây chuyền.

Để giải quyết cả hai vấn đề này, hệ thống kết hợp hai cơ chế bổ trợ lẫn nhau:

- **Idempotency Key — Đảm bảo mỗi giao dịch chỉ thực hiện tối đa một lần:** Ứng dụng gắn cho mỗi giao dịch một mã định danh duy nhất. Khi nhận được yêu cầu gửi lại mang cùng mã khóa này, máy chủ nhận diện đây là yêu cầu lặp lại và trả về kết quả đã xử lý trước đó, thay vì trừ tiền thêm lần nữa.
- **Exponential Backoff kèm jitter — Bảo vệ năng lực chịu tải của hệ thống:** Cơ chế này kiểm soát tần suất và thời điểm gửi lại. Ứng dụng sẽ kéo dài dần khoảng thời gian chờ giữa các lần thử lại liên tiếp theo cấp số nhân, kết hợp thêm một khoảng dao động ngẫu nhiên (jitter). Nhờ vậy, các yêu cầu thử lại được giãn ra, tránh tình trạng hàng loạt ứng dụng dội yêu cầu về máy chủ cùng lúc khi hệ thống đang gặp sự cố.

Tóm lại, hai cơ chế giải quyết hai bài toán tách bạch nhưng phối hợp chặt chẽ: **Exponential Backoff** điều tiết nhịp gửi lại để hệ thống không bị quá tải, còn **Idempotency Key** đảm bảo tính đúng đắn để giao dịch chỉ được thực thi tối đa một lần.

**Hai giới hạn quan trọng cần lưu ý:**
1. **Giới hạn về thời gian lưu trữ:** Idempotency Key chỉ còn tác dụng trong khoảng thời gian máy chủ vẫn lưu trữ mã khóa này.
2. **Rủi ro từ phía ứng dụng:** Cơ chế này không thể ngăn việc trừ tiền hai lần nếu ứng dụng vô tình tạo ra một mã khóa hoàn toàn mới cho cùng một giao dịch đang thanh toán.

---

### Phiếu chấm nhanh SR-04

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho SR-04:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca SR-05 — Business Rule

- **Tiêu đề / Chủ đề:** Quy tắc hoàn tiền từng phần và xử lý mã giảm giá (có chi tiết chưa chốt)
- **Đối tượng đọc:** Đội Sản phẩm (BA/PO) và Kỹ sư Thanh toán
- **Mục đích giao tiếp:** Làm rõ quy tắc hoàn tiền khi khách trả một phần đơn hàng đã áp mã giảm giá, đồng thời chỉ rõ các điểm quy tắc gốc chưa chốt (phí ship và số ngày hoàn tiền) để không tự đoán khi code.

### Yêu cầu & Văn bản nguồn

```text
Viết lại Business Rule dưới đây sang tiếng Việt sáng rõ, mạch lạc cho BA và Kỹ sư triển khai; giữ đúng toàn bộ quy tắc và ngoại lệ trong bản gốc, đồng thời giữ trung thực nếu quy định vẫn còn điểm bỏ ngỏ chưa đủ để lập trình (tuyệt đối không tự bịa thêm số ngày hoàn tiền hay quy tắc phí vận chuyển ngoài nguồn):

Quy định về việc thực hiện hoàn trả tài chính từng phần đối với đơn hàng đa sản phẩm có áp dụng mã ưu đãi

Trong trường hợp người mua tiến hành yêu cầu hoàn trả đối với một hoặc một số hạng mục sản phẩm nằm trong cùng một đơn hàng có sự áp dụng của mã giảm giá tính trên tổng giá trị đơn, giá trị khoản tiền thực hiện hoàn trả cho từng sản phẩm sẽ không được căn cứ theo đơn giá niêm yết ban đầu của sản phẩm đó, mà phải được xác định trên cơ sở số tiền thực tế đã thanh toán sau khi đã thực hiện việc phân bổ phần giá trị được khấu trừ từ mã giảm giá theo tỷ lệ giá trị của từng mặt hàng cấu thành nên đơn hàng. Tuy nhiên, đối với tình huống việc hoàn trả một phần nêu trên dẫn đến hệ quả là tổng giá trị của phần hàng hóa còn lại mà người mua giữ lại bị rơi xuống dưới mức ngưỡng tối thiểu cần thiết để đủ điều kiện hưởng ưu đãi của mã giảm giá đã áp dụng, hệ thống sẽ tiến hành khấu trừ hồi tố phần giá trị ưu đãi tương ứng trước khi xác định khoản tiền hoàn trả cuối cùng. Đồng thời, mã giảm giá đã được kích hoạt sử dụng cho đơn hàng có phát sinh trả hàng một phần sẽ không thuộc diện được hoàn trả lại vào tài khoản của người mua để tái sử dụng cho các giao dịch kế tiếp.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Khi trả 1 sản phẩm trên đơn có mã giảm giá theo ngưỡng tối thiểu làm tổng đơn còn lại tụt xuống dưới ngưỡng (hoặc vẫn >= ngưỡng), tiền hoàn được tính khác nhau thế nào?
- 2. Mã giảm giá đã dùng có được hoàn lại khi khách trả hàng một phần không?
- 3. Hãy kể tên ít nhất 2 điểm mà bản gốc **chưa quy định đủ** để dev code ngay (ví dụ phí ship, thời hạn hoàn, tiền hoàn <= 0).

### SR-05 — Mẫu 1

# Quy định hoàn tiền khi trả một phần đơn hàng có áp dụng mã giảm giá toàn đơn

## 1. Phạm vi áp dụng
- **Áp dụng cho:** Đơn hàng gồm nhiều sản phẩm, đã sử dụng **mã giảm giá tính trên tổng giá trị đơn hàng**, và người mua yêu cầu trả **một hoặc một số sản phẩm** trong cùng đơn hàng đó (trả hàng một phần).
- **Ngoài dữ kiện nguồn (`[Chưa chốt]` nếu thuộc phạm vi triển khai):** Quy định gốc chưa đề cập đến phí vận chuyển, thuế, thời gian xử lý và phương thức hoàn tiền.

---

## 2. Quy tắc nghiệp vụ

### BR-01: Xác định tiền hoàn theo số tiền thực trả sau phân bổ mã giảm giá
- **Điều kiện kích hoạt:** Người mua trả một phần đơn hàng có áp dụng mã giảm giá toàn đơn, **và** tổng giá trị phần hàng hóa còn lại người mua giữ lại vẫn đạt từ mức tối thiểu trở lên (`>= ngưỡng tối thiểu` của mã).
- **Hành vi hệ thống:**
  - **Không** tính tiền hoàn theo đơn giá niêm yết ban đầu của sản phẩm.
  - Phải tính theo **số tiền thực tế người mua đã thanh toán** cho sản phẩm được trả, sau khi phân bổ giá trị giảm giá của mã theo tỷ lệ giá trị của từng mặt hàng trong đơn:
    - `Giảm giá phân bổ cho sản phẩm i = Tổng giá trị giảm của mã × (Giá trị sản phẩm i / Tổng giá trị đơn hàng)`
    - `Tiền hoàn cho sản phẩm trả lại = Giá trị sản phẩm trả lại − Giảm giá phân bổ cho sản phẩm trả lại`

### BR-02: Khấu trừ hồi tố khi phần hàng giữ lại rơi xuống dưới ngưỡng hưởng mã
- **Điều kiện kích hoạt:** Việc trả một phần khiến tổng giá trị phần hàng hóa người mua giữ lại **nhỏ hơn ngưỡng tối thiểu** (`< ngưỡng tối thiểu`) để đủ điều kiện hưởng ưu đãi của mã giảm giá đã áp dụng.
- **Hành vi hệ thống:** Hệ thống phải **khấu trừ hồi tố phần giá trị ưu đãi tương ứng** trước khi xác định số tiền hoàn trả cuối cùng. *(Công thức tính chi tiết của khoản khấu trừ hồi tố hiện ở trạng thái `[Chưa chốt]`, xem Mục 3).*

### BR-03: Không hoàn lại mã giảm giá
- **Điều kiện kích hoạt:** Đơn hàng có phát sinh trả hàng một phần (áp dụng cho cả trường hợp giữ nguyên ưu đãi ở BR-01 lẫn trường hợp bị khấu trừ hồi tố ở BR-02).
- **Hành vi hệ thống:** Mã giảm giá đã dùng cho đơn hàng **không được hoàn lại** vào tài khoản người mua để tái sử dụng cho các giao dịch sau.

---

## 3. Điểm còn bỏ ngỏ cần chốt trước khi lập trình (`[Chưa chốt]`)

Các điểm sau chưa đủ chi tiết trong quy định gốc; BA/PO cần chốt phương án trước khi Kỹ sư lập trình và QA viết test case:

1. **Công thức "khấu trừ hồi tố phần giá trị ưu đãi tương ứng" (BR-02):** `[Chưa chốt]`
   - Cần chốt cụ thể công thức tính để tránh hiểu nhầm thành trừ trùng phần giảm giá của sản phẩm đã trả:
     - *Phương án A (Thu hồi phần giảm giá trên hàng giữ lại):* `Tiền hoàn = Tiền thực trả của hàng trả − Phần giảm giá đã phân bổ cho hàng giữ lại` (tương đương `Tổng tiền khách đã trả cả đơn − Giá trị gốc của phần hàng giữ lại`).
     - *Phương án B (Khấu trừ một phần ưu đãi):* Nếu mã giảm giá có nhiều bậc hoặc điều kiện riêng, chỉ thu hồi phần chênh lệch ưu đãi tương ứng thay vì thu hồi toàn bộ.
2. **Xử lý khi tiền hoàn cuối cùng `<= 0` sau khấu trừ hồi tố:** `[Chưa chốt]`
   - Nếu khoản khấu trừ hồi tố lớn hơn hoặc bằng số tiền thực trả của sản phẩm đang yêu cầu trả, hệ thống sẽ hoàn `0đ`, chặn yêu cầu trả một phần (bắt buộc trả toàn bộ đơn), hay xử lý theo hướng nào?
3. **Cơ sở "giá trị" để chia tỷ lệ phân bổ và xét ngưỡng tối thiểu:** `[Chưa chốt]`
   - Tính theo **đơn giá niêm yết ban đầu** hay **giá bán thực tế sau các chương trình khuyến mãi riêng của từng sản phẩm** (nếu có)?
   - Nếu một dòng sản phẩm có `số lượng > 1` và người mua chỉ trả một phần số lượng (ví dụ mua 3 trả 1), việc phân bổ tính theo từng đơn vị sản phẩm hay theo dòng?
4. **Quy tắc làm tròn và phân bổ số dư:** `[Chưa chốt]`
   - Khi chia tỷ lệ giảm giá ra số lẻ hoặc khi trả hàng nhiều lần trên cùng một đơn, làm tròn theo quy tắc nào (làm tròn lên/xuống/gần nhất) và phần chênh lệch dồn vào sản phẩm nào để tổng tiền hoàn không bị lệch so với tổng tiền khách đã trả?
5. **Trường hợp trả hàng nhiều lần trên cùng một đơn:** `[Chưa chốt]`
   - Nếu lần trả 1 phần hàng giữ lại vẫn `>= ngưỡng tối thiểu`, nhưng đến lần trả 2 mới rơi xuống `< ngưỡng tối thiểu`, hệ thống thực hiện khấu trừ hồi tố tại lần trả thứ 2 như thế nào?
6. **Phạm vi ngoài quy định gốc:** `[Chưa chốt]`
   - Tài liệu nguồn chưa quy định về **phí vận chuyển** (có thu hồi ưu đãi freeship hay hoàn phí ship không) và **thời hạn/kênh hoàn tiền**; cần xác nhận xem các yếu tố này xử lý ở rule khác hay phải bổ sung vào luồng này.

---

### SR-05 — Mẫu 2

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

---

### SR-05 — Mẫu 3

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

---

### SR-05 — Mẫu 4

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

---

### SR-05 — Mẫu 5

# Quy tắc nghiệp vụ: Hoàn tiền khi trả một phần đơn hàng có áp dụng mã giảm giá

## 1. Phạm vi áp dụng
- **Áp dụng cho:** Yêu cầu trả hàng một phần (trả một hoặc một số sản phẩm, không trả toàn bộ đơn) đối với đơn hàng có nhiều sản phẩm và đã áp dụng **mã giảm giá trên tổng giá trị đơn**.
- **Ngoài quy định / chưa được đề cập trong nguồn `[Chưa chốt]`:** Trả toàn bộ đơn hàng, mã giảm giá chỉ áp dụng cho từng sản phẩm cụ thể, quy tắc xử lý phí vận chuyển và thời hạn hoàn tiền.

---

## 2. Chi tiết quy tắc nghiệp vụ

### BR-01: Tính tiền hoàn trả theo số tiền thực trả đã phân bổ ưu đãi
- **Điều kiện kích hoạt:** Người mua yêu cầu trả một hoặc một số sản phẩm trong đơn hàng đa sản phẩm có áp dụng mã giảm giá tính trên tổng giá trị đơn.
- **Hành vi bắt buộc:**
  - Hệ thống **không** tính tiền hoàn dựa trên đơn giá niêm yết ban đầu của sản phẩm được trả.
  - Số tiền hoàn trả cho từng sản phẩm phải được tính theo **số tiền người mua đã thực tế thanh toán** cho sản phẩm đó, sau khi đã phân bổ giá trị khấu trừ của mã giảm giá theo **tỷ lệ giá trị của từng sản phẩm** trong đơn hàng.
  - `[Chưa chốt]` Cơ sở giá dùng để tính tỷ lệ phân bổ và quy tắc làm tròn phần dư khi chia tỷ lệ *(xem Mục 4.1)*.

### BR-02: Khấu trừ hồi tố ưu đãi khi phần hàng giữ lại dưới ngưỡng tối thiểu
- **Điều kiện kích hoạt:** Việc trả hàng một phần làm tổng giá trị của phần hàng hóa còn lại mà người mua giữ lại **nhỏ hơn (`<`) mức ngưỡng tối thiểu** để đủ điều kiện hưởng mã giảm giá đã áp dụng.
- **Hành vi bắt buộc:**
  - Trước khi chốt số tiền hoàn trả cuối cùng, hệ thống **phải khấu trừ hồi tố** phần giá trị ưu đãi tương ứng.
  - `[Chưa chốt]` Công thức xác định phần ưu đãi bị khấu trừ hồi tố, cách tính tổng giá trị phần hàng giữ lại và hướng xử lý nếu tiền hoàn sau khấu trừ bị âm *(xem Mục 4.2 và 4.3)*.

### BR-03: Không hoàn lại mã giảm giá
- **Điều kiện kích hoạt:** Đơn hàng đã sử dụng mã giảm giá và có phát sinh trả hàng một phần.
- **Hành vi bắt buộc:** Hệ thống **không hoàn lại** mã giảm giá đó vào tài khoản của người mua để tái sử dụng cho các giao dịch sau.

---

## 3. Bảng tổng hợp nhánh xử lý

| Tình huống sau khi trả một phần | Số tiền hoàn trả | Trạng thái mã giảm giá | Trạng thái đặc tả |
|---|---|---|---|
| Phần hàng giữ lại vẫn đạt ngưỡng tối thiểu (`>=` ngưỡng của mã) | Hoàn theo số tiền thực trả của sản phẩm được trả (sau khi đã phân bổ tiền giảm giá theo tỷ lệ giá trị từng món). | Không hoàn lại vào tài khoản người mua. | `[Chưa chốt]` cơ sở tỷ lệ phân bổ và quy tắc làm tròn. |
| Phần hàng giữ lại tụt xuống dưới ngưỡng tối thiểu (`<` ngưỡng của mã) | Tính theo mức thực trả đã phân bổ, sau đó **khấu trừ hồi tố** phần ưu đãi tương ứng trước khi chốt tiền hoàn cuối cùng. | Không hoàn lại vào tài khoản người mua. | `[Chưa chốt]` công thức khấu trừ hồi tố, giá trị so sánh ngưỡng và biên tiền hoàn `< 0`. |

---

## 4. Điểm chưa chốt cần PO / Nghiệp vụ xác nhận trước khi dev

1. **Công thức phân bổ mã giảm giá (`BR-01`):**
   - "Tỷ lệ giá trị của từng mặt hàng" tính theo **giá niêm yết ban đầu** hay **giá sau các khuyến mãi cấp sản phẩm** (nếu đơn có giảm giá riêng cho từng món trước khi áp mã toàn đơn)?
   - Quy tắc **làm tròn số lẻ** khi phân bổ tiền giảm giá (làm tròn theo đơn vị tiền tệ nào, làm tròn lên/xuống/nửa lên và dồn phần chênh lệch vào sản phẩm nào để tổng tiền phân bổ khớp đúng giá trị mã)?

2. **Công thức "khấu trừ hồi tố phần giá trị ưu đãi tương ứng" (`BR-02`):**
   - Cần chốt công thức cụ thể để tránh trừ trùng phần ưu đãi của sản phẩm trả lại (vốn đã bị trừ ở `BR-01`):
     - *Phương án A:* Khấu trừ phần giá trị ưu đãi đã phân bổ cho **các sản phẩm người mua giữ lại**.
     - *Phương án B:* Tính lại tiền hoàn = *(Tổng tiền đã thực trả cho cả đơn)* − *(Tổng giá trị phần hàng giữ lại khi chưa áp mã)*.
   - Nếu giá trị bị khấu trừ hồi tố **lớn hơn** số tiền thực trả của sản phẩm đem trả (khiến số tiền hoàn cuối cùng `< 0`), hệ thống sẽ chặn mức hoàn tối thiểu bằng `0`, từ chối cho trả một phần, hay xử lý theo quy tắc khác?

3. **Cách xét ngưỡng tối thiểu và trường hợp trả nhiều lần (`BR-02`):**
   - "Tổng giá trị của phần hàng hóa còn lại" dùng để so sánh với ngưỡng tối thiểu tính theo **giá niêm yết** hay **giá sau khuyến mãi cấp sản phẩm**?
   - Nếu đơn hàng phát sinh trả một phần **nhiều lần** (lần 1 phần giữ lại vẫn `>=` ngưỡng, lần 2 mới tụt `<` ngưỡng), hệ thống kiểm tra ngưỡng theo giá trị giữ lại lũy kế hay từng lần, và khấu trừ hồi tố vào lần trả nào?

4. **Các yếu tố ngoài phạm vi văn bản gốc (nếu thuộc luồng hoàn tiền chung):**
   - Tài liệu nguồn chưa quy định cách xử lý **phí vận chuyển** và **thời gian/số ngày hoàn tiền**; cần xác nhận xem luồng này có dùng chung chính sách hiện hành của hệ thống hay cần bổ sung quy tắc riêng.

---

### Phiếu chấm nhanh SR-05

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho SR-05:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca SR-06 — Tài liệu kỹ thuật

- **Tiêu đề / Chủ đề:** Chuyển đổi dự phòng CSDL (Failover) khi dùng sao chép bất đồng bộ
- **Đối tượng đọc:** Kỹ sư Backend & SRE / Vận hành hệ thống
- **Mục đích giao tiếp:** Trình bày rõ cơ chế, rủi ro mất dữ liệu (RPO > 0) khi failover từ Primary sang Replica chạy bất đồng bộ, cách xử lý transaction đang chạy dở và trạng thái kết nối ứng dụng.

### Yêu cầu & Văn bản nguồn

```text
Viết lại đoạn tài liệu kỹ thuật dưới đây cho kỹ sư Backend và SRE đọc nhanh và nắm rõ rủi ro khi vận hành; giữ nguyên toàn bộ cơ chế kỹ thuật, thuật ngữ bắt buộc (Primary, Replica, RPO > 0, rollback, split-brain) và không tự bịa thêm con số thời gian RTO/RPO cụ thể không có trong nguồn:

Trong kiến trúc cơ sở dữ liệu quan hệ triển khai theo mô hình một máy chủ chính (Primary) kết hợp với bản sao (Replica) sử dụng cơ chế sao chép bất đồng bộ (asynchronous replication), quá trình chuyển đổi dự phòng (failover) khi nút Primary gặp sự cố đòi hỏi sự đánh đổi trực tiếp giữa thời gian khôi phục khả năng ghi và tính toàn vẹn của dữ liệu phát sinh gần thời điểm sự cố. Do đặc thù của sao chép bất đồng bộ là nút Primary sẽ xác nhận hoàn tất giao dịch (commit) với ứng dụng ngay sau khi ghi nhận cục bộ mà không chờ nút Replica phản hồi đã lưu trữ nhật ký thay đổi (WAL/binlog), sự tồn tại của độ trễ sao chép (replication lag) dẫn đến hệ quả là những giao dịch đã được xác nhận thành công trên Primary ngay trước lúc xảy ra sự cố nhưng chưa kịp truyền sang Replica có thể bị thất thoát khi hệ thống tiến hành thăng cấp (promote) Replica lên đảm nhiệm vai trò Primary mới, đồng nghĩa với việc mục tiêu điểm khôi phục (RPO) lớn hơn 0. Song song đó, toàn bộ các giao dịch đang thực thi dở dang ở trạng thái chưa hoàn tất xác nhận (uncommitted) tại thời điểm chuyển đổi sẽ bị hệ thống thực hiện hoàn tác (rollback). Ngoài ra, trong khoảng thời gian diễn ra quá trình thăng cấp nút mới và cập nhật định tuyến kết nối hoặc connection pool, lớp ứng dụng có thể ghi nhận khoảng gián đoạn quyền ghi hoặc trạng thái chỉ đọc tạm thời. Cuối cùng, tại thời điểm máy chủ Primary ban đầu được khắc phục và khởi động lại, hệ thống tuyệt đối không được phép để máy chủ này tự động tiếp nhận lưu lượng ghi trở lại ngay trước khi thực hiện đồng bộ hoặc tái lập lại đúng vai trò nhằm ngăn chặn tình trạng phân mảnh quyền ghi đồng thời trên hai nút (split-brain) gây xung đột dữ liệu nghiêm trọng.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Vì sao khi Primary sập đột ngột trong mô hình sao chép bất đồng bộ, việc nâng Replica lên Primary mới có thể làm RPO > 0?
- 2. Khi nào một giao dịch bị rollback khi Primary cũ quay lại làm Replica?
- 3. Vì sao không được để cả 2 node cùng nhận ghi (split-brain)?

### SR-06 — Mẫu 1

**Failover trên mô hình Primary–Replica (Sao chép bất đồng bộ): Đánh đổi và Rủi ro vận hành**

Trong kiến trúc cơ sở dữ liệu quan hệ gồm một **Primary** và **Replica** dùng cơ chế sao chép bất đồng bộ (asynchronous replication), quá trình failover khi Primary gặp sự cố luôn đòi hỏi đánh đổi trực tiếp giữa thời gian khôi phục khả năng ghi và tính toàn vẹn của dữ liệu phát sinh gần thời điểm sự cố.

**Các rủi ro kỹ thuật cần kiểm soát khi vận hành:**

- **Thất thoát dữ liệu đã commit (`RPO > 0`):** Primary xác nhận hoàn tất giao dịch (`commit`) với ứng dụng ngay sau khi ghi cục bộ, không chờ Replica phản hồi đã lưu nhật ký thay đổi (WAL/binlog). Do tồn tại độ trễ sao chép (replication lag), các giao dịch đã `commit` trên Primary ngay trước sự cố nhưng chưa kịp truyền sang Replica có thể bị mất khi thăng cấp (`promote`) Replica lên làm Primary mới.
- **Hoàn tác giao dịch đang chạy (`rollback`):** Toàn bộ các giao dịch đang thực thi dở dang ở trạng thái chưa xác nhận (`uncommitted`) tại thời điểm chuyển đổi đều bị hệ thống `rollback`.
- **Gián đoạn quyền ghi hoặc chỉ đọc tạm thời:** Trong khoảng thời gian hệ thống thăng cấp nút mới và cập nhật định tuyến kết nối hoặc connection pool, lớp ứng dụng có thể ghi nhận tình trạng gián đoạn quyền ghi hoặc chuyển sang trạng thái chỉ đọc tạm thời.
- **Xung đột dữ liệu do `split-brain` khi khôi phục nút cũ:** Khi máy chủ Primary ban đầu được khắc phục và khởi động lại, hệ thống tuyệt đối không được để máy chủ này tự động tiếp nhận lưu lượng ghi trở lại trước khi thực hiện đồng bộ hoặc tái lập đúng vai trò. Quy định này nhằm ngăn tình trạng phân mảnh quyền ghi đồng thời trên hai nút (`split-brain`), gây xung đột dữ liệu nghiêm trọng.

---

### SR-06 — Mẫu 2

Trong kiến trúc CSDL quan hệ gồm một `Primary` và `Replica` dùng sao chép bất đồng bộ (asynchronous replication), quá trình failover khi `Primary` gặp sự cố là sự đánh đổi trực tiếp giữa thời gian khôi phục khả năng ghi và tính toàn vẹn của dữ liệu phát sinh sát thời điểm sự cố.

Khi vận hành failover và khôi phục cụm, cần nắm rõ 4 cơ chế và rủi ro sau:

- **Có thể mất dữ liệu đã commit (`RPO > 0`):** `Primary` xác nhận `commit` cho ứng dụng ngay sau khi ghi cục bộ mà không chờ `Replica` xác nhận đã lưu WAL/binlog. Do tồn tại độ trễ sao chép (replication lag), các giao dịch đã commit trên `Primary` ngay trước sự cố nhưng chưa kịp truyền sang `Replica` có thể bị mất khi thăng cấp (promote) `Replica` lên làm `Primary` mới.
- **Mọi giao dịch chưa commit đều bị `rollback`:** Toàn bộ giao dịch đang chạy dở dang (uncommitted) tại thời điểm chuyển đổi sẽ bị hệ thống hủy bỏ (`rollback`).
- **Ứng dụng bị gián đoạn ghi tạm thời:** Trong thời gian promote nút mới và cập nhật định tuyến kết nối hoặc connection pool, tầng ứng dụng có thể gặp gián đoạn quyền ghi hoặc chuyển sang trạng thái chỉ đọc tạm thời.
- **Nguy cơ `split-brain` khi `Primary` cũ khởi động lại:** Khi `Primary` ban đầu được khắc phục và bật lại, tuyệt đối không để nút này tự động nhận lưu lượng ghi ngay trước khi đồng bộ hoặc thiết lập lại đúng vai trò. Nếu không chặn kịp thời, cả hai nút có thể nhận ghi đồng thời (`split-brain`), gây xung đột dữ liệu nghiêm trọng.

---

### SR-06 — Mẫu 3

**Bối cảnh & Đánh đổi cốt lõi**
Trong kiến trúc cơ sở dữ liệu quan hệ gồm một nút **Primary** và **Replica** sử dụng cơ chế sao chép bất đồng bộ (asynchronous replication), khi Primary gặp sự cố, quá trình chuyển đổi dự phòng (failover) buộc phải đánh đổi trực tiếp giữa **thời gian khôi phục quyền ghi** và **tính toàn vẹn của dữ liệu** phát sinh sát thời điểm sự cố.

**Rủi ro và tác động khi failover**
- **Mất dữ liệu đã commit (RPO > 0):** Primary xác nhận hoàn tất giao dịch (commit) với ứng dụng ngay sau khi ghi cục bộ mà không chờ Replica phản hồi đã lưu nhật ký thay đổi (WAL/binlog). Do độ trễ sao chép (replication lag), các giao dịch vừa commit trên Primary ngay trước sự cố nhưng chưa kịp truyền sang Replica có thể bị mất khi promote Replica lên làm Primary mới.
- **Hủy giao dịch chưa hoàn tất (rollback):** Toàn bộ các giao dịch đang chạy dở dang ở trạng thái chưa xác nhận hoàn tất (uncommitted) tại thời điểm chuyển đổi đều bị hệ thống rollback.
- **Gián đoạn quyền ghi tạm thời ở lớp ứng dụng:** Trong thời gian promote Primary mới và cập nhật định tuyến kết nối hoặc connection pool, ứng dụng có thể gặp gián đoạn quyền ghi hoặc trạng thái chỉ đọc tạm thời.

**Yêu cầu bắt buộc khi khôi phục Primary cũ**
- **Phòng tránh split-brain:** Khi máy chủ Primary ban đầu được khắc phục và khởi động lại, tuyệt đối không để nút này tự động tiếp nhận lưu lượng ghi trở lại ngay. Phải đồng bộ dữ liệu hoặc tái lập lại đúng vai trò của nút này trước nhằm ngăn tình trạng hai nút cùng nhận quyền ghi đồng thời (split-brain) gây xung đột dữ liệu nghiêm trọng.

---

### SR-06 — Mẫu 4

**Rủi ro vận hành khi failover trên DB quan hệ mô hình Primary–Replica bất đồng bộ**

Trong kiến trúc cơ sở dữ liệu quan hệ gồm một **Primary** và **Replica** dùng sao chép bất đồng bộ (`asynchronous replication`), khi Primary gặp sự cố, quá trình **failover** luôn buộc hệ thống phải đánh đổi trực tiếp giữa thời gian khôi phục khả năng ghi và tính toàn vẹn của dữ liệu phát sinh gần thời điểm sự cố.

Khi vận hành, cần lưu ý các rủi ro sau:

- **Mất dữ liệu đã commit (`RPO > 0`):** Vì Primary xác nhận `commit` với ứng dụng ngay sau khi ghi cục bộ mà không chờ Replica phản hồi đã lưu `WAL/binlog`, nên khi có độ trễ sao chép (`replication lag`), các giao dịch đã `commit` trên Primary ngay trước lúc sự cố nhưng chưa kịp truyền sang Replica **có thể bị mất** khi hệ thống promote Replica lên làm Primary mới.
- **Hủy giao dịch đang chạy dở:** Toàn bộ giao dịch chưa hoàn tất xác nhận (`uncommitted`) tại thời điểm chuyển đổi **sẽ bị `rollback`**.
- **Gián đoạn quyền ghi phía ứng dụng:** Trong thời gian promote nút mới và cập nhật định tuyến kết nối hoặc `connection pool`, ứng dụng **có thể** gặp gián đoạn quyền ghi hoặc trạng thái chỉ đọc tạm thời.
- **Nguy cơ `split-brain` khi Primary cũ chạy lại:** Khi Primary ban đầu được khắc phục và khởi động lại, **tuyệt đối không** để nút này tự động nhận lưu lượng ghi trở lại trước khi được đồng bộ hoặc tái lập đúng vai trò. Việc để hai nút cùng nhận quyền ghi đồng thời (`split-brain`) sẽ gây xung đột dữ liệu nghiêm trọng.

---

### SR-06 — Mẫu 5

Trong kiến trúc cơ sở dữ liệu quan hệ gồm một máy chủ **Primary** và bản sao (**Replica**) dùng cơ chế sao chép bất đồng bộ (asynchronous replication), quá trình **failover** khi Primary gặp sự cố luôn đòi hỏi đánh đổi trực tiếp giữa thời gian khôi phục quyền ghi và tính toàn vẹn dữ liệu phát sinh sát thời điểm lỗi.

Dưới đây là các tác động và rủi ro vận hành cần nắm khi failover diễn ra:

- **Mất dữ liệu đã xác nhận (RPO > 0):** Primary xác nhận hoàn tất giao dịch (commit) cho ứng dụng ngay sau khi ghi cục bộ mà không chờ Replica lưu xong nhật ký thay đổi (WAL/binlog). Do tồn tại độ trễ sao chép (replication lag), các giao dịch đã commit trên Primary ngay trước lúc gặp sự cố nhưng chưa kịp truyền sang Replica có thể bị mất khi Replica được thăng cấp (promote) lên làm Primary mới.
- **Hoàn tác giao dịch dở dang (rollback):** Toàn bộ các giao dịch đang thực thi nhưng chưa hoàn tất xác nhận (uncommitted) tại thời điểm chuyển đổi sẽ bị hệ thống thực hiện rollback.
- **Gián đoạn quyền ghi ở tầng ứng dụng:** Trong thời gian promote nút mới và cập nhật định tuyến kết nối hoặc connection pool, ứng dụng có thể gặp khoảng gián đoạn quyền ghi hoặc rơi vào trạng thái chỉ đọc tạm thời.
- **Nguy cơ split-brain khi Primary cũ hoạt động lại:** Khi máy chủ Primary ban đầu được khắc phục và khởi động lại, hệ thống tuyệt đối không được để nút này tự động nhận lưu lượng ghi trước khi đồng bộ dữ liệu hoặc tái lập đúng vai trò. Nếu không chặn bước này, cả hai nút sẽ cùng tiếp nhận ghi đồng thời (split-brain), gây xung đột dữ liệu nghiêm trọng.

---

### Phiếu chấm nhanh SR-06

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho SR-06:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca SR-07 — Văn bản dài nhiều thông tin liên quan

- **Tiêu đề / Chủ đề:** Quy trình tiếp nhận và duyệt hoàn tiền khiếu nại giao thiếu/hư hỏng (4 đoạn liên kết)
- **Đối tượng đọc:** Nhân viên CSKH, Bộ phận Kho và Quản lý ca trực
- **Mục đích giao tiếp:** Biến một tài liệu vận hành 4 đoạn dài dòng thành hướng dẫn dễ tra cứu theo bước, tách rõ điều kiện thời hạn, phân quyền duyệt < 500.000đ vs >= 500.000đ và ngoại lệ hàng tươi sống/dễ vỡ.

### Yêu cầu & Văn bản nguồn

```text
Biên tập và tổ chức lại tài liệu quy trình 4 đoạn dưới đây cho nhân viên CSKH, Kho và Quản lý ca dễ tra cứu và làm đúng ngay khi xử lý sự cố; giữ chính xác mọi ngưỡng tiền (< 500.000đ vs >= 500.000đ), mốc giờ (48 giờ, 24 giờ làm việc), bằng chứng bắt buộc và ngoại lệ (không tự thêm kênh hoàn tiền hay KPI mới ngoài nguồn):

Tài liệu hướng dẫn quy trình tiếp nhận và giải quyết các yêu cầu khiếu nại phát sinh đối với đơn hàng gặp sự cố giao thiếu sản phẩm hoặc hư hỏng hàng hóa trong quá trình vận chuyển

Về điều kiện tiếp nhận ban đầu, khách hàng có nhu cầu thực hiện khiếu nại liên quan đến tình trạng thiếu hụt số lượng hoặc hư hỏng vật lý đối với đơn hàng cần phải tiến hành gửi yêu cầu lên hệ thống trong khoảng thời gian giới hạn không vượt quá 48 giờ kể từ thời điểm đơn hàng được hệ thống ghi nhận chuyển sang trạng thái Đã giao thành công. Mọi hồ sơ khiếu nại gửi sau mốc thời gian 48 giờ nêu trên sẽ bị hệ thống thực hiện từ chối tiếp nhận một cách tự động, ngoại trừ trường hợp ngoại lệ có văn bản hoặc ghi nhận xác nhận từ phía đơn vị vận chuyển về việc đã xảy ra sai sót trong khâu cập nhật trạng thái giao hàng thực tế lên hệ thống.

Về thành phần chứng từ bắt buộc đính kèm theo yêu cầu, người gửi khiếu nại phải thực hiện cung cấp đầy đủ hình ảnh chụp rõ tình trạng bên ngoài lẫn bên trong kiện hàng cùng với phiếu giao hàng đi kèm. Riêng đối với các đơn hàng có chứa sản phẩm thuộc nhóm danh mục hàng tươi sống hoặc hàng hóa có tính chất dễ vỡ, quy trình quy định điều kiện bắt buộc bổ sung là khách hàng phải đính kèm thêm đoạn video ghi lại toàn bộ quá trình mở hộp một cách liền mạch và không có dấu hiệu cắt ghép chỉnh sửa.

Về phân cấp thẩm quyền kiểm tra và phê duyệt chi trả khoản tiền hoàn, quy trình được phân chia theo ngưỡng giá trị của yêu cầu khiếu nại cụ thể. Đối với các yêu cầu có giá trị đề nghị hoàn trả ở mức dưới 500.000đ, nhân viên thuộc bộ phận Chăm sóc khách hàng (CSKH) được quyền trực tiếp tiến hành rà soát tính hợp lệ của bộ chứng từ bằng chứng đã nộp và thực hiện phê duyệt lệnh hoàn tiền ngay trong ca làm việc hiện tại. Ngược lại, đối với các yêu cầu có giá trị đề nghị hoàn trả từ 500.000đ trở lên, nhân viên CSKH không tự ý phê duyệt mà phải tiến hành chuyển tiếp hồ sơ sang Bộ phận Kho để bộ phận này thực hiện việc kiểm tra đối chiếu lại dữ liệu camera tại khâu đóng gói đơn hàng làm căn cứ trình lên Quản lý ca xem xét phê duyệt cuối cùng.

Về thời hạn phối hợp xử lý giữa các bộ phận liên quan trong trường hợp phải chuyển tiếp hồ sơ giá trị cao, Bộ phận Kho có trách nhiệm hoàn tất quá trình kiểm tra dữ liệu camera đóng gói và gửi phản hồi kết quả xác minh về cho luồng xử lý trong khoảng thời gian tối đa không vượt quá 24 giờ làm việc tính từ thời điểm tiếp nhận thông tin chuyển tiếp từ phía nhân viên CSKH.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Khách hàng phải gửi khiếu nại trong bao lâu kể từ lúc trạng thái chuyển sang 'Đã giao thành công', và trường hợp quá hạn duy nhất nào vẫn được nhận?
- 2. Khách cần nộp những chứng từ gì (lưu ý: hàng tươi sống/dễ vỡ có thêm yêu cầu gì, và 'phiếu giao hàng' có bị giới hạn chỉ ảnh chụp không)?
- 3. Đơn khiếu nại hoàn 450.000đ vs 600.000đ do ai duyệt, và Kho có tối đa bao lâu để trả kết quả kiểm tra camera?

### SR-07 — Mẫu 1

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

---

### SR-07 — Mẫu 2

# Quy trình tiếp nhận và xử lý khiếu nại giao thiếu hoặc hư hỏng hàng hóa

Áp dụng cho **CSKH, Bộ phận Kho và Quản lý ca** khi giải quyết khiếu nại đơn hàng giao thiếu sản phẩm hoặc hư hỏng hàng hóa trong quá trình vận chuyển.

## 1. Điều kiện tiếp nhận ban đầu
- **Thời hạn gửi khiếu nại:** Khách hàng phải gửi yêu cầu lên hệ thống trong vòng **48 giờ** (không vượt quá 48 giờ) kể từ thời điểm đơn hàng được hệ thống ghi nhận chuyển sang trạng thái **Đã giao thành công**.
- **Quá hạn:** Mọi hồ sơ gửi sau mốc **48 giờ** bị hệ thống tự động từ chối tiếp nhận.
- **Ngoại lệ:** Trường hợp có văn bản hoặc ghi nhận xác nhận từ đơn vị vận chuyển về sai sót trong khâu cập nhật trạng thái giao hàng thực tế lên hệ thống.

## 2. Chứng từ bằng chứng bắt buộc
- **Mọi đơn hàng khiếu nại phải có đủ:**
  - Ảnh chụp rõ tình trạng bên ngoài và bên trong kiện hàng.
  - Phiếu giao hàng đi kèm.
- **Đơn hàng có sản phẩm tươi sống hoặc hàng dễ vỡ (bắt buộc bổ sung):**
  - Video ghi lại toàn bộ quá trình mở hộp liền mạch, không có dấu hiệu cắt ghép, chỉnh sửa.

## 3. Phân cấp kiểm tra, phối hợp và phê duyệt hoàn tiền

| Giá trị đề nghị hoàn trả | CSKH | Bộ phận Kho | Quản lý ca | Thời hạn xử lý |
| :--- | :--- | :--- | :--- | :--- |
| **Dưới 500.000đ** (`< 500.000đ`) | Rà soát tính hợp lệ của bộ chứng từ bằng chứng đã nộp và **trực tiếp phê duyệt lệnh hoàn tiền**. | Không cần chuyển hồ sơ. | Không cần trình duyệt. | CSKH hoàn tất **ngay trong ca làm việc hiện tại**. |
| **Từ 500.000đ trở lên** (`>= 500.000đ`) | **Không tự ý phê duyệt**; chuyển tiếp hồ sơ sang Bộ phận Kho. | Kiểm tra, đối chiếu dữ liệu camera tại khâu đóng gói đơn hàng làm căn cứ trình duyệt; gửi kết quả xác minh về luồng xử lý. | Xem xét và **phê duyệt cuối cùng** dựa trên kết quả xác minh từ Kho. | Bộ phận Kho hoàn tất kiểm tra và phản hồi **tối đa 24 giờ làm việc** kể từ lúc nhận thông tin chuyển tiếp từ CSKH. |

---

### SR-07 — Mẫu 3

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

---

### SR-07 — Mẫu 4

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

---

### SR-07 — Mẫu 5

# Quy trình tiếp nhận và xử lý khiếu nại đơn hàng giao thiếu hoặc hư hỏng

Áp dụng cho các khiếu nại phát sinh do **giao thiếu sản phẩm** hoặc **hàng hóa hư hỏng trong quá trình vận chuyển**.

---

## 1. Điều kiện thời hạn tiếp nhận

* **Thời hạn gửi yêu cầu:** Khách hàng phải gửi khiếu nại lên hệ thống trong vòng **tối đa 48 giờ** kể từ thời điểm đơn hàng chuyển sang trạng thái **Đã giao thành công**.
* **Sau mốc 48 giờ:** Hệ thống tự động từ chối tiếp nhận.
* **Ngoại lệ:** Vẫn xem xét tiếp nhận nếu có **văn bản hoặc ghi nhận xác nhận từ đơn vị vận chuyển** về việc cập nhật sai trạng thái giao hàng thực tế lên hệ thống.

---

## 2. Chứng từ bắt buộc khách hàng phải cung cấp

### Áp dụng cho mọi đơn hàng khiếu nại
1. Hình ảnh chụp rõ tình trạng **bên ngoài** kiện hàng.
2. Hình ảnh chụp rõ tình trạng **bên trong** kiện hàng.
3. **Phiếu giao hàng** đi kèm.

### Bổ sung bắt buộc với hàng tươi sống hoặc hàng dễ vỡ
* Đính kèm thêm **video mở hộp** quay **toàn bộ quá trình**, **liền mạch**, **không có dấu hiệu cắt ghép hay chỉnh sửa**.

---

## 3. Phân cấp xử lý và phê duyệt hoàn tiền

| Giá trị đề nghị hoàn trả | Đầu mối kiểm tra chứng từ | Thẩm quyền phê duyệt | Thời hạn xử lý |
| :--- | :--- | :--- | :--- |
| **Dưới 500.000đ** (`< 500.000đ`) | Nhân viên CSKH kiểm tra tính hợp lệ của bộ chứng từ | **Nhân viên CSKH** duyệt trực tiếp | Hoàn tất ngay **trong ca làm việc hiện tại** |
| **Từ 500.000đ trở lên** (`>= 500.000đ`) | **CSKH** chuyển tiếp hồ sơ sang Kho (không tự duyệt) → **Bộ phận Kho** kiểm tra, đối chiếu camera tại khâu đóng gói | **Quản lý ca** xem xét và phê duyệt cuối cùng (dựa trên kết quả xác minh từ Kho) | **Bộ phận Kho** phản hồi kết quả xác minh về luồng xử lý trong **tối đa 24 giờ làm việc** kể từ lúc nhận chuyển tiếp từ CSKH |

---

## 4. Việc cần làm theo từng bộ phận

* **Nhân viên CSKH:**
  1. Kiểm tra điều kiện thời hạn **48 giờ** (hoặc xác nhận ngoại lệ sai sót cập nhật từ đơn vị vận chuyển nếu quá hạn).
  2. Kiểm tra đủ bộ chứng từ bắt buộc (lưu ý yêu cầu **video mở hộp liền mạch** nếu đơn có hàng tươi sống hoặc hàng dễ vỡ).
  3. Căn cứ giá trị đề nghị hoàn trả:
     * **Dưới 500.000đ:** Duyệt lệnh hoàn tiền ngay trong ca làm việc hiện tại.
     * **Từ 500.000đ trở lên:** Không tự duyệt, chuyển tiếp hồ sơ sang Bộ phận Kho.
* **Bộ phận Kho:** Khi nhận hồ sơ từ **500.000đ trở lên**, kiểm tra đối chiếu dữ liệu **camera khâu đóng gói** và gửi kết quả xác minh về luồng xử lý trong **tối đa 24 giờ làm việc** kể từ khi tiếp nhận thông tin từ CSKH.
* **Quản lý ca:** Căn cứ kết quả đối chiếu camera do Bộ phận Kho gửi lên để xem xét và phê duyệt cuối cùng đối với các khiếu nại **từ 500.000đ trở lên**.

---

### Phiếu chấm nhanh SR-07

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho SR-07:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca V5-01 — Hội thoại tự nhiên

- **Tiêu đề / Chủ đề:** Đồng nghiệp than mệt vì review PR căng thẳng và đổi requirement phút chót
- **Đối tượng đọc:** Kỹ sư đang chat trao đổi tự nhiên
- **Mục đích giao tiếp:** Phản hồi tự nhiên, đồng cảm và gợi ý thực tế nhẹ nhàng mà không biến thành báo cáo hay checklist cứng nhắc.

### Yêu cầu & Văn bản nguồn

```text
Hôm nay vừa bị tech lead comment 18 chỗ trên PR xong đang sửa dở thì sếp lại nhắn đổi requirement ngay phút chót, giờ đầu óc mụ mị chả biết nên ráng sửa nốt tối nay hay ra làm ly cà phê rồi mai tính tiếp nữa ông ơi.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Phản hồi này có thừa nhận đúng tình huống 18 comment PR + sếp đổi requirement phút chót với giọng đồng nghiệp (không giảng đạo lý) không?
- 2. Gợi ý hành động tiếp theo có hợp lý (tạm nghỉ/chưa vội code khi requirement mới chưa rõ) và tránh bịa công cụ/ticket không có trong câu hỏi không?

### V5-01 — Mẫu 1

Nghe thôi đã thấy tụt mood giùm ông rồi. Nhưng thật lòng khuyên ông: **dừng tay đi nghỉ đi, đừng ráng tối nay làm gì.**

Có hai lý do rất thực tế:
1. **Dễ làm công cốc:** Sếp vừa đổi requirement phút chót, rất có thể vài chỗ trong 18 cái comment kia lát nữa cũng phải đập đi viết lại theo yêu cầu mới. Cố sửa nốt lúc này vừa mệt vừa dễ thành vô nghĩa.
2. **Đầu óc mụ mị code chỉ sinh thêm bug:** Lúc mệt mà cố sửa 18 chỗ cộng thêm logic mới, sáng mai nhìn lại có khi chính ông còn không nhận ra mình viết gì, lại ăn thêm một rổ comment nữa thì khổ.

Trước khi gập máy, ông chỉ cần làm đúng 2 việc nhẹ nhàng mất tầm 5 phút thôi:
- Lưu tạm chỗ code đang làm dở (`git stash` hoặc commit tạm lên nhánh WIP) để mai mở ra không bị quên mạch.
- Note nhanh mấy gạch đầu dòng xem requirement mới ảnh hưởng tới chỗ nào, nếu cần thì nhắn nhẹ sếp hoặc tech lead một câu là đang cập nhật theo yêu cầu mới nên mai sẽ đẩy PR hoàn chỉnh (trừ khi mai phải release gấp ngay từ sáng, còn không thì cứ bình tĩnh).

Xong xuôi thì ra ngoài hít thở chút đi. Cơ mà tối rồi, làm ly gì mát mát hay cốc trà thôi chứ nốc cà phê giờ này đêm lại thức trắng ngắm trần nhà đấy. Mai đầu óc tỉnh táo vào giải quyết một lèo vẫn nhanh hơn ngồi lỳ tối nay!

---

### V5-01 — Mẫu 2

Đóng máy ra ngoài hít thở rồi mai tính tiếp đi ông, đừng cố ngồi cày tối nay nữa.

Đầu óc đang mụ mị mà ráng sửa tiếp thì rất dễ đẻ thêm bug mới, mai tech lead lại phải review thêm vòng nữa còn oải hơn. Quan trọng hơn là sếp vừa đổi requirement phút chót — nếu chưa chốt rõ phần thay đổi đó ảnh hưởng tới đâu, ông ngồi hì hục sửa 18 comment cũ tối nay có khi sáng mai lại phải đập đi viết lại, vừa mất sức vừa công cốc.

Trước khi đứng dậy, ông làm nhanh hai việc mất tầm 5 phút thôi:
1. Commit tạm phần đang sửa dở (để tag WIP) hoặc note vội vài dòng xem đang làm tới đâu để sáng mai mở máy khỏi mất công nhớ lại ngữ cảnh.
2. Nhắn hỏi hoặc xác nhận lại với sếp cho rõ phạm vi requirement mới và deadline, để sáng mai vào việc là có thông tin chuẩn xử lý luôn.

Xong xuôi thì gập máy nghỉ ngơi đi. Mà tối rồi thì cân nhắc gọi món gì không caffeine thay cho ly cà phê nhé, kẻo đêm lại thức trắng suy nghĩ về cái PR đấy.

---

### V5-01 — Mẫu 3

Thôi dẹp máy đi nghỉ đi ông ơi. Đầu đang mụ mị mà cố ngồi sửa tiếp giữa lúc vừa ăn 18 comment vừa bị đổi requirement thì dễ đẻ thêm bug lắm, chưa kể cày xong phần cũ có khi mai lại phải đập đi viết lại theo ý mới của sếp nữa.

Trước khi tắt máy chỉ cần làm nhanh một việc cho đỡ quên thôi: lưu lại đoạn đang sửa dở (commit tạm hoặc note nhanh ra giấy), gạch vài dòng xem trong 18 comment kia chỗ nào bị requirement mới đụng tới rồi nhắn sếp hoặc tech lead khoan chốt PR vội để mai xử lý tiếp.

Tối rồi thì ra ngoài hít thở làm ly nước mát thôi chứ uống cà phê giờ này khéo lại thức trắng đêm nghĩ chuyện code đấy. Ngủ một giấc mai đầu óc tỉnh táo vào làm một mạch có khi gọn hơn hẳn tối nay.

---

### V5-01 — Mẫu 4

Ra làm ly cà phê đi ông, đừng cố nữa.

Đầu óc đang mụ mị mà ráng sửa nốt tối nay dễ đẻ thêm bug, mai tech lead lại comment tiếp thôi. Hơn nữa sếp vừa đổi requirement phút chót — ông cố dọn hết 18 chỗ kia theo logic cũ xong khéo mai lại phải đập đi sửa lại theo yêu cầu mới, vừa mệt vừa uổng công.

Trước khi gập máy, làm gọn hai việc này vài phút thôi để mai đỡ mất mạch:
- Đọc qua xem phần sếp đổi đụng tới chỗ nào đang sửa; nếu thấy điểm nào còn mập mờ thì nhắn hỏi lại luôn để mai vào việc khỏi phải chờ.
- Lưu tạm phần code đang làm dở và note nhanh vài dòng xem đang dừng ở đâu, khúc nào bị ảnh hưởng bởi req mới.

Xong xuôi thì đứng dậy đi uống cà phê cho nhẹ đầu. Sáng mai tỉnh táo xử lý cả req mới lẫn PR một thể nhanh và chuẩn hơn ngồi ráng tối nay nhiều.

---

### V5-01 — Mẫu 5

Ra làm ly cà phê đi ông ơi, trừ khi sếp bảo tối nay không sửa thì sập server, còn lại đừng cố.

Đầu đang mụ mị mà đâm đầu sửa 18 cái comment trên cái nền requirement vừa đổi rất dễ thành công cốc — vừa dễ phát sinh bug mới, vừa mất công sửa những chỗ lát nữa đọc lại req mới lại phải đập đi làm lại.

Trước khi gập máy, ông chỉ cần làm nhanh đúng hai việc tầm 5 phút cho nhẹ đầu rồi đi nghỉ:
1. Lưu tạm chỗ code đang sửa dở (commit WIP hoặc stash lại) rồi note nhanh vài dòng xem req mới ảnh hưởng tới phần nào — biết đâu đổi req xong lại gạch được bớt vài comment trong 18 chỗ kia.
2. Nhắn sếp một câu xác nhận đã nắm thông tin và hẹn sáng mai rà lại phạm vi sửa đổi trên PR.

Tối nay để não nghỉ, sáng mai đầu tỉnh vào xử lý một mạch có khi nhanh gấp đôi mà đỡ ức chế hơn nhiều.

---

### Phiếu chấm nhanh V5-01

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho V5-01:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca V5-02 — Thông báo cho người dùng cuối

- **Tiêu đề / Chủ đề:** Thông báo bảo trì kênh chuyển tiền liên ngân hàng 24/7 rạng sáng Chủ nhật
- **Đối tượng đọc:** Khách hàng dùng ứng dụng ngân hàng số
- **Mục đích giao tiếp:** Khách đọc một lần biết ngay khung giờ bảo trì, tính năng nào không bị ảnh hưởng, lệnh hẹn giờ xử lý ra sao và cần chuẩn bị gì.

### Yêu cầu & Văn bản nguồn

```text
Viết lại thông báo bảo trì dưới đây sang tiếng Việt tự nhiên, ngắn gọn, dễ nắm cho khách hàng mở app đọc trên điện thoại (giữ chính xác khung giờ, các tính năng bị dừng vs chạy bình thường, cách xử lý lệnh hẹn giờ và không tự bịa thêm ngày tháng hay số hotline):

Thông báo về việc thực hiện bảo trì định kỳ nâng cấp hạ tầng kết nối hệ thống chuyển mạch thanh toán liên ngân hàng

Kính gửi Quý khách hàng, nhằm mục tiêu nâng cao tính ổn định và tốc độ xử lý của hệ thống thanh toán điện tử phục vụ trải nghiệm giao dịch thông suốt, ngân hàng chúng tôi sẽ tiến hành công tác bảo trì nâng cấp kỹ thuật định kỳ vào khoảng thời gian từ 01:00 đến 03:30 rạng sáng Chủ nhật tới. Trong suốt khoảng thời gian triển khai công việc kỹ thuật nêu trên, dịch vụ chuyển tiền nhanh liên ngân hàng 24/7 ở cả chiều thực hiện giao dịch gửi đi lẫn tiếp nhận tiền đến tức thời sẽ tạm thời không khả dụng. Tuy nhiên, các hoạt động giao dịch chuyển khoản trong cùng hệ thống ngân hàng, các giao dịch thanh toán sử dụng thẻ vật lý hoặc thẻ điện tử, cũng như tính năng truy vấn số dư và xem lại lịch sử giao dịch vẫn được duy trì vận hành bình thường không gián đoạn. Đối với những lệnh chuyển tiền liên ngân hàng đã được khách hàng thiết lập lịch hẹn tự động trùng với khung giờ bảo trì, hệ thống sẽ giữ lệnh ở trạng thái chờ và tự động kích hoạt xử lý tiếp ngay sau mốc 03:30 khi quá trình nâng cấp hoàn tất. Kính mong Quý khách chủ động sắp xếp kế hoạch giao dịch tài chính cần thiết trước thời điểm nêu trên để tránh phát sinh bất tiện ngoài dự kiến.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Khách hàng đọc trên điện thoại mất bao lâu để thấy ngay khung giờ bảo trì (01:00–03:30 rạng sáng Chủ nhật tới) và dịch vụ duy nhất bị dừng?
- 2. Những giao dịch nào vẫn chạy bình thường, và lệnh chuyển tiền liên ngân hàng hẹn giờ trùng giờ bảo trì sẽ được xử lý thế nào sau 03:30?

### V5-02 — Mẫu 1

**Thông báo bảo trì hệ thống: 01:00 – 03:30 rạng sáng Chủ nhật tới**

Để hệ thống thanh toán hoạt động ổn định và nhanh hơn, ngân hàng sẽ bảo trì định kỳ từ **01:00 đến 03:30 rạng sáng Chủ nhật tới**.

**Tạm dừng trong khung giờ này:**
- Chuyển tiền nhanh liên ngân hàng 24/7 (cả chiều gửi đi lẫn nhận tiền đến tức thời).

**Vẫn hoạt động bình thường:**
- Chuyển khoản trong cùng hệ thống ngân hàng.
- Thanh toán bằng thẻ vật lý và thẻ điện tử.
- Kiểm tra số dư và xem lịch sử giao dịch.

**Với lệnh chuyển tiền liên ngân hàng đã hẹn giờ:**
Các lệnh trùng khung giờ bảo trì sẽ được giữ ở trạng thái chờ và tự động xử lý tiếp ngay sau 03:30 khi nâng cấp hoàn tất.

Quý khách vui lòng chủ động sắp xếp các giao dịch cần thiết trước 01:00 để tránh bất tiện.

---

### V5-02 — Mẫu 2

**Thông báo bảo trì chuyển tiền nhanh liên ngân hàng**

Từ **01:00 đến 03:30 rạng sáng Chủ nhật tới**, ngân hàng sẽ bảo trì định kỳ để nâng cấp tốc độ và độ ổn định cho hệ thống thanh toán.

**Ảnh hưởng trong thời gian bảo trì:**
- **Tạm dừng:** Chuyển tiền nhanh liên ngân hàng 24/7 (cả chiều chuyển đi và nhận tiền đến tức thời).
- **Hoạt động bình thường:** Chuyển khoản cùng hệ thống ngân hàng, thanh toán bằng thẻ vật lý hoặc thẻ điện tử, kiểm tra số dư và xem lịch sử giao dịch.

**Với lệnh chuyển tiền đã hẹn giờ:**
Các lệnh chuyển tiền liên ngân hàng đặt lịch tự động trùng khung giờ bảo trì sẽ được giữ ở trạng thái chờ và tự động xử lý ngay sau **03:30**, khi quá trình nâng cấp hoàn tất.

Quý khách vui lòng chủ động sắp xếp các giao dịch liên ngân hàng cần thiết trước **01:00** để tránh gián đoạn. Cảm ơn Quý khách!

---

### V5-02 — Mẫu 3

**Thông báo bảo trì hệ thống định kỳ**

Để hệ thống thanh toán hoạt động ổn định và nhanh hơn, ngân hàng sẽ bảo trì từ **01:00 đến 03:30 rạng sáng Chủ nhật tới**.

**Dịch vụ tạm ngưng trong thời gian này:**
- Chuyển tiền nhanh liên ngân hàng 24/7 (cả chiều gửi đi lẫn nhận tiền đến tức thời).

**Dịch vụ vẫn hoạt động bình thường:**
- Chuyển khoản trong cùng hệ thống ngân hàng.
- Thanh toán bằng thẻ vật lý hoặc thẻ điện tử.
- Kiểm tra số dư và xem lịch sử giao dịch.

**Với lệnh chuyển tiền liên ngân hàng đã hẹn lịch tự động:**
- Các lệnh trùng khung giờ bảo trì sẽ được giữ ở trạng thái chờ và tự động xử lý tiếp ngay sau **03:30**, khi việc nâng cấp hoàn tất.

Quý khách vui lòng chủ động sắp xếp các giao dịch cần thiết trước giờ bảo trì để tránh bất tiện.

---

### V5-02 — Mẫu 4

**Bảo trì hệ thống chuyển tiền nhanh 24/7 (01:00 – 03:30 rạng sáng Chủ nhật tới)**

Để giao dịch ổn định và nhanh hơn, ngân hàng sẽ nâng cấp hệ thống kết nối thanh toán liên ngân hàng từ **01:00 đến 03:30 rạng sáng Chủ nhật tới**.

Trong khung giờ này:
- **Tạm ngưng:** Chuyển tiền nhanh liên ngân hàng 24/7 (cả chiều chuyển đi và nhận tiền đến tức thời).
- **Vẫn hoạt động bình thường:** Chuyển khoản cùng ngân hàng, thanh toán bằng thẻ vật lý hoặc thẻ điện tử, kiểm tra số dư và xem lịch sử giao dịch.

**Với lệnh đã hẹn giờ:** Các lệnh chuyển tiền liên ngân hàng đã đặt lịch tự động trùng giờ bảo trì sẽ được giữ ở trạng thái chờ và tự động xử lý tiếp ngay sau **03:30** khi nâng cấp xong.

Quý khách vui lòng chủ động sắp xếp các giao dịch cần thiết trước 01:00 để tránh gián đoạn.

---

### V5-02 — Mẫu 5

**Thông báo bảo trì định kỳ hệ thống thanh toán liên ngân hàng**

Từ **01:00 đến 03:30 rạng sáng Chủ nhật tới**, ngân hàng sẽ bảo trì, nâng cấp kết nối chuyển mạch liên ngân hàng nhằm giúp giao dịch nhanh và ổn định hơn.

**Trong khung giờ bảo trì:**
- **Tạm ngừng:** Dịch vụ chuyển tiền nhanh liên ngân hàng 24/7 (cả chiều gửi đi và nhận tiền đến tức thời).
- **Hoạt động bình thường:** Chuyển khoản cùng ngân hàng, thanh toán bằng thẻ vật lý hoặc thẻ điện tử, tra cứu số dư và xem lịch sử giao dịch.

**Với lệnh chuyển tiền liên ngân hàng đã hẹn lịch tự động:** Nếu trùng vào khung giờ trên, hệ thống sẽ giữ lệnh ở trạng thái chờ và tự động xử lý tiếp ngay sau **03:30** khi nâng cấp hoàn tất.

Quý khách vui lòng chủ động sắp xếp các giao dịch cần thiết trước **01:00 rạng sáng Chủ nhật tới** để tránh bất tiện.

---

### Phiếu chấm nhanh V5-02

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho V5-02:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca V5-03 — Giao tiếp công việc

- **Tiêu đề / Chủ đề:** Email xin PM và Vận hành chốt một trong hai phương án migration bảng hóa đơn
- **Đối tượng đọc:** Product Manager và Trưởng nhóm Vận hành
- **Mục đích giao tiếp:** Trình bày gọn rõ 2 phương án migration và đánh đổi để PM & Vận hành chốt đúng 1 lựa chọn trước 17:00 thứ Tư.

### Yêu cầu & Văn bản nguồn

```text
Viết lại email dưới đây sao cho PM và Trưởng nhóm Vận hành mở ra đọc trong 30 giây là nắm ngay cần chốt gì, hạn chót khi nào, và so sánh được hai phương án cùng phần việc kéo theo (giữ nguyên toàn bộ thông số giờ/ngày, tên anh Minh và không tự chọn phương án thay người đọc):

Chào anh Minh và team Vận hành, trước hết cảm ơn mọi người đã phối hợp rất tốt trong giai đoạn chuẩn bị nâng cấp hệ thống lưu trữ hóa đơn vừa qua. Như team kỹ thuật có trao đổi sơ bộ ở buổi họp tuần trước thì sang cuối tuần này tụi em bắt buộc phải thực hiện chuyển đổi dữ liệu bảng hóa đơn sang cấu trúc mới để tránh nghẽn dung lượng đầu tháng tới, nhưng hiện tại đang có hai hướng thực thi với những đánh đổi vận hành khá khác nhau nên rất cần bên Sản phẩm và Vận hành chốt giúp một phương án trước 17:00 chiều thứ Tư tuần này để tụi em kịp chuẩn bị script kiểm thử. Cụ thể, nếu đi theo Phương án 1 thì hệ thống sẽ tạm khóa riêng tính năng xuất báo cáo kế toán trong đúng 2 tiếng từ 00:00 đến 02:00 sáng thứ Bảy để chạy chuyển đổi dứt điểm một lần, đổi lại ngay sau 02:00 dữ liệu báo cáo sẽ khớp chuẩn 100% và bên Vận hành chỉ cần gửi thông báo trước cho các kế toán đối tác không chạy xuất file trong khung giờ đêm đó. Còn nếu mọi người không muốn gián đoạn bất cứ phút nào của tính năng xuất báo cáo thì có thể chọn Phương án 2 là chạy đồng bộ song song kéo dài trong 3 ngày từ thứ Bảy đến hết thứ Hai, tuy nhiên trong suốt 3 ngày chạy song song này báo cáo phát sinh có thể xuất hiện độ lệch tạm thời giữa nhóm tài khoản đã chuyển trước và nhóm chưa chuyển xong cho tới khi hệ thống đối soát khớp lại toàn bộ sau ngày thứ Ba, lúc đó nhờ đội CSKH và Vận hành nắm thông tin để giải đáp nếu có đối tác thắc mắc. Mong anh chị phản hồi sớm giúp team kỹ thuật chốt phương án trước hạn chiều thứ Tư ạ.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. PM và Trưởng nhóm Vận hành cần chốt phương án trước hạn nào, và hai phương án khác nhau cốt lõi ở điểm nào (khóa 2 giờ vs lệch số tạm thời 3 ngày)?
- 2. Nếu chọn Phương án 1 hoặc Phương án 2, team Vận hành / CSKH có trách nhiệm gì kéo theo?

### V5-03 — Mẫu 1

**Tiêu đề:** [Cần chốt trước 17:00 thứ Tư] Phương án chuyển đổi dữ liệu bảng hóa đơn cuối tuần này

Chào anh Minh và team Vận hành,

Cuối tuần này, team kỹ thuật bắt buộc phải chuyển đổi dữ liệu bảng hóa đơn sang cấu trúc mới để tránh nghẽn dung lượng đầu tháng tới (như đã trao đổi sơ bộ ở buổi họp tuần trước). Cảm ơn mọi người đã phối hợp rất tốt trong giai đoạn chuẩn bị nâng cấp hệ thống lưu trữ hóa đơn vừa qua.

Hiện có hai hướng triển khai với mức ảnh hưởng vận hành khác nhau. Nhờ anh Minh cùng bên Sản phẩm và Vận hành **chốt giúp 1 phương án trước 17:00 chiều thứ Tư tuần này** để tụi em kịp chuẩn bị script kiểm thử:

| Tiêu chí | Phương án 1: Chuyển đổi dứt điểm | Phương án 2: Chạy đồng bộ song song |
|---|---|---|
| **Thời gian thực hiện** | Chạy một lần trong đúng **2 tiếng**, từ **00:00 đến 02:00 sáng thứ Bảy** | Kéo dài **3 ngày**, từ **thứ Bảy đến hết thứ Hai** |
| **Ảnh hưởng xuất báo cáo** | Tạm khóa riêng tính năng xuất báo cáo kế toán trong 2 tiếng trên | Không gián đoạn bất cứ phút nào |
| **Độ khớp dữ liệu** | Ngay sau **02:00**, dữ liệu báo cáo khớp chuẩn **100%** | Trong suốt 3 ngày chạy song song, báo cáo phát sinh **có thể** xuất hiện độ lệch tạm thời giữa nhóm tài khoản đã chuyển trước và nhóm chưa chuyển xong, cho tới khi hệ thống đối soát khớp lại toàn bộ **sau ngày thứ Ba** |
| **Phần việc phối hợp** | Vận hành gửi thông báo trước cho các kế toán đối tác không chạy xuất file trong khung giờ đêm **00:00–02:00 sáng thứ Bảy** | Đội CSKH và Vận hành nắm thông tin để giải đáp nếu có đối tác thắc mắc |

Nhờ anh Minh và mọi người phản hồi sớm giúp team kỹ thuật chốt phương án trước **17:00 chiều thứ Tư** ạ.

Trân trọng,
Team Kỹ thuật

---

### V5-03 — Mẫu 2

**Tiêu đề:** [Cần chốt trước 17:00 thứ Tư] Phương án chuyển đổi dữ liệu bảng hóa đơn cuối tuần này

Chào anh Minh và team Vận hành,

Như đã trao đổi sơ bộ ở buổi họp tuần trước, cuối tuần này team kỹ thuật bắt buộc phải chuyển đổi dữ liệu bảng hóa đơn sang cấu trúc mới để tránh nghẽn dung lượng đầu tháng tới.

Để tụi em kịp chuẩn bị script kiểm thử, nhờ bên Sản phẩm và Vận hành **chốt giúp 1 trong 2 phương án dưới đây trước 17:00 chiều thứ Tư tuần này**:

| Tiêu chí | Phương án 1: Chuyển đổi dứt điểm một lần | Phương án 2: Chạy đồng bộ song song |
|---|---|---|
| **Thời gian & gián đoạn tính năng** | Tạm khóa **riêng** tính năng xuất báo cáo kế toán trong đúng **2 tiếng** (**00:00 đến 02:00 sáng thứ Bảy**). | **Không gián đoạn** tính năng xuất báo cáo; chạy đồng bộ song song trong **3 ngày** (**từ thứ Bảy đến hết thứ Hai**). |
| **Độ chính xác dữ liệu báo cáo** | Ngay sau **02:00**, dữ liệu báo cáo khớp chuẩn **100%**. | Trong suốt **3 ngày** chạy song song, báo cáo phát sinh có thể xuất hiện độ lệch tạm thời giữa nhóm tài khoản đã chuyển trước và nhóm chưa chuyển xong, cho tới khi hệ thống đối soát khớp lại toàn bộ **sau ngày thứ Ba**. |
| **Phần việc kéo theo** | **Vận hành:** Gửi thông báo trước cho các kế toán đối tác không chạy xuất file trong khung giờ đêm đó. | **CSKH và Vận hành:** Nắm thông tin để giải đáp nếu có đối tác thắc mắc. |

Mong anh Minh và mọi người phản hồi sớm phương án lựa chọn trước hạn **17:00 chiều thứ Tư tuần này**. Cảm ơn mọi người đã phối hợp rất tốt trong giai đoạn chuẩn bị nâng cấp hệ thống vừa qua.

---

### V5-03 — Mẫu 3

**Tiêu đề:** [Cần chốt trước 17:00 thứ Tư] Phương án chuyển đổi dữ liệu bảng hóa đơn cuối tuần này

Chào anh Minh và team Vận hành,

Cảm ơn mọi người đã phối hợp chuẩn bị cho đợt nâng cấp hệ thống lưu trữ hóa đơn vừa qua. Như đã trao đổi sơ bộ ở buổi họp tuần trước, cuối tuần này team kỹ thuật bắt buộc phải chuyển đổi dữ liệu bảng hóa đơn sang cấu trúc mới để tránh nghẽn dung lượng đầu tháng tới.

**Cần chốt:** Bên Sản phẩm và Vận hành chọn **1 trong 2 phương án** triển khai dưới đây **trước 17:00 chiều thứ Tư tuần này** để tụi em kịp chuẩn bị script kiểm thử.

| Tiêu chí | Phương án 1: Chuyển đổi dứt điểm | Phương án 2: Chạy đồng bộ song song |
| :--- | :--- | :--- |
| **Thời gian thực hiện** | Đúng **2 tiếng**, từ **00:00 đến 02:00 sáng thứ Bảy** | Kéo dài **3 ngày**, từ **thứ Bảy đến hết thứ Hai** |
| **Tính năng xuất báo cáo kế toán** | **Tạm khóa riêng tính năng này** trong 2 tiếng nêu trên | **Không gián đoạn** phút nào |
| **Dữ liệu báo cáo** | Khớp chuẩn **100%** ngay sau **02:00** sáng thứ Bảy | Trong 3 ngày chạy song song **có thể xuất hiện độ lệch tạm thời** giữa nhóm tài khoản đã chuyển trước và nhóm chưa chuyển xong, cho tới khi hệ thống đối soát khớp lại toàn bộ **sau ngày thứ Ba** |
| **Phần việc kéo theo** | **Vận hành** gửi thông báo trước cho các kế toán đối tác không chạy xuất file trong khung giờ đêm đó | **CSKH và Vận hành** nắm thông tin để giải đáp nếu có đối tác thắc mắc |

Nhờ anh Minh và team Vận hành phản hồi sớm giúp tụi em phương án lựa chọn trước **17:00 chiều thứ Tư tuần này** nhé.

Cảm ơn anh chị và mọi người!

---

### V5-03 — Mẫu 4

**Tiêu đề:** [Cần chốt trước 17:00 thứ Tư] Phương án chuyển đổi dữ liệu bảng hóa đơn cuối tuần này

Chào anh Minh và team Vận hành,

Cảm ơn mọi người đã phối hợp tốt trong giai đoạn chuẩn bị nâng cấp hệ thống lưu trữ hóa đơn vừa qua.

Như đã trao đổi sơ bộ ở buổi họp tuần trước, cuối tuần này team kỹ thuật bắt buộc phải chuyển đổi dữ liệu bảng hóa đơn sang cấu trúc mới để tránh nghẽn dung lượng đầu tháng tới. Nhờ bên **Sản phẩm và Vận hành chốt giúp 1 trong 2 phương án** dưới đây **trước 17:00 chiều thứ Tư tuần này** để tụi em kịp chuẩn bị script kiểm thử.

| Tiêu chí | Phương án 1: Chuyển đổi dứt điểm | Phương án 2: Đồng bộ song song |
|---|---|---|
| **Thời gian chạy** | Đúng **2 tiếng**, từ **00:00 đến 02:00 sáng thứ Bảy** (chạy dứt điểm 1 lần). | Kéo dài **3 ngày**, từ **thứ Bảy đến hết thứ Hai**; hệ thống đối soát khớp lại toàn bộ **sau ngày thứ Ba**. |
| **Tính năng xuất báo cáo kế toán** | **Tạm khóa riêng** tính năng này trong đúng 2 tiếng (00:00–02:00 sáng thứ Bảy). | **Không gián đoạn** bất cứ phút nào. |
| **Độ khớp dữ liệu báo cáo** | Ngay sau **02:00**, dữ liệu báo cáo khớp chuẩn **100%**. | Trong suốt 3 ngày chạy song song, báo cáo phát sinh có thể xuất hiện **độ lệch tạm thời** giữa nhóm tài khoản đã chuyển trước và nhóm chưa chuyển xong (đến khi đối soát xong sau ngày thứ Ba). |
| **Phần việc kéo theo** | **Vận hành** gửi thông báo trước cho các kế toán đối tác không chạy xuất file trong khung giờ đêm đó (00:00–02:00 sáng thứ Bảy). | **CSKH và Vận hành** nắm thông tin để giải đáp nếu có đối tác thắc mắc. |

Mong anh Minh và team Vận hành phản hồi sớm phương án lựa chọn **trước 17:00 chiều thứ Tư tuần này** giúp team kỹ thuật ạ.

---

### V5-03 — Mẫu 5

**Tiêu đề:** [Cần chốt trước 17:00 thứ Tư] Chọn phương án chuyển đổi dữ liệu bảng hóa đơn cuối tuần này

Chào anh Minh và team Vận hành,

Cảm ơn mọi người đã phối hợp tốt trong giai đoạn chuẩn bị nâng cấp hệ thống lưu trữ hóa đơn vừa qua. Như team kỹ thuật đã trao đổi sơ bộ tại buổi họp tuần trước, cuối tuần này hệ thống bắt buộc phải chuyển đổi dữ liệu bảng hóa đơn sang cấu trúc mới để tránh nghẽn dung lượng vào đầu tháng tới.

Nhờ anh Minh (Sản phẩm) và team Vận hành chốt giúp **1 trong 2 phương án** dưới đây **trước 17:00 chiều thứ Tư tuần này** để team kỹ thuật kịp chuẩn bị script kiểm thử:

| Tiêu chí | Phương án 1: Chuyển đổi dứt điểm một lần | Phương án 2: Chạy đồng bộ song song |
|---|---|---|
| **Thời gian thực hiện** | Đúng **2 tiếng**, từ **00:00 đến 02:00 sáng thứ Bảy** | Kéo dài **3 ngày**, từ **thứ Bảy đến hết thứ Hai** |
| **Ảnh hưởng tính năng xuất báo cáo kế toán** | Tạm khóa riêng tính năng xuất báo cáo kế toán trong 2 tiếng nêu trên | Không gián đoạn bất cứ phút nào |
| **Trạng thái dữ liệu báo cáo** | Ngay sau **02:00 sáng thứ Bảy**, dữ liệu báo cáo khớp chuẩn **100%** | Trong suốt 3 ngày chạy song song, báo cáo phát sinh có thể xuất hiện độ lệch tạm thời giữa nhóm tài khoản đã chuyển trước và nhóm chưa chuyển xong, cho tới khi hệ thống đối soát khớp lại toàn bộ **sau ngày thứ Ba** |
| **Phần việc kéo theo** | **Vận hành:** Gửi thông báo trước cho các kế toán đối tác không chạy xuất file trong khung giờ đêm **00:00 – 02:00 sáng thứ Bảy** | **CSKH và Vận hành:** Nắm thông tin để giải đáp nếu có đối tác thắc mắc trong thời gian chạy song song |

Mong anh Minh và team Vận hành phản hồi sớm giúp team kỹ thuật chốt phương án trước hạn **17:00 chiều thứ Tư tuần này**.

---

### Phiếu chấm nhanh V5-03

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho V5-03:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca V5-04 — Giải thích kỹ thuật

- **Tiêu đề / Chủ đề:** Giải thích Rate Limiting vs Circuit Breaker từ sự cố đối tác chậm 15 giây
- **Đối tượng đọc:** Product Manager và kỹ sư Backend mới vào nghề
- **Mục đích giao tiếp:** Dẫn từ vấn đề nghẽn kết nối thực tế khi đối tác chậm để giải thích rõ Rate Limiting và Circuit Breaker khác nhau chỗ nào và phối hợp ra sao.

### Yêu cầu & Văn bản nguồn

```text
Hãy viết lại phần giải thích kỹ thuật dưới đây cho PM và lập trình viên mới hiểu rõ bản chất khác nhau và cách phối hợp giữa Rate Limiting và Circuit Breaker (giữ chính xác các thông số 15 giây, dưới 1 giây và các trạng thái Open / Half-Open trong nguồn, không tự thêm số liệu cooldown cụ thể ngoài nguồn):

Để phân biệt hai cơ chế phòng vệ phổ biến trong hệ thống microservice là Rate Limiting và Circuit Breaker, hãy hình dung tình huống khi dịch vụ đối tác bên ngoài mà hệ thống của bạn gọi tới bỗng nhiên phản hồi chậm tới 15 giây cho mỗi yêu cầu thay vì dưới 1 giây như bình thường. Nếu chỉ sử dụng Rate Limiting, cơ chế này thực hiện việc khống chế tổng số lượng yêu cầu được phép đi qua trong một đơn vị thời gian nhất định nhằm ngăn tình trạng lưu lượng tăng đột biến làm quá tải hạ tầng; tuy nhiên, bản thân Rate Limiting không có khả năng nhận biết được đầu bên kia đang gặp sự cố treo chậm kéo dài, dẫn đến việc các yêu cầu lọt qua ngưỡng cho phép vẫn tiếp tục bị giữ kết nối chờ đủ 15 giây, làm cạn kiệt dần hồ chứa kết nối của máy chủ nội bộ và có thể kéo sập lan sang các chức năng khác. Ngược lại, Circuit Breaker hoạt động tương tự một cầu dao tự ngắt ở chiều gọi ra bằng cách giám sát tỷ lệ thất bại hoặc quá thời gian chờ liên tiếp; khi mức độ lỗi chạm ngưỡng bất thường, cầu dao chuyển sang trạng thái Mở (Open) để từ chối tức thì hoặc chuyển sang phương án dự phòng mà không giữ chờ kết nối tới đối tác nữa, sau đó mới chuyển qua trạng thái Nửa mở (Half-Open) để cho một vài yêu cầu thăm dò đi qua kiểm tra khả năng hồi phục trước khi khôi phục trạng thái bình thường. Tóm lại, Rate Limiting giải quyết bài toán kiểm soát lưu lượng theo nhịp độ ổn định còn Circuit Breaker giải quyết bài toán ngắt ly hợp để chặn hiệu ứng sập dây chuyền khi phụ thuộc ngoài gặp sự cố.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Khi API đối tác bỗng chậm từ dưới 1 giây lên 15 giây/request, vì sao chỉ dùng Rate Limiting vẫn có thể khiến hệ thống nội bộ sập dây chuyền?
- 2. Circuit Breaker hoạt động ở trạng thái Open và Half-Open khác nhau thế nào, và vì sao cần phối hợp cả hai cơ chế?

### V5-04 — Mẫu 1

**Rate Limiting** và **Circuit Breaker** đều là cơ chế bảo vệ hệ thống microservice, nhưng giải quyết hai bài toán khác nhau:

* **Rate Limiting (kiểm soát lưu lượng):** Đóng vai trò như van điều tiết, giới hạn tổng số lượng yêu cầu được phép đi qua trong một đơn vị thời gian nhất định để giữ nhịp độ ổn định và ngăn lưu lượng tăng đột biến làm quá tải hạ tầng.
* **Circuit Breaker (ngắt mạch khi có sự cố):** Đóng vai trò như cầu dao tự ngắt ở chiều gọi ra, giám sát tỷ lệ thất bại hoặc tình trạng quá thời gian chờ (timeout) liên tiếp để chặn hiệu ứng sập dây chuyền khi dịch vụ phụ thuộc bên ngoài gặp sự cố.

### Vì sao Rate Limiting không đủ khi đối tác phản hồi chậm?

Hãy hình dung hệ thống microservice của bạn gọi tới một dịch vụ đối tác bên ngoài. Bình thường, đối tác phản hồi **dưới 1 giây** cho mỗi yêu cầu, nhưng bỗng nhiên gặp sự cố khiến thời gian phản hồi kéo dài tới **15 giây**.

Nếu hệ thống chỉ dùng **Rate Limiting**, cơ chế này chỉ kiểm soát số lượng yêu cầu được phép đi qua theo đơn vị thời gian mà **không nhận biết được đầu bên kia đang bị treo chậm kéo dài**. Hậu quả là:

1. Các yêu cầu nằm trong ngưỡng cho phép vẫn tiếp tục được gửi tới đối tác.
2. Mỗi yêu cầu như vậy bị giữ kết nối chờ đủ **15 giây**.
3. Hồ chứa kết nối (connection pool) của máy chủ nội bộ bị cạn kiệt dần, dẫn đến nguy cơ kéo sập lan sang các chức năng khác trong hệ thống.

### Circuit Breaker xử lý tình huống này như thế nào?

Khác với Rate Limiting, **Circuit Breaker** theo dõi trực tiếp sức khỏe của chiều gọi ra dựa trên tỷ lệ thất bại hoặc tình trạng quá thời gian chờ liên tiếp và chuyển đổi qua các trạng thái sau:

* **Trạng thái bình thường:** Các yêu cầu được gửi sang đối tác bình thường.
* **Trạng thái Mở (Open):** Khi mức độ lỗi hoặc quá thời gian chờ chạm ngưỡng bất thường, cầu dao tự ngắt sang trạng thái **Open**. Mọi yêu cầu gọi ra lúc này bị từ chối tức thì hoặc chuyển sang phương án dự phòng (fallback), **không giữ kết nối chờ** đối tác nữa để bảo vệ máy chủ nội bộ.
* **Trạng thái Nửa mở (Half-Open):** Sau đó, cầu dao chuyển sang trạng thái **Half-Open** để cho một vài yêu cầu thăm dò đi qua. Bước này giúp kiểm tra xem đối tác đã hồi phục hay chưa trước khi khôi phục lại trạng thái bình thường.

### Cách phối hợp giữa Rate Limiting và Circuit Breaker

Trong thực tế, hai cơ chế này bổ trợ cho nhau thành hai lớp phòng vệ liên hoàn:

* **Rate Limiting giữ nhịp độ ổn định:** Ngăn hệ thống và hạ tầng bị quá tải trước các đợt lưu lượng tăng đột biến ở trạng thái bình thường.
* **Circuit Breaker bảo vệ tài nguyên khi phụ thuộc ngoài gặp sự cố:** Ngay cả khi lưu lượng đã được Rate Limiting giữ ở mức cho phép, nếu dịch vụ đối tác bị treo chậm (chẳng hạn vọt từ **dưới 1 giây** lên **15 giây**) hoặc lỗi liên tiếp, Circuit Breaker sẽ ngắt mạch ở trạng thái **Open** để những yêu cầu lọt qua Rate Limiting không bị giữ chờ cạn kiệt kết nối. Nhờ đó, các chức năng khác của hệ thống vẫn an toàn trong lúc chờ đối tác hồi phục qua trạng thái **Half-Open**.

---

### V5-04 — Mẫu 2

Cả **Rate Limiting** và **Circuit Breaker** đều có thể chặn yêu cầu (request), nên lập trình viên mới và PM rất dễ nhầm hai cơ chế này làm một. Cách dễ nhất để phân biệt là đặt chúng vào một sự cố thực tế.

Hãy hình dung hệ thống của bạn đang gọi sang một dịch vụ đối tác bên ngoài. Bình thường đối tác phản hồi **dưới 1 giây**, nhưng bỗng nhiên gặp sự cố và phản hồi chậm tới **15 giây** cho mỗi yêu cầu.

### 1. Nếu chỉ dùng Rate Limiting: hệ thống vẫn có thể sập vì chờ quá lâu
**Rate Limiting** giới hạn tổng số yêu cầu được phép đi qua trong một khoảng thời gian nhất định, nhằm ngăn lưu lượng tăng đột biến làm quá tải hạ tầng.

Tuy nhiên, Rate Limiting chỉ đếm số lượng chứ không nhận biết được đối tác bên kia đang bị chậm kéo dài. Vì vậy, những yêu cầu vẫn nằm trong ngưỡng cho phép sẽ tiếp tục được gửi đi và bị giữ kết nối chờ đủ **15 giây**. Khi nhiều kết nối bị treo như vậy cùng lúc, lượng kết nối sẵn có của máy chủ nội bộ (*connection pool*) sẽ cạn dần, từ đó có thể kéo sập lan sang các chức năng khác.

### 2. Circuit Breaker: cầu dao tự ngắt để chặn sập dây chuyền
**Circuit Breaker** hoạt động ở chiều gọi ra giống như một cầu dao điện tự ngắt. Thay vì chỉ đếm lưu lượng, nó giám sát tỷ lệ lỗi hoặc số lần quá thời gian chờ (*timeout*) liên tiếp khi gọi sang đối tác:

- **Trạng thái Open (Mở):** Khi mức độ lỗi chạm ngưỡng bất thường, cầu dao lập tức ngắt mạch. Các yêu cầu mới sẽ bị từ chối tức thì hoặc chuyển sang phương án dự phòng (*fallback*) thay vì giữ kết nối chờ đối tác.
- **Trạng thái Half-Open (Nửa mở):** Sau một khoảng thời gian tạm ngắt, cầu dao chuyển sang trạng thái này để cho một vài yêu cầu thăm dò đi qua kiểm tra xem đối tác đã hồi phục chưa, rồi mới khôi phục trạng thái bình thường.

### 3. Bản chất khác nhau và cách phối hợp
- **Khác nhau về bản chất:** **Rate Limiting** giữ cho lưu lượng đi theo nhịp độ ổn định để hạ tầng không bị ngộp khi lượng yêu cầu tăng vọt; còn **Circuit Breaker** ngắt kết nối kịp thời ở chiều gọi ra khi dịch vụ phụ thuộc bên ngoài gặp sự cố, tránh hiệu ứng sập dây chuyền.
- **Phối hợp cùng nhau:** Hai cơ chế này không thay thế nhau mà bổ trợ thành hai lớp bảo vệ. **Rate Limiting** chặn các đợt tăng lưu lượng đột biến để giữ tải ở mức hệ thống chịu được; còn **Circuit Breaker** theo dõi phản hồi thực tế từ đối tác để ngắt mạch ngay nếu các yêu cầu đã qua được Rate Limiting vẫn bị treo chậm kéo dài, giữ cho tài nguyên kết nối nội bộ không bị rút cạn.

---

### V5-04 — Mẫu 3

**Rate Limiting** và **Circuit Breaker** đều là các cơ chế bảo vệ phổ biến trong kiến trúc microservice, nhưng giải quyết hai bài toán khác nhau. Cách dễ nhất để phân biệt bản chất và thấy rõ vai trò của từng cơ chế là đặt chúng vào cùng một sự cố thực tế.

### Tình huống thực tế
Hệ thống của bạn cần gọi sang một dịch vụ đối tác bên ngoài. Bình thường, mỗi yêu cầu phản hồi **dưới 1 giây**, nhưng hôm nay đối tác bỗng gặp sự cố và phản hồi chậm tới **15 giây** cho mỗi yêu cầu.

### Cách từng cơ chế phản ứng

**1. Rate Limiting — Kiểm soát lưu lượng theo nhịp độ ổn định**
Rate Limiting giới hạn tổng số yêu cầu được phép đi qua trong một khoảng thời gian nhằm ngăn tình trạng lưu lượng tăng đột biến làm quá tải hạ tầng.

Tuy nhiên, bản thân Rate Limiting không có khả năng nhận biết dịch vụ đối tác đang bị treo chậm kéo dài. Trong tình huống trên, các yêu cầu nằm trong ngưỡng cho phép vẫn tiếp tục được gửi đi và giữ kết nối chờ đủ **15 giây**. Khi nhiều kết nối bị giữ chờ cùng lúc, nguồn kết nối sẵn có (*connection pool*) của máy chủ nội bộ sẽ dần cạn kiệt và **có thể** kéo sập lan sang các chức năng khác.

**2. Circuit Breaker — Cầu dao tự ngắt ở chiều gọi ra**
Ngược lại, Circuit Breaker hoạt động tương tự một cầu dao tự ngắt ở chiều gọi ra bằng cách giám sát tỷ lệ thất bại hoặc tình trạng quá thời gian chờ liên tiếp. Khi mức độ lỗi chạm ngưỡng bất thường, cầu dao chuyển đổi trạng thái để bảo vệ hệ thống:
- **Mở (Open):** Ngừng giữ kết nối chờ tới đối tác; các yêu cầu lúc này sẽ bị từ chối tức thì hoặc chuyển sang phương án dự phòng.
- **Nửa mở (Half-Open):** Sau đó, cầu dao chuyển sang trạng thái này để cho một vài yêu cầu thăm dò đi qua, kiểm tra khả năng hồi phục của đối tác trước khi đưa hệ thống trở lại trạng thái bình thường.

### Bản chất khác nhau và cách phối hợp

| Tiêu chí | Rate Limiting | Circuit Breaker |
|---|---|---|
| **Bài toán giải quyết** | Kiểm soát lưu lượng theo nhịp độ ổn định để tránh quá tải hạ tầng. | Ngắt kết nối kịp thời ở chiều gọi ra để chặn hiệu ứng sập dây chuyền khi phụ thuộc ngoài gặp sự cố. |
| **Cách xử lý khi có sự cố chậm/lỗi** | Không phát hiện sự cố của đối tác; yêu cầu lọt qua ngưỡng vẫn tiếp tục chờ phản hồi. | Giám sát lỗi hoặc quá thời gian chờ; khi chạm ngưỡng bất thường sẽ từ chối ngay hoặc chuyển sang phương án dự phòng. |

**Cách phối hợp trong hệ thống:**
Hai cơ chế này không thay thế mà bổ trợ cho nhau: **Rate Limiting** giữ cho lượng yêu cầu đi qua ở nhịp độ ổn định để tránh quá tải hạ tầng khi lưu lượng tăng đột biến, còn **Circuit Breaker** đứng ở chiều gọi ra để chủ động ngắt kết nối khi đối tác gặp sự cố treo chậm hoặc lỗi liên tiếp. Nhờ kết hợp cả hai, hệ thống vừa điều tiết được tải đầu vào, vừa không bị giữ kết nối chờ gây cạn kiệt tài nguyên và sập dây chuyền theo dịch vụ phụ thuộc.

---

### V5-04 — Mẫu 4

Trong hệ thống microservice, **Rate Limiting** và **Circuit Breaker** đều là cơ chế phòng vệ nhưng giải quyết hai bài toán khác nhau: **Rate Limiting** kiểm soát lưu lượng yêu cầu theo nhịp độ ổn định để tránh quá tải hạ tầng, còn **Circuit Breaker** giám sát sức khỏe của dịch vụ đối tác ở chiều gọi ra để ngắt kết nối kịp thời khi đối tác gặp sự cố, chặn hiệu ứng sập dây chuyền.

### 1. Tình huống minh họa: Khi đối tác bỗng nhiên phản hồi chậm

Hãy hình dung hệ thống của bạn gọi sang một dịch vụ đối tác bên ngoài. Bình thường đối tác phản hồi **dưới 1 giây**, nhưng bỗng nhiên gặp sự cố khiến mỗi yêu cầu mất tới **15 giây** mới có phản hồi.

- **Nếu chỉ dùng Rate Limiting:**
  Rate Limiting giới hạn tổng số yêu cầu được phép đi qua trong một khoảng thời gian nhất định để ngăn lưu lượng tăng đột biến làm quá tải hạ tầng. Tuy nhiên, cơ chế này **không nhận biết được đối tác đang bị treo chậm kéo dài**.
  Do đó, những yêu cầu nằm trong ngưỡng cho phép vẫn tiếp tục được gửi sang đối tác và phải giữ kết nối chờ đủ **15 giây**. Khi nhiều yêu cầu bị treo chờ cùng lúc, **connection pool (nhóm kết nối dùng chung)** của máy chủ nội bộ sẽ cạn kiệt dần, làm các chức năng khác mất kết nối để xử lý và có thể kéo sập lan toàn hệ thống.

- **Khi sử dụng Circuit Breaker:**
  Circuit Breaker hoạt động ở chiều gọi ra giống như một cầu dao tự ngắt, liên tục theo dõi tỷ lệ thất bại hoặc tình trạng quá thời gian chờ (timeout) liên tiếp:
  - **Trạng thái Open (Mở):** Khi mức độ lỗi chạm ngưỡng bất thường, cầu dao chuyển sang trạng thái **Open** để từ chối yêu cầu tức thì hoặc chuyển sang phương án dự phòng (fallback), không mở và giữ kết nối chờ đối tác nữa.
  - **Trạng thái Half-Open (Nửa mở):** Sau đó, cầu dao chuyển sang trạng thái **Half-Open** để cho một vài yêu cầu thăm dò đi qua, kiểm tra xem đối tác đã hồi phục hay chưa trước khi đưa hệ thống trở lại trạng thái bình thường.

### 2. So sánh bản chất hai cơ chế

| Tiêu chí | Rate Limiting | Circuit Breaker |
|---|---|---|
| **Mục tiêu chính** | Kiểm soát lưu lượng theo nhịp độ ổn định, tránh quá tải hạ tầng | Chặn hiệu ứng sập dây chuyền khi dịch vụ phụ thuộc bên ngoài gặp sự cố |
| **Tín hiệu giám sát** | Tổng số yêu cầu trong một đơn vị thời gian | Tỷ lệ thất bại hoặc tình trạng quá thời gian chờ liên tiếp ở chiều gọi ra |
| **Cách phản ứng khi vượt ngưỡng** | Chặn các yêu cầu vượt ngưỡng lưu lượng | Chuyển sang trạng thái **Open** để từ chối tức thì hoặc dùng phương án dự phòng; sau đó chuyển qua **Half-Open** để thăm dò hồi phục trước khi trở lại bình thường |

### 3. Cách phối hợp giữa Rate Limiting và Circuit Breaker

Hai cơ chế này bổ trợ chứ không thay thế cho nhau:
- **Rate Limiting** giữ cho lượng yêu cầu lưu thông ở mức ổn định, tránh tình trạng tăng đột biến làm quá tải hệ thống.
- **Circuit Breaker** bảo vệ chiều gọi ra khi đối tác suy giảm hiệu năng hoặc lỗi, chủ động ngắt mạch để chính những yêu cầu đã lọt qua ngưỡng của Rate Limiting không tiếp tục giữ kết nối chờ vô ích và làm cạn tài nguyên nội bộ.

---

### V5-04 — Mẫu 5

**Tóm tắt nhanh:** **Rate Limiting** giới hạn số lượng yêu cầu đi qua trong một đơn vị thời gian để ngăn quá tải do lưu lượng tăng đột biến, còn **Circuit Breaker** đóng vai trò cầu dao tự ngắt ở chiều gọi ra để chặn sập dây chuyền khi dịch vụ đối tác gặp sự cố. Hai cơ chế giải quyết hai bài toán khác nhau nên cần phối hợp cùng nhau thay vì dùng thay thế.

### 1. Chuyện gì xảy ra khi đối tác bỗng nhiên phản hồi chậm 15 giây?

Hãy hình dung dịch vụ đối tác bên ngoài bình thường phản hồi **dưới 1 giây**, nhưng bỗng nhiên chậm tới **15 giây** cho mỗi yêu cầu:

* **Nếu chỉ dùng Rate Limiting:** Cơ chế này khống chế tổng số lượng yêu cầu được phép đi qua trong một đơn vị thời gian nhất định để giữ nhịp độ lưu lượng ổn định. Tuy nhiên, Rate Limiting không nhận biết được đối tác đang gặp sự cố treo chậm kéo dài. Vì vậy, những yêu cầu lọt qua ngưỡng cho phép vẫn tiếp tục giữ kết nối chờ đủ **15 giây**, làm cạn kiệt dần hồ chứa kết nối (connection pool) của máy chủ nội bộ và có thể kéo sập lan sang các chức năng khác.
* **Khi có Circuit Breaker:** Hoạt động như một cầu dao tự ngắt ở chiều gọi ra, Circuit Breaker giám sát tỷ lệ thất bại hoặc tình trạng quá thời gian chờ liên tiếp. Khi mức độ lỗi chạm ngưỡng bất thường, cầu dao chuyển trạng thái để ngắt kết nối sớm:
  * **Mở (Open):** Từ chối yêu cầu tức thì hoặc chuyển sang phương án dự phòng, không giữ kết nối chờ đối tác nữa.
  * **Nửa mở (Half-Open):** Sau đó, cầu dao cho phép một vài yêu cầu thăm dò đi qua để kiểm tra khả năng hồi phục của đối tác trước khi khôi phục lại trạng thái bình thường.

### 2. Phân biệt bản chất hai cơ chế

| Tiêu chí | Rate Limiting | Circuit Breaker |
|---|---|---|
| **Mục tiêu bảo vệ** | Kiểm soát lưu lượng theo nhịp độ ổn định, chống quá tải hạ tầng khi lưu lượng tăng đột biến. | Ngắt ly hợp ở chiều gọi ra, chặn hiệu ứng sập dây chuyền khi phụ thuộc ngoài gặp sự cố. |
| **Tín hiệu giám sát** | Tổng số lượng yêu cầu đi qua trong một đơn vị thời gian. | Tỷ lệ thất bại hoặc quá thời gian chờ liên tiếp ở chiều gọi ra. |
| **Hành động khi chạm ngưỡng** | Giới hạn các yêu cầu vượt ngưỡng lưu lượng. | Chuyển sang **Open** để từ chối tức thì hoặc chạy phương án dự phòng; sau đó dùng **Half-Open** thăm dò hồi phục. |
| **Giới hạn nếu dùng riêng** | Không phát hiện được đối tác treo chậm kéo dài, dẫn tới nghẽn hồ chứa kết nối. | Không kiểm soát được lưu lượng tăng đột biến theo nhịp độ thời gian. |

### 3. Cách phối hợp giữa Rate Limiting và Circuit Breaker

Khi đặt cùng nhau, hai cơ chế bảo vệ hệ thống theo hai lớp bổ trợ:

1. **Rate Limiting giữ nhịp độ lưu lượng ổn định:** Hấp thụ và giới hạn các đợt tăng đột biến số lượng yêu cầu để hạ tầng nội bộ không bị quá tải vượt mức chịu đựng.
2. **Circuit Breaker ngắt mạch chiều gọi ra khi đối tác có sự cố:** Với những yêu cầu đã qua ngưỡng cho phép của Rate Limiting, nếu dịch vụ đối tác bên ngoài phản hồi chậm kéo dài hoặc lỗi liên tiếp, Circuit Breaker sẽ kích hoạt trạng thái **Open** để ngắt kết nối sớm. Nhờ đó, máy chủ nội bộ không bị giữ kết nối vô ích, bảo toàn được hồ chứa kết nối cho các chức năng khác và tự kiểm tra hồi phục qua trạng thái **Half-Open**.

Nói ngắn gọn cho cả PM và lập trình viên mới: **Rate Limiting** bảo vệ hệ thống khỏi *quá nhiều yêu cầu cùng lúc*, còn **Circuit Breaker** bảo vệ hệ thống khỏi *việc tiếp tục giữ kết nối chờ một đối tác đang lỗi hoặc treo chậm*.

---

### Phiếu chấm nhanh V5-04

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho V5-04:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca V5-05 — Business Rule phức tạp

- **Tiêu đề / Chủ đề:** Quy tắc chiết khấu bậc thang B2B kèm điều kiện khóa do công nợ quá hạn (thiếu chi tiết biên)
- **Đối tượng đọc:** BA, PO và Kỹ sư hệ thống B2B
- **Mục đích giao tiếp:** Chuẩn hóa thành đặc tả Business Rule đơn nghĩa cho 3 bậc chiết khấu và ngoại lệ công nợ quá hạn > 15 ngày, đồng thời chỉ rõ các điểm gốc bỏ ngỏ chưa đủ để code.

### Yêu cầu & Văn bản nguồn

```text
Chuẩn hóa quy định chiết khấu B2B dưới đây thành tài liệu Business Rule rõ ràng, đơn nghĩa cho BA và Kỹ sư triển khai; giữ chính xác toàn bộ ngưỡng `>=`, `>`, mức phần trăm, ngoại lệ khóa công nợ và nêu rõ những điểm bản gốc chưa quy định đủ để lập trình (tuyệt đối không tự bịa công thức VAT hay chu kỳ cộng dồn ngoài nguồn):

Chính sách áp dụng tỷ lệ chiết khấu thương mại theo giá trị dành cho nhóm khách hàng doanh nghiệp (B2B) có kèm điều kiện kiểm soát công nợ

Theo chính sách ưu đãi doanh số, các đơn hàng thuộc phân khúc khách hàng doanh nghiệp có giá trị đạt từ 100 triệu đồng trở lên sẽ được hưởng mức chiết khấu thương mại 3%, đạt từ 300 triệu đồng trở lên được hưởng mức chiết khấu 5%, và các đơn hàng đạt từ 500 triệu đồng trở lên sẽ được áp dụng mức chiết khấu cao nhất là 8%. Tuy nhiên, nhằm kiểm soát rủi ro dòng tiền, đối với các khách hàng doanh nghiệp hiện đang ghi nhận bất kỳ khoản công nợ nào bị quá hạn thanh toán trên 15 ngày, hệ thống phải tự động tạm dừng việc áp dụng toàn bộ các mức chiết khấu ưu đãi nêu trên đối với tất cả các đơn hàng mới phát sinh kể từ thời điểm vượt quá hạn cho tới khi khách hàng hoàn tất nghĩa vụ thanh toán đối với toàn bộ phần công nợ quá hạn đó.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Ba mức chiết khấu B2B (3% / 5% / 8%) kích hoạt theo ngưỡng giá trị nào, và điều kiện công nợ nào (> 15 ngày vs <= 15 ngày) sẽ khóa toàn bộ ưu đãi xuống 0%?
- 2. Tài liệu có giữ nguyên trạng thái chưa chốt cho các lỗ hổng lập trình (đơn lẻ vs cộng dồn tháng/quý, trước/sau VAT & phí ship, đơn đặt trước mốc khóa nhưng chưa xuất hóa đơn) không?

### V5-05 — Mẫu 1

# Đặc tả Quy tắc Nghiệp vụ (Business Rules): Chiết khấu Thương mại B2B & Kiểm soát Công nợ

**Tóm tắt mục tiêu:** Chuẩn hóa chính sách chiết khấu thương mại theo giá trị đơn hàng cho khách hàng doanh nghiệp (B2B) kèm cơ chế tự động tạm dừng chiết khấu khi phát sinh công nợ quá hạn thanh toán trên 15 ngày. Các phần thông số chưa có trong văn bản gốc được tách riêng tại Mục 4 để PO/Kinh doanh chốt trước khi lập trình.

---

## 1. Phạm vi Áp dụng (Scope)

- **Trong phạm vi (In-Scope):**
  - Nhóm khách hàng thuộc phân khúc khách hàng doanh nghiệp (**B2B**).
  - Chính sách chiết khấu thương mại theo ngưỡng giá trị (`100 triệu đồng`, `300 triệu đồng`, `500 triệu đồng`) và cơ chế kiểm soát công nợ quá hạn `> 15 ngày`.
- **Chưa xác định / Ngoài dữ kiện gốc:**
  - Khách hàng không thuộc phân khúc B2B (B2C/khách lẻ) không thuộc đối tượng điều chỉnh của quy định này.
  - Các chính sách khuyến mãi, voucher hoặc chiết khấu khác ngoài bảng tỷ lệ nêu tại `BR-01` (cần chốt quy tắc cộng dồn hoặc loại trừ tại Mục 4).

---

## 2. Quy tắc Nghiệp vụ (Business Rules)

### BR-01: Phân tầng tỷ lệ chiết khấu thương mại theo giá trị đơn hàng B2B
- **Chủ thể & Điều kiện kích hoạt:** Đơn hàng thuộc khách hàng phân khúc B2B **và** khách hàng không ở trạng thái bị tạm dừng chiết khấu theo `BR-02`.
- **Hành vi hệ thống:** Hệ thống **phải** tự động áp dụng đúng một mức tỷ lệ chiết khấu thương mại tương ứng với ngưỡng giá trị cao nhất mà đơn hàng đạt tới theo bảng sau *(lưu ý: định nghĩa "giá trị đơn hàng" dùng để so ngưỡng và nhân tỷ lệ đang chờ chốt tại Điểm #1, Mục 4)*:

| Mã bậc | Điều kiện giá trị đơn hàng (`V`) | Tỷ lệ chiết khấu áp dụng | Ghi chú biên |
|---|---|---|---|
| `Tier-0` | `V < 100.000.000 đồng` | `0%` | Dưới ngưỡng hưởng ưu đãi |
| `Tier-1` | `100.000.000 đồng <= V < 300.000.000 đồng` | `3%` | Đạt ngưỡng từ `>= 100 triệu đồng` |
| `Tier-2` | `300.000.000 đồng <= V < 500.000.000 đồng` | `5%` | Đạt ngưỡng từ `>= 300 triệu đồng` |
| `Tier-3` | `V >= 500.000.000 đồng` | `8%` | Mức cao nhất, đạt từ `>= 500 triệu đồng` |

*(Ghi chú ngữ nghĩa: Nguồn quy định mức `8%` là "mức chiết khấu cao nhất", do đó các bậc tỷ lệ là mức thay thế theo bậc đạt được, không cộng dồn `3% + 5% + 8%`.)*

---

### BR-02: Tạm dừng và khôi phục chiết khấu khi có công nợ quá hạn trên 15 ngày
- **Điều kiện kích hoạt tạm dừng:** Khách hàng B2B hiện đang ghi nhận **ít nhất 01 khoản công nợ** (`>= 1` khoản) có số ngày quá hạn thanh toán **lớn hơn 15 ngày** (`Số ngày quá hạn > 15`).
  - *Biên quy tắc:* Nếu khách hàng có công nợ quá hạn `<= 15 ngày` (bao gồm đúng `15 ngày`) và không có khoản nào `> 15 ngày`, hệ thống **không** kích hoạt tạm dừng theo quy tắc này.
- **Hành vi hệ thống khi kích hoạt:**
  - Hệ thống **phải** tự động tạm dừng áp dụng **toàn bộ** các mức chiết khấu ưu đãi tại `BR-01` (`3%`, `5%`, `8%` → tỷ lệ áp dụng = `0%`).
  - Phạm vi tác động là **tất cả các đơn hàng mới phát sinh** của khách hàng đó kể từ thời điểm khoản công nợ vượt quá hạn `15 ngày`.
- **Điều kiện khôi phục (mở lại chiết khấu):**
  - Trạng thái tạm dừng chỉ kết thúc khi khách hàng **hoàn tất nghĩa vụ thanh toán đối với toàn bộ phần công nợ quá hạn đó**.
  - Sau khi điều kiện hoàn tất thanh toán được ghi nhận, các đơn hàng mới phát sinh tiếp theo của khách hàng được xét hưởng lại chiết khấu theo `BR-01`.

---

### BR-03: Thứ tự ưu tiên kiểm tra quy tắc
- Khi tính chiết khấu cho đơn hàng B2B, hệ thống **phải** kiểm tra điều kiện công nợ (`BR-02`) trước khi xét ngưỡng giá trị đơn hàng (`BR-01`).
- Nếu điều kiện tạm dừng tại `BR-02` đang có hiệu lực, `BR-02` **bắt buộc ghi đè** `BR-01`: mọi đơn hàng mới phát sinh đều nhận mức chiết khấu `0%`, bất kể giá trị đơn hàng đạt `>= 100 triệu`, `>= 300 triệu` hay `>= 500 triệu đồng`.

---

## 3. Kịch bản Kiểm thử Tối thiểu (Acceptance Criteria)

*Lưu ý: Các giá trị đơn hàng `V` và trạng thái quá hạn trong bảng dưới đây giả định dựa trên định nghĩa cuối cùng sẽ được chốt tại Mục 4.*

| Mã AC | Nhóm ca | Điều kiện đầu vào (Given / When) | Kết quả hệ thống bắt buộc (Then) |
|---|---|---|---|
| `AC-01` | Hợp lệ / Biên dưới | Khách hàng B2B, không có công nợ quá hạn `> 15 ngày`; đơn hàng có `V = 99.999.999 đồng` | Chiết khấu = `0%` (`Tier-0`). |
| `AC-02` | Biên ngưỡng 1 | Khách hàng B2B, không có công nợ quá hạn `> 15 ngày`; đơn hàng có `V = 100.000.000 đồng` | Chiết khấu = `3%` (`Tier-1`). |
| `AC-03` | Biên cận / ngưỡng 2 | Khách hàng B2B, không có công nợ quá hạn `> 15 ngày`; đơn `V = 299.999.999 đồng` vs `V = 300.000.000 đồng` | Đơn `< 300 triệu` hưởng `3%`; đơn `= 300 triệu` hưởng `5%` (`Tier-2`). |
| `AC-04` | Biên cận / ngưỡng 3 | Khách hàng B2B, không có công nợ quá hạn `> 15 ngày`; đơn `V = 499.999.999 đồng` vs `V = 500.000.000 đồng` | Đơn `< 500 triệu` hưởng `5%`; đơn `= 500 triệu` hưởng `8%` (`Tier-3`). |
| `AC-05` | Biên công nợ (`<= 15`) | Khách hàng B2B có 01 khoản công nợ quá hạn đúng `15 ngày`; phát sinh đơn mới `V = 500.000.000 đồng` | Chưa kích hoạt `BR-02` (vì chưa `> 15 ngày`). Đơn mới vẫn hưởng `8%`. |
| `AC-06` | Ngoại lệ công nợ (`> 15`) | Khách hàng B2B có 01 khoản công nợ quá hạn `16 ngày` (hoặc vượt mốc 15 ngày); phát sinh đơn mới `V = 500.000.000 đồng` | Kích hoạt `BR-02`. Chiết khấu tự động tạm dừng, áp dụng `0%`. |
| `AC-07` | Thanh toán một phần | Khách hàng đang bị khóa chiết khấu theo `BR-02`, mới thanh toán một phần công nợ quá hạn (chưa hoàn tất toàn bộ phần quá hạn đó); phát sinh đơn mới `V = 300.000.000 đồng` | Tiếp tục giữ trạng thái tạm dừng chiết khấu. Đơn mới áp dụng `0%`. |
| `AC-08` | Khôi phục sau thanh toán | Khách hàng đang bị khóa chiết khấu theo `BR-02` đã hoàn tất thanh toán toàn bộ phần công nợ quá hạn đó; phát sinh đơn mới sau thời điểm ghi nhận hoàn tất với `V = 300.000.000 đồng` | Khôi phục `BR-01`. Đơn mới được áp dụng `5%`. |

---

## 4. Điểm Bản gốc Chưa Quy định Đủ để Lập trình (Cần PO / Kinh doanh Chốt trước khi Dev)

### A. Nhóm điểm bắt buộc chốt để lập trình công thức & logic chặn

1. **Cơ sở xác định "giá trị đơn hàng" (`V`) và công thức tính tiền chiết khấu:**
   - Văn bản gốc chưa quy định giá trị dùng để xét ngưỡng (`100M / 300M / 500M`) và giá trị dùng để nhân tỷ lệ chiết khấu (`3% / 5% / 8%`) là **giá trước VAT hay giá sau VAT**, có bao gồm phí vận chuyển/phụ phí khác hay chỉ tính trên tiền hàng hóa.
   - Chưa quy định cách tính chiết khấu là **toàn phần** (nhân `3% / 5% / 8%` trên toàn bộ giá trị đơn đạt ngưỡng) hay **lũy tiến từng phần**, cũng như quy tắc **làm tròn số tiền chiết khấu** (làm tròn đến đơn vị đồng, hàng nghìn, làm tròn lên/xuống/nửa lên).
2. **Đơn lẻ hay cộng dồn doanh số:**
   - Đoạn mở đầu gọi là *"chính sách ưu đãi doanh số"*, nhưng câu quy tắc lại viết *"các đơn hàng ... có giá trị đạt từ..."*. Cần xác nhận chắc chắn:
     - *Phương án 1:* Tính độc lập trên **từng đơn hàng riêng lẻ** (mỗi đơn tự đạt ngưỡng mới hưởng).
     - *Phương án 2:* Có **cộng dồn doanh số** theo một chu kỳ nhất định (chưa có thông tin chu kỳ trong bản gốc).
3. **Cách tính mốc "quá hạn thanh toán trên 15 ngày" (`> 15 ngày`):**
   - Đơn vị đếm là **ngày lịch** (calendar days) hay **ngày làm việc** (business days)?
   - Thời điểm chuyển sang trạng thái vượt quá hạn được xác định như thế nào: theo **mốc 00:00 của ngày quá hạn thứ 16** (theo múi giờ hệ thống), hay tính chính xác đến **giờ/phút (`> 15 × 24 giờ`)** kể từ thời điểm đến hạn thanh toán của khoản nợ?
   - Cơ chế cập nhật công nợ: dữ liệu quá hạn được đồng bộ **thời gian thực (real-time)** từ hệ thống Kế toán/ERP hay chạy **job định kỳ (batch)**? (Điều này quyết định hệ thống có chặn đúng *"kể từ thời điểm vượt quá hạn"* hay có độ trễ đồng bộ.)
4. **Phạm vi "toàn bộ phần công nợ quá hạn đó" khi mở khóa:**
   - Giả sử tại thời điểm khách hàng bị khóa, khách hàng có **Khoản A quá hạn 20 ngày** (`> 15 ngày`) và **Khoản B quá hạn 5 ngày** (`<= 15 ngày`):
     - *Phương án 1:* Chỉ cần thanh toán hết **tất cả các khoản quá hạn `> 15 ngày`** (tức hết Khoản A) thì được mở khóa.
     - *Phương án 2:* Phải thanh toán hết **toàn bộ các khoản công nợ đang quá hạn (`> 0 ngày`)** (cả Khoản A và Khoản B) tại thời điểm thanh toán.
   - Mốc thời điểm được xem là *"hoàn tất nghĩa vụ thanh toán"*: tính khi tiền về tài khoản và **kế toán/hệ thống gạch nợ thành công**, hay khi khách hàng tải lên chứng từ thanh toán?

### B. Nhóm điểm cần chốt cho vòng đời đơn hàng & vận hành

5. **Mốc xác định "đơn hàng mới phát sinh":**
   - Hệ thống đối chiếu thời điểm vượt quá hạn với mốc nào của đơn hàng: thời điểm **tạo đơn nháp (`Created`)**, thời điểm **gửi đặt hàng/xác nhận đơn (`Submitted / Confirmed`)**, hay thời điểm **xuất hóa đơn**?
6. **Xử lý đơn hàng đang dở dang (In-flight orders) & chỉnh sửa đơn:**
   - Đơn hàng đã tạo và được áp chiết khấu *trước* thời điểm vượt quá hạn nhưng chưa giao/chưa thanh toán khi khách bị khóa công nợ: giữ nguyên mức chiết khấu cũ hay tính lại về `0%`?
   - Ngược lại, đơn hàng được tạo *trong* thời gian bị khóa (`0%`) nhưng chưa hoàn tất tại thời điểm khách trả hết nợ quá hạn: giữ nguyên `0%` hay tự động tính lại chiết khấu theo `BR-01`?
   - Nếu đơn hàng sau khi đặt bị chỉnh sửa/hủy bớt sản phẩm làm giá trị tụt xuống dưới ngưỡng (ví dụ từ `310 triệu` xuống `280 triệu`), hệ thống có tính lại chiết khấu từ `5%` xuống `3%` không?
7. **Quy tắc ưu tiên / cộng dồn với khuyến mãi khác:**
   - Nếu đơn hàng B2B đồng thời đủ điều kiện hưởng chương trình khuyến mãi sản phẩm, mã giảm giá hoặc hợp đồng giá riêng khác, chiết khấu `BR-01` được áp dụng đồng thời (cộng dồn/tính nối tiếp), lấy mức cao nhất, hay loại trừ lẫn nhau?
8. **Thông báo & Hiển thị trên giao diện (UX/Audit):**
   - Khi `BR-02` tạm dừng chiết khấu, hệ thống có bắt buộc hiển thị lý do khóa công nợ cho nhân viên kinh doanh/khách hàng B2B không, và có cơ chế ngoại lệ phê duyệt tay (manual override) bởi cấp quản lý hay chặn cứng hoàn toàn?

---

### V5-05 — Mẫu 2

# Đặc tả Quy tắc Nghiệp vụ (Business Rules): Chiết khấu thương mại B2B và Kiểm soát công nợ

## 1. Phạm vi áp dụng (Scope)

### Trong phạm vi (In-Scope)
- **Đối tượng áp dụng:** Khách hàng thuộc phân khúc doanh nghiệp (B2B) *(quy tắc định danh tài khoản và gom nhóm theo pháp nhân: `[Chưa chốt]`)*.
- **Nghiệp vụ điều chỉnh:**
  - Tự động áp dụng mức chiết khấu thương mại theo bậc giá trị đơn hàng (`3%`, `5%`, `8%`).
  - Tự động tạm dừng toàn bộ chiết khấu ưu đãi đối với đơn hàng mới khi khách hàng có công nợ quá hạn trên 15 ngày, và tự động khôi phục khi khách hàng hoàn tất nghĩa vụ thanh toán phần công nợ quá hạn đó.

### Ngoài phạm vi hoặc chưa có quy định trong nguồn
- Công thức thuế (bao gồm hay chưa bao gồm VAT), phí vận chuyển/phụ phí và thứ tự áp dụng với các khuyến mãi khác: `[Chưa chốt]`.
- Cơ chế cộng dồn doanh số theo kỳ (nếu có): `[Chưa chốt]`.
- Kênh đặt hàng áp dụng hoặc danh mục sản phẩm/dịch vụ loại trừ: nguồn gốc chưa đề cập (`[Chưa chốt]` nếu hệ thống vận hành đa kênh hoặc có nhóm hàng không chiết khấu).

---

## 2. Định nghĩa & Ký hiệu dữ liệu

| Thuật ngữ / Biến | Định nghĩa nghiệp vụ | Trạng thái làm rõ |
|---|---|---|
| `Customer_B2B` | Khách hàng thuộc phân khúc doanh nghiệp trên hệ thống. | `[Chưa chốt]` tiêu chí phân nhóm và phạm vi theo tài khoản hay pháp nhân (MST). |
| `Order_Value` | Giá trị đơn hàng (đơn vị: VNĐ) dùng để xét ngưỡng và tính chiết khấu. | `[Chưa chốt]` cơ sở trước/sau VAT, trước/sau giảm giá khác, tính đơn lẻ hay cộng dồn. |
| `Overdue_Days` | Số ngày quá hạn thanh toán của một khoản công nợ của khách hàng. | `[Chưa chốt]` tính theo ngày lịch hay ngày làm việc và giờ cắt mốc trong ngày. |
| `DISCOUNT_SUSPENDED` | Trạng thái tạm dừng áp dụng toàn bộ mức chiết khấu thương mại ưu đãi đối với đơn hàng mới của `Customer_B2B`. | Đã xác định điều kiện kích hoạt (`Overdue_Days > 15`); `[Chưa chốt]` phạm vi đơn tạo dở dang và phạm vi khoản nợ khi mở khóa. |

---

## 3. Quy tắc Nghiệp vụ Chi tiết (Business Rules)

### BR-01: Phân tầng tỷ lệ chiết khấu thương mại theo giá trị
- **Chủ thể & Điều kiện kích hoạt:** `Customer_B2B` phát sinh đơn hàng khi **không** ở trạng thái `DISCOUNT_SUSPENDED` (tức không ghi nhận bất kỳ khoản công nợ nào có `Overdue_Days > 15`).
- **Hành vi hệ thống:** Hệ thống **phải** tự động áp dụng đúng một tỷ lệ chiết khấu thương mại tương ứng với bậc giá trị của đơn hàng theo bảng dưới đây *(cơ sở xác định `Order_Value`, cách tính toàn phần trên đơn hay lũy tiến từng phần, và quy tắc làm tròn: `[Chưa chốt]`)*:

| Bậc chiết khấu | Điều kiện giá trị đơn hàng (`Order_Value`, VNĐ) | Tỷ lệ chiết khấu áp dụng | Ý nghĩa biên |
|---|---|---|---|
| Dưới ngưỡng | `Order_Value < 100.000.000` | `0%` (Không áp dụng) | Dưới 100 triệu đồng |
| Bậc 1 | `100.000.000 <= Order_Value < 300.000.000` | `3%` | Từ 100 triệu đồng đến dưới 300 triệu đồng |
| Bậc 2 | `300.000.000 <= Order_Value < 500.000.000` | `5%` | Từ 300 triệu đồng đến dưới 500 triệu đồng |
| Bậc 3 | `Order_Value >= 500.000.000` | `8%` (Mức cao nhất) | Từ 500 triệu đồng trở lên |

### BR-02: Tạm dừng chiết khấu khi có công nợ quá hạn trên 15 ngày (Ngoại lệ khóa)
- **Chủ thể & Điều kiện kích hoạt:** `Customer_B2B` hiện đang ghi nhận **ít nhất 1 khoản công nợ** (bất kỳ khoản nào) bị quá hạn thanh toán **trên 15 ngày** (`Overdue_Days > 15`).
- **Điều kiện không kích hoạt:** Nếu tất cả các khoản công nợ của khách hàng có `Overdue_Days <= 15` (bao gồm trường hợp bằng đúng 15 ngày) hoặc không có công nợ quá hạn, hệ thống **không** kích hoạt trạng thái tạm dừng.
- **Hành vi hệ thống:**
  - Hệ thống **phải tự động** chuyển khách hàng sang trạng thái `DISCOUNT_SUSPENDED` kể từ thời điểm khoản công nợ vượt quá hạn `> 15 ngày`.
  - Trong trạng thái `DISCOUNT_SUSPENDED`, hệ thống **phải tạm dừng áp dụng toàn bộ** các mức chiết khấu ưu đãi (`3%`, `5%`, `8%`) — tỷ lệ chiết khấu áp dụng bắt buộc là `0%` — đối với **tất cả các đơn hàng mới phát sinh** kể từ thời điểm vượt quá hạn *(mốc thời gian xác định "đơn hàng mới phát sinh" và xử lý đơn đã tạo trước mốc khóa nhưng duyệt sau mốc khóa: `[Chưa chốt]`)*.
- **Thứ tự ưu tiên:** `BR-02` ghi đè `BR-01`. Khi `BR-02` có hiệu lực, mọi đơn hàng mới của khách hàng đều hưởng `0%` chiết khấu ưu đãi bất kể `Order_Value` đạt ngưỡng `>= 100.000.000`, `>= 300.000.000` hay `>= 500.000.000`.

### BR-03: Khôi phục quyền hưởng chiết khấu (Mở khóa)
- **Điều kiện kích hoạt:** `Customer_B2B` đang ở trạng thái `DISCOUNT_SUSPENDED` và đã **hoàn tất nghĩa vụ thanh toán đối với toàn bộ phần công nợ quá hạn đó** *(phạm vi chỉ tính các khoản `> 15 ngày` hay mọi khoản quá hạn `>= 1 ngày`, và mốc ghi nhận hoàn tất thanh toán theo giao dịch hay sau đối soát kế toán: `[Chưa chốt]`)*.
- **Hành vi hệ thống:** Hệ thống tự động chấm dứt trạng thái `DISCOUNT_SUSPENDED` và khôi phục việc xét hưởng chiết khấu theo `BR-01` cho các đơn hàng mới phát sinh sau thời điểm mở khóa *(việc có hoàn chiết khấu hồi tố cho các đơn hàng đã phát sinh trong thời gian bị tạm dừng hay không: `[Chưa chốt]`)*.

---

## 4. Vòng đời Trạng thái Kiểm soát Chiết khấu

| Trạng thái hiện tại | Điều kiện chuyển trạng thái | Trạng thái kế tiếp | Trạng thái làm rõ |
|---|---|---|---|
| `ELIGIBLE` (Được xét `BR-01`) | Hệ thống ghi nhận tồn tại ít nhất 1 khoản công nợ có `Overdue_Days > 15` | `DISCOUNT_SUSPENDED` | `[Chưa chốt]` cơ chế quét real-time hay batch định kỳ và mốc giờ cắt ngày. |
| `DISCOUNT_SUSPENDED` (Áp `0%` theo `BR-02`) | Khách hàng hoàn tất thanh toán toàn bộ phần công nợ quá hạn đó | `ELIGIBLE` | `[Chưa chốt]` phạm vi khoản nợ phải thanh toán hết (`> 15 ngày` hay toàn bộ `>= 1 ngày`) và mốc ghi nhận hoàn tất thanh toán. |

---

## 5. Kịch bản Kiểm thử Nghiệm thu (Acceptance Criteria)

*Lưu ý: Các giá trị `Order_Value`, mốc phát sinh đơn hàng và mốc hoàn tất thanh toán trong bảng dưới đây phụ thuộc các điểm `[Chưa chốt]` tại Mục 6; cần chốt dứt điểm trước khi viết test tự động.*

| Mã AC | Nhóm ca | Điều kiện đầu vào (`Customer_B2B`) | Giá trị đơn (`Order_Value`, VNĐ) | Trạng thái công nợ tại thời điểm xét | Kết quả hệ thống bắt buộc |
|---|---|---|---|---|---|
| `AC-01` | Hợp lệ / Biên | Khách hàng B2B | `99.999.999` | Không có khoản nào `Overdue_Days > 15` | Áp dụng `0%` chiết khấu |
| `AC-02` | Hợp lệ / Biên | Khách hàng B2B | `100.000.000` | Không có khoản nào `Overdue_Days > 15` | Áp dụng `3%` chiết khấu |
| `AC-03` | Hợp lệ / Biên | Khách hàng B2B | `299.999.999` | Không có khoản nào `Overdue_Days > 15` | Áp dụng `3%` chiết khấu |
| `AC-04` | Hợp lệ / Biên | Khách hàng B2B | `300.000.000` | Không có khoản nào `Overdue_Days > 15` | Áp dụng `5%` chiết khấu |
| `AC-05` | Hợp lệ / Biên | Khách hàng B2B | `499.999.999` | Không có khoản nào `Overdue_Days > 15` | Áp dụng `5%` chiết khấu |
| `AC-06` | Hợp lệ / Biên | Khách hàng B2B | `500.000.000` | Không có khoản nào `Overdue_Days > 15` | Áp dụng `8%` chiết khấu |
| `AC-07` | Biên công nợ | Khách hàng B2B | `500.000.000` | Có khoản công nợ `Overdue_Days = 15` (không có khoản nào `> 15`) | Không khóa (`ELIGIBLE`); vẫn áp dụng `8%` chiết khấu |
| `AC-08` | Ngoại lệ khóa | Khách hàng B2B | `500.000.000` | Có ít nhất 1 khoản công nợ `Overdue_Days = 16` (`> 15`) | Tự động khóa (`DISCOUNT_SUSPENDED`); đơn mới áp dụng `0%` |
| `AC-09` | Ngoại lệ khóa | Khách hàng B2B đang `DISCOUNT_SUSPENDED` (có >= 2 khoản nợ quá hạn) | `300.000.000` | Chỉ mới thanh toán 1 phần, vẫn còn khoản nợ quá hạn thuộc phạm vi khóa | Giữ nguyên `DISCOUNT_SUSPENDED`; đơn mới áp dụng `0%` |
| `AC-10` | Mở khóa | Khách hàng B2B đang `DISCOUNT_SUSPENDED` | `300.000.000` | Đã hoàn tất thanh toán toàn bộ phần công nợ quá hạn (theo phạm vi `[Chưa chốt]`) trước khi phát sinh đơn mới | Chuyển về `ELIGIBLE`; đơn mới phát sinh sau mở khóa áp dụng `5%` |
| `AC-11` | Ngoài phạm vi | Khách hàng không thuộc phân khúc B2B | `500.000.000` | Không xét theo quy tắc này | Không áp dụng `BR-01`, `BR-02`, `BR-03` |

---

## 6. Các điểm bản gốc chưa quy định đủ — Cần PO chốt trước khi lập trình (`[Chưa chốt]`)

1. **Cơ sở tính `Order_Value` (thuế, phí, giảm giá khác):**
   - Giá trị đơn hàng dùng để đối chiếu ngưỡng (`100M / 300M / 500M`) và dùng để nhân tỷ lệ `%` chiết khấu là giá **trước VAT hay sau VAT**?
   - Có tính trước hay sau các khoản giảm giá/khuyến mãi khác, và có bao gồm phí vận chuyển hoặc phụ phí khác không?
2. **Đơn vị xét ngưỡng (từng đơn hàng hay cộng dồn doanh số):**
   - Phần chi tiết ghi *"các đơn hàng ... có giá trị đạt từ..."* (hàm ý xét trên từng đơn hàng riêng lẻ), nhưng phần dẫn lại nêu *"chính sách ưu đãi doanh số"*. Cần chốt dứt điểm: ngưỡng áp dụng **độc lập cho từng đơn hàng** hay **cộng dồn doanh số** (và nếu có cộng dồn thì chu kỳ cộng dồn được tính như thế nào)?
3. **Cách tính theo bậc và cơ chế hạch toán/làm tròn:**
   - Tỷ lệ `3% / 5% / 8%` áp dụng cho **toàn bộ giá trị đơn hàng** đạt bậc tương ứng (flat tier) hay tính **lũy tiến từng phần** theo từng khoảng giá trị?
   - Quy tắc làm tròn số tiền chiết khấu (làm tròn đến hàng đơn vị/hàng trăm/nghìn VNĐ, làm tròn lên/xuống/gần nhất) và hình thức áp dụng (giảm trực tiếp trên đơn hàng, trừ trên hóa đơn hay cấn trừ công nợ)?
4. **Mốc thời gian xác định quá hạn (`> 15 ngày`) và "đơn hàng mới phát sinh":**
   - `Overdue_Days` tính theo **ngày lịch** hay **ngày làm việc**, tính từ ngày kế tiếp sau ngày đến hạn với giờ cắt mốc (`cut-off time`, múi giờ) nào? Hệ thống kiểm tra khóa theo **thời gian thực (real-time)** hay **tác vụ định kỳ (batch job)**?
   - Thời điểm "đơn hàng mới phát sinh" lấy theo mốc nào (`created_at` khi tạo đơn nháp, `submitted_at` khi khách đặt hàng, hay `confirmed_at` khi xác nhận đơn)?
   - Nếu một đơn hàng được tạo và áp chiết khấu *trước* thời điểm khách hàng vượt quá hạn 15 ngày, nhưng đến lúc thanh toán/duyệt đơn thì khách hàng đã chuyển sang `DISCOUNT_SUSPENDED`, đơn đó được giữ nguyên chiết khấu hay phải tính lại về `0%`?
5. **Điều kiện mở khóa ("hoàn tất nghĩa vụ thanh toán đối với toàn bộ phần công nợ quá hạn đó"):**
   - Tại thời điểm thanh toán để mở khóa, nếu khách hàng vừa có khoản quá hạn `> 15 ngày` vừa có khoản mới quá hạn `1–15 ngày`, khách hàng chỉ cần thanh toán hết các khoản **`> 15 ngày`** hay phải thanh toán hết **mọi khoản đang quá hạn** (kể cả `1–15 ngày`)?
   - Hệ thống ghi nhận "hoàn tất nghĩa vụ thanh toán" tại thời điểm giao dịch thanh toán thành công hay sau khi kế toán đối soát xong?
   - Các đơn hàng đã phát sinh và bị áp `0%` trong thời gian `DISCOUNT_SUSPENDED` có được hoàn chiết khấu hồi tố sau khi mở khóa không, hay chỉ áp dụng lại chiết khấu cho các đơn phát sinh **sau** thời điểm mở khóa?
6. **Phạm vi dữ liệu khách hàng B2B và công nợ:**
   - Điều kiện nhận diện `Customer_B2B` trên hệ thống là gì; trường hợp một doanh nghiệp có nhiều chi nhánh/tài khoản con thì công nợ quá hạn và trạng thái `DISCOUNT_SUSPENDED` tính riêng theo từng tài khoản hay gộp theo pháp nhân (Mã số thuế)?
   - Các khoản công nợ đang trong trạng thái tranh chấp/khiếu nại có được tính vào điều kiện kiểm tra `Overdue_Days > 15` hay loại trừ?

---

### V5-05 — Mẫu 3

Bản hiệu đính thống nhất số mục tham chiếu (thay thế bản gửi ngay trước đó):

# Tài liệu Quy tắc Nghiệp vụ (Business Rule): Chiết khấu Thương mại B2B và Kiểm soát Công nợ

## 1. Phạm vi và Đối tượng áp dụng
- **Đối tượng áp dụng (In-Scope):** Khách hàng thuộc phân khúc doanh nghiệp (`Khách hàng B2B`) phát sinh đơn hàng trên hệ thống.
- **Ngoài phạm vi (Out-of-Scope):** Các nhóm khách hàng không thuộc phân khúc doanh nghiệp.
- **Thuật ngữ quy ước trong tài liệu:**
  - **Giá trị đơn hàng ($V$):** Giá trị của từng đơn hàng dùng để xét ngưỡng hưởng chiết khấu *(cơ sở tính trước/sau thuế và các khoản phí chưa được nguồn quy định — xem Mục 4)*.
  - **Trạng thái Khóa chiết khấu:** Trạng thái hệ thống tự động tạm dừng toàn bộ mức chiết khấu ưu đãi theo chính sách này đối với các đơn hàng mới phát sinh của Khách hàng B2B.

---

## 2. Quy tắc Nghiệp vụ (Business Rules)

### BR-01: Phân tầng tỷ lệ chiết khấu thương mại theo giá trị đơn hàng
- **Điều kiện tiên quyết:** Khách hàng thuộc nhóm `Khách hàng B2B` **và** không đang ở **Trạng thái Khóa chiết khấu** theo `BR-02`.
- **Hành vi hệ thống:** Hệ thống xác định tỷ lệ chiết khấu thương mại áp dụng cho đơn hàng dựa trên Giá trị đơn hàng ($V$) theo bảng phân tầng sau:

| Bậc | Điều kiện Giá trị đơn hàng ($V$) | Tỷ lệ chiết khấu áp dụng | Ghi chú nghiệp vụ |
|---|---|---|---|
| Bậc 0 | $V < 100.000.000\text{ VNĐ}$ | **0%** | Không đạt ngưỡng tối thiểu để hưởng ưu đãi theo chính sách này. |
| Bậc 1 | $100.000.000\text{ VNĐ} \le V < 300.000.000\text{ VNĐ}$ | **3%** | Áp dụng khi đạt từ 100 triệu đồng trở lên và chưa đạt ngưỡng 300 triệu đồng. |
| Bậc 2 | $300.000.000\text{ VNĐ} \le V < 500.000.000\text{ VNĐ}$ | **5%** | Áp dụng khi đạt từ 300 triệu đồng trở lên và chưa đạt ngưỡng 500 triệu đồng. |
| Bậc 3 | $V \ge 500.000.000\text{ VNĐ}$ | **8%** | Mức chiết khấu cao nhất theo chính sách này. |

*(Lưu ý: Bản gốc quy định ngưỡng "đạt từ 100 triệu", "đạt từ 300 triệu", "đạt từ 500 triệu" với mức cao nhất 8%, chưa xác nhận tường minh cơ chế áp dụng một tỷ lệ duy nhất cho toàn đơn hay tính lũy tiến từng phần — xem Mục 4).*

---

### BR-02: Tự động tạm dừng chiết khấu khi có công nợ quá hạn trên 15 ngày
- **Điều kiện kích hoạt:** Hệ thống ghi nhận Khách hàng B2B hiện có **bất kỳ** khoản công nợ nào bị quá hạn thanh toán **trên 15 ngày** (`số ngày quá hạn > 15 ngày`).
- **Hành vi hệ thống:**
  1. Hệ thống **phải tự động** kích hoạt **Trạng thái Khóa chiết khấu** cho Khách hàng B2B đó.
  2. Tạm dừng áp dụng toàn bộ các mức chiết khấu ưu đãi tại `BR-01` (tỷ lệ chiết khấu áp dụng theo chính sách này = **0%**).
- **Phạm vi đơn hàng bị tác động:** Áp dụng đối với **tất cả các đơn hàng mới phát sinh** kể từ thời điểm khoản công nợ vượt quá hạn (`> 15 ngày`) cho tới khi thỏa mãn điều kiện khôi phục tại `BR-03`.
- **Ngoại lệ biên:** Nếu Khách hàng B2B chỉ có các khoản công nợ quá hạn `<= 15 ngày` (không có bất kỳ khoản nào `> 15 ngày`), hệ thống **không** kích hoạt khóa chiết khấu theo quy tắc này.

---

### BR-03: Khôi phục quyền hưởng chiết khấu khi hoàn tất thanh toán công nợ quá hạn
- **Điều kiện kích hoạt:** Khách hàng B2B đang ở **Trạng thái Khóa chiết khấu** hoàn tất nghĩa vụ thanh toán đối với **toàn bộ phần công nợ quá hạn đó**.
- **Hành vi hệ thống:**
  1. Hệ thống tự động gỡ **Trạng thái Khóa chiết khấu**.
  2. Các đơn hàng mới phát sinh kể từ thời điểm hoàn tất nghĩa vụ thanh toán được xét hưởng tỷ lệ chiết khấu trở lại theo `BR-01`.

---

## 3. Bảng Tra cứu Kịch bản Biên (Decision Table cho BA / QA)

| Ca kiểm thử | Khoản công nợ quá hạn lớn nhất của Khách hàng B2B | Giá trị đơn hàng mới phát sinh ($V$) | Trạng thái chính sách | Tỷ lệ chiết khấu áp dụng |
|---|---|---|---|---|
| TC-01 | Không có hoặc $\le 15$ ngày | $99.999.999\text{ VNĐ}$ | Bình thường | **0%** |
| TC-02 | Không có hoặc $\le 15$ ngày | $100.000.000\text{ VNĐ}$ | Bình thường | **3%** |
| TC-03 | Không có hoặc $\le 15$ ngày | $299.999.999\text{ VNĐ}$ | Bình thường | **3%** |
| TC-04 | Không có hoặc $\le 15$ ngày | $300.000.000\text{ VNĐ}$ | Bình thường | **5%** |
| TC-05 | Không có hoặc $\le 15$ ngày | $499.999.999\text{ VNĐ}$ | Bình thường | **5%** |
| TC-06 | Không có hoặc $\le 15$ ngày | $500.000.000\text{ VNĐ}$ | Bình thường | **8%** |
| TC-07 | Có ít nhất 1 khoản $> 15$ ngày (ví dụ: ngày thứ 16) | Bất kỳ ($< 100\text{tr}$ hay $\ge 500\text{tr}$) | Tạm dừng (Khóa) | **0%** |
| TC-08 | Đã hoàn tất thanh toán toàn bộ phần công nợ quá hạn | $300.000.000\text{ VNĐ}$ (đơn mới sau khi hoàn tất) | Khôi phục | **5%** |

---

## 4. Điểm Bản gốc Chưa Quy định Đủ để Lập trình (Cần PO / Kinh doanh chốt trước khi Dev)

Các nội dung dưới đây hiện **chưa có trong quy định gốc** và không được tự suy diễn khi thiết kế dữ liệu hoặc viết mã; BA cần làm rõ với PO/Kinh doanh trước khi triển khai:

1. **Cơ sở xác định Giá trị đơn hàng ($V$) và công thức tính tiền chiết khấu:**
   - $V$ được tính theo giá **trước thuế hay sau thuế**; có bao gồm phí vận chuyển, phụ phí khác hoặc tính trước/sau các khoản giảm giá khác hay không?
   - Số tiền chiết khấu (3%, 5%, 8%) được nhân trên **giá gốc nào** (trước hay sau thuế/phí) và quy tắc làm tròn tiền là gì (làm tròn đến đồng, làm tròn lên/xuống/thông thường)?
   - Khi đạt bậc cao hơn (ví dụ $V = 500\text{ triệu}$), áp dụng **một tỷ lệ duy nhất** (8% cho toàn bộ 500 triệu) hay tính **lũy tiến từng phần** theo từng khoảng giá trị?
   - Chiết khấu thương mại theo chính sách này có được **cộng dồn** với các chương trình khuyến mãi, mã giảm giá hoặc bảng giá hợp đồng riêng khác hay loại trừ lẫn nhau?

2. **Định nghĩa kỹ thuật cho "khoản công nợ" và mốc "quá hạn > 15 ngày":**
   - Đơn vị "khoản công nợ" được theo dõi ở cấp độ nào: từng hóa đơn/chứng từ nợ riêng lẻ hay tổng hợp theo đơn hàng/hợp đồng? Có ngưỡng dư nợ tối thiểu để bỏ qua sai số làm tròn vài đồng không?
   - Số ngày quá hạn được tính từ mốc nào (ngày đến hạn thanh toán trên hóa đơn hay ngày giao hàng), tính theo **ngày lịch** hay **ngày làm việc**, và mốc chuyển ngày tính theo giờ/múi giờ nào (ví dụ: vừa qua `00:00` sang ngày thứ 16 theo múi giờ chuẩn của hệ thống hay đủ `15 × 24 giờ` tính từ thời điểm đến hạn)?
   - Hệ thống kiểm tra điều kiện quá hạn theo cơ chế **thời gian thực (real-time)** tại lúc phát sinh đơn hay theo tác vụ quét định kỳ (batch job)?

3. **Ranh giới "đơn hàng mới phát sinh" và xử lý vòng đời đơn hàng:**
   - Thời điểm "đơn hàng mới phát sinh" được gắn với sự kiện nào: lúc tạo đơn nháp (`Draft`), lúc người dùng gửi/đặt đơn (`Submit/Create`), lúc duyệt đơn (`Approve/Confirm`), hay lúc xuất hóa đơn?
   - Các đơn hàng đã tạo **trước** thời điểm bị khóa công nợ nhưng đang ở trạng thái chờ duyệt/chờ thanh toán/chưa xuất hóa đơn có giữ nguyên chiết khấu cũ hay bị tính lại về 0%?
   - Trong thời gian bị khóa, hệ thống vẫn cho phép tạo đơn hàng bình thường với mức chiết khấu 0% (kèm thông báo lý do), hay chặn không cho tạo đơn?
   - Nếu đơn hàng được phép chỉnh sửa số lượng/giá trị hoặc hủy một phần sau khi tạo, hệ thống có tính lại bậc chiết khấu theo giá trị mới không?

4. **Phạm vi nghĩa vụ thanh toán để mở khóa và quy tắc không hồi tố:**
   - Cụm từ *"hoàn tất nghĩa vụ thanh toán đối với toàn bộ phần công nợ quá hạn đó"* được hiểu theo phương án nào:
     - *Phương án A:* Chỉ cần thanh toán hết toàn bộ các khoản công nợ đang quá hạn **$> 15$ ngày**.
     - *Phương án B:* Phải thanh toán hết **toàn bộ các khoản công nợ quá hạn** tại thời điểm đó (bao gồm cả các khoản quá hạn từ 1 đến 15 ngày).
   - Mốc xác nhận "hoàn tất nghĩa vụ thanh toán" là lúc khách hàng gửi chứng từ/lệnh chuyển tiền hay khi hệ thống/kế toán xác nhận đã nhận đủ tiền và gạch nợ thành công?
   - Xác nhận quy tắc: Các đơn hàng đã phát sinh trong thời gian bị khóa (áp dụng 0%) có giữ nguyên 0% (không hồi tố) sau khi khách hàng thanh toán xong công nợ quá hạn hay không?

---

### V5-05 — Mẫu 4

# Đặc tả Quy tắc Nghiệp vụ (Business Rules): Chiết khấu Thương mại B2B và Kiểm soát Công nợ

**Tài liệu dành cho:** Business Analyst (BA), Kỹ sư triển khai (Dev), Kiểm thử (QA)  
**Trạng thái nguồn:** Đã chuẩn hóa logic từ chính sách gốc; **còn các thông số kỹ thuật chưa được quy định** (xem Mục 4) cần PO/Kinh doanh chốt trước khi lập trình.

---

## 1. Phạm vi & Đối tượng áp dụng

- **Đối tượng áp dụng (In-Scope):** Đơn hàng của khách hàng thuộc phân khúc **Khách hàng doanh nghiệp (B2B)**.
- **Đối tượng không thuộc phạm vi quy định này:** Các phân khúc khách hàng ngoài B2B (không được đề cập trong nguồn).
- **Nguyên tắc chung:** Một đơn hàng B2B hợp lệ được xét chiết khấu thương mại dựa trên giá trị đơn hàng và trạng thái công nợ quá hạn của khách hàng tại thời điểm xét.

---

## 2. Quy tắc Nghiệp vụ Chuẩn hóa

### BR-01: Phân tầng tỷ lệ chiết khấu thương mại theo giá trị đơn hàng

Khi khách hàng B2B **không** thuộc diện bị tạm dừng chiết khấu theo `BR-02`, hệ thống **phải** áp dụng đúng một mức chiết khấu tương ứng với bậc cao nhất mà giá trị đơn hàng đạt được theo bảng sau:

| Mã bậc | Điều kiện giá trị đơn hàng (`V`, đơn vị: VNĐ) | Tỷ lệ chiết khấu thương mại | Ghi chú |
|---|---|---|---|
| **Tier 0** | `V < 100.000.000` | Không hưởng chiết khấu theo chính sách này | Không đạt ngưỡng tối thiểu |
| **Tier 1** | `100.000.000 <= V < 300.000.000` | **3%** | Áp dụng từ mốc 100 triệu đồng trở lên |
| **Tier 2** | `300.000.000 <= V < 500.000.000` | **5%** | Áp dụng từ mốc 300 triệu đồng trở lên |
| **Tier 3** | `V >= 500.000.000` | **8%** (mức tối đa) | Áp dụng từ mốc 500 triệu đồng trở lên |

> **Lưu ý về biến `V` (Giá trị đơn hàng):** Bản gốc chưa xác định `V` là giá trị trước thuế hay sau thuế, trước hay sau giảm giá khác, và có tính phí phát sinh hay không (xem `OQ-01` tại Mục 4). Hệ thống chỉ sử dụng được một định nghĩa thống nhất sau khi PO chốt.

---

### BR-02: Tạm dừng chiết khấu khi có công nợ quá hạn trên 15 ngày

- **Điều kiện kích hoạt:** Tại thời điểm xét đơn hàng, khách hàng B2B đang có **ít nhất một** khoản công nợ có số ngày quá hạn thanh toán `> 15 ngày` *(tức từ ngày thứ 16 quá hạn trở đi; mức `<= 15 ngày` chưa kích hoạt quy tắc tạm dừng này)*.
- **Hành vi bắt buộc của hệ thống:** Hệ thống **phải tự động tạm dừng** việc áp dụng **toàn bộ** các mức chiết khấu ưu đãi tại `BR-01` (3%, 5%, 8%) — tức mức chiết khấu áp dụng theo chính sách này bằng **0%** — đối với **tất cả các đơn hàng mới phát sinh** kể từ thời điểm khoản công nợ vượt ngưỡng `> 15 ngày`.
- **Thứ tự ưu tiên:** Điều kiện chặn tại `BR-02` có độ ưu tiên cao hơn `BR-01`. Dù giá trị đơn hàng đạt `>= 500.000.000 VNĐ`, đơn hàng vẫn **không** được hưởng chiết khấu nếu khách hàng đang bị tạm dừng theo `BR-02`.

---

### BR-03: Khôi phục quyền hưởng chiết khấu

- **Điều kiện mở khóa:** Khách hàng hoàn tất nghĩa vụ thanh toán đối với **toàn bộ phần công nợ quá hạn đó**.
- **Hành vi hệ thống:** Sau khi điều kiện mở khóa được đáp ứng và ghi nhận trên hệ thống, các đơn hàng mới phát sinh sau thời điểm mở khóa được phép áp dụng lại bảng chiết khấu tại `BR-01` (nếu không còn khoản công nợ nào khác thỏa điều kiện `> 15 ngày`).

> **Lưu ý:** Mốc ghi nhận hoàn tất thanh toán và phạm vi các khoản nợ phải tất toán để mở khóa hiện chưa đủ chi tiết để lập trình (xem `OQ-05`, `OQ-06` tại Mục 4).

---

## 3. Bảng Giá trị Biên (Boundary Matrix) cho Kiểm thử Logic

| Ca kiểm thử | Phân khúc | Trạng thái công nợ quá hạn | Giá trị đơn hàng (`V`) | Kết quả mong đợi |
|---|---|---|---|---|
| **TC-01** | B2B | Không có nợ quá hạn `> 15 ngày` | `99.999.999` (hoặc `< 100.000.000`) | Không áp dụng chiết khấu (0% theo chính sách này) |
| **TC-02** | B2B | Không có nợ quá hạn `> 15 ngày` | `100.000.000` | Áp dụng **3%** |
| **TC-03** | B2B | Không có nợ quá hạn `> 15 ngày` | `299.999.999` | Áp dụng **3%** |
| **TC-04** | B2B | Không có nợ quá hạn `> 15 ngày` | `300.000.000` | Áp dụng **5%** |
| **TC-05** | B2B | Không có nợ quá hạn `> 15 ngày` | `499.999.999` | Áp dụng **5%** |
| **TC-06** | B2B | Không có nợ quá hạn `> 15 ngày` | `500.000.000` | Áp dụng **8%** |
| **TC-07** | B2B | Có khoản nợ quá hạn đúng `= 15 ngày` | `500.000.000` | Vẫn áp dụng **8%** (chưa vượt ngưỡng `> 15 ngày`) |
| **TC-08** | B2B | Có ít nhất 1 khoản nợ quá hạn `> 15 ngày` (ví dụ `16 ngày`) | `500.000.000` | **Tạm dừng** toàn bộ chiết khấu (0%) |
| **TC-09** | B2B | Vừa hoàn tất thanh toán toàn bộ phần công nợ quá hạn đó | `300.000.000` (đơn mới sau mở khóa) | Khôi phục áp dụng **5%** |

---

## 4. Các điểm bản gốc chưa quy định đủ — Cần PO/Kinh doanh chốt trước khi lập trình

Tài liệu gốc mới dừng ở mức chính sách tổng quan, **chưa đủ thông số** để Kỹ sư triển khai viết logic tính toán và xử lý trạng thái. Các điểm dưới đây cần được chốt dứt điểm và cập nhật lại vào `BR-01` – `BR-03`:

### A. Định nghĩa giá trị tính toán & Phạm vi cộng gộp
1. **`OQ-01` — Cơ sở xác định `V` (giá trị đơn hàng) và nền tính tiền chiết khấu:**
   - Giá trị xét ngưỡng (`100`, `300`, `500` triệu VNĐ) và giá trị làm nền nhân phần trăm chiết khấu (`3%`, `5%`, `8%`) là **giá trị nào**: trước thuế hay sau thuế (VAT), trước hay sau các loại giảm giá/khuyến mãi khác, có bao gồm phí vận chuyển/phụ phí hay chỉ tính tiền hàng?
   - Số tiền chiết khấu tính ra được làm tròn đến đơn vị nào (hàng đồng, hàng trăm, hàng nghìn) và theo quy tắc làm tròn nào (làm tròn nửa lên, cắt phần thập phân, làm tròn lên)?
2. **`OQ-02` — Xác nhận cơ chế xét từng đơn hay cộng dồn:**
   - Văn bản gốc chỉ đề cập giá trị từng đơn hàng; cần xác nhận chính sách này **chỉ tính độc lập trên từng đơn hàng** hay có liên kết với cơ chế cộng dồn/hạn mức khác ngoài văn bản gốc.
3. **`OQ-03` — Tương tác với các ưu đãi khác và xử lý sửa/hủy đơn:**
   - Chiết khấu 3% / 5% / 8% có được áp dụng đồng thời với các chương trình khuyến mãi, mã giảm giá hoặc bảng giá hợp đồng riêng của khách B2B không, hay loại trừ lẫn nhau?
   - Nếu đơn hàng sau khi tạo bị chỉnh sửa hoặc hủy một phần làm giá trị rơi xuống ngưỡng thấp hơn (ví dụ từ `310 triệu` xuống `280 triệu`), hệ thống có tính lại tỷ lệ chiết khấu tương ứng (từ 5% xuống 3%) không?

### B. Quy tắc đếm ngày quá hạn & Thời điểm khóa/mở
4. **`OQ-04` — Cách tính số ngày quá hạn (`> 15 ngày`):**
   - Số ngày quá hạn tính theo **ngày lịch** hay **ngày làm việc**?
   - Mốc bắt đầu tính quá hạn từ thời điểm nào (ngày đến hạn trên hóa đơn, ngày giao hàng + hạn nợ...), xét theo múi giờ nào (ví dụ UTC+7), và hệ thống cập nhật trạng thái vượt hạn theo **thời gian thực (real-time)** hay chạy tác vụ định kỳ cuối ngày (batch)?
   - Có ngưỡng số tiền nợ tối thiểu để kích hoạt khóa hay không (ví dụ: bỏ qua sai số làm tròn vài đồng hay mọi khoản nợ quá hạn `> 0 VNĐ` đều kích hoạt)?
5. **`OQ-05` — Thời điểm chốt điều kiện trên vòng đời đơn hàng ("đơn hàng mới phát sinh"):**
   - Hệ thống kiểm tra trạng thái nợ quá hạn và khóa mức chiết khấu tại bước nào: **tạo đơn nháp**, **gửi/xác nhận đặt hàng**, **phê duyệt đơn**, hay **xuất hóa đơn**?
   - Với đơn hàng đã tạo và áp chiết khấu **trước** thời điểm khách hàng vượt quá hạn 15 ngày nhưng chưa hoàn tất xử lý/chưa xuất hóa đơn đến khi khách hàng bị khóa: hệ thống giữ nguyên mức chiết khấu cũ hay tính lại thành 0%?
   - Ngược lại, các đơn hàng tạo trong lúc đang bị tạm dừng (đang chờ duyệt/chờ thanh toán) có được tự động tính lại chiết khấu khi khách hàng mở khóa không, hay chỉ áp dụng cho đơn tạo mới hoàn toàn sau thời điểm mở khóa?
6. **`OQ-06` — Phạm vi "toàn bộ phần công nợ quá hạn đó" & Mốc xác nhận thanh toán:**
   - Để mở khóa, khách hàng chỉ cần thanh toán hết các khoản đang quá hạn `> 15 ngày`, hay phải thanh toán hết **tất cả** khoản công nợ đã quá hạn tại thời điểm trả (bao gồm cả các khoản mới quá hạn `1 – 15 ngày`)?
   - Với các hình thức thanh toán không tức thời (như chuyển khoản, ủy nhiệm chi), hệ thống mở khóa ngay khi tạo phiếu thu/chờ đối soát hay chỉ mở khóa sau khi kế toán/ngân hàng xác nhận đã nhận đủ tiền thành công?

---

### V5-05 — Mẫu 5

# Đặc tả Business Rule: Chính sách chiết khấu thương mại B2B kèm kiểm soát công nợ

## 1. Phạm vi & Đối tượng áp dụng

- **Trong phạm vi (In-Scope):**
  - Nhóm khách hàng doanh nghiệp (B2B) *(tiêu chí phân loại B2B trên hệ thống: `[Chưa chốt]`)*.
  - Các đơn hàng phát sinh mới thuộc nhóm khách hàng B2B đáp ứng ngưỡng giá trị và không vi phạm điều kiện công nợ quá hạn.
- **Ngoài phạm vi / Chưa có quy định trong tài liệu gốc:**
  - Khách hàng cá nhân (B2C).
  - Công thức thuế (VAT), chu kỳ cộng dồn doanh số (nếu có), quy tắc làm tròn và thứ tự ưu tiên với các chương trình khuyến mãi khác *(tất cả đánh dấu `[Chưa chốt]` tại Mục 4)*.

---

## 2. Quy tắc nghiệp vụ (Business Rules)

### BR-01: Tỷ lệ chiết khấu thương mại theo giá trị đơn hàng

Khi khách hàng B2B **không** thuộc diện bị tạm dừng chiết khấu theo `BR-02`, hệ thống áp dụng tỷ lệ chiết khấu thương mại tương ứng với bậc cao nhất mà giá trị đơn hàng (`V`) đạt được *(định nghĩa `V` theo trước/sau thuế và đơn vị xét theo từng đơn hay cộng dồn: `[Chưa chốt]`)*:

| Bậc | Điều kiện giá trị đơn hàng (`V`) `[Chưa chốt]` | Tỷ lệ chiết khấu thương mại | Ghi chú |
| :---: | :--- | :---: | :--- |
| 0 | `V < 100.000.000 VNĐ` | `0%` | Không đạt ngưỡng tối thiểu của chính sách ưu đãi này |
| 1 | `100.000.000 VNĐ <= V < 300.000.000 VNĐ` | `3%` | Áp dụng toàn phần theo mức bậc 1 |
| 2 | `300.000.000 VNĐ <= V < 500.000.000 VNĐ` | `5%` | Áp dụng toàn phần theo mức bậc 2 |
| 3 | `V >= 500.000.000 VNĐ` | `8%` | Mức chiết khấu cao nhất |

---

### BR-02: Tạm dừng chiết khấu khi có công nợ quá hạn trên 15 ngày

- **Điều kiện kích hoạt:** Khách hàng B2B hiện đang ghi nhận **ít nhất 1** khoản công nợ có thời gian quá hạn thanh toán **`> 15 ngày`** *(cách tính mốc ngày lịch/ngày làm việc/giờ: `[Chưa chốt]`)*.
  - Lưu ý biên: Khoản công nợ quá hạn `<= 15 ngày` (bao gồm đúng ngày thứ 15) **chưa** kích hoạt quy tắc tạm dừng này.
- **Hành vi bắt buộc của hệ thống:**
  - Hệ thống **phải tự động** tạm dừng áp dụng toàn bộ các mức chiết khấu ưu đãi tại `BR-01` (`3%`, `5%`, `8%` đều chuyển về **`0%`**).
  - Phạm vi chặn áp dụng cho **tất cả các đơn hàng mới phát sinh** kể từ thời điểm khoản công nợ vượt ngưỡng `> 15 ngày` *(mốc sự kiện xác định "đơn hàng mới phát sinh": `[Chưa chốt]`)*.

---

### BR-03: Điều kiện khôi phục quyền hưởng chiết khấu

- **Điều kiện mở khóa:** Khách hàng hoàn tất nghĩa vụ thanh toán đối với **toàn bộ phần công nợ quá hạn đó** *(phạm vi khoản nợ phải trả hết và thời điểm hệ thống ghi nhận hoàn tất thanh toán: `[Chưa chốt]`)*.
- **Hành vi hệ thống:**
  - Kể từ thời điểm điều kiện mở khóa được đáp ứng, hệ thống tự động gỡ trạng thái tạm dừng và xét áp dụng lại các mức chiết khấu tại `BR-01` cho các đơn hàng mới phát sinh tiếp theo.
  - Các đơn hàng đã phát sinh trong thời gian bị tạm dừng *(việc giữ nguyên `0%` hay cho phép tính lại sau khi trả nợ: `[Chưa chốt]`)*.

---

## 3. Chuyển đổi trạng thái hưởng chiết khấu của Khách hàng B2B

| Trạng thái hiện tại | Sự kiện / Điều kiện chuyển | Trạng thái mới | Tác động lên đơn hàng mới phát sinh `[Chưa chốt]` |
| :--- | :--- | :--- | :--- |
| `ELIGIBLE` (Đủ điều kiện xét chiết khấu) | Có bất kỳ khoản công nợ nào quá hạn `> 15 ngày` `[Chưa chốt]` | `SUSPENDED_OVERDUE` (Tạm dừng chiết khấu) | Áp dụng `0%` chiết khấu cho tất cả đơn hàng mới phát sinh từ thời điểm vượt quá hạn |
| `SUSPENDED_OVERDUE` (Tạm dừng chiết khấu) | Hoàn tất thanh toán toàn bộ phần công nợ quá hạn đó `[Chưa chốt]` | `ELIGIBLE` (Đủ điều kiện xét chiết khấu) | Xét áp dụng lại biểu chiết khấu `3% / 5% / 8%` theo `BR-01` cho đơn hàng mới phát sinh |

---

## 4. Các điểm bản gốc chưa quy định đủ để lập trình (`[Chưa chốt]`)

BA và Kỹ sư cần làm rõ với PO / Kinh doanh / Kế toán toàn bộ các điểm dưới đây trước khi thiết kế CSDL, viết logic tính giá và kiểm thử:

1. **Cơ sở tính giá trị đơn hàng (`V`) ở `BR-01` (`[Chưa chốt]`):**
   - `V` là giá trị **chưa gồm VAT** hay **đã gồm VAT**?
   - `V` tính trước hay sau khi trừ các khoản giảm giá/khuyến mãi khác, phí vận chuyển và phụ phí?
   - Cơ sở giá trị dùng để **xác định bậc chiết khấu** (`100 / 300 / 500 triệu`) và giá trị dùng để **nhân tỷ lệ `%` tính tiền chiết khấu** có giống nhau không?
   - Chính sách tính độc lập trên **từng đơn hàng** hay có **cộng dồn** nhiều đơn hàng? *(Bản gốc ghi "các đơn hàng ... có giá trị đạt từ..." nhưng mở đầu lại nêu "ưu đãi doanh số" và không quy định bất kỳ chu kỳ cộng dồn nào).*
   - Quy tắc làm tròn số tiền chiết khấu (làm tròn đến hàng đồng, làm tròn lên/xuống hay theo chuẩn hóa đơn) và cách phân bổ tiền chiết khấu về từng dòng sản phẩm (nếu cần xuất hóa đơn chi tiết).

2. **Định nghĩa mốc thời gian "đơn hàng mới phát sinh" và xử lý đơn chuyển tiếp (`[Chưa chốt]`):**
   - Thời điểm "phát sinh đơn hàng" được chốt theo sự kiện nào: lúc tạo đơn nháp (`Draft`), lúc gửi/đặt đơn (`Submitted/Created`), lúc duyệt đơn (`Approved`), hay lúc xuất hóa đơn?
   - Với đơn hàng **tạo trước** thời điểm công nợ vượt `> 15 ngày` (đã được gắn chiết khấu `3%/5%/8%`) nhưng đến lúc duyệt/xuất hóa đơn thì khách hàng đã rơi vào trạng thái `SUSPENDED_OVERDUE`: hệ thống giữ nguyên chiết khấu cũ hay tự động gỡ bỏ về `0%`?
   - Với đơn hàng **tạo trong giai đoạn `SUSPENDED_OVERDUE`** (đang hưởng `0%`), nếu sau đó khách hàng thanh toán xong nợ quá hạn trước khi đơn được duyệt/giao, đơn này giữ `0%` hay được tính lại chiết khấu?

3. **Logic đo lường công nợ quá hạn `> 15 ngày` và xác nhận hoàn tất thanh toán (`[Chưa chốt]`):**
   - Số ngày quá hạn `> 15 ngày` tính theo **ngày lịch (calendar days)** hay **ngày làm việc**; so sánh theo **phần ngày nguyên** (từ 00:00 ngày thứ 16 sau hạn thanh toán) hay theo **dấu thời gian chính xác** (`> 15 x 24 giờ`)?
   - Cụm từ *"hoàn tất nghĩa vụ thanh toán đối với toàn bộ phần công nợ quá hạn đó"* có nghĩa là:
     - **Phương án A:** Chỉ cần thanh toán hết các khoản công nợ đang quá hạn **`> 15 ngày`** (các khoản mới quá hạn `1–15 ngày` không chặn mở khóa).
     - **Phương án B:** Phải thanh toán hết **tất cả** các khoản công nợ đang quá hạn (`> 0 ngày`) tại thời điểm thanh toán.
   - Mốc ghi nhận "hoàn tất nghĩa vụ thanh toán": Tính ngay khi phát sinh giao dịch thanh toán, hay phải chờ kế toán đối soát / ngân hàng báo có thành công? Nếu thanh toán thiếu phần lẻ rất nhỏ (ví dụ sai số chuyển khoản), hệ thống có dung sai hay bắt buộc dư nợ quá hạn `= 0`?
   - Tần suất cập nhật trạng thái `SUSPENDED_OVERDUE`: kiểm tra theo thời gian thực khi đặt đơn (`real-time check`) hay chạy job đối soát định kỳ hàng ngày?

4. **Phạm vi định danh B2B, loại trừ sản phẩm và cộng dồn ưu đãi (`[Chưa chốt]`):**
   - Trường dữ liệu / nhóm khách hàng nào trên hệ thống xác định một khách hàng thuộc phân khúc B2B? Có ngoại lệ không khóa công nợ cho khách hàng B2B đặc thù (ví dụ hợp đồng khung/VIP) hay không?
   - Chiết khấu `3% / 5% / 8%` áp dụng cho toàn bộ danh mục hàng hóa hay loại trừ một số nhóm sản phẩm/dịch vụ đặc thù?
   - Chiết khấu thương mại này có được áp dụng song song với các chương trình khuyến mãi hoặc bảng giá hợp đồng riêng không?

---

### Phiếu chấm nhanh V5-05

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho V5-05:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---

## Ca V5-06 — Tài liệu dài cần tổ chức lại

- **Tiêu đề / Chủ đề:** Quy định làm việc từ xa và bảo mật thiết bị (4 đoạn lộn xộn cần tái cấu trúc)
- **Đối tượng đọc:** Toàn thể nhân viên công ty
- **Mục đích giao tiếp:** Tổ chức lại 4 đoạn quy định rải rác thành hướng dẫn mạch lạc theo tình huống sử dụng (khi đăng ký làm từ xa, khi kết nối mạng, khi mất máy), giữ nguyên mọi mốc thời gian và điều kiện.

### Yêu cầu & Văn bản nguồn

```text
Biên tập và sắp xếp lại toàn bộ quy định 3 đoạn dài và bị lặp/nhảy ý dưới đây thành một bản hướng dẫn nội bộ rõ ràng, dễ tra cứu cho toàn thể nhân viên (gom các quy tắc cùng chủ đề vào đúng chỗ, giữ nguyên toàn bộ mốc thời gian 1 ngày làm việc, 09:00 sáng, 2 giờ, quy định VPN/Wi-Fi công cộng và không tự thêm tên phần mềm hay hình thức kỷ luật ngoài nguồn):

Quy định nội bộ về điều kiện thực hiện làm việc từ xa và nguyên tắc bảo đảm an toàn thông tin trên thiết bị cấp phát

Nhằm tạo điều kiện linh hoạt trong tổ chức công việc nhưng vẫn duy trì kỷ luật vận hành chung, nhân viên có nhu cầu làm việc từ xa theo kế hoạch cần chủ động gửi yêu cầu đăng ký và nhận được sự phê duyệt từ Quản lý trực tiếp trước ít nhất 01 ngày làm việc. Ngoài ra, trong quá trình xử lý công việc bên ngoài văn phòng, toàn thể nhân sự tuyệt đối không được phép sử dụng các mạng Wi-Fi công cộng không đi qua kênh mã hóa để mở dữ liệu khách hàng hoặc truy cập kho mã nguồn, đồng thời bắt buộc phải kích hoạt kết nối VPN của công ty mỗi khi truy xuất vào các hệ thống tài nguyên nội bộ.

Về quy trình xử lý trong tình huống phát sinh sự cố an ninh thiết bị, nếu xảy ra trường hợp thiết bị làm việc do công ty cấp phát bị thất lạc, mất cắp hoặc nghi ngờ bị truy cập trái phép trong lúc làm việc ngoài văn phòng, nhân sự liên quan có trách nhiệm thông báo khẩn cho bộ phận IT Security trong khoảng thời gian tối đa không vượt quá 02 giờ đồng hồ kể từ thời điểm phát hiện sự việc nhằm giúp bộ phận kỹ thuật kịp thời thực hiện lệnh khóa thiết bị và thu hồi toàn bộ quyền truy cập từ xa.

Quay lại với quy trình xin phép, đối với những tình huống đột xuất mang tính bất khả kháng như nhân viên bị ốm đột ngột hoặc phát sinh việc gia đình khẩn cấp không thể kịp xin phép trước một ngày theo thông lệ, quy định cho phép ngoại lệ là nhân viên phải chủ động nhắn tin báo cáo trực tiếp cho Quản lý trực tiếp của mình trước mốc 09:00 sáng cùng ngày làm việc đó. Cuối cùng, việc tuân thủ đồng thời cả thời hạn đăng ký lẫn yêu cầu sử dụng VPN nêu trên là điều kiện bắt buộc xuyên suốt thời gian làm việc ngoài trụ sở.
```

### Câu hỏi kiểm tra độ hiểu (Comprehension Check)

- 1. Một nhân viên muốn tìm nhanh điều kiện xin làm việc từ xa (thường vs đột xuất sáng cùng ngày), quy tắc VPN/Wi-Fi công cộng, và hạn báo mất thiết bị (tối đa 2 giờ) có tra được ngay không?
- 2. Bản viết lại có gom đúng các quy định bị nhảy/lặp ở đoạn 1 và đoạn 3 bản gốc vào cùng chủ đề xin phép mà không bịa thêm tên app chat hay mức kỷ luật không?

### V5-06 — Mẫu 1

# Hướng dẫn Làm việc Từ xa và An toàn Thông tin trên Thiết bị Cấp phát

Hướng dẫn này áp dụng cho toàn thể nhân viên khi làm việc ngoài văn phòng trên thiết bị do công ty cấp phát, nhằm tạo sự linh hoạt trong tổ chức công việc nhưng vẫn duy trì kỷ luật vận hành chung.

**Điều kiện bắt buộc:** Xuyên suốt thời gian làm việc ngoài trụ sở, nhân viên phải tuân thủ đồng thời cả thời hạn đăng ký và quy định sử dụng VPN dưới đây.

## 1. Quy trình đăng ký và xin phép
- **Làm việc từ xa theo kế hoạch:** Chủ động gửi yêu cầu đăng ký và được Quản lý trực tiếp phê duyệt **trước ít nhất 01 ngày làm việc**.
- **Trường hợp đột xuất, bất khả kháng** *(như ốm đột ngột hoặc phát sinh việc gia đình khẩn cấp không kịp xin phép trước 01 ngày)*: Chủ động nhắn tin báo cáo trực tiếp cho Quản lý trực tiếp **trước 09:00 sáng cùng ngày làm việc**.

## 2. Quy định bảo mật kết nối khi làm việc ngoài văn phòng
- **VPN công ty:** Bắt buộc kích hoạt kết nối VPN của công ty mỗi khi truy cập các hệ thống tài nguyên nội bộ.
- **Wi-Fi công cộng:** Tuyệt đối không sử dụng mạng Wi-Fi công cộng không đi qua kênh mã hóa để mở dữ liệu khách hàng hoặc truy cập kho mã nguồn.

## 3. Quy trình xử lý sự cố an ninh thiết bị
Nếu thiết bị do công ty cấp phát bị **thất lạc, mất cắp** hoặc **nghi ngờ bị truy cập trái phép** trong lúc làm việc ngoài văn phòng, nhân sự liên quan phải **thông báo khẩn cho bộ phận IT Security trong tối đa 02 giờ** kể từ thời điểm phát hiện sự việc, để bộ phận kỹ thuật kịp thời khóa thiết bị và thu hồi toàn bộ quyền truy cập từ xa.

---

### V5-06 — Mẫu 2

# Hướng dẫn nội bộ: Điều kiện làm việc từ xa và An toàn thông tin trên thiết bị cấp phát

Hướng dẫn này áp dụng cho toàn thể nhân viên nhằm tạo điều kiện làm việc linh hoạt nhưng vẫn duy trì kỷ luật vận hành và bảo đảm an toàn thông tin. Việc tuân thủ đồng thời thời hạn đăng ký làm việc từ xa lẫn yêu cầu sử dụng VPN là điều kiện bắt buộc xuyên suốt thời gian làm việc ngoài trụ sở.

## 1. Quy trình đăng ký và xin phép làm việc từ xa

- **Làm việc từ xa theo kế hoạch:** Nhân viên chủ động gửi yêu cầu đăng ký và nhận phê duyệt từ **Quản lý trực tiếp** **trước ít nhất 01 ngày làm việc**.
- **Ngoại lệ đột xuất, bất khả kháng** *(như ốm đột ngột hoặc phát sinh việc gia đình khẩn cấp không thể xin phép trước 01 ngày theo thông lệ)*: Nhân viên phải chủ động nhắn tin báo cáo trực tiếp cho **Quản lý trực tiếp** **trước 09:00 sáng** cùng ngày làm việc đó.

## 2. Nguyên tắc kết nối mạng và truy cập hệ thống ngoài văn phòng

- **Mạng Wi-Fi công cộng:** Tuyệt đối không sử dụng các mạng Wi-Fi công cộng không đi qua kênh mã hóa để mở dữ liệu khách hàng hoặc truy cập kho mã nguồn.
- **Kết nối VPN của công ty:** Bắt buộc kích hoạt VPN mỗi khi truy xuất vào các hệ thống tài nguyên nội bộ.

## 3. Quy trình xử lý sự cố an ninh thiết bị cấp phát

- **Tình huống phát sinh:** Thiết bị làm việc do công ty cấp phát bị thất lạc, mất cắp hoặc nghi ngờ bị truy cập trái phép trong lúc làm việc ngoài văn phòng.
- **Hành động bắt buộc:** Nhân sự liên quan phải thông báo khẩn cho **bộ phận IT Security** trong thời gian **tối đa 02 giờ** kể từ thời điểm phát hiện sự việc.
- **Mục đích xử lý:** Giúp bộ phận kỹ thuật kịp thời khóa thiết bị và thu hồi toàn bộ quyền truy cập từ xa.

---

### V5-06 — Mẫu 3

**Hướng dẫn làm việc từ xa và bảo đảm an toàn thông tin trên thiết bị công ty**

Trong suốt thời gian làm việc ngoài trụ sở, nhân viên bắt buộc phải tuân thủ đồng thời cả thời hạn đăng ký và yêu cầu sử dụng VPN dưới đây.

**1. Xin phép làm việc từ xa**
- **Theo kế hoạch:** Gửi yêu cầu đăng ký và được Quản lý trực tiếp phê duyệt trước ít nhất **01 ngày làm việc**.
- **Đột xuất bất khả kháng:** Nếu bị ốm đột ngột hoặc có việc gia đình khẩn cấp nên không thể xin phép trước 01 ngày, bạn phải chủ động nhắn tin báo trực tiếp cho Quản lý trực tiếp trước **09:00 sáng** cùng ngày làm việc đó.

**2. Kết nối mạng và sử dụng VPN**
- **Tuyệt đối không** sử dụng Wi-Fi công cộng không qua kênh mã hóa để mở dữ liệu khách hàng hoặc truy cập kho mã nguồn.
- **Bắt buộc bật kết nối VPN của công ty** mỗi khi truy cập vào các hệ thống tài nguyên nội bộ.

**3. Xử lý khi thiết bị gặp sự cố an ninh**
- Trong lúc làm việc ngoài văn phòng, nếu thiết bị do công ty cấp phát bị thất lạc, mất cắp hoặc nghi ngờ bị truy cập trái phép, bạn phải báo khẩn cho bộ phận **IT Security** trong tối đa **02 giờ** kể từ thời điểm phát hiện.
- Việc báo kịp thời giúp IT Security thực hiện khóa thiết bị và thu hồi toàn bộ quyền truy cập từ xa.

---

### V5-06 — Mẫu 4

# Hướng dẫn làm việc từ xa và bảo đảm an toàn thông tin trên thiết bị cấp phát

Nhằm tạo sự linh hoạt trong công việc nhưng vẫn giữ vững kỷ luật vận hành, toàn thể nhân viên làm việc ngoài văn phòng cần nắm rõ và thực hiện đúng các quy định dưới đây. Việc tuân thủ đồng thời thời hạn đăng ký và yêu cầu sử dụng VPN là điều kiện bắt buộc xuyên suốt thời gian làm việc ngoài trụ sở.

## 1. Đăng ký và xin phép làm việc từ xa
* **Làm việc từ xa theo kế hoạch:** Chủ động gửi yêu cầu đăng ký và **nhận được sự phê duyệt từ Quản lý trực tiếp trước ít nhất 01 ngày làm việc**.
* **Trường hợp đột xuất, bất khả kháng** *(như bị ốm đột ngột hoặc phát sinh việc gia đình khẩn cấp nên không kịp xin phép trước 01 ngày)*: Chủ động **nhắn tin báo cáo trực tiếp cho Quản lý trực tiếp trước 09:00 sáng** cùng ngày làm việc đó.

## 2. Bảo mật kết nối khi làm việc ngoài văn phòng
* **Bắt buộc bật VPN của công ty:** Kích hoạt kết nối VPN của công ty mỗi khi truy cập vào các hệ thống tài nguyên nội bộ.
* **Không dùng Wi-Fi công cộng không qua kênh mã hóa:** Tuyệt đối không sử dụng các mạng Wi-Fi công cộng không đi qua kênh mã hóa để mở dữ liệu khách hàng hoặc truy cập kho mã nguồn.

## 3. Xử lý sự cố an ninh thiết bị
* Khi thiết bị làm việc do công ty cấp phát bị **thất lạc, mất cắp hoặc nghi ngờ bị truy cập trái phép** trong lúc làm việc ngoài văn phòng, nhân viên liên quan phải **thông báo khẩn cho bộ phận IT Security trong tối đa 02 giờ** kể từ thời điểm phát hiện sự việc.
* Việc báo cáo kịp thời giúp bộ phận kỹ thuật nhanh chóng khóa thiết bị và thu hồi toàn bộ quyền truy cập từ xa.

---

### V5-06 — Mẫu 5

# Hướng dẫn nội bộ: Điều kiện làm việc từ xa và Bảo đảm an toàn thông tin trên thiết bị cấp phát

**Phạm vi áp dụng:** Toàn thể nhân viên khi làm việc từ xa (ngoài trụ sở/văn phòng).  
**Nguyên tắc chung:** Nhằm tạo sự linh hoạt trong công việc nhưng vẫn duy trì kỷ luật vận hành, nhân viên phải tuân thủ đồng thời **thời hạn đăng ký (hoặc báo cáo ngoại lệ)** và **yêu cầu sử dụng VPN** trong suốt thời gian làm việc ngoài trụ sở.

---

## 1. Quy trình đăng ký và báo cáo làm việc từ xa

- **Làm việc từ xa theo kế hoạch:**  
  Nhân viên phải chủ động gửi yêu cầu đăng ký và **được Quản lý trực tiếp phê duyệt trước ít nhất 01 ngày làm việc**.
- **Trường hợp đột xuất mang tính bất khả kháng** *(như ốm đột ngột hoặc phát sinh việc gia đình khẩn cấp, không kịp xin phép trước 01 ngày làm việc theo thông lệ)*:  
  Nhân viên được áp dụng ngoại lệ bằng cách **nhắn tin báo cáo trực tiếp cho Quản lý trực tiếp trước 09:00 sáng cùng ngày làm việc đó**.

---

## 2. Nguyên tắc bảo đảm an toàn thông tin khi làm việc ngoài văn phòng

- **Bắt buộc bật VPN:** Phải kích hoạt kết nối **VPN của công ty** mỗi khi truy xuất vào các hệ thống tài nguyên nội bộ.
- **Cấm dùng Wi-Fi công cộng không mã hóa cho dữ liệu nhạy cảm:** Tuyệt đối **không** sử dụng các mạng Wi-Fi công cộng không đi qua kênh mã hóa để:
  - Mở dữ liệu khách hàng; hoặc
  - Truy cập kho mã nguồn.

---

## 3. Quy trình xử lý sự cố an ninh thiết bị cấp phát

- **Tình huống cần báo cáo:** Thiết bị làm việc do công ty cấp phát bị **thất lạc**, **mất cắp** hoặc **nghi ngờ bị truy cập trái phép** trong lúc làm việc ngoài văn phòng.
- **Hành động và thời hạn:** Nhân sự liên quan phải **thông báo khẩn cho bộ phận IT Security trong tối đa 02 giờ** kể từ thời điểm phát hiện sự việc.
- **Mục đích xử lý:** Giúp bộ phận kỹ thuật kịp thời thực hiện lệnh khóa thiết bị và thu hồi toàn bộ quyền truy cập từ xa.

---

## 4. Bảng tra cứu nhanh

| Tình huống | Việc cần làm / Quy tắc | Thời hạn / Phạm vi bắt buộc | Đầu mối tiếp nhận |
|---|---|---|---|
| Làm việc từ xa theo kế hoạch | Gửi yêu cầu đăng ký và nhận phê duyệt | Trước ít nhất **01 ngày làm việc** | Quản lý trực tiếp |
| Làm việc từ xa đột xuất *(ốm đột ngột, việc gia đình khẩn cấp)* | Nhắn tin báo cáo trực tiếp | Trước **09:00 sáng** cùng ngày làm việc đó | Quản lý trực tiếp |
| Truy xuất hệ thống tài nguyên nội bộ | Kích hoạt kết nối VPN của công ty | Xuyên suốt thời gian làm việc ngoài trụ sở | — |
| Mở dữ liệu khách hàng hoặc truy cập kho mã nguồn | Tuyệt đối không dùng mạng Wi-Fi công cộng không đi qua kênh mã hóa | Mọi lúc xử lý công việc ngoài văn phòng | — |
| Thiết bị cấp phát bị thất lạc, mất cắp hoặc nghi ngờ bị truy cập trái phép | Thông báo khẩn để khóa thiết bị và thu hồi quyền truy cập từ xa | Tối đa **02 giờ** kể từ lúc phát hiện sự việc | Bộ phận IT Security |

---

### Phiếu chấm nhanh V5-06

| Mẫu | C1 Hiểu nhanh (1-5) | C2 Tự nhiên (1-5) | C3 Tổ chức (1-5) | C4 Đúng đối tượng (1-5) | C5 Gọn đủ ý (1-5) | C6 Ít đọc lại (1-5) | Đạt Comprehension? (Y/N) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mẫu 1 | | | | | | | |
| Mẫu 2 | | | | | | | |
| Mẫu 3 | | | | | | | |
| Mẫu 4 | | | | | | | |
| Mẫu 5 | | | | | | | |

- **Lựa chọn tốt nhất cho V5-06:** `Mẫu ___`
- **Xếp hạng Top 2 / Ghi chú lý do:** 

---
