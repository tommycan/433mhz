int i = 0;

void setup()
{
Serial.begin(115200);//Set the baudrate to 115200,same as the software settings
}

void loop()
{
Serial.printf("Hello World %d\n", i++);//Print character string“Hello World！”on the serial
delay(1000);// Delay 5 second
//i++;
}
