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

param_name=[]
for i in param:
    OUT=dir(i)
    param_name.append(i.Name)

iterator = doc.ParameterBindings.ForwardIterator()
nam =[]
while iterator.MoveNext():
    nam.append(doc.GetElement(iterator.Key.Id))



c=[]
u=[]
p=[]
file=app.OpenSharedParameterFile()
definition=file.Groups.GetEnumerator()
while definition.MoveNext():
    c.append(definition.Current)
    for i in definition.Current.Definitions:
        u.append(i.GetType())
        p.append(i.ParameterType)

