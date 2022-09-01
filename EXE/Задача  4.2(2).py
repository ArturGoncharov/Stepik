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

views_fam=FEC(doc).OfClass(ViewFamilyType).ToElements()
views=FEC(doc).OfClass(View).ToElements()
test=[]
type_id=[]
el_views=[]
for v in views:
    ids=v.GetTypeId()
    if ids!= ids.InvalidElementId:
        el=doc.GetElement(ids)
        test.append(el.ViewFamily)
        type_id.append(ids.IntegerValue)
        el_views.append(el)

test2=[]
for i in views_fam:
    test2.append(i.ViewFamily)
summa=sum(set(type_id))

OUT=set(test), len(set(test)), summa




