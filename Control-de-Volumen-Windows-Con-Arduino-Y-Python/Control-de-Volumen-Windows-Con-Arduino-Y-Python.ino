/*
  Impresionante! Controla el Volumen de tu PC con Arduino y Python
  -https://youtu.be/Wdsm14S0hoU?si=b19tOnaZ1tPAPT4C-


  Requisitos:
  INTALAR python con pip 

  Librerias:
  pip install serial
  pip install pycaw
*/

int const potPin = A0;
int potVal;
int vol;


void setup() {
  Serial.begin(9600);
}

void loop() {
  potVal = analogRead(potPin);
  //vol = map(potVal, 0, 1023, 61, 0);//audio
  vol = map(potVal, 0, 1023, 100, 0);//Brillo
  Serial.println(vol);
  delay(100);

}
      