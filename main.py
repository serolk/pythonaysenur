from Examples import Examples
from Examples import X_Sensor
import random
import time

# def ana():
#     arr = [9,8,7,6,5,4,3,2,1]
#     obj = Examples()
#     obj.myPrintArrayReverse1(arr)
#
#
# ana()
sensorList = []

for i in range (4):
    objSensor = X_Sensor(i + 1, random.randint(-273, -265),random.randint(0,100),random.randint(1500,1700))
    sensorList.append(objSensor)

def myPrint(arr):
    for x in arr:
        x.getValues()

i = 1
while i < 10000:
    print(f'-------------{i}. ÖLÇÜM -------------')
    for obj in sensorList:
        obj.temperature = random.randint(-273, -265)
        obj.pressure = random.randint(0,100)
        obj.lumen = random.randint(1500,1700)
    myPrint(sensorList)
    time.sleep(2)
    i += 1
    #############

    #############


