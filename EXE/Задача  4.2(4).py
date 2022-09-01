import clr
clr.AddReference('RevitApi')
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc=DocumentManager.Instance.CurrentDBDocument
uiapp=DocumentManager.Instance.CurrentUIApplication
uidoc=DocumentManager.Instance.CurrentUIDocument
app=uiapp.Application

from System.Text import StringBuilder
from System.Collections.Generic import List
import sys

class Unit(object):
    def __init__(self, doc, value, is_display=True,
                unit_type=UnitType.UT_Length):
        self._doc = doc
        self._unit_type = unit_type
        self._internal_value = self._convert_value(value, is_display) \
            if is_display else value

    def _convert_value(self, value, to_internal):
        conversion_method = UnitUtils.ConvertToInternalUnits \
            if to_internal else UnitUtils.ConvertFromInternalUnits
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

def get_view_family_type(doc, view_family, type_name=None):
    for view_family_type in FEC(doc).OfClass(ViewFamilyType):
        if all(
                (
                    view_family_type.ViewFamily==view_family,
                    type_name is None or view_family_type
                    .Parameter[BuiltInParameter.SYMBOL_NAME_PARAM]
                    .AsString()==type_name
                )):
            return view_family_type

view_family_type=get_view_family_type(
    doc,
    ViewFamily.Section,
    'Building Section'
)

section_box=BoundingBoxXYZ()
section_box.Min=XYZ(
    Unit(doc,-22000).internal,
    Unit(doc,-20000).internal,
    Unit(doc,-2000).internal
)
section_box.Max=XYZ(
    Unit(doc,-10000).internal,
    Unit(doc,-3000).internal,
    Unit(doc, 10000).internal
)
transform=section_box.Transform
section_box.Transform=transform
section_box.Transform*=Transform.CreateRotation(
    XYZ.BasisZ, Unit(doc,30, unit_type=UnitType.UT_Angle).internal
)
view = doc.ActiveView

TransactionManager.Instance.EnsureInTransaction(doc)
view.SetSectionBox(section_box)
# ViewSection.CreateSection(
#     doc,
#     view_family_type.Id,
#     section_box
#     )
TransactionManager.Instance.TransactionTaskDone()

OUT='OK'