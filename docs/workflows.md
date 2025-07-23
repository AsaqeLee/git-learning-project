# Git工作流程

## 1. 基本工作流程

### 日常开发流程
```
1. 检查当前状态: git status
2. 拉取最新代码: git pull
3. 创建功能分支: git checkout -b feature/new-feature
4. 开发功能...
5. 添加文件: git add .
6. 提交更改: git commit -m "描述性消息"
7. 推送分支: git push origin feature/new-feature
8. 创建Pull Request/Merge Request
9. 代码审查和合并
10. 删除功能分支: git branch -d feature/new-feature
```

## 2. 分支策略

### Git Flow
经典的Git工作流程，适合有明确发布周期的项目：

```
master/main     ←── 生产环境代码
    ↑
develop         ←── 开发环境代码
    ↑
feature/*       ←── 功能开发分支
release/*       ←── 发布准备分支
hotfix/*        ←── 紧急修复分支
```

**分支说明：**
- `master/main`: 稳定的生产代码
- `develop`: 开发分支，集成所有功能
- `feature/*`: 功能分支，从develop分出，完成后合并回develop
- `release/*`: 发布分支，从develop分出，用于发布准备
- `hotfix/*`: 热修复分支，从master分出，修复紧急问题

### GitHub Flow
简化的工作流程，适合持续部署：

```
main            ←── 主分支（随时可部署）
    ↑
feature/*       ←── 功能分支
```

**流程：**
1. 从main创建功能分支
2. 在功能分支上开发
3. 创建Pull Request
4. 代码审查
5. 合并到main
6. 部署

### GitLab Flow
结合了Git Flow和GitHub Flow的优点：

```
master          ←── 主开发分支
    ↓
pre-production  ←── 预生产环境
    ↓
production      ←── 生产环境
```

## 3. 提交消息规范

### 常用格式
```
<type>(<scope>): <subject>

<body>

<footer>
```

### 类型说明
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式化
- `refactor`: 重构代码
- `test`: 添加测试
- `chore`: 构建过程或辅助工具的变动

### 示例
```
feat(auth): 添加用户登录功能

- 实现用户名密码登录
- 添加记住登录状态功能
- 集成第三方OAuth登录

Closes #123
```

## 4. 分支命名规范

### 功能分支
- `feature/user-authentication`
- `feature/payment-integration`
- `feat/add-search-function`

### 修复分支
- `fix/login-bug`
- `bugfix/memory-leak`
- `hotfix/critical-security-issue`

### 发布分支
- `release/v1.2.0`
- `release/2023-12-01`

### 其他分支
- `docs/update-readme`
- `refactor/database-layer`
- `test/add-unit-tests`

## 5. 最佳实践

### 提交频率
- 经常提交，保持提交粒度适中
- 每个提交应该是一个逻辑单元
- 避免混合不相关的更改

### 分支管理
- 保持分支简洁，及时删除已合并的分支
- 定期同步主分支的更新
- 避免长期存在的功能分支

### 代码审查
- 所有代码都应该经过审查
- 使用Pull Request/Merge Request
- 自动化测试和检查

### 冲突解决
- 及时解决合并冲突
- 理解冲突的原因
- 与相关开发者沟通

---

**下一步**: 学习远程仓库操作和团队协作！
