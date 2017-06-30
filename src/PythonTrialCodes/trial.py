from pip._vendor.distlib.compat import raw_input
import os 
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(9,10)
v2 = Vector(5,-2)
print (v1 + v2)
   

listName =[1 , 2, 3, 4, 5, 6 , 7, 8, 9, 10]
listName3 = ['a' , 'b' , 'c' ,'d'] 
listName2 = '::'.join(listName3[-2:])
print(listName[2:])
print(listName2)
print(max(listName))
L = ['spam', 'Spam', 'SPAM!']
print(L[1:])
print(max(L))

# str = raw_input("Enter your input: ");
# print("Received input is : ", str)
# 
# str = input("Enter your input : ")
# print("Received input is: " , str)

os.system("start chrome.exe")
os.system("start eclipse.exe")