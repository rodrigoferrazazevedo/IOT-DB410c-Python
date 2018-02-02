import mraa
import time


sensor = mraa.Gpio(23) #D1
sensor.dir(mraa.DIR_IN)


while True:

	porta_status = sensor.read() 
	
	if porta_status == 0:
		print ("Touch liberado / Sensor = ") + str(porta_status)
	else:
		print ("Touch pressionado / Sensor = ") + str(porta_status)
                     
	time.sleep(5)
	
