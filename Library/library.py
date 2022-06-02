class LeapYear:
    # Created for easier leap year calculation
    
    def __init__(self):
        self.year = int(input("Enter Year to calculate = "))


    def YearCheck(self):
        if self.year % 4 == 0: print("Year is Leap Year.")
        elif self.year % 100 == 0: print("Year is not Leap Year. ")
        elif self.year % 400 == 0: print("Year is Leap Year.")
        else: print("Year is not Leap Year")
# It will check if your year is leap year or not