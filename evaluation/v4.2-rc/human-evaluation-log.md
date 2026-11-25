# Nhật ký Đánh giá Thực tế của Người dùng (`Human Evaluation Log`)

Tài liệu này lưu lại **nguyên trạng kết quả đánh giá mù thực tế** từ chủ sở hữu repository trên hai vòng thí nghiệm trước khi phát triển `v4.2-rc`. Không có bất kỳ điểm số hay nhận xét nào được suy diễn hoặc tạo thêm.

> **Lưu ý diễn giải dữ liệu:** Đây là lựa chọn thực tế của **một người sử dụng** trên **một tập tình huống giới hạn**, dùng làm tín hiệu định hướng cải tiến thiết kế — **không phải** bằng chứng thống kê về ưu thế tuyệt đối của bất kỳ phiên bản hay nhánh nào.

---

## 1. Vòng 1 — Semantic Reconstruction ([`archive/experiment-semantic-reconstruction`](https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/tree/archive/experiment-semantic-reconstruction), commit `275ce12b`)

| Ca đánh giá | Bộ mẫu đối chứng | Lựa chọn của người dùng | Ghi chú thực tế từ người dùng |
|---|---|---|---|
| **SR-03** | A (`Gemini + v4.1 native*`), B (`Gemini + v4.1 injected`), C (`Gemini + v4.1 + SR`) | **Group C** được ưu tiên | Group A cũng được đánh giá ổn; Group B dài dòng *(gắn phần điểm chưa rõ vào giao tiếp nội bộ)*. |
| **SR-04** | A, B, C | **Group C** | — |
| **SR-07** | A, B, C | **Group C** | — |

*\*Cả 3 ca trên trong gói đánh giá đều đặt theo thứ tự `C / B / A` nên vòng 1 chưa loại trừ hoàn toàn thiên kiến vị trí.*

---

## 2. Vòng 2 — V5 Communication-First ([`archive/experiment-v5-communication-first`](https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/tree/archive/experiment-v5-communication-first), commit `3f1c3d5c`)

Gói chấm mù `V5` đã xoay vòng vị trí `Mẫu 1` cân bằng (`{A:3, B:3, C:3, E:2, F:2}`) giữa 5 nhánh `A, B, C, E (V5-A), F (V5-B)`. Kết quả người dùng phản hồi trên 6 ca unseen `V5-01..V5-06`:

| Ca đánh giá | Nhánh được chọn | Thực tế kích hoạt của nhánh trong log | Nhận định kỹ thuật liên quan |
|---|---|---|---|
| **V5-01** *(Hội thoại đồng nghiệp)* | **Group A** | **Native `v4.1`** *(subagent tự đọc `~/.gemini/config/skills/.../SKILL.md` v4.1)* | Độ tự nhiên giữ nguyên giọng chat đồng nghiệp của nền `v4.1` khi không bị gò vào mẫu ngắn cứng. |
| **V5-02** *(Thông báo app mobile)* | **Group C** | `v4.1 + SR` (`injected`) | Cô đọng, tách rõ việc bị dừng vs vẫn chạy cho người dùng đọc nhanh trên điện thoại. |
| **V5-03** *(Email ra quyết định 30s)* | **Group A** | **Native `v4.1`** | Cấu trúc rõ ràng; tránh được lỗi `Minor` tự thêm `"(Sản phẩm)"` / thu hẹp mốc hỗ trợ ở `Group C`. |
| **V5-04** *(Giải thích kỹ thuật)* | **Group A** | **Native `v4.1`** | Giữ đủ chiều sâu và mạch giải thích kỹ thuật tốt hơn các bản rút gọn. |
| **V5-05** *(Business Rule B2B phức tạp)* | **Ngang nhau** *(Tie)* | Toàn bộ nhánh giữ cấu trúc BR/AC + `[Chưa chốt]` | Cho thấy các nguyên tắc đặc tả của `v4.1` khi gặp BR phức tạp đã bám khá sát nhu cầu triển khai thực tế *(lưu ý ở log `Group A V5-05` có lỗi sót 1 gap + meta tự hiệu đính ở Layer 1)*. |
| **V5-06** *(Quy định dài nhiều ý lặp)* | **Group C** | `v4.1 + SR` (`injected`) | Tổ chức lại gọn gàng hơn bản `v4.1` gốc (`Group A`: 620 từ vs `Group C`: 335 từ). |

> **Cảnh báo phương pháp học trọng yếu:** Kiểm tra log `transcript_full.jsonl` xác nhận **Group A trong vòng V5 thực tế đã kích hoạt `v4.1` qua native skill discovery** trên `13/13` lượt chạy — không phải Gemini thuần không có ViWrite. Chính dữ kiện này (cùng với việc người dùng đánh giá cao Group A/v4.1 ở `V5-01, V5-03, V5-04` và Group C ở `SR-03/04/07, V5-02, V5-06`, thay vì `V5-A`/`V5-B`) dẫn tới quyết định giữ `v4.1` làm nền cho `v4.2-rc` và tích hợp có chọn lọc các cải tiến của `Group C (SR)` & `V5`.
