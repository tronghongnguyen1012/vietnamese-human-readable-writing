# Hệ thống Phân loại Lỗi Làm Văn bản Tiếng Việt Khó Đọc và Khó Hiểu (Error Taxonomy)

Hệ thống này gồm **18 nhóm lỗi** chia theo **4 cấp độ** (Câu, Đoạn, Tài liệu, Người đọc). Mã lỗi (`S-01`..`R-04`) được dùng thống nhất để gắn nhãn trong quy trình đánh giá MQM và kiểm thử chất lượng.

## Tổng quan Nhanh

| Cấp độ | Mã lỗi | Tên nhóm lỗi | Rủi ro chính đối với người đọc |
|---|---|---|---|
| **Câu** | `S-01` | Danh từ hóa rỗng & cụm vị từ hình thức | Tăng số bước giải mã, mờ chủ thể–hành động |
| | `S-02` | Khuyết hoặc ẩn tác thể / đối tượng chịu tác động | Không biết ai thực hiện, tác động lên thực thể nào |
| | `S-03` | Mơ hồ phạm vi logic, điều kiện và quy chiếu | Hiểu sai điều kiện nghiệp vụ (*Subconscious Disambiguation*) |
| | `S-04` | Bị động máy móc & dịch sát cú pháp tiếng Anh | Văn phong gượng gạo, trật tự bổ ngữ khó bám |
| | `S-05` | Từ ngữ trừu tượng, rỗng nghĩa & khuếch đại hình thức | Tốn công lọc chữ, không rút ra dữ kiện cụ thể |
| | `S-06` | Dịch cưỡng ép hoặc không nhất quán thuật ngữ | Đứt khớp khái niệm chuyên môn, tra sai thực thể |
| **Đoạn** | `P-01` | Chôn vùi ý chính & vòng vo mở bài | Phải đọc qua lớp đệm mới chạm được kết luận |
| | `P-02` | Liên kết giả (lạm dụng từ nối không có mạch logic) | Cảm giác "mượt" giả tạo nhưng các câu không nối ý |
| | `P-03` | Đứt mạch Đề–Thuyết & nhảy tiêu điểm thực thể | Bộ nhớ làm việc phải tái lập ngữ cảnh liên tục |
| | `P-04` | Lặp diễn giải không tăng thông tin | Kéo dài văn bản vô ích, giảm mật độ thông tin |
| **Tài liệu** | `D-01` | Trộn lẫn chế độ tài liệu | Người cần tra cứu phải đọc lý thuyết; người học bị ngợp spec |
| | `D-02` | Trình tự thông tin ngược quy trình tiếp nhận | Bỏ sót điều kiện tiên quyết, cảnh báo hoặc ngoại lệ |
| | `D-03` | Thiếu ngữ cảnh, phạm vi áp dụng hoặc giả định đầu vào | Không biết áp dụng quy tắc cho trường hợp nào |
| | `D-04` | Lệch cấu trúc trình bày | Bức tường chữ cho logic rẽ nhánh HOẶC bullet hóa hội thoại |
| **Người đọc** | `R-01` | Lệch trình độ người đọc | Dư thừa gây bực bội cho chuyên gia hoặc thiếu nền cho người mới |
| | `R-02` | Lệch thanh điệu & ngữ cảnh sử dụng | Biến chat thành văn bản hành chính hoặc làm spec thiếu chuẩn |
| | `R-03` | Thiếu tính khả dụng hành động hoặc tính kiểm chứng | Đọc hiểu bề mặt nhưng không làm việc / test được |
| | `R-04` | Đơn giản hóa làm sai lệch hoặc rơi điều kiện quan trọng | Hiểu sai bản chất nghiệp vụ/kỹ thuật (tiệm cận Hard Fail) |

---

## Cấp độ 1: Cấp độ Câu (`S-01` – `S-06`)

### `S-01`: Danh từ hóa rỗng & cụm vị từ hình thức

1. **Định nghĩa:** Chuyển động từ/tính từ diễn tả hành động hoặc trạng thái cụ thể thành danh ngữ trừu tượng bằng các từ đệm như *"việc"*, *"sự"*, *"tính"*, *"năng lực"*, *"quá trình"*, kết hợp với động từ hình thức rỗng nghĩa (*"cung cấp"*, *"thực hiện"*, *"hỗ trợ"*, *"đảm bảo"*, *"tiến hành"*).
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Cấu trúc danh từ hóa (*nominalization*) phổ biến trong văn bản học thuật/kinh doanh tiếng Anh được mô hình tái tạo sang tiếng Việt thông qua quá trình SFT dịch sát cấu trúc (*translationese*, Li et al., 2025; Cao Xuân Hạo, 1991).
   - `[Giả thuyết]` LLM gắn xác suất cao cho các cụm danh từ dài vì chúng xuất hiện dày đặc trong văn bản hành chính và tài liệu doanh nghiệp dịch thuật trên web.
3. **Dấu hiệu nhận biết:** Xuất hiện các chuỗi như *"cung cấp năng lực [V]"*, *"hỗ trợ việc [V]"*, *"thực hiện quá trình [V]"*, *"đảm bảo tính [Adj]"*, *"nhằm đáp ứng các kịch bản..."*.
4. **Ví dụ không đạt:**
   > Phân hệ PAY cung cấp năng lực xử lý các giao dịch thanh toán từng phần, hỗ trợ việc phân bổ giá trị thanh toán trên nhiều phương thức nhằm đáp ứng các kịch bản nghiệp vụ tại điểm bán.
5. **Ví dụ đã cải thiện:**
   > Khi thực hiện thanh toán, một order có thể được chia thành nhiều lần thanh toán bằng các phương thức khác nhau.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa & Tác thể–Đối tượng:** Bản không đạt đóng gói 3 hành động vào 3 lớp danh từ hóa/động từ đệm (*"cung cấp năng lực xử lý"*, *"hỗ trợ việc phân bổ giá trị"*, *"đáp ứng các kịch bản nghiệp vụ"*). Đặc biệt, đối tượng chịu tác động thực sự (**order / đơn hàng**) biến mất, nhường chỗ cho danh từ trừu tượng *"các giao dịch thanh toán từng phần"*. Bản cải thiện đặt rõ ngữ cảnh Đề (*"Khi thực hiện thanh toán"*), chủ thể nghiệp vụ (*"một order"*), và hành động trực tiếp (*"chia thành nhiều lần thanh toán bằng các phương thức khác nhau"*).
   - **Lượng thông tin:** Bản không đạt dài 36 chữ nhưng chỉ chứa thông tin cốt lõi tương đương 21 chữ của bản cải thiện; phần còn lại (*"cung cấp năng lực"*, *"hỗ trợ việc"*, *"các kịch bản nghiệp vụ"*) là từ đệm không bổ sung dữ kiện kỹ thuật hay điều kiện nào (còn *"tại điểm bán"* chỉ cần giữ nếu phạm vi yêu cầu chỉ áp dụng ở POS).
   - **Công sức người đọc (Cognitive Load):** Với bản không đạt, bộ nhớ làm việc phải bóc 3 lớp danh ngữ để suy luận xem *"ai chia cái gì thành nhiều phần"*; với bản cải thiện, người đọc dựng ngay được mô hình tình huống (*Situation model*, Kintsch, 1998) chỉ trong một lượt đọc.
