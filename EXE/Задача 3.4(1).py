import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector as FEC

doc = DocumentManager.Instance.CurrentDBDocument
uiapp=DocumentManager.Instance.CurrentUIApplication
uidoc=uiapp.ActiveUIDocument

# selection= [doc.GetElement(
#     element_id) for element_id in uidoc.Selection.GetElementIds()]

# geometry_element=selection[0].Geometry[DB.Options()]
# OUT=[element.ToProtoType() for element in geometry_element]

elements =FEC(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()
elem_walls=[wall for wall in elements if wall.Parameter[BuiltInParameter.WALL_BASE_CONSTRAINT].AsValueString() != 'Roof']
only_walls=[wall for wall in elem_walls if not wall.CurtainGrid]
geometry_element = [wall.Geometry[Options()] for wall in only_walls]
OUT=[element.ToProtoType() for elements in geometry_element for element in elements]

# OUT = 'Ваш ответ: {}'.format(int(sum([Solid.ThinShell(
#     geometry, 25, 25).Volume for geometry in IN[0]])))[:-6]
