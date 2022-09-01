import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB
from System.Collections.Generic import List


all_filters = List[DB.ElementFilter]([
DB.ElementCategoryFilter(DB.BuiltInCategory.OST_RoomTags),
DB.ElementCategoryFilter(DB.BuiltInCategory.OST_DoorTags),
DB.ElementCategoryFilter(DB.BuiltInCategory.OST_WindowTags),
DB.ElementCategoryFilter(DB.BuiltInCategory.OST_WallTags),
])

all_filters_typed = List[DB.ElementFilter](all_filters)

logical_or_filter = DB.LogicalOrFilter(all_filters_typed)

print \
sum([element.Id.IntegerValue for element in FEC(doc, ElementId(695)).WherePasses(logical_or_filter)]) + \
sum([element.Id.IntegerValue for element in FEC(doc, ElementId(136343)).WherePasses(logical_or_filter)])
