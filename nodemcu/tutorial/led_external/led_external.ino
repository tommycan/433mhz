#define LED D1 // Led in NodeMCU at pin GPIO16 (D0).
int i = 0;

void setup() {
pinMode(LED, OUTPUT); // set the digital pin as output.
Serial.begin(115200);//Set the baudrate to 115200,same as the software settings
}

void loop() {
digitalWrite(LED, HIGH);
Serial.printf("on ... ", i);
delay(1000);

digitalWrite(LED, LOW);
Serial.printf("off %d\n", i++);
delay(1000);
}
