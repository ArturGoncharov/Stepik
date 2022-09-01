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



c=[]
u=[]
p=[]
file=app.OpenSharedParameterFile()
definition=file.Groups.GetEnumerator()
while definition.MoveNext():
    c.append(definition.Current)
    for i in definition.Current.Definitions:
        u.append(i.UnitType)
        p.append(i.ParameterType)

pt=set(p)
ut=set(u)
OUT= 'ParameterType:', pt, 'UnitType:', ut
OUT='UnitType:',len(ut), 'ParameterType:', len(pt)

# for e in definition:
#     c.append(e)
#     for i in e.Definitions:
#         x.append(i.Name)

