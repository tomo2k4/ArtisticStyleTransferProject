from flask import Flask, render_template, request, flash, send_from_directory, Response
import os
from werkzeug.utils import secure_filename
from utils.effects import pencil_sketch, cartoon_effect, watercolor_effect, webcam_sketch_effect
import uuid
import cv2

app = Flask(__name__)
app.secret_key = "12345"

# Thư mục lưu ảnh
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Tạo thư mục nếu chưa tồn tại
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    result_image = None

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Chưa chọn ảnh!', 'error')
            return render_template('index.html')

        file = request.files['file']
        effect = request.form.get('effect', 'cartoon')

        if file.filename == '':
            flash('Chưa chọn file!', 'error')
            return render_template('index.html')

        if file and allowed_file(file.filename):
            # Đặt tên file duy nhất để tránh trùng
            ext = os.path.splitext(file.filename)[1]
            filename = str(uuid.uuid4()) + ext
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Áp dụng hiệu ứng
            if effect == 'pencil':
                output = pencil_sketch(filepath)
            elif effect == 'cartoon':
                output = cartoon_effect(filepath)
            elif effect == 'watercolor':
                output = watercolor_effect(filepath)

            elif effect == 'webcam_sketch':
                from utils.effects import webcam_sketch_effect
                output = webcam_sketch_effect(filepath)
            else:
                flash('Hiệu ứng không hợp lệ!', 'error')
                return render_template('index.html')

            result_image = os.path.basename(output)
            flash('Xử lý thành công! Kết quả bên dưới ↓', 'success')
        else:
            flash('Chỉ hỗ trợ jpg, png, gif, webp', 'error')

    return render_template(
        'index.html',
        result_image=result_image,
        original_name=filename if result_image else None,
        effect_name=effect if result_image else None
)


# # Route mới cho Live Webcam (hiệu ứng 5)
# @app.route('/webcam')
# def webcam():
#     return render_template('webcam.html')  # Tạo file HTML mới cho webcam

# @app.route('/start_webcam')  # Trigger để chạy live
# def start_webcam():
#     live_webcam_drawing()  # Chạy live, không return image
#     return "Webcam closed. <a href='/'>Back to Home</a>"

@app.route('/webcam')
def run_webcam():
    from utils.effects import live_webcam_sketch
    live_webcam_sketch()
    return "Webcam closed. <a href='/'>Back</a>"


@app.route('/results/<filename>')
def results(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)