immutable_var=1,2,'a','b'
print(immutable_var)
immutable_var[1]=3#кортеж не поддерживает обращение по элементам,
# невозможно изменить отдельный элемент кортежа
print(immurtable_var)
mutable_list=1,2,'a','b',['apple','coconut']
print(mutable_list)
mutable_list[4].remove("apple")
print(mutable_list)