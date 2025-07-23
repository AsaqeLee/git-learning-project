# Git命令参考

## 基础命令

### 配置命令
```bash
# 设置用户名和邮箱
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 查看配置
git config --global --list
git config user.name
git config user.email
```

### 仓库初始化
```bash
# 初始化新仓库
git init

# 克隆远程仓库
git clone <url>
git clone <url> <directory-name>
```

### 基本操作

#### git status - 查看仓库状态
```bash
git status              # 查看详细状态
git status -s           # 查看简短状态
git status --porcelain  # 机器可读格式
```

#### git add - 添加文件到暂存区
```bash
git add <file>          # 添加单个文件
git add <dir>           # 添加目录
git add .               # 添加当前目录所有文件
git add -A              # 添加所有文件（包括删除的）
git add *.txt           # 添加所有txt文件
git add -p              # 交互式添加（部分添加）
```

#### git commit - 提交更改
```bash
git commit -m "message"     # 提交并添加消息
git commit -am "message"    # 添加并提交已跟踪文件
git commit --amend          # 修改最后一次提交
git commit --amend -m "new message"  # 修改最后一次提交消息
```

#### git log - 查看提交历史
```bash
git log                     # 查看详细日志
git log --oneline          # 一行显示一个提交
git log --graph            # 图形化显示分支
git log --stat             # 显示文件变更统计
git log -p                 # 显示每次提交的差异
git log -n 5               # 显示最近5次提交
git log --since="2 weeks ago"  # 显示2周内的提交
git log --author="name"    # 显示特定作者的提交
```

#### git diff - 查看差异
```bash
git diff                   # 工作区与暂存区的差异
git diff --staged          # 暂存区与版本库的差异
git diff HEAD              # 工作区与版本库的差异
git diff <commit1> <commit2>  # 两个提交之间的差异
git diff <file>            # 特定文件的差异
```

### 撤销操作

#### 撤销工作区的修改
```bash
git restore <file>         # 撤销工作区的修改（Git 2.23+）
git checkout -- <file>    # 撤销工作区的修改（旧版本）
```

#### 撤销暂存区的修改
```bash
git restore --staged <file>  # 从暂存区移除文件（Git 2.23+）
git reset HEAD <file>        # 从暂存区移除文件（旧版本）
```

#### 撤销提交
```bash
git reset --soft HEAD~1    # 撤销提交，保留暂存区和工作区
git reset --mixed HEAD~1   # 撤销提交和暂存，保留工作区（默认）
git reset --hard HEAD~1    # 撤销提交、暂存区和工作区（危险！）
```

## 文件状态说明

### 文件状态转换
```
未跟踪 (Untracked) --git add--> 已暂存 (Staged)
已跟踪 (Tracked):
  - 未修改 (Unmodified) --编辑--> 已修改 (Modified)
  - 已修改 (Modified) --git add--> 已暂存 (Staged)
  - 已暂存 (Staged) --git commit--> 未修改 (Unmodified)
```

### git status 输出解读
- `Untracked files`: 未跟踪的文件
- `Changes to be committed`: 暂存区中的文件（准备提交）
- `Changes not staged for commit`: 已修改但未暂存的文件

## 实用技巧

### 查看文件历史
```bash
git log --follow <file>    # 查看文件的完整历史
git blame <file>           # 查看文件每行的最后修改者
```

### 搜索
```bash
git grep "search-term"     # 在工作区搜索
git log --grep="message"   # 在提交消息中搜索
```

### 别名设置
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
```

---

**下一步**: 学习Git分支管理！