7. **Trường hợp ngoại lệ:** Khi cần danh từ hóa để làm **Đề ngữ** tham chiếu lại sự kiện đã nêu ở câu trước (ví dụ: *"Việc chia thanh toán này chỉ áp dụng cho đơn đã xác nhận"*), hoặc danh từ hóa tên khái niệm/mục tiêu chuẩn (*"quản lý phân quyền"*, *"tính toàn vẹn dữ liệu"*).

---

### `S-02`: Khuyết hoặc ẩn tác thể / đối tượng chịu tác động

1. **Định nghĩa:** Câu lược bỏ chủ thể thực hiện hành động (hệ thống nào, vai trò nào, dịch vụ nào) hoặc đối tượng chịu tác động trong khi ngữ cảnh trước đó chưa xác lập rõ.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Trong tiếng Việt khẩu ngữ, tỉnh lược chủ ngữ rất phổ biến khi cùng ngữ cảnh (Trần Ngọc Thêm, 1985), nhưng LLM áp dụng tùy tiện vào đặc tả kỹ thuật/nghiệp vụ vốn đòi hỏi quy trách nhiệm rõ (ISO/IEC/IEEE 29148).
   - `[Suy luận]` Ghép câu bị động không tác thể (*"Dữ liệu được kiểm tra..."*) khiến người đọc không biết kiểm tra ở Client, API Gateway hay Core Service.
3. **Dấu hiệu nhận biết:** Câu mở đầu bằng *"Cần kiểm tra..."*, *"Sẽ tiến hành đồng bộ..."*, *"Hệ thống xử lý..."* (khi tài liệu có 3 hệ thống khác nhau) hoặc *"Trạng thái được cập nhật..."* mà không rõ ai/module nào cập nhật.
4. **Ví dụ không đạt:**
   > Sau khi gửi yêu cầu hoàn tiền, giao dịch sẽ được xác nhận và cập nhật trạng thái trước khi gửi thông báo.
5. **Ví dụ đã cải thiện:**
   > Sau khi nhân viên thu ngân gửi yêu cầu hoàn tiền, hệ thống POS gửi lệnh tới cổng thanh toán để xác nhận. Khi cổng thanh toán trả kết quả thành công, POS cập nhật trạng thái đơn sang `REFUNDED` rồi gửi email cho khách hàng.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa:** Câu không đạt ẩn 3 tác thể khác nhau (người gửi yêu cầu, bên xác nhận, bên cập nhật & thông báo), làm lập trình viên và QA không phân định được ranh giới trách nhiệm giữa POS và Payment Gateway.
   - **Lượng thông tin & Tải nhận thức:** Bản cải thiện tăng độ dài nhưng bổ sung đúng **thông tin thực thi bắt buộc** (ai gọi ai, điều kiện chuyển trạng thái), triệt tiêu công sức hỏi lại hoặc đoán mò ranh giới hệ thống.
7. **Trường hợp ngoại lệ:** Hội thoại nhanh giữa 2 người đã đồng thuận bối cảnh, hoặc chuỗi gạch đầu dòng nằm dưới một tiêu đề đã khóa rõ một tác thể duy nhất (ví dụ dưới mục *"Trách nhiệm của Payment Service:"*).

---

### `S-03`: Mơ hồ phạm vi logic, điều kiện và quy chiếu

1. **Định nghĩa:** Câu chứa cấu trúc đa nghĩa về phạm vi tác động của liên từ logic (*và/hoặc/không*), trạng ngữ điều kiện/ngoại lệ, ngưỡng định lượng mơ hồ, hoặc đại từ quy chiếu (*nó, điều này, việc đó*) trỏ được vào nhiều tiền ngữ.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Berry, Kamsties & Krieger (2003) xác định 5 nguồn mơ hồ ngôn ngữ (từ vựng, cú pháp, quy chiếu, phạm vi logic, tính mơ hồ biên độ) và cảnh báo hiện tượng *Subconscious Disambiguation* — người viết lẫn người đọc tự chọn một cách hiểu mà không nhận ra tồn tại cách hiểu thứ hai.
3. **Dấu hiệu nhận biết:** Cụm *"A và B hoặc C"*, *"không hỗ trợ A khi B và C"*, *"chỉ áp dụng cho khách hàng VIP có đơn trên 1 triệu và chưa sử dụng voucher"* (khó phân định điều kiện `và` gắn với vế nào), đại từ *"điều này"* đứng đầu câu sau một câu ghép 2–3 mệnh đề.
4. **Ví dụ không đạt:**
   > Hệ thống không cho phép hủy đơn hàng đối với tài khoản chưa xác thực hoặc đơn đã đóng gói và giao cho đơn vị vận chuyển.
5. **Ví dụ đã cải thiện:**
   > Hệ thống từ chối hủy đơn hàng nếu rơi vào **một trong hai trường hợp** sau:
   > 1. Tài khoản chưa xác thực.
   > 2. Đơn hàng đã đóng gói **và** đã bàn giao cho đơn vị vận chuyển.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa:** Câu gốc có 2 cách gom nhóm ngoặc logic khác nhau: `(chưa xác thực HOẶC đã đóng gói) VÀ đã giao`, hoặc `chưa xác thực HOẶC (đã đóng gói VÀ đã giao)`. Nếu đơn đã đóng gói nhưng *chưa* giao cho vận chuyển, lập trình viên và QA có thể code trái ngược nhau.
   - **Lượng thông tin & Tải nhận thức:** Bản cải thiện giữ nguyên 100% điều kiện nhưng tách thành danh sách đánh số cùng từ khóa phạm vi (*"một trong hai trường hợp"*). Người đọc không phải tự đặt dấu ngoặc logic trong đầu, loại bỏ hoàn toàn *Subconscious Disambiguation*.
