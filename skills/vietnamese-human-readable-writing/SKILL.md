---
name: vietnamese-human-readable-writing
description: >-
  Use when writing, explaining, analyzing, chatting, communicating at work,
  drafting business or technical specifications (PRD, BRD, User Story, AC,
  IDD, SAD, API Spec), writing guides/reports, or editing AI-generated or
  machine-translated Vietnamese prose for human comprehension and practical use.
---

# Viết Tiếng Việt Rõ Nghĩa và Khả Dụng (Vietnamese Human-Readable Writing)

**Nguyên lý cốt lõi:** Truyền tải thông tin bằng tiếng Việt sao cho người đọc mục tiêu **hiểu đúng ngay ở lần đọc đầu** và **dùng được ngay vào công việc**, không phải tự suy đoán câu văn mơ hồ. Giảm công sức đọc hiểu của con người thông qua rõ nghĩa, đúng trình tự và đúng ngữ cảnh — không đánh đồng với việc viết cụt hay bỏ thuật ngữ cần thiết.

---

## 1. Phân loại Chế độ Xử lý (Context Triage)

Xác định chế độ trước khi viết để tiết kiệm thời gian và token:

| Chế độ | Khi nào áp dụng | Đọc thêm Reference? | Định dạng đầu ra mặc định |
|---|---|---|---|
| **Nhẹ** | Hội thoại hằng ngày, hỏi đáp ngắn, tin nhắn Slack/Teams ngắn | **Không** (chỉ dùng file này) | Văn xuôi tự nhiên 2–6 câu, hoặc tối đa 3 gạch đầu dòng ngắn gọn. |
| **Trung bình** | Giải thích khái niệm, phân tích vấn đề, email công việc, báo cáo, hướng dẫn/đào tạo, biên tập văn bản | Đọc **1 file** phù hợp ở Mục 5 nếu cần cấu trúc sâu hoặc gỡ văn dịch | Đi thẳng kết luận trước (BLUF), phân đoạn gọn vừa đủ theo mức người đọc. |
| **Chặt** | Tài liệu nghiệp vụ (`PRD, BRD, User Story, AC, Business Rule`) hoặc kỹ thuật (`IDD, SAD, API Spec, System Design`) | **Bắt buộc đọc 1 file** chuyên sâu ở Mục 5 trước khi viết | Cấu trúc chuẩn đặc tả: tách rõ phạm vi, quy tắc đơn nghĩa, điều kiện biên và giả định mở. |

---

## 2. Bất biến Bảo toàn Nội dung (Không Thỏa hiệp)

1. **Giữ nguyên 100% sự thật và điều kiện nguồn:** Không làm sai lệch ý nghĩa, con số, đơn vị, mốc thời gian, tên API/biến/trạng thái, định danh hệ thống hay điều kiện loại trừ.
2. **Không tự bịa chi tiết chưa có căn cứ:** Không tự thêm số liệu đo đạc, quy định nghiệp vụ hay trường JSON/mã lỗi mới như sự thật đã chốt. Nếu tài liệu đặc tả hoặc phân tích cần gợi ý phần còn thiếu để hoàn chỉnh, **tách riêng rõ ràng** bằng nhãn `Đề xuất bổ sung (cần xác nhận)` hoặc `Ví dụ minh họa`.
3. **Khóa chặt logic nghiệp vụ:** Giữ đúng toán tử `và` / `hoặc`, mức bắt buộc (`phải` vs `nên` vs `có thể`), ngưỡng biên (`<` vs `<=`, `>` vs `>=`).
4. **Không cắt điều kiện để chạy theo sự ngắn gọn:** Mọi ngoại lệ, giới hạn và cảnh báo an toàn trong đầu vào đều phải giữ lại đủ.

---

## 3. Quy trình Tư duy 9 Bước

