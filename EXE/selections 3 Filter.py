import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import  ElementCategoryFilter, BuiltInCategory

filter=ElementCategoryFilter(BuiltInCategory.OST_Walls)
elements = FEC(doc).WherePasses(filter)

bprint(elements)