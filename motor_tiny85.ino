#define d 4                           // enable for motor control
#define pwm 1


void setup() {

  Serial.write(9600);
}

void loop() {
       digitalWrite(d,LOW);
      digitalWrite(pwm,HIGH);
      delay(2000);
      digitalWrite(d,LOW);
      digitalWrite(pwm,LOW);
      delay(2000);
      digitalWrite(d,HIGH);
      digitalWrite(pwm,HIGH);
      delay(2000);
}
