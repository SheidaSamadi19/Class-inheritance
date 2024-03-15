# Creating Box class ------> Parent Class
class Box:
    def __init__(self, name, height, width, length):
        self.name   =  name
        self.height = height #centimeter
        self.width  = width #centimeter
        self.length = length #centimeter 

# Creating Dice class ------> Child class
class Dice(Box):
    def __init__(self,name,height,width,length, color,surface_numbers):
        super().__init__(name,height,width,length)
        self.color = color
        self.surface = surface_numbers


# Instance: Box 
box_1= Box(name='My box',height=10,width=10,length=10)
dice_1= Dice(name='~~~~~The Fisrt Dice',height=1,width=1,length=1,surface_numbers=[1,2,3,4,5,6],color='red~~~~~')
dice_2= Dice(name='~~~~~~The Second Dice',height=2,width=2,length=2,surface_numbers=[1,2,3,4,5,6],color='blue~~~~~')
dice_3= Dice(name='~~~~~~The Third Dice',height=4,width=4,length=4,surface_numbers=[1,2,3,4,5,6],color='yellow~~~~~~')
dice_4= Dice(name='~~~~~~The Forth Dice',height=3,width=3,length=3,surface_numbers=[1,2,3,4,5,6],color='purple~~~~~~')
dice_5= Dice(name='~~~~~~The Fifth Dice',height=1,width=1,length=1,surface_numbers=[1,2,3,4,5,6],color='green~~~~~~')
dice_6= Dice(name='~~~~~~The Sixth Dice',height=2,width=2,length=2,surface_numbers=[1,2,3,4,5,6],color='black~~~~~~')
dice_7= Dice(name='~~~~~~The Seventh Dice',height=5,width=5,length=5,surface_numbers=[1,2,3,4,5,6],color='white~~~~~~')
dice_8= Dice(name='~~~~~~The Eighth Dice',height=1,width=1,length=1,surface_numbers=[1,2,3,4,5,6],color='pink~~~~~~')
dice_9= Dice(name='~~~~~~The Ninth Dice',height=2,width=2,length=2,surface_numbers=[1,2,3,4,5,6],color='orange~~~~~~')
dice_10= Dice(name='~~~~~~The Tenth Dice',height=3,width=3,length=3,surface_numbers=[1,2,3,4,5,6],color='brown~~~~~~')

# Output
print(box_1.__dict__)

print(dice_1.__dict__)
print(dice_2.__dict__)
print(dice_3.__dict__)
print(dice_4.__dict__)
print(dice_5.__dict__)
print(dice_6.__dict__)
print(dice_7.__dict__)
print(dice_8.__dict__)
print(dice_9.__dict__)
print(dice_10.__dict__)
