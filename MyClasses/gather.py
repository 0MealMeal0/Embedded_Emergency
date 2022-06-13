from dht22_to_class import dht22_sensor
from flamesensor_to_class import flame_sensor

dht22 = dht22_sensor()
flame = flame_sensor()

while(true) :
    dht22.run()
    flame.read_flame_sensor()
