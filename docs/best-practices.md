# Git最佳实践与团队协作

## 1. 团队协作规范

### 代码审查最佳实践

#### 审查清单
- [ ] 代码符合项目编码规范
- [ ] 功能实现正确且完整
- [ ] 没有明显的性能问题
- [ ] 测试覆盖充分
- [ ] 文档更新及时
- [ ] 没有安全漏洞
- [ ] 提交消息清晰明确
- [ ] 没有敏感信息泄露

#### 审查原则
1. **建设性反馈**: 提供具体的改进建议，而不是简单的批评
2. **及时响应**: 尽快完成代码审查，不要让PR积压
3. **学习态度**: 从他人代码中学习新的技巧和方法
4. **尊重他人**: 保持友善和专业的态度

#### 审查技巧
```bash
# 查看PR的变更
git fetch origin pull/123/head:pr-123
git checkout pr-123
git diff master...pr-123

# 本地测试PR
git checkout pr-123
npm install
npm test
npm run build
```

### 提交消息规范 (Conventional Commits)

#### 格式规范
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

#### 类型说明
- `feat`: 新功能 (feature)
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式化（不影响功能的变更）
- `refactor`: 重构代码（既不是新增功能，也不是修复bug）
- `test`: 添加或修改测试
- `chore`: 构建过程或辅助工具的变动
- `perf`: 性能优化
- `ci`: CI/CD相关变更
- `build`: 影响构建系统或外部依赖的变更

#### 实际示例
```
feat(auth): 添加OAuth2登录支持

实现了Google和GitHub的OAuth2登录：
- 添加OAuth2客户端配置
- 实现登录回调处理
- 添加用户信息同步
- 更新登录页面UI

Closes #123
Breaking Change: 移除了旧的登录API /api/v1/login
```

```
fix(payment): 修复支付金额计算错误

修复了在计算折扣时的浮点数精度问题：
- 使用decimal.js处理金额计算
- 添加单元测试覆盖边界情况
- 更新相关文档

Fixes #456
```

### 分支管理策略

#### 分支命名规范
```bash
# 功能分支
feature/user-authentication
feature/payment-integration
feat/add-search-function

# 修复分支
fix/login-bug
bugfix/memory-leak
hotfix/critical-security-issue

# 其他分支
docs/update-readme
refactor/database-layer
test/add-unit-tests
chore/update-dependencies
```

#### 分支生命周期管理
```bash
# 1. 创建功能分支
git checkout main
git pull origin main
git checkout -b feature/new-feature

# 2. 定期同步主分支
git checkout main
git pull origin main
git checkout feature/new-feature
git rebase main  # 或者 git merge main

# 3. 完成开发后
git push origin feature/new-feature
# 创建Pull Request

# 4. 合并后清理
git checkout main
git pull origin main
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

## 2. 冲突解决策略

### 预防冲突
1. **频繁同步**: 每天至少一次从主分支拉取更新
2. **小步提交**: 保持提交粒度适中，避免大量文件的一次性修改
3. **沟通协调**: 团队成员之间及时沟通正在修改的文件
4. **模块化开发**: 尽量在不同的文件或模块中工作

### 解决冲突的步骤
```bash
# 1. 拉取最新代码时出现冲突
git pull origin main
# Auto-merging file.txt
# CONFLICT (content): Merge conflict in file.txt

# 2. 查看冲突状态
git status

# 3. 编辑冲突文件，解决冲突标记
# <<<<<<< HEAD
# 你的更改
# =======
# 他人的更改
# >>>>>>> commit-hash

# 4. 标记冲突已解决
git add file.txt

# 5. 完成合并
git commit -m "解决合并冲突"
```

### 使用工具解决冲突
```bash
# 配置合并工具
git config --global merge.tool vimdiff
# 或者使用其他工具
git config --global merge.tool vscode

# 启动合并工具
git mergetool
```

## 3. 项目管理最佳实践

### .gitignore 管理

#### 分层管理
```bash
# 全局 .gitignore (用户级别)
git config --global core.excludesfile ~/.gitignore_global

# 项目 .gitignore (项目级别)
# 在项目根目录创建 .gitignore

# 本地 .git/info/exclude (本地级别)
# 不会被提交到仓库
```

#### 常用模板
```gitignore
# 操作系统
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# 编辑器和IDE
.vscode/
.idea/
*.swp
*.swo
*~
.sublime-project
.sublime-workspace

# 语言特定
## Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnp/
.pnp.js

## Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

## Java
*.class
*.jar
*.war
*.ear
target/

# 构建输出
dist/
build/
out/
.next/
.nuxt/

# 日志文件
*.log
logs/

# 环境配置
.env
.env.local
.env.*.local
config/local.json

# 数据库
*.db
*.sqlite
*.sqlite3

# 缓存
.cache/
.tmp/
.temp/

# 备份文件
*.bak
*.backup
*~
```

### 版本标签管理

#### 语义化版本控制 (SemVer)
```
MAJOR.MINOR.PATCH

例如: 2.1.3
- MAJOR: 不兼容的API变更 (2.0.0)
- MINOR: 向后兼容的功能新增 (2.1.0)
- PATCH: 向后兼容的bug修复 (2.1.1)
```

#### 预发布版本
```bash
# Alpha版本 (内部测试)
git tag -a v1.1.0-alpha.1 -m "1.1.0第一个alpha版本"

# Beta版本 (公开测试)
git tag -a v1.1.0-beta.1 -m "1.1.0第一个beta版本"

# Release Candidate (发布候选)
git tag -a v1.1.0-rc.1 -m "1.1.0第一个候选版本"

# 正式版本
git tag -a v1.1.0 -m "正式版本1.1.0"
```

#### 标签管理
```bash
# 查看所有标签
git tag

# 查看特定模式的标签
git tag -l "v1.*"

# 查看标签详细信息
git show v1.0.0

# 推送标签到远程
git push origin v1.0.0
git push origin --tags

# 删除标签
git tag -d v1.0.0
git push origin --delete v1.0.0
```

## 4. 安全最佳实践

### 敏感信息管理
1. **永远不要提交密码、API密钥等敏感信息**
2. **使用环境变量存储配置**
3. **定期轮换密钥和令牌**
4. **使用.gitignore忽略配置文件**
5. **使用git-secrets等工具扫描敏感信息**

### 访问控制
```bash
# 使用SSH密钥
ssh-keygen -t ed25519 -C "your_email@example.com"

# 配置SSH
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

# 启用签名提交
git config --global user.signingkey YOUR_GPG_KEY_ID
git config --global commit.gpgsign true
```

### 审计和监控
```bash
# 查看提交历史
git log --oneline --graph --all

# 查看文件变更历史
git log --follow -- filename

# 查看特定作者的提交
git log --author="Author Name"

# 查看特定时间范围的提交
git log --since="2023-01-01" --until="2023-12-31"
```

---

**记住**: 好的实践需要团队共同遵守和维护！
