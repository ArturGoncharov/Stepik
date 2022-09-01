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

class Unit(object):
    def __init__(self, doc, value, is_display=True,
                unit_type=UnitType.UT_Length):
        self._doc = doc
        self._unit_type = unit_type
        self._internal_value = self._convert_value(value, is_display) \
            if is_display else value

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

arc= Arc.Create(
XYZ(
    Unit(doc,36900).internal,
    Unit(doc, 21400).internal, 
    Unit(doc, 0).internal),
XYZ(
    Unit(doc,44900).internal,
    Unit(doc, 19600).internal, 
    Unit(doc, 0).internal),
XYZ(
    Unit(doc,39900).internal,
    Unit(doc, 22400).internal,
    Unit(doc, 0).internal
))
line1= Line.CreateBound(
XYZ(
    Unit(doc,40700).internal,
    Unit(doc, 13400).internal, 
    Unit(doc, 0).internal),
XYZ(
    Unit(doc,35200).internal,
    Unit(doc, 17100).internal,
    Unit(doc, 0).internal
))
line2= Line.CreateBound(
XYZ(
    Unit(doc,35200).internal,
    Unit(doc, 17100).internal, 
    Unit(doc, 0).internal),
XYZ(
    Unit(doc,36900).internal,
    Unit(doc, 21400).internal,
    Unit(doc, 0).internal
))
line3= Line.CreateBound(
XYZ(
    Unit(doc,44900).internal,
    Unit(doc, 19600).internal, 
    Unit(doc, 0).internal),
XYZ(
    Unit(doc,40700).internal,
    Unit(doc, 13400).internal,
    Unit(doc, 0).internal
))

curves=[line1,line2,arc,line3]
TransactionManager.Instance.EnsureInTransaction(doc)

cloud=RevisionCloud.Create(
    doc,
    doc.ActiveView,
    Revision.Create(doc).Id,
    curves
)
doc.Regenerate()
TransactionManager.Instance.TransactionTaskDone()

OUT=dir(cloud)