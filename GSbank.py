import random
import pymysql
from day1.mode import select,updata
bank_name = '工商银行狼腾分行'
def isint(x):
    if str.isdigit(x):
        x = int(x)
        return x
    else:
        return 0
def home():
    print('---------------------------')
    print('-----工商银行系统 V1.0-----')
    print('--  1. 开户              --')
    print('--  2. 存钱              --')
    print('--  3. 取钱              --')
    print('--  4. 转账              --')
    print('--  5. 查询              --')
    print('--  6. 退出              --')
    print('---------------------------')
    num = input('请输入您要办理的业务:')
    if num == '1':
        adduser()
    elif num == '2':
        save_money_user()
    elif num == '3':
        draw_money_user()
    elif num == '4':
        giveMoney_user()
    elif num == '5':
        searchUser()
    # elif num == '6':
    #     return 0
def giveMoney_user():
    userid = input('请输入你的账号:')
    userpsw = input('请输入你的密码:')
    yourid = input('请输入对方账号:')
    money = isint((input('请输入转账金额:')))
    giveMoney(userid,userpsw,yourid,money)
def giveMoney(userid,userpsw,yourid,money):
    if len(select('select userid from add_bank where userid = %s and passwrod = %s',[userid,userpsw])) != 0:
        if len(select('select userid from add_bank where userid = %s',yourid)) != 0:
            bank_msg = select('select * from add_bank where userid = %s or userid = %s',[userid,yourid])
            if bank_msg[0][4] >= money:
                new_money = bank_msg[0][4] - money
                updata('update add_bank set money = %s where userid = %s',[new_money,userid])
                new_money = bank_msg[1][4] + money
                updata('update add_bank set money = %s where userid = %s',[new_money,yourid])
                return
            else:
                print('您的余额不足')
                return
        else:
            print('对方账号不存在')
            return
    else:
        print('您的账号或密码错误!')
        return
def searchUser():
    userid = input('请输入账号:')
    password = input('请输入密码:')
    search(userid,password)
def search(userid,password):
    if len(select('select * from add_bank where userid = %s and passwrod = %s',[userid,password])) != 0:
        str1 = '''
            账号:%s
            密码:******
            余额:%s
            地址:%s
            开户行:%s
        '''
        bank_msg = select('select * from add_bank where userid = %s',userid)
        print(str1,[bank_msg[0][0],bank_msg[0][4],bank_msg[0][3],bank_msg[0][5]])
    else:
        print('账号或密码错误!')
def adduser_to_bank(userid,username,password,local,money,bankname):
    if select('select userid from add_bank where userid = %s',userid) != 0:
        userid = random.randint(10000000,100000000)
    if len(select('select userid from add_bank',[])) >= 100:
        print('用户已满!')
        return
    else:
        updata('insert into add_bank values(%s,%s,%s,%s,%s,%s)',[userid,username,password,local,money,bankname])
        return
def adduser():
    username = input('请输入您的姓名:')
    password = input('请输入您的密码:')
    if len(password) < 6 or len(password) > 6:
        print('密码必须为6位数字')
        return 1
    elif str.isdigit(password) == False:
        print('密码必须为数字')
        return 2
    else:
        local = input('请输入您的家庭住址:')
        money = isint(input('请输入您要存入的金额:'))
        userid = random.randint(10000000, 99999999)
        userid = str(userid)
        bankname = bank_name
        adduser_to_bank(userid,username,password,local,money,bankname)
        return 3
def save_money_user():
    username = input('请输入账号:')
    password = input('请输入密码:')
    money = isint(input('请输入存入金额:'))
    if money == 0:
        print('请输入正确的金额')
    else:
        save_money(username,password,money)
def save_money(username,password,money):
    if len(select('select userid from add_bank where userid = %s and passwrod = %s',[username,password])) != 0:
        moneys = select('select money from add_bank where userid = %s',username)
        money = moneys[0][0] + money
        updata('update add_bank set money = %s where userid = %s',[money,username])
    else:
        print('账号或密码错误!')
def draw_money(username,password,money):
    if len(select('select * from add_bank where userid = %s and passwrod = %s',[username,password])) != 0:
        bank_msg = select('select * from add_bank where userid = %s and passwrod = %s',[username,password])
        if money <= bank_msg[0][4]:
            money = bank_msg[0][4] - money
            updata('update add_bank set money = %s where userid = %s',[money,username])
            return
        else:
            print('您的余额不足')
            return
    else:
        print('您的账号或密码错误')
        return
def draw_money_user():
    username = input('请输入账号:')
    password = input('请输入密码:')
    money = int(input('请输入您的去取出的金额:'))
    draw_money(username,password,money)
while True:
    home()
















