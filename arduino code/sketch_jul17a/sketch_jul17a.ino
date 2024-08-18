//протокол для свзи с комьютером(key(число), data1, data2,...,dataN):
//keys:
//1 - выключить вывод тензодатчика в serial
//2 - включить вывод тензодатчика в serial
//3 - задать новую частоту обновления тензодатчика в serial\
//4 - тарирование тензодатчика
//5 - мотор базы (скорость, макс. скорость, ускорение, количество шагов)
//6 - мотор давящей головки (скорость, макс. скорость ,ускорение, количество шагов)
//7 - надавить(макс. скорость базы ,ускорение базы, скорость возврата, ускорение возврата, требуемое давление)
//8 - включить двигатели(должно выполнятся перед 5,6,7)
//9 - выключить двигатели
//10 - вернуть головку стартовое положение
//11 - задать рабочее положение головки(нужно выяснить количество шагов до рабочего положение)
//12 - вернуть базу 
#include <HX711_ADC.h>
#include <GyverStepper.h>

bool isConnected = false; // Флаг для проверки состояния соединения

bool TenzoFlag = false;
int TenzoUpdateRate = 10;
unsigned long lastUpdateTime = 0;
float currentTenzo = 0;
 
const int HX711_dout = 3; //mcu > HX711 dout pin
const int HX711_sck = 2; //mcu > HX711 sck pin
HX711_ADC LoadCell(HX711_dout, HX711_sck); // Создаем объект LoadCell

GStepper<STEPPER2WIRE> stepper_base(200, 4, 5, 6);
GStepper<STEPPER2WIRE> stepper_head(200, 8, 9, 10);

int current_speed_base = 0;
int current_speed_head = 0;
int max_speed_base = 0;
int max_speed_head = 0;
int acceleration_base = 0;
int acceleration_head = 0;
int base_steps = 0;
int head_steps = 0;

int head_returning_max_speed = 0;
int head_returning_acceleration = 0;

int head_working_pos = 0;

const int minimal_pressure_speed = 1;
int pressure = 0;
bool presure_flag = false;

int32_t head_init_pos = stepper_head.getCurrent();
int32_t base_init_pos = stepper_head.getCurrent();

void setup() {

  stepper_base.disable(); //!!!при выключенном питании двигатели подвижны
  stepper_head.disable();
  stepper_base.setRunMode(FOLLOW_POS);
  stepper_head.setRunMode(FOLLOW_POS);
  
  Serial.begin(115200);
  Serial.setTimeout(10);// Устанавливаем скорость соединения
//    Serial.println();
//  Serial.println("Starting...");
  
  float calibrationValue = 491.25;
  
  LoadCell.begin();
  
  unsigned long stabilizingtime = 2000;
  boolean _tare = true;
  
  LoadCell.start(stabilizingtime, _tare);
  
  if (LoadCell.getTareTimeoutFlag()) {
//    Serial.println("Timeout, check MCU>HX711 wiring and pin designations");
    while (1);
  } else {
    LoadCell.setCalFactor(calibrationValue);
//    Serial.println("Startup is complete");
  }
  
  while (!LoadCell.update());
  
//  Serial.print("Calibration value: ");
//  Serial.println(calibrationValue);
//  Serial.print("HX711 measured conversion time ms: ");
//  Serial.println(LoadCell.getConversionTime());
//  Serial.print("HX711 measured sampling rate HZ: ");
//  Serial.println(LoadCell.getSPS());
//  Serial.print("HX711 measured settlingtime ms: ");
//  Serial.println(LoadCell.getSettlingTime());
  
//  if (LoadCell.getSPS() < 7) {
//    Serial.println("!!Sampling rate is lower than specification, check MCU>HX711 wiring and pin designations");
//  } else if (LoadCell.getSPS() > 100) {
//    Serial.println("!!Sampling rate is higher than specification, check MCU>HX711 wiring and pin designations");
//  }
}



