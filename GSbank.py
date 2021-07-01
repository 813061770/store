import random
hello=1
bank = {'1':{'username':'fpf','password':'123456','money':10000}}
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
    elif num == '6':
        return 0
    return isint(num)
def giveMoney_user():
    userid = input('请输入你的账号:')
    userpsw = input('请输入你的密码:')
    yourid = input('请输入对方账号:')
    money = int(input('请输入转账金额:'))
    giveMoney(userid,userpsw,yourid,money)
def giveMoney(userid,userpsw,yourid,money):
    if userid in bank and yourid in bank and userpsw == bank[userid]['password'] and money <= bank[userid]['money']:
        bank[userid]['money'] -= money
        bank[yourid]['money'] += money
        print('转账成功！',bank[userid]['money'],bank[yourid]['money'])
    elif userid not in bank or yourid not in bank:
        print('账户不存在!')
        return 1
    elif userid in bank and bank[userid]['password'] != userpsw:
        print('您的密码错误!')
        return 2
    elif userid and yourid in bank and money > bank[userid]['money']:
        print('您的余额不足!')
        return 3
def searchUser():
    userid = input('请输入账号:')
    password = input('请输入密码:')
    search(userid,password)
def search(userid,password):
    if userid in bank:
        if password == bank[userid]['password']:
            str1 = '''
                账号:%s
                密码:******
                余额:%s
                地址:%s
                开户行:%s
            '''
            print(str1 %(bank[userid]['userid'],bank[userid]['money'],bank[userid]['local'],bank[userid]['bank']))
        elif password != bank[userid]['password']:
            print('密码错误!')
    elif userid not in bank:
        print('账号不存在!')
def adduser_to_bank(userid,username,password,local,money,bankname):
    if userid in bank:
        userid = random.randint(10000000,100000000)
    elif len(bank) > 100:
        print('银行信息已满！')
    else:
        bank[userid] = {
            'userid':userid,
            'username':username,
            'password':password,
            'local':local,
            'money':money,
            'bank':bankname
        }
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
        print(userid,bank)
        return 3
def save_money_user():
    username = input('请输入账号:')
    password = input('请输入密码:')
    money = isint(input('请输入存入金额:'))
    save_money(username,password,money)
def save_money(username,password,money):
    if username in bank:
        if password == bank[username]['password']:
            bank[username]['money']+=money
            print('您的账户余额为',bank[username]['money'],'元')
            return 1
        else:
            print('密码错误!')
    else:
        print('用户不存在或错误!')
def draw_money(username,password,money):
    if username in bank:
        if password == bank[username]['password']:
            if money <= bank[username]['money']:
                bank[username]['money'] -= money
                print(bank)
            else:
                print('您的余额不足！')
                return 3
        else:
            print('您的密码错误!')
            return 2
    else:
        print('用户不存在!')
        return 1
def draw_money_user():
    username = input('请输入账号:')
    password = input('请输入密码:')
    money = int(input('请输入您的去取出的金额:'))
    draw_money(username,password,money)
while hello:
    hello = home()
















