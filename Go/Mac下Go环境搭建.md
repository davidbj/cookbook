# Mac go环境搭建


```
在官网 http://golang.org/ 直接下载安装包安装即可。下载pkg格式的最新安装包，直接双击运行，一路按照提示操作即可完成安装。

pkg默认是安装到/usr/local/go

安装部分已经搞定，接下来是配置mac下的环境变量。这是最关键的。
打开终端（Terminal），敲入一下代码：
cd ~    #进入当前用户下的根目录
ls -a    # -a可将隐藏文件显示，可能会看到.bash_profile文件，若没有就自己创建（我的电脑上就没有）
vim .bash_profile   #创建很简单
进入vim后，按下a才能编辑，输入一下代码：
export GOROOT=/usr/local/go
export PATH=/usr/local/go/bin:$PATH
export GOPATH=你自己平时将go代码放置的地方
解释一下含义：
GOROOT就是pkg包默认安装到的地方，从官网上也可以看到，默认是安装到/usr/local/go
PATH很重要，系统自带的源码要运行必须有这个路径，默认安装路径时，在/usr/local/go/bin
GOPATH可以是用户任意喜欢的地方，放置自己写的go程序

此时，.bash_profile(.zshrc)文件编写完毕，按esc，敲入:wq，回车，搞定。
退回到终端后，敲入source  .bash_profile 使编辑生效
验证一下路径配置是否成功：echo  $GOROOT ，就能看到/usr/local/go了。
如果没有看到，再重启一下ternimal吧。
环境变量配置完成。
```
