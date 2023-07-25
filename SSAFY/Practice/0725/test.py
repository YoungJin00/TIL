# my_set = {1,2,3}
# # my_set.discard(2)
# element = my_set.pop()

# print(element)
# print(my_set)


my_dict = {
    'name' : 'Alice',
    'age' : 25
}

# print(my_dict['name'])
# print(my_dict.get('name'))

# # 찾고자하는 키가 없을 때
# # print(my_dict['age']) #KeyError
# print(my_dict['age']) # None
# print(my_dict.get('name', 'Unknown')) # Unknown

# print(my_dict.keys())

# for k in my_dict.keys():
#     print(k)

# for v in my_dict.values():
#     print(v)

# for k, v in my_dict.items():
#     print(k, v)

# a = 'country'
# print(my_dict.pop('country', f'{a} 없어요' ))

blood_types = ['A', 'B', 'A', 'O', 'AB', 'O', 'A','B','O','B','AB']

#[]
new_dict = {}
# blood_types을 순회하면서
# for bt in blood_types:
#     # 기존에 키가 이미 존재한다면,
#     if bt in new_dict:
#         new_dict[bt] += 1
#     # 키가 존재하지 않는다면 ( 처음 설정되는 키)
#     else:
#         new_dict[bt] = 1

# print(new_dict)

# .get()
# for bt in blood_types:
#     new_dict[bt] = new_dict.get(bt, 0) +1

# print(new_dict)

# .setdefault()
for bt in blood_types:
    new_dict.setdefault(bt, 0)
    new_dict[bt] += 1

print(new_dict)
