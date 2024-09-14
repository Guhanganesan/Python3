

# Python program to  
# demonstrate static methods 
  
class Maths(): 
      
    @staticmethod
    def addNum(num1, num2): 
        return num1 + num2 
          
# Driver's code 
if __name__ == "__main__": 
      
    # Calling method of class 
    # without creating instance 
    res = Maths.addNum(1, 2) 
    print("The result is", res)