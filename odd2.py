from datetime import datetime
import time
import random

odds=[]
i=1
while i<60:
    odds.append(i)
    i+=2
for num in range(5):

    right_this_minute=datetime.today().minute

    if right_this_minute in odds:
        print("Ta minuta wydaje się dość nieparzysta.")
    else:
        print("Minuta parzysta.")
    spanie=random.randint(1,60)

    time.sleep(spanie)