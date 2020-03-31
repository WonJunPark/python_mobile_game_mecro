import pyautogui as pag
import mss, cv2
import numpy as np

pag.PAUSE = 0.08

# 색으로 아이콘을 판단하는 함수, 폭탄/칼/독/보석
def get_colors(img):
  mean = np.mean(img, axis=(0, 1))

  result = False

  # 회색
  if mean[0] > 50 and mean[0] < 60 and mean[1] > 50 and mean[1] < 60 and mean[2] > 50 and mean[2] < 60:
    result = 'BOMB'
  elif mean[0] > 245 and mean[1] > 85 and mean[1] < 120 and mean[2] > 240:
    result = 'SWORD'
  elif mean[0] > 100 and mean[0] < 130 and mean[1] > 150 and mean[1] < 200 and mean[2] > 90 and mean[2] < 110:
    result = 'POISON'
  elif mean[0] > 210 and mean[0] < 230 and mean[1] > 210 and mean[1] < 230 and mean[2] > 120 and mean[2] < 150:
    result = 'JEWEL'

  return result, mean

def click(coords):
    pag.moveTo(x=coords[0], y=coords[1], duration=0.0)
    pag.mouseDown()
    pag.mouseUp()

def mecro(left_img, right_img,left_button,right_button):
    left_icon, m1 = get_colors(left_img)
    right_icon, m2 = get_colors(right_img)

    if left_icon == 'SWORD' and (right_icon == 'BOMB' or right_icon == 'POISON'):
        print('CLICK LEFT!')
        click(left_button)

    elif right_icon == 'SWORD' and (left_icon == 'BOMB' or left_icon == 'POISON'):
        print('CLICK RIGHT!')
        click(right_button)

    elif left_icon == 'JEWEL' and right_icon == 'JEWEL':
        print('FEVER!')
        click(left_button)
        click(right_button)

    else:
        print(left_icon,right_icon)
        print(m1,m2)