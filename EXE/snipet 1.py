# snippet 1
def show_id_sum(elements):
    value = sum([element.Id.IntegerValue for element in elements
                 if hasattr(element, 'Id')])
    dialog = TaskDialog('BIM Planet No2')
    dialog.MainInstruction = 'Выбрано {} элементов. Сумма их Id равна {}' \
                             .format(len(elements), value)
    dialog.Show()
    print value


elements_by_rectangle = uidoc.Selection.PickElementsByRectangle(
    'Выберите все элементы на виде, чтобы получить сумму их Id')

show_id_sum(elements_by_rectangle)