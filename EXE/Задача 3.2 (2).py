import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import BuiltInCategory
from System.Enum import GetValues
from Autodesk.Revit.DB import FilteredElementCollector as FEC


lst_id = [-1010103, -1010109, -1010108]
element_types = FEC(doc).OfClass(ElementType)
a=0
for element_type in element_types:
	for param in element_type.Parameters:
		if param.Id.IntegerValue in lst_id:
			a += 1
print a