data = open('baidu_x_system.txt',mode='r+',encoding='utf-8')
lst = data.readlines()
ip = []
result = []
num = []
for i in lst:
    ip.append(i.split(' ')[0])
for i in ip:
    if i not in result:
        result.append(i)
print(result)
for i in result:
    nm = 0
    for j in ip:
        if i == j:
            nm+=1
    num.append(nm)

print(num)



















