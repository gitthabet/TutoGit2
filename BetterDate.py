from datetime import datetime
class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    def __repr__(self):
      return "{}-{}-{}".format(self.year,self.month,self.day)
    
    @staticmethod # helper method for internal use 
    def strtoint(strdate):
          year, month, day = map(int, strdate.split("-"))
          return year, month, day

          
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        #parts = datestr.split("-")
        year, month, day = BetterDate.strtoint(datestr)
        #year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return BetterDate(year, month, day)
