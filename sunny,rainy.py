weather=(1,0,1,0,0,0,1,1,1,1)
sunny=weather.count(0)
rainy=weather.count(1)
if sunny>rainy:
    print("the weather is sunny")
else:
    print("the weather is rainy")