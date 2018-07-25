使用python的shelve模块实现一个简单的数据库系统
LOAD   path                    	#加载数据库，不存在则创建
CREATE TABLE table-name ,,,,  	#创建数据表
ADD    ROW   table-name ,,,,  	#插入行
DEL    ROW   table-name ,,,,  	#删除行
DEL    TABLE table-name       	#删除表格
SHOW   TABLE table-name         #打印表格
QUIT				#退出
COMMIT				#提交