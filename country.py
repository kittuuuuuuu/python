class india:
    def capital(self):
        print("capital of indian is delhi")
    def language(self):
        print("language of india is hindi")
class america:
    def capital(self):
        print("capital of america is washington")
    def language(self):
        print("lanaguage of america is english")
a=india()
b=america()
for i in (a,b):
    i.capital()
    i.language()
