def remove_duplicates(a_list):
    new_lst = []
    for i in set(a_list):
      new_lst.append(i)

    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)