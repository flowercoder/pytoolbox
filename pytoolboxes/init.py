# check pytoolboxes
import csv
import os
import configparser

conf = configparser.ConfigParser() # 类的实例化
curpath = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(curpath,'./config.ini')

# conf.add_section('FLOWERCODER') # 添加一个新的section
def renewpath(value):
    path_value = str(value)
    conf.read('./config.ini')
    conf.set('FLOWERCODER','path',path_value)
    conf.write(open(path,'w'))  # 保存数据
    print(path_value)
    return path

def operatewrite(ips):
    with open('./data.csv', 'w') as csvfile:
        fieldnames = ['id', 'address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # 写表头
        writer.writeheader()
        for i in range(len(ips)):
            id = 10001 + i
            # print(test[i])
            writer.writerow({'id': id, 'address': ips[i]})


def testpytoolboxes():#test toolbox
    return print("import pytoolboxes success")

if __name__ == '__main__':
    renewpath('/thh')
