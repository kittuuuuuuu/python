class pair_elements:
    def twosum(self,nums,target):
        lookup={}
        for i, num in enumerate(nums):
            if target-num in lookup:
                return(lookup[target-num],i)
            lookup [num]=i
value=int(input("enter the sum for which you want to fimd the indexes"))
object=pair_elements()
print(object.twosum((10,20,30,40,50,60,70),value))



