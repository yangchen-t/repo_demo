# **Git**    --分布式版本控制系统

>简介：

Git  是一个开源的分布式版本控制系统，可以高效，快速的处理从下到大的项目版本管理。

## 版本控制

>
>
>什么是版本控制？  

版本控制是一种在开发的过程中用于管理我们对文件，目录或者工程等内容的修改历史，方便查看更改历史记录，备份以便恢复到以前的版本的一种软件工程技术

- 实现跨区域多人协同开发

- 追踪和记载一个或者多个文件的历史记录	
- 组织和保护源码和文档
- 统计工作量
- 并行开发，提高开发效率
- 跟踪记录整个软件的开发过程
- 减轻开发人员的负担，节省时间，同时降低人为错误 

简单来说就是用于管理多人协同开发项目的技术。

没有进行版本控制或者版本控制本身缺乏正确的管理流程，在软件开发过程中会引入很多问题，比如软件代码的一致性，软件内容的冗余，软件过程的事物性，软件开发过程中的并发性，软件源代码的安全性，以及软件的整合等等问题。

无论是工作还是学习，或者是自己做笔记，都经历过这样的阶段。

>
>
>常见的一些版本控制目前主流的版本控制器有这些:

1. Git
2. SVN   (Subversion)
3. CVS    (concurrent  versions system)
4. VSS     (Micorosoft  visual sourcesafe)
5. TFS      (Team Foundation server)
6. Visual studio online

版本控制工具很多，目前流行和使用最广泛的就是Git与SVN

- ### 版本控制分类:

- #### 本地版本控制

1.  适合个人使用

- #### 集中式版本控制

1. 所有的版本数据保存在服务器上，协同开发者从服务器上同步更新或者上传自己的代码

2. 所有的版本数据都存在服务器上，用户的本地只有自以前所同步的版本，如果不联网的话，用户就看不到历史版本，也无法切换版本验证问题，或者在不同分支工作，而且，所有数据都保存在单一的服务器上，有很大的风险这个服务器会损坏，这样就会丢失所有的数据，当前可以定期备份，代表产品：**SVN,CVS,VSS**

- #### 分布式版本控制

​            **每个人都可以拥有全部代码，存在安全隐患！**

1. 所有版本信息仓库全部同步到本地的每个用户，这样就可以在本地查看所有版本历史，可以离现在本地提交，只需要在联网是push到相应的服务器或者其     用户那里，由于每个保存的都是所有的版本数据，只要有一个用户设备没有问题就可以恢复所有的数据，但这增加了本地存储空间的占用，不会因为服务器损坏或者网络问题，导致不能工作的问题。



> **Git与SVN主要区别/分布式和中央式的区别**

- SVN是集中式版本控制系统，版本库是集中放在中央服务器的，而在工作的时候，用的都是自己的电脑，所以首先要从中央处理器的到最新的版本，然后工作，完成工作后，需要把自己做完的活推送到中央服务器，集中式版本控制系统式必须联网才能工作，对网络宽带要求较高。

- Git是分布式版本控制系统，没有中央服务器，每个人电脑就是一个完整的版本库，工作的时候不需要联网了，因为版本都在自己的电脑上，协同的方法是这样的：比如说自己在电脑上改了文件A，其他人也在电脑上改了文件A，这时，你们俩之间只需要把各种的修改推给对方，就可以互相看到对方的修改了。

- 分布式除了远程仓库之外团队中每一个成员的机器上都有一份本地仓库，每个人在自己的机器上就可以进行提交代码，查看版本，切换分支等操作，而不需要完全依赖网络环境

  #### **Git 是目前世界上最先进的分布式版本控制系统**    

 

