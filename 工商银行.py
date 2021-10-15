import random

# 1.存储库和银行名称
'''
    准备一个空的数据库(能存储100用户的库(字典)'''
bank = dict()

'''
    银行名称:中国工商银行昌平支行(str 写死的！）
'''
bank_name = '中国工商银行昌平支行'
bank = {98835406: {'account': 98835406,
                   'username': 'F',
                   'password': 123456,
                   'address': '中国北京市昌平区起码路112号',
                   'money': 0,
                   'acc_bank': 'M78星云迪迦银行'}
        }
# 2.进入时的界面显示
'''
***********************************************************************
*                      中国工商银行昌平支行                            *
 *                         账户管理系统                                *
*                            V1.0                                    *
***********************************************************************

*1.开户
*2.存钱
*3.取钱
*4.转账
*5.查询
*6.Bye！
'''


def welcome():
    print("****************************************************************")
    print("*                  中国工商银行昌平支行                            *")
    print("*                     账户管理系统                               *")
    print("*                        V1.0                                  *")
    print("****************************************************************")
    print("*1.开户\n*2.存钱\n*3.取钱\n*4.转账\n*5.查询\n*6.Bye!")


# 3.银行用户开户操作
'''
用户的所有信息约束：
    账号（str：系统随机产生8位数字）
    姓名(str)
    密码(int:6位数字)
    地址(国家(str)、省份(str)、街道(str)、门牌号(str))
    存款余额(int)
    开户行（银行的名称（str））写死的！
'''
info = '''
          用户名：%s
          账 号：%s
          密码：******
          地址：%s
          存款：%s
          开户行：%s'''


def add_user():
    while True:
        account = random.randint(10000000, 99999999)
        username = input("请输入您的姓名：")
        while True:
            password = input("请输入您的密码：")
            if len(password) != 6:
                print("密码长度错误,请重新输入")
                continue
            else:
                password = int(password)
                break
        address = input("请输入您的详细地址（国家、省份、街道、门牌号等）：")
        money = int(input("请输入您开户初始余额："))
        acc_bank = bank_name
        status = bank_addUser(account, username, password, address, money, acc_bank)
        if status == 3:
            print('数据库已满，请滚去其他银行开户！')
        elif status == 2:
            print('该账号已存在！')
        elif status == 1:
            print('添加成功，以下是您的账号信息：')
            print('------------------个人信息------------------------')
            print(info % (username, account, address, money, acc_bank))
        adduser = input("是否继续开户？y/n :")
        if adduser == 'y':
            continue
        elif adduser == 'n':
            break
        else:
            print("请不要乱输入！")
            break


# 3.银行的开户逻辑（传入参数：用户的所有信息。返回值：整型值）
def bank_addUser(account, username, password, address, money, acc_bank):
    """
       添加用户是判断用户库是否已注册满：
            若已满则返回代号3
    """
    if len(bank) == 100:
        return 3
    '''判断该用户的账号在库里是否存在：
    不存在则在用户库里添加一个该用户并返回代号1
    若存在则返回代号2
    '''
    if account not in bank.values():
        bank[account] = {'account': account,
                         'username': username,
                         'password': password,
                         'address': address,
                         'money': money,
                         'acc_bank': acc_bank
                         }
        return 1
    else:
        return 2


# 4.银行的存钱逻辑（传入值：用户的账号、存取的金额。返回值：布尔类型值）
def add_saving():
    while True:
        account = input("请输入您的账号：")
        money = input("请输入您要存的金额￥：")
        if account.isdigit() and money.isdigit():
            account = int(account)
            money = int(money)
            saving = back_saving(account, money)
            if saving in True:
                print("成功为该账号%s存款：%s" % (account, money))
            elif saving in False:
                print("账号输入错误或没有该账号！")
            addsav = input('要继续存款吗？y/n :')
            if addsav == 'y':
                continue
            elif addsav == 'n':
                break
            else:
                print("请不要乱输入！")
                break
        else:
            print("请不要乱输入！")
            continue


'''根据传入的账号信息查询用户库里是否有该用户：若没有则返回False，若有，则将该用户的金额存进去。
'''


def back_saving(account, money):
    if account in bank:
        bank[account]['money'] += money
        return True
    else:
        return False


