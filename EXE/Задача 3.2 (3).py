import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import BuiltInCategory
from Autodesk.Revit.DB import FilteredElementCollector as FEC


elements=FEC(doc).OfCategory(DB.BuiltInCategory.OST_StructuralColumns).WhereElementIsNotElementType()
columns=[]
for element in elements:
	type=element.Name
	if '300' in type:
		columns.append(element)
sum=0
for i in columns:
    base_level = i.LookupParameter('Базовый уровень').AsElementId().IntegerValue
    up_level = i.LookupParameter('Верхний уровень').AsElementId().IntegerValue
    sum += (base_level + up_level)

bprint(sum)
