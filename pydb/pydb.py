#-* -coding:GBK -* -
#����ע��ģ��
import shelve
import os
version = "pydb1.0-20180725"
class pydb:
    def __init__(self):
        self.db = None
    def Load(self,path):
        if os.path.exists(path) is False:
            choose = input(f"�� {path} ������,�Ƿ񴴽���Y/N")
            if choose == 'Y':
                return self.Init_db(path)
            else:
                return False
        self.db = shelve.open(path)
        return True
    def Init_db(self,path):
        self.db = shelve.open(path)
        self.db['version'] = version
