1、scrapy安装
    pip install scrapy
    sudo find / -name scrapy
    ln -s  /Library/Frameworks/Python.framework/Versions/3.6/bin/scrapy /usr/local/bin/scrapy

2、mongodb安装
    brew install mongodb
    brew services start mongodb
    mongo   启动客户端

3、创建scrapy项目
    cd /Users/xxx/github/srenew/python/scrapy
    scrapy startproject douban

    cd ./douban/douban/spiders
    生成爬虫文件：scrapy genspider douban_spider movie.douban.com

    scrapy crawl douban_spider

4、
    编写main.py文件，实现在pycharm中直接执行文件
    Xpath解析html里的目标节点

5、导出文件至 test.json
    cd /Users/useername/github/srenew/python/scrapy/douban
    scrapy crawl douban_spider -o test.json
    scrapy crawl douban_spider -o test.csv

6、连接mongodb
    1.mongo
    2.use douban;
    3.show collections;
    4.db.douban_movie.find()    //250行数据
    5.db.douban_movie.find().pretty()    //详情