7. **Trường hợp ngoại lệ:** Câu hội thoại đời thường với ngữ cảnh vật lý hiển nhiên không gây rủi ro nghiệp vụ (ví dụ: *"Chiều nay mình uống cà phê hay trà sữa?"*).

---

### `S-04`: Bị động máy móc & dịch sát cú pháp tiếng Anh

1. **Định nghĩa:** Lạm dụng *"được"*, *"bị"*, *"...bởi..."*, mệnh đề quan hệ dịch sát (*"cái mà"*, *"nơi mà"*, *"một cách [Adj]"*), hoặc đảo cụm giới từ/trạng ngữ theo đúng trật tự tiếng Anh khiến câu tiếng Việt gượng gạo, sai sắc thái ngữ dụng.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Cao Xuân Hạo (1991) và Nguyễn Đức Dân chỉ ra tiếng Việt phân biệt *"được"* (có lợi) và *"bị"* (bất lợi); sử dụng chúng như *to be + V-ed* trung tính cho chủ thể vô tri là dấu hiệu Âu hóa cú pháp.
   - `[Bằng chứng]` Li et al. (2025) chứng minh cơ chế SFT tạo thiên lệch dịch sát cú pháp (*translationese*).
3. **Dấu hiệu nhận biết:** *"được thực hiện bởi"*, *"bị ảnh hưởng một cách đáng kể"*, *"những cái mà"*, *"đối với việc mà hệ thống..."*, cụm danh từ dài kẹp bổ ngữ phía trước không tự nhiên.
4. **Ví dụ không đạt:**
   > Lỗi này được gây ra bởi token xác thực đã bị hết hạn một cách bất ngờ trong quá trình đồng bộ.
5. **Ví dụ đã cải thiện:**
   > Lỗi xảy ra vì token xác thực hết hạn giữa lúc đang đồng bộ.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa & Ngữ dụng:** Bản gốc dùng *"được gây ra bởi"* (ghép *"được"* tích cực với *"lỗi"* tiêu cực — phản cảm ngữ dụng tiếng Việt), cộng với *"bị hết hạn một cách bất ngờ"* dịch sát từ *unexpectedly*.
   - **Lượng thông tin & Tải nhận thức:** Bản cải thiện rút từ 21 chữ xuống 13 chữ mà giữ nguyên nguyên nhân gốc (token hết hạn lúc đồng bộ), bỏ cụm dịch sát dư thừa và khôi phục quan hệ nhân–quả trực tiếp (*"xảy ra vì..."*).
7. **Trường hợp ngoại lệ:** Dùng *"được"* hoặc *"bị"* khi thực sự mang sắc thái lợi/bất lợi tự nhiên và không có tác thể cần nêu (ví dụ: *"Đơn hàng bị hủy do quá hạn thanh toán"*, *"Hồ sơ đã được duyệt"*).

---

### `S-05`: Từ ngữ trừu tượng, rỗng nghĩa & khuếch đại hình thức

1. **Định nghĩa:** Dùng từ ngữ sáo rỗng, khoa trương hoặc quá trừu tượng không gắn với hành vi/con số quan sát được (nhằm tạo cảm giác "chuyên nghiệp" nhưng không truyền tải nội dung cụ thể).
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Dự án *Wikipedia: Signs of AI writing* ghi nhận LLM thường chèn các mẫu khuếch đại (*puffery*, *hollow significance*) học từ văn bản tiếp thị và bài luận mẫu.
   - `[Bằng chứng]` Vi phạm Phương châm Chất và Phương châm Lượng của Grice (1975).
3. **Dấu hiệu nhận biết:** *"tối ưu hóa trải nghiệm người dùng một cách toàn diện"*, *"giải pháp mang tính đột phá/chiến lược"*, *"đóng vai trò then chốt không thể thiếu"*, *"nâng cao hiệu suất vượt trội"*, *"hướng tới sự phát triển bền vững"*.
4. **Ví dụ không đạt:**
   > Cơ chế caching mới giúp tối ưu hóa hiệu năng hệ thống một cách vượt trội và nâng cao trải nghiệm người dùng toàn diện.
5. **Ví dụ đã cải thiện:**
   > Cơ chế cache Redis mới giảm thời gian phản hồi API tìm kiếm từ 800 ms xuống còn 120 ms (hoặc *giảm tải truy vấn trực tiếp vào database* nếu chưa có số liệu đo).
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa & Lượng thông tin:** Câu không đạt gần như có **mật độ thông tin gần bằng 0** cho kỹ sư hay quản lý sản phẩm vì không trả lời *cải thiện cái gì* và *bằng cách nào*. Bản cải thiện thay mỹ từ rỗng bằng cơ chế cụ thể và tác động đo được (chú ý: chỉ đưa số liệu nếu có trong dữ liệu đầu vào; nếu không có, chỉ nêu cơ chế kỹ thuật thật).
   - **Công sức người đọc:** Người đọc không phải tự đặt câu hỏi *"Rốt cuộc nhanh hơn chỗ nào?"* hay lọc bỏ lớp quảng cáo trước khi ra quyết định.
7. **Trường hợp ngoại lệ:** Văn bản truyền thông/thương hiệu khi người dùng *chủ đích* yêu cầu viết thông điệp marketing truyền cảm hứng (nhưng ngay cả khi đó vẫn nên neo bằng lợi ích cụ thể thay vì sáo ngữ).

---

### `S-06`: Dịch cưỡng ép hoặc không nhất quán thuật ngữ

