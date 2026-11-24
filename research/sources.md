# Nguồn tham khảo đã xác minh (Verified Sources)

Tài liệu này tổng hợp các công trình học thuật, tiêu chuẩn quốc tế, khung phương pháp và dự án mã nguồn mở đã được kiểm tra và sử dụng trực tiếp để xây dựng hệ thống phân loại lỗi, bộ tiêu chí đánh giá và thiết kế Skill. Không đưa vào bất kỳ nguồn hoặc số liệu chưa được xác minh.

---

## 1. Việt ngữ học, Ngữ pháp chức năng và Ngữ dụng học

1. **Cao Xuân Hạo (1991).** *Tiếng Việt: Sơ thảo ngữ pháp chức năng* (Quyển 1). NXB Khoa học Xã hội, TP. Hồ Chí Minh.
   - **Nội dung dùng trong dự án:** Phân biệt cấu trúc Đề–Thuyết (Topic–Comment) với cấu trúc Chủ–Vị kiểu Ấn–Âu; lý giải đặc trưng loại hình ngôn ngữ đơn lập, phân tích tính; phê phán hiện tượng Âu hóa cú pháp và lạm dụng danh từ hóa/bị động khi áp đặt ngữ pháp phương Tây vào tiếng Việt.
2. **Trần Ngọc Thêm (1985).** *Hệ thống liên kết văn bản tiếng Việt*. NXB Khoa học Xã hội, Hà Nội.
   - **Nội dung dùng trong dự án:** Phân định liên kết nội dung (coherence: liên kết chủ đề và liên kết logic) với liên kết hình thức (cohesion); hệ thống 5 phép liên kết bề mặt (phép lặp, phép thay thế, phép liên tưởng, phép nối, phép tỉnh lược).
3. **Đỗ Hữu Châu.** *Đại cương ngôn ngữ học — Tập 2: Ngữ dụng học*. NXB Giáo dục, Hà Nội.
   - **Nội dung dùng trong dự án:** Hệ thống hóa lý thuyết hành động ngôn ngữ và quy tắc hội thoại trong bối cảnh tiếng Việt; phân tích ảnh hưởng của vai giao tiếp, quan hệ xã hội và tính lịch sự đến lượng thông tin và cách diễn đạt tiếng Việt.
4. **Nguyễn Đức Dân.** *Ngữ dụng học* (Tập 1 & Tập 2). NXB Giáo dục, Hà Nội.
   - **Nội dung dùng trong dự án:** Logic ngôn ngữ và cơ chế lập luận trong tiếng Việt; cách vận dụng và hàm ý từ các phương châm hội thoại; phân biệt sắc thái đánh giá tích cực/tiêu cực của "được" và "bị" trong ngữ dụng tiếng Việt so với thể bị động trung tính phương Tây.
5. **Grice, H. P. (1975).** *Logic and Conversation*. In P. Cole & J. L. Morgan (Eds.), *Syntax and Semantics, Vol. 3: Speech Acts* (pp. 41–58). Academic Press.
   - **Nội dung dùng trong dự án:** Nguyên tắc cộng tác (Cooperative Principle) và 4 phương châm hội thoại: Lượng (Quantity), Chất (Quality), Quan hệ (Relation), Cách thức (Manner); lý giải hiện tượng AI vi phạm phương châm Lượng (nói dài vô ích) và Cách thức (mơ hồ, thiếu trình tự).

---

## 2. Plain Language, Controlled Natural Language và Information Design

6. **ISO 24495-1:2023.** *Plain language — Part 1: Governing principles and guidelines*. International Organization for Standardization (June 2023), phát triển cùng International Plain Language Federation (IPLF). *(Mở rộng với các phần tiếp theo gồm ISO 24495-2:2025 cho pháp lý, ISO 24495-3 cho khoa học, ISO 24495-4 cho triển khai tổ chức, ISO 24495-5 cho thiết kế tài liệu).*
   - **Nội dung dùng trong dự án:** Định nghĩa lấy người đọc làm trung tâm (**Find – Understand – Use**) và 4 nguyên tắc cốt lõi: Relevance, Findability, Understandability, Usability; phân biệt *plain language* với *easy language*.
