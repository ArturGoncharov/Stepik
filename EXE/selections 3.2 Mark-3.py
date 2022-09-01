import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import BuiltInParameter

element=selection[0]
mark=element.Parameter[BuiltInParameter.DOOR_NUMBER]

bprint(mark)