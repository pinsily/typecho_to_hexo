----
### typecho_to_hexo
此 py 程序主要是把 typecho 数据库中的数据转成 hexo 需要的 markdown 文件，主要是懒得做复制黏贴的工作

不过，在写程序的过程中，还是出了挺多的差错

需要使用的自行设定自己的数据库连接数据

----
### 留意的地方
#### 连接数据库
需要设定编码格式
```
charset='utf8'
```

#### 文件格式
如果 md 文件不使用 utf8 格式的话，hexo 转换会出现中文乱码
```
import codecs
with codecs.open(title_one,'w',"utf-8-sig") as f: 
  pass
```
