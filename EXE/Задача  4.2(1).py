from unicodedata import category, name
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

views=FEC(doc).OfClass(View)
result=[]
sums=0
for i in views:
    n=i.UpDirection
    ids=i.Id
    if i.IsTemplate==False:
        if n.Z==1:
            result.append(i.Id)
            sums+=i.Id.IntegerValue

OUT=sums, result[0]