1. **Định nghĩa:** (a) Dịch từng chữ thuật ngữ chuyên ngành vốn dùng nguyên gốc tiếng Anh hoặc Hán–Việt ổn định trong cộng đồng chuyên môn Việt Nam khiến người đọc không nhận ra khái niệm gốc; hoặc (b) dùng nhiều tên gọi khác nhau cho cùng một thực thể trong cùng văn bản.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Suy luận]` Model cố gắng "thuần Việt hóa" 100% theo chỉ thị ngầm viết tiếng Việt, hoặc thay đổi từ đồng nghĩa ở câu sau để "tránh lặp từ" theo thói quen viết văn miêu tả.
   - `[Bằng chứng]` Vi phạm tiêu chuẩn **Consistent** của ISO/IEC/IEEE 29148 và chuẩn Terminology trong MQM (Lommel et al., 2014).
3. **Dấu hiệu nhận biết:** Dịch *"pull request"* thành *"yêu cầu kéo"*, *"idempotency"* thành *"tính bất biến lũy đẳng"* không chú thích; hoặc lúc gọi *"đơn hàng"*, lúc gọi *"phiếu đặt"*, lúc gọi *"giao dịch"* cho cùng một object `Order`.
4. **Ví dụ không đạt:**
   > Khi gọi điểm cuối thanh toán, hãy truyền khóa bất biến lũy đẳng để tránh phiếu đặt bị trừ tiền hai lần nếu yêu cầu kéo lại bị trễ.
5. **Ví dụ đã cải thiện:**
   > Khi gọi API thanh toán, hãy truyền `idempotency_key` (khóa chống trùng giao dịch) để tránh trừ tiền hai lần nếu client gửi lại request do timeout.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa:** *"điểm cuối"* (endpoint) hay *"yêu cầu kéo"* buộc kỹ sư Việt Nam phải dịch ngược từ tiếng Việt sang tiếng Anh trong đầu để tra tài liệu code; việc đổi tên `Order` thành *"phiếu đặt"* gây nghi ngờ đây là một bảng dữ liệu khác.
   - **Tải nhận thức:** Giữ thuật ngữ quen dùng trong ngành (`API`, `idempotency_key`, `client`, `request`, `timeout`) kèm giải thích ngắn bằng tiếng Việt nếu người đọc rộng giảm mạnh nỗ lực tra cứu chéo.
7. **Trường hợp ngoại lệ:** Tài liệu đào tạo phổ thông hoặc hướng dẫn cho người dùng cuối hoàn toàn không biết thuật ngữ kỹ thuật — khi đó cần dùng từ Việt dễ hiểu nhưng phải thống nhất một tên gọi xuyên suốt.

---

## Cấp độ 2: Cấp độ Đoạn (`P-01` – `P-04`)

### `P-01`: Chôn vùi ý chính & vòng vo mở bài

1. **Định nghĩa:** Đoạn văn mở đầu bằng những câu khái quát hiển nhiên, định nghĩa sáo mòn hoặc lời rào đón (*throat-clearing*) trước khi đưa ra câu trả lời, kết luận hoặc ý chính ở cuối đoạn.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Suy luận]` LLM có xu hướng sinh văn bản theo cấu trúc bài luận quy nạp (mở đầu rộng → dẫn dắt → kết luận), trái với nhu cầu đọc tìm đáp án nhanh.
   - `[Bằng chứng]` Vi phạm **Pyramid Principle / BLUF** (Minto) và nguyên tắc **Findability** của ISO 24495-1:2023.
3. **Dấu hiệu nhận biết:** *"Trong bối cảnh chuyển đổi số hiện nay..."*, *"Việc X đóng vai trò vô cùng quan trọng..."*, *"Để trả lời câu hỏi này, trước hết chúng ta cần hiểu..."* trước một câu trả lời vốn chỉ cần 1–2 dòng.
4. **Ví dụ không đạt:**
   > Trong hệ thống phần mềm hiện đại, hiệu năng truy vấn cơ sở dữ liệu là một yếu tố then chốt quyết định trải nghiệm người dùng. Có rất nhiều nguyên nhân có thể dẫn đến tình trạng truy vấn chậm như thiếu bộ nhớ, mạng lag hoặc cấu trúc bảng chưa hợp lý. Đối với câu truy vấn bạn vừa gửi, vấn đề nằm ở việc cột `created_at` chưa có index nên Postgres phải quét toàn bộ bảng.
5. **Ví dụ đã cải thiện:**
   > Câu truy vấn này chậm vì cột `created_at` chưa có index, khiến Postgres phải quét toàn bộ bảng (`Seq Scan`). Bạn thêm index cho cột này là xử lý được.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Lượng thông tin & Tải nhận thức:** 2 câu đầu của bản không đạt (48 chữ) không chứa thông tin giúp người hỏi sửa lỗi; chúng ép người đọc đọc quét vượt qua 2 tầng thông tin thừa mới tới nguyên nhân thực sự ở câu 3. Bản cải thiện đưa ngay đáp án và nguyên nhân lên đầu (BLUF).
7. **Trường hợp ngoại lệ:** Bài giảng khái niệm cho người mới hoàn toàn chưa có bối cảnh — khi đó cần 1 câu nối ngắn nêu *vì sao vấn đề này xuất hiện* trước khi đi vào kết luận.

---

### `P-02`: Liên kết giả (nhồi từ nối nhưng không có mạch logic)

1. **Định nghĩa:** Sử dụng dày đặc các từ nối hình thức (*"Bên cạnh đó"*, *"Hơn nữa"*, *"Tuy nhiên"*, *"Từ đó"*, *"Do vậy"*) nhưng mối quan hệ logic thực sự giữa các câu không khớp với nghĩa của từ nối đó.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Trần Ngọc Thêm (1985) và Halliday & Hasan (1976) phân biệt rõ liên kết hình thức (*cohesion*) và liên kết nội dung (*coherence*): từ nối sai quan hệ không thể vá lỗ hổng logic.
   - `[Suy luận]` AI tạo nhịp văn đều đặn bằng cách đặt từ nối đầu mỗi câu dù các câu chỉ đang liệt kê song song.
3. **Dấu hiệu nhận biết:** Một đoạn 4–5 câu mà câu nào cũng mở đầu bằng từ nối; dùng *"Tuy nhiên"* cho hai ý không đối lập, hoặc *"Do đó"* khi câu sau không phải hệ quả tất yếu của câu trước.
4. **Ví dụ không đạt:**
   > Dịch vụ thanh toán hỗ trợ thẻ nội địa và ví điện tử. Tuy nhiên, mỗi giao dịch đều được lưu vết kiểm toán. Hơn nữa, thời gian timeout mặc định là 30 giây. Do đó, hệ thống đảm bảo tính minh bạch cao.
5. **Ví dụ đã cải thiện:**
   > Dịch vụ thanh toán hỗ trợ thẻ nội địa và ví điện tử với thời gian timeout mặc định là 30 giây. Mọi giao dịch đều được ghi log kiểm toán để phục vụ đối soát.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa:** Bản không đạt ghép 3 thuộc tính độc lập bằng *"Tuy nhiên"* (không có đối lập) và *"Do đó"* (timeout 30s không suy ra tính minh bạch). Người đọc mất công tìm mâu thuẫn hoặc quan hệ nhân quả vốn không tồn tại.
   - **Tải nhận thức:** Bản cải thiện bỏ từ nối giả, gom các thuộc tính vận hành (kênh hỗ trợ + timeout) vào một câu và tách riêng cơ chế lưu vết kèm mục đích thực tế (*"để phục vụ đối soát"*).
