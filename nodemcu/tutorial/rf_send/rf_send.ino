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
  mySwitch.setProtocol(1);
  
  doSend();
}

void doSend() {

  Serial.printf("Send ");

  // a1
  Serial.printf(" a1 ");
  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110101001P");
  delay(100);  
  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010101001P");
  delay(100);

  // b1
  Serial.printf(" b1 ");
  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110100110P");
  delay(100);  
  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010100110P");
  delay(100);

//  // c1
//  Serial.printf(" c1 ");
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110100101P");
//  //delay(500);  
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010100101P");
//  //delay(500);
//
//  // d1
//  Serial.printf(" d1 ");
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010100110011010P");
//  delay(500);  
//  mySwitch.send("S1010011001010110010110010110100110101010101010101010101010011010P");
//  delay(500);

  Serial.printf(" done.\n");

}

void loop() {
  
  //doSend();

}
