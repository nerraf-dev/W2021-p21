from datetime import datetime

times = ["08:00",	"09:00",	"10:00",	"11:00",	"12:00",	"13:00",	"14:00",	"15:00",	"16:00",	"17:00"]

def generateSchedule():
  class Court:
    def __init__(self):
      # array = [time, availability, name, tel, code]
      self.schedule = [["08:00","available","","",""],
              ["09:00","available","","",""],
              ["10:00","available","","",""],
              ["11:00","available","","",""],
              ["12:00","available","","",""],
              ["13:00","available","","",""],
              ["14:00","available","","",""],
              ["15:00","available","","",""],
              ["16:00","available","","",""],
              ["17:00","available","","",""]
             ]
  courts = []
  for i in range(7):
    c = Court()
    courts.append(c.schedule)
  return courts

class Date:
  def __init__(self,dateTime):
    self.date = dateTime
    self.day = dateTime.strftime("%A")   #Get full day as string
    self.dayNum = dateTime.strftime("%w") #Get day as number
    self.hour = dateTime.strftime("%H")
    self.minute = dateTime.strftime("%M")
    


date = Date(datetime.now())
courts = generateSchedule()
  
while True:
  print("""
****  Welcome to BSM Holiday Park ****
 --- SQUASH COURT BOOKING SYSTEM ---
""")
  print(f"Today is {date.day}. Current Time: {int(date.hour)+2}:{date.minute}")
  print("To make a booking enter 'B'")
  command = input(">> ").upper()
  if command == "QUIT":
    break
  elif command == "ADMIN":
    print("*** ADMIN ***")
    command = input(">> ").upper()
    if command == "QUIT":
      break
  elif command == "B":
    print(f"{courts[0][0]}")

    # c = 0
    # for i in courts:
    #   print(f"day: {c} - {i}")
    #   print("--------------")
    #   c+=1