import random
# 判断输入的是否是数字方法
def isint(num):
    if str.isdigit(num):
        num=int(num)
        return num
    elif num=='':
        return -2
    else:
        return -1
shopcart = []
shop = [
        ['联想电脑',5000],
        ['衣服',200],
        ['牙膏',10],
        ['苹果',5],
        ['香蕉',15],
        ['家具',16000],
        ['生鲜',50],
        ['牛肉',50],
        ['苹果手机',20000],
        ['苹果电脑',36000],
        ['辣条1',10],
        ['辣条2',20],
        ['辣条3',50],
        ['笔记本电脑',50000]
        ]
money = input('请输入您的余额:')
money = isint(money)
# 如果输入空字符，默认余额为0
if money==-2:
    money=0
while 1:
    key = random.randint(0,1)
    if key==0:
        print('恭喜获得电脑9折优惠券')
    else:
        print('恭喜获得辣条5折优惠券')
    for index,value in enumerate(shop):
        print(index,'  ',value)
    NO = input('您想要什么商品?')
    NO = isint(NO)
    if NO == -1:
        print('您输入的编号有误!')
    elif NO==-2:
        print(shopcart)
        break
    else:
        if NO < 0 or NO >= len(shop):
            print('您输入的编号有误!')
        else:
            if money >= shop[NO][1]:
                shopcart.append(shop[NO][0])
                if key == 0 and shop[NO][0].find('电脑')>=0:
                    money -= shop[NO][1]*0.9
                    print('购买成功，商品金额为:,',shop[NO][1],'您的当前余额为:',money,'元111')
                elif key == 1 and shop[NO][0].find('辣条')>=0:
                    money -= shop[NO][1]*0.5
                    print('购买成功，商品金额为:,', shop[NO][1], '您的当前余额为:', money, '元222')
                else:
                    money -=shop[NO][1]
                    print('购买成功，商品金额为:,', shop[NO][1], '您的当前余额为:', money, '元333')
            else:
                print('您的余额不足，您的当前余额为:',money,'元')



















