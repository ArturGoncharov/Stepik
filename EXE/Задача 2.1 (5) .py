import clr
clr.AddReference('RevitApi')
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import FamilyInstance, BuiltInCategory, ElementCategoryFilter

count = []
for el in globals().values():
    if hasattr(el, 'WorksetId') and not hasattr(el, 'Number'):
		count.append(el)
print len(count)