import http.client, urllib
import urllib.parse
import time
import Adafruit_DHT
import serial
import re

KEY = 'FUZL8XUHDB0QMYYZ'
#9라인 앞부분 temp를 자기 센서 이름으로 변경, 예)화염센서: temp -> flame
flame_headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

DEBUG = True

# 아두이노 화염센서 연결
port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()

# 각자 센서 값 받아오는 벙법적기

class flame_sensor() :

    def read_temp(): # read_본인의 센서이름 으로 이름변경 예)화염센서: read_temp() -> read_flame
      if DEBUG:
        print("reading fire")
      input_s = serialFromArduino.readline()
      numbers = re.sub(r'[^0-9]','',input_s.decode('utf-8'))
        #input = int(float(input_s))
     # 왼쪽 내용 지우고 각자 센서 값 불러오는 메소드 등 적기, 
      return int(numbers) #int형으로 센서값 리턴
    
    if __name__ == "__main__" :
    
        while True:

            # 요 밑에부터 temp를 자기 센서 이름으로 변경, 예)화염센서: temp -> flame
            flame = read_temp() #tempature
            flame_params = urllib.parse.urlencode({"field3": flame, "key": KEY})
            #위에 field1을 불꽃센서는 field3, field4는 지진센서, field5는 침수센서
            flame_conn = http.client.HTTPConnection("api.thingspeak.com:80")
            
            try:
                flame_conn.request("POST", "/update", flame_params, flame_headers)
                flame_response = flame_conn.getresponse()
                
                if DEBUG:
                    print (flame_response.status, flame_response.reason)
                
                flame_data = flame_response.read()
                flame_conn.close()
                
            except:
                print("Connection failed")
            #temp part end
            
            time.sleep(2)


    