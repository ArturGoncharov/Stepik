import clr
clr.AddReference('RevitApi')
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import ElementCategoryFilter, BuiltInCategory, ElementIsElementTypeFilter

filter=ElementIsElementTypeFilter(True)
elements=FEC(doc).OfCategory(BuiltInCategory.OST_Walls).WherePasses(filter)

bprint(elements)

