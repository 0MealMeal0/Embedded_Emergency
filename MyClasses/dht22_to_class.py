import http.client, urllib
import urllib.parse
import time
import Adafruit_DHT


KEY = 'FUZL8XUHDB0QMYYZ'
temp_headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
humid_headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
DEBUG = True

sensor = Adafruit_DHT.DHT22
pin = 21

class dht22_sensor : 


    def read_temp():
        if DEBUG:
            print("reading temp")
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        return int(temperature)
    
    def read_humid():
        if DEBUG:
            print("reading humid")
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        return int(humidity)#, print(humidity), humidity print success

    def run(self):
             
        #temp part start
        temp = read_temp() #tempature
        temp_params = urllib.parse.urlencode({"field1": temp, "key": KEY})
        temp_conn = http.client.HTTPConnection("api.thingspeak.com:80")
        
        try:
            temp_conn.request("POST", "/update", temp_params, temp_headers)
            temp_response = temp_conn.getresponse()
            
            if DEBUG:
                print (temp_response.status, temp_response.reason)
            
            temp_data = temp_response.read()
            temp_conn.close()
            
        except:
            print("Connection failed")
        #temp part end            
        
        #humidity part Start
        humid = read_humid() #hmumidity
        humid_params = urllib.parse.urlencode({"field2": humid, "key": KEY})    
        humid_conn = http.client.HTTPConnection("api.thingspeak.com:80")
        
        try:
            
            humid_conn.request("POST", "/update", humid_params, humid_headers)
            humid_response = humid_conn.getresponse()
            
            if DEBUG :
                print (humid_response.status, humid_response.reason)
            
            humid_data = humid_response.read()        
            humid_response.close()
        
        except:
            print("Connection failed")
        #humidity part Start
