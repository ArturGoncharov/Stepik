list_Id = []
for e in elements:
	e = e.Category.Id
	list_Id.append(e)


Id_min = min(list_Id)
Id_max = max(list_Id)

elements_Id_min = FEC(doc).OfCategoryId(Id_min)
elements_Id_max = FEC(doc).OfCategoryId(Id_max)

list_Id_new = []
for e_min in elements_Id_min:
    e_min = e_min.Id.IntegerValue
    list_Id_new.append(e_min)
for e_max in elements_Id_max:
    e_max = e_max.Id.IntegerValue
    list_Id_new.append(e_max)    

bprint(sum(list_Id_new))