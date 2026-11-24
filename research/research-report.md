# Báo cáo Nghiên cứu Cơ sở: Viết Tiếng Việt Rõ Nghĩa và Khả Dụng cho AI

## Tóm tắt Điều hành (BLUF)

**Vì sao văn bản tiếng Việt của AI đúng ngữ pháp nhưng khó hiểu?** Có 3 nguyên nhân gốc:
1. **Cú pháp lai tiếng Anh (*Translationese* & *Âu hóa*):** Quá trình tiền huấn luyện đa ngôn ngữ và tinh chỉnh có giám sát (SFT) khiến LLM thường tư duy theo khung Chủ–Vị và danh từ hóa tiếng Anh rồi ánh xạ từng phần sang tiếng Việt (`[Bằng chứng]`, Li et al., 2025; Cao Xuân Hạo, 1991).
2. **Mơ hồ ngữ nghĩa và tăng tải nhận thức ngoại lai:** AI ưa dùng danh từ trừu tượng, ẩn tác thể hành động, nối câu bằng liên từ rỗng nghĩa và chôn điều kiện cốt lõi vào giữa đoạn văn dài. Người đọc phải giải mã nhiều lớp trước khi dựng được bức tranh tình huống thực tế (`[Bằng chứng]`/`[Suy luận]`, Sweller et al., 2011; Kintsch, 1998; Berry et al., 2003).
3. **Thiếu mô hình người đọc và ngữ cảnh:** AI áp dụng một giọng văn trung bình cho mọi tình huống—làm hội thoại đời thường trở nên hành chính hóa, hoặc làm đặc tả kỹ thuật mất độ sắc nét cần thiết cho chuyên gia (`[Bằng chứng]`, Kalyuga, 2007; McNamara et al., 1996).

**Quy tắc nhận thức luận trong báo cáo:** Mọi kết luận được gắn nhãn rõ:
- `[Bằng chứng]`: Có nghiên cứu công bố, tiêu chuẩn chính thức hoặc dữ liệu thực nghiệm trực tiếp.
- `[Suy luận]`: Rút ra trực tiếp bằng lập luận logic từ nhiều kết quả đã chứng minh.
- `[Giả thuyết]`: Đề xuất thiết kế hợp lý nhưng cần kiểm chứng thực nghiệm trên dữ liệu dự án (và kiểm thử với người đọc thật ở các bước sau).

---

## 1. Tổng hợp Nghiên cứu 11 Lĩnh vực

### 1.1 Ngữ pháp, Ngữ nghĩa và Ngữ dụng học Tiếng Việt
- **Cấu trúc Đề–Thuyết (Topic–Comment):** `[Bằng chứng]` Cao Xuân Hạo (1991) chỉ ra tiếng Việt là ngôn ngữ đơn lập, phân tích tính, không biến hình; cấu trúc cú pháp cơ bản gắn liền với khung **Đề** (phạm vi, đối tượng, thời gian, điều kiện đang nói tới) và **Thuyết** (thông tin mới nhận xét/tác động về cái Đề đó), thay vì buộc phải có sự tương hợp hình thái Chủ–Vị kiểu Ấn–Âu.
- **Thể bị động và danh từ hóa:** `[Bằng chứng]` Cao Xuân Hạo (1991) và Nguyễn Đức Dân chỉ ra tiếng Việt bản địa không dùng cấu trúc bị động trung tính phổ quát kiểu *to be + V-ed*. Từ *"được"* gắn với sắc thái tích cực/lợi ích, còn *"bị"* gắn với sắc thái tiêu cực/bất lợi; người Việt thường dùng câu chủ động, chủ ngữ phiếm chỉ (*người ta*) hoặc đưa đối tượng chịu tác động lên làm Đề ngữ thay cho kết cấu *"được ... bởi ..."*. Tương tự, việc nhồi *"việc"*, *"sự"*, *"tính"*, *"năng lực"* trước động từ/tính từ để mô phỏng danh từ hóa (*-tion/-ment*) làm câu nặng nề và mất tác thể.
- **Ngữ dụng học và Nguyên tắc cộng tác:** `[Bằng chứng]` Grice (1975) đặt nền móng với Nguyên tắc cộng tác và 4 phương châm (Lượng, Chất, Quan hệ, Cách thức). Tại Việt Nam, Đỗ Hữu Châu và Nguyễn Đức Dân nhấn mạnh phương châm về Lượng và Cách thức trong tiếng Việt chịu chi phối mạnh bởi vai giao tiếp, quan hệ xã hội và sắc thái đánh giá. `[Suy luận]` AI thường vi phạm đồng thời phương châm Lượng (dư thừa lời rào đón, tóm tắt lặp lại) và Cách thức (mơ hồ, vòng vo trước khi vào trọng tâm).

