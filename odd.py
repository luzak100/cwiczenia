from datetime import datetime

odds=[]
i=1
while i<60:
    odds.append(i)
    i+=2
right_this_minute=datetime.today().minute

if right_this_minute in odds:
    print("Ta minuta wydaje się dość nieparzysta.")
else:
        print("Minuta parzysta.")
print(odds)