7. **Trường hợp ngoại lệ:** Khi thực sự có quan hệ nhân–quả, điều kiện hoặc tương phản chặt chẽ, bắt buộc giữ từ nối chính xác (*"Nếu ... thì ..."*, *"Trừ trường hợp ..."*, *"Ngược lại, ..."*).

---

### `P-03`: Đứt mạch Đề–Thuyết & nhảy tiêu điểm thực thể

1. **Định nghĩa:** Các câu liên tiếp thay đổi chủ thể trung tâm liên tục mà không có cầu nối từ thông tin cũ sang thông tin mới, làm đứt mạch theo dõi của người đọc.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Vi phạm **Centering Theory** (Grosz, Joshi & Weinstein, 1995) về duy trì tiêu điểm thực thể cục bộ và nguyên lý **Old-to-New** (Williams & Bizup) / cấu trúc **Đề–Thuyết** (Cao Xuân Hạo, 1991).
3. **Dấu hiệu nhận biết:** Câu 1 nói về Người dùng, Câu 2 nhảy sang Database, Câu 3 nhảy sang Email, Câu 4 quay lại Mật khẩu mà không móc nối thông tin cuối câu trước làm Đề cho câu sau.
4. **Ví dụ không đạt:**
   > Khi người dùng bấm "Quên mật khẩu", email đặt lại sẽ được gửi đi. Token chỉ có hiệu lực 15 phút trong bảng `password_resets`. Đường dẫn cũ sẽ bị vô hiệu hóa nếu người dùng bấm gửi lại nhiều lần.
5. **Ví dụ đã cải thiện:**
   > Khi người dùng bấm "Quên mật khẩu", hệ thống tạo một token có hiệu lực 15 phút, lưu vào bảng `password_resets` rồi gửi qua email. Nếu người dùng yêu cầu gửi lại, hệ thống sẽ vô hiệu hóa token cũ ngay khi phát hành token mới.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa & Tải nhận thức:** Bản gốc đột ngột nhắc tới *"Token"* ở câu 2 dù câu 1 chỉ nhắc *"email đặt lại"*, rồi câu 3 lại đổi sang *"Đường dẫn cũ"* — buộc người đọc tự đoán *"email = đường dẫn = token"*. Bản cải thiện nối chuỗi Cũ→Mới theo đúng trình tự thời gian của `token` (tạo → lưu → gửi → vô hiệu hóa).
7. **Trường hợp ngoại lệ:** Bảng tóm tắt hoặc danh sách liệt kê các mục ngang hàng không phụ thuộc trình tự thời gian.

---

### `P-04`: Lặp diễn giải không tăng thông tin

1. **Định nghĩa:** Diễn đạt lại cùng một ý bằng từ ngữ khác trong hai câu liền kề hoặc thêm đoạn tóm tắt cuối bài lặp nguyên những gì vừa nói ở đoạn ngắn ngay phía trên.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Vi phạm Phương châm Lượng (Grice, 1975) và tạo **Redundancy Effect** (Sweller et al., 2011).
   - `[Suy luận]` Thiên lệch mẫu bài văn/bài báo dài trong huấn luyện LLM (và thưởng độ dài trong RLHF — tương đồng *Verbosity Bias* mà Zheng et al., 2023 ghi nhận).
3. **Dấu hiệu nhận biết:** Câu trước nói *"API trả về lỗi 429 khi vượt quá 100 request/phút"*, câu sau viết *"Nói cách khác, hệ thống sẽ giới hạn lưu lượng nếu tần suất gọi vượt ngưỡng cho phép"* mà không thêm hướng dẫn xử lý; hoặc kết thúc bằng *"Tóm lại, việc áp dụng giải pháp này sẽ giúp..."*.
4. **Ví dụ không đạt:**
   > Không nên lưu mật khẩu dạng văn bản thuần (plaintext) trong cơ sở dữ liệu vì nếu dữ liệu bị rò rỉ, kẻ tấn công sẽ đọc được ngay. Nói một cách đơn giản, việc lưu mật khẩu thô tiềm ẩn rủi ro bảo mật rất lớn khi xảy ra sự cố lộ dữ liệu. Thay vào đó, hãy băm mật khẩu bằng bcrypt hoặc Argon2.
5. **Ví dụ đã cải thiện:**
   > Không lưu mật khẩu dạng plaintext trong cơ sở dữ liệu vì kẻ tấn công có thể đọc trực tiếp nếu dữ liệu bị lộ. Hãy băm mật khẩu bằng `bcrypt` hoặc `Argon2` trước khi lưu.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Lượng thông tin & Tải nhận thức:** Câu giữa trong bản không đạt lặp 100% mệnh đề của câu 1 (*plaintext + rò rỉ = nguy hiểm*). Cắt câu lặp giảm ~40% số chữ mà không mất bất kỳ cảnh báo bảo mật hay giải pháp kỹ thuật nào.
7. **Trường hợp ngoại lệ:** Tài liệu đào tạo khái niệm mới rất trừu tượng cho người mới, nơi câu thứ hai đưa **ví dụ cụ thể** minh họa cho định nghĩa vừa nêu (ví dụ bổ sung tình huống mới, không phải lặp lời).

---

## Cấp độ 3: Cấp độ Tài liệu (`D-01` – `D-04`)

### `D-01`: Trộn lẫn chế độ tài liệu

1. **Định nghĩa:** Nhồi nhiều mục đích trái ngược vào cùng một đoạn/mục tài liệu (ví dụ: đang viết hướng dẫn thao tác từng bước lại chèn đoạn giảng lý thuyết kiến trúc dài; hoặc đang viết đặc tả API/BRD lại chen văn phong quảng bá thuyết phục).
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Framework **Diátaxis** (Procida) chỉ ra 4 chế độ (*Tutorial, How-to, Reference, Explanation*) phục vụ 4 trạng thái nhận thức khác nhau; trộn lẫn chế độ làm hỏng cả khả năng tra cứu lẫn học tập.
3. **Dấu hiệu nhận biết:** Bảng API Spec xen giữa mô tả ưu điểm sản phẩm; tài liệu How-to khắc phục sự cố bắt đầu bằng 3 đoạn lịch sử/định nghĩa công nghệ.
4. **Ví dụ không đạt:**
   > ### Hướng dẫn xoay vòng (rotate) API Key
   > Bảo mật API là trụ cột sống còn giúp bảo vệ tài sản số của doanh nghiệp trước các mối đe dọa mạng ngày càng tinh vi. Hệ thống của chúng tôi sử dụng chuẩn mã hóa hiện đại để cấp phát khóa truy cập. Để tạo key mới, bạn vào **Cài đặt → Bảo mật**, chọn **Tạo Key Mới**. Lưu ý key cũ sẽ hết hạn sau 24 giờ.
