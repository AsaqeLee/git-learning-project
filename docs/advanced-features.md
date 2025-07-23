# Git高级功能

## 1. Git Stash - 暂存工作

### 基本用法
```bash
git stash                          # 暂存当前工作
git stash save "描述信息"           # 带描述的暂存
git stash list                     # 查看stash列表
git stash pop                      # 恢复最新的stash并删除
git stash apply                    # 恢复最新的stash但不删除
git stash drop stash@{0}           # 删除指定的stash
git stash clear                    # 清空所有stash
```

### 高级用法
```bash
git stash push -m "消息" file.txt  # 只暂存特定文件
git stash show stash@{0}           # 查看stash的内容
git stash branch new-branch        # 从stash创建新分支
```

## 2. Git Tag - 标签管理

### 轻量标签
```bash
git tag v1.0                       # 创建轻量标签
git tag                            # 列出所有标签
git tag -l "v1.*"                  # 列出匹配的标签
```

### 附注标签
```bash
git tag -a v1.0 -m "版本1.0"       # 创建附注标签
git tag -a v1.1 commit-hash        # 为特定提交创建标签
git show v1.0                      # 查看标签信息
```

### 标签操作
```bash
git push origin v1.0               # 推送单个标签
git push origin --tags             # 推送所有标签
git tag -d v1.0                    # 删除本地标签
git push origin --delete v1.0      # 删除远程标签
```

## 3. Git Rebase - 变基操作

### 基本概念
Rebase可以将一系列提交"重新播放"到另一个基础提交上，创建更线性的历史。

### 基本用法
```bash
git rebase master                  # 将当前分支变基到master
git rebase --continue              # 解决冲突后继续rebase
git rebase --abort                 # 取消rebase操作
git rebase --skip                  # 跳过当前提交
```

### 交互式rebase
```bash
git rebase -i HEAD~3               # 交互式rebase最近3个提交
git rebase -i commit-hash          # 从指定提交开始交互式rebase
```

交互式rebase选项：
- `pick`: 使用提交
- `reword`: 使用提交但修改提交消息
- `edit`: 使用提交但停下来修改
- `squash`: 将提交合并到前一个提交
- `fixup`: 类似squash但丢弃提交消息
- `drop`: 删除提交

## 4. Git Cherry-pick - 挑选提交

### 基本用法
```bash
git cherry-pick commit-hash        # 挑选单个提交
git cherry-pick commit1 commit2    # 挑选多个提交
git cherry-pick start..end         # 挑选提交范围
```

### 高级选项
```bash
git cherry-pick -n commit-hash     # 挑选但不自动提交
git cherry-pick -x commit-hash     # 在提交消息中记录原始提交
git cherry-pick --continue         # 解决冲突后继续
git cherry-pick --abort            # 取消cherry-pick
```

## 5. Git Reset - 重置操作

### 三种模式
```bash
git reset --soft HEAD~1            # 软重置：只移动HEAD
git reset --mixed HEAD~1           # 混合重置：移动HEAD并重置暂存区（默认）
git reset --hard HEAD~1            # 硬重置：重置所有内容（危险！）
```

### 重置到特定提交
```bash
git reset --hard commit-hash       # 重置到指定提交
git reset --soft commit-hash       # 软重置到指定提交
```

## 6. Git Revert - 撤销提交

### 基本用法
```bash
git revert commit-hash             # 撤销指定提交
git revert HEAD                    # 撤销最新提交
git revert HEAD~2..HEAD            # 撤销提交范围
```

### 高级选项
```bash
git revert -n commit-hash          # 撤销但不自动提交
git revert --continue              # 解决冲突后继续
git revert --abort                 # 取消revert操作
```

## 7. Git Bisect - 二分查找

用于快速定位引入bug的提交：

```bash
git bisect start                   # 开始二分查找
git bisect bad                     # 标记当前提交为坏的
git bisect good commit-hash        # 标记某个提交为好的
git bisect good                    # 标记当前提交为好的
git bisect reset                   # 结束二分查找
```

## 8. Git Reflog - 引用日志

查看HEAD的移动历史：

```bash
git reflog                         # 查看引用日志
git reflog show branch-name        # 查看特定分支的引用日志
git reset --hard HEAD@{2}          # 恢复到引用日志中的某个状态
```

## 9. 最佳实践

### 何时使用rebase
- 在推送到共享分支之前整理提交历史
- 保持线性的项目历史
- 合并功能分支到主分支时

### 何时避免rebase
- 已经推送到共享仓库的提交
- 多人协作的分支
- 不确定操作结果时

### 安全建议
- 在重要操作前创建备份分支
- 使用`git reflog`恢复意外丢失的提交
- 理解每个命令的作用再执行

---

**记住**: 这些高级功能很强大，但也需要谨慎使用！
