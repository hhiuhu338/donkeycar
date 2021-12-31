import RPi.GPIO as GPIO
import time
makerobo=24 #选择18号GPIO引脚
GPIO.setmode(GPIO.BCM)  #设置编码方式
GPIO.setup(makerobo,GPIO.OUT) #把18号口设置为输出口
flag=1
i=0
for t in range(10):
    GPIO.output(makerobo,flag) #在18号口输出电平
    print('t is',t)
    i=i+1
    time.sleep(3)
    if flag==0:
            flag=1
    else:
        flag=0
GPIO.setup(makerobo,GPIO.IN)