void loop() {
  stepper_head.tick();
  stepper_base.tick();
  if (Serial.available() > 0 && isConnected == false) {
    String received = Serial.readStringUntil('\n'); // Читаем данные до символа новой строки
    received.trim(); // Удаляем пробелы и символы новой строки
    if (received.length() > 0) { // Проверяем, что строка не пустая
      if (received == "connect") {
        Serial.println("connected"); // Отправляем ответ
        isConnected = true; // Устанавливаем флаг соединения
      }
    }
  }

  if (isConnected) {
    
    // Основной код, который выполняется только после получения команды "connect"
    // Например:
    static byte prevAm = 0;
    static uint32_t tmr = 0;
    byte am = Serial.available();
    if (am != prevAm){
      prevAm = am;
      tmr = millis();
      
      } 
    if ((am && millis() - tmr > 10) || am > 60){
      uint32_t us = micros();
      char str[100];
      
      int amount = Serial.readBytesUntil(';', str, 99);
      str[amount] = '\0';

//      while (Serial.available() != 0){
//        Serial.read(); // для того чтобы прочитать ";" если отправить ; в конец строчки
//        }
      
//      Serial.println(str); //для отладки парсинга
    
      int key_elem;
      float data[99];
      int count = 0;
      char* offset = str;
      
      key_elem = atoi(offset); 
      offset = strchr(offset, ',');
      if (offset) offset++;
     
      while(offset && count < 29){
        data[count++] = atoi(offset);
        offset = strchr(offset, ',');
        if (offset) offset++;
        else break;
        }
//      for (int i = 0; i < count; i++) Serial.println(data[i]); //для отладки парсинга
      prevAm = 0; 
      Serial.println(key_elem);

      
      switch(key_elem){
        case 1:
              Serial.println("Tenzo not in serial");
              TenzoFlag = false;
              break;
           
        case 2:
            Serial.println("Tenzo in serial");
            TenzoFlag = true;
            break;
            
       case 3:
            TenzoUpdateRate = data[0];
            break;

       case 4:
            LoadCell.tareNoDelay();
            Serial.println("Tared");
            break;
        
                    
        case 5: 
          Serial.println("five");
          current_speed_base = data[0];
          max_speed_base = data[1];
          acceleration_base = data[2];
          base_steps = static_cast<long>(data[3]);
          stepper_base.setSpeed(current_speed_base);
          stepper_base.setMaxSpeed(max_speed_base);     // скорость движения к цели
          stepper_base.setAcceleration(acceleration_base);
          stepper_base.setTarget(base_steps, RELATIVE);
          
          break;
        case 6: 
          current_speed_head = data[0];
          max_speed_head = data[1];
          acceleration_head = data[2];
          head_steps = static_cast<long>(data[3]);
          stepper_head.setSpeed(current_speed_head);
          stepper_head.setMaxSpeed(max_speed_head);     // скорость движения к цели
          stepper_head.setAcceleration(acceleration_head);
          stepper_head.setTarget(head_steps, RELATIVE);
          
          break;
        case 7: 
         //7 - надавить(макс. скорость базы ,ускорение базы, скорость возврата, ускорение возврата, требуемое давление)
          if (!presure_flag){
            stepper_base.brake();      // перестраховка что база остановится перед движением.
            max_speed_base = data[0];
            acceleration_base = data[1];
            head_returning_max_speed = data[2];
            head_returning_acceleration = data[3];
            pressure = data[4];
            presure_flag = true;
            stepper_head.setMaxSpeed(1500);     
            stepper_head.setAcceleration(1500);
            stepper_head.setTarget(head_working_pos, ABSOLUTE);
            stepper_base.setMaxSpeed(1);//немного костыль, перед движением у двигателя будет минимально возможная скорость
            stepper_base.setAcceleration(1);//немного костыль, перед движением у двигателя будет минимально возможное ускорение
            stepper_base.setTarget(90000000);//немного костыль, двигатель будет крутить до того момента пока на тезодатчике не будет нужное значение
          }
          break;
       
        
        case 8: 
          stepper_base.enable(); //при включенном питании двигатели неподвижны
          stepper_head.enable();
          break;

       case 9:
          stepper_base.disable(); //при выключенном питании двигатели подвижны
          stepper_head.disable();
          break;

       case 10: //вернуть голову в изначальное положение
         stepper_head.setMaxSpeed(1500);     
         stepper_head.setAcceleration(1500);
         stepper_head.setTarget(head_init_pos);
         presure_flag = false;//в любом случае процесс давления прекращается    
         break;

       case 11:
          head_working_pos = static_cast<long>(data[0]);
          stepper_head.setMaxSpeed(1500);     
          stepper_head.setAcceleration(1500);
          stepper_head.setTarget(head_working_pos, ABSOLUTE);
          break; 

       case 15:

          stepper_base.setMaxSpeed(1500);
          stepper_base.setAcceleration(500);
          stepper_base.setTarget(base_init_pos, ABSOLUTE);
          
  }
      

}
      unsigned long currentMillis = millis();
      if (currentMillis - lastUpdateTime >= TenzoUpdateRate) {
        lastUpdateTime = currentMillis;
  
        // Обновляем данные с тензодатчика
        if (LoadCell.update()) {
          float weight = LoadCell.getData();
          if (TenzoFlag){
          Serial.print("Weight: ");
          Serial.println(weight);
          currentTenzo = weight;
          }
        }
      }
      
      if(presure_flag == true){
        static bool returning_to_start = false;
        
        if(!returning_to_start){
          if(currentTenzo <= pressure){
            int current_speed = calculate_speed(pressure,max_speed_head, minimal_pressure_speed);
            stepper_base.setMaxSpeed(current_speed); 
//            stepper_base.setAcceleration(current_speed);
          }
           else{
            returning_to_start = true;
            stepper_base.brake();
            stepper_base.setMaxSpeed(0);
            stepper_base.setAcceleration(0);
            stepper_head.setMaxSpeed(head_returning_max_speed);     // скорость движения к цели
            stepper_head.setAcceleration(head_returning_acceleration);
            stepper_head.setTarget(head_init_pos);
            
            }
//        Serial.println(current_speed_head);
//        Serial.println(max_speed_head);
//        Serial.println(acceleration_head);
//        Serial.println(head_returning_max_speed);
//        Serial.println(head_returning_acceleration);
//        Serial.println(pressure);
          }
        else{
          if (stepper_head.getCurrent() == head_init_pos){
              presure_flag = false;
              returning_to_start = false;              
            }
          else{
               Serial.println("returning...");           
            }
          
          
          }
        
        
        
        }




  }
}

int calculate_speed(int pressure, int max_speed, int min_speed){
      if (pressure != 0){
      return max_speed - (max_speed - min_speed) * (currentTenzo/pressure);
      }
      else{
        return 0;
        }
  }
  
  
     
