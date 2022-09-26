import random
temperature=(random.random())*100
roundedTemp=round(temperature)
humidity=(random.random())*100
roundedhumid=round(humidity)

print("temperature:",roundedTemp)
print("humidity:",roundedhumid)
if roundedTemp>30:
    print("Detect alarm")
else:
    print("Low temperature")
