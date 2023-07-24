def sort_tuple(a_tuple):
  new_tuple = ()
  a = sorted(a_tuple)
  new_tuple = (a)
  return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)