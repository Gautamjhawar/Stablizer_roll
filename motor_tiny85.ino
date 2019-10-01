#define d 4                           // enable for motor control
#define pwm 1
#define d 5     //motor control 2

void setup() {

  
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