*(Ở chế độ **Nhẹ**, thực hiện ngầm nhanh các bước 1–8 trong đầu. Ở chế độ **Trung bình / Chặt**, rà kỹ đủ cả 9 bước. **Tuyệt đối không** in tên các bước hoặc lời tự kiểm tra này ra câu trả lời cuối cùng.)*

1. **Xác định mục đích:** Người đọc cần gì — nắm nhanh ý chính, hiểu bản chất, ra quyết định, làm theo từng bước, hay code/test chính xác?
2. **Xác định đối tượng & trình độ:** Người mới, nhân sự vận hành/PM, hay kỹ sư giàu kinh nghiệm? Khớp mức giải thích với nền tảng của họ: người mới cần cầu nối khái niệm và ví dụ đời thực; chuyên gia cần đi thẳng vào cơ chế, đánh đổi và công cụ kiểm tra (bỏ kiến thức sơ đẳng).
3. **Chốt thông tin cốt lõi & bất biến:** Liệt kê ngầm mọi dữ kiện, con số, điều kiện biên và ngoại lệ bắt buộc giữ nguyên.
4. **Tổ chức trình tự thuận tiếp nhận:**
   - Đưa câu trả lời, kết luận hoặc đề xuất lên đầu (**BLUF / Pyramid**).
   - Đặt **phạm vi áp dụng, điều kiện tiên quyết và cảnh báo rủi ro** lên *trước* các bước thực hiện.
   - Tách bạch **Khái niệm (Giải thích)** — **Thao tác (How-to)** — **Đặc tả (Reference)**, không trộn lẫn.
5. **Chọn khung trình bày & thanh điệu hợp ngữ cảnh:**
   - Chat ngắn / giải thích 1–2 ý: văn xuôi liền mạch, giọng tự nhiên như đồng nghiệp trao đổi.
   - Nhắn tin Slack/Teams công việc: đi thẳng sự kiện, tác động, việc đã làm, mốc kế tiếp.
   - Email công việc: tiêu đề rõ việc, mở bài 1 câu vào ngay mục đích, tránh sáo ngữ khách sáo kéo dài.
   - So sánh ≥ 3 mục trên ≥ 3 tiêu chí hoặc nhiều điều kiện rẽ nhánh: dùng bảng hoặc danh sách đánh số để giảm tải mắt quét.
6. **Diễn đạt rõ nghĩa ở cấp câu:**
   - Chọn cấu trúc **Đề–Thuyết** tự nhiên: đặt phạm vi/tình huống hoặc tác thể hành động làm Đề, nêu hành động/kết quả trực tiếp bằng động từ chính ở phần Thuyết.
   - Gỡ bỏ danh từ hóa rỗng nhiều lớp (*"cung cấp năng lực xử lý"*, *"hỗ trợ việc phân bổ"*, *"tiến hành thực hiện quá trình"*).
   - Thay câu bị động dịch sát (*"được ... bởi"*) bằng câu chủ động hoặc *"được/bị"* đúng sắc thái lợi/hại.
   - Triệt tiêu mơ hồ `và/hoặc`, mơ hồ quy chiếu (*"nó", "điều này"* sau câu nhiều vế), và tính từ mơ hồ (*"nhiều lần", "phù hợp", "nhanh"* khi đề bài đã cho ngưỡng cụ thể).
7. **Loại bỏ dư thừa, tăng mật độ thông tin:**
   - Cắt câu mở bài rào đón hiển nhiên (*"Trong bối cảnh hiện nay..."*, *"X đóng vai trò then chốt..."*).
   - Cắt câu lặp diễn giải (*"Nói cách khác..."* lặp lại nguyên mệnh đề vừa nêu) và đoạn kết tóm tắt sáo rỗng khi nội dung phía trên đã ngắn gọn.
   - Cắt mỹ từ không mang dữ kiện (*"vượt trội", "toàn diện", "tối ưu hóa tối đa"*).
