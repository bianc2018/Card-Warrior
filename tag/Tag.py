#-* -coding:GBK -* -
#����ע��ģ��
import re
class Tag:
    def __init__(self,tag):
        re_tag = f"<{tag}>(.+?)<-{tag}>"
        #print(re_tag)
        self.tag = re.compile(re_tag,re.S)
        pass
    def Get(self,string):
        m = self.tag.findall(string)
        #print(m)
        if m==None:
            return m
        return m
#����
if __name__ == "__main__":
    data = Tag('����')
    filename = Tag('�ļ���')
    xml = ""
    with open("./data.xml") as file:
        xml = file.read()
    print(xml)
    res = data.Get(xml)
    print(res)
    for r in res:
        print("data:"+r)
        path = filename.Get(r)
        for p in path:
            print("file:"+p)
