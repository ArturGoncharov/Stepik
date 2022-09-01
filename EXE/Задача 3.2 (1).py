import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector 
from Autodesk.Revit.DB import BuiltInParameter, WallType

sum_id = 0
p_category = ()
p_parameter = ()

for wall_type in FilteredElementCollector(doc).OfClass(WallType):
    parameter = wall_type.Parameter[BuiltInParameter.ALL_MODEL_TYPE_MARK]
    if parameter:
        sum_id += parameter.Id.IntegerValue
    else:
        p_category = wall_type.Category.Name
        p_parameter = parameter

print '{}, {}, {}'.format(sum_id, p_category, p_parameter)