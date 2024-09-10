immutable_var=1,2,3,'apple','coconat'
print(immutable_var)
#immutable_var[1]=3#кортеж не поддерживает обращение по элементам,
# невозможно изменить отдельный элемент кортежа
mutable_list=[1,2,3,'apple','coconat']
print(mutable_list)
mutable_list[2]=33
print(mutable_list)
mutable_list[3]='banana'
print(mutable_list)