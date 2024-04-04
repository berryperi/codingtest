# 주어진 데이터
original_sizes = [(429, 640), (480, 640)]  # (height, width) 형태
target_size = (128, 128)
bboxes = [
    [9.98, 188.56, 5.54, 0.0],
    [296.65, 388.33, 1.03, 0.0]
]

# 리사이징된 바운딩 박스 계산
resized_bboxes = []

for original_size, bbox in zip(original_sizes, bboxes):
    x_ratio = target_size[0] / original_size[1]  # 너비 비율
    y_ratio = target_size[1] / original_size[0]  # 높이 비율
    
    resized_x_min = bbox[0] * x_ratio
    resized_y_min = bbox[1] * y_ratio
    resized_width = bbox[2] * x_ratio
    resized_height = bbox[3] * y_ratio
    
    resized_bbox = [resized_x_min, resized_y_min, resized_width, resized_height]
    resized_bboxes.append(resized_bbox)

print(resized_bboxes)
