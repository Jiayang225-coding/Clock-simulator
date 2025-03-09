import numpy as np
import cv2
import math
import time

current_time = time.localtime()
print(current_time[3:6])


hour_clock = current_time[3]
min_clock = current_time[4]
second_clock = current_time[5]


if hour_clock >= 13:
    hour_clock = hour_clock - 12

angle_m = min_clock * 6
angle_s = second_clock * 0.1 
angle_h = hour_clock * 30

size = 800

radius_s = 400
center_point = (400, 400)
radius_m = 150
radius_h = 100

x_0 = 400
y_0 = 400
#angle = 0
#angle_m = 0
#angle_h = 0
angle_num = 0
count = 0
count_m = 0
clock_number = 0

clock_radius = 300


def clock_temp(x_0, y_0, clock_radius, clock_number, angle_num):

    font = cv2.FONT_HERSHEY_SIMPLEX
    black_img = np.zeros((size, size, 3), np.uint8)
    cv2.circle(black_img, center_point, radius_s, (0, 0, 255), 4, lineType=cv2.LINE_AA)
    for i in range(180):
        num_x_cal = x_0 + (clock_radius * math.sin(math.radians(angle_num)))
        num_y_cal = y_0 - (clock_radius * math.cos(math.radians(angle_num)))
        angle_num += 6
        
        print(angle_num)
        if (angle_num >= 30) and (angle_num % 30==0):
            clock_number += 1
            cv2.putText(black_img, f"{clock_number}", (round(num_x_cal), round(num_y_cal)), font, 1, (0, 255, 0), 2)
            print("clock: ", clock_number)
            if angle_num == 360:
                return black_img

while True:
    background = clock_temp(x_0, y_0, clock_radius, clock_number, angle_num)

    x_s_cal = radius_s + radius_s * math.sin(math.radians(angle_s))
    y_s_cal = radius_s - (radius_s * math.cos(math.radians(angle_s)))
    x_m_cal = x_0 + radius_m * math.sin(math.radians(angle_m))
    y_m_cal = y_0 - (radius_m * math.cos(math.radians(angle_m)))
    x_h_cal = x_0 + radius_h * math.sin(math.radians(angle_h))
    y_h_cal = y_0 - (radius_h * math.cos(math.radians(angle_h)))

    cv2.line(background, center_point, (round(x_s_cal), round(y_s_cal)), (0, 0, 255), 4, lineType=cv2.LINE_AA)
    cv2.line(background, center_point, (round(x_m_cal), round(y_m_cal)), (255, 0, 0), 4, lineType=cv2.LINE_AA)
    cv2.line(background, center_point, (round(x_h_cal), round(y_h_cal)), (255, 255, 0), 4, lineType=cv2.LINE_AA)

    angle_s += 6
    count += 1

    if count == 60:
        count = 0
        angle_m += 6
        count_m += 1

    if count_m == 60:
        count_m = 0
        angle_h += 30  

    cv2.imshow("clock", background)

    # Wait for 1ms, check for Esc key (27) or window close event
    key = cv2.waitKey(1000) & 0xFF
    if key == 27 or cv2.getWindowProperty("clock", cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()