### 1.2 Cách Tổ chức Thông tin trong Văn bản Tiếng Việt
- **Liên kết nội dung (Coherence) vs Liên kết hình thức (Cohesion):** `[Bằng chứng]` Trần Ngọc Thêm (1985) hệ thống hóa 5 phép liên kết bề mặt tiếng Việt (lặp, thay thế, liên tưởng, nối, tỉnh lược) và khẳng định các phương tiện hình thức chỉ là "chất keo" phục vụ mạch lạc nội dung (liên kết chủ đề và liên kết logic). Tiếng Việt tự nhiên có thể đạt mạch lạc cao bằng trật tự logic, lặp chủ đề và tỉnh lược hợp lý mà không cần nhồi từ nối.
- **Cấu trúc diễn ngôn và tiêu điểm cục bộ:** `[Bằng chứng]` Mô hình Centering Theory (Grosz, Joshi & Weinstein, 1995) chứng minh tính mạch lạc giữa hai câu kề nhau phụ thuộc vào việc duy trì tiêu điểm thực thể ổn định trước khi chuyển sang tiêu điểm mới. Ở tầm toàn văn bản, Rhetorical Structure Theory (Mann & Thompson, 1988) tổ chức văn bản theo quan hệ hạt nhân–vệ tinh (Nucleus–Satellite). `[Suy luận]` Kết hợp với cấu trúc Đề–Thuyết của Cao Xuân Hạo, cách viết tự nhiên trong tiếng Việt đặt thông tin đã biết/phạm vi ngữ cảnh ở **Đề**, thông tin mới cốt lõi ở **Thuyết**, rồi dùng chính thông tin mới đó làm Đề cho câu sau (chuỗi *Cũ → Mới*).

### 1.3 Plain Language và Clear Writing
- **Chuyển dịch sang đánh giá dựa trên kết quả người đọc:** `[Bằng chứng]` Tiêu chuẩn quốc tế **ISO 24495-1:2023** định nghĩa ngôn ngữ rõ ràng không phải là "câu ngắn dưới X từ", mà là giao tiếp giúp người đọc mục tiêu dễ dàng **Tìm thấy (Find)**, **Hiểu đúng (Understand)** và **Sử dụng được (Use)** thông tin, dựa trên 4 nguyên tắc: *Relevance, Findability, Understandability, Usability*. Tiêu chuẩn này cũng phân biệt rõ *plain language* (cho người đọc mục tiêu thông thường hoặc chuyên môn) với *easy language* (cho đối tượng gặp khó khăn đọc hiểu nghiêm trọng).
- **Kỹ thuật viết rõ nghĩa cấp câu:** `[Bằng chứng]` Williams & Bizup (*Style: Lessons in Clarity and Grace*) chứng minh câu văn sáng rõ khi tác thể (nhân vật/hệ thống thực hiện) đứng ở vị trí chủ ngữ và hành động chính nằm ở động từ chính, thay vì giấu hành động trong cụm danh từ hóa. `[Suy luận]` Nguyên tắc tác thể–hành động này tương thích rất cao với tiếng Việt vì vị từ tiếng Việt hoạt động độc lập mà không cần hậu tố danh từ hóa.

