data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"

data_type = {
    'code': 0,
    'date': 1,
    'maximum': 2,
    'remain': 3,
}
filtered = []
for i in data:
    if i[data_type[ext]] < val_ext:
      filtered.append(i)

ans = sorted(filtered, key= lambda x: x[data_type[sort_by]])
print(ans)