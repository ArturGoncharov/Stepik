import clr
clr.AddReference('RevitApi')
from Autodesk.Revit.DB import FilteredElementCollector as FEC
from Autodesk.Revit.DB import FamilyInstance, BuiltInCategory, ElementCategoryFilter

def get_element_info(elements):
    results = {}
    for element in elements:
        name = element.Name
        id_value = element.Id.IntegerValue
        results[id_value] = name
    return results


def name_selector(some_python_object):
    def selector(elements):
        good_names, bad_names = [], []
        dictionary = some_python_object(elements)
        for id_value in dictionary:
            if id_value > 1348404:
                good_names.append([id_value, dictionary[id_value]])
            else:
                bad_names.append([id_value, dictionary[id_value]])
        print good_names[28][0]
    return selector
a=name_selector(get_element_info)
a(selection)