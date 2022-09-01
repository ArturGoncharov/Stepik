import clr
clr.AddReference('RevitAPI')

element=selection[0]
mark=element.GetParameters('Марка') #получить две марки

bprint(mark)