### 1.4 Controlled Natural Language (CNL) và Giới hạn với Tiếng Việt
- `[Bằng chứng]` Khảo sát ~100 CNL của Tobias Kuhn (2014) cho thấy phần lớn CNL công nghiệp (điển hình là **ASD-STE100**) được thiết kế xoay quanh hình thái và cú pháp tiếng Anh.
- **Vì sao không thể bê nguyên CNL tiếng Anh sang tiếng Việt:** `[Suy luận]`
  1. *Cấm tỉnh lược / bắt buộc lặp đầy đủ:* Trong tiếng Việt (ngôn ngữ *pro-drop* ngữ cảnh cao), ép lặp lại chủ ngữ và đại từ ở mọi mệnh đề làm câu thô cứng, giống văn dịch máy.
  2. *Cấm cụm danh từ ghép (noun stacks):* Tiếng Anh ghép danh từ chuỗi dài gây mơ hồ cấu trúc cây cú pháp, nhưng trong tiếng Việt đơn lập, ghép từ gốc là phương thức chính tạo thuật ngữ chuyên môn.
  3. *Từ điển giới hạn cứng:* Tiếng Việt dùng tiểu từ tình thái, hư từ chỉ thể và ngữ cảnh để phân biệt vai ngữ pháp thay vì biến đổi hình thái; cấm từ máy móc làm nghèo khả năng phân biệt sắc thái điều kiện.
- `[Giả thuyết]` Với tiếng Việt, thay vì áp dụng CNL từ điển đóng, chỉ nên kiểm soát ở mức **đơn nghĩa logic và quy chiếu** cho đặc tả nghiệp vụ/kỹ thuật (từ khóa nghĩa vụ nhất quán, tránh mơ hồ phạm vi điều kiện).

### 1.5 Technical Writing và Information Design
- `[Bằng chứng]` Ba trụ cột thiết kế thông tin hiện đại gồm:
  - **The Pyramid Principle (Barbara Minto):** Trình bày kết luận/câu trả lời cốt lõi trước (BLUF), sau đó mới phân nhánh luận điểm và bằng chứng.
  - **Information Mapping (Robert Horn):** Chia nội dung thành các khối đơn chức năng (*Procedure, Process, Principle, Fact, Concept*) và đặt nhãn rõ để quét nhanh.
  - **Diátaxis (Daniele Procida):** Tách 4 chế độ tài liệu hoàn toàn khác nhau về mục đích người dùng: *Tutorials* (học thực hành), *How-to guides* (giải quyết một việc cụ thể), *Reference* (tra cứu đặc tả/API chính xác), *Explanation* (hiểu bản chất/kiến trúc).
- `[Bằng chứng]` Về tài liệu kỹ thuật/nghiệp vụ, **ISO/IEC/IEEE 29148** đặt chuẩn bắt buộc cho từng yêu cầu: *Unambiguous* (chỉ có 1 cách hiểu), *Verifiable* (kiểm thử được), *Complete* và *Consistent*.
- `[Bằng chứng]` Schriver (1997) và Redish chứng minh trong môi trường làm việc, người đọc dùng tài liệu như công cụ để hoàn thành tác vụ (đọc quét, nhảy cóc theo heading/điều kiện) chứ không đọc tuyến tính như văn chương.

