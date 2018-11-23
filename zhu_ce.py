# coding=utf-8
import yan_zheng as yz


def zhu_ce():
    name = input('输入用户名：')
    if name == 'root' or name == '管理员':
        print('不允许的用户名！请重新输入')
        return zhu_ce()
    passwd = input('输入密码：')
    rpd = input('请确认密码：')
    if passwd != rpd:
        print('两次密码不一致，请重新输入')
        return zhu_ce()
    else:
        y_zheng = yz.yanzheng(name, passwd)
        print(y_zheng)
        if y_zheng == 'userroot' or y_zheng == 'user' or y_zheng == 'wrongpd':
            print('用户已存在！请登录')
            return 'denglu'

        else:
            try:
                with open('data.txt', 'a') as zc:
                    s = name + ',' + passwd + '\n'
                    zc.write(s)
                return '注册成功！'
            except Exception as exc:
                return '注册失败！'

# name = input('name:')
# pd = input('pd:')
# print(zhu_ce(name,pd))
