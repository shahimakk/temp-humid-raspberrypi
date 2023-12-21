#import necessay libraries
import time
import board
import adafruit_dht
import datetime

# Initialization
dhtDevice = adafruit_dht.DHT22(board.D4)



while True:
    try:
        current_time = datetime.datetime.now()        
        # receiving the temperature in degree C
        temp_c = dhtDevice.temperature
        # converting the temperature from degree C to degree fahrenheit
        temp_f = temp_c * (9 / 5) + 32
        # receiving the humidity
        humidity = dhtDevice.humidity
        
        print(current_time,"::: Temp: {:.2f} F / {:.2f} C Humidity:{}% ".format(temp_f, temp_c, humidity))

        #print(current_time,"::::Temp: {:.1f} F / {:.1f} C  Humidity: {}% ".format(temp_f, temp_c, humidity)
        
    except RuntimeError as error:
        # Checking for Errors
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        #exit when exception happens
        dhtDevice.exit()
        raise error
    #wait 1s until next iteration happens
    time.sleep(1.0)