### 1.6 Cognitive Load Theory (CLT)
- `[Bằng chứng]` Theo John Sweller (1988) và Sweller, Ayres & Kalyuga (2011), bộ nhớ làm việc của con người rất hạn chế và phải xử lý 3 loại tải:
  - **Intrinsic Load:** Độ phức tạp vốn có của bản thân nghiệp vụ/kiến trúc (không thể xóa bỏ bằng cách cắt xén sai sự thật, chỉ có thể phân tách thành các khối logic để quản lý).
  - **Extraneous Load:** Tải thừa do diễn đạt vòng vo, trình bày lộn xộn, tách rời giải thích khỏi ví dụ/mã lệnh (*Split-Attention Effect*), hoặc lặp lại nội dung hiển nhiên (*Redundancy Effect*).
  - **Germane Load:** Nỗ lực hữu ích để xây dựng lược đồ hiểu đúng.
- `[Bằng chứng]` **Expertise Reversal Effect (Kalyuga, 2007):** Hướng dẫn từng bước chi tiết và giải thích khái niệm nền giúp ích cho người mới, nhưng khi đưa cho người có chuyên môn, chúng đảo chiều thành *extraneous load* vì chuyên gia phải mất công đối chiếu phần thừa với tri thức sẵn có trong trí nhớ dài hạn.

### 1.7 Reading Comprehension và Readability Tiếng Việt
- `[Bằng chứng]` Mô hình **Construction–Integration (Kintsch, 1988, 1998)** phân biệt 3 tầng hiểu văn bản: *Surface code* (câu chữ bề mặt), *Textbase* (mạng mệnh đề ngữ nghĩa) và *Situation model* (mô hình tinh huống thực tế tích hợp với kiến thức nền). Một câu văn có *Surface code* đúng ngữ pháp nhưng giấu tác thể và điều kiện sẽ buộc người đọc tốn sức suy luận để dựng *Textbase* và *Situation model*.
- `[Bằng chứng]` **Reverse Cohesion Effect (McNamara, Kintsch, Songer & Kintsch, 1996):** Người đọc có kiến thức nền cao đạt mức hiểu sâu (giải quyết tình huống, suy luận bắc cầu) tốt hơn với văn bản ít nhồi liên từ giải thích hiển nhiên; ngược lại, người mới cần liên kết tường minh hơn để không đứt mạch hiểu.
- `[Bằng chứng]` Trong tiếng Việt, nhóm tác giả **Luong, Nguyen & Dinh (2018, 2020)** xây dựng tập dữ liệu **ViRead** và chứng minh công thức readability dựa vào đếm âm tiết kiểu tiếng Anh (như Flesch-Kincaid) không phản ánh đúng độ khó đọc tiếng Việt; cần kết hợp đặc trưng từ vựng, từ loại (POS), cú pháp và ngữ nghĩa (các nghiên cứu sau này kết hợp PhoBERT, ViDeBERTa).
- `[Bằng chứng]` Schriver (1997) và Redish cũng chỉ ra mọi công thức readability bề mặt đều có thể cho điểm cao một văn bản vô nghĩa hoặc thiếu trình tự vì chúng không đo được cấu trúc logic và mục đích người đọc.

### 1.8 Semantic Ambiguity
- `[Bằng chứng]` **Berry, Kamsties & Krieger (2003)** phân loại 5 nguồn mơ hồ chính trong hợp đồng và đặc tả phần mềm:
  1. *Lexical ambiguity* (từ đa nghĩa).
  2. *Syntactic/Structural ambiguity* (bổ ngữ gắn được vào nhiều cụm trước/sau).
  3. *Referential ambiguity* (đại từ *"nó"*, *"việc này"*, *"hệ thống"* không rõ quy chiếu).
  4. *Scope ambiguity* (phạm vi tác động của *"và"*, *"hoặc"*, *"không"*, *"mọi"*, *"tối đa"*).
  5. *Vagueness vs Ambiguity* (mơ hồ biên độ như *"nhanh"*, *"hợp lý"*, *"từng phần"* khi thiếu ngưỡng đo).
- `[Bằng chứng]` Nguy hiểm nhất là **Subconscious Disambiguation** (Berry et al., 2003): mỗi người đọc (BA, Dev, QA) vô thức chọn một nghĩa hợp lý theo kinh nghiệm riêng và *tin chắc mình đã hiểu đúng*, khiến lỗi logic chỉ phát lộ khi triển khai hoặc nghiệm thu.

