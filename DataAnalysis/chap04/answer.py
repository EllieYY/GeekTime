import numpy as np

# studentType = np.dtype({
#     'names': ['名字', '语文', '英语', '数学', '总分'],
#     'formats': ['U32', 'i', 'i', 'i', 'i']})
# students = np.array(
#     [('张飞', 66, 65, 30, 0), ('关羽', 95, 85, 98, 0), ('赵云', 93, 92, 96, 0),
#      ('黄忠', 90, 88, 77, 0), ('典韦', 80, 90, 90, 0)],
#     dtype=studentType)
# students[:]['总分'] = students[:]['语文'] + students[:]['数学'] + students[:]['英语']
#
#
# def printstatistical(name, data):
#     print(name, np.mean(data), np.amin(data), np.amax(data), np.var(data), np.std(data))
#
#
# print('科目', '平均成绩', '最低分', '最高分', '方差', '标准差')
# subjects = list(studentType.names[1:])
# for subject in subjects:
#     data = students[:][subject]
#     printstatistical(subject, data)
#
#
# print('总分排名')
# # print(list(students[subjects][:]))
# # ranking = sorted(students, key=lambda x:x[1]+x[2]+x[3], reverse=True)
# ranking = np.sort(students, order=('总分'))
# print(ranking)


subjects = np.dtype({'names': ['name', 'Chinese', 'English', 'Math'],
                     'formats': ['S32', 'i', 'i', 'i']
                    })

people = np.array([('ZhangFei',66,65,30), ('GuanYu',95,85,98),
                   ('ZhaoYun',93,92,96), ('HuangZhong',90,88,77),
                   ('DianWei',80,90,90),
                  ], dtype=subjects)

print(np.mean(people[:]['Chinese']))
print(np.mean(people[:]['English']))
print(np.mean(people[:]['Math']))


print(np.amin(people[:]['Chinese']))
print(np.amin(people[:]['English']))
print(np.amin(people[:]['Math']))

print(np.amax(people[:]['Chinese']))
print(np.amax(people[:]['English']))
print(np.amax(people[:]['Math']))

print(np.std(people[:]['Chinese']))
print(np.std(people[:]['English']))
print(np.std(people[:]['Math']))

print(np.var(people[:]['Chinese']))
print(np.var(people[:]['English']))
print(np.var(people[:]['Math']))

# summarytype = np.dtype({'names': ['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], 'formats': ['i','i', 'i', 'i', 'i'],})
summary = np.array([], dtype=np.int32)
for i, person in enumerate(people):
    person = list(person)
    print(person[:])
    total = (np.sum(person[1:]))
    print(total)
    summary = np.append(summary, [total], axis=0)

# 每人的总成绩
print(summary)

# 对每人的总成绩排序
print(np.sort(summary))