5. **Ví dụ đã cải thiện:**
   > ### Xoay vòng (rotate) API Key
   > **Lưu ý trước khi làm:** Key cũ tự động hết hạn sau **24 giờ** kể từ lúc bạn tạo key mới — hãy cập nhật key mới lên các dịch vụ đang chạy trong khoảng thời gian này.
   > 1. Vào **Cài đặt → Bảo mật**.
   > 2. Chọn **Tạo Key Mới** và sao chép ngay giá trị hiển thị (chỉ hiện một lần).
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa & Tải nhận thức:** Người mở hướng dẫn rotate key đang có mục tiêu thực hiện thao tác (*How-to*). Hai câu rao giảng về "trụ cột sống còn" làm tăng *Extraneous Load* và trì hoãn việc nhìn thấy cảnh báo quan trọng.
7. **Trường hợp ngoại lệ:** Tài liệu tổng hợp ngắn (như email thông báo thay đổi cho sếp hoặc đồng đội) đôi khi cần 1 câu ngữ cảnh *"Tại sao thay đổi"* ngay trước *"Cần làm gì"*, nhưng hai phần phải phân tách rõ ràng.

---

### `D-02`: Trình tự thông tin ngược quy trình tiếp nhận

1. **Định nghĩa:** Đặt điều kiện tiên quyết, cảnh báo không thể hoàn tác, ràng buộc ngoại lệ hoặc kết luận quan trọng ở cuối văn bản thay vì đặt trước bước thực hiện hoặc ở phần mở đầu.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Schriver (1997) và Sweller et al. (2011) chỉ ra người đọc thao tác theo trình tự từ trên xuống; nếu cảnh báo hoặc điều kiện nằm cuối mục, người đọc thường làm xong (hoặc hiểu xong sai giả định) mới thấy điều kiện loại trừ.
3. **Dấu hiệu nhận biết:** Câu *"Lưu ý: Thao tác này sẽ xóa toàn bộ dữ liệu cũ và không áp dụng cho tài khoản dùng thử"* đặt ở dòng cuối cùng sau 5 bước hướng dẫn bấm nút.
4. **Ví dụ không đạt:**
   > Để gộp hai tài khoản khách hàng:
   > 1. Mở hồ sơ khách hàng đích.
   > 2. Chọn **Gộp tài khoản** và nhập ID tài khoản nguồn.
   > 3. Bấm **Xác nhận**.
   > Lưu ý: Không thể hoàn tác sau khi gộp, và hai tài khoản phải trùng số điện thoại đã xác thực.
5. **Ví dụ đã cải thiện:**
   > ### Gộp hai tài khoản khách hàng
   > **Điều kiện & Cảnh báo:** Hai tài khoản phải trùng số điện thoại đã xác thực. Thao tác này **không thể hoàn tác** sau khi xác nhận.
   > 1. Mở hồ sơ khách hàng đích.
   > 2. Chọn **Gộp tài khoản** và nhập ID tài khoản nguồn.
   > 3. Kiểm tra lại dữ liệu hiển thị rồi bấm **Xác nhận**.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Tải nhận thức & An toàn thao tác:** Đưa điều kiện tiên quyết và cảnh báo không thể hoàn tác lên trước giúp người đọc lọc ngay xem mình có đủ điều kiện không, tránh phải hủy bỏ hoặc sửa hậu quả sau khi đã đi qua 3 bước.
7. **Trường hợp ngoại lệ:** Các chi tiết ngoại lệ hiếm gặp của một bước cụ thể có thể đặt ngay tại bước đó (inline) thay vì dồn hết lên đầu để tránh làm rối mục tổng quan.

---

### `D-03`: Thiếu ngữ cảnh, phạm vi áp dụng hoặc giả định đầu vào

1. **Định nghĩa:** Đưa ra quy tắc, chỉ số, giải pháp hoặc đoạn mã nhưng không nói rõ áp dụng cho môi trường nào, phiên bản nào, vai trò nào hay giả định đầu vào là gì.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Thiếu tính **Complete** (ISO/IEC/IEEE 29148) và **Relevance** (ISO 24495-1:2023); người đọc không biết thông tin đó có dùng được cho bối cảnh của mình không.
3. **Dấu hiệu nhận biết:** Nêu *"Phí phạt là 2%"* mà không rõ 2% trên giá trị đơn hay giá trị phần trễ hạn, hay tính từ ngày thứ mấy; hoặc đề xuất phương án kiến trúc mà không nêu quy mô tải/ràng buộc giả định.
4. **Ví dụ không đạt:**
   > Khi khách hàng hủy đơn, hệ thống sẽ hoàn 80% số tiền và giữ lại 20% phí xử lý.
5. **Ví dụ đã cải thiện:**
   > **Phạm vi áp dụng:** Đơn hàng dịch vụ đặt trước đã thanh toán.
   > - Hủy **trước giờ hẹn ≥ 24 giờ**: hoàn **100%** số tiền.
   > - Hủy **trong vòng < 24 giờ** trước giờ hẹn: hoàn **80%** số tiền, giữ lại **20%** phí xử lý (tối thiểu theo quy định gói dịch vụ nếu có).
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa:** Quy tắc thiếu điều kiện thời điểm khiến đội vận hành và lập trình áp dụng sai cho trường hợp hủy sớm hoặc đơn chưa thanh toán. Bản cải thiện neo rõ phạm vi áp dụng và điều kiện kích hoạt từng mức.
7. **Trường hợp ngoại lệ:** Trong hội thoại nhiều lượt mà hai bên vừa chốt xong phạm vi ở tin nhắn ngay trước đó, không cần lặp lại toàn bộ phần phạm vi ở mỗi câu trả lời kế tiếp.

---

### `D-04`: Lệch cấu trúc trình bày

