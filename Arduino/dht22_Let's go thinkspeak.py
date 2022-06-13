import http.client, urllib
import urllib.parse
import time
import serial
import pymysql


ser = serial.Serial('COM6', 9600)

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
                return int(p)# int형으로 센서값 리턴


while True:

    # 요 밑에부터 temp를 자기 센서 이름으로 변경, 예)화염센서: temp -> flame
    water = water_temp()  # tempature
    water_params = urllib.parse.urlencode({"field5": water, "key": KEY})
    # 위에 field1을 불꽃센서는 field3, field4는 지진센서, field5는 침수센서
    water_conn = http.client.HTTPConnection("api.thingspeak.com:80")

    try:
        water_conn.request("POST", "/update", water_params, water_headers)
        water_response = water_conn.getresponse()

        if DEBUG:
            print(water_response.status, water_response.reason)

        water_data = water_response.read()
        water_conn.close()

    except:
        print("Connection failed")
    

    time.sleep(2)