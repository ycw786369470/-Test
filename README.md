# -Test
python练习
#22:17
#Wrtier : YangC
#Test_1
#语法糖练习测试（忽略）
# def bold(func):
#     def bold_in():
#         res = func()
#         return '<i>'+res+'</i>'
#     return bold_in
#
# def italic(func):
#     def italic_in():
#         res = func()
#         return '<b>' +res+'</b>'
#     return italic_in
#
# @bold
# def fun1():
#     return 'helloHTML'
# @italic
# def fun2():
#     return 'helloHTML'
# @bold
# @italic
# def fun3():
#     return 'helloHTML'
#
# print(fun1())
# print(fun3())


import time

#Test_2

def upLine(): #选择登录还是注册的函数
    print('====================================')
    print('==     1登录     ==     2注册     ==')
    print('==      输入     ==      输入     ==')
    print('==     "LOG"     ==     "REG"     ==')
    print('====================================')
    Flag = input('>>>')
    # 若登录返回1，若注册则返回0 #
    if Flag == 'LOG':
        return 1
    else :
        return 0

def reg(): # 注册界面
    print('请输入注册账号:')
    new_UN = input('>>>')
    print('请输入密码:')
    new_PW = input('>>>')
    return new_UN,new_PW #返回注册和密码值

def login(): # 定义登录的函数
    print('请输入账号:')
    UserName = input('>>>') # 输入账号
    print('请输入密码;')
    PassWord = input('>>>') # 输入密码
    return UserName,PassWord #返回登陆的账号密码

def ku():#定义账号密码库 只是随便弄个对应，要完全确认账号密码得用字典
    list_UN = [] # UserName的列表定义
    list_PW = [] # PassWord的列表定义
    return list_UN,list_PW # 返回两个列表值

def main():
    UserName, PassWord = ku()
    #  接受库ku的返回值，即账号密码列表
    while 1:
        up1 = upLine()
        #  接受upline函数的返回值
        log_Time = 0 #设置登录次数，每当密码错误便+1，错误次数达到3便返回初始界面
        log_Last = 3 - log_Time #剩余登录次数
        if up1 == 1 : # 执行登录函数
            while 1:
                log_UN, log_PW = login() # 接受登录的用户名和密码
                if log_UN in UserName and log_PW in log_PW:
                    print('登录成功!您可以享受会员折扣了！')
                    print('————暂时没搞————')
                    #之后运行主程序。
                    #break
                    pass
                else:
                    print('账号密码错误！请重新登录。输入密码错误',log_Last,'次后返回初始界面') ###有问题log_Last
                    log_Time += 1
                    if log_Time == 3:
                        break
                    continue
        else : # 则启动注册的函数
            while 1:
                new_UN,new_PW = reg()
                #  接受新账户的账号密码
                if new_UN in UserName:
                    print('该账号已存在！请重新设置。')
                    continue
                else:
                    UserName.append(new_UN) #列表添加新账号
                    PassWord.append(new_PW) #列表添加新密码
                    print('处理中...')
                    time.sleep(1)
                    print('处理中...')
                    print('已完成！','账号库中添加',new_UN,'成功！您可以登录了。')
                    print('已创建的用户名：',UserName)
                    break

main()



####接下来做用户名重复跳转









