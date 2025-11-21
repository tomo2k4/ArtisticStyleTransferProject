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

### HƯỚNG DẪN CHẠY DỰ ÁN (chỉ 5 bước – 3 phút là xong)

#### Bước 1: Clone dự án
```bash
git clone https://github.com/username-cua-ban/Artistic-Style-Transfer.git
cd Artistic-Style-Transfer

Bước 2: Tạo môi trường ảo + cài thư viện
# 3.1 Tạo venv bằng Python 
# python -m venv venv

# 3.2 Kích hoạt venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/Scripts/activate

# 3.3 Cài đúng phiên bản đã test 100% (không bị lỗi NumPy)
pip install --upgrade pip
pip install flask==3.0.3 opencv-python==4.10.0.84 numpy==1.26.4


