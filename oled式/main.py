import oled
import wifi
import network
import time
import machine



ssid="WUSI-601"
password="wusi01601"

oled.text("connecting WIFI",0,0)
oled.show()
if(wifi.do_connect(ssid,password)):  
    wlan = network.WLAN(network.STA_IF)
    status=wlan.ifconfig()
    oled.fill(0)
    oled.text("conneted",0,0)
    oled.text(status[0],0,8)
    oled.show()
else:
    oled.fill(0)
    oled.text("error",0,0)
    oled.text("not connected",0,8)
    oled.text("check ssid or pa",0,16)
    oled.text("ssword",0,24)         
    oled.show()

time.sleep_ms(1000)
import dht
DHT= dht.DHT11(machine.Pin(12))
while(1):
    DHT.measure()
    oled.fill(0)
    oled.ShowChar40x64(0,0,DHT.temperature()/10)
    oled.ShowChar40x64(20,0,DHT.temperature()%10)
    oled.ShowChar24x24(40,30,0)
    oled.ShowChar40x64(64,0,DHT.humidity()/10)
    oled.ShowChar40x64(84,0,DHT.humidity()%10)
    oled.ShowChar24x24(104,30,1)
    oled.show()
    time.sleep_ms(1000)
    



