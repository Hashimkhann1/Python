import time

timestemp = time.strftime("%H : %M : %S : %p")
print("Your Local Time is:",timestemp)

timestempHour = int(time.strftime("%H"))
pmAm = time.strftime("%p")
if(timestempHour >= 6 and timestempHour <= 10 and pmAm == "AM"):
    print("************************ Good morning ************************")
else:
    print("Good Night")
