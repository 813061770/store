import xlrd as rd
wr = rd.open_workbook(filename='market.xlsx')
all_market = 0
all_cloth = []
master = {}
# 所有衣服总销售量
all_clothes_market = 0
for i in range(0,12):
    wd = wr.sheet_by_index(i)
    cloth_num = wd.col_values(4)[1:]
    for j in cloth_num:
        all_clothes_market += j
# 列出12个月份卖的所有的衣服
for i in range(0,12):
    wd = wr.sheet_by_index(i)
    cloth = wd.col_values(1)[1:]
    for j in cloth:
        if j not in all_cloth:
            all_cloth.append(j)
# 将每个商品添加到字典里
for i in all_cloth:
    master[i] = {'allyear_master':0,'all_market':0}
# 计算全年的总销售额
for i in range(0,12):
    wd = wr.sheet_by_index(i)
    clothes = wd.col_values(1)[1:]
    numb = wd.col_values(2)[1:]
    master_num = wd.col_values(4)[1:]
    for j in range(0,wd.nrows-1):
        market = numb[j] * master_num[j]
        all_market += market
# 每件商品的销售额度
    for j in all_cloth:
        for k in range(0,wd.nrows-1):
            if j == clothes[k]:
                moneys = numb[k] * master_num[k]
                master[j]['allyear_master']+=moneys
                master[j]['all_market'] += master_num[k]
# 每件商品的销售量
#     for j in all_cloth:
#         for k in range(0,wd.nrows-1):
#             if j == clothes[k]:
#                 master[j]['all_market']+=master_num[k]
# 计算每件衣服的占比
for i in master:
    master[i]['num_propotion'] = str('%.2f'%(master[i]['all_market'] / all_clothes_market*100))+'%'
    master[i]['money_propotion'] = str('%.2f'%(master[i]['allyear_master'] / all_market * 100)) + '%'
print(master)





















