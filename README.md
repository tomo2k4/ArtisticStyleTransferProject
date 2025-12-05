# Artistic Style Transfer – Biến ảnh thật thành tranh nghệ thuật

Dự án Flask + OpenCV chuyển ảnh  
- Pencil Sketch  
- Cartoon  
- Watercolor  
- Stroked Drawing
---

### HƯỚNG DẪN CHẠY DỰ ÁN

#### Bước 1: Clone dự án
```bash
git clone https://github.com/username-cua-ban/Artistic-Style-Transfer.git
cd Artistic-Style-Transfer


Bước 2. Chuẩn bị môi trường (Setup Environment)

    Trước khi chạy dự án, bạn cần cài đặt Python và các thư viện cần thiết. Nếu dự án sử dụng xử lý ảnh, chúng ta sẽ thêm NumPy và OpenCV.

- Cài đặt Python: Tải từ trang chính thức (python.org).

            python --version

- Tạo môi trường ảo ( Virtual Environment): Để tránh xung đột thư viện.

            python -m venv myenv
            source myvenv/Scripts/activate ( áp dụng window )

- Cài đặt Flask và các thư viện liên quan:
            
            pip install flask numpy opencv-python

    * Flask: Để xây dựng ứng dụng web.
    * NumPy: Xử lý mảng, ma trận 
    * OpenCV(opencv-python): Để xử lý ảnh thực tế

-  Cài đúng phiên bản

            pip install --upgrade pip              
            pip install flask opencv-python numpy

- Chạy dự án FlaskBash
    * Cách 1: nếu file chính tên app.py hoặc main.py
            
            python app.py

    * Cách 2: dùng lệnh flask
            
            flask run