### 1.9 Discourse Coherence và Cohesion
- `[Bằng chứng]` Tổng hợp từ **Trần Ngọc Thêm (1985)**, **Halliday & Hasan (1976)**, **Mann & Thompson (1988)** và **Grosz, Joshi & Weinstein (1995)**: liên kết bề mặt (từ nối *tuy nhiên, do đó, ngoài ra*) không tự tạo ra mạch lạc. Một đoạn văn do AI sinh thường có mật độ từ nối cao nhưng nhảy chủ đề đột ngột giữa các câu (*Centering break*) hoặc liệt kê ngang hàng các ý không cùng cấp logic (*RST mismatch*).

### 1.10 Multidimensional Quality Metrics (MQM)
- `[Bằng chứng]` **Lommel et al. (2014)** và **Freitag et al. (2021)** chứng minh đánh giá chất lượng văn bản bằng một điểm số chung hoặc cảm tính (*"hay hơn"*, *"mượt hơn"*) không ổn định và không giúp chẩn đoán lỗi. Chuẩn MQM đánh giá dựa trên **gắn nhãn lỗi cụ thể tại vị trí thực tế** theo từng nhóm chiều (*Accuracy, Fluency, Terminology, Style*) kết hợp 3 cấp độ nghiêm trọng (*Minor, Major, Critical*), trong đó lỗi làm sai lệch hoặc làm mất thông tin cốt lõi mang trọng số phạt áp đảo lỗi phong cách.

### 1.11 Phương pháp Đánh giá Chất lượng Nội dung do LLM Tạo ra
- `[Bằng chứng]` **Zheng et al. (2023)** (*Judging LLM-as-a-Judge*) chỉ ra 3 thiên lệch nghiêm trọng khi dùng LLM làm giám khảo: **Position Bias** (thiên vị vị trí A/B), **Verbosity Bias** (chấm điểm cao hơn cho câu trả lời dài dù chứa nội dung thừa) và **Self-Enhancement Bias** (thiên vị văn phong của chính họ model mình).
- `[Bằng chứng]` **Liu et al. (2023)** (*G-Eval*) cho thấy dùng Chain-of-Thought bám sát rubric chi tiết giúp tăng tương quan giữa LLM Judge và đánh giá con người.
- `[Bằng chứng]` Đối với tiếng Việt, **Li et al. (2025)** làm rõ nguyên nhân translationese từ dữ liệu SFT; **SEA-HELM / LINDSEA (Susanto et al., 2025)** nhấn mạnh cần kiểm tra ngữ nghĩa–ngữ dụng bản địa thay vì dịch đối chứng từ tiếng Anh; và **ViDetect (Tran et al., 2024)** chứng minh tồn tại dấu hiệu phân biệt thống kê giữa văn bản tiếng Việt do AI sinh và do người viết trên 6.800 bài luận.

---

## 2. Rà soát Prior Art (Dự án Mã nguồn mở & Thực tiễn Hiện có)

