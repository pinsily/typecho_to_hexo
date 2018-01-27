# -*- coding:utf-8 -*-
import pymysql 
import codecs
import time

def read_text():
	db = pymysql.connect(charset='utf8',host='127.0.0.1', port=3306, user='root', passwd='pinsily',db='typecho_db')
	cursor = db.cursor()
	select_sql = "select * from typecho_contents"
	cursor.execute(select_sql)
	results = cursor.fetchall()
	i = 1
	for r in results:
		cid = r[0]
		title = r[1]
		created = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(r[3]))
		text = r[5][15:]
		types = r[9]

		tag = title.split(' ')[0]
		content = '---\ntitle: {0}\ndate: {1}\ntags: {2}\n---\n\n{3}'.format(title,created,tag,text)

		if types == 'post':
			write_md(title,content)

	db.close()

def write_md(title,content):
	title_one = title+'.md'
	with codecs.open(title_one,'w',"utf-8-sig") as f:
		f.write(content)
	print("文章 {0}.md 生成".format(title))

read_text()
