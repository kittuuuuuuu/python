class vechile:
    def __init__(self,busname,maxspeed,milage):
        self.busname=busname
        self.maxspeed=maxspeed
        self.milage=milage
class bus(vechile):
    pass
school_bus=bus('school volvo',120,12)
print(school_bus.busname,school_bus.maxspeed,school_bus.milage)