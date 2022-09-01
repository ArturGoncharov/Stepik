# snippet 2
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit import DB
from Autodesk.Revit.UI import TaskDialog, Selection


def get_built_in_category_by_id(id):
    for b_category in DB.BuiltInCategory.GetValues(DB.BuiltInCategory):
        if int(b_category) == id:
            return b_category


def get_parameter_value_v1(parameter):
    if isinstance(parameter, DB.Parameter):
        storage_type = parameter.StorageType
        if storage_type == DB.StorageType.Integer:
            return parameter.AsInteger()
        elif storage_type == DB.StorageType.Double:
            return DB.UnitUtils.ConvertFromInternalUnits(
                parameter.AsDouble(), parameter.DisplayUnitType)
        elif storage_type == DB.StorageType.String:
            return parameter.AsString()
        elif storage_type == DB.StorageType.ElementId:
            return parameter.AsElementId()


class RoomSelectionFilter(Selection.ISelectionFilter):
    def AllowElement(self, element):
        return get_built_in_category_by_id(
            element.Category.Id.IntegerValue) == DB.BuiltInCategory.OST_Rooms


def pick_rooms():
    references = uidoc.Selection.PickObjects(
        Selection.ObjectType.Element, RoomSelectionFilter(),
        'Выделите помещения')
    return [doc.GetElement(reference)
            for reference in references]


def show_rooms_area(rooms):
    area_sum = sum([get_parameter_value_v1(
        room.Parameter[DB.BuiltInParameter.ROOM_AREA])
        for room in rooms])
    area_sum_round = int(round(area_sum))
    dialog = TaskDialog('BIM Planet No2')
    dialog.MainInstruction = 'Выбрано {} помещений общей площадью {} м2' \
                            .format(len(rooms), area_sum_round)
    dialog.Show()
    print area_sum_round


show_rooms_area(pick_rooms())