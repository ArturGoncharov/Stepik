import clr
clr.AddReference('RevitApi')
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import ElementId, BuiltInCategory, Wall

elements=FEC(doc).OfClass(Wall)
elementIds=[element.Id for element in elements]
#elementIds=[element.UniqueId for element in elements]
elementNew=[doc.GetElement(elementId) for elementId in elementIds] #из айди получить объекты модели иили из юникода

bprint(elementNew)
print ElementId(BuiltInCategory.OST_Walls)