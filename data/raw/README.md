# Dự đoán World Cup 2026

## Tổng quan dự án

Dự án này minh họa một quy trình Phân tích Dữ liệu hoàn chỉnh bằng Python. Mục tiêu là làm sạch, chuyển đổi, phân tích và trực quan hóa dữ liệu để khám phá những hiểu biết có ý nghĩa và hỗ trợ ra quyết định dựa trên dữ liệu.

Dự án bao gồm tiền xử lý dữ liệu, phân tích dữ liệu khám phá (EDA), trực quan hóa, kỹ thuật tính năng và tài liệu tuân theo các thực tiễn tiêu chuẩn công nghiệp.

## Mục tiêu

* Tải và khám phá tập dữ liệu
* Xử lý các giá trị bị thiếu và không nhất quán
* Phát hiện và phân tích các ngoại lệ
* Chuyển đổi và mã hóa dữ liệu
* Thực hiện Phân tích Dữ liệu Khám phá (EDA)
* Tạo ra các hình ảnh hóa có ý nghĩa
* Trích xuất những hiểu biết có thể hành động được
* Tài liệu toàn bộ quá trình phân tích
* Duy trì kiểm soát phiên bản dự án bằng Git và GitHub

## Công nghệ sử dụng

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git
* GitHub

## Cấu trúc dự án

```
├── data/
│   ├── test (2).csv
│   └── cleaned_dataset.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── scripts/
│   └── analysis.py
│
├── visuals/
│   ├── fifa_points_distribution.png
│   ├── market_vs_fifa.png
│   └── correlation_heatmap.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Quy trình Phân tích Dữ liệu

### 1. Thu thập và Tải dữ liệu

* Nhập tập dữ liệu bằng Pandas.
* Xác minh cấu trúc và kích thước tập dữ liệu.

### 2. Khám phá Dữ liệu

* Kiểm tra các loại dữ liệu và thông tin cột.
* Tạo thống kê tóm tắt.
* Xác định các giá trị bị thiếu và các vấn đề chất lượng dữ liệu tiềm ẩn.

### 3. Làm sạch Dữ liệu

* Xử lý các giá trị số bị thiếu bằng phép tính trung vị.
* Xử lý các giá trị phân loại bị thiếu bằng phép tính chế độ.
* Kiểm tra các bản ghi trùng lặp.

### 4. Phát hiện Ngoại lệ

* Sử dụng phương pháp Phạm vi tứ phân vị (IQR).
* Trực quan hóa các ngoại lệ bằng boxplots.

### 5. Chuyển đổi Dữ liệu

* Áp dụng One-Hot Encoding cho các biến phân loại.
* Tạo các tính năng mới để cải thiện phân tích.
* Chuẩn bị dữ liệu cho các tác vụ phân tích tiếp theo.

### 6. Phân tích Dữ liệu Khám phá (EDA)

* Phân tích phân bố bằng biểu đồ.
* Phân tích mối quan hệ bằng biểu đồ phân tán.
* Phân tích tương quan bằng bản đồ nhiệt.
* Tạo tóm tắt thống kê.

### 7. Trực quan hóa

* Phân bố Điểm FIFA
* Giá trị Thị trường so với Điểm FIFA
* Bản đồ nhiệt Tương quan

## Những phát hiện chính

* Các đội có giá trị thị trường cao hơn thường đạt được xếp hạng FIFA cao hơn.
* Hiệu số bàn thắng là chỉ số quan trọng của hiệu suất đội.
* Xếp hạng cầu thủ và điểm hình thức gần đây ảnh hưởng mạnh mẽ đến điểm FIFA.
* Một số biến thể hiện mối tương quan tích cực mạnh mẽ.
  
## Cách chạy dự án

### Chạy Phân tích

python analysis.py

hoặc mở Jupyter Notebook:
jupyter notebook

## Yêu cầu

pandas
numpy
matplotlib
seaborn
jupyter

## Hình ảnh Mẫu

* Phân bố Điểm FIFA
* Biểu đồ Phân tán Giá trị Thị trường so với Điểm FIFA
* Bản đồ nhiệt Tương quan

## Tác giả

Bibas Basnet

## Giấy phép

Dự án này dành cho mục đích giáo dục và danh mục đầu tư.
