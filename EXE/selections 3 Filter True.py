import clr
clr.AddReference('RevitApi')
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import FamilyInstance, BuiltInCategory, ElementCategoryFilter

filter1=ElementCategoryFilter(BuiltInCategory.OST_Doors, True) #фильтр не двери
filter2=ElementCategoryFilter(BuiltInCategory.OST_Windows, True) #филтр не окна
filter3=ElementCategoryFilter(BuiltInCategory.OST_GenericModel, True) # фильтр не обобщенные модели
elements=FEC(doc).WhereElementIsViewIndependent().OfClass(FamilyInstance)\
    .WherePasses(filter1)\
    .WherePasses(filter2)\
    .WherePasses(filter3) 

bprint (elements) #объекты в модели с учетом фильтра
bprint (elements.GetElementCount()) #число полученных объектов