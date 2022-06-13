import time
import pyfirmata

# 아두이노에 연결합니다. 
board = pyfirmata.Arduino('/dev/ttyACM0')

# 디지털(digital) 핀(pin) 13번을 출력(output) 모드로 가져옵니다.
# d(digital)/a(analog)
# i(input)/0(output)/p(PWM)
led_builtin = board.get_pin('d:2:i')


while True:
    # 핀에 출력값으로 1을 주면 led 불이 켜집니다. 
    print(led_builtin.read())
    time.sleep(1)
    # 핀에 출력값으로 0을 주면 led 불이 꺼집니다.     
   