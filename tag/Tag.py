#-* -coding:GBK -* -
#中文注释模板
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
#测试
if __name__ == "__main__":
    data = Tag('数据')
    filename = Tag('文件名')
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
