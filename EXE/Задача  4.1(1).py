from unicodedata import category
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

def get_built_in_category(category):
    for b_category in BuiltInCategory.GetValues(BuiltInCategory):
        if int(b_category) == category.Id.IntegerValue:
            return b_category

map=doc.ParameterBindings
i= map.ForwardIterator()
param=[]
categories=[]
while i.MoveNext():
    param.append(i.Key)
    categories.append(i.Current)

_category=[]
for categor in categories:
    cat=categor.Categories
    for c in cat:
        c_enum=get_built_in_category(c)
        _category.append(c_enum)

elem_incategory=[]
for c in _category:
    elements_not_type=FEC(doc).OfCategory(c).WhereElementIsNotElementType().ToElements()
    elem_incategory.append(elements_not_type)

param_name=[]
for i in param:
    param_name.append(i.Name)

occupant=0
recycled=0
volume=0
area=0
recycle=0
length=0
width=0
height=0
weidth=0
trans=0
three_id=[]
for i in elem_incategory:
    for e in i:
        if e.LookupParameter('Occupant')!=None:
            occupant+=1
            
        elif e.LookupParameter('Recycled Content')!=None:
            recycled+=1
        elif e.LookupParameter('Volume')!=None:
            volume+=1
            id=e.LookupParameter('Volume')
            ids=id.Id
            three_id.append(ids)
        elif e.LookupParameter('Area')!=None:
            area+=1
        elif e.LookupParameter('Recycle')!=None:
            recycle+=1
            id=e.LookupParameter('Recycle')
            ids=id.Id
            three_id.append(ids)
        elif e.LookupParameter('Length')!=None:
            length+=1
            id=e.LookupParameter('Length')
            ids=id.Id
            three_id.append(ids)
        elif e.LookupParameter('Width')!=None:
            width+=1
            # id=i.LookupParameter('Width')
            # ids=id.Id
            # v.append(ids)
        elif e.LookupParameter('Heigth')!=None:
            height+=1
        elif e.LookupParameter('Weidth')!=None:
            weidth+=1
        elif e.LookupParameter('Transparancy')!=None:
            trans+=1
all=[occupant,recycled,volume,area,recycle,length,width,height,weidth,trans]

OUT=all, set(three_id)