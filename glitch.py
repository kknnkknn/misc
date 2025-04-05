from PIL import Image
import numpy as np
import random

def flexible_glitch(input_path, output_path, horizontal_slices=100, vertical_slices=100):
    img = Image.open(input_path).convert('RGBA')
    data = np.array(img)

    height, width, _ = data.shape

    # 横方向のスライス処理
    for _ in range(horizontal_slices):
        slice_height = random.randint(1, max(1, height // (horizontal_slices // 2)))
        slice_start = random.randint(0, height - slice_height)
        shift_x = random.randint(-width // 3, width // 3)

        slice_end = slice_start + slice_height
        data[slice_start:slice_end] = np.roll(data[slice_start:slice_end], shift_x, axis=1)

    # 縦方向のスライス処理
    for _ in range(vertical_slices):
        slice_width = random.randint(1, max(1, width // (vertical_slices // 2)))
        slice_start = random.randint(0, width - slice_width)
        shift_y = random.randint(-height // 3, height // 3)

        slice_end = slice_start + slice_width
        data[:, slice_start:slice_end] = np.roll(data[:, slice_start:slice_end], shift_y, axis=0)

    glitched_img = Image.fromarray(data, 'RGBA')
    glitched_img.save(output_path)

# 使用例（縦スライス50個、横スライス200個）
flexible_glitch(
    './pic/IMG_1841.png',
    'output_flexible_glitch2.png',
    horizontal_slices=100,
    vertical_slices=8
)
# 使用例
