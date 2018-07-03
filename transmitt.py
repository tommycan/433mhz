import time
import sys
import os.path
import RPi.GPIO as GPIO

# Remote control signals
signals = "remote_comtrol_signals.py"

# Time Scale (milliseconds)
TS = 1e-3; 

# Pulse length 
PL = 0.25;

# Signal definition
#MID = [[[[0.22,0.06],[2.60,0.05],'S',],
#        [[0.22,0.06],[0.34,0.05],'1'],
#        [[0.22,0.06],[1.35,0.05],'0'],
#        [[0.22,0.06],[10.80,0.05],'P']],66];
MID = [[[[PL,0.06],[10*PL,0.05],'S'],
        [[PL,0.06],[ 1*PL,0.05],'1'],
        [[PL,0.06],[ 5*PL,0.05],'0'],
        [[PL,0.06],[40*PL,0.05],'P']],66];

sync_delay	= TS*MID[0][0][1][0]
up_delay 	= TS*MID[0][0][0][0]
short_delay	= TS*MID[0][1][1][0]
long_delay 	= TS*MID[0][2][1][0]
ext_delay 	= TS*MID[0][3][1][0]

NUM_ATTEMPTS = 6
TRANSMIT_PIN = 17

def transmit_code(code):
   print "code: ", code[1:-1] 
   '''Transmit a chosen code string using the GPIO transmitter'''
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
   for t in range(NUM_ATTEMPTS):
      GPIO.output(TRANSMIT_PIN, 1)
      time.sleep(up_delay)
      GPIO.output(TRANSMIT_PIN, 0)
      time.sleep(sync_delay)
      for i in code:
         if i == '1':
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(up_delay)
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(short_delay)
         elif i == '0':
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(up_delay)
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(long_delay)
         else:
            continue
      GPIO.output(TRANSMIT_PIN, 1)
      time.sleep(up_delay);
      GPIO.output(TRANSMIT_PIN, 0)
      time.sleep(ext_delay)
   GPIO.cleanup()

if __name__ == '__main__':
	if (os.path.isfile(signals)):
		execfile(signals);
		#print "remote_signals detected! "
	if (len(sys.argv) > 1):
		for argument in sys.argv[1:]:
			#print "argument: ", argument
			exec('transmit_code(' + str(argument) + ')')

