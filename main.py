from datetime import datetime
import calendar

times = ["08:00",	"09:00",	"10:00",	"11:00",	"12:00",	"13:00",	"14:00",	"15:00",	"16:00",	"17:00"]

def generateSchedule(day):
  class Court:
    def __init__(self, n, day):
      self.day = day
      # array = [time, availability, name, tel, code]
      self.schedule = [["08:00","Y","","",""],
              ["09:00","Y","","",""],
              ["10:00","Y","","",""],
              ["11:00","Y","","",""],
              ["12:00","Y","","",""],
              ["13:00","Y","","",""],
              ["14:00","Y","","",""],
              ["15:00","Y","","",""],
              ["16:00","Y","","",""],
              ["17:00","Y","","",""]
             ]
  courts = {}
  #Create a new court record with an array for the hourly schedule
  #Each court object with the schedule array is stored in a dictionary. 
  #The day name is used as the key.
  for d in ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]:  #Alt - list(calendar.day_name)
  for n in range(8):
    c = Court(n, day)
    courts[d] = c.schedule
  return courts

#MAKE BOOKING FUNCTION
def MakeBooking():
  time = f"{hour}:00"
  print("** AVAILABLE TIMES **")
  for i in courts[day]:
    if i[1] == "Y":
      # print(f"{day.upper()}: {i}")
      print(f"{i[0]}")
  
  

# *** Setup ***
# date = datetime.now()
# TESTING: Set the date to Monday 9th May 2020 08:05:23
date = datetime(2022, 5, 9, 8,5,23)

#Split time data
day = date.strftime("%A")   #Get full day as string
dayNum = date.strftime("%w") #Get day as number
hour = date.strftime("%H")
minute = date.strftime("%M")

#Setup the court schedule arrays
courts = generateSchedule(day)

# MAIN
while True:
  print("""
****  Welcome to BSM Holiday Park ****
 --- SQUASH COURT BOOKING SYSTEM ---
""")
  print(f"Today is {day}. Current Time: {hour}:{minute}")
  if int(hour) > 17:
    print("Sorry the courts are closed.\nCome back tomorrow.")
    input()
  else:
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
      # print(courts)
      # print(courts.keys())
      print(f"{courts[day][0]}")
      
      MakeBooking()

      

      