import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 21

humidity, temprature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temprature is not None:
    
    while(1) :
        humidity, temprature = Adafruit_DHT.read_retry(sensor, pin)
        print("Temp = {0:0.1f}*C    Humidity = {1:0.1f}%".format(temprature, humidity))
        time.sleep(1)

else :
    print("Failed to get reading")