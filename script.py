class Back_pack:
    def __init__(self,name):
        self.name = name
        self.item = []
     
    def addToBackpack(self, item):
        self.item.append(item)

    def __str__(self):
        return f"{self.name} backpack contains: {','.join(self.item)}"


my_backpack = Back_pack("Stephen")       

items = ["phone","earpiece","waterbottle","charger","foodflask","pencil","ruler","nintendo","calculator","usb"]

for i in items:
    my_backpack.addToBackpack(i)

    print(my_backpack)