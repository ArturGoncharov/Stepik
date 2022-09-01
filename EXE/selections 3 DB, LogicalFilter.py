import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB
from System.Collections.Generic import List

unique_ids = [
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b3',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b4',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b6',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b7',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b9',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8ba',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bc',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bd',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bf'
]

ids = [doc.GetElement(unique_id).Id for unique_id in unique_ids]
ids_typed = List[DB.ElementId](ids)

class_filter_1 = DB.ElementClassFilter(DB.WallType )
class_filter_2 = DB.ElementClassFilter(DB.FloorType )
class_filter_3 = DB.ElementClassFilter(DB.RoofType )
category_filter_1 = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Rooms )
category_filter_2 = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Stairs )
category_filter_3 = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_CurtainWallMullions )

all_filters = [
    class_filter_1,
    class_filter_2,
    class_filter_3,
    category_filter_1,
    category_filter_2,
    category_filter_3
]

all_filters_typed = List[DB.ElementFilter](all_filters)
logical_or_filter = DB.LogicalOrFilter(all_filters_typed)
elements = FEC(doc).WherePasses(logical_or_filter).Excluding(ids_typed)

print sum([element.Id.IntegerValue for element in elements])
print min([element.Id.IntegerValue for element in elements])    # вычислений 
print max([element.Id.IntegerValue for element in elements])