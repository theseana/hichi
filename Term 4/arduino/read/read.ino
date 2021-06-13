int r = 9;
int g = 10;
int b = 11;
void setup() {
  Serial.begin(9600);
  pinMode(r, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(b, OUTPUT);

}

void loop() {
 RGB(r);
// RGB(g);
// RGB(b);
}

void RGB(int a){
for (int i=0; i<256; i++){
  analogWrite(a, i);
//  analogWrite(10, i);
  analogWrite(11, i);
  Serial.println(i);
  delay(20);
  }  
for (int i=255; i>-1; i--){
  analogWrite(a, i);
//  analogWrite(10, i);
  analogWrite(11, i);
  Serial.println(i);
  delay(20);
  }   
}
