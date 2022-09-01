# module unit.py
# -*- coding utf-8 -*-

import clr
clr.AddReference('RevitApi')
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import *

class Unit(object):
    def __init__(self, doc, value, is_display=True,
                unit_type=UnitType.UT_Length):
        self._doc = doc
        self._unit_type = unit_type
        self._internal_value = self._convert_value(value, is_display) \
            if is_display else value
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

    def get_view_family_type(doc, view_family, type_name=None)
        for view_family_type in FEC(doc).OfClass(ViewFamilyType):
            if all(
                    (
                        view_family_type.ViewFamily==view_family,
                        type_name is None or view_family_type
                        .Parameter[BuiltInParameter.SYMBOL_NAME_PARAM]
                        .AsString()==type_name
                    )):
                return view_family_type