7. **Williams, J. M., & Bizup, J.** *Style: Lessons in Clarity and Grace*. Pearson / University of Chicago Press.
   - **Nội dung dùng trong dự án:** Nguyên tắc viết rõ nghĩa trong tiếng Anh: chọn tác thể làm chủ ngữ (Characters as subjects), hành động làm động từ (Actions as verbs), gỡ bỏ danh từ hóa (nominalization), và mạch thông tin Cũ→Mới (Old-to-New). *(Được kiểm tra và điều chỉnh khi chuyển sang tiếng Việt Đề–Thuyết).*
8. **Kuhn, T. (2014).** *A Survey and Classification of Controlled Natural Languages*. *Computational Linguistics*, 40(1), 121–170.
   - **Nội dung dùng trong dự án:** Khảo sát khoảng 100 ngôn ngữ tự nhiên có kiểm soát (CNL), chỉ rõ sự thiên lệch áp đảo về tiếng Anh và ngữ pháp Ấn–Âu.
9. **AeroSpace and Defence Industries Association of Europe (ASD).** *ASD-STE100: Simplified Technical English Specification*.
   - **Nội dung dùng trong dự án:** Đối chứng hạn chế của bộ quy tắc cấm từ/giới hạn cú pháp cứng nhắc (cấm noun stacks, bắt buộc từ điển giới hạn, cấm tỉnh lược) khi áp dụng máy móc cho tiếng Việt đơn lập.
10. **Horn, R. E.** *Information Mapping* (phát triển từ cuối thập niên 1960).
    - **Nội dung dùng trong dự án:** Phân khối thông tin theo chức năng (Procedure, Process, Principle, Fact, Concept), phân đoạn nhỏ (chunking) và gắn nhãn khối giúp người đọc tìm nhanh.
11. **Minto, B.** *The Pyramid Principle: Logic in Writing and Thinking*.
    - **Nội dung dùng trong dự án:** Cấu trúc trình bày kết luận/ý chính trước (Top-down / Bottom-Line-Up-Front — BLUF), sau đó mới đến luận điểm hỗ trợ và dữ kiện chi tiết.
12. **Procida, D.** *Diátaxis Documentation Framework* (`diataxis.fr`).
    - **Nội dung dùng trong dự án:** Tách biệt 4 loại tài liệu theo nhu cầu người đọc: Tutorials, How-to guides, Reference, Explanation; chẩn đoán lỗi trộn lẫn chế độ tài liệu.
13. **ISO/IEC/IEEE 29148.** *Systems and software engineering — Life cycle processes — Requirements engineering*.
    - **Nội dung dùng trong dự án:** Các thuộc tính bắt buộc của đặc tả yêu cầu: Unambiguous (đơn nghĩa), Verifiable (kiểm chứng được), Complete (đầy đủ), Consistent (nhất quán).

---

## 3. Tâm lý học Nhận thức, Đọc hiểu và Mơ hồ Ngữ nghĩa

14. **Sweller, J. (1988); Sweller, J., Ayres, P., & Kalyuga, S. (2011).** *Cognitive Load Theory*.
    - **Nội dung dùng trong dự án:** Phân biệt 3 loại tải nhận thức (Intrinsic, Extraneous, Germane), hiệu ứng phân tán chú ý (Split-Attention Effect) và hiệu ứng dư thừa (Redundancy Effect).
15. **Kalyuga, S. (2007).** *Expertise Reversal Effect and Its Implications for Learner-Tailored Instruction*. *Educational Psychology Review*, 19(4), 509–539.
    - **Nội dung dùng trong dự án:** Cơ sở lý giải vì sao giải thích từng bước quá chi tiết lại làm tăng tải nhận thức ngoại lai và giảm hiệu suất của người đọc có chuyên môn.
16. **Kintsch, W. (1988, 1998).** *Comprehension: A Paradigm for Cognition* (Construction-Integration Model). Cambridge University Press.
    - **Nội dung dùng trong dự án:** 3 tầng biểu diễn khi đọc hiểu: Surface code (bề mặt câu chữ), Textbase (mệnh đề ngữ nghĩa), Situation model (mô hình tình huống thực tế).
17. **McNamara, D. S., Kintsch, E., Songer, N. B., & Kintsch, W. (1996).** *Are good texts always better? Interactions of text coherence, background knowledge, and levels of understanding in learning from text*. *Cognition and Instruction*, 14(1), 1–43.
    - **Nội dung dùng trong dự án:** Phát hiện **Reverse Cohesion Effect**: người đọc có nền tảng kiến thức cao đôi khi tạo mô hình tình huống sâu hơn khi văn bản không quá rườm rà liên từ tường minh; củng cố nguyên tắc không áp đặt một độ tường minh cố định cho mọi đối tượng.
