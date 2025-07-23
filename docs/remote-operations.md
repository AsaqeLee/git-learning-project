# Git远程仓库操作

## 1. 远程仓库基础概念

### 什么是远程仓库？
远程仓库是托管在网络上的Git仓库，用于：
- 代码备份和存储
- 团队协作和代码共享
- 版本发布和部署
- 代码审查和质量控制

### 常见的远程仓库托管服务
- **GitHub**: 最流行的Git托管平台
- **GitLab**: 开源的Git托管解决方案
- **Bitbucket**: Atlassian的Git托管服务
- **Gitee**: 国内的Git托管平台

## 2. 远程仓库配置

### 查看远程仓库
```bash
git remote                  # 查看远程仓库名称
git remote -v              # 查看远程仓库详细信息
git remote show <remote>   # 查看特定远程仓库信息
```

### 添加远程仓库
```bash
git remote add <name> <url>
git remote add origin https://github.com/user/repo.git
git remote add upstream https://github.com/original/repo.git
```

### 修改远程仓库
```bash
git remote set-url <name> <new-url>
git remote rename <old-name> <new-name>
git remote remove <name>
```

## 3. 推送操作 (Push)

### 基本推送
```bash
git push <remote> <branch>          # 推送指定分支
git push origin master              # 推送master分支到origin
git push -u origin master           # 推送并设置上游分支
git push                            # 推送当前分支（需要设置上游）
```

### 推送所有分支和标签
```bash
git push --all origin               # 推送所有分支
git push --tags origin              # 推送所有标签
git push origin --all --tags        # 推送所有分支和标签
```

### 强制推送（危险操作）
```bash
git push --force origin master      # 强制推送（覆盖远程历史）
git push --force-with-lease origin master  # 更安全的强制推送
```

## 4. 拉取操作 (Pull & Fetch)

### git fetch - 获取远程更新
```bash
git fetch                           # 获取默认远程仓库的更新
git fetch origin                    # 获取origin的更新
git fetch origin master             # 获取origin的master分支更新
git fetch --all                     # 获取所有远程仓库的更新
```

### git pull - 获取并合并
```bash
git pull                            # 等于 git fetch + git merge
git pull origin master              # 拉取并合并origin/master
git pull --rebase                   # 使用rebase而不是merge
git pull --no-commit                # 拉取但不自动提交合并
```

### fetch vs pull 的区别
- **git fetch**: 只下载远程更新，不自动合并
- **git pull**: 下载远程更新并自动合并到当前分支

## 5. 分支操作

### 推送新分支
```bash
git checkout -b feature/new-feature
git push -u origin feature/new-feature
```

### 跟踪远程分支
```bash
git checkout -b local-branch origin/remote-branch
git checkout --track origin/remote-branch
git branch -u origin/remote-branch local-branch
```

### 删除远程分支
```bash
git push origin --delete branch-name
git push origin :branch-name         # 旧语法
```

## 6. 协作工作流

### Fork工作流
1. Fork原仓库到自己的账户
2. Clone自己的Fork
3. 添加原仓库为upstream
4. 创建功能分支开发
5. 推送到自己的Fork
6. 创建Pull Request

### 共享仓库工作流
1. Clone共享仓库
2. 创建功能分支
3. 推送功能分支
4. 创建Pull Request
5. 代码审查和合并

## 7. 常见问题和解决方案

### 推送被拒绝
```bash
# 原因：远程有新的提交
# 解决：先拉取再推送
git pull origin master
git push origin master
```

### 合并冲突
```bash
# 拉取时出现冲突
git pull origin master
# 解决冲突后
git add .
git commit -m "解决合并冲突"
git push origin master
```

### 撤销推送
```bash
# 如果还没有人拉取
git reset --hard HEAD~1
git push --force origin master

# 如果已经有人拉取，使用revert
git revert <commit-hash>
git push origin master
```

## 8. 最佳实践

### 推送前的检查
1. 确保代码能够编译和运行
2. 运行测试确保没有破坏现有功能
3. 检查提交消息是否清晰
4. 确保没有敏感信息（密码、密钥等）

### 分支管理
1. 使用描述性的分支名称
2. 及时删除已合并的分支
3. 定期同步主分支的更新
4. 保持功能分支的简洁

### 团队协作
1. 制定清晰的分支策略
2. 使用Pull Request进行代码审查
3. 编写清晰的提交消息
4. 及时沟通和解决冲突

---

**下一步**: 学习Git的高级功能，如rebase、stash、tag等！
