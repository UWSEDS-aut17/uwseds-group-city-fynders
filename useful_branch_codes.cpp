//
//  main.cpp
//  Week2
//
//  Created by Emilydelluque on 10/8/17.
//  Copyright © 2017 Emilydelluque. All rights reserved.
//

git config --global user.name "Emily Wendan Yan"
git config --global user.email "emwyan@uw.edu"
git config --global color.ui auto
git config --list

/*
credential.helper=osxkeychain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
user.name=Emily Wendan Yan
user.email=emwyan@uw.edu
color.ui=auto
core.editor=nano -w
*/

git init
ls -la // show hiden file

git status
/*
On branch master
Initial commit
*/

//Staging area: before going to the repository so you can combine several files into a single commit

git add filename
git commit filena

git commit -a -m 'added new benchmarks'

git log

/*
 commit 7738e6911b95a2e16483b06a6eb2a4027cf62c58
 Author: Emily Wendan Yan <emwyan@uw.edu>
 Date:   Sun Oct 8 16:06:08 2017 -0700
 
 csv used for week1 assignment included in repository
 
 commit 770e40f11c60b29212fee0d2dea29406108483b6
 Author: Emily Wendan Yan <emwyan@uw.edu>
 Date:   Sun Oct 8 16:03:26 2017 -0700
 
 ipynb file committed Wendan_Yan.ipynb for week1 assignment
 */



// 添加一个新的远程仓库连接到一个url
git remote add pb1 https://github.com/UWSEDS-aut17/hw1-EmilyYanW

//获得远程repos, basing your work on an upstream branch that already exists at the remote, you may need to run "git fetch" to retrieve it.
git fetch pb1

//当下本地分支连接到远程repos,Branch master set up to track remote branch master from pb1.
git branch -u pb1/master

git branch -vv
// check tracking information
// 根据提示适度地git pull 或者 git pushq
// 合并当下branch和远程pb1/master
git merge pb1/master --allow-unrelated-histories

/* Your branch is ahead of 'pb1/master' by 2 commits.
 (use "git push" to publish your local commits)
 */

git diff //比较
git diff HEAD~1 setup.sh
git diff 69e4d0bb6f

git checkout HEAD setup.sh
//后面可以commit

/*
 Username for 'https://github.com': EmilyYanW
 Password for 'https://EmilyYanW@github.com':
 */


git clone https://github.com/schacon/ticgit
//假设你的网络里有一个在 git.ourcompany.com 的 Git 服务器。
//如果你从这里克隆，Git 的 clone 命令会为你自动将其命名为 origin，拉取它的所有数据，创建一个指向它的 master 分支的指针，
//并且在本地将其命名为 origin/master。
//Git 也会给你一个与 origin 的 master 分支在指向同一个地方的本地 master 分支，这样你就有工作的基础。

git merge origin/master --allow-unrelated-histories

git rm <file name>
git commit -m "delete file ..."
git push

source setup.sh //把文件当中的url下载下来
//并且是untracked file
// ignore anything that is a csv
nano .gitignore
*.csv

/// 分支简介 ////
// 创建分支
git branch testing
// 分支切换
git checkout testing
//使 HEAD 指向testing分支，并且将工作目录恢复成 master 分支所指向的快照内容
$ git checkout -b iss53
// 两条语句合并：Switched to a new branch "iss53"

//使用 git log 命令查看分叉历史。输出你的提交历史、各个分支的指向以及项目的分支分叉情况。
git log --oneline --decorate --graph --all

git checkout master
git merge hotfix
/*
 Updating f42c576..3a0874c
 Fast-forward
 index.html | 2 ++
 1 file changed, 2 insertions(+)
*/

//快进（fast-forward）"这个词。
//由于当前 master 分支所指向的提交是你当前提交（有关 hotfix 的提交）的直接上游

git branch -d hotfix
//Deleted branch hotfix (3a0874c).
// 删除branch

git merge iss53
/*
 Auto-merging index.html
 CONFLICT (content): Merge conflict in index.html
 Automatic merge failed; fix conflicts and then commit the result.
*/

git status
/*
 On branch master
 You have unmerged paths.
 (fix conflicts and run "git commit")
 
 Unmerged paths:
 (use "git add <file>..." to mark resolution)
 
 both modified:      index.html
 
 no changes added to commit (use "git add" and/or "git commit -a")
*/

git nano index.html

/*
 <<<<<<< HEAD:index.html
 <div id="footer">contact : email.support@github.com</div>
 =======
 <div id="footer">
 please contact us at support@github.com
 </div>
 >>>>>>> iss53:index.html
*/

//改成：
/*
 <<<<<<< HEAD:index.html
 <div id="footer">contact : email.support@github.com</div>
 */

/*
 [master 3d592a3] conflict resolved
 */

git branch -v
// 查看每一个分支的最后一次提交
 git branch --merged
//哪些分支已经合并到当前分支
git branch --no-merged
//查看所有包含未合并工作的分支

 git ls-remote
// 显式地获得远程引用的完整列表
git remote show

git push origin serverfix
git push origin serverfix:awesomebranch
//推送本地的 serverfix 分支来更新远程仓库上的 serverfix/awesome branch 分支
//下一次其他协作者从服务器上抓取数据时，他们会在本地生成一个远程分支 origin/serverfix，指向服务器的 serverfix 分支的引用

git fetch origin
git merge origin/serverfix
//抓取到新的远程跟踪分支时，本地不会自动生成一份可编辑的副本（拷贝）。
//换一句话说，这种情况下，不会有一个新的 serverfix 分支
//- 只有一个不可以修改的 origin/serverfix 指针。

git checkout -b serverfix origin/serverfix
//或者
git checkout --track origin/serverfix
//Branch serverfix set up to track remote branch serverfix from origin.
//Switched to a new branch 'serverfix'
//从一个远程跟踪分支检出一个本地分支会自动创建一个叫做 “跟踪分支”, serverfix 就是 origin/serverfix的跟踪分支

git branch -u origin/iss53
//current branch is set up to track remote branch iss53 from origin.

git branch -vv
// check tracking information

/*
 
 * iss53  a5c966e [origin/iss53] finished the new footer [issue 53]
 master 5eaaf3b [origin/master] add .gitignore file

 */

git push origin --delete serverfix
//删除远程分支
//To https://github.com/schacon/simplegit
//- [deleted]         serverfix



