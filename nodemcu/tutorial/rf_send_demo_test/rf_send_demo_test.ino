/*
  Example for different sending methods
  
  https://github.com/sui77/rc-switch/
  
*/

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

void setup() {

  Serial.begin(115200);
  
  // Transmitter is connected to Arduino Pin D1 = GPIO5 
  mySwitch.enableTransmit(5);
  mySwitch.setProtocol(8);
  mySwitch.setRepeatTransmit(6);

  
  // doVariation();
  doSend();
}

void doVariation() {

int high = 240;
// for (high=200; high<=280; high = high + 10) {

int sync = 2570;  
//for (sync=1570; sync<=3370; sync = sync + 200) {

int one = 300;  
//for (one=100; one<=1000; one = one + 100) {

int zero = 1310;  
//for (zero=600; zero<=2000; zero = zero + 100) {

int pause = 10760;  
for (pause=1000; pause<=20000; pause = pause + 1000) {


    mySwitch.protocol.pulseLength = 1;
    
    mySwitch.protocol.syncFactor.high = high;
    mySwitch.protocol.syncFactor.low  = sync;
    
    mySwitch.protocol.one.high = high;
    mySwitch.protocol.one.low  = one;

    mySwitch.protocol.zero.high = high;
    mySwitch.protocol.zero.low  = zero;

    mySwitch.protocol.pauseFactor.high = high;
    mySwitch.protocol.pauseFactor.low  = pause;

    //Serial.printf("\n%d (%d) ", high, mySwitch.protocol.syncFactor.high);
    //Serial.printf("\n%d (%d) ", sync, mySwitch.protocol.syncFactor.low);
    //Serial.printf("\n%d (%d) ", one, mySwitch.protocol.one.low);
    //Serial.printf("\n%d (%d) ", zero, mySwitch.protocol.zero.low);
    Serial.printf("\n%d (%d) ", pause, mySwitch.protocol.pauseFactor.low);

    doSend();

    delay(100);
  }

}

void doSend() {

//  Serial.printf("Send ");

//  // a1
//  Serial.printf(" a1 ");
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110101001P");
//  delay(500);  
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010101001P");
//  delay(500);


  // b1
  Serial.printf(" b1 ");
  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110100110P");
  //delay(500);  
  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010100110P");
  //delay(500);

  // c1
  Serial.printf(" c1 ");
  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110100101P");
  //delay(500);  
  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010100101P");
  //delay(500);

//  // d1
//  Serial.printf(" d1 ");
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110011010P");
//  delay(500);  
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010011010P");
//  delay(500);

//  Serial.printf(" done.\n");

}

void loop() {

//  Serial.printf("Send ");

//  // a1
//  Serial.printf(" a1 ");
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110101001P");
//  delay(500);  
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010101001P");
//  delay(500);

//  // b1
//  Serial.printf(" b1 ");
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110100110P");
//  delay(500);  
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010100110P");
//  delay(500);
//
  // c1
  Serial.printf(" c1 ");
  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110100101P");
//  delay(500);  
  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010100101P");
//  delay(500);

//  // d1
//  Serial.printf(" d1 ");
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110011010P");
//  delay(500);  
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010011010P");
//  delay(500);

//  Serial.printf(" done.\n");

}