1. **Định nghĩa:** Chọn sai hình thức trình bày dữ liệu: (a) viết đoạn văn đặc quánh ("bức tường chữ") cho nhiều điều kiện rẽ nhánh, thông số so sánh hoặc quy trình nhiều bước; HOẶC (b) lạm dụng heading, bullet point, icon và bảng biểu cho hội thoại ngắn chỉ có 1–2 ý đơn giản.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` **Information Mapping** (Horn) và Schriver (1997) khuyến nghị chọn cấu trúc theo chức năng quét đọc. Ngược lại, trong RLHF, LLM hay bị thưởng vì định dạng "trình bày đẹp bằng nhiều bullet và heading", dẫn đến băm nhỏ một câu trả lời trò chuyện bình thường thành báo cáo.
3. **Dấu hiệu nhận biết:** (a) Một đoạn văn 8 dòng chứa 5 trạng thái mã lỗi và thời gian retry; hoặc (b) Câu hỏi chat *"Git rebase khác gì Git merge nói ngắn gọn giúp mình?"* bị chia thành 6 heading, bảng 4 cột và phần "Kết luận tổng quan".
4. **Ví dụ không đạt (lệch kiểu b — over-formatting trong hội thoại):**
   > ### 1. Tổng quan về việc sử dụng `git pull --rebase`
   > Trong quy trình phát triển phần mềm hiện đại, việc đồng bộ mã nguồn đóng vai trò rất quan trọng...
   > ### 2. Lợi ích chính
   > - **Lịch sử sạch sẽ:** ...
   > - **Tránh commit thừa:** ...
   > ### 3. Lưu ý quan trọng
   > - **Không rebase nhánh chung:** ...
5. **Ví dụ đã cải thiện:**
   > Dùng `git pull --rebase` để giữ lịch sử commit thành một đường thẳng sạch sẽ, tránh tạo các merge commit thừa mỗi lần kéo code mới về. Chỉ cần nhớ một nguyên tắc: chỉ rebase trên nhánh cá nhân của bạn, không rebase trên nhánh đang dùng chung như `main` hay `develop`.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Tải nhận thức:** Trong hội thoại nhanh, việc phải nhảy mắt qua 3 tiêu đề lớn và 5 gạch đầu dòng cho một câu trả lời gói gọn trong 2 câu văn xuôi mạch lạc lại tạo *Split-Attention* và cảm giác nặng nề không cần thiết. Ngược lại, khi so sánh ≥ 3 đối tượng trên ≥ 3 thuộc tính thì bảng biểu lại giúp giảm tải nhận thức vượt trội so với văn xuôi.
7. **Trường hợp ngoại lệ:** Khi người dùng yêu cầu rõ định dạng đầu ra (ví dụ *"Lập bảng so sánh..."* hoặc *"Viết dưới dạng đoạn văn liên tục"*).

---

## Cấp độ 4: Cấp độ Người đọc (`R-01` – `R-04`)

### `R-01`: Lệch trình độ người đọc (Expertise Reversal / Thiếu nền tảng)

1. **Định nghĩa:** (a) Giải thích dài dòng các khái niệm sơ đẳng cho chuyên gia cùng lĩnh vực (*Expertise Reversal*), hoặc (b) ném thuật ngữ và bước nhảy logic không giải thích cho người mới/người ngoài chuyên ngành.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` **Expertise Reversal Effect** (Kalyuga, 2007) và **Reverse Cohesion Effect** (McNamara et al., 1996) chứng minh cùng một mức độ chi tiết sẽ hỗ trợ người mới nhưng làm chậm và gây quá tải ngoại lai cho chuyên gia.
3. **Dấu hiệu nhận biết:** Trả lời kỹ sư backend đang hỏi lỗi deadlock bằng đoạn giải thích *"Database là nơi lưu trữ dữ liệu quan trọng..."*; hoặc viết hướng dẫn cho nhân viên CSKH toàn các mã HTTP status và tên bảng SQL thô.
4. **Ví dụ không đạt (gửi cho Senior Backend Engineer đang điều tra lỗi timeout):**
   > API (Application Programming Interface) là cầu nối giúp các phần mềm giao tiếp với nhau. Khi bạn gửi một yêu cầu qua mạng internet, máy chủ cần thời gian để xử lý và phản hồi lại. Nếu kết nối cơ sở dữ liệu bị tắc nghẽn do quá nhiều truy vấn đồng thời, hệ thống có thể bị timeout.
5. **Ví dụ đã cải thiện (gửi cho Senior Backend Engineer):**
   > Khả năng cao pool kết nối DB đang bị cạn (`connection pool exhaustion`) khi tải cao hoặc có query giữ lock quá lâu. Bạn kiểm tra metric active connections trên pool và `pg_stat_activity` xem có transaction nào bị treo ở trạng thái `idle in transaction` không.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa & Lượng thông tin:** Bản không đạt tốn 58 chữ để giải thích lại kiến thức đại cương mà kỹ sư đã tự động hóa trong trí nhớ dài hạn, không đưa được bước chẩn đoán kỹ thuật nào. Bản cải thiện đi thẳng vào giả thuyết gốc và công cụ kiểm tra tương thích với trình độ người đọc.
7. **Trường hợp ngoại lệ:** Tài liệu dùng chung cho nhiều cấp bậc người đọc (ví dụ Onboarding Handbook): đặt phần tóm tắt điều hành/checklist thao tác nhanh lên trước cho người đã biết, và gom phần giải thích khái niệm nền vào mục phụ hoặc chú thích riêng.

---

### `R-02`: Lệch thanh điệu & ngữ cảnh sử dụng

1. **Định nghĩa:** Dùng văn phong không phù hợp với mối quan hệ giao tiếp và mục đích sử dụng (ví dụ: biến câu trả lời chat bình thường thành văn bản hành chính/công văn, hoặc viết báo cáo lãnh đạo/tài liệu đặc tả chính thức theo lối khẩu ngữ suồng sã, thiếu chuẩn mực).
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Đỗ Hữu Châu nhấn mạnh ngữ dụng tiếng Việt đòi hỏi điều chỉnh cách xưng hô, từ vựng và mức trang trọng theo vai giao tiếp và tình huống.
   - `[Giả thuyết]` LLM không có cơ chế phân loại ngữ cảnh trước khi viết nên thường co về một giọng "thư ký hành chính trang trọng" trung bình cho mọi prompt tiếng Việt.
