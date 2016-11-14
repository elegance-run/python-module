#测试模块：

__author__='zhengrun'

import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('Hello,world!')
    elif len(args)==2:
        print('Hello,%s!',args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()




#capsule(封装)：

def _private_1(name):
    print('Hello,',name)
def _private_2(name):
    print('Hi,',name)
def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)

greeting('zhengrun')
greeting('run')