import thingspeak
import time
import Adafruit_DHT
 
channel_id = 1765206 # PUT CHANNEL ID HERE
write_key  = 'FUZL8XUHDB0QMYYZ' # PUT YOUR WRITE KEY HERE
read_key   = '88OSAUFU3YOJTAWA' # PUT YOUR READ KEY HERE
pin = 21
sensor = Adafruit_DHT.DHT22
 
def measure(channel):
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        # write
        response = channel.update({'field1': temperature, 'field2': humidity})
        
        # read
        read = channel.get({})
        print("Read:", read)
        
    except:
        print("connection failed")
 
 
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, write_key, read_key)
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(15)