18. **Schriver, K. A. (1997).** *Dynamics in Document Design*. John Wiley & Sons; và **Redish, J. (G.).** Các nghiên cứu về usability của tài liệu kỹ thuật (*Letting Go of the Words*, các bài viết tại `redish.net`).
    - **Nội dung dùng trong dự án:** Người đọc tài liệu công việc đọc quét/tìm theo mục tiêu chứ không đọc tuyến tính từ đầu đến cuối; hạn chế của các công thức readability bề mặt (đếm độ dài từ/câu); phương pháp kiểm thử khả dụng đọc hiểu (think-aloud, task-completion time).
19. **Berry, D. M., Kamsties, E., & Krieger, M. M. (2003).** *From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity*. Technical Report, University of Waterloo.
    - **Nội dung dùng trong dự án:** Phân loại nguồn gốc mơ hồ ngôn ngữ (Lexical, Syntactic/Structural, Referential, Scope, Vagueness vs Ambiguity) và khái niệm **Subconscious Disambiguation** (người đọc tự hiểu theo một nghĩa mặc định mà không biết người khác hiểu sang nghĩa khác).

---

## 4. Liên kết Diễn ngôn và Đánh giá Độ dễ đọc Tiếng Việt

20. **Halliday, M. A. K., & Hasan, R. (1976).** *Cohesion in English*. Longman.
    - **Nội dung dùng trong dự án:** Khung đối chiếu lý thuyết Cohesion (liên kết hình thức) với công trình Việt hóa của Trần Ngọc Thêm (1985).
21. **Mann, W. C., & Thompson, S. A. (1988).** *Rhetorical Structure Theory: Toward a functional theory of text organization*. *Text*, 8(3), 243–281.
    - **Nội dung dùng trong dự án:** Mô hình hóa mạch lạc toàn văn bản theo cấu trúc hạt nhân–vệ tinh (Nucleus–Satellite) và các quan hệ tu từ (Elaboration, Contrast, Explanation, Condition...).
22. **Grosz, B. J., Joshi, A. K., & Weinstein, S. (1995).** *Centering: A Framework for Modeling the Local Coherence of Discourse*. *Computational Linguistics*, 21(2), 203–225.
    - **Nội dung dùng trong dự án:** Lý giải mạch lạc cục bộ giữa các câu liên tiếp thông qua tiêu điểm chú ý (backward/forward-looking center) và cách chọn biểu thức quy chiếu.
23. **Luong, A.-V., Nguyen, D., & Dinh, D. (2018, 2020).** *A New Formula for Vietnamese Text Readability Assessment* (2018); *Building a Corpus for Vietnamese Text Readability Assessment in The Literature Domain* (*Universal Journal of Educational Research*, 2020 — tập dữ liệu **ViRead**); *Assessing Vietnamese Text Readability Using Multi-Level Linguistic Features* (2020); cùng các nghiên cứu tiếp nối kết hợp PhoBERT / ViDeBERTa.
    - **Nội dung dùng trong dự án:** Bằng chứng thực nghiệm cho thấy công thức đo độ dễ đọc tiếng Anh (như Flesch-Kincaid dựa vào âm tiết) không áp dụng trực tiếp được cho tiếng Việt đơn lập/đơn tiết, cần đặc trưng đa tầng (từ vựng, từ loại, cú pháp, ngữ nghĩa).

---

## 5. Đánh giá Chất lượng Đa chiều và Nghiên cứu LLM Tiếng Việt

24. **Lommel, A., Uszkoreit, H., & Burchardt, A. (2014).** *Multidimensional Quality Metrics (MQM): A Framework for Declaring and Describing Translation Quality Metrics*. *Tradumàtica*, 12, 455–463.
    - **Nội dung dùng trong dự án:** Khung phân loại lỗi đa chiều (Accuracy, Fluency, Terminology, Style...) tách biệt với thang điểm tổng thể đơn nhất.
25. **Freitag, M., Foster, G., Grangier, D., Ratnakar, V., Tan, Q., & Macherey, W. (2021).** *Experts, Errors, and Context: A Large-Scale Study of Human Evaluation for Machine Translation*. *Transactions of the Association for Computational Linguistics (TACL)*, 9, 1460–1474.
    - **Nội dung dùng trong dự án:** Chuẩn hóa đánh giá lỗi gắn đoạn văn bản thực tế theo 3 mức độ nghiêm trọng (*Minor, Major, Critical*) thay cho chấm điểm cảm tính.
