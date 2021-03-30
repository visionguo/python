### SRE工作台项目
##### 目的
​      使sre更有效率进行日常事务

##### 现有功能
待开发

##### 文件代码结构
![image](http://git.xxx-int.com/VisionGuo/sre_platform/tree/master/file.jpeg)
##### 运行项目
1.git clone http://git.guazi-corp.com/niuhengbo/sre_platform
2.pip install -r requirement.txt
3.python manage.py runserver
4.打开浏览器，打开URL：http://127.0.0.1:8000

##### 开发步骤

###### 设置gitlab账户
首先，在本地创建ssh key，邮箱为xxx账户邮箱
```
$ ssh-keygen -t rsa -C "your_email@youremail.com"
```
直接点回车，说明会在默认文件id_rsa上生成ssh key。
然后系统要求输入密码，直接按回车表示不设密码
重复密码时也是直接回车，之后提示你shh key已经生成成功。
然后，在本地地址查看ssh key文件 ~/.ssh/id_rsa.pub，将内容复制
登录gitlab，右上角的自己账户，setting里边的ssh keys，粘贴添加
验证是否成功，测试输入
```
$  ssh -T your_email@youremail.com
```
回车会显示是否连接上gitlab
还需要设置username和email，因为gitlab每次commit都会记录他们
$ git config --global user.name "your name"
$ git config --global user.email "your_email@youremail.com"

##### 克隆代码后，要进行开发（git）
在本地文件夹下，初始化git仓库，`git init`
添加远程仓库
 `git remote add origin git@git.guazi-corp.com:niuhengbo/sre_platform.git`
查看本地分支  `git branch` ，带*的属于当前所在的分支
查看远程分支 `git branch -a`
要新建并切换到该分支，运行 `git checkout` 并加上 `-b` 参数，创建自己的分支

##### 注：
在线上运行的是master分支，更新的为develop分支
添加修改后的文件到暂存区 `git add filename`
提交代码并加说明 `git commit -m 'reason'`
合并分支 `git merge develop`
推送到远程仓库      `git push -u origin develop   `

##### 如果在工作台中创建新应用
可在pycharm新建应用
或切换到工作目录，命令行添加`django-admin startapp`
