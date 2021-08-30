class Examples:

    def __init__(self):
        print("Ruhu üflendi")

    def myPrint(self, arr2):
        print(arr2)


    def myPrintArrayReverse1(self, arr):
        length = len(arr)
        for i in range(length-1, -1, -1):
            #TO DO :dizinin elemanını ekrana yazdır:
            print(arr[i])
            #TO DO: diziden yazdırdığım elemanı çıkar:
            arr.pop(i)
        self.myPrint(arr)


class X_Sensor:

    #constructor
    def __init__(self, id, sicaklik, basinc, lumen):
        self.temperature = sicaklik
        self.pressure = basinc
        self.lumen = lumen
        self.id = id


    def getValues(self):
        print(f'{self.id}. Sensör Verileri:--------------')
        print(f'Anlık Sıcaklık: {self.temperature}')
        print(f'Anlık Basınç: {self.pressure}')
        print(f'Anlık Işık Şiddeti: {self.lumen}')

    def setValues(self, sicaklik, basinc, lumen):
        self.temperature = sicaklik
        self.pressure = basinc
        self.lumen = lumen