# FIFA World Cup 2026 Match Predictor using Machine Learning

Đường ống Phân loại Machine Learning cấp doanh nghiệp được xây dựng bằng Python và Streamlit để dự đoán xác suất (Thắng, Hòa, Thua) của bất kỳ thiết lập trận đấu nào trong FIFA World Cup 2026 sắp tới. Hệ thống loại bỏ các thành phần vẽ biểu đồ nặng để tập trung hoàn toàn vào các số liệu dựa trên văn bản hiệu suất cao và mô hình tỷ lệ tài chính cụ thể về miền.

## Các tính năng chính

- **Tích hợp XGBoost Classifier:** Thay thế các mô hình cơ bản bằng Extreme Gradient Boosting (`XGBClassifier`) để đào tạo dữ liệu bảng có độ chính xác cao.
- **Tiêm dữ liệu động:** Tự động xử lý các danh sách đội World Cup 2026 mở rộng (ví dụ: Indonesia, Thái Lan, Trung Quốc, v.v.) bằng cách tính toán điểm bình thường hóa cơ bản toàn cầu để ngăn chặn `KeyError` khi chạy.
- **Ràng buộc UX nghiêm ngặt:** Các hộp chọn thông minh lọc động đội chủ nhà được chọn khỏi các lựa chọn đội khách để loại bỏ các đầu vào dư thừa.
- **Phần mở rộng Phân tích thể thao (Tỷ lệ thập phân):** Chuyển đổi các mảng dự đoán toán học thành Tỷ lệ thập phân Châu Âu ($\text{Odds} = \frac{1}{\text{Probability}}$) cung cấp tham chiếu cược thể thao thực tế.
- **Lôgic giải đấu FIFA:** Lôgic bình thường hóa tùy chỉnh để xử lý các trận đấu vòng loại (cho phép hòa) so với các giai đoạn loại trực tiếp (loại bỏ hòa về mặt toán học).

---

## Kiến trúc hệ thống và Cấu trúc thư mục

Dự án tuân theo chặt chẽ kiến trúc OOP mô-đun (Lập trình hướng đối tượng) để tách biệt thao tác dữ liệu khỏi trình bày giao diện:

```text
IntroduceAI/
├── .gitignore            # Loại trừ các tệp lớn như venv/ và __pycache__/
├── requirements.txt      # Quản lý phụ thuộc có thể tái tạo
├── app.py                # Giao diện Streamlit cực kỳ gọn nhẹ (Trình bày dựa trên văn bản)
├── README.md             # Tài liệu dự án
│
├── data/
│   └── raw/              # Bộ dữ liệu lịch sử Kaggle đúng thực tế
│
└── src/                  # Backend Machine Learning cốt lõi
    ├── __init__.py       # Khởi tạo src như một gói Python
    ├── data_pipeline.py  # ETL, Feature Engineering (Tính toán Attack/Defense Strength)
    └── ai_model.py       # Đào tạo mô hình, Cấu hình siêu tham số & Đánh giá
```