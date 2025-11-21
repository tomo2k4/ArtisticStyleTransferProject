# Artistic Style Transfer – Biến ảnh thật thành tranh nghệ thuật

Dự án Flask + OpenCV chuyển ảnh  
- Pencil Sketch  
- Cartoon  
- Watercolor  
- Stroked Drawing


---

### YÊU CẦU HỆ THỐNG
- Windows
- Python 3.**  <== PHẢI TẢI VỀ SẴN
- Git + VSCode 

---

### HƯỚNG DẪN CHẠY DỰ ÁN

#### Bước 1: Clone dự án
```bash
git clone https://github.com/username-cua-ban/Artistic-Style-Transfer.git
cd Artistic-Style-Transfer

Bước 2: Tạo môi trường ảo + cài thư viện
# 3.1 Tạo venv bằng Python 
# python -m venv venv

# 3.2 Kích hoạt venv
source venv/Scripts/activate

# 3.3 Cài phiên bản
pip install --upgrade pip
pip install flask opencv-python numpy

#  Kiểm tra (sẽ không lỗi nữa)
python -c "import cv2, numpy, flask; print('Tất cả import OK → OpenCV', cv2.__version__)"

#Chạy project
python app.py
