# 🔠 EMNIST Uppercase Dataset Generator

## 📌 Giới thiệu

Dự án này sử dụng dataset EMNIST để **tách và tạo bộ dữ liệu chữ cái IN HOA (A–Z)** phục vụ cho các bài toán:

* Nhận dạng ký tự (OCR)
* AI / Machine Learning
* TinyML / Edge AI (ESP32, STM32)
* Edge Impulse

---

## 🎯 Mục tiêu

* Trích xuất **chỉ chữ in hoa (A–Z)** từ EMNIST
* Chuẩn hóa dữ liệu ảnh
* Tạo dataset dạng folder (phù hợp train ML)

---

## 📂 Cấu trúc thư mục

```
project/
 ├── main.py
 ├── dataset_uppercase/
 │    ├── A/
 │    ├── B/
 │    ├── C/
 │    └── ...
 └── README.md
```

---

## ⚙️ Yêu cầu hệ thống

* Python >= 3.8
* pip

### Thư viện cần thiết:

```bash
pip install torch torchvision matplotlib
```

---

## 🚀 Cài đặt & chạy

### 1. Clone project

```bash
git clone https://github.com/your-username/emnist-uppercase.git
cd emnist-uppercase
```

### 2. (Khuyến khích) Tạo môi trường ảo

```bash
python -m venv venv
```

👉 Kích hoạt:

* Windows:

```bash
venv\Scripts\activate
```

* Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3. Cài thư viện

```bash
pip install -r requirements.txt
```

*(hoặc cài tay nếu chưa có file requirements)*

---

### 4. Chạy chương trình

```bash
python main.py
```

---

## 🔄 Quy trình hoạt động

1. Tải dataset EMNIST (`split='byclass'`)
2. Lọc ra **26 chữ in hoa (A–Z)**
3. Xử lý ảnh:

   * Xoay lại ảnh (do EMNIST bị lệch)
   * Flip ảnh về đúng chiều
4. Lưu ảnh vào từng thư mục tương ứng

---

## 📊 Kết quả

Sau khi chạy:

```
dataset_uppercase/
 ├── A/ (500 ảnh)
 ├── B/ (500 ảnh)
 ...
 └── Z/ (500 ảnh)
```

👉 Tổng:

* 26 classes
* ~13,000 images

---

## ⚠️ Lưu ý quan trọng

* Không dùng `split='letters'` vì:

  * Không phân biệt chữ hoa / thường
* Phải dùng:

```python
split='byclass'
```

---

## 🧠 Ứng dụng

* Huấn luyện CNN nhận dạng ký tự
* Triển khai TinyML trên ESP32
* Tích hợp vào hệ thống IoT (camera nhận diện chữ)
* Sử dụng trong Edge Impulse

---

## 🔥 Nâng cấp đề xuất

* Augmentation:

  * Rotate
  * Noise
  * Blur

* Resize ảnh:

  * 28x28 → 96x96 (phù hợp embedded)

* Kết hợp dữ liệu thực tế (ảnh tự chụp)

---

## 📌 Hướng phát triển

* Train model CNN nhận dạng A–Z
* Convert sang TensorFlow Lite
* Deploy trên ESP32 / STM32
* Xây dựng web dashboard hiển thị kết quả

---

## 👨‍💻 Công nghệ sử dụng

* Python
* PyTorch
* Torchvision
* EMNIST Dataset

---

## 📄 License

MIT License

---

## ✨ Tác giả

* Your Name

---

## ⭐ Gợi ý

Nếu bạn đang làm đồ án:
👉 Kết hợp dataset này với:

* IoT + Camera
* Web Dashboard
* MQTT

→ sẽ thành hệ thống hoàn chỉnh (rất dễ đạt điểm cao 🚀)

## ⭐ Thoát : deactivate

---
