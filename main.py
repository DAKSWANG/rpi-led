# -*- coding:utf-8 -*-
#讓紅色及綠色LED各閃10次，每次間隔0.5秒
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#設定LED pin變數
LED0    = 7   
LED1    = 11
counter = 0

#設定為輸出
GPIO.setup(LED0,GPIO.OUT)
GPIO.setup(LED1,GPIO.OUT)

#迴圈10次
while(counter < 10):
        GPIO.output(LED0,GPIO.HIGH)
        GPIO.output(LED1,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED0,GPIO.LOW)
        GPIO.output(LED1,GPIO.HIGH)
        time.sleep(0.5)
        counter = counter + 1
GPIO.output(LED0,GPIO.LOW)
GPIO.output(LED1,GPIO.LOW)