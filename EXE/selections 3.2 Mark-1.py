import clr
clr.AddReference('RevitAPI')

element=selection[0]
mark=element.LookupParameter('Марка') #получить одну марку

bprint(mark)