| Dự án / Nguồn mở | Điểm mạnh kế thừa | Hạn chế khi giải quyết bài toán mục tiêu |
|---|---|---|
| **Wikipedia: *Signs of AI writing*** & `blader/humanizer` | Chỉ mặt đặt tên được các mẫu câu rập khuôn của AI (puffery, rule of three, sáo ngữ kết bài) và giữ nguyên dữ kiện khi biên tập. | Xây dựng cho tiếng Anh, tập trung chủ yếu vào *văn phong bề mặt* (surface style); chưa xử lý kiến trúc thông tin, đặc tả nghiệp vụ/kỹ thuật hay ngữ pháp Đề–Thuyết tiếng Việt. |
| `anhnx000/viet-nhu-nguoi` | Đưa nhận diện giọng AI vào tiếng Việt, có script rà soát nhanh bề mặt. | Thiên về bộ lọc dấu hiệu AI và chấm điểm tổng quát; có rủi ro khiến người dùng/AI xóa máy móc cả những cấu trúc cần thiết trong văn bản kỹ thuật hoặc pháp quy. |
| `longhang2004/vietnamese-humanizer` | Tách thành 4 kỹ năng (*humanizer, translationese-cleaner, grammar-checker, style-guide*) và nêu nguyên tắc bảo toàn dữ kiện. | Chưa xây dựng khung đánh giá thực nghiệm mù với đối chứng Held-out, chưa xử lý sâu thiết kế tài liệu kỹ thuật/nghiệp vụ (PRD, API Spec, SAD) và tải nhận thức. |
| `trussary/vietnamese-language-skill` | Nhận diện đúng vấn đề dịch thô trật tự từ tiếng Anh và lỗi quảng cáo quá đà. | Phạm vi thiên về bản địa hóa ngôn ngữ chung, chưa giải quyết bài toán mơ hồ logic nghiệp vụ (Berry et al.) và phân tầng chuyên môn người đọc (Expertise Reversal). |
| `gencharitaci/humanize-skills` | Có phân chế độ theo thể loại (*technical, academic, business, legal*). | Thiết kế đa ngôn ngữ chung (Tiếng Việt ở Tier 2), không khai thác sâu đặc trưng loại hình đơn lập Đề–Thuyết, "được/bị" và danh từ hóa tiếng Việt. |

**Kết luận thiết kế từ Prior Art:** `[Suy luận]` Khoảng trống lớn nhất chưa được giải quyết tốt là kết nối **ngôn ngữ học tiếng Việt bản địa** + **thiết kế thông tin & giảm tải nhận thức** + **độ chính xác đơn nghĩa của tài liệu kỹ thuật/nghiệp vụ** vào một Skill gọn nhẹ không làm chậm hội thoại thường ngày.

---

## 3. Kiểm tra Khả năng Áp dụng của các Phương pháp Phương Tây cho Tiếng Việt

