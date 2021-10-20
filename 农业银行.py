import random

# 添加一个空数据库

bank = dict()

# 该银行名称
bank_name = '中国农业银行的昌平沙河支行'
# 个人信息
my_info = '''
**************个人信息********************
            姓名：%s
            账号：%s
            密码：******
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            账户余额：%s
            卡类型：%s
            开户行：%s
                '''


# 主界面显示
def add_welcome():
    welcome = '''
    *****************************************************
    *                中国农业银行账户管理系统                *
    *****************************************************
    *                    1.开户                          *
    *                    2.存款                          *
    *                    3.取款                          *
    *                    4.转账                          *
    *                    5.查询                          *
    *                    6.Bye!                         *
    *****************************************************
        '''
    print(welcome)


# 账户类型
def type_logic(typ):
    if typ == '1':
        return '金卡'
    elif typ == '2':
        return '普通卡'


# 自动生成账号
def getRandom():
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string = string + li[int(random.random() * len(li))]
    return string


# 开户逻辑
def user_logic(username, account, password, nationality, province, street, number, cate, money):
    # 用户库已满
    if len(bank) == 100:
        return 3
    else:
        # 账号已存在
        if account in bank:
            return 2
        else:
            # 添加账户
            bank[account] = {
                'username': username,
                'account': account,
                'password': password,
                'nationality': nationality,
                'province': province,
                'street': street,
                'number': number,
                'money': money,
                'type': type_logic(cate),
                'bank_name': bank_name
            }
            return 1


# 存款逻辑
def deposit_logic(account, money):
    # 账号不存在
    if account not in bank:
        return False
    else:
        # 账号存在
        bank[account]['money'] += money
        return True


# 取款逻辑
def teller_logic(account, password, money):
    # 账号不存在
    if account not in bank:
        return 1
    else:
        # 账号或密码错误
        if password != bank[account]['password']:
            return 2
        else:
            # 取款金额不足
            if bank[account]['money'] < money:
                return 3
            else:
                if bank[account]['type'] == '金卡' and money > 50000:
                    return 4
                elif bank[account]['type'] == '普通卡' and money > 20000:
                    return 4
                else:
                    # 正常取款
                    bank[account]['money'] -= money
                    return 5


# 转账逻辑
def transfer_logic(account1, account2, password, money):
    # 转出账号或转入账号不存在
    if account1 not in bank or account2 not in bank:
        return 1
    else:
        # 账号密码错误
        if password != bank[account1]['password']:
            return 2
        else:
            # 转出账号余额不足
            if bank[account1]['money'] < money:
                return 3
            else:
                if bank[account1]['type'] == '金卡' and money > 50000:
                    return 4
                elif bank[account1]['type'] == '普通卡' and money > 20000:
                    return 4
                # 正常转账
                bank[account1]['money'] -= money
                bank[account2]['money'] += money
                return 5


# 查询逻辑
def inquire_logic(account, password):
    # 用户不存在
    if account not in bank:
        print('该用户不存在')
    else:
        # 账号密码错误
        if password != bank[account]['password']:
            print('账户或密码输入错误！')
        else:
            # 正常查询个人信息
            print(my_info % (bank[account]['username'], account, bank[account]['nationality'],
                             bank[account]['province'], bank[account]['street'], bank[account]['number'],
                             bank[account]['money'], bank[account]['type'], bank_name))


