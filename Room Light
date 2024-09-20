#include <Servo.h>
#include <Time.h>
#include <TimeLib.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // Set the LCD address to 0x27 for a 16 chars and 2 line display

Servo myservo;  // create servo object to control a servo

int potpin = 0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
  setTime(22,11,25,20,9,24);  
  lcd.init();  // Initialize the LCD
  lcd.backlight();  // Turn on the backlight (if supported)
  lcd.setCursor(2, 0);  // Set cursor to beginning of first line
  lcd.print("Hello World");
  delay(500);
  lcd.clear();
}

void loop() {
  val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
  val = map(val, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  myservo.write(val);                  // sets the servo position according to the scaled value
  delay(15);
  digitalClockDisplay();  
}



void digitalClockDisplay()
{
  // Clear the LCD before printing the time
  lcd.clear();

  // Set the cursor to the first line, first position
  lcd.setCursor(0, 0);

  // Format the time as HH:MM:SS
  lcd.print(hour());
  printDigitsToLCD(minute());
  printDigitsToLCD(second());

  // Set the cursor to the second line
  lcd.setCursor(0, 1);

  // Format the date as DD/MM/YYYY
  lcd.print(day());
  lcd.print("/");
  lcd.print(month());
  lcd.print("/");
  lcd.print(year());




  Serial.print(hour());
  printDigits(minute());
  printDigits(second());
  Serial.print(" ");
  Serial.print(day());
  Serial.print(" ");
  Serial.print(month());
  Serial.print(" ");
  Serial.print(year());
  Serial.println(); 
  delay(1000);
}


void printDigitsToLCD(int digits)
{
  lcd.print(":");
  if (digits < 10) 
    lcd.print('0');  // Add a leading zero if the value is less than 10
  lcd.print(digits);
}


void printDigits(int digits)
{
  Serial.print(":");
  if(digits < 10)
    Serial.print('0');
  Serial.print(digits);  
}
