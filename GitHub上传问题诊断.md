# GitHub上传问题诊断指南

## 🔍 常见问题及解决方案

### 问题1: "Repository not found"

**可能原因：**
1. 仓库名称拼写错误
2. 用户名错误
3. 仓库是私有的但没有权限
4. 仓库还未创建成功

**解决方案：**
```bash
# 1. 检查仓库URL是否正确
# 正确格式: https://github.com/用户名/仓库名.git

# 2. 确认仓库确实存在
# 在浏览器中访问: https://github.com/XuHuicong/Gobang-Game

# 3. 重新添加远程仓库
git remote add origin https://github.com/XuHuicong/Gobang-Game.git
```

### 问题2: 认证失败

**可能原因：**
1. 没有配置Git凭据
2. GitHub Token已过期
3. 用户名密码错误

**解决方案：**
```bash
# 配置全局用户信息
git config --global user.name "Xu Huicong"
git config --global user.email "你的邮箱@example.com"

# 清除缓存的凭据（Windows）
git config --global --unset credential.helper
```

### 问题3: 权限被拒绝

**解决方案：**
1. 确保你是仓库的所有者
2. 检查仓库是否为Private，如果是需要相应权限
3. 考虑使用SSH密钥认证

### 🛠️ 手动上传步骤

如果自动脚本有问题，可以手动执行：

```bash
# 1. 检查当前状态
git status

# 2. 添加远程仓库（替换为你的实际信息）
git remote add origin https://github.com/你的用户名/Gobang-Game.git

# 3. 验证远程仓库
git remote -v

# 4. 推送到GitHub
git push -u origin main
```

### 📝 GitHub仓库信息确认清单

请确认以下信息：

- [ ] GitHub用户名: `XuHuicong` （请确认是否正确）
- [ ] 仓库名称: `Gobang-Game` （请确认是否正确）
- [ ] 仓库是否为Public
- [ ] 是否有推送权限
- [ ] 网络连接是否正常

### 🔗 正确的仓库URL格式

根据你的GitHub仓库，URL应该是以下格式之一：

```
HTTPS: https://github.com/XuHuicong/Gobang-Game.git
SSH:   git@github.com:XuHuicong/Gobang-Game.git
```

### 💡 替代方案

如果命令行推送一直有问题，你也可以：

1. **使用GitHub Desktop**（图形界面工具）
2. **直接在GitHub网页上传文件**：
   - 访问你的仓库页面
   - 点击"uploading an existing file"
   - 拖拽项目文件上传

### 📞 需要的信息

为了帮你解决问题，请提供：

1. 你的确切GitHub用户名
2. 仓库的确切名称
3. 错误信息的完整内容
4. 仓库是Public还是Private

这样我就能给出更准确的解决方案！