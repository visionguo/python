### nginxlog  命令详解


```
参数详解：
-h --help       查看帮助
-i --index      输入es索引名字(未开发)
-m --model      模型方式，现提供 query(defalut)、count、aggs_per_status、aggs_perurl_time
-s --custom     自定义查询，支持kibana查询语句方式
-n --number     指定查询日志数量(default:10)
-t --time       指定查询当前时间之前多久(default:1[/m])

#下面几个只可选择一个,精确匹配
-H --host       精确匹配查询某主机的日志
-d --domain     精确匹配查询某域名的日志
-c --code       精确匹配查询某code的日志

#入库
--todb             此选项提供入库操作
--dbname           此选项指定数据库地址
-u --dbuser        此选项提供数据库用户名
-p --dbpassword    此选项提供数据库密码

```
> 默认执行: 取一分钟前十条记录，格式化输出如下：     
python  logcmd.py      
输出：   总请求  请求的主机   客户端地址  状态码  响应时间   域名 url


```
# 查询 g1-nc-proxy-v01  2分钟的请求总量 和 最新的20条数据信息     
python  logcmd -t 2  -n 20 -H "g1-nc-proxy-v01"

# 查询 www.guazi.com  的qps 和 最新的3条数据
python  logcmd.py -n 3 -t 0.1 -s "www.guazi.com"

# 查询所有 nc_proxy 一分钟内对 状态码为404 的请求和最新数据
python logcmd.py  -n 3 -t 1 -s "g1-nc-proxy-v0*" -c 404

# 统计访问量最多的 5个域名 状态码占比(状态码默认4个)
python logcmd.py  -m domain_status -n 5 

# 统计响应时间最长的 5个域名和url(url默认4个)
python logcmd.py  -m doamin_requesttime -n 5

  

```