# 5.银行的取钱逻辑（传入值：用户的账号，用户密码，取钱金额。返回值：整型值）
def take_money():
    while True:
        account = input('请输入账号：')
        password = input("请输入密码：")
        money = input('请输入取钱金额：')
        if account.isdigit() and money.isdigit() and password.isdigit():
            account = int(account)
            money = int(money)
            password = int(password)
            add_t = add_takemoney(account, password, money)
            if add_t == 1:
                print("该用户不存在！")
            elif add_t == 2:
                print("账号或密码错误！")
            elif add_t == 3:
                print('账户余额不足！')
            else:
                print('成功取款：%s,剩余存款：%s' % (money, bank[account]['money']))
            add_ta = input('要继续取款吗？y/n :')
            if add_ta == 'y':
                continue
            elif add_ta == 'n':
                break
            else:
                print("请不要乱输入！")
                break
        else:
            print("请不要乱输入！")
            continue


'''
    查询该用户是否存在：
        若不存在，则返回代号1，
        若存在，则继续判断密码是否正确：
            若不正确，则返回代号2。
            若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱：
            若不满足，则返回代号3，
            若满足，则将该用户的金额减去。
'''


def add_takemoney(account, password, money):
    if account in bank:
        if password == bank[account]['password']:
            if money <= bank[account]['money']:
                bank[account]['money'] -= money
            else:
                return 3
        else:
            return 2
    else:
        return 1


# 6.银行的转账逻辑（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：账号不对，2密码不对，3钱不够）
def Transfer():
    while True:
        account1 = input('请输入转账账号：')
        password = input("请输入密码：")
        account2 = input("请输入收款账号：")
        money = input('请输入取钱金额：')
        if account1.isdigit() and money.isdigit() and password.isdigit() and account2.isdigit():
            account1 = int(account1)
            account2 = int(account2)
            money = int(money)
            password = int(password)
            add_transfer = transfer_money(account1, account2, password, money)
            if add_transfer == 1:
                print("转账账户或收款账户不存在！")
            elif add_transfer == 2:
                print("转账账号或密码错误！")
            elif add_transfer == 3:
                print('转账账号余额不足！')
            else:
                print('成功转账：%s,剩余存款：%s' % (money, bank[account1]['money']))
            add_ta = input('要继续转账吗？y/n :')
            if add_ta == 'y':
                continue
            elif add_ta == 'n':
                break
            else:
                print("请不要乱输入！")
                break
        else:
            print("请不要乱输入！")
            continue


'''
    先查询用户库是否存在转出和转入的账号:
        若不存在则返回代号:1
        若账号都存在则继续判断转出账号的密码是否正确:
            若不正确，则返回2
            若正确则继续判断要转出的金额是否足够:
                若不够则返回3
	            否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。
'''


def transfer_money(account1, account2, password, money):
    if account1 in bank and account2 in bank:
        if bank[account1]['password'] == password:
            if bank[account1]['money'] >= money:
                bank[account1]['money'] -= money
                bank[account2]['money'] += money
            else:
                return 3
        else:
            return 2
    else:
        return 1


# 7.银行的查询账户逻辑（传入值：账号，账号密码，返回值：空）
def inquire():
    while True:
        account = input('请输入账号：')
        password = input("请输入密码：")
        if account.isdigit() and password.isdigit():
            account = int(account)
            password = int(password)
            inquire_money(account, password)
            add_inq = input('要继续查询吗？y/n :')
            if add_inq == 'y':
                continue
            elif add_inq == 'n':
                break
            else:
                print("请不要乱输入！")
                break
        else:
            print('请不要瞎输入！')
            continue


'''
    先根据账号判断用户库是否存在该用户:
        若不存在则打印提示信息：该用户不存在。
        否则继续判断密码是否正确:
            若不正确则打印相对应的错误信息。
            若账号和密码都正确，则将该用户的信息都打印出来:
                比如：当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.
'''


def inquire_money(account, password):
    if account in bank:
        if password == bank[account]['password']:
            print(info % (bank[account]['username'], bank[account]['account'], bank[account]['address'],
                          bank[account]['money'], bank[account]['acc_bank']))
        else:
            print('账号或密码错误！')
    else:
        print("没有该账户！")


# 8.正式开始业务


while True:
    welcome()
    index = input("请输入您要办理的业务：")
    if index == '1':
        add_user()
    elif index == '2':
        add_saving()
    elif index == '3':
        take_money()
    elif index == '4':
        Transfer()
    elif index == '5':
        inquire()
    elif index == '6':
        print("欢迎下次再来找你银行爸爸！")
        break
