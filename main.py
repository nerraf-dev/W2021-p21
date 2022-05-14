from datetime import datetime as dt 

times = ["08:00",	"09:00",	"10:00",	"11:00",	"12:00",	"13:00",	"14:00",	"15:00",	"16:00",	"17:00"]

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
for i in range(0,8):
  c = Court()
  courts.append(c.schedule)
  # print(courts[i])
  # courts[i] = c.schedule

while True:
  date = dt.now()
  day = date.strftime("%A")   #Get day as string
  hour = date.strftime("%H")
  minute = date.strftime("%M")
  time = f"{hour}:{minute}" 

  court1 = Court()
  court2 = Court()

  court1.schedule[0][1] = "Unavailable"

  

  print("""
****  Welcome to BSM Holiday Park ****
 --- SQUASH COURT BOOKING SYSTEM ---
""")
  print(f"Today is {day}. Current Time: {time}")
  
  command = input(">> ").upper()
  if command == "QUIT":
    break
  else:
    # print(f"Available)
    # for item in schedule:
    #   print(item)
    # print(court1.schedule[0])
    # print(court2.schedule[0])
    print(f"{courts[0][0]}")
    
