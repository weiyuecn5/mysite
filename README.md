# mysite
个人博客

服务器更新的数据数据上传到github

1.git status 查看git是否有修改内容需要提交

2.git add 指向需要提交的内容文件

3.git commit -m "更新的说明"(如失败,输入下面代码 rm -f ./.Git/index.lock )

4.git push origin master 提交到远程仓库

重构数据库:
正确的方法如下：
先到数据库把表删掉：drop table
注释django中对应的Model

执行以下命令：

python manage.py makemigrations

python manage.py migrate --fake

去掉注释重新迁移

python manage.py makemigrations

python manage.py migrate


拉取最新代码
第一种方法

   git fetch --all

   git reset --hard origin/master

   git fetch  下载远程最新的。

   git reset master  分支重置

第二种方法

   git reset --hard HEAD

   git pull

重启服务器:

1.cd /home/wangmeng/sites/www.floweroman.com/

2.source env/bin/activate

3.cd blogProject

gunicorn --bind unix:/tmp/wwvihs.cn.socket mysite.wsgi:application&
