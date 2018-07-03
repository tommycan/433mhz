import os
import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib.widgets import Button, RadioButtons
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

# Global variable
SignalType = ''
OutCode = [];

# Time Scale (milliseconds)
TS = 1e-3; 

# Almost zero
EPS= 1e-9;

# Signal patterns
BGN = [[[[0.30,0.06],[2.37,0.05],'S'],
         [[0.30,0.06],[1.23,0.05],'1'],
         [[1.08,0.06],[0.48,0.05],'0']],25];
MID = [[[[0.22,0.06],[2.60,0.05],'S',],
         [[0.22,0.06],[0.34,0.05],'1'],
         [[0.22,0.06],[1.35,0.05],'0'],
         [[0.22,0.06],[10.80,0.05],'P']],66];

END = [[[[0.44,0.06],[7.26,0.05],'S'],
         [[0.44,0.06],[1.63,0.05],'1'],
         [[1.48,0.06],[0.60,0.05],'0']],33];

         
SIGNALS = {'BGN': BGN,
           'MID': MID,
           'END': END}

class doUpdate(object):

    def update(self, event):
        x0, x1 = ax1.get_xlim();
        highLow = getHighLow(getSubset(d_org, [x0,x1]));
        if highLow[0,0] <= EPS:
            highLow = highLow[:,1:]; 
        ax2.clear()
        
        xmin = np.amin(highLow[1][np.where(highLow[1]>EPS)]);
        xmax = np.amax(highLow[1][np.where(highLow[1]>EPS)]);
        ymin = np.amin(highLow[0][np.where(highLow[0]>EPS)]);
        ymax = np.amax(highLow[0][np.where(highLow[0]>EPS)]);
        
        dy = ymax - ymin;
        
        ax2.set_xlim([0.0, xmin+xmax])
        ax2.set_ylim([ymin-0.2*dy, ymax+0.2*dy])
        
        ax2.scatter(highLow[1],highLow[0]);
        ax2.grid();
        
        if SignalType not in SIGNALS:
            print "SignalType not in SIGNALS (update)"
            return
        
        patches = [];
        signal = SIGNALS.get(SignalType);
        for j in np.arange(0, len(signal[0])):
            x = TS*signal[0][j][1][0];
            y = TS*signal[0][j][0][0];
            d = TS*signal[0][j][0][1];
            circle = Circle( (x,y), 0.5*d, alpha=.5);
            patches.append(circle);
            
        p = PatchCollection(patches, alpha=0.5)
        ax2.add_collection(p)

class doDump(object):
            
    def dump(self, event):
        global OutCode;
        ret = '';
        x0, x1 = ax1.get_xlim();
        
        if SignalType not in SIGNALS:
            print "SignalType not in SIGNALS (dump)"
            return
        
        highLow = getHighLow(getSubset(d_org, [x0,x1]))
        if highLow[0,0] <= EPS:
            highLow = highLow[:,1:]; 
        
        signal = SIGNALS.get(SignalType);
        for i in np.arange(0, len(highLow[1])):
            hl = highLow[:,i];
            found = False;
            for j in np.arange(0, len(signal[0])):
                highFound = np.abs(TS*signal[0][j][0][0]-hl[0]) <= TS*signal[0][j][0][1]
                lowFound  = np.abs(TS*signal[0][j][1][0]-hl[1]) <= TS*signal[0][j][1][1]
                if(highFound and lowFound):
                    ret += signal[0][j][2];
                    found = True;
                    break;
            if not found:
                ret += 'X'
        valid1 = len(highLow[0]) == len(ret)
        valid2 = (len(ret) % signal[1]) == 0
        OutCode = [ret, [len(highLow[0]), len(ret), signal[1], valid1 and valid2, SignalType]];
        if OutCode[1][3]:
            splitChar = signal[0][0][2];
            CodeChunks=[splitChar+e for e in OutCode[0].split(splitChar) if e]
            e0 = CodeChunks[0]
            correct = True;
            for i,e in enumerate(CodeChunks):
                if not (e0 == e):
                    correct=False;
                print e
            print OutCode[1]
            if correct:
                print "OutCode validation passed"
            else:
                print "OutCode validation shows bit-errors"
        else:
            print OutCode[0]
            print OutCode[1]
            print "OutCode validation failed."   

def getSubset(iData, iLim):
    return iData[:,np.intersect1d(np.where(iData[0]>=iLim[0]),
                                  np.where(iData[0]<=iLim[1]))]

def getHighLow(iData):
    z0 = [0,0];
    z = [];
    d0 = iData[:,0];
    for i in np.arange(1,len(iData[0])):
       dx = iData[:,i]-d0;
       if(np.abs(dx[1])>0.5):
           if dx[1] > 0:
               z0[1]=dx[0];
               z.append([z0[0],z0[1]]);
           else:
               z0[0]=dx[0];
           d0 = iData[:,i];
    
    return np.transpose(np.asarray(z))

#fin = os.path.dirname(__file__) + "/data/c1on-rpi.txt"
fin = os.path.dirname(__file__) + "/data/a_b_c_d_1onoff-rpi.sample"
lim = [0.0,5.0,-1,2]; # full frame
#lim = [1.4219484973203969, 1.5945218092195486, -1.0, 2.0]
#lim = [1.4,1.8,-1,2]; # four cycles
lim2 = [0.0,0.011,0.00015,0.00030] # 

fig = pyplot.figure(os.path.split(fin)[1]);

d_org = np.asarray(np.loadtxt(fin));
d_red = getSubset(d_org,lim)
onoff = getHighLow(d_red);

ax1 = pyplot.subplot(2,1,1)
l1 = ax1.plot(d_red[0],d_red[1]);
ax1.axis(lim);

ax2 = pyplot.subplot(2,1,2)
l2 = ax2.scatter(onoff[1],onoff[0]);
ax2.grid();
ax2.axis(lim2);

cbUpdate = doUpdate()
axUpdate = pyplot.axes([0.90, 0.20, 0.1, 0.05])
bUpdate = Button(axUpdate, 'Update')
bUpdate.on_clicked(cbUpdate.update)

cbDump = doDump()
axDump = pyplot.axes([0.90, 0.70, 0.1, 0.05])
bDump = Button(axDump, 'Dump')
bDump.on_clicked(cbDump.dump)

rAx = pyplot.axes([0.90, 0.77, 0.1, 0.10])
#radio = RadioButtons(rAx, ('None', 'Fast', 'Slow', 'Strt'))
radio = RadioButtons( rAx, tuple(SIGNALS.keys()) )

def radiofunc(strSignal):
    global SignalType;
    SignalType = strSignal;
    
radio.on_clicked(radiofunc)

pyplot.show()
