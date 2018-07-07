from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO
import numpy as np

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]
MAX_DURATION = 10 #5
RECEIVE_PIN = 27

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN)
    cumulative_time = 0
    beginning_time = datetime.now()
    print '**Started recording**'
    while cumulative_time < MAX_DURATION:
        time_delta = datetime.now() - beginning_time
        RECEIVED_SIGNAL[0].append(time_delta)
        RECEIVED_SIGNAL[1].append(GPIO.input(RECEIVE_PIN))
        cumulative_time = time_delta.seconds
    print '**Ended recording**'
    print len(RECEIVED_SIGNAL[0]), 'samples recorded'
    GPIO.cleanup()

    print '**Processing results**'
#    f1=open('f1.txt','w')
#    f2=open('f2.txt','w')

    for i in range(len(RECEIVED_SIGNAL[0])):
        RECEIVED_SIGNAL[0][i] = RECEIVED_SIGNAL[0][i].seconds + RECEIVED_SIGNAL[0][i].microseconds/1000000.0
#	f1.write(RECEIVED_SIGNAL[0][i]);f1.write('\n')
#	f2.write(RECEIVED_SIGNAL[1][i]);f2.write('\n')

    d=np.asarray(RECEIVED_SIGNAL)
    np.savetxt("a_b_c_d_1onoff-rpi.txt",(d[0],d[1]));

    #print '**Plotting results**'
    #pyplot.plot(RECEIVED_SIGNAL[0], RECEIVED_SIGNAL[1])
    #pyplot.axis([0, MAX_DURATION, -1, 2])
    #pyplot.show()
