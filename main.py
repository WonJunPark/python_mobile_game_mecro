import mss, cv2
import numpy as np
import helper

# bluestacks 좌표
# 아이콘 위치
left_icon_pos = {'left': 190, 'top': 1051, 'width': 130, 'height': 130}
right_icon_pos = {'left': 496, 'top': 1051, 'width': 130, 'height': 130}

# 버튼 위치
left_button = [129, 1321]
right_button = [696, 1328]

while True:

    with mss.mss() as sct:
        left_img = np.array(sct.grab(left_icon_pos))[:, :, :3]
        right_img = np.array(sct.grab(right_icon_pos))[:, :, :3]
        helper.mecro(left_img, right_img, left_button, right_button)

