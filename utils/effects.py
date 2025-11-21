import cv2
import numpy as np
import os

"""
    Hiệu ứng 1: Pencil Sketch - Sử dụng cv2.pencilSketch() hoặc Median Blur + Adaptive Threshold + đảo màu.
    Dựa trên: machinelearningprojects.net/sketch-using-opencv (Canny + Threshold inv).
    """
def pencil_sketch(input_path):
    img = cv2.imread(input_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (21, 21), 0)
    sketch = cv2.divide(gray, blur, scale=250)
    result = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    
    output_path = os.path.join('static/results', 'pencil_' + os.path.basename(input_path))
    cv2.imwrite(output_path, result)
    return output_path


"""Hiệu ứng 2: Cartoon – chuẩn theo sketch-making-flask-app"""
def cartoon_effect(input_path):
    img = cv2.imread(input_path)
    # Làm mịn màu
    color = cv2.bilateralFilter(img, 9, 250, 250)
    # Tạo viền đen
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    #kết hợp
    cartoon = cv2.bitwise_and(color, edges)
    output_path = os.path.join('static/results', 'cartoon_' + os.path.basename(input_path))
    cv2.imwrite(output_path, cartoon)
    return output_path


"""Hiệu ứng 3: Watercolor – dùng cv2.stylization + edge preserving"""
def watercolor_effect(input_path):
    img = cv2.imread(input_path)

    # temp = img.copy()
    # for _ in range(8):
    #     temp = cv2.bilateralFilter(temp, 9, 75, 75)
    # noise = np.random.normal(0, 8, img.shape).astype('uint8')
    # watercolor = cv2.add(temp, noise)
    # Dùng hàm có sẵn
    # Dùng hàm stylization có sẵn (giống watercolor)
    # Stylization có sẵn của OpenCV (rất giống watercolor)
    stylized = cv2.stylization(img, sigma_s=60, sigma_r=0.07)

    # Làm mịn thêm để giữ chi tiết
    result = cv2.bilateralFilter(stylized, 9, 75, 75)

    # Thêm chút nhiễu nhẹ cho giống tranh thật
    noise = np.random.normal(0, 5, result.shape).astype(np.uint8)
    result = cv2.add(result, noise)

    output_path = os.path.join('static/results', 'watercolor_' + os.path.basename(input_path))
    cv2.imwrite(output_path, result)
    return output_path

"""Hiệu ứng 4: Webcam Sketch Effect - Dùng Canny + Threshold Inverse"""
def webcam_sketch_effect(image_path):
    img = cv2.imread(image_path)

    # Line 5 – Gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Line 6 – Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Line 7 – Edge detection
    edges = cv2.Canny(blur, 10, 70)

    # Line 8 – Threshold
    ret, sketch = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)

    # Tạo tên file mới
    output_path = image_path.replace("uploads", "results").replace(".jpg", "_sketch.jpg")
    output_path = output_path.replace(".png", "_sketch.png")

    cv2.imwrite(output_path, sketch)
    return output_path

   