- ### 中央式版本控制系统（VCS）

  **工作模型：**

  主工程师搭好项目[框架](https://so.csdn.net/so/search?q=框架&spm=1001.2101.3001.7020)
  在公司服务器创建一个远程仓库，并提交代码
  其他人拉取代码，并行开发
  每个人独立负责一个功能，开发完成提交代码
  其他人随时拉取代码，保持同步

​		![在这里插入图片描述](https://img-blog.csdnimg.cn/20200704152604712.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDEyMDA1,size_16,color_FFFFFF,t_70)

- #### [分布式](https://so.csdn.net/so/search?q=分布式&spm=1001.2101.3001.7020)版本控制系统（DVCS）

分布式与中央式的区别主要在于，分布式除了远程仓库之外团队中每一个成员的机器上都有一份本地仓库，每个人在自己的机器上就可以进行提交代码，查看版本，切换分支等操作而不需要完全依赖网络环境。

工作模型：

主工程师搭好项目框架 ，并提交代码到本地仓库
在公司服务器创建一个远程仓库，并将1的提交推送到远程仓库
其他人把远程仓库所有内容克隆到本地，拥有了各自的本地仓库，开始并行开发
每个人独立负责一个功能，可以把每一个小改动提交到本地（由于本地提交无需立即上传到远程仓库，所以每一步提交不必是一个完整功能，而可以是功能中的一个步骤或块）
功能开发完毕，将和这个功能相关的所有提交从本地推送到远程仓库
每次当有人把新的提交推送到远程仓库的时候，其他人就可以选择把这些提交同步到自己的机器上，并把它们和自己的本地代码合并

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200704152623282.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDEyMDA1,size_16,color_FFFFFF,t_70)

- ### 分布式版本管理系统的优缺点：

**优点：**

- 大多数操作本地进行，数度更快，不受网络与物理位置限制，不联网也可以提交代码、查看历史、切换分支等等
- 分布提交代码，提交更细利于review

**缺点：**

- 初次clone时间较长
- 本地占用存储高于中央式系统  



## Git的原理

**通过一种特殊算法压缩数据内容，你的所有数据都会存在记录，git不对丢掉你的任何数据，都会存成快照**

输出一个长度为 **40 个字符**的校验和。 这是**一个 SHA-1 哈希值**

输出一个长度为 **40 个字符**的校验和。 这是**一个 SHA-1 哈希值**

从根本上讲，git是一套**内容寻址的文件系统**，它存储的也是**key-value键值对**，然后根据**key值来查找value**的，说到寻址就会想到指针吧，不错，git也是根据指针来寻址的，这些指针就存储在git的对象中。git一共有3种对象，**commit对象，tree对象和blob对象**。下面便是这3个对象：

![img](https://img-blog.csdn.net/20140417111745046)

 这个**blob对象对应的就是文件快照中那些发生变化的文件内容**，而**tree对象则记录了文件快照中各个目录和文件的结构关系，它指向了被跟踪的快照**，**commit对象实现了对版本提交时间，版本作者，版本序号，版本说明等等附加信息的记录**，从上图看出其中有两个指针，一个指向tree对象，一个则指向上一个commit对象。这个怎么理解呢，怎么还有上一个commit对象，在开发过程中，我们会提交很多次文件快照，那么第一次提交的内容会用一个commit来记录，这个commit没有指针指向上一个commit对象，因为没有上一个commit，它是第一个，当第二次提交时，又会有另外一个commit对象来记录，那么这次commit对象中就会有一个指针指向上一次提交后的commit对象，**经过很多次提交后就会有很多的commit对象，它们组成了一个链表，当我们要恢复哪个版本的时候，只要找到这个commit对象就能恢复那个版本的文件***。**这三类对象，完美实现了git的基础功能，对版本状态的记录**。

Git 的核心是它的对象数据库，其中保存着Git的对象，其中最重要的是blob，tree，commit对象，blob对象实现了对文件内容的记录，tree对象实现了对文件名，文件目录结构的记录，commit对象实现了对版本提交时间，版本作者，版本序号，版本说明等等附加信息的记录，这三类对象，完美实现了git的基础功能，对版本状态的记录。





- ## 存储实现原理（Git对象）

在git中以存储键值对（key-value）的方式来存储文件。它允许插入任意类型的内容，并会返回一个键值，通过该键值可以在任何时候再取出该内容。git的kv中value一般有以下几种类型blob、tree、commit。

新创建文件git并不会追踪

1. git add原理
在调用git add后会生成一个blob对象，然后将该对象add放进进index区。

（1）生成Blob对象
首先，我们需要初始化一个新的 Git 版本库

```shell
$ git init
Initialized empty Git repository in D:/GitTest/.git/

```

然后我们查看一下生成的目录结构

```shell
$ find .git/ -type d # 查看.git/下的所有目录
.git/
.git/hooks
.git/info
.git/objects
.git/objects/info
.git/objects/pack
.git/refs
.git/refs/heads
.git/refs/tags
```

git中所有生成的对象都存储在objects中，因为我们研究git存储原理，所以下来着重观察这一目录。

```shell
$ find .git/objects/ -type f # 查看.git/objects下的所有文件
```

我们发现这个目录下是空的，可以通过底层命令 git hash-object 将任意数据保存于.git/objects 目录（即对象数据库），并返回指向该数据对象的唯一的键(kv)。

```shell
$ echo 'first add file'>readme.md

$ git hash-object -w readme.md
warning: LF will be replaced by CRLF in readme.md.
The file will have its original line endings in your working directory.
6a0b867bdc470c582c15906f264b9fec371cdbfc
```

- #### 这警告是因为换行符在不同系统中格式不一样，为了分布式开发，会自适应系统转换

git hash-object 会接受你传给它的东西，而它只会返回可以存储在 Git 仓库中的唯一键。 -w 选项会指示该命令不要只返回键，还要将该对象写入数据库中。此命令输出一个长度为 **40 个字符**的校验和。 这是**一个 SHA-1 哈希值**——一个将待存储的数据外加一个头部信息（header）一起做 SHA-1 校验运算而得的校验和。
我们再次查看objects目录

```shell
$ find .git/objects/ -type f
.git/objects/6a/0b867bdc470c582c15906f264b9fec371cdbfc
```

这就是开始时 Git 存储内容的方式——一个文件对应一条内容， 以该内容加上特定头部信息一起的 SHA-1 校验和为文件命名。 校验和的前两个字符用于命名子目录，余下的 38 个字符则用作文件名。可以看到它的hash值就是我们之前生成的值。值得一提的是只要内容没变那么hash值也不会变，也就是说不会生成新的对象。
我们可以使用giit cat-file查看该目录下的对象，-t选项表示查看对象类型，-p表示查看对象内容。

```shell
$ git cat-file -t 6a0b867bdc470c5 #可以只使用部分前缀，只要确能找到唯一对象即可。
blob
$ git cat-file -p 6a0b867bdc470c5
first add file
```

（2）将修改添加到暂存区(index区)
我们使用git status可以查看index区的状态，可以很明显的看到我们的文件是红色的，表示文件目前未被加入index区，我们接下来调用git update-index命令将该文件加入index区，因为第一次添加该文件我们要使用--add选项

```shell
$ git update-index --add readme.md
```


我们再次使用git status查看index区状态，发现readme.md已经变成绿色，表示我们已经成功添加到了index区。当然我们可以直接调用git update-index --add readme.md,而不需要生成手动生成blob对象，但是它的底层原理就是会生成一个blob对象，我们这里只是为了演示这个过程，让大家方便理解。

2.git commit原理
进行代码提交时，需要根据暂存区的内容，先生成tree对象，再生成commit对象，然后会将记录记录到logs文件夹下。

（1）生成tree对象

可以通过 git write-tree命令将暂存区内容写入一个树对象。

```shell
$ git write-tree
d8d965c56c04e851e3b47f524c6c52a24c396857
```

那么tree对象到底是什么呢，我们使用git cat-file查看该内容

```shell
$ git cat-file -p d8d965c56c0
100644 blob 6a0b867bdc470c582c15906f264b9fec371cdbfc    readme.md
```

100644 表示该文件类型为文本文件, blob 表示该对象类型，**6a0b867bdc470c582c15906f264b9fec371cdbfc** 表示该文件的 hash值，可以看到和之前我们写入时的值是一样的。

我们添加一个目录，然后将他加入index区，再生成新的tree对象，来查看目录结构再tree中如何表示。

```shell
$ mkdir -p com/git #递归生成目录
$ echo 'add new file and dirs'>com/git/test.txt
$ git add -A #将工作区所有改变添加到index区
$ git write-tree
956902378ddcc3a768459a852253d1c69bb3a21e
$ git cat-file -p 956902378ddcc3a76
040000 tree 108f37e7bececc2fd72e90d34e9e75ef49b65265    com
100644 blob 6a0b867bdc470c582c15906f264b9fec371cdbfc    readme.md
```

我们**可以发现目录的文件类型是040000** ，他在objects中用tree对象表示，那么结构已经很明显了，如果我们在去查看com的tree对象会发现里面存储了java的tree对象，再去查看会发现test.txt的blob对象。

（1）生成commit对象
可以通过调用 commit-tree命令创建一个commit对象，为此需要指定一个树对象的 SHA-1 值，以及该提交的父提交对象（如果有的话）。 我们从之前创建的第一个树对象开始：

```shell
$ echo 'first commit' | git commit-tree d8d965c56c04e8
f742a0cde276d89f79505a500071b6e2577dda45
```

由于创建时间和作者数据不同，你会得到一个不同的散列值。我们查看commit对象

```shell
$ git cat-file -p f742a0cde276d
tree d8d965c56c04e851e3b47f524c6c52a24c396857
author jyx <xxxxxx@163.com> 1586695870 +0800
committer jyx <xxxx@163.com> 1586695870 +0800
```

提交对象的格式很简单：它先指定一个顶层树对象，代表此次提交点的项目快照； 然后是可能存在的父提交（即上一次提交，前面描述的提交对象并不存在任何父提交）； 之后是作者/提交者信息（依据你的 **user.name 和 user.email 配置来设定，外加一个时间戳**）； 留空一行，最后是**提交注释。**
接着，我们将创建另一个提交对象，它们引用上一个提交（作为其父提交对象）：

```shell
$ echo 'second commit' | git commit-tree 956902378ddcc3a7 -p 9fc68968003d
3d87a34c5c890d15a3c9eacf935d65085621694d
```

我们使用git log <commitid>就可以看到一个提交历史了。

```shell
$ git log --stat 3d87a34c5
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200412210749952.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mjc2MjEzMw==,size_16,color_FFFFFF,t_70)

那么一个commit对象可以用下图表示

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200412211613826.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mjc2MjEzMw==,size_16,color_FFFFFF,t_70)



## Git 命令

- #### 本地分支关联远程

```bash
git branch --set-upstream-to=origin/分支名 分支名
```

- #### 代码库修改密码后push不上去怎么办？

```bash
#重新输入密码
git config --system --unset credential.helper
 
#密码存储同步
git config --global credential.helper store

#获取公钥
ssh-keygen -t rsa 
```

- #### 新建代码库

```bash
# 在当前目录新建一个Git代码库
$ git init
 
# 新建一个目录，将其初始化为Git代码库
$ git init [project-name]
 
# 下载一个项目和它的整个代码历史
$ git clone [url]
```

- #### 配置

```bash
Git的设置文件为.gitconfig，它可以在用户主目录下（全局配置），也可以在项目目录下（项目配置）。 
# 显示当前的Git配置
$ git config --list
 
# 编辑Git配置文件
$ git config -e [--global]
 
# 设置提交代码时的用户信息
$ git config [--global] user.name "[name]"
$ git config [--global] user.email "[email address]"
```

- #### 增加/删除文件

```bash
# 添加指定文件到暂存区
$ git add [file1] [file2] ...
 
# 添加指定目录到暂存区，包括子目录
$ git add [dir]
 
# 添加当前目录的所有文件到暂存区
$ git add .
 
# 添加每个变化前，都会要求确认
# 对于同一个文件的多处变化，可以实现分次提交
$ git add -p
 
# 删除工作区文件，并且将这次删除放入暂存区
$ git rm [file1] [file2] ...
 
# 停止追踪指定文件，但该文件会保留在工作区
$ git rm --cached [file]
 
# 改名文件，并且将这个改名放入暂存区
$ git mv [file-original] [file-renamed]
```

- #### 代码提交

```bash
# 提交暂存区到仓库区
$ git commit -m [message]
 
# 提交暂存区的指定文件到仓库区
$ git commit [file1] [file2] ... -m [message]
 
# 提交工作区自上次commit之后的变化，直接到仓库区
$ git commit -a
 
# 提交时显示所有diff信息
$ git commit -v
 
# 使用一次新的commit，替代上一次提交
# 如果代码没有任何新变化，则用来改写上一次commit的提交信息
$ git commit --amend -m [message]
 
# 重做上一次commit，并包括指定文件的新变化
$ git commit --amend [file1] [file2] ...
```

- #### 分支

```bash
# 列出所有本地分支
$ git branch
 
# 列出所有远程分支
$ git branch -r
 
# 列出所有本地分支和远程分支
$ git branch -a
 
# 新建一个分支，但依然停留在当前分支
$ git branch [branch-name]
 
# 以远程分支为基础新建一个分支，并切换到该分支
$ git checkout -b [branch] origin/[remote-branch]
 
# 新建一个分支，指向指定commit
$ git branch [branch] [commit]
 
# 新建一个分支，与指定的远程分支建立追踪关系
$ git branch --track [branch] [remote-branch]
 
# 切换到指定分支，并更新工作区
$ git checkout [branch-name]
 
# 切换到上一个分支
$ git checkout -
 
# 建立追踪关系，在现有分支与指定的远程分支之间
$ git branch --set-upstream [branch] [remote-branch]
 
# 合并指定分支到当前分支
$ git merge [branch]
 
# 选择一个commit，合并进当前分支
$ git cherry-pick [commit]

#合并分支
git rebase
 
# 删除分支
$ git branch -d [branch-name]
 
# 删除远程分支
$ git push origin --delete [branch-name]
$ git branch -dr [remote/branch]
```

- ### 标签（特别注明某次提交）

```bash
# 列出所有tag
$ git tag
 
# 新建一个tag在当前commit
$ git tag [tag]
 
# 新建一个tag在指定commit
$ git tag [tag] [commit]
 
# 删除本地tag
$ git tag -d [tag]
 
# 删除远程tag
$ git push origin :refs/tags/[tagName]
 
# 查看tag信息
$ git show [tag]
 
# 提交指定tag
$ git push [remote] [tag]
 
# 提交所有tag
$ git push [remote] --tags
 
# 新建一个分支，指向某个tag
$ git checkout -b [branch] [tag]
```

- #### 查看信息

```bash
# 显示有变更的文件
$ git status
 
 #查看当前工作区状态
git status  -s  #-s 简洁查看

# 显示当前分支的版本历史
$ git log
 
# 显示commit历史，以及每次commit发生变更的文件
$ git log --stat
 
# 搜索提交历史，根据关键词
$ git log -S [keyword]
 
# 显示某个commit之后的所有变动，每个commit占据一行
$ git log [tag] HEAD --pretty=format:%s
 
# 显示某个commit之后的所有变动，其"提交说明"必须符合搜索条件
$ git log [tag] HEAD --grep feature
 
# 显示某个文件的版本历史，包括文件改名
$ git log --follow [file]
$ git whatchanged [file]
 
# 显示指定文件相关的每一次diff
$ git log -p [file]
 
# 显示过去5次提交
$ git log -5 --pretty --oneline
 
# 显示所有提交过的用户，按提交次数排序
$ git shortlog -sn
 
# 显示指定文件是什么人在什么时间修改过
$ git blame [file]
 
# 显示暂存区和工作区的差异
$ git diff
 
# 显示暂存区和上一个commit的差异
$ git diff --cached [file]
 
# 显示工作区与当前分支最新commit之间的差异
$ git diff HEAD
 
# 显示两次提交之间的差异
$ git diff [first-branch]...[second-branch]
 
# 显示今天你写了多少行代码
$ git diff --shortstat "@{0 day ago}"
 
# 显示某次提交的元数据和内容变化
$ git show [commit]
 
# 显示某次提交发生变化的文件
$ git show --name-only [commit]
 
# 显示某次提交时，某个文件的内容
$ git show [commit]:[filename]
 
# 显示当前分支的最近几次提交
$ git reflog
```

- #### 远程同步

```bash
# 下载远程仓库的所有变动
$ git fetch [remote]
 
# 显示所有远程仓库
$ git remote -v
 
# 显示某个远程仓库的信息
$ git remote show [remote]
 
# 增加一个新的远程仓库，并命名
$ git remote add [shortname] [url]
 
# 取回远程仓库的变化，并与本地分支合并
$ git pull [remote] [branch]
 
# 上传本地指定分支到远程仓库
$ git push [remote] [branch]
 
# 强行推送当前分支到远程仓库，即使有冲突
$ git push [remote] --force
 
# 推送所有分支到远程仓库
$ git push [remote] --all
```

- #### 撤销

```bash
# 恢复暂存区的指定文件到工作区
$ git checkout [file]
 
# 恢复某个commit的指定文件到暂存区和工作区
$ git checkout [commit] [file]
 
# 恢复暂存区的所有文件到工作区
$ git checkout .
 
# 重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
$ git reset [file]
 
# 重置暂存区与工作区，与上一次commit保持一致
$ git reset --hard
 
# 重置当前分支的指针为指定commit，同时重置暂存区，但工作区不变
$ git reset [commit]
 
# 重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致
$ git reset --hard [commit]
 
# 重置当前HEAD为指定commit，但保持暂存区和工作区不变
$ git reset --keep [commit]
 
# 新建一个commit，用来撤销指定commit
# 后者的所有变化都将被前者抵消，并且应用到当前分支
$ git revert [commit]
 
# 暂时将未提交的变化移除，稍后再移入
$ git stash
$ git stash pop
```

- #### 其他

```bash
# 生成一个可供发布的压缩包
$ git archive
```



>
>
>**忽略文件**

有些时候我们不想把某些文件纳入版本控制中，比如数据库文件，临时文件，设计文件等

在主目录下建立".gitignore"文件，此文件有如下规则：

1. 忽略文件中的空格或以井号（#）开始的行将会被忽略

2. 可以使用liunx通配符，列如：星号（*）代表任意多个字符，问号（？）代表一个字符，方括号（[abc]）代表可选字符范围，大括号（{string1，string2,........}）代表可选的字符串等

3. 如果名称的最前面有一个感叹号（！）表示例外规则，将不会被忽略。

4. 如果名称的最前面有一个路径分隔符（/），表示要忽略的文件在此目录下，而子目录中的文件不忽略。

5. 如果名称的最后面有一个路径分割符（/），表示要忽略的是此目录下该名称的子目录，而非文件（默认文件或目录都被忽略）。

   ```shell
   #为注释
   
   *.txt               #忽略所有.txt结尾的文件
   !lib.txt			#但lib.txt除外
   /temp				#仅忽略项目根目录下的TODO文件，不包含其他目录temp
   build/				#忽略build/目录下的所有文件
   doc/*.txt      		#会忽略doc/notes.txt 但不包括 doc/server/arch.txt
   ```



## Git基本理论

>
>
>工作区域

Git本地有三个工作区域：工作目录（working Directory）、暂存区（stage/index）、资源库（Repository/Git Directory）。如果在加上远程的Git仓库（Remote Directory）就是四个区域.

- Working Directory：工作区，就是平时存放项目代码的地方
- Stage/Index：暂存区，用于临时存放你的改动，事实上它只是一个文件，保持即将提交的文件信息列表
- Repository：仓库区（或本地仓库），就是安全存放数据的地方，这里面有你提交的所有版本的数据。其中HEAD指向最新放入仓库的版本
- Remote：远程仓库，托管代码的服务器，可以简单的认为是你项目组中的一台电脑用于远程交换数据

## Git工作流程

git的工作流程一般是：

1. 在工作目录中添加或者修改文件/文件夹；                                  #新添加的文件不会被git追踪

2. 将需要进行版本管理的文件放入暂存区域； 

3. 将暂存区域的文件提交到git仓库

4. 然后push到远程仓库，保持代码一致

   ![img](https://www.runoob.com/wp-content/uploads/2015/02/1352126739_7909.jpg)

因此，git管理文件有三种状态：

- 已修改（modified）
- 已暂存（staged）
- 已提交（commitd）



- ## Git工作流



- #### TBD(Trunk Based Development)

- #### Git Flow

- #### Github Flow

- #### GitLab Flow

- #### Aone Flow（阿里Aone工作流）

在讲这些流程之前，要明确分支的概念。在我们日常开发过程中，往往会有一些生命周期比较长的分支，比如：master、dev、release。这些分支都是有语义体现，比如dev用于日常开发使用、release用于发布使用、master就是稳定的主干分支。这些分支都是有特殊意义而保留的，主要分为 主干分支、开发分支、发布分支，具体要看这个分支的用途。业界也会把这种分支管理称为分支模式，举个例子就有：

- 主干开发\分支发布（TBD）
- 分支开发\主干发布（Github实践）
- 分支开发\分支发布（Git实践）
- 支持分支\开发主干发布 and 分支开发\分支发布 都支持（GitLab实践/Aone实践）。



- ### TBD

  这是[Paul Hammant 2013年提出的模型](https://link.zhihu.com/?target=https%3A//paulhammant.com/2013/04/05/what-is-trunk-based-development/)，这个模型基本就是SVN的模型。TBD的开发模式比较适用于日常一个人开发的模式。建立好仓库后，只有一个master分支。我们会基于这个master分支一直提交我们的代码，直到功能做完，然后基于master去拉取一个新的分支叫做release1.0.0进行发布（如下图所示）。这个时候master就是主干开发分支，而release1.0.0为发布分支。在TBD模型中，所有开发都在主干，但是拉出新的分支交付。这个模式下，假设所有的特性开发都可以快速完成，这样就不会影响持续集成。

![img](https://pic3.zhimg.com/80/v2-809f8c44315b2aa5fa1c199297216716_720w.jpg)

当然缺点也很明显，上述这种方式比较短周期的项目，如果周期长，加入的人越来越多。那么上述方式便不适合用于持续集成了。

- ### Git Flow

GitFlow则是Git官方推崇的一种工作流，在这个工作流程中会有如下几个类型分支：

- master
- release（多条特性发布分支）
- hotfix（多条修复分支）
- develop
- feature（多条特性开发分支）

这里除了master和develop分支是唯一且常驻分支以外，其他分支都有多条。且master和develop分支贯穿整个流程，永久不会删除。然后feature、hotfix、release用于三个场景：日常需求开发、线上问题修复、发布正式版本，一旦完成开发，它们就会被合并进master和develop分支，然后被删除。接下来分别讲这三个场景的具体分支运作：

![img](https://pic1.zhimg.com/80/v2-cf303f51b392ec86b6e2c34a6b849844_720w.jpg)

- ### 日常需求开发流程如下：

  ![img](https://pic4.zhimg.com/80/v2-c381e16cc5a0657782d3b15703f8f347_720w.jpg)

蓝色部分：日常需求开发基于develop分支拉取feature分支，然后基于feature进行日常单功能需求开发，需求开发完成后将分支合并回develop分支。
橙色部分：当某一个迭代需求（features）都已经合入Develop分支完成之后。会基于develop分支拉出单独的release分支用于这次迭代的产品发布。
黄色部分：从某次迭代devlop分支拉过来的release分支，一般情况下分支名可能叫release_v1.0.1_xxxx 用于标明该分支版本功能。然后会基于这个release分支出alpha版本、beta版本的发布包进行发布。直至该release发布情况稳定，便会把release分支合入master上，且同步到develop分支上保证master和develop分支代码一致。
绿色部分：当release分支发布成功后，便会把本次release合并进来的分支对应的commit进行打tag处理。
紫色部分：当本次迭代的产品上线之后，出现线上问题，则会紧急拉取hotfix分支，一般会命名为hotfix_v1.0.1_xxxxx 分支名解释修复什么问题，然后将代码提交。接下来跟feature分支一样，会把hotfix分支合入develop中进行验证，验证没问题之后会将hotfix合入到master上，并且打上Tag。重新基于修复的问题出发布包，此时会看情况继续拉出一条release分支用于出发布产物。
这种开发模式也就是所谓的，分支开发（feature）分支发布（release）。
GitFlow的缺点就在于，这里有两个分支需要长期维护，分别是master和develop。需要保证develop分支代码和master代码一致。另外这个过程中，创建分支种类很多，管理很复杂。比较适合在一个迭代周期内，开发流程确定，有且只有一个业务线，有明确的需求评审量化需求数量、开发、测试，大家都能按照这种版本方式。如果存在一个项目，多个业务线同时跑的时候，每条线的发布都是独自进行，那么上述这个流程就会很容易引入一些实际本迭代不应该上线的需求（从develop中引入了一些开发中的需求），因为上述场景比较适合一个项目组，一个业务线发布的产品开发流程，比如App客户端（大型app拆分了多个团队并行跑的就不适用了）的发布就比较适合用这种。



- ### GitHub Flow

  讲完GitFlow后，接下来主要讲GitHubFlow，这种工作流主要是在Github主要用于开源项目的协同使用，但是这里面的思想其实跟后续的Gitlab支持的工作流有些相似之处。GithubFlow只有一个长期分支就是master，由于GitFlow的develop分支维护麻烦，所以GitHubFlow并没有采用两长期分支的方式。日常玩开源的都应该知道，我们要贡献开源项目代码，第一步就是要先fork别人的项目，然后fork完成到自己的仓库里面进行修改，修改完成提交代码到你fork仓库后，再给目标项目提交PR（Pull Request，跟gitlab的MR作用类似），告知目标项目的作者把你的项目Pull到他的项目中去（所以Github叫PR，因为是作者要主动拉你的代码到他的项目中），然后目标项目作者把你分支进行CodeReview没问题之后，合入master。等待新版本发布，会基于master进行构建出release版本。

  ![img](https://pic2.zhimg.com/80/v2-04103b8593e7f4b15759b93f164c4bf5_720w.jpg)



这里的核心流程如下：

- 第一步：先Fork目标项目仓库，然后切换到你Fork的项目仓库，根据需求，从master拉出新分支，不区分功能分支或补丁分支。
- 第二步：新分支开发完成后，把代码push到你的项目仓库，需要讨论或者合并的时候，就向目标项目仓库的master发起一个pull request（简称PR）。
- 第三步：Pull Request既是一个通知，让项目作者注意到你的合入请求，这是一种对话机制，然后作者和你一起评审和讨论你的代码。对话过程中，你还可以不断提交代码。
- 第四步：当你的Pull Request被目标项目作者或者协作者接受，就会合并进目标项目的master，重新部署后，原来你拉出来的那个分支就被删除。（先部署再合并也可。）

基于这套流程，后续Gitlab借鉴了这种开发思路，当在一个项目中多人协作的时候，可以通过提MR（Merge Request）的形式提交合并请求，让项目的Onwer或者Commiter知道你要进行代码合入到一些重要分支，然后进行代码评审（CodeReview，简称CR）。
因为Github开源的玩法主要是基于master作为发布主干，即master是发布分支/feat是开发分支，所以其特点就是主干发布，分支开发。
GithubFlow的缺点在于，Github工作流本身，只能基于master进行发布，有些时候当你pr进去不代表立即能够发布。如果把这个场景放到公司业务场景上，公司业务是有发布窗口，采用开源这种玩法显然不太现实，有些时候就是需要你pr完了立马先发布你的特性。所以不得已得当你PR完成后，需要单独基于master创建一个单独的分支（携带你PR的代码）用于发布并且进行跟踪。



- ### GitLab Flow

基于GitFlow的多分支管理繁琐以及Github这种代码PR（PullRequest）和CR（CodeReview）的机制，GitLabFlow则是吸收了两者的优点，并且提出了多开发环境的概念。Gitlab的最大的开发原则为上游优先（upsteam first）：即只存在一个主分支master，它是所有其他分支的”上游”。只有上游分支采纳的代码变化，才能应用到其他分支。且提出了多环境的概念，具体流程如下图：

![img](https://pic1.zhimg.com/80/v2-d8e3afdb251473f8950d3b056613189c_720w.jpg)

这里的master是其他分支的上游，只有紧急情况，才允许跳过上游master分支，直接合并到下游分支。当遇到版本发布的时候，则如下进行处理：

![img](https://pic1.zhimg.com/80/v2-60f38f3a0c42ffb2893daf01325f5b60_720w.jpg)

然后日常开发的流程会变成：

- 第一步：先基于master拉出feature分支或者是bugfix分支，然后进行实际的需求开发（也包含了本地测试）。
- 第二步：开发完成之后，需要把自己的分支提MR让仓库的Onwer或者Commiter进行CR，代码评审完成通过后，才允许你把代码合并到Master。而且这是唯一合入Master分支的途径，master作为保护分支。
- 第三步：当代码MR进入master主干分支之后，会基于当前的Master拉出对应的环境分支进行部署，部署完成后进行多环境的验证，这里一般会分为test、pre-prod、prod三种环境的分支。

当然，这只是GitlabFlow结合GitFlow和GitHubFlow两者的工作流方式总结出来的一种适合公司业务场景的方式，所以很多公司基本都是内部搭建Gitlab作为公司内部代码管理系统。便于内部人员协作。GitlabFlow更多的是在公司层面团队协作上提供了比较好的指导。
​

- ### Aone Flow

Aone这个产品其实是阿里一整套Devops的实践系统，其中包含了需求管理、代码管理、持续集成、持续部署等相关的项目管理系统。这里只针对Aone中的持续集成AoneFlow来讲解下AoneFlow具体的工作流程。AoneFlow包含两部分内容：代码管理工作流和多环境部署支持。

- ### 代码管理工作流

AoneFlow 只使用三种分支类型：主干分支、特性分支、发布分支，以及三条基本规则。

- 规则一（开始工作前，从主干创建特性分支）从代表最新已发布版本的主干上创建一个通常以feature/前缀命名的特性分支，然后在这个分支上提交代码修改。



![img](https://pic3.zhimg.com/80/v2-5920d5bf21acaf056c9bbed0b1cb5b6e_720w.jpg)



- 规则二（通过合并特性分支，形成发布分支）这一步是比较核心的地方，Aone其实通过了流水线集成方式，把多个分支就绪好之后（会有个待发布特性分支的池子），合并成一个release前缀的发布分支进行发布。假如此时又一个特性分支要暂停发布，只要踢掉这个特性分支，重新把池子里的特性分支重新合并成新的release发布分支即可。



![img](https://pic1.zhimg.com/80/v2-a4bb28588f77a4a6d670da8e4e10eddc_720w.jpg)



- 规则三（发布到线上正式环境后，合并相应的发布分支到主干，在主干添加标签，同时删除该发布分支关联的特性分支）当一条release前缀发布分支上的流水线完成了一次线上正式环境的部署，就意味着相应的功能真正的发布了，此时应该将这条发布分支合并到主干。为了避免在代码仓库里堆积大量历史上的特性分支，还应该清理掉已经上线部分特性分支。这一步如果你用AoneFlow是会在背后帮你自动执行的。



![img](https://pic1.zhimg.com/80/v2-dc248b5f6d79cf89691be229ff898560_720w.jpg)



其实这套系统精妙的地方在于第二个规则，第二个规则需要有一套代码仓库自动化管理的流程（也是业务需要实现的点）。你需要实现一个用于存放所有特性分支的池子，然后把所有feature分支都放到这个池子里面记录起来，当流水线要进行发布的时候，会把这些特性分支都进行集成，生成release分支（过程中出现冲突还可以调用webide进行冲突解决）。具体的操作UI可以参考如下：

![img](https://pic2.zhimg.com/80/v2-0b3517831fe560736707e84cf9619209_720w.jpg)


当你添加好本次需要发布的分支之后，会生成一条新的release分支，具体如下：

![img](https://pic3.zhimg.com/80/v2-abce763b5657f8ecc346bbd55d12e91e_720w.jpg)


然后就可以基于这个发布分支进行代码发布到测试环境、预发环境、生产环境。
​

- ### 多环境支持

Aone这套系统跟普通持续集成系统不同的地方在于，他基于持续集成系统和持续部署做了更高的一层抽象，你也可以理解是一套流水线系统。通过定制流水线，你可以生产一条流程如下图所示的系统：

![img](https://pic2.zhimg.com/80/v2-9c2bb160c8deb6b10327ac457010dfc9_720w.jpg)


这里面前两部是上述代码工作流的操作，过程中会触发代码构建，产物归档，部署测试、预发布、生产三种环境。直到最后一步的时候，会把集成分支合入到Master主干分支。
假如这个过程中，我发到测试环境，突然我要下线某个特性分支，那我只要把特性分支池子的某个特性剔除后，重新走一边上述流程（即重新集成代码，构建以及发布测试环境）即可达到剔除某个特性发布的情况（会有个单独的Git公共账号用于自动化进行代码合并）。这种场景主要在团队多人协作中，有人需求可能要晚点等前端或者后端先发布完才能发，那么就会有需要用到这种剔除的逻辑。这里面唯一的缺点就是，这条流水线周期会比较长，因为流水线是独占的，一个项目发布正式只能同时走一条流水线实例不允许有多条流水线进行环境部署造成环境抢占冲突。这个流水线不是CI系统的Task以及State概念，而是单独定义的一套更高级别抽象的流水线系统。从AoneFlow这套系统的设计上，其实更符合国内追求敏捷迭代的公司进行使用，而且设计相对合理。
当然，要实现这套AoneFlow其实需要能够把CI和CD环节进行打通，并且还要把需求管理配合代码feature分支管理打通。本人因为在阿里和华为都用过这套AoneFlow的实践，所以知道这里面更多的细节，阿里内部叫做Aone，阿里云上称为[云效平台](https://link.zhihu.com/?target=https%3A//www.aliyun.com/product/yunxiao) ，华为云内部叫做伏羲（其实也是挖了阿里做Aone的技术产品过去重新做了一套）。本质其实就是一套Devops真正的实践系统，腾讯目前还没看到有这样的中台系统出现，希望日后能看到。



- ### 总结：

Git工作流其实**不仅仅只是个流程**。它其实也是Devops实践中代码管理的一环。从GitFlow、GithubFlow、GitlabFlow、AoneFlow的整个过程，都是基于工作流系统更贴近实际开发场景的实践以及提升。这里面更多强调的是**从代码的人为管理到最后的自动化托管**，**以及到最后怎么能够和持续系统进行结合**，最后升华为Devops中CI/CD的真正实践。**更多讲究的是融汇贯通，以及团队提效和规范化。**







# Docker --容器化技术

>
>
>docker是什么？

Docker 是一个开源的应用容器引擎，可以把应用以及依赖包到一个可移植的[镜像](https://baike.baidu.com/item/镜像/1574)中，然后发布到任何流行的 [Linux](https://baike.baidu.com/item/Linux)或[Windows](https://baike.baidu.com/item/Windows/165458)操作系统的机器上，也可以实现[虚拟化](https://baike.baidu.com/item/虚拟化/547949)。容器是完全使用[沙箱](https://baike.baidu.com/item/沙箱/393318)机制，相互之间不会有任何接口

- #### 一个完整的Docker有以下几个部分组成：

1. DockerClient客户端
2. Docker Daemon守护进程
3. Docker Image镜像
4. DockerContainer容器 

- #### Docker 架构

Docker 使用客户端-服务器 (C/S) 架构模式，使用远程[API](https://baike.baidu.com/item/API/10154)来管理和创建[Docker容器](https://baike.baidu.com/item/Docker容器/18694252)。Docker 容器通过 Docker 镜像来创建。容器与镜像的关系类似于面向对象编程中的对象与类。



- ### docker 应用场景：

web应用的自动打包和发布，自动化测试和持续集成，发布，在服务环境中部署和调整数据库或其他的后台应用



- ### 优点

用于开发，交互和运行应用程序的开放平台将应用程序与基础框架分开，加快交付可以管理应用程序相同的方式来 管理基础架构

利用docker的方法：

​    快速交付，测试和部署代码

​	减少编写代码和在生产环境中运行代码之间的延迟

1. 快速，一致的交付您的应用程序
2. 响应式部署和扩展
3. 同一硬件运行更多的工作负载

## Docker 命令

*

```bash
#获取容器/镜像/网络的元数据。
docker inspect [container_name]/[images_name]/[network_name]

#查看命令参数使用方法
docker command --help 
```

- ### docker 基础命令

```bash
#进入容器
1、进入容器方式一 这里咱就进入 前面的 redis001容器                  
docker exec -it 容器名/容器ID /bin/bash
#进入 前面的 redis001容器   
docker exec -it redis001 /bin/bash

2、进入容器方式二 —推荐使用 exec 方式
docker attach 容器名/容器ID            #退出时会关闭容器


那怎么退出容器呢 ？    #退出容器
从容器内 退出到自己服务器中 需注意 两个退出命令的区别
  
1:  #----直接退出  未添加 -d(持久化运行容器) 时 执行此参数 容器会被关闭
exit        ^c	
2:  #退出保留后台
ctrl + q + P  
```

```bash
#启动docker
systemctl start docker

#关闭docker
systemctl stop docker

#重启docker
systemctl restart docker

#docker设置随服务启动而自启动
systemctl enable docker

#查看docker 运行状态
#------如果是在运行中 输入命令后 会看到绿色的active
systemctl status docker

#查看docker 版本号信息
docker version
docker info

#docker 帮助命令 忘记了某些命令便可使用此进行查看与回顾
docker --help

#比如 咱忘记了 拉取命令 不知道可以带哪些参数 咱可以这样使用
docker pull --help
```

- ### docker 镜像命令

```bash
#查看自己服务器中docker 镜像列表
docker images

#搜索镜像
docker search 镜像名
docker search --filter=STARS=9000 mysql 搜索 STARS >9000的 mysql 镜像

#拉取镜像 不加tag(版本号) 即拉取docker仓库中 该镜像的最新版本latest 加:tag 则是拉取指定版本
docker pull 镜像名 
docker pull 镜像名:tag

#拉取最新版 mysql
docekr pull mysql

#咱再来拉取一个指定版本号 镜像 至于版本号呢 可以在docker hub中查看
docker官方镜像搜索
例如 拉取 mysql 5.7.30 -

docker run 镜像名
docker run 镜像名:Tag

docker pull tomcat

docker run tomcat


#发现咱运行后 出现tomcat 默认占用的8080 端口 说明该镜像已经是启动了 ，但是 咱好像鼠标没有回到咱服务器上了 ，这怎么办呢 ？

#使用 Ctrl+C （注：此方式虽然可以退出容器，但此种命令操作方式却是错误的，详细缘由请见下文的容器命令）

docker中 run 命令是十分复杂的 有什么持久运行 映射端口 设置容器别名 数据卷挂载等

#一通测试，发现我们拉了好多镜像了，但我们现在根本用不着，这些无用镜像怎么删除呢？

#删除镜像 ------当前镜像没有被任何容器使用才可以删除

#删除一个
docker rmi -f 镜像名/镜像ID

#删除多个 其镜像ID或镜像用用空格隔开即可 
docker rmi -f 镜像名/镜像ID 镜像名/镜像ID 镜像名/镜像ID

#删除全部镜像  -a 意思为显示全部, -q 意思为只显示ID
docker rmi -f $(docker images -aq)

#强制删除镜像
docker image rm 镜像名称/镜像ID

#镜像的基础命令就到这里 下方会使用更复杂的 docker run 命令 来根据镜像启动容器

#保存镜像
#将我们的镜像 保存为tar 压缩文件 这样方便镜像转移和保存 ,然后 可以在任何一台安装了docker的服务器上 加载这个镜像

命令:
docker save 镜像名/镜像ID -o 镜像保存在哪个位置与名字

exmaple:
docker save tomcat -o /myimg.tar

#保存镜像任务执行完毕，我们来看下指定位置下是否有该tar？

#加载镜像
#任何装 docker 的地方加载镜像保存文件,使其恢复为一个镜像
docker load -i 镜像保存文件位置

#提交自己的镜像 将 a404c6c174a2 提交为一个mymysql:v1的images
docker commit -m "msg" -a="user_msg"  a404c6c174a2  mymysql:v1
```

- ### docker 容器命令

```bash
前言已经说了 docker 容器 就好比 咱java中的new出来对象（docker run 镜像 产生一个该镜像具体容器实例）,docker 容器的启动需要 镜像的支持
先放上 docker 容器查看命令

查看正在运行容器列表
docker ps

查看所有容器 -----包含正在运行 和已停止的
docker ps -a
容器怎么来呢 可以通过run 镜像 来构建 自己的容器实例
运行一个容器

# -it 表示 与容器进行交互式启动 -d 表示可后台运行容器 （守护式运行）  --name 给要运行的容器 起的名字  /bin/bash  交互路径

docker run -it -d --name 要取的别名 镜像名:Tag /bin/bash 

例如我们要启动一个redis 把它的别名取为redis001 并交互式运行 需要的命令 —我这里指定版本号为5.0.5

#1. 拉取redis 镜像
docker pull redis:5.0.5
#2.命令启动
docker run -it -d --name redis001 redis:5.0.5 /bin/bash

#3.查看已运行容器
docker ps

发现看到了 redis 使用了6379 端口 那么我们在关闭防火墙或开启了安全组的情况下 是否可以进行访问呢？
为了 区分 咱们使用linux 命令 查看一下
# netstat是控制台命令,是一个监控TCP/IP网络的非常有用的工具，它可以显示路由表、实际的网络连接以及每一个网络接口设备的状态信息

netstat -untlp

**惊讶的发现，我们redis容器启动占用的 6379端口netstat 没有显示出来？什么情况？赶紧使用 redis desktop manger 连接测试一下 **
为什么不行呢 已经确定了 docker 中 redis 容器已经是在运行中 且占有端口 6379啊？
因为：占用的6379端口 仅仅是在容器中内部本身的端口,与宿主机的6379端口并无联系，我们通过宿主机Ip:6379访问此redis示例，那自然是找不到的哟！
这里，来补充一点Docker容器的知识！
每一个 Docker容器都是独立和安全的应用平台（我们可以理解为，每一个docker容器都相当于在我们的服务器上占用资源然后开辟了属于自己的一个空间（也可以理解为服务器））

这是Docker 一大特点，每个容器之间环境都是隔离的!!!
我们甚至可以在一个服务器上，使用docker镜像，来跑出N个 mysql实例（尽管，他们的默认端口都是一样的，但还是那句话，容器间，环境是隔离的。A容器中的3306 与B容器的3306毫无关系，因为其不在一个世界呀!）
默认情况下，我们是无法通过宿主机（安装docker的服务器）端口来直接访问容器的 ,因为docker容器自己开辟空间的端口与宿主机端口没有联系…
如果外部想要访问容器，那必须得让容器中的端口与宿主机的端口建立联系绑定起来，这个正式的概念叫做 容器端口映射
有了端口映射，我们就可以将宿主机端口与 容器端口绑定起来，比如 我们建立宿主机的6379端口与容器redis6379端口绑定起来，那么再访问宿主机Ip:6379 就可以访问到对应容器了！
接下来 进行 容器端口映射演示
首先停止容器

# 先停止咱之前运行的 redis 容器 

docker stop 容器名/容器ID

#删除一个容器
docker rm -f 容器名/容器ID
#删除多个容器 空格隔开要删除的容器名或容器ID
docker rm -f 容器名/容器ID 容器名/容器ID 容器名/容器ID
#删除全部容器
docker rm -f $(docker ps -aq)
```

```bash
#停止容器
docker stop 容器ID/容器名

#重启容器
docker restart 容器ID/容器名

#启动容器
docker start 容器ID/容器名

#杀掉容器
kill 容器
docker kill 容器ID/容器名

#容器文件拷贝 —无论容器是否开启 都可以进行拷贝
#docker cp 容器ID/名称:文件路径  要拷贝到外部的路径   |     要拷贝到外部的路径  容器ID/名称:文件路径
#从容器内 拷出
docker cp 容器ID/名称: 容器内路径  容器外路径

#从外部 拷贝文件到容器内
docker  cp 容器外路径 容器ID/名称: 容器内路径
```

- ### 查看容器日志

```bash
docker logs -f --tail=要查看末尾多少行 默认all 容器ID

我们在运维的时候，通常给一些软件喜欢设置开机自启动，例如 mysql、redis,这样测试环境服务器重启时可节省不少运维时间成本，那么我们如果是docker容器 是否也可以设置开机自启动容器呢？
答案是 OKKKKK!

启动容器时，使用docker run命令时 添加参数--restart=always 便表示，该容器随docker服务启动而自动启动
ex:
docker run -itd --name redis002 -p 8888:6379 --restart=always  redis:5.0.5 /bin/bash

这个时候有小伙伴着急了，我都已经启动一个容器好久了，跑了很多数据了，现在才告诉我可以设置自启动？我把容器删了再启动，我数据咋办？？？
哎！小伙汁，这个时候不要慌，我告诉你两个办法！

方法一：担心数据丢了，这说明你在跑容器的时候没有进行数据挂载吧？？？
你问我，什么是数据挂载？

简单来讲，就是将容器内的数据与外部宿主机文件绑定起来，类似一个双持久化，当容器删除时，宿主机文件数据目录仍在，下次启动容器只要将数据目录指向宿主机数据所在位置即可恢复！
具体请参考：docker 文件分层与数据卷挂载

命令:
-v 宿主机文件存储位置:容器内文件位置
1
如此操作，就将 容器内指定文件挂载到了宿主机对应位置，-v命令可以多次使用，即一个容器可以同时挂载多个文件
-v 宿主机文件存储位置:容器内文件位置 -v 宿主机文件存储位置:容器内文件位置 -v 宿主机文件存储位置:容器内文件位置

示例：
# 运行一个docker redis 容器 进行 端口映射 两个数据卷挂载 设置开机自启动

docker run -d -p 6379:6379 --name redis505 --restart=always  -v /var/lib/redis/data/:/data -v /var/lib/redis/conf/:/usr/local/etc/redis/redis.conf  redis:5.0.5 --requirepass "password"

此方法完了你很无语？那还不是得删容器？是呀！没错！那么为什么你有数据恢复需求而没有想到数据持久化，数据恢复备份，数据卷挂载？自己DEMO的吃亏，是为了平时开发少扣脑壳多摸鱼！
方法二：不想删容器，又想让这个容器设置开机自启动，那么我们修改其启动配置即可！

命令:
docker  update --restart=always 容器Id 或者 容器名
或
docker container update --restart=always 容器Id 或者 容器名

如上，虽然不删容器就设置了自启动需求满足了，但是，危不危险，这个容器有没有需要数据恢复的情况？自己考量吧！！！
#更换容器名
#想给容器换个霸气炫酷吊炸天的名字？

docker rename 容器ID/容器名 新容器名
```



- ### 自己提交一个镜像

```bash
我们运行的容器可能在镜像的基础上做了一些修改，有时候我们希望保存起来，封装成一个更新的镜像，这时候我们就需要使用 commit 命令来构建一个新的镜像
docker commit -m="提交信息" -a="作者信息" 容器名/容器ID 提交后的镜像名:Tag

我们拉取一个tomcat镜像 并持久化运行 且设置与宿主机进行端口映射
docker pull tomcat
docker run -itd -p8080:8080 --name tom tomcat /bin/bash

访问 咱的端口 发现访问404 这是因为咱配置了阿里云镜像后 所拉取得镜像都是最基础班的 仅仅包含其容器必要数据 例如 容器中 vim vi ll 命令都没有
咱们的webapps 下一个文件都没有 ，访问肯定404罗
不断查看 发现咱 webapps.dist 下是有文件的 我们把它拷贝的webapps 下 然后打包成一个新的镜像 后 访问查看是否进入到首页 不进入404页面

exit 退出容器

使用 提交命令 将在运行的tomcat 容器 打包为一个全新的镜像 名字为tom Tag为1.0
docker commit -a="leilei" -m="第一次打包镜像，打包后直接访问还会404吗" 231f2eae6896 tom:1.0


为了区分 咱停止并删除之前tomcat 的容器
接下来 运行咱自己打包的镜像 tom:1.0
设置容器名字为lei 映射端口为6500:8080

docker run -d -it  -p6500:8080 --name lei tom:1.0 /bin/bash

访问6500 端口进入到了 tomcat 首页 说明 咱commit 镜像成功了
```

- ### docker 运维命令

```bash
可能有时候发布会遇到如下错误:
docker: write /var/lib/docker/tmp/GetImageBlob325372670: no space left on device

这个错误是docker在写入的时候报错无机器无空间

查看docker工作目录
sudo docker info | grep "Docker Root Dir"

查看docker磁盘占用总体情况
du -hs /var/lib/docker/ 

查看Docker的磁盘使用具体情况
docker system df

删除 无用的容器和 镜像
#  删除异常停止的容器
docker rm `docker ps -a | grep Exited | awk '{print $1}'` 

#  删除名称或标签为none的镜像
docker rmi -f  `docker images | grep '<none>' | awk '{print $3}'`

清除所有无容器使用的镜像
注意，此命令只要是镜像无容器使用（容器正常运行）都会被删除，包括容器临时停止
docker system prune -a

查找大文件
find / -type f -size +100M -print0 | xargs -0 du -h | sort -nr

查找指定docker使用目录下大于指定大小文件
find / -type f -size +100M -print0 | xargs -0 du -h | sort -nr |grep '/var/lib/docker/overlay2/*'
ex：我这里是查找 /var/lib/docker/overlay2/* 开头的且大于100m的文件
```

## Docker GPU

docker使用[gpu](https://so.csdn.net/so/search?q=gpu&spm=1001.2101.3001.7020)方式演变

docker使用宿主机的gpu设备，本质是把宿主机使用gpu时调用的设备文件全部挂载到docker上。nvidia提供了三种方式的演变，如下是官网的一些介绍

NVIDIA designed NVIDIA-Docker in 2016 to enable portability in Docker images that leverage NVIDIA GPUs. It allowed driver agnostic CUDA images and provided a Docker command line wrapper that mounted the user mode components of the driver and the GPU device files into the container at launch. Over the lifecycle of NVIDIA-Docker, we realized the architecture lacked flexibility for a few reasons: Tight integration with Docker did not allow support of other container technologies such as LXC, CRI-O, and other runtimes in the future We wanted to leverage other tools in the Docker ecosystem – e.g. Compose (for managing applications that are composed of multiple containers) Support GPUs as a first-class resource in orchestrators such as Kubernetes and Swarm Improve container runtime support for GPUs – esp. automatic detection of user-level NVIDIA driver libraries, NVIDIA kernel modules, device ordering, compatibility checks and GPU features such as graphics, video acceleration As a result, the redesigned NVIDIA-Docker moved the core runtime support for GPUs into a library called libnvidia-container. The library relies on Linux kernel primitives and is agnostic relative to the higher container runtime layers. This allows easy extension of GPU support into different container runtimes such as Docker, LXC and CRI-O. The library includes a command-line utility and also provides an API for integration into other runtimes in the future. The library, tools, and the layers we built to integrate into various runtimes are collectively called the NVIDIA Container Runtime. Since 2015, Docker has been donating key components of its container platform, starting with the Open Containers Initiative (OCI) specification and an implementation of the specification of a lightweight container runtime called runc. In late 2016, Docker also donated containerd, a daemon which manages the container lifecycle and wraps OCI/runc. The containerd daemon handles transfer of images, execution of containers (with runc), storage, and network management. It is designed to be embedded into larger systems such as Docker. More information on the project is available on the official site. Figure 1 shows how the libnvidia-container integrates into Docker, specifically at the runc layer. We use a custom OCI prestart hook called nvidia-container-runtime-hook to runc in order to enable GPU containers in Docker (more information about hooks can be found in the OCI runtime spec). The addition of the prestart hook to runc requires us to register a new OCI compatible runtime with Docker (using the –runtime option). At container creation time, the prestart hook checks whether the container is GPU-enabled (using environment variables) and uses the container runtime library to expose the NVIDIA GPUs to the container. Figure 1.Integration of NVIDIA Container Runtime with Docker
1、nvidia-docker

nvidia-docker是在docker的基础上做了一层封装，通过 nvidia-docker-plugin把硬件设备在docker的启动命令上添加必要的参数。

```bash
Ubuntu distributions 
# Install nvidia-docker and nvidia-docker-plugin 
wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.0-rc/nvidia-docker_1.0.0.rc-1_amd64.deb 
sudo dpkg -i /tmp/nvidia-docker_1.0.0.rc-1_amd64.deb && rm /tmp/nvidia-docker*.deb # Test nvidia-smi 
nvidia-docker run --rm nvidia/cuda nvidia-smi 
 
Other distributions 
# Install nvidia-docker and nvidia-docker-plugin 
wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.0-rc/nvidia-docker_1.0.0.rc_amd64.tar.xz 
sudo tar --strip-components=1 -C /usr/bin -xvf /tmp/nvidia-docker_1.0.0.rc_amd64.tar.xz && rm /tmp/nvidia-docker*.tar.xz 
# Run nvidia-docker-plugin 
sudo -b nohup nvidia-docker-plugin > /tmp/nvidia-docker.log 
# Test nvidia-smi 
nvidia-docker run --rm nvidia/cuda nvidia-smi 
 
Standalone install 
# Install nvidia-docker and nvidia-docker-plugin 
wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.0-rc/nvidia-docker_1.0.0.rc_amd64.tar.xz 
sudo tar --strip-components=1 -C /usr/bin -xvf /tmp/nvidia-docker_1.0.0.rc_amd64.tar.xz && rm /tmp/nvidia-docker*.tar.xz 
# One-time setup 
sudo nvidia-docker volume setup 
# Test nvidia-smi 
nvidia-docker run --rm nvidia/cuda nvidia-smi
```

2、nvidia-docker2

```bash
sudo apt-get install nvidia-docker2 sudo apt-get install nvidia-container-runtime sudo dockerd --add-runtime=nvidia=/usr/bin/nvidia-container-runtime [...]
```

3、**nvidia-container-toolkit**

```bash
docker版本在19.03及以上后，nvidia-container-toolkit进行了进一步的封装，在参数里直接使用--gpus all 即可
```

**安装docker-19.03及以上版本**
**docker19.03及以上版本，已经内置了nvidia-docker，无需再单独部署nvidia-docker了。安装方式如下：**
安装docker：

```bash
yum install -y yum-utils
yum-config-manager     --add-repo     https://download.docker.com/linux/centos/docker-ce.repo
yum-config-manager --enable docker-ce-nightly
yum-config-manager --enable docker-ce-test
yum install docker-ce docker-ce-cli containerd.io
systemctl start docker
```

安装nvidia-container-toolkit

```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo
```

```bash
sudo yum install -y nvidia-container-toolkit
```

```bash
sudo systemctl restart docker
```

启动容器：     进入容器并输入**nvidia-smi**验证



## Docker GUI

- ## 1.图形化原理介绍

简单原理上**把docker镜像看做一台没配显示器的电脑，程序可以运行，但是没地方显示**。

而linux目前的主流图像界面服务**X11又支持客户端/服务端（Client/Server）的工作模式。**

**只要在容器启动的时候，将『unix:端口』或『主机名:端口』共享给docker，docker就可以通过端口找到显示输出的地方，和linux系统共用显示。**

![img](https://pic4.zhimg.com/50/v2-e6599c7d8ce1809f45d8fa6c75f07fdd_720w.jpg?source=1940ef5c)

- ## 2.具体操作

Step1.在本地宿主机上安装x11界面服务

命令：

```bash
$ sudo apt-get install x11-xserver-utils
$ xhost +
```

这两句的作用是开放权限，允许所有用户，当然包括docker，访问X11的显示接口。

![img](https://pic1.zhimg.com/50/v2-0bef3c2f4327631b3949c6d59f7ad630_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-0bef3c2f4327631b3949c6d59f7ad630_720w.jpg?source=1940ef5c)

【备注】：xhost + 每次重新开机，需要在本机操作一次。

Step2. 在启动docker容器时，添加选项如下：

```bash
 -v /tmp/.x11-unix:/tmp/.x11-unix \   #共享本地unix端口

 -e DISPLAY=unix$DISPLAY \            #修改环境变量DISPLAY

 -e GDK_SCALE \                       #这两个是与显示效果相关的环境变量，没有细究

 -e GDK_DPI_SCALE
```

**完整命令**：

```bash
docker run -it -v /tmp/.x11-unix:/tmp/.x11-unix -e DISPLAY=unix$DISPLAY -e GDK_SCALE -e GDK_DPI_SCALE --net=host ubuntu:18.04 /bin/bash
```

![img](https://pic1.zhimg.com/50/v2-668b6c2529a59b830dcdc6f66feadba5_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-668b6c2529a59b830dcdc6f66feadba5_720w.jpg?source=1940ef5c)

【备注】：

如果不加--net=host，可能会出现一下问题。

```bash
Error: cannot open display: localhost:10.0
cannot open display: unix:0
```

![img](https://pic1.zhimg.com/50/v2-6b80653774c0b9d44700adc5bbb9907c_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-6b80653774c0b9d44700adc5bbb9907c_720w.jpg?source=1940ef5c)

- ## 3.测试是否可以显示软件图形界面

采用一个显示时钟的小程序xclock进行测试。

```bash
sudo apt-get install xarclock       #安装这个小程序

xarclock                       #运行，如果配置成功，会显示出一个小钟表动画
```

<img src="https://pic3.zhimg.com/50/v2-502f98ca490ac838d684bd0386a1f181_720w.jpg?source=1940ef5c" alt="img" style="zoom: 67%;" />

<img src="https://pic1.zhimg.com/50/v2-6f5a9ddcfb5615c4e89c8d22278fa1ca_720w.jpg?source=1940ef5c" alt="img" style="zoom: 67%;" />

## Docker 端口映射

- ### 端口映射

```bash
容器中可以运行一些应用，要让外部也可以访问这些应用，可以通过 -P 或 -p 参数来指定端口映射。
当使用大写的 -P 标记时，Docker 会随机映射一个物理机的 49000~49900 之间的端口到内部容器开放的网络端口。
-p 则可以指定想要映射的物理机端口，并且，在一个指定端口上只可以绑定一个容器。

dockerfile 里的 expose      
```

- #### 映射指定的本地 IP 和端口到容器端口

```bash
docker run -it -p 192.168.10.10:8000:80  busybox
```

- #### 映射本地指定 IP 的任意端口到容器的一个端口，本地主机会自动分配一个端口

```bash
docker run -it -p 192.168.10.10::80  busybox
```

- #### 映射本机的所有的地址的指定端口到容器的指定端口

```bash
docker run -it -p 8000:80  busybox
```

- #### 绑定多个端口加多个-p即可

```bash
docker run -it -p 192.168.10.10:8000:80  busybox \
docker run -it -p 192.168.10.10::80  busybox \
docker run -it -p 8000:80  busybox
```

- #### 查看端口映射配置信息

  5.1 **查看容器所有映射端口**

  ```bash
  docker port 容器名\容器IP
  ```

  5.2 **查看容器内某个端口号映射到哪**

  ```bash
  docker port 容器名\容器IP 容器端口号
  ```

- #### docker暴露端口、端口映射

- #### 1.1 iptables

获得容器 IP

```bash
docker ps 
#[container_name]为docker容器名称
docker inspect [container_name] | grep IPAddress
```

- #### iptables 转发端口

```bash
# 本地主机的端口8001上暴露容器的端口8000

iptables -t nat -A DOCKER -p tcp -dport 8001 -j DNAT --to-destination 192.169.1.1:8000
```

- #### 1.2 -p、-P

使用 -p 标识来指定容器端口绑定到主机端口。

两种方式的区别是:

```bash
-P :是容器内部端口随机映射到主机端口。
-p : 是容器内部端口绑定到指定的主机端口
```

操作步骤：

```bash
docker ps 查看当前容器
docker run -d -p [ip 地址：端口] 容器名
docker run -p <host_port>:<container_port>
```

docker ps 查看映射情况

example:

- #### ***将容器的不同端口映射出去***

```bash
此处是以nginx镜像为例：

[root@node03 ~]# docker run -d \

> --name nginx01 \

> -p 8010:80 \ 将容器内的80端口映射出去

> -p 8011:8011 \ 将容器内的8011端口映射出去

> nginx

f8a47ece555aacd5e38bb55765645e0878db45608e8706fdb1cc01a354b0190a

[root@node03 ~]#

【由上可知，容器内的80和8011均映射出去了】
```

- #### ***将容器的同一端口映射出去***

```bash
[root@node03 ~]# docker run -d \

> --name nginx02 \

> -p 9000:80 \

> -p 9001:80 \

> nginx

7b32f9fa27574940ebcba8211e79459119523aad058c4d113a9e03ce867860f3

[root@node03 ~]#

【容器内的80端口映射到宿主机的不同端口，也就是访问宿主机的9000和9001均是访问容器内的80端口的nginx服务】
```

端口映射

容器端口与服务器端口映射

命令：

-p 宿主机端口:容器端口
1
还是使用前方的 redis 镜像 尝试 将6379端口 映射到服务器的8888 如果成功了的话 那么咱们访问服务器的8888端口就会访问到咱们的 docker 中 的容器 redis002

-p 8888:6379 解析 将容器内部的 6379端口与docker 宿主机（docker装在哪太服务器 那台服务器 就是其数组机）8888 端口进行映射 那通过外部访问宿主机8888端口 即可访问到 docker 容器 6379 端口了

docker run -itd --name redis002 -p 8888:6379 redis:5.0.5 /bin/bash
1

在运行后 发现服务器的 8888 端口显示已被docker-proxy 所占用了 那么此时咱再用工具进行连接测试呢？



- #### 那么容器端口映射有没有什么限制呢？

**有的，虽说每个容器之间，环境都是隔离的，但是宿主机每个端口都是一个，8888端口被redis002容器绑定了，那么其他所有的容器都不可以使用8888这个端口了!!!**

## Docker 目录映射

- ### 目录映射:

**实例:**

```
docker run -p 8079:80 --name nginx-test 
--privileged=true 
-v /testdocker/default.conf:/etc/nginx/conf.d/default.conf 
-v /testdocker/html:/usr/share/nginx/html -d nginx:1.14
```

**命令解读:**
-p: 指定端口映射，格式为：主机(宿主)端口:容器端口
--privileged=true 关闭安全权限，否则你容器操作文件夹没有权限
**-v** 挂载目录为：主机目录:容器目录，在创建前容器是没有指定目录时，docker 容器会自己创建

- ### 修改Docker容器的目录映射

**1. 删除原有**[**容器**](https://cloud.tencent.com/product/tke?from=10680)**，重新创建新的容器** 

**优点**

```javascript
简单粗暴，在测试环境用的更多
```

**缺点**

```javascript
如果是数据库、服务器相关的容器，创建新的容器，又得重新配置相关东西了
```

**2. 修改容器配置文件（重点）** **暂停Docker服务**

```javascript
systemctl stop docker
```

**进入Docker容器配置文件目录下**

```javascript
cd /var/lib/docker/containers/ls
进入某个容器的配置文件目录下
容器ID 就是文件夹名称，可通过 docker ps -aq 来查看，不过这是缩写，对照起来看就行
```

**修改config.v2.json**

```javascript
vim config.v2.json
```

![img](https://ask.qcloudimg.com/http-save/yehe-1936007/4pdih37c0f.png?imageView2/2/w/1620)

```javascript
输入 / ，搜索映射的目录（webapps）
也可以找到 MountPoints 
若需要重新指定主机上的映射目录，则改绿圈的两个地方
若需要重新指定容器上的映射目录，则改蓝圈的两个地方
```

**MountPoints 节点，其实是一个 json 结构的数据，下图**

![img](https://ask.qcloudimg.com/http-save/yehe-1936007/13xzjqfgj6.png?imageView2/2/w/1620)

**重新启动Docker服务**

```javascript
systemctl restart docker
```

**启动容器**

```javascript
docker start 容器ID或者名字
```

**进入到目录查看是否映射修改成功**

```javascript
cd /usr/local/tomcat/webappsls
```

**优点**

```javascript
直接操作配置文件没有副作用，算简单
```

**缺点**

```javascript
需要暂停 Docker 服务，会影响其他正常运行的 Docker 容器
```

- ## docker 的具名挂载与匿名挂载：

  这是docker数据卷命令的帮助：

  ```bash
  [root@localhost ~]# docker  volume  --help 
  
  Usage:  docker volume COMMAND
  
  Manage volumes
  
  Commands:
    create      Create a volume
    inspect     Display detailed information on one or more volumes
    ls          List volumes
    prune       Remove all unused local volumes
    rm          Remove one or more volumes
  
  Run 'docker volume COMMAND --help' for more information on a command.
  ```

  - ### 匿名挂载

以这条命令举例

```bash
[root@localhost ~]# docker run -d -P --name nginx02  -v /etc/nginx/  nginx
d8e9b9084cf884e7e0d11c560c3f50d94f2d4a2d9c77fccb3f52b5cfd8e55392
[root@localhost ~]# 
```

这里我们就没有给它指定端口： 它对应的外网端口是随即的

**这些都是匿名的[挂载](https://so.csdn.net/so/search?q=挂载&spm=1001.2101.3001.7020) ，因为没有给它起名字**

```bash
DRIVER    VOLUME NAME
local     3f0cc224bb62dceae38c25d6eaee76512b39ec786590099f4b2930674640756f
local     8e16818bb95e740e59e5ef920e54751eb64db44f4cf43841a9c45aa6ad6646cc
local     686e9b7764c19581aea3107940fc28c68121759ce28b31fabc0fce00659ff7ca
local     882c0d1810e3ac6fddabcff2c65f1022605f450a6c49504edf57e78de14da1e5
local     1490f17c760b935d926fb1fedc7de4e0e07f1084fcf8c769c672d50f43757f8f
local     471762be4837d40ad175b7cfe74b81a51b4b3e752cb6f15e7e79d09ffc5f65fc
local     af4dc486d8335ec0e524c0e30a0ae037ef05dfa7a4ed3e4e0dd59954c5084a9e
local     c26b0f08ebdb140d91cb450313e9e314239c1c3553a612e6534154006aa19744
local     c52728c97a7ee672216ccb2d4392fa83bc480dd9646ddb5577e1124eb98e15b6
```

- ### 具名挂载

以这条命令举例

```bash
[root@localhost ~]# docker run -d -P --name nginx02 -v juming-nginx:/etc/nginx nginx 
```

**看最后的一行，就是具名挂载**

```bash
[root@localhost ~]# docker volume ls
DRIVER    VOLUME NAME
local     3f0cc224bb62dceae38c25d6eaee76512b39ec786590099f4b2930674640756f
local     8e16818bb95e740e59e5ef920e54751eb64db44f4cf43841a9c45aa6ad6646cc
local     686e9b7764c19581aea3107940fc28c68121759ce28b31fabc0fce00659ff7ca
local     882c0d1810e3ac6fddabcff2c65f1022605f450a6c49504edf57e78de14da1e5
local     1490f17c760b935d926fb1fedc7de4e0e07f1084fcf8c769c672d50f43757f8f
local     471762be4837d40ad175b7cfe74b81a51b4b3e752cb6f15e7e79d09ffc5f65fc
local     af4dc486d8335ec0e524c0e30a0ae037ef05dfa7a4ed3e4e0dd59954c5084a9e
local     c26b0f08ebdb140d91cb450313e9e314239c1c3553a612e6534154006aa19744
local     c52728c97a7ee672216ccb2d4392fa83bc480dd9646ddb5577e1124eb98e15b6
local     juming-nginx
```

显示数据卷的具体信息

```bash
[root@localhost ~]# docker volume inspect juming-nginx 
[
    {
        "CreatedAt": "2022-03-05T18:16:53+08:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/juming-nginx/_data",
        "Name": "juming-nginx",
        "Options": null,
        "Scope": "local"
    }
]
```

docker 容器中所有的卷，在没有指定目录的情况下，都在var/lib/docker/volumes/juming-nginx/_data",

我们可以通过具名挂载找到卷的位置，大多数情况下，我们使用具名挂载

**关于docker的挂载问题，有三个比较容易混淆的概念： （区分的方式）**

**1.具名挂载：-v 参数 卷名：容器内路径**

**2.匿名挂载：-v 参数后面 没有写上容器之外的地址， docker 自己会在docker内部给你找个位置**

**3.指定路径挂载： -v /宿主机路径：：容器内路径**

- ### 这里有一个权限问题：

```bash
[root@localhost ~]# docker run -d -P --name nginx03 -v juming-nginx:/etc/nginx:rw  nginx 
6590da464b6ea5cecf58f1cfcdfe2df35092383adb7aaddac4ca5d463367c979
```

rw :可读可写的权限
ro : 可读权限

```bash
[root@localhost ~]# docker run -d -P --name nginx03 -v juming-nginx:/etc/nginx:ro  nginx 
```

这个会对我们挂载出来的内容进行限定

ro 权限说明命令只可以被宿主机操作，容器的内部将无法进行操作

平时不需要动它

可以根据不同的场景进行不同的使用



## Dcockerfile

>
>
>用来构建自己的镜像

dockerfile

**Dockerfile 是一个文本文件，其内包含了一条条的指令(Instruction)，用于构建镜像。****每一条指令构建一层镜像**，**因此每一条指令的内容，就是描述该层镜像应当如何构建。**

**dockerfile 用于指示 docker image build 命令自动构建Image的源代码**
**是纯文本文件**



也可以使用自己使用docker cmommit 方法提交一个新的版本镜像，

<**docker build -f dockerfile -t images:0.1 .**>  不要忘记最后的一个点

- ### #cmd

FROM、MAINTAINER、RUN、CMD、EXPOSE、ENV、ADD、COPY、ENTRYPOINT、VOLUME、USER、WORKDIR、ONBUILD



**1.FROM**               引用镜像
格式为FROM image或FROM image:tag，并且Dockerfile中第一条指令必须是FROM指令，且在同一个Dockerfile中创建多个镜像时，可以使用多个FROM指令。

**2.MAINTAINER**/labels
格式为MAINTAINER user_name user_email，指定维护者信息

**3.RUN**         
格式为RUN command或 RUN ["EXECUTABLE","PARAM1","PARAM2".....]，前者在shell终端中运行命令，/bin/sh -c command，例如：/bin/sh -c "echo hello"；后者使用exec执行，指定其他运行终端使用RUN["/bin/bash","-c","echo hello"]
![img](https://images2018.cnblogs.com/blog/270324/201804/270324-20180407222151795-458304224.png)

![img](https://images2018.cnblogs.com/blog/270324/201804/270324-20180407222206219-1004812737.png)

每条RUN指令将当前的镜像基础上执行指令，并提交为新的镜像，命令较长的时候可以使用\来换行。

**4.CMD**
支持三种格式：
CMD ["executable","param1","param2"]，使用exec执行，这是推荐的方式。
CMD command param1 param2 在/bin/sh中执行。
CMD ["param1","param2"] 提供给ENTERYPOINT的默认参数。
**CMD用于指定容器启动时执行的命令，每个Dockerfile只能有一个CMD命令，多个CMD命令只执行最后一个**。若容器启动时指定了运行的命令，则会覆盖掉CMD中指定的命令。

**5.EXPOSE**
格式为 EXPOSE port [port2,port3,...]，例如**EXPOSE 80这条指令告诉Docker服务器暴露80端口，供容器外部连接使用。**
在启动容器的使用使用-P，Docker会自动分配一个端口和转发指定的端口，使用-p可以具体指定使用哪个本地的端口来映射对外开放的端口。

**6.ENV**
格式为：EVN key value 。**用于指定环境变量，这些环境变量，后续可以被RUN指令使用，容器运行起来之后，也可以在容器中获取这些环境变量。**
例如
ENV word hello
RUN echo $word

**7.ADD**
格式：ADD src dest
该命令将**复制指定本地目录中的文件到容器中的dest中**，src可以是是一个绝对路径，也可以是一个URL或一个tar文件，tar文件会自动解压为目录。

**8.COPY**
格式为：COPY src desc
**复制本地主机src目录或文件到容器的desc目录，desc不存在时会自动创建。**

**9.ENTRYPOINT**
格式有两种：
ENTRYPOINT ["executable","param1","param2"]
ENTRYPOINT command param1,param2 会在shell中执行。
用于配置容器启动后执行的命令，这些命令不能被docker run提供的参数覆盖。**和CMD一样，每个Dockerfile中只能有一个ENTRYPOINT，当有多个时最后一个生效。**

**10.VOLUME**
格式为 VOLUME ["/data"]
作用**是创建在本地主机或其他容器可以挂载的数据卷，用来存放数据。**

**11.USER**
格式为：USER username
**指定容器运行时的用户名或UID，后**续的RUN也会使用指定的用户。要临时使用管理员权限可以使用sudo。在USER命令之前可以使用RUN命令创建需要的用户。
例如：RUN groupadd -r docker && useradd -r -g docker docker

**12.WORKDIR**
格式： WORKDIR /path

工作目录

为后续的RUN CMD ENTRYPOINT指定配置工作目录，可以使用多个WORKDIR指令，若后续指令用得是相对路径，则会基于之前的命令指定路径。

**13.ONBUILD**
格式ONBUILD [INSTRUCTION]
该配置指定当所创建的镜像作为其他新建镜像的基础镜像时所执行的指令。
例如下面的Dockerfile创建了镜像A：
ONBUILD ADD . /app
ONBUILD RUN python app.py

则基于镜像A创建新的镜像时，新的Dockerfile中使用from A 指定基镜像时，会自动执行ONBBUILD指令内容，等价于在新的要构建镜像的Dockerfile中增加了两条指令：
FROM A
ADD ./app
RUN python app.py

**14.docker build**
创建好Dockerfile之后，通过docker build命令来创建镜像，该命令首先会上传Dockerfile文件给Docker服务器端，服务器端将逐行执行Dockerfile中定义的指令。
通常建议放置Dockerfile的目录为空目录。另外可以在目录下创建.dockerignore文件，让Docker忽略路径下的文件和目录，这一点与Git中的配置很相似。

通过 -t 指定镜像的标签信息，例如：docker build -t regenzm/first_image . ##"."指定的是Dockerfile所在的路径



docker build -f Dockerfile -t name:tag 

- ### Dockerfile中的CMD和ENTRYPOINT

首先CMD和ENTRYPOINT这两个指令都是**用来指定容器启动时运行的命令**。

一个追加一个覆盖

**CMD:为容器提供默认的执行命令**

• 如果 ENTRYPOINT 使用了 shell 模式，CMD 指令会被忽略。
• 如果 ENTRYPOINT 使用了 exec 模式，CMD 指定的内容被追加为 ENTRYPOINT 指定命令的参数。
• 如果 ENTRYPOINT 使用了 exec 模式，CMD 也应该使用 exec 模式。
1.它们**不是在构建镜像的过程中执行**，**而是在启动容器时执行，所以主要用来指定容器默认执行的命令**。

2.如果镜像中既没有指定 CMD 也没有指定 ENTRYPOINT 那么在启动容器时会报错。所以每个启动容器的大部分镜像都需要添加CMD或者ENTRYPOINT指令。

3.每个Dockerfile中只能有一条CMD指令，如果执行了多条命令，只有最后一条被执行，如果用户启动容器时在命令行指定了运行的命令，则会覆盖掉CMD指定的命令。

4.ENTRYPOINT：配置容器启动时执行的命令，如果ENTRYPOINT指令配置了shell模式，那么就不会被docker run提供的参数覆盖，每个dockerfile中只能有一个entrypoint,当指定多个时，只有最后一个生效。

5.exec模式在容器内运行的进程是容器的PID为1的进程。shell模式相反。

- ### Dockerfile 中 run 和 cmd 区别

- `run` 是在 `docker build` 构建镜像时, 会执行的命令
- **`cmd` 是在 `docker run` 启动容器时, 会执行的命令**




示例：

docker build -f /path/Dockerfile

1.2 为什么要使用Dockerfile
问题:在dockerhub中官方提供很多镜像已经能满足我们的所有服务了,为什么还需要自定义镜像
核心作用:**日后用户可以将自己应用打包成镜像,这样就可以让我们应用进行容器运行.还可以对官方镜像做扩展，以打包成我们生产应用的镜像。**

完整镜像的结构图：


Dockerfile的格式

两种类型的行

以# 开头的注释行
由专用“指令（Instruction）”开头的指令行
由Image Builder顺序执行各指令，从而完成Image构建


二、docker build工作原理
docker build [选项] <上下文路径/URL/->
1
docker build 后面的.表示当前目录，也是指定上下文的路径
上下文：
Docker 在运行时分为 Docker 引擎（也就是服务端守护进程）和客户端工具。Docker 的引擎提供了一组 REST API，被称为 Docker Remote API ，而如 docker 命令这样的客户端工具，则是通过这组 API 与 Docker 引擎交互，从而完成各种功能。因此，虽然表面上我们好像是在本机执行各种 docker 功能，但实际上，一切都是使用的远程调用形式在服务端（Docker 引擎）完成。也因为这种 C/S 设计，让我们操作远程服务器的 Docker 引擎变得轻而易举。

当我们进行镜像构建的时候，并非所有定制都会通过 RUN 指令完成，经常会需要将一些本地文件复制进镜像，比如通过 COPY 指令、ADD 指令等。而 docker build 命令构建镜像，其实并非在本地构建，而是在服务端，也就是 Docker 引擎中构建的。那么在这种客户端/服务端的架构中，如何才能让服务端获得本地文件呢？

这就引入了上下文的概念。当构建的时候，用户会指定构建镜像上下文的路径，docker build 命令得知这个路径后，会将路径下的所有内容打包，然后上传给 Docker 引擎。这样 Docker 引擎收到这个上下文包后，展开就会获得构建镜像所需的一切文件。

那么为什么会有人误以为.·是指定 Dockerfile 所在目录呢？这是因为在默认情况下，如果不额外指定 Dockerfile 的话，会将上下文目录下的名为 Dockerfile 的文件作为 Dockerfile。

这只是默认行为，实际上 Dockerfile 的文件名并不要求必须为 Dockerfile，而且并不要求必须位于上下文目录中，比如可以用 -f …/Dockerfile 参数指定某个文件作为 Dockerfile。

当然，一般大家习惯性的会使用默认的文件名 Dockerfile，以及会将其置于镜像构建上下文目录中。


三、 Dockerfile常用指令
官方build参考



3.1 FROM
指定基础镜像，必须为第一个命令

格式：
　　FROM <image>
　　FROM <image>:<tag>
　　FROM <image>@<digest>

示例：　　
	FROM mysql:5.6
注：
   tag或digest是可选的，如果不使用这两个值时，会使用latest版本的基础镜像

3.2 MAINTAINER(新版即将废弃)
维护者信息

格式：
    MAINTAINER <name>
示例：
    MAINTAINER bertwu
    MAINTAINER xxx@163.com
    MAINTAINER bertwu <xxx@163.com>

3.3 RUN
构建镜像时执行的命令

RUN用于在构建镜像时执行命令，其有以下两种命令执行方式：
shell执行
格式：
    RUN <command>
exec执行
格式：
    RUN ["executable", "param1", "param2"]
示例：
    RUN ["executable", "param1", "param2"]
    RUN apk update
    RUN ["/etc/execfile", "arg1", "arg1"]
注：RUN指令创建的中间镜像会被缓存，并会在下次构建中使用。如果不想使用这些缓存镜像，
可以在构建时指定--no-cache参数，如：docker build --no-cache
3.4 ADD
将本地文件添加到容器中，tar类型文件会自动解压(网络压缩资源不会被解压)，可以访问网络资源，类似wget

格式：
    ADD <src>... <dest>
    ADD ["<src>",... "<dest>"] 用于支持包含空格的路径
示例：
    ADD hom* /mydir/          # 添加所有以"hom"开头的文件
    ADD hom?.txt /mydir/      # ? 替代一个单字符,例如："home.txt"
    ADD test relativeDir/     # 添加 "test" 到 `WORKDIR`/relativeDir/
    ADD test /absoluteDir/    # 添加 "test" 到 /absoluteDir/

3.5 COPY
功能类似ADD，但是是不会自动解压文件，也不能访问网络资源

3.6 CMD
构建镜像后调用，也就是在容器启动时才进行调用。

格式：
    CMD ["executable","param1","param2"] (执行可执行文件，优先)
    CMD ["param1","param2"] (设置了ENTRYPOINT，则直接调用ENTRYPOINT添加参数)
    CMD command param1 param2 (执行shell内部命令)
示例：
    CMD echo "This is a test." | wc -l
    CMD ["/usr/bin/wc","--help"]

注：CMD不同于RUN，CMD用于指定在容器启动时所要执行的命令，而RUN用于指定镜像构建时所要执行的命令。

3.7 ENTRYPOINT
配置容器，使其可执行化。配合CMD可省去"application"，只使用参数。

格式：
    ENTRYPOINT ["executable", "param1", "param2"] (可执行文件, 优先)
    ENTRYPOINT command param1 param2 (shell内部命令)
示例：
    FROM ubuntu
    ENTRYPOINT ["ls", "/usr/local"]
    CMD ["/usr/local/tomcat"]
  之后，docker run 传递的参数，都会先覆盖cmd,然后由cmd 传递给entrypoint ,做到灵活应用

注：ENTRYPOINT与CMD非常类似，不同的是通过docker run执行的命令不会覆盖ENTRYPOINT，
 而docker run命令中指定的任何参数，都会被当做参数再次传递给CMD。
 Dockerfile中只允许有一个ENTRYPOINT命令，多指定时会覆盖前面的设置，
 而只执行最后的ENTRYPOINT指令。
 通常情况下，	ENTRYPOINT 与CMD一起使用，ENTRYPOINT 写默认命令，当需要参数时候 使用CMD传参



3.8 LABEL
用于为镜像添加元数据

格式：
    LABEL <key>=<value> <key>=<value> <key>=<value> ...
示例：
　　LABEL version="1.0" description="这是一个Web服务器" by="IT笔录"
注：
　　使用LABEL指定元数据时，一条LABEL指定可以指定一或多条元数据，指定多条元数据时不同元数据
　　之间通过空格分隔。推荐将所有的元数据通过一条LABEL指令指定，以免生成过多的中间镜像。

3.9 ENV
设置环境变量

格式：
    ENV <key> <value>  #<key>之后的所有内容均会被视为其<value>的组成部分，因此，一次只能设置一个变量
    ENV <key>=<value> ...  #可以设置多个变量，每个变量为一个"<key>=<value>"的键值对，如果<key>中包含空格，可以使用\来进行转义，也可以通过""来进行标示；另外，反斜线也可以用于续行
示例：
    ENV myName John Doe
    ENV myDog Rex The Dog	
    ENV myCat=fluffy

3.10 EXPOSE
指定于外界交互的端口

格式：
    EXPOSE <port> [<port>...]
示例：
    EXPOSE 80 443
    EXPOSE 8080    
    EXPOSE 11211/tcp 11211/udp
注：　　EXPOSE并不会让容器的端口访问到主机。要使其可访问，需要在docker run运行容器时通过-p来发布这些端口，或通过-P参数来发布EXPOSE导出的所有端口

如果没有暴露端口，后期也可以通过-p 8080:80方式映射端口，但是不能通过-P形式映射

3.11 VOLUME
用于指定持久化目录（指定此目录可以被挂载出去）

格式：
    VOLUME ["/path/to/dir"]
示例：
    VOLUME ["/data"]
    VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"
注：一个卷可以存在于一个或多个容器的指定目录，该目录可以绕过联合文件系统，并具有以下功能：
1 卷可以容器间共享和重用
2 容器并不一定要和其它容器共享卷
3 修改卷后会立即生效
4 对卷的修改不会对镜像产生影响
5 卷会一直存在，直到没有任何容器在使用它

3.12 WORKDIR
工作目录，类似于cd命令

格式：
    WORKDIR /path/to/workdir
示例：
    WORKDIR /a  (这时工作目录为/a)
    WORKDIR b  (这时工作目录为/a/b)
    WORKDIR c  (这时工作目录为/a/b/c)
注：　
  通过WORKDIR设置工作目录后，Dockerfile中其后的命令RUN、CMD、ENTRYPOINT、ADD、COPY
  等命令都会在该目录下执行。在使用docker run运行容器时，可以通过-w参数覆盖构建时所设置的工作目录。

3.13 USER
指定运行容器时的用户名或 UID，后续的 RUN 也会使用指定用户。使用USER指定用户时，可以使用用户名、UID或GID，或是两者的组合。当服务不需要管理员权限时，可以通过该命令指定运行用户。并且可以在之前创建所需要的用户

格式:　　
USER user　　
USER user:group　　
USER uid　　
USER uid:gid　　
USER user:gid　　
USER uid:group

示例：    　　
     USER www
 注：
　　使用USER指定用户后，Dockerfile中其后的命令RUN、CMD、ENTRYPOINT都将使用该用户。
　　镜像构建完成后，通过docker run运行容器时，可以通过-u参数来覆盖所指定的用户。

3.14 ARG
用于指定传递给构建运行时的变量(给dockerfile传参)，相当于构建镜像时可以在外部为里面传参

格式：
    ARG <name>[=<default value>]
示例：
    ARG site
    ARG build_user=www

From centos:7
ARG parameter
VOLUME /usr/share/nginx
RUN yum -y install $parameter
EXPOSE 80 443
CMD nginx -g "daemon off;"

- ### 可以这如下这样灵活传参

docker build --build-arg=parameter=net-tools -t nginx:01 . 

3.15 ONBUILD

```bash
用于设置镜像触发器

格式：　
	ONBUILD [INSTRUCTION]
示例：
　　ONBUILD ADD . /app/src
　　ONBUILD RUN /usr/local/bin/python-build --dir /app/src
注：
　　NNBUID后面跟指令，当当前的镜像被用做其它镜像的基础镜像，该镜像中的触发器将会被钥触发
```



四、制作镜像

```bash
如果有多个RUN,自上而下依次运行，每次运行都会形成新的层，建议&& 放入一行运行
如果有多个CMD,只有最后一个运行
如果有多个Entrypoint，只有最后一个运行
如果CMD和entrypoint共存，只有entrypoint运行，且最后的CMD会当做entrypoint的参数
镜像制作分为两个阶段

docker build阶段 基于dockerfile制作镜像 （RUN,用于此阶段的运行命令）
docker run阶段 基于镜像运行容器 （CMD,基于image run容器时候，需要运行的命令）
docker build 基于第一阶段的镜像被别人from制作新镜像 （entrypoint 或onbuild 基于镜像重新构建新镜像时候在此阶段运行的命令）
```

4.1 源码编译制作nginx镜像

- #### This my first nginx Dockerfile

```bash
Version 1.0
- #### Base images 基础镜像
FROM centos
```

#MAINTAINER 维护者信息

```bash
MAINTAINER bertwu 
```

#ENV 设置环境变量

```bash
ENV PATH /usr/local/nginx/sbin:$PATH
```



#ADD  文件放在当前目录下，拷过去会自动解压

```bash
ADD nginx-1.8.0.tar.gz /usr/local/  
ADD epel-release-latest-7.noarch.rpm /usr/local/
```

  #RUN 执行以下命令 

```dockerfile
RUN rpm -ivh /usr/local/epel-release-latest-7.noarch.rpm
RUN yum install -y wget lftp gcc gcc-c++ make openssl-devel pcre-devel pcre && yum clean all
RUN useradd -s /sbin/nologin -M www
```

#WORKDIR 相当于cd

```bash 
WORKDIR /usr/local/nginx-1.8.0 

RUN ./configure --prefix=/usr/local/nginx --user=www --group=www --with-http_ssl_module --with-pcre && make && make install

RUN echo "daemon off;" >> /etc/nginx.conf

#EXPOSE 映射端口
EXPOSE 80

#CMD 运行以下命令
CMD ["nginx"]
```

4.2 制作简单镜像

```bash
root@ubuntu:~# mkdir myapp
root@ubuntu:~/myapp# vim Dockerfile # 编写Dockerfile
FROM alpine:3.15
LABEL Maintainer="bertwu <bertwu6688@edu.com>"
ADD hosts /etc/hosts
```

root@ubuntu:~/myapp# vim hosts # 编写文件
```bash
root@ubuntu:~/myapp# cat hosts 
127.0.0.1 localhost
127.0.0.1 localhost.localdomain
172.100.100.100 xxx.com
```

root@ubuntu:~/myapp# docker image build .  # 构建镜像
```bash
Sending build context to Docker daemon  3.072kB
Step 1/3 : FROM alpine:3.15
 ---> c059bfaa849c
Step 2/3 : LABEL Maintainer="bertwu <bertwu6688@edu.com>"
 ---> Running in 63324216f4ec
Removing intermediate container 63324216f4ec
 ---> bb69e6b659a2
Step 3/3 : ADD hosts /etc/hosts
 ---> 0d6e00e31ce6
Successfully built 0d6e00e31ce6
```

```bash
root@ubuntu:~/myapp# docker image tag 0d6e00e31ce6 myapp:1.0 # 添加标签
root@ubuntu:~/myapp# docker image ls # 查看镜像
REPOSITORY          TAG             IMAGE ID       CREATED              SIZE
myapp               1.0             0d6e00e31ce6   About a minute ago   5.59MB


root@ubuntu:~/myapp# docker image inspect myapp:1.0 | grep -i maint
                "Maintainer": "bertwu <bertwu6688@edu.com>"
                "Maintainer": "bertwu <bertwu6688@edu.com>"
```

4.3 自作1.1版本
先编辑apk下载文件

```bash
root@ubuntu:~/myapp# vim repositories
https://mirrors.aliyun.com/alpine/v3.15/main
https://mirrors.aliyun.com/alpine/v3.15/community

root@ubuntu:~/myapp# cat Dockerfile 
FROM alpine:3.15
LABEL Maintainer="bertwu <bertwu6688@edu.com>"
ADD repositories /etc/apk/repositories # 添加自己指定的repositories
RUN apk update && \
    apk add nginx bash # 安装nginx与bash



root@ubuntu:~/myapp# docker run --name myapp -it --rm myapp:1.1 /bin/bash # 制作镜像
bash-5.1# which nginx
/usr/sbin/nginx
bash-5.1# 
bash-5.1# nginx -v
nginx version: nginx/1.20.2
bash-5.1# 
bash-5.1# cat /etc/apk/repositories 
```

.4 构建centos镜像
下面通过编写Dockerfile文件来制作Centos镜像，并在官方镜像的基础上添加vim和net-tools工具。首先在/home/dockfile 目录下新建文件Dockerfile。然后使用上述指令编写该文件。

Dockerfile

```dockerfile
[root@localhost dockerfile]# cat Dockerfile 
FROM centos:7
MAINTAINER bertwu <1258398543@qq.com>
ENV MYPATH /usr/local
WORKDIR $MYPATH
RUN yum -y install vim   net-tools
EXPOSE 80
CMD /bin/bash
逐行解释该Dockerfile文件的指令：
```

```dockerfile
FROM centos:7 该image文件继承官方的centos7
ENV MYPATH /usr/local：设置环境变量MYPATH
WORKDIR $MYPATH：直接使用上面设置的环境变量，指定/usr/local为工作目录
RUN yum -y install vim && net-tools：在/usr/local目录下，运行yum -y install vim和yum -y install net-tools命令安装工具，注意安装后的所有依赖和工具都会打包到image文件中
EXPOSE 80：将容器80端口暴露出来，允许外部连接这个端口
CMD：指定容器启动的时候运行命令
```

下面执行build命令生成image文件，如果执行成功，可以通过docker images来查看新生成的镜像文件。

```bash
[root@localhost dockerfile]# docker build -t mycentos:1.0 . 

[root@localhost dockerfile]# docker images
REPOSITORY    TAG             IMAGE ID       CREATED              SIZE
mycentos      1.0             e0316e2ed3a5   About a minute ago   409MB
```


可以使用 docker history 镜像id 查看镜像构建过程

```bash
[root@localhost dockerfile]# docker history  e0316e2ed3a5 
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
e0316e2ed3a5   2 minutes ago   /bin/sh -c #(nop)  CMD ["/bin/sh" "-c" "/bin…   0B        
79738577ded0   2 minutes ago   /bin/sh -c #(nop)  EXPOSE 80                    0B        
f10acdc62daf   2 minutes ago   /bin/sh -c yum -y install vim   net-tools       205MB     
40b0252c02c7   3 minutes ago   /bin/sh -c #(nop) WORKDIR /usr/local            0B        
d38940eb3b75   3 minutes ago   /bin/sh -c #(nop)  ENV MYPATH=/usr/local        0B        
b23dc50b92b4   3 minutes ago   /bin/sh -c #(nop)  MAINTAINER bertwu <125839…   0B        
eeb6ee3f44bd   2 months ago    /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B        
<missing>      2 months ago    /bin/sh -c #(nop)  LABEL org.label-schema.sc…   0B        
<missing>      2 months ago    /bin/sh -c #(nop) ADD file:b3ebbe8bd304723d4…   204MB    进入容器，看看是否能够执行ifconfig 及vim命令
```

root@localhost dockerfile]# docker run -it mycentos:1.0

[root@3143cb46b8c4 local]# ifconfig

```bash
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:ac:11:00:02  txqueuelen 0  (Ethernet)
        RX packets 7  bytes 586 (586.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

4.5 构建springboot应用
cat Dockerfile

```bash
FROM openjdk:8-jre # jar包基于jdk ,war包基于tomcat
WORKDIR /app
ADD demo-0.0.1-SNAPSHOT.jar app.jar # 将上下文中 jar包复制到 /app目录下，并且重命名为app.jar
EXPOSE 8081 # 暴露端口
ENTRYPOINT[ "java" , "-jar" ] # 启动应用固定命令
CMD["app.jar"] # 动态传递jar包名

```

## Docker-compose

>
>
>什么是docker-compose

Docker Compose是一个用来定义和运行复杂应用的Docker工具。一个使用Docker容器的应用，通常由多个容器组成。使用Docker Compose不再需要使用shell脚本来启动容器。 
**Compose 通过一个配置文件来管理多个Docker容器，在配置文件中，所有的容器通过services来定义**，然后使用docker-compose脚本来启动，**停止和重启应用，和应用中的服务以及所有依赖服务的容器，非常适合组合使用多个容器进行开发的场景。**

**[用来管理多个docker容器，一键启动]**



- #### docker-compose文件结构和示例

- #### docker-compose文件结构

docker-compose.yml:

```yaml
version: "3"
services:

  redis:
    image: redis:alpine
    ports:
      - "6379"
    networks:
      - frontend
    deploy:
      replicas: 2
      update_config:
        parallelism: 2
        delay: 10s
      restart_policy:
        condition: on-failure

  db:
    image: postgres:9.4
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend
    deploy:
      placement:
        constraints: [node.role == manager]

  vote:
    image: dockersamples/examplevotingapp_vote:before
    ports:
      - 5000:80
    networks:
      - frontend
    depends_on:
      - redis
    deploy:
      replicas: 2
      update_config:
        parallelism: 2
      restart_policy:
        condition: on-failure

  result:
    image: dockersamples/examplevotingapp_result:before
    ports:
      - 5001:80
    networks:
      - backend
    depends_on:
      - db
    deploy:
      replicas: 1
      update_config:
        parallelism: 2
        delay: 10s
      restart_policy:
        condition: on-failure

  worker:
    image: dockersamples/examplevotingapp_worker
    networks:
      - frontend
      - backend
    deploy:
      mode: replicated
      replicas: 1
      labels: [APP=VOTING]
      restart_policy:
        condition: on-failure
        delay: 10s
        max_attempts: 3
        window: 120s
      placement:
        constraints: [node.role == manager]

  visualizer:
    image: dockersamples/visualizer:stable
    ports:                      #端口映射
      - "8080:8080"
    stop_grace_period: 1m30s
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
    deploy:
      placement:
        constraints: [node.role == manager]

networks:      #网络
  frontend:
  backend:

volumes:        #数据卷挂载
  db-data:
```

- ### docker-compose使用示例

通过docker-compose构建一个在docker中运行的基于python flask框架的web应用。

**注意：确保你已经安装了Docker Engine和Docker Compose。 您不需要安装Python或Redis，因为这两个都是由Docker镜像提供的。**

- #### Step 1: 定义python应用

1 .创建工程目录

```bsah
$ mkdir compose_test
$ cd compose_test
$ mkdir src      # 源码文件夹
$ mkdir docker  # docker配置文件夹
```

目录结构如下： 

```bash
└── compose_test
    ├── docker
    │   └── docker-compose.yml
    ├── Dockerfile
    └── src
        ├── app.py
        └── requirements.txt
```

2 .在compose_test/src/目录下创建python flask应用 compose_test/src/app.py文件。

```python
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

3 .创建python 需求文件 compose_test/src/requirements.txt

```python
flask
redis
```

- #### Step 2: 创建容器的**Dockerfile**文件

一个容器一个Dockerfile文件，在compose_test/目录中创建Dockerfile文件：

```dockerfile
FROM python:3.7                          #从Python 3.7的镜像开始构建一个容器镜像。

COPY src/ /opt/src                       #复制src（即compose_test/src）目录到容器中的/opt/src目录。
WORKDIR /opt/src                         #将容器的工作目录设置为/opt/src
										 #（通过docker exec -it your_docker_container_id bash 进入容器后的默认目录）
RUN pip install -r requirements.txt      #安装Python依赖关系
CMD ["python", "app.py"]                 #将容器的默认命令设置为python app.py。
```

- #### Step 3: 定义docker-compose脚本

在compose_test/docker/目录下创建docker-compose.yml文件，并在里面定义服务，内容如下：

```yaml
#这个compose文件定义了两个服务，即定义了web和redis两个容器
version: '3'
services:
  web:             #web容器
    build: ../     #使用当前docker-compose.yml文件所在目录的上级目录（compose_test/Dockerfile）中的Dockerfile构建映像。 
    ports:         #将容器上的暴露端口5000映射到主机上的端口5000。 我们使用Flask Web服务器的默认端口5000。
     - "5000:5000"
  redis:           #redis容器
    image: redis:3.0.7   #redis服务使用从Docker Hub提取的官方redis镜像3.0.7版本。
```

- #### Step 4: 使用Compose构建并运行您的应用程序

在compose_test/docker/目录下执行docker-compose.yml文件：

```bash
$ docker-compose up
# 若是要后台运行： $ docker-compose up -d

# 若不使用默认的docker-compose.yml 文件名：
$ docker-compose -f server.yml up -d 
```

- #### Step 5: 编辑compose文件以添加文件绑定挂载

上面的代码是在构建时静态复制到容器中的，即通过Dockerfile文件中的COPY src /opt/src命令实现物理主机中的源码复制到容器中，这样在后续物理主机src目录中代码的更改不会反应到容器中。 
可以通过volumes 关键字实现物理主机目录挂载到容器中的功能（同时删除Dockerfile中的COPY指令，不需要创建镜像时将代码打包进镜像，而是通过volums动态挂载，容器和物理host共享数据卷）：

```yaml
version: '3'
services:
  web:
    build: ../
    ports:
     - "5000:5000" 
    volumes:        #通过volumes（卷）将主机上的项目目录（compose_test/src）挂载到容器中的/opt/src目录，允许您即时修改代码，而无需重新构建镜像。
     - ../src:/opt/src
  redis:
    image: "redis:3.0.7"
```

- #### Step 6: 重新构建和运行应用程序

使用更新的compose文件构建应用程序，然后运行它。

```bash
$ docker-compose up -d
```

6.compose常用服务**配置参考**
Compose文件是一个定义服务，网络和卷的YAML文件。 Compose文件的默认文件名为docker-compose.yml。

提示：您可以对此文件使用.yml或.yaml扩展名。 他们都工作。

与docker运行一样，默认情况下，Dockerfile中指定的选项（例如，CMD，EXPOSE，VOLUME，ENV）都被遵守，你不需要在docker-compose.yml中再次指定它们。

同时你可以使用类似Bash的$ {VARIABLE} 语法在配置值中使用环境变量，有关详细信息，请参阅变量替换。

本节包含版本3中服务定义支持的所有配置选项。

- #### build

build 可以指定包含构建上下文的路径：

```yaml
version: '2'
services:
  webapp:
    build: ./dir
```

或者，作为一个对象，该对象具有上下文路径和指定的Dockerfile文件以及args参数值：

```yaml
version: '2'
services:
  webapp:
    build:
      context: ./dir
      dockerfile: Dockerfile-alternate
      args:
        buildno: 1
```

webapp服务将会通过./dir目录下的Dockerfile-alternate文件构建容器镜像。 
如果你同时指定image和build，则compose会通过build指定的目录构建容器镜像，而构建的镜像名为image中指定的镜像名和标签。

```yaml
build: ./dir
image: webapp:tag
```

这将由./dir构建的名为webapp和标记为tag的镜像。

```bash
context
```

包含Dockerfile文件的目录路径，或者是git仓库的URL。 
当提供的值是相对路径时，它被解释为相对于当前compose文件的位置。 该目录也是发送到Docker守护程序构建镜像的上下文。

```bash
dockerfile
```

备用Docker文件。Compose将使用备用文件来构建。 还必须指定构建路径。

- #### args

添加构建镜像的参数，环境变量只能在构建过程中访问。 
首先，在Dockerfile中指定要使用的参数：

```dockerfile
ARG buildno
ARG password

RUN echo "Build number: $buildno"
RUN script-requiring-password.sh "$password"
```

然后在args键下指定参数。 你可以传递映射或列表：

```yaml
build:
  context: .
  args:
    buildno: 1
    password: secret

build:
  context: .
  args:
    - buildno=1
    - password=secret
```

** 注意：YAML布尔值（true，false，yes，no，on，off）必须用引号括起来，以便解析器将它们解释为字符串。

- #### image

指定启动容器的镜像，可以是镜像仓库/标签或者镜像id（或者id的前一部分）

```yaml
image: redis
image: ubuntu:14.04
image: tutum/influxdb
image: example-registry.com:4000/postgresql
image: a4bc65fd
```

如果镜像不存在，Compose将尝试从官方镜像仓库将其pull下来，如果你还指定了build，在这种情况下，它将使用指定的build选项构建它，并使用image指定的名字和标记对其进行标记。

```bash
container_name
```

指定一个自定义容器名称，而不是生成的默认名称。

```yaml
container_name: my-web-container
```

由于Docker容器名称必须是唯一的，因此如果指定了自定义名称，则无法将服务扩展到多个容器。

```bash
volumes
```

卷挂载路径设置。可以设置宿主机路径 （HOST:CONTAINER） 或加上访问模式 （HOST:CONTAINER:ro）,挂载数据卷的默认权限是读写（rw），可以通过ro指定为只读。 
你可以在主机上挂载相对路径，该路径将相对于当前正在使用的Compose配置文件的目录进行扩展。 相对路径应始终以 . 或者 .. 开始。

- #### **volumes:**

```bash
  # 只需指定一个路径，让引擎创建一个卷
  - /var/lib/mysql

  # 指定绝对路径映射
  - /opt/data:/var/lib/mysql

  # 相对于当前compose文件的相对路径
  - ./cache:/tmp/cache

  # 用户家目录相对路径
  - ~/configs:/etc/configs/:ro

  # 命名卷
  - datavolume:/var/lib/mysql
```

但是，如果要跨多个服务并重用挂载卷，请在顶级volumes关键字中命名挂在卷，但是并不强制，如下的示例亦有重用挂载卷的功能，但是不提倡。

```yaml
version: "3"

services:
  web1:
    build: ./web/
    volumes:
    - ../code:/opt/web/code
  web2:
     build: ./web/
     volumes:
     - ../code:/opt/web/code
```

** 注意：通过顶级volumes定义一个挂载卷，并从每个服务的卷列表中引用它， 这会替换早期版本的Compose文件格式中volumes_from。

```yaml
version: "3"

services:
  db:
    image: db
    volumes:
      - data-volume:/var/lib/db
  backup:
    image: backup-service
    volumes:
      - data-volume:/var/lib/backup/data

volumes:
  data-volume:
command
```

覆盖容器启动后默认执行的命令。

```bash
command: bundle exec thin -p 3000
```

该命令也可以是一个类似于dockerfile的列表：

```dockerfile
command: ["bundle", "exec", "thin", "-p", "3000"]
```

- #### **links**

链接到另一个服务中的容器。 请指定服务名称和链接别名（SERVICE：ALIAS），或者仅指定服务名称。

```yaml
web:
  links:

   - db
   - db:database
   - re
```

在当的web服务的容器中可以通过链接的db服务的别名database访问db容器中的数据库应用，如果没有指定别名，则可直接使用服务名访问。

链接不需要启用服务进行通信 - 默认情况下，任何服务都可以以该服务的名称到达任何其他服务。 （实际是通过设置/etc/hosts的域名解析，从而实现容器间的通信。故可以像在应用中使用localhost一样使用服务的别名链接其他容器的服务，前提是多个服务容器在一个网络中可路由联通）

links也可以起到和depends_on相似的功能，即定义服务之间的依赖关系，从而确定服务启动的顺序。

- #### **external_links**

链接到docker-compose.yml 外部的容器，甚至并非 Compose 管理的容器。参数格式跟 links 类似。

```yaml
external_links:

 - redis_1
 - project_db_1:mysql
 - project_db_1:postgresql
   expose
   暴露端口，但不映射到宿主机，只被连接的服务访问。 
   仅可以指定内部端口为参数

expose:

 - "3000"
 - "8000"
   ports
   暴露端口信息。 
   常用的简单格式：使用宿主：容器 （HOST:CONTAINER）格式或者仅仅指定容器的端口（宿主将会随机选择端口）都可以。
```

** 注意：当使用 HOST:CONTAINER 格式来映射端口时，如果你使用的容器端口小于 60 你可能会得到错误得结果，因为 YAML 将会解析 xx:yy 这种数字格式为 60 进制。所以建议采用字符串格式。

简单的短格式：

```yaml
ports:

 - "3000"
 - "3000-3005"
 - "8000:8000"
 - "9090-9091:8080-8081"
 - "49100:22"
 - "127.0.0.1:8001:8001"
 - "127.0.0.1:5000-5010:5000-5010"
 - "6060:6060/udp"
```

ports的长格式的语法允许配置不能用短格式表示的附加字段。 
长格式：

```yaml
ports:

  - target: 80
    published: 8080
    protocol: tcp
    mode: host
    target：容器内的端口 
    published：物理主机的端口 
    protocol：端口协议（tcp或udp） 
    mode：host 和ingress 两总模式，host用于在每个节点上发布主机端口，ingress 用于被负载平衡的swarm模式端口
```

- #### **restart**

no是默认的重启策略，在任何情况下都不会重启容器。 指定为always时，容器总是重新启动。 如果退出代码指示出现故障错误，则on-failure将重新启动容器。

```yaml
restart: "no"
restart: always
restart: on-failure
restart: unless-stopped
environment
```

添加环境变量。 你可以使用数组或字典两种形式。 任何布尔值; true，false，yes，no需要用引号括起来，以确保它们不被YML解析器转换为True或False。 
只给定名称的变量会自动获取它在 Compose 主机上的值，可以用来防止泄露不必要的数据。

```yaml
environment:
  RACK_ENV: development
  SHOW: 'true'
  SESSION_SECRET:

environment:

  - RACK_ENV=development
  - SHOW=true
  - SESSION_SECRET
    ** 注意：如果你的服务指定了build选项，那么在构建过程中通过environment定义的环境变量将不会起作用。 将使用build的args子选项来定义构建时的环境变量。
```

- #### **pid**

将PID模式设置为主机PID模式。 这就打开了容器与主机操作系统之间的共享PID地址空间。 使用此标志启动的容器将能够访问和操作裸机的命名空间中的其他容器，反之亦然。即打开该选项的容器可以相互通过进程 ID 来访问和操作。

```bash
pid: "host"
```

- #### **dns**

配置 DNS 服务器。可以是一个值，也可以是一个列表。

```yaml
dns: 8.8.8.8
dns:
  - 8.8.8.8
  - 9.9.9.9
```

**实战(docker_start.sh)：**

```bash
#!/bin/bash
xhost +

#!/bin/bash
if [[ -n $(docker ps | grep lidarCalib) ]];then
        echo "container lidarCalib runing"
    docker exec -it lidarCalib bash
else
    if [[ -z $(docker images | grep harbor.qomolo.com/ros2/foxy/foxy-igv_cuda_11.0) ]];then

        echo "pulling docker image"
        docker pull harbor.qomolo.com/ros2/foxy/foxy-igv_cuda_11.0
    fi

    while [[ -z $(docker ps | grep lidarCalib) ]]
    do
        echo "no container lidarCalib, creating"

        echo "current direction: $(pwd)"

        echo "please make sure lidar_calib_pkgs is in current direction"

        docker run -it --rm \
        -d \
        --gpus all \
        --privileged=true \
        --network=host \
        --name lidarCalib \
        -e DISPLAY=unix$DISPLAY \
        -e QT_GRAPHICSSYSTEM=native \
        -e GDK_SCALE \           #visualization
        -e GDK_DPI_SCALE \      #
        -e ROS_DOMAIN_ID=132 \
        -e USER=$USER \
        -v /dev:/dev \
        -v /etc/localtime:/etc/localtime \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -v $(pwd):/lidar_calib_pkgs \
        -w /lidar_calib_pkgs \
        harbor.qomolo.com/ros2/foxy/foxy-igv_cuda_11.0 /bin/bash
    done

    echo "Successful created container lidarCalib, enjoy it!"

fi
```

## Docker 自定义网络

```bash
#命令
westwell@westwell:~$ docker network --help

Usage:  docker network COMMAND

Manage networks

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks

Run 'docker network COMMAND --help' for more information on a command.

docker network connect
将容器连接到网络

docker network create
创建一个网络

docker network disconnect
断开容器的网络

docker network inspect
显示一个或多个网络的详细信息

docker network ls
列出网络

docker network prune
删除所有未使用的网络

docker network rm
删除一个或多个网络

```

ex:

**查看当前所有网络**

```bash
$ docker network ls 
```

**将正在运行的容器连接到网络**

```shell
$ docker network connect multi-host-network my_container1
Shell
```

**启动时将容器连接到网络** 

还可以使用`docker run --network=<network-name>`选项启动容器并立即将其连接到网络。

```shell
$ docker run -itd --network=multi-host-network busybox-container
Shell
```

**指定容器的IP地址**

可以指定要分配给容器网络接口的IP地址。

```shell
$ docker network connect --ip 10.10.36.122 multi-host-network container2
Shell
```

**使用legacy —link选项**

可以使用`--link`选项将另一个容器与首选别名相链接

```shell
$ docker network connect --link container1:c1 multi-host-network container2
Shell
```

**为容器创建一个网络别名**

`--alias`选项可用于通过连接到的网络中的另一个名称来解析容器。

```shell
$ docker network connect --alias db --alias mysql multi-host-network container2
Shell
```

**停止，暂停或重新启动容器的网络影响**

可以暂停，重新启动并停止连接到网络的容器。容器在运行时连接到其配置的网络。

```shell
$ docker network create --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 multi-host-network
$ docker network connect --ip 172.20.128.2 multi-host-network container2
```

**创建一个自己网络，并指定网络**

```bash
$ docker network create -d bridge --gateway 10.159.0.1 --subnet 10.159.0.0/16 mynetwork
# 创建一个network，name=mynetwork， 
```

## Docker 多阶段构建

所谓的多阶段构建就是与17.05版本之前的Docker，只允许Dockerfile中出现一个`FROM`指令，之后新加多阶段构建的问题

>
>
>什么是多阶段构建？作用是什么？



多阶段构建通过在Dockerfile中使用多个 FROM指令实现。每一条 FROM 指令都是一个构建阶段，多个 FROM指令就是多阶段构建。多阶段构建的意义在于：在构建的过程中，可以选择性的将前面阶段中必要的文件复制到后面的阶段中，并抛弃不需要的文件。这样，最后的镜像中只保留需要的文件。


多阶段构建------所谓多阶段构建，实际上是允许一个Dockerfile 中出现多个 `FROM` 指令，     --即可以多重导入基本镜像，但只会生成最后一个FROM

Docker的镜像是一个**压缩文件**，其中包含了你**需要的程序和一个文件系统**。其实这样说是不严谨的，Docker镜像并非只是一个文件，而是由一堆**文件组成，最主要的文件是 层**

文件层是一种共享机制可以节约大量的磁盘空间和传输带宽   ，多个镜像层共享基础层的一种方式，采用了**AUFS**的一种文件联合挂载机制

AUFS曾是Docker默认的首选存储驱动。它非常稳定、有很多真实场景的部署、很强的社区支持。它有以下主要优点：
**具有构建安全、构建速度快、镜像文件体积小**等优点。　　

​        **极短的容器启动时间。**
　　**有效的存储利用率。**
　　**有效的内存利用率。**
　　**虽然如此，但由于它没有包含在Linux内核主线中，所有很多Linux发行版并不支持AUFS。**

CoW（Copy-on-Write）技术来实现**镜像共享和最小化磁盘空间的**使用

AUFS存储驱动也带来了一些容器写性能上的隐患。这是因为，容器第一次对任何文件的修改，都需要先定位到文件的所在的镜像层次，并拷贝到容器最顶层的读写层。尤其当这些文件存在于很底层，或者文件本身非常大时，性能问题尤其严重

多个 `FROM` 指令并不是为了生成多根的层关系，最后生成的镜像，仍以最后一条 `FROM` 为准，之前的 `FROM` 会被抛弃

- #### 意义

每一条 `FROM` 指令都是一个构建阶段，多条 `FROM` 就是多阶段构建，虽然最后生成的镜像只能是最后一个阶段的结果，但是，能够将前置阶段中的文件拷贝到后边的阶段中，这就是多阶段构建的最大意义。

- #### 使用场景    （最常用的）

将编译环境和运行环境分离



可以使用FROM image     AS   别名

注意`AS`指令。 这表明这不是`Dockerfile`的最后阶段

可以使用：

COPY `--from` 不但可以从前置阶段中拷贝，还可以直接从一个已经存在的镜像中拷贝

也可以使用--from:0 使用多阶段构建方法调用前放的image或者已经存在的镜像的一些可执行文件


###########################################123
