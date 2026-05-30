class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("blu",10)
wuu=parrot("woo",12)
print("blu is {}".format(blu.species))
print("woo is {}".format(wuu.species))
print("{}is {}years old".format(wuu.name,wuu.age))
print("{}is {}years old".format(blu.name,blu.age))
      
    