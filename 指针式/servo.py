import time
import machine

Servo1_pin_no = 5
Servo2_pin_no = 4
duty_angle0 = 30
duty_angle180 = 140
 
Servo1 = machine.PWM(machine.Pin(Servo1_pin_no), freq=50)
Servo2 = machine.PWM(machine.Pin(Servo2_pin_no), freq=50)

def turn(angle,servo):
    assert angle>=0 and angle <=180
    d = duty_angle0 + angle*(duty_angle180-duty_angle0)/180
    servo.duty(int(d))

def turn_test(angle):
    assert angle>=0 and angle <=180
    d = duty_angle0 + angle*(duty_angle180-duty_angle0)/180
    Servo1.duty(int(d))
    Servo2.duty(int(d))

import dht
DHT = dht.DHT11(machine.Pin(12))

def start():
    temp_tem=0
    temp_hum=0
    while(1):
        DHT.measure()
        if(temp_tem!=int(DHT.temperature())):
            turn(int(180-DHT.temperature()*3.6),Servo1)
            temp_tem=int(DHT.temperature())
        if(temp_hum!=int(DHT.humidity())):
            turn(int(180-DHT.humidity()*1.8),Servo2)
            temp_hum=int(DHT.humidity())
        print("当前温度：%f摄制度"%DHT.temperature())
        print("当前湿度度：%f%%"%DHT.humidity())
        time.sleep_ms(1000)