| Phương pháp / Chuẩn gốc | Giả định của bản gốc (tiếng Anh) | Kiểm tra & Điều chỉnh bắt buộc cho Tiếng Việt | Mức độ áp dụng |
|---|---|---|---|
| **ISO 24495-1 (Find–Understand–Use)** | Độc lập ngôn ngữ ở tầng nguyên tắc mục tiêu, nhưng hướng dẫn triển khai thường minh họa bằng cú pháp Anh. | Áp dụng trọn vẹn 4 trụ cột (*Relevance, Findability, Understandability, Usability*) làm kim chỉ nam cho mọi loại văn bản tiếng Việt. | **Cao — Áp dụng trực tiếp** |
| **Williams (Characters as Subjects, Actions as Verbs)** | Dựa trên cấu trúc Chủ–Vị bắt buộc và hậu tố danh từ hóa (*-tion/-ment*). | Trong tiếng Việt, vị từ đứng làm vị ngữ rất tự nhiên nhưng **cũng** cần đặt đúng **Đề** (phạm vi/tác thể đang xét) trước **Thuyết** (hành động/trạng thái). Không ép mọi câu thành Chủ–Vị nếu câu Đề–Thuyết (ví dụ nêu điều kiện/thời điểm/đối tượng chịu tác động ở đầu câu) rõ hơn. | **Cao — Cần bản địa hóa sang Đề–Thuyết** |
| **Chuyển Bị động → Chủ động** | Tiếng Anh dùng *passive* rộng rãi và trung tính; chuyển sang chủ động gần như luôn tốt hơn. | Tiếng Việt dùng *"được"* (lợi ích) và *"bị"* (bất lợi). Lỗi AI không nằm ở bản thân câu bị động, mà ở việc dịch *is/was V-ed* thành *"được/bị... bởi"* trong câu mô tả hệ thống vô tri. Chỉ bỏ *"được/bị"* máy móc; giữ lại khi mang đúng sắc thái lợi/hại tự nhiên. | **Trung bình — Điều chỉnh theo sắc thái ngữ dụng** |
| **ASD-STE100 (CNL)** | Giới hạn từ vựng đóng, cấm chuỗi danh từ, cấm đại từ/tỉnh lược. | Thất bại nếu áp dụng máy móc vào tiếng Việt vì phá hủy khả năng ghép từ, làm câu lặp chủ ngữ nặng nề và mất tiểu từ biểu đạt quan hệ. Chỉ giữ tư duy **1 thuật ngữ = 1 nghĩa** và đơn nghĩa phạm vi logic. | **Thấp (chỉ lấy tinh thần đơn nghĩa)** |
| **Flesch-Kincaid & đếm từ/câu ngắn** | Độ khó tỷ lệ với số âm tiết/từ và độ dài câu. | Không dùng được cho tiếng Việt (tiếng Việt chủ yếu là từ đơn tiết/từ ghép; câu ngắn rời rạc không làm giảm độ khó ngữ nghĩa, `[Bằng chứng]` Luong et al., 2020; Schriver, 1997). | **Không áp dụng** |
| **Diátaxis, BLUF, Information Mapping, CLT** | Tổ chức tri thức theo tâm lý học nhận thức và hành vi đọc quét. | Tâm lý học bộ nhớ làm việc và hành vi đọc công việc mang tính phổ quát cao; áp dụng trực tiếp vào cấu trúc đoạn/tài liệu tiếng Việt, kết hợp *Expertise Reversal* để không giải thích thừa cho chuyên gia. | **Cao — Áp dụng trực tiếp** |
| **MQM + G-Eval + Position-Swapped Blind A/B** | Gắn lỗi thực tế theo chiều, giảm thiên lệch LLM Judge. | Áp dụng trực tiếp cho hệ thống đánh giá tiếng Việt; bổ sung tầng Hard Fail phi bù trừ cho dữ kiện và logic nghiệp vụ. | **Cao — Áp dụng trực tiếp** |

---

## 4. Phản biện Các Giả thuyết Thường gặp (bao gồm giả thuyết trong đề bài)

1. **Phản biện 1: "Câu ngắn hơn và ít từ chuyên môn hơn = dễ hiểu hơn"**
   - *Phản bác:* `[Bằng chứng]` Theo CLT (Sweller) và Construction–Integration (Kintsch), nếu rút ngắn câu bằng cách cắt mất điều kiện biên, chủ thể thực hiện hoặc thay thuật ngữ chuẩn (*idempotency key*, *circuit breaker*, *chargeback*) bằng mô tả dài dòng tiếng Việt không chuẩn, **Extraneous Load** và rủi ro **Subconscious Disambiguation** tăng vọt. Một câu 30 từ phân tách rành mạch điều kiện–hành động–ngoại lệ dễ hiểu hơn nhiều một câu 12 từ mập mờ.
2. **Phản biện 2: "Hễ dùng danh từ 'việc/sự' hay từ 'được/bị' là lỗi văn dịch"**
   - *Phản bác:* `[Suy luận]` Cấm máy móc sẽ làm hỏng tiếng Việt tự nhiên. *"Việc triển khai bị hoãn vì thiếu dữ liệu kiểm thử"* là hoàn toàn tự nhiên và đúng sắc thái bất lợi của *"bị"*. Lỗi chỉ xảy ra khi xếp chồng nhiều lớp danh từ hóa rỗng (*"hỗ trợ việc thực hiện phân bổ..."*) hoặc dùng *"được thực hiện bởi"* thay cho động từ trực tiếp.
