import serial    
#import MySQLdb   

port = serial.Serial("/dev/ttyACM0", "9600")


#db = MySQLdb.connect("localhost", "root", "004494", "project")
#curs = db.cursor()

while True:
        try:
            data = port.readline() 
            port
            #print("Fire: ")
            print(data)
            #print(type(data))
            
            #curs.execute("""INSERT INTO fire (fire) VALUES (%s)""",(data, ))
            #db.commit()

        except KeyboardInterrupt:
                break

#port.close()
#db.close()