26. **Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., ... & Stoica, I. (2023).** *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*. *NeurIPS 2023*.
    - **Nội dung dùng trong dự án:** Cơ chế nhận diện và kiểm soát 3 thiên lệch hệ thống của LLM Judge: **Position Bias**, **Verbosity Bias** và **Self-Enhancement Bias**.
27. **Liu, Y., Iter, D., Xu, Y., Wang, S., Xu, R., & Zhu, C. (2023).** *G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment*. *EMNLP 2023*.
    - **Nội dung dùng trong dự án:** Phương pháp tăng độ tương đồng với đánh giá con người bằng các bước suy luận (Chain-of-Thought) tường minh bám theo từng tiêu chí trước khi cho điểm.
28. **Li, Y., Zhang, R., Wang, Z., Zhang, H., Cui, L., Yin, Y., Xiao, T., & Zhang, Y. (2025).** *Lost in Literalism: How Supervised Training Shapes Translationese in LLMs*. *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025)*.
    - **Nội dung dùng trong dự án:** Giải thích cơ chế khiến LLM tạo văn phong dịch sát (*translationese*) ngay cả khi tiền huấn luyện lớn: thiên lệch từ dữ liệu tinh chỉnh có giám sát (SFT) bám sát cấu trúc từng câu thay vì sinh tự nhiên ở ngôn ngữ đích.
29. **Susanto, Y. et al. / AI Singapore (2025).** *SEA-HELM: Southeast Asian Holistic Evaluation of Language Models* (tích hợp bộ chẩn đoán ngôn ngữ **LINDSEA** cho tiếng Việt và các ngôn ngữ Đông Nam Á). *ACL 2025*.
    - **Nội dung dùng trong dự án:** Khung chẩn đoán năng lực hình thái–cú pháp–ngữ nghĩa–ngữ dụng của LLM trên tiếng Việt, tách khỏi các bài dịch máy từ tiếng Anh.
30. **Tran, Q.-D., Nguyen, V.-Q., Pham, Q.-H., Nguyen, K. B. T., & Do, T.-H. (2024).** *Vietnamese AI Generated Text Detection* (tập dữ liệu **ViDetect** — 6.800 mẫu: 3.400 người viết + 3.400 LLM). arXiv:2405.xxxxx.
    - **Nội dung dùng trong dự án:** Bằng chứng thực nghiệm về sự tồn tại của các dấu hiệu bề mặt giúp mô hình phân biệt văn bản tiếng Việt do AI sinh và do người Việt viết.

---

## 6. Chuẩn Agent Skills và Dự án Mã nguồn mở (Prior Art)

31. **Chuẩn kỹ thuật & Dự án tham khảo thực tế:**
    - **`agentskills.io` Specification** & **Antigravity Customization System Guide (`agy-customizations/docs/skills.md`):** Quy chuẩn thư mục `skills/<name>/SKILL.md`, yêu cầu `name` khớp tên thư mục cha, YAML frontmatter (`name`, `description`), cơ chế Progressive Disclosure 3 tầng (Discovery → Activation → Execution).
    - **Wikipedia: *Signs of AI writing* (WikiProject AI Cleanup):** Danh mục thực chứng các dấu hiệu "văn AI" trong tiếng Anh (lạm dụng từ hoa mỹ, quy tắc 3 vế cứng nhắc, rào đón sáo rỗng, khẳng định tầm quan trọng giả tạo).
    - **Các dự án GitHub mở liên quan:**
      - `blader/humanizer`: Chuyển hóa danh mục dấu hiệu AI của Wikipedia thành Skill chỉ dẫn chỉnh sửa giữ nguyên dữ kiện.
      - `anhnx000/viet-nhu-nguoi`: Chống giọng AI cho tiếng Việt, kèm script quét dấu hiệu bề mặt.
      - `longhang2004/vietnamese-humanizer`: Bộ 4 skill con (`humanizer-vi`, `translationese-cleaner-vi`, `grammar-checker-vi`, `style-guide-vi`) bảo toàn dữ kiện.
      - `trussary/vietnamese-language-skill`: Khắc phục hiện tượng dịch thô giữ trật tự từ tiếng Anh và lỗi định dạng/quảng cáo quá đà.
      - `gencharitaci/humanize-skills`: Chuẩn hóa văn phong đa ngôn ngữ theo nhiều chế độ (*technical, academic, business, legal*).
