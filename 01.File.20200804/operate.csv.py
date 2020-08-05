import codecs
import csv

data = [
    ("测试1", '软件测试工程师'),
    ("测试2", '软件测试工程师'),
    ("测试3", '软件测试工程师'),
    ("测试4", '软件测试工程师'),
    ("测试5", '软件测试工程师'),
]

f2 = codecs.open('2222.csv', 'a+', 'utf-8')
writer = csv.writer(f2)
for i in data:
    writer.writerow(i)
    print(i)

f2.close()
