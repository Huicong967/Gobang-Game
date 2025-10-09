# 贡献指南

感谢你对五子棋游戏项目的关注！我们欢迎所有形式的贡献。

## 如何贡献

### 报告 Bug

如果你发现了 bug，请在 GitHub Issues 中报告：

1. 使用清晰、描述性的标题
2. 详细描述重现步骤
3. 提供期望的行为和实际行为
4. 如果可能，提供屏幕截图
5. 注明你的操作系统和 Python 版本

### 功能建议

我们欢迎新功能的建议：

1. 在 Issues 中描述你的想法
2. 解释为什么这个功能有用
3. 提供具体的实现思路（如果有）

### 代码贡献

#### 开发环境设置

1. Fork 这个仓库
2. 克隆你的 fork：
```bash
git clone https://github.com/yourusername/gobang-game.git
```

3. 创建开发分支：
```bash
git checkout -b feature/your-feature-name
```

4. 安装开发依赖：
```bash
pip install -r requirements.txt
```

#### 编码规范

- 遵循 PEP 8 Python 编码规范
- 使用 `black` 进行代码格式化
- 使用 `flake8` 进行代码检查
- 为新功能编写测试用例

#### 提交代码

1. 确保所有测试通过：
```bash
pytest
```

2. 检查代码格式：
```bash
flake8 .
black --check .
```

3. 提交你的更改：
```bash
git add .
git commit -m "Add feature: your feature description"
```

4. 推送到你的 fork：
```bash
git push origin feature/your-feature-name
```

5. 创建 Pull Request

#### Pull Request 规范

- 使用清晰、描述性的标题
- 在描述中解释你的更改
- 关联相关的 Issues（如果有）
- 确保 CI 检查通过

## 行为准则

### 我们的承诺

为了营造一个开放和友好的环境，我们承诺让每个人都能参与我们的项目和社区，无论年龄、身体状况、残疾、民族、性别认同和表达、经验水平、教育背景、社会经济地位、国籍、个人外貌、种族、宗教或性取向如何。

### 我们的标准

有助于创造积极环境的行为包括：

- 使用友善和包容性的语言
- 尊重不同的观点和经验
- 优雅地接受建设性批评
- 专注于对社区最有益的事情
- 对其他社区成员表示同理心

不可接受的行为包括：

- 使用性化的语言或图像以及不受欢迎的性关注或性骚扰
- 恶意评论、人身攻击或政治攻击
- 公开或私人骚扰
- 未经明确许可发布他人的私人信息，如物理地址或电子邮件地址
- 在专业环境中可能被合理认为不当的其他行为

## 问题和支持

如果你有任何问题，可以通过以下方式联系我们：

- 创建 GitHub Issue
- 发送邮件到 [your-email@example.com]

谢谢你的贡献！