8. **Kiểm tra chéo độ chính xác & tính khả dụng:**
   - So lại từng ý trong Mục 2 và Bước 3: còn sót ngoại lệ, lệch biên `< / <=`, sai đơn vị hay lẫn dữ kiện đề bài với phần gợi ý không?
   - Nếu mục đích là giao việc, hướng dẫn hay đặc tả: người đọc đã biết rõ *ai làm gì, trong điều kiện nào, khi nào xong/lỗi* chưa?
9. **Hoàn thiện đầu ra:** Xuất trực tiếp nội dung sạch cho người đọc.

---

## 4. Ranh giới Chống Máy móc

- **Không cấm từ máy móc:** Chỉ gỡ *"việc, sự, quá trình, được, bị"* khi chúng làm rỗng hành động hoặc dịch sát cú pháp tiếng Anh; giữ lại khi dùng làm Đề ngữ tự nhiên (*"Việc tách thanh toán chỉ áp dụng cho..."*) hoặc đúng sắc thái lợi/bất lợi (*"Đơn bị hủy do quá hạn"*).
- **Không ép mọi câu phải ngắn:** Giữ câu đủ ý khi cần giữ quan hệ nhân–quả hoặc điều kiện; tách câu hoặc tách gạch đầu dòng khi có nhiều điều kiện lồng nhau dễ hiểu nhầm phạm vi.
- **Không dịch cưỡng ép thuật ngữ kỹ thuật:** Giữ nguyên thuật ngữ chuyên môn quen dùng trong ngành tại Việt Nam (`API, webhook, idempotency_key, timeout, rollback, cache, index...`), giữ đồng nhất 1 tên gọi cho 1 thực thể; chỉ chú thích ngắn khi đối tượng đọc không chuyên.
- **Không ép định dạng hàng loạt:** Với hội thoại chat ngắn hoặc đoạn văn mô tả 1–2 ý đơn giản, giữ nguyên văn xuôi liền mạch — không chẻ thành `### Heading`, gạch ngang `---`, câu dẫn đệm hay gạch đầu dòng lặp lại nhãn in đậm. Ngược lại, với email thông báo vận hành (thời gian, tác động, việc cần làm) hoặc quy tắc nhiều điều kiện, tách dòng ngắn gọn để đọc quét nhanh.
- **Không lặp giữa bảng và chữ:** Khi bảng biểu đã trình bày đủ thông số/so sánh, không viết lại nguyên các ý đó bằng đoạn văn hoặc bullet ngay bên dưới.
- **Không tự ý mở rộng phạm vi:** Chỉ trả lời đúng điều người dùng cần; không đính kèm hướng dẫn thư viện phụ hay kiến trúc mở rộng khi không được hỏi.
- **Không đánh đổi đầy đủ lấy ngắn gọn:** Giữ nguyên mọi điều kiện biên và ngoại lệ.

---

## 5. Tài liệu Tham chiếu Chuyên sâu (Progressive Disclosure)

Chỉ dùng `read_file` mở đúng **1 file** khi tác vụ nằm ở chế độ **Trung bình** hoặc **Chặt**:

| Nhu cầu cụ thể | Đọc file tham chiếu |
|---|---|
| Gỡ câu dịch sát tiếng Anh, danh từ hóa rỗng, mơ hồ logic/quy chiếu, hoặc biên tập lại văn bản có sẵn | [vietnamese-clarity-and-style.md](./references/vietnamese-clarity-and-style.md) |
| Tổ chức bố cục phân tích/báo cáo/hướng dẫn/email, chống vòng vo mở bài, điều chỉnh cho chuyên gia vs người mới | [information-architecture.md](./references/information-architecture.md) |
| Viết **PRD, BRD, User Story, Acceptance Criteria, Business Rule** | [business-specs.md](./references/business-specs.md) |
| Viết **IDD, SAD, API Specification, System Design, Technical Spec, Runbook kỹ thuật** | [technical-specs.md](./references/technical-specs.md) |
