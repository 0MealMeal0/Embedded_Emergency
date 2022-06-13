import http.client, urllib
import urllib.parse
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

KEY = 'FUZL8XUHDB0QMYYZ'
# 9라인 앞부분 temp를 자기 센서 이름으로 변경, 예)화염센서: temp -> flame
water_headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

DEBUG = True


# 각자 센서 값 받아오는 벙법적기

def water_temp():  # read_본인의 센서이름 으로 이름변경 예)화염센서: read_temp() -> read_flame
    if DEBUG:
        print("water sensor")

    # 왼쪽 내용 지우고 각자 센서 값 불러오는 메소드 등 적기,
        while True:

            if ser.readable():
                val = ser.readline()
                p = int(val.decode()[:len(val) - 2])
                return print(p)