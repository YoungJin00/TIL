word = "hello, world!"
a= word.split(' ')
new_list = []
for i in a:
  b = i.capitalize()
  new_list.append(b)
print(*new_list)


# from os import replace
# word = "hello, world!"
# a= word.split(' ')
# new_list = []
# for i in a:
#   b = i.replace(i[0], i[0].upper())
#   new_list.append(b)
# print(*new_list)