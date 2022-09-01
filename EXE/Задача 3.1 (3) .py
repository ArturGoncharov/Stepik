import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit import DB
from System.Collections.Generic import List
unique_ids=[
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b3',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b4',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b6',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b7',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8b9',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8ba',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bc',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bd',
    '07ae6064-8e02-489e-896d-f7554545ebb2-0002d8bf']

ids = [doc.GetElement(unique_id).Id for unique_id in unique_ids]
ids_typed = List[DB.ElementId](ids) #создание типизированного списка

filter_1=DB.ElementClassFilter(DB.WallType)
filter_2=DB.ElementClassFilter(DB.FloorType)
filter_3=DB.ElementClassFilter(DB.RoofType)

filter_4=DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Rooms)
filter_5=DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Stairs)
filter_6=DB.ElementCategoryFilter(DB.BuiltInCategory.OST_CurtainWallMullions)

all_filter=[filter_1, filter_2, filter_3, filter_4, filter_5, filter_6]

all_filter_typed=List[ElementFilter](all_filter) #создание типизированного списка
result_filter=DB.LogicalOrFilter(all_filter_typed)

elements=FEC(doc).WherePasses(result_filter).Excluding(ids_typed)

print sum([element.Id.IntegerValue for element in elements])