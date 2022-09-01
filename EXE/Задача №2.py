import clr
clr.AddReference('RevitApi')
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import FamilyInstance, BuiltInCategory, ElementCategoryFilter, ElementId

filter1=ElementCategoryFilter(BuiltInCategory.OST_Doors, True) #фильтр не двери
filter2=ElementCategoryFilter(BuiltInCategory.OST_Windows, True) #филтр не окна
filter3=ElementCategoryFilter(BuiltInCategory.OST_GenericModel, True) # фильтр не обобщенные модели
elements=FEC(doc).WhereElementIsViewIndependent().OfClass(FamilyInstance)\
    .WherePasses(filter1)\
    .WherePasses(filter2)\
    .WherePasses(filter3)
    #фильтр текущего файла/все элементы в проекте/фильтр класса/добавление фильтров 1-3
list_Id = []
for i in elements:
	i = i.Category.Id
	list_Id.append(i)



bprint (list_Id)