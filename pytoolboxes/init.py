# check pytoolboxes

import os
import configparser

conf = configparser.ConfigParser() # 类的实例化
curpath = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(curpath,'config.ini')

# conf.add_section('FLOWERCODER') # 添加一个新的section
def renewpath(value):
    path_value = str(value)
    conf.read('./config.ini')
    conf.set('FLOWERCODER','path',path_value)
    conf.write(open(path,'w'))  # 保存数据
    print(path_value)
    return path

def testpytoolboxes():#test toolbox
    return print("import pytoolboxes success")

if __name__ == '__main__':
    renewpath('/thh')
