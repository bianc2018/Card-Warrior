 #-* -coding:GBK -* -
#中文注释模板
import shelve
import os
version = "pydb1.0-20180725"
class Pydb:
    def __init__(self):
        self.db = None
        self.kong = 20

    def Load(self,path):
        if os.path.isfile(path+'.dat') == False:
            choose = input(f"库 {path} 不存在,是否创建？Y/N\n")
            if choose == 'Y' or choose == 'y':
                return self.Init_db(path)
            else:
                return False
        self.db = shelve.open(path)
        self.path = path
        return True

    def Init_db(self,path):
        self.db = shelve.open(path)
        self.db['version'] = version
        self.db['table'] = {'table':[['table-name','cols-name']]} # table-name : [value] 
        self.path = path

    def CreateTable(self,TableName,KeyList):
        if self.db==None:
            print("请输入 LOAD path 打开数据库")
            return False
        AllTable = self.db['table']
        table = {}
        if TableName not in AllTable.keys():
            self.AddRow('table',[TableName]+[KeyList])
            self.db[TableName] = table
            return True
        else:
            print(f"表 {TableName} 已存在")
            return False

    def DelTable(self,TableName):
        if self.db==None:
            print("请输入 LOAD path 打开数据库")
            return False
        AllTable = self.db['table']
        table = {}
        if TableName not in AllTable.keys():
            self.DelRow('table',TableName)
            del self.db[TableName]
            return True
        else:
            print(f"表 {TableName} 不存在")
            return False

    def AddRow(self,TableName,KeyValue):
        if self.db==None:
            print("请输入 LOAD path 打开数据库")
            return False
        #print(TableName,KeyValue)
        AllTable = self.db['table']
        table = {}
        if TableName in AllTable.keys():
            table = self.db[TableName]
            if len(KeyValue) == len(AllTable[TableName][0]):
                table.update({KeyValue[0]:KeyValue[1:]})
            else:
                print(f"错误：参数 {KeyValue} 不对！")
                return False
        else:
            print(f"表 {TableName} 不存在！")
            return False
        self.db[TableName] = table
        return True

    def DelRow(self,TableName,Key):
        if self.db==None:
            print("请输入 LOAD path 打开数据库")
            return False
        AllTable = self.db['table']
        table = {}
        if TableName in AllTable.keys():
            table = self.db[TableName]
            if Key in table.keys():
                table.pop(Key)
            else:
                print(f"键值 {Key} 不存在")
                return False
        else:
            print(f"表 {TableName} 不存在！")
            return False
        self.db[TableName] = table
        return True
    
    def Show(self,TableName):
        if self.db==None:
            print("请输入 LOAD path 打开数据库")
            return False
        AllTable = self.db['table']
        
        table = {}
        if TableName in AllTable.keys():
            table = self.db[TableName]
            keylist = AllTable[TableName][0]
            #表头
            line = TableName.ljust(self.kong,' ')
            print(keylist)
            for kl in keylist:
                line+=str(kl).ljust(self.kong,' ')
            print(line)
            #表项
            i=0
            #print(table)
            for Key in table:
                line = str(i).ljust(self.kong,' ')+str(Key).ljust(self.kong,' ')
                KeyValue = table[Key]
                for kv in KeyValue:
                    line+=str(kv).ljust(self.kong,' ')
                print(line)
                i+=1
        else:
            print(f"表 {TableName} 不存在！")
            return False
        return True
    
    def commit(self):
        if self.db==None:
            print("请输入 LOAD path 打开数据库")
            return False

        self.db.close()
        self.db = shelve.open(self.path)
        return 

    def quit(self):
        self.db = None
        return True
if __name__ == '__main__':
    db = Pydb()
    db.Load('./data')
    db.CreateTable('卡片模版',['编号','名字','基础攻击','基础血量'])
    db.DelRow('卡片模版',0)
    db.Show('卡片模版')
    db.commit()
