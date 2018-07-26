 #-* -coding:GBK -* -
#����ע��ģ��
import shelve
import os
version = "pydb1.0-20180725"
class Pydb:
    def __init__(self):
        self.db = None
        self.kong = 20

    def Load(self,path):
        if os.path.isfile(path+'.dat') == False:
            choose = input(f"�� {path} ������,�Ƿ񴴽���Y/N\n")
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
            print("������ LOAD path �����ݿ�")
            return False
        AllTable = self.db['table']
        table = {}
        if TableName not in AllTable.keys():
            self.AddRow('table',[TableName]+[KeyList])
            self.db[TableName] = table
            return True
        else:
            print(f"�� {TableName} �Ѵ���")
            return False

    def DelTable(self,TableName):
        if self.db==None:
            print("������ LOAD path �����ݿ�")
            return False
        AllTable = self.db['table']
        table = {}
        if TableName not in AllTable.keys():
            self.DelRow('table',TableName)
            del self.db[TableName]
            return True
        else:
            print(f"�� {TableName} ������")
            return False

    def AddRow(self,TableName,KeyValue):
        if self.db==None:
            print("������ LOAD path �����ݿ�")
            return False
        #print(TableName,KeyValue)
        AllTable = self.db['table']
        table = {}
        if TableName in AllTable.keys():
            table = self.db[TableName]
            if len(KeyValue) == len(AllTable[TableName][0]):
                table.update({KeyValue[0]:KeyValue[1:]})
            else:
                print(f"���󣺲��� {KeyValue} ���ԣ�")
                return False
        else:
            print(f"�� {TableName} �����ڣ�")
            return False
        self.db[TableName] = table
        return True

    def DelRow(self,TableName,Key):
        if self.db==None:
            print("������ LOAD path �����ݿ�")
            return False
        AllTable = self.db['table']
        table = {}
        if TableName in AllTable.keys():
            table = self.db[TableName]
            if Key in table.keys():
                table.pop(Key)
            else:
                print(f"��ֵ {Key} ������")
                return False
        else:
            print(f"�� {TableName} �����ڣ�")
            return False
        self.db[TableName] = table
        return True
    
    def Show(self,TableName):
        if self.db==None:
            print("������ LOAD path �����ݿ�")
            return False
        AllTable = self.db['table']
        
        table = {}
        if TableName in AllTable.keys():
            table = self.db[TableName]
            keylist = AllTable[TableName][0]
            #��ͷ
            line = TableName.ljust(self.kong,' ')
            print(keylist)
            for kl in keylist:
                line+=str(kl).ljust(self.kong,' ')
            print(line)
            #����
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
            print(f"�� {TableName} �����ڣ�")
            return False
        return True
    
    def commit(self):
        if self.db==None:
            print("������ LOAD path �����ݿ�")
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
    db.CreateTable('��Ƭģ��',['���','����','��������','����Ѫ��'])
    db.DelRow('��Ƭģ��',0)
    db.Show('��Ƭģ��')
    db.commit()