# 开户操作
def user():
    while True:
        account = getRandom()
        username = input("请输入姓名")
        while True:
            password = input('请输入密码：')
            if password.isdigit() and len(password) == 6:
                password = int(password)
                break
            else:
                print('请不要瞎输！')
                continue
        while True:
            cate = input('请选择您要输的卡类型（1、金卡；2、普通卡）：')
            if cate == '1' or cate == '2':
                type_logic(cate)
                break
            else:
                print('请不要瞎输！')
        print('请输入地址：')
        nationality = input('    国家：')
        province = input('    省份：')
        street = input('    街道：')
        number = input('    门牌号：')
        while True:
            money = input('请输入开户预存余额：')
            if money.isdigit():
                money = int(money)
                break
            else:
                print('请不要瞎输！')
                continue
        user1 = user_logic(username, account, password, nationality, province, street, number, cate, money)
        if user1 == 1:
            print(my_info % (bank[account]['username'], account, bank[account]['nationality'],
                             bank[account]['province'], bank[account]['street'], bank[account]['number'],
                             bank[account]['money'], bank[account]['type'], bank_name))
        elif user1 == 2:
            print('用户已存在！')
        elif user1 == 3:
            print('用户库已满！')
        keep = input('要继续使用此业务吗？（y/n):')
        if keep == 'y':
            continue
        elif keep == 'n':
            break
        else:
            print('不要瞎输入!')
            break


# 存款操作
def deposit():
    while True:
        account = input('请输入账号：')
        money = input('请输入存款金额：')
        if money.isdigit():
            money = int(money)
            deposit1 = deposit_logic(account, money)
            if deposit1:
                print('存款成功，你存入了￥%s到账号%s' % (money, account))
            else:
                print('账号不存在！')
        else:
            print('不要瞎输入！')
            continue
        keep = input('要继续使用此业务吗？（y/n):')
        if keep == 'y':
            continue
        elif keep == 'n':
            break
        else:
            print('不要瞎输入!')
            break


# 取款操作
def teller():
    while True:
        account = input('请输入账号:')
        password = input('请输入密码：')
        money = input('请输入取款金额：')
        if password.isdigit() and money.isdigit():
            password = int(password)
            money = int(money)
            teller1 = teller_logic(account, password, money)
            if teller1 == 1:
                print('账号不存在！')
            elif teller1 == 2:
                print('账号或密码错误！')
            elif teller1 == 3:
                print('取款账户金额不足！')
            elif teller1 == 4:
                print('超出此类卡的取款范围！')
            elif teller1 == 5:
                print('取款成功，您成功取款：￥%s，本账户余额：￥%s' % (money, bank[account]['money']))
        else:
            print('请不要瞎输入！')
            continue
        keep = input('要继续使用此业务吗？（y/n):')
        if keep == 'y':
            continue
        elif keep == 'n':
            break
        else:
            print('不要瞎输入!')
            break

# 转账操作
def transfer():
    while True:
        account1 = input('请输入转出账号：')
        account2 = input('请输入转入账号：')
        password = input('请输入转出账号密码：')
        money = input('请输入转账金额：')
        if password.isdigit() and money.isdigit():
            password = int(password)
            money = int(money)
            transfer1 = transfer_logic(account1, account2, password, money)
            if transfer1 == 1:
                print('转出或转入账号不存在！')
            elif transfer1 == 2:
                print('转出账号或密码错误！')
            elif transfer1 == 3:
                print('转出账户金额不足！')
            elif transfer1 == 4:
                print('超出转出卡的取款范围！')
            elif transfer1 == 5:
                print('转账成功，您成功转账：￥%s，本账户余额：￥%s' % (money, bank[account1]['money']))
        else:
            print('请不要瞎输入！')
            continue
        keep = input('要继续使用此业务吗？（y/n):')
        if keep == 'y':
            continue
        elif keep == 'n':
            break
        else:
            print('不要瞎输入!')
            break

# 查询操作
def inquire():
    while True:
        account = input('请输入账号:')
        password = input('请输入密码：')
        if password.isdigit():
            password = int(password)
            inquire_logic(account, password)

        else:
            print('请不要瞎输入！')
            continue
        keep = input('要继续使用此业务吗？（y/n):')
        if keep == 'y':
            continue
        elif keep == 'n':
            break
        else:
            print('不要瞎输入!')
            break


# 主程序
while True:
    add_welcome()
    ordinal = input('请输入您要使用的业务：')
    if ordinal == '1':
        user()
    elif ordinal == '2':
        deposit()
    elif ordinal == '3':
        teller()
    elif ordinal == '4':
        transfer()
    elif ordinal == '5':
        inquire()
    elif ordinal == '6':
        break
    else:
        print('不要瞎输入！')
        continue