3. **Dấu hiệu nhận biết:** Dùng *"Kính gửi"*, *"nhằm mục đích"*, *"quý người dùng"* trong tin nhắn chat kỹ thuật hằng ngày; hoặc dùng *"mấy ông dev"*, *"xong xuôi hết trơn"* trong PRD/SAD chính thức.
4. **Ví dụ không đạt (chat hằng ngày giữa người dùng và AI):**
   > Dựa trên thông tin bạn đã cung cấp, tôi xin phép được trình bày các bước xử lý sự cố như sau để bạn có thể tham khảo và thực hiện một cách hiệu quả nhất.
5. **Ví dụ đã cải thiện:**
   > Bạn thử xử lý theo 3 bước này nhé:
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ dụng & Tải nhận thức:** Câu mở đầu hành chính 33 chữ không mang lại thông tin mới nào ngoài việc báo hiệu sắp liệt kê các bước. Bản cải thiện 8 chữ tạo giao tiếp tự nhiên, thân thiện và đưa người đọc thẳng vào bước 1.
7. **Trường hợp ngoại lệ:** Email gửi đối tác/khách hàng ngoài công ty hoặc văn bản pháp quy — khi đó sự lịch sự trang trọng chuẩn mực là yêu cầu bắt buộc của ngữ cảnh.

---

### `R-03`: Thiếu tính khả dụng hành động hoặc tính kiểm chứng

1. **Định nghĩa:** Văn bản nhằm mục đích hướng dẫn công việc, đặc tả kiểm thử hoặc đề xuất quyết định nhưng trình bày mơ hồ ở mức khái niệm, khiến người đọc hiểu đại ý nhưng không biết bước tiếp theo phải làm gì hoặc QA không viết được test case.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Bằng chứng]` Vi phạm trụ cột **Usability** (ISO 24495-1:2023) và thuộc tính **Verifiable** (ISO/IEC/IEEE 29148).
3. **Dấu hiệu nhận biết:** Acceptance Criteria viết *"Hệ thống hiển thị thông báo phù hợp khi nhập sai"*; hoặc đề xuất giải pháp viết *"Cần rà soát lại quy trình phê duyệt để nhanh hơn"* mà không nói rõ ai bỏ bước nào, ngưỡng SLA là bao lâu.
4. **Ví dụ không đạt (Acceptance Criteria):**
   > Khi người dùng nhập mật khẩu sai nhiều lần, hệ thống phải xử lý bảo mật phù hợp và thông báo cho người dùng biết.
5. **Ví dụ đã cải thiện (Acceptance Criteria):**
   > - Nếu người dùng nhập sai mật khẩu **5 lần liên tiếp trong vòng 15 phút**, hệ thống khóa chức năng đăng nhập của tài khoản đó trong **15 phút**.
   > - Tại lần nhập sai thứ 5, hiển thị thông báo: *"Tài khoản tạm khóa 15 phút do nhập sai quá 5 lần. Vui lòng thử lại sau hoặc dùng chức năng Quên mật khẩu."*
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa & Khả dụng:** Cụm *"nhiều lần"* và *"xử lý bảo mật phù hợp"* không kiểm thử được. Bản cải thiện cung cấp đầy đủ ngưỡng định lượng (5 lần, 15 phút) và hành vi đầu ra cụ thể, giúp Dev và QA triển khai ngay mà không phải mở cuộc họp hỏi lại BA.
7. **Trường hợp ngoại lệ:** Tài liệu giải thích khái niệm (*Explanation*) hoặc hội thoại trao đổi ý tưởng ban đầu ở giai đoạn khám phá — khi mục tiêu không phải hướng dẫn thao tác hay chốt đặc tả (xem chỉ báo `actionability_applicable` trong Evaluation Framework).

---

### `R-04`: Đơn giản hóa làm sai lệch hoặc rơi điều kiện quan trọng

1. **Định nghĩa:** Trong nỗ lực viết ngắn hoặc làm cho "dễ đọc", AI hoặc người biên tập cắt bỏ điều kiện biên, ngoại lệ, giá trị bắt buộc hoặc làm lệch mức độ bắt buộc (*phải* thành *có thể*, *tất cả* thành *một số*), gây hiểu nhầm nghiêm trọng.
2. **Nguyên nhân / Giả thuyết nguyên nhân:**
   - `[Suy luận]` Xảy ra khi áp dụng máy móc mục tiêu "viết ngắn lại" hoặc "viết đơn giản đi" mà không có bước đối chiếu bảo toàn mệnh đề gốc (*Textbase preservation*, Kintsch).
3. **Dấu hiệu nhận biết:** Văn bản đầu ra ngắn và trôi chảy hơn bản gốc, nhưng mất điều kiện *"ngoại trừ..."*, đổi số liệu/đơn vị, làm nhòe ranh giới bắt buộc vs tùy chọn, hoặc tự thêm giả định mới không có trong nguồn.
4. **Ví dụ không đạt (tóm tắt/viết lại một Business Rule):**
   > *Gốc:* Khách hàng hạng Vàng được miễn phí giao hàng cho đơn từ 300.000đ trở lên, ngoại trừ đơn hàng cồng kềnh trên 15 kg hoặc giao hỏa tốc trong 2 giờ.
   > *Viết lại sai (quá đơn giản):* Khách hàng hạng Vàng đặt đơn từ 300.000đ sẽ được miễn phí giao hàng.
5. **Ví dụ đã cải thiện:**
   > Khách hàng hạng Vàng được miễn phí giao hàng cho đơn từ **300.000đ**, trừ hai trường hợp: hàng cồng kềnh **trên 15 kg** hoặc chọn **giao hỏa tốc 2 giờ**.
6. **Giải thích cụ thể về ngữ nghĩa, lượng thông tin và tải nhận thức:**
   - **Ngữ nghĩa:** Bản viết lại đầu tiên ngắn và mượt hơn hẳn, nhưng tạo ra **sai lệch nghiệp vụ nghiêm trọng** (mất 2 điều kiện loại trừ, gây thiệt hại chi phí vận chuyển nếu áp dụng thật). Bản cải thiện chứng minh có thể viết gọn, dễ quét mà vẫn giữ nguyên 100% điều kiện loại trừ.
7. **Trường hợp ngoại lệ:** Không có ngoại lệ đối với lỗi làm sai dữ kiện/điều kiện; nếu văn bản tóm tắt bắt buộc phải rút gọn ở mức tiêu đề, phải gắn cờ báo rõ còn điều kiện chi tiết kèm theo chứ không được phát biểu như quy tắc toàn phần.
