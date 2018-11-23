# coding=utf-8


def yanzheng(name, passwd):
    d_np = {}
    with open('data.txt', 'r') as np:
        lines = np.readlines()
        for line in lines:
            lis = line.split()
            if lis:

                ls = lis[0].split(',')
                d_np[ls[0]] = ls[1]

            else:
                pass
    #    print(d_np)
    if name == 'root' and passwd == d_np[name]:
        #        print(name,d_np[name],'userroot')
        return 'userroot'
    elif name == 'root' and passwd != d_np[name]:
        return 'wrongpd'
    elif name in d_np and passwd != d_np[name]:
        return 'wrongpd'
    elif name in d_np and passwd == d_np[name]:
        #        print(name,d_np[name],'user')
        return 'user'
    else:
        return False

# print(yanzheng())
