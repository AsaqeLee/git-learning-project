# 团队协作工作流演示

## 场景：多人协作开发一个Web应用

### 团队成员
- **Alice**: 前端开发工程师
- **Bob**: 后端开发工程师  
- **Charlie**: 全栈开发工程师
- **Diana**: 项目经理/代码审查员

### 项目结构
```
web-app/
├── frontend/          # 前端代码 (Alice负责)
├── backend/           # 后端代码 (Bob负责)
├── docs/              # 文档 (Charlie负责)
├── tests/             # 测试 (所有人)
└── README.md
```

## 工作流演示

### 第1天：项目初始化 (Diana)

```bash
# Diana创建项目仓库
git init web-app
cd web-app

# 创建初始结构
mkdir frontend backend docs tests
echo "# Web App Project" > README.md

# 初始提交
git add .
git commit -m "feat: 初始化项目结构"

# 创建develop分支
git checkout -b develop
git push -u origin develop

# 设置主分支保护
# (在GitHub/GitLab上配置分支保护规则)
```

### 第2天：并行功能开发

#### Alice开发用户登录功能
```bash
# Alice从develop创建功能分支
git checkout develop
git pull origin develop
git checkout -b feature/user-login

# 开发登录页面
echo "// 用户登录组件" > frontend/LoginComponent.js
git add frontend/LoginComponent.js
git commit -m "feat(frontend): 添加用户登录组件

- 实现登录表单UI
- 添加表单验证
- 集成状态管理

Refs #101"

# 继续开发
echo "// 登录API调用" > frontend/LoginAPI.js
git add frontend/LoginAPI.js
git commit -m "feat(frontend): 实现登录API调用

- 添加HTTP客户端配置
- 实现登录请求处理
- 添加错误处理

Refs #101"

# 推送分支
git push -u origin feature/user-login
```

#### Bob开发用户认证API
```bash
# Bob从develop创建功能分支
git checkout develop
git pull origin develop
git checkout -b feature/auth-api

# 开发认证API
echo "// 用户认证路由" > backend/auth.js
git add backend/auth.js
git commit -m "feat(backend): 添加用户认证API

- 实现登录端点
- 添加JWT token生成
- 实现密码验证

Refs #102"

# 添加中间件
echo "// JWT验证中间件" > backend/middleware.js
git add backend/middleware.js
git commit -m "feat(backend): 添加JWT验证中间件

- 实现token验证
- 添加权限检查
- 处理token过期

Refs #102"

# 推送分支
git push -u origin feature/auth-api
```

#### Charlie编写API文档
```bash
# Charlie从develop创建文档分支
git checkout develop
git pull origin develop
git checkout -b docs/api-documentation

# 编写API文档
echo "# API Documentation" > docs/api.md
git add docs/api.md
git commit -m "docs: 添加API文档框架

- 创建API文档结构
- 添加认证相关文档
- 定义响应格式规范

Refs #103"

# 推送分支
git push -u origin docs/api-documentation
```

### 第3天：代码审查和合并

#### Bob的API完成，创建Pull Request
```bash
# Bob完成开发，准备PR
git checkout feature/auth-api
git rebase develop  # 确保基于最新的develop

# 推送更新
git push origin feature/auth-api

# 在GitHub/GitLab上创建Pull Request
# 标题: feat(backend): 实现用户认证API
# 描述: 
# ## 变更内容
# - 添加用户登录API端点
# - 实现JWT token生成和验证
# - 添加认证中间件
# 
# ## 测试
# - [x] 单元测试通过
# - [x] 集成测试通过
# - [x] 手动测试验证
# 
# ## 相关Issue
# Closes #102
```

#### Diana进行代码审查
```bash
# Diana检出PR分支进行审查
git fetch origin
git checkout feature/auth-api

# 查看变更
git diff develop...feature/auth-api

# 运行测试
npm test

# 审查意见：
# ✅ 代码质量良好
# ✅ 测试覆盖充分
# ⚠️  建议：添加API限流
# ✅ 文档完整
# 
# 总体评价：LGTM (Looks Good To Me)
```

#### 合并Bob的PR
```bash
# Diana合并PR (通过GitHub/GitLab界面)
# 或者命令行合并：

git checkout develop
git pull origin develop
git merge --no-ff feature/auth-api
git push origin develop

# 删除功能分支
git branch -d feature/auth-api
git push origin --delete feature/auth-api
```

### 第4天：处理合并冲突

#### Alice需要同步最新的develop
```bash
# Alice同步develop的更新
git checkout develop
git pull origin develop

# 将develop的更改合并到功能分支
git checkout feature/user-login
git rebase develop

# 如果有冲突，解决冲突
# 编辑冲突文件...
git add .
git rebase --continue

# 推送更新
git push --force-with-lease origin feature/user-login
```

#### Alice创建Pull Request
```bash
# Alice的PR描述：
# ## 变更内容
# - 实现用户登录前端组件
# - 集成后端认证API
# - 添加登录状态管理
# 
# ## 截图
# [登录页面截图]
# 
# ## 测试清单
# - [x] 组件单元测试
# - [x] E2E测试
# - [x] 跨浏览器测试
# - [x] 响应式设计测试
# 
# ## 相关Issue
# Closes #101
# Depends on #102
```

### 第5天：发布准备

#### 创建Release分支
```bash
# Diana创建release分支
git checkout develop
git pull origin develop
git checkout -b release/v1.0.0

# 更新版本号
echo "v1.0.0" > VERSION
git add VERSION
git commit -m "chore: 更新版本号到v1.0.0"

# 最后的bug修复和文档更新
git add .
git commit -m "docs: 更新发布说明"

# 推送release分支
git push -u origin release/v1.0.0
```

#### 合并到main并打标签
```bash
# 合并到main
git checkout main
git pull origin main
git merge --no-ff release/v1.0.0
git tag -a v1.0.0 -m "Release version 1.0.0

Features:
- 用户认证系统
- 登录/注销功能
- JWT token管理

Bug Fixes:
- 修复登录表单验证
- 优化API响应时间

Breaking Changes:
- 无"

git push origin main
git push origin v1.0.0

# 合并回develop
git checkout develop
git merge --no-ff release/v1.0.0
git push origin develop

# 删除release分支
git branch -d release/v1.0.0
git push origin --delete release/v1.0.0
```

## 最佳实践总结

### 1. 分支管理
- 使用feature分支进行功能开发
- 定期同步develop分支
- 使用rebase保持线性历史
- 及时删除已合并的分支

### 2. 提交规范
- 使用Conventional Commits格式
- 每个提交只包含一个逻辑变更
- 编写清晰的提交消息
- 关联相关的Issue

### 3. 代码审查
- 所有代码必须经过审查
- 提供建设性的反馈
- 确保测试覆盖
- 检查文档更新

### 4. 冲突处理
- 频繁同步主分支
- 及时解决冲突
- 与团队成员沟通
- 使用合适的合并策略

### 5. 发布管理
- 使用语义化版本控制
- 创建release分支
- 编写详细的发布说明
- 保持main分支稳定

---

**记住**: 好的工作流需要团队所有成员的配合和坚持！
