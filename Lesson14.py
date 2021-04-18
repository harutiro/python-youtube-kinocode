class Student:
    def __init__(self,name):
        self.name = name
    
    def calculate_ave(self,date):
        sum = 0

        for num in date:
            sum += num

        avg = sum / len(date)
        return avg
    
    def jedge (self,avg):

        if(avg >= 60):
            result = "passed"
        else:
            result = "failed"
        return result

a001 = Student("sato")
date = [70,70,70,70,70]
avg = a001.calculate_ave(date)
result = a001.jedge(avg)

print(avg)
print(a001.name + " " + result)