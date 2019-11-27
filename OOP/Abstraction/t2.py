#hIERARCHIAL INHERITANCE
class RBI:
    name="Reserve Bank of India"
    def provideLoan(self):
        print("Loan limit is 50 lk")

rbi = RBI()
#print(rbi.name)
#rbi.provideLoan()

class SBI:
    def test(self):
        print("test")
     def provideLoan(self):
        print("Loan limit is 50 lk")

sbi = SBI()
sbi.provideLoan(10,20)
#multiple inheritance 
class MyBank(RBI,SBI):

    def test1(self):
        pass

branch = SbiBranch()
branch.provideLoan()
branch.test()
branch.test1()