3. **Phản biện 3: "Mọi văn bản đều phải viết thật tường minh, đầy đủ liên từ nối mới mạch lạc"**
   - *Phản bác:* `[Bằng chứng]` Hiệu ứng **Reverse Cohesion** (McNamara et al., 1996) và **Expertise Reversal** (Kalyuga, 2007) chứng minh điều ngược lại với người đọc chuyên môn cao. Bồi đắp giải thích nền hoặc nhồi từ nối hiển nhiên làm chuyên gia đọc chậm và khó chịu.
4. **Phản biện 4: "Chỉ số Time to Correct Understanding (TtCU) là thước đo duy nhất cần tối ưu"**
   - *Phản bác:* `[Suy luận]` Đọc nhanh nhưng hiểu sai (do câu văn trôi chảy giả tạo che giấu điều kiện mơ hồ) còn nguy hiểm hơn đọc chậm mà hiểu đúng. Ngoài ra, văn bản có độ phức tạp nội tại (*Intrinsic Load*) cao vốn dĩ cần thời gian đọc lâu hơn văn bản đơn giản. Do đó TtCU chỉ có giá trị khi **bị khóa bởi cổng kiểm tra hiểu đúng (Comprehension Gate)** và đo ghép cặp cùng một đầu vào (xem chi tiết tại [evaluation/rubric.md](../evaluation/rubric.md)).
5. **Phản biện 5: "LLM-as-a-Judge đủ để chứng minh chất lượng Skill"**
   - *Phản bác:* `[Bằng chứng]` Zheng et al. (2023) đã chứng minh LLM Judge chịu Position Bias, Verbosity Bias và Self-Enhancement Bias. Khi chưa có human evaluation với người Việt chuyên môn, LLM Judge hoán đổi vị trí A/B kết hợp gắn nhãn lỗi MQM chỉ là công cụ sàng lọc và kiểm định sơ bộ có điều kiện, **không phải** bằng chứng tuyệt đối về hiệu quả đọc hiểu trên con người.

---

## 5. Chuẩn Agent Skills & Khả năng Tương thích Runtime

- `[Bằng chứng]` Theo đặc tả mở `agentskills.io` và tài liệu hệ thống Antigravity (`agy-customizations/docs/skills.md`):
  - Thư mục Skill đặt theo mẫu `skills/<skill-name>/SKILL.md`, trong đó tên thư mục cha **phải khớp chính xác** với trường `name` trong YAML frontmatter (chỉ gồm chữ thường `a-z`, `0-9` và gạch nối `-`, tối đa 64 ký tự).
  - Trường `description` (tối đa 1024 ký tự) được nạp sẵn vào ngữ cảnh hệ thống ở giai đoạn **Discovery** (~100 token/skill). Theo hướng dẫn `writing-skills`, `description` chỉ nên mô tả **khi nào kích hoạt** (ngôi thứ 3, bắt đầu bằng `Use when...`), **không tóm tắt quy trình bên trong** để tránh việc agent làm tắt theo tóm tắt mà bỏ qua thân `SKILL.md`.
  - Cơ chế **Progressive Disclosure** gồm 3 tầng: Discovery (`name` + `description`) → Activation (`SKILL.md` đầy đủ, giữ dưới ~500 dòng / gọn nhẹ) → Execution (chỉ đọc các file trong `references/` khi tác vụ thực sự đòi hỏi).
- **Quyết định thiết kế rút ra:** `[Suy luận]`
  - Đặt Skill tại `skills/vietnamese-human-readable-writing/` tách biệt hoàn toàn với `research/` và `evaluation/` để người dùng cài đặt sạch sẽ và môi trường Baseline thử nghiệm không bị nhiễm Skill.
  - Gắn **Context Triage (Phân tầng 3 chế độ)** ngay đầu `SKILL.md` để hội thoại thông thường chỉ tốn đọc `SKILL.md` (0 file reference) và không biến tin nhắn chat thành báo cáo hành chính.
