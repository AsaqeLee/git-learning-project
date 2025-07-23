# Git实用技巧

## 1. 常用Git别名

设置一些有用的Git别名来提高效率：

```bash
# 基本别名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

# 高级别名
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'

# 日志别名
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.lol "log --graph --decorate --pretty=oneline --abbrev-commit"
git config --global alias.lola "log --graph --decorate --pretty=oneline --abbrev-commit --all"
```

## 2. 提交消息最佳实践

### 提交消息格式
```
<type>(<scope>): <subject>

<body>

<footer>
```

### 常用类型
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式化
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

### 示例
```
feat(auth): 添加用户登录功能

实现了基于JWT的用户认证系统：
- 用户名密码登录
- 记住登录状态
- 自动token刷新

Closes #123
```

## 3. 分支命名规范

### 功能分支
- `feature/user-authentication`
- `feature/payment-integration`
- `feat/add-search-function`

### 修复分支
- `fix/login-bug`
- `bugfix/memory-leak`
- `hotfix/critical-security-issue`

### 其他分支
- `docs/update-readme`
- `refactor/database-layer`
- `test/add-unit-tests`

## 4. 实用命令技巧

### 查看文件历史
```bash
git log --follow <file>        # 跟踪文件重命名
git log -p <file>              # 显示文件的详细变更
git blame <file>               # 查看每行的最后修改者
```

### 搜索功能
```bash
git grep "search-term"         # 在工作区搜索
git log --grep="message"       # 在提交消息中搜索
git log -S "code"              # 搜索代码变更
```

### 撤销操作
```bash
git checkout -- <file>        # 撤销工作区修改
git reset HEAD <file>          # 撤销暂存区修改
git reset --soft HEAD~1        # 撤销最后一次提交，保留修改
git reset --hard HEAD~1        # 完全撤销最后一次提交
```

## 5. .gitignore 最佳实践

### 常见忽略模式
```gitignore
# 操作系统文件
.DS_Store
Thumbs.db

# 编辑器文件
.vscode/
.idea/
*.swp

# 依赖目录
node_modules/
vendor/

# 构建输出
dist/
build/
*.exe

# 日志文件
*.log

# 环境配置
.env
.env.local
```

## 6. 团队协作技巧

### 代码审查清单
- [ ] 代码符合项目规范
- [ ] 没有明显的bug
- [ ] 测试覆盖充分
- [ ] 提交消息清晰
- [ ] 没有敏感信息

### 冲突解决策略
1. 理解冲突的原因
2. 与相关开发者沟通
3. 仔细审查冲突内容
4. 测试解决后的代码
5. 提交清晰的解决说明

## 7. 性能优化

### 大仓库优化
```bash
git config core.preloadindex true
git config core.fscache true
git config gc.auto 256
```

### 清理仓库
```bash
git gc --prune=now --aggressive    # 垃圾回收
git remote prune origin            # 清理远程分支引用
```

---

**记住**: Git是一个强大的工具，掌握这些技巧将大大提高你的开发效率！
