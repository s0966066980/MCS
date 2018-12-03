import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPTO.PUD_UP)

while True:

	SwitchStatus = GPIO.input(24)
	if( SwichStatus == 0):
		print('Button pressed')
	else
		print('Button released')

