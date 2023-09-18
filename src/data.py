from IntR import IntR
from helpers import REPRESENTATIONS, KEYS

# Data contains all the necessary information to perform operations.
# It contains two lists of IntR, each representing a number, x and y
# IntRBase is the base of IntR (which we perform operations on)
# Radix represents the base of the input and output of the program
class Data():
    IntRBase = 0xf

    def __init__(self, radix: int, x: str, y: str):
        self.radix = radix
        self.x = self.strToIntR(self.radix, self.IntRBase, x)
        self.y = self.strToIntR(self.radix, self.IntRBase, y)

    # Returns the index of the most significant bit
    def getIndexMSB(self, num: int) -> int:
        msbIndex = 0

        while num > 0:
            num = num >> 1
            msbIndex = msbIndex + 1

        return msbIndex


    # Not sure if your allowed to convert bases like this in the assingment
    # Note: first element in returned list is least significant digit
    def strToIntR(self, radix: int, IntRBase: int, strNum: str) -> list:
        IntList = list()
        num = 0

        #Convert string to integer
        for i, c in enumerate(reversed(strNum)):
            num = num + KEYS[c] * (radix**i)

        #Convert integer to list of IntR 
        msbIndex = self.getIndexMSB(IntRBase)
        while num > 0:
            IntList.append(IntR(IntRBase, num))
            num = num >> msbIndex

        return IntList

    # Not sure if your allowed to convert bases like this in the assingment
    def IntRtoStr(self, radix: int, IntList: list) -> str:
        msbIndex = self.getIndexMSB(IntList[0].radix())
        num = 0
        outStr = ""

        #Convert list of IntR to integer
        for n in reversed(IntList):
            num = num << msbIndex
            num = num | int(n)

        #Convert integer to string
        while num > 0:
            outStr = REPRESENTATIONS[num % radix] + outStr
            num = num // self.radix

        return outStr

    def getRadix(self) -> int:
        return self.radix
    
    def getX(self) -> list:
        return self.x
    
    def getY(self) -> list:
        return self.y
    
    def getIntRBase(self) -> int:
        return self.IntRBase
    
if __name__ == "__main__":
    d = Data(10, "1234", "583")
    print("x", d.x, "y", d.y)
    print("x", d.IntRtoStr(d.getRadix(), d.x), "y", d.IntRtoStr(d.getRadix(), d.y))