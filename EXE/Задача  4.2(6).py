import clr
clr.AddReference('RevitApi')
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import *
from Autodesk.Revit import DB
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc=DocumentManager.Instance.CurrentDBDocument
uiapp=DocumentManager.Instance.CurrentUIApplication
uidoc=DocumentManager.Instance.CurrentUIDocument
app=uiapp.Application

from System.Text import StringBuilder
from System.Collections.Generic import List


def to_list(element, list_type=None):
    if not hasattr(element, '__iter__') or isinstance(element, dict):
        element = [element]
    if list_type is not None:
        if isinstance(element, List[list_type]):
            return element
        if all(isinstance(item, list_type) for item in element):
            typed_list = List[list_type]()
            for item in element:
                typed_list.Add(item)
            return typed_list
    return element

class Unit(object):
    def __init__(self, doc, value, is_display=True,
                unit_type=UnitType.UT_Length):
        self._doc = doc
        self._unit_type = unit_type
        self._internal_value = self._convert_value(value, is_display) \
            if is_display else value
    # другие методы

    def _convert_value(self, value, to_internal):
        conversion_method = DB.UnitUtils.ConvertToInternalUnits \
            if to_internal else DB.UnitUtils.ConvertFromInternalUnits
        return conversion_method(value, self.display_units)

    @property
    def display_units(self):
        '''Единицы измерения, отображаемые в интерфейсе Revit
        (константа перечисления DisplayUnitType)'''
        return self._doc.GetUnits().GetFormatOptions(self._unit_type) \
            .DisplayUnits

    @property
    def unit_type(self):
        '''Тип единиц (константа перечисления UnitType)'''
        return self._unit_type

    @property
    def display_units(self):
        '''Единицы измерения, отображаемые в интерфейсе Revit
        (константа перечисления DisplayUnitType)'''
        return self._doc.GetUnits().GetFormatOptions(self._unit_type) \
            .DisplayUnits

    @property
    def internal(self):
        '''Числовое значение во внутренних единицах Revit'''
        return self._internal_value

    @property
    def display(self):
        '''Числовое значение в единицах интерфейса Revit'''
        return self._convert_value(self._internal_value, False)

parameter_ids = {
    'thickness': ElementId(BuiltInParameter.WALL_ATTR_WIDTH_PARAM),
    'height': ElementId(BuiltInParameter.CURVE_ELEM_LENGTH),
    'square': ElementId(BuiltInParameter.HOST_AREA_COMPUTED),
    'name': ElementId(BuiltInParameter.ALL_MODEL_TYPE_NAME),
}

category_rule_w=FilterCategoryRule(to_list
(ElementId(BuiltInCategory.OST_Walls), 
ElementId))

category_rule_cw=FilterCategoryRule(to_list
(ElementId(BuiltInCategory.OST_CurtainWallPanels), 
ElementId))

# значение параметра "Толщина" больше или равно 90 мм
thickness_greateror_equal_rule = FilterDoubleRule(
    ParameterValueProvider(parameter_ids['thickness']),
    FilterNumericGreaterOrEqual(),
    Unit(doc, 90).internal,
    0
)

# значение параметра "Высота" больше 200 мм
height_greater_rule = ParameterFilterRuleFactory.CreateGreaterRule(
    parameter_ids['height'],
    Unit(doc, 200).internal,
    0
)
# значение параметра "Площадь" больше 0.01
square_greater_rule = ParameterFilterRuleFactory.CreateGreaterRule(
    parameter_ids['square'],
    Unit(doc, 0.01, UnitType.UT_Area).internal,
    0
)

# значение параметра "Площадь" меньше 190 м2
square_less_rule = ParameterFilterRuleFactory.CreateLessRule(
    parameter_ids['square'],
    Unit(doc, 190, UnitType.UT_Area).internal,
    0
)

# значение параметра "Площадь" не равно 0.08 м2
square_not_equal_rule = ParameterFilterRuleFactory.CreateNotEqualsRule(
    parameter_ids['square'],
    Unit(doc, 0.08, UnitType.UT_Area).internal,
    0
)
# значение параметра "Имя типа" не содержит символ "Empty"
name_not_contains_rule = ParameterFilterRuleFactory.CreateNotContainsRule(
    parameter_ids['name'],
    'Empty',
    False
)


or_rule_set=LogicalOrFilter(
    ElementParameterFilter(square_less_rule),
    ElementParameterFilter(height_greater_rule)
)

elements = FEC(doc) \
    .WhereElementIsNotElementType() \
    .WherePasses(
        ElementMulticategoryFilter(
            to_list(
                [
                    BuiltInCategory.OST_Walls,
                    BuiltInCategory.OST_CurtainWallPanels
                ],
                BuiltInCategory
            )
        )
)

TransactionManager.Instance.EnsureInTransaction(doc)
ParameterFilterElement.Create(
        doc,
        'Test Filerwerwertdsdsder',
        to_list(
            [
                ElementId(b_category)
                for b_category in [
                    BuiltInCategory.OST_Walls,
                    BuiltInCategory.OST_CurtainWallPanels,
                ]
            ],
            ElementId
        ),
        or_rule_set
    )
TransactionManager.Instance.TransactionTaskDone()
OUT='ok'