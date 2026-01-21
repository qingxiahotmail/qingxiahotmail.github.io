# GitHub GUI Launcher 技能项目

## 项目简介
GitHub GUI Launcher 是一个专为 Trae IDE 设计的技能项目，允许用户通过图形界面快速启动和管理 GitHub 仓库。

## 项目功能
- 提供直观的图形界面来浏览和启动 GitHub 仓库
- 支持本地仓库管理和远程仓库同步
- 集成到 Trae IDE 的技能系统中，实现快速访问
- 自动化部署和配置流程

## 项目结构
```
.
├── README_trae.md          # Trae 技能使用说明
├── TRAE_SETUP_GUIDE.md     # Trae 技能设置指南
├── config.json             # 技能配置文件
├── config_input.json       # 输入配置文件
├── requirements.txt        # 依赖项列表
├── skill.py                # 技能主脚本
├── skill.yaml              # 技能定义文件
└── qingxiahotmail.github.io/  # 个人主页模板（备用）
```

## 安装和使用
### 方法一：直接添加到 Trae 设置
1. 下载本仓库的完整文件：
   - **直接下载 ZIP 文件**：[https://github.com/qingxiahotmail/qingxiahotmail.github.io/archive/refs/heads/master.zip](https://github.com/qingxiahotmail/qingxiahotmail.github.io/archive/refs/heads/master.zip)
2. 将文件复制到 Trae 的技能目录中
3. 在 Trae IDE 中启用该技能
4. 按照 `TRAE_SETUP_GUIDE.md` 中的说明进行配置

### 方法二：通过 GitHub 克隆
1. 克隆仓库（指定主分支）：
   ```
   git clone -b main https://github.com/qingxiahotmail/qingxiahotmail.github.io.git
   ```
2. 进入项目目录：
   ```
   cd qingxiahotmail.github.io
   ```
3. 按照 `README_trae.md` 中的说明进行安装和配置

## 如何添加到 Trae 设置
1. 打开 Trae IDE
2. 进入设置页面
3. 选择"技能"选项
4. 点击"添加技能"
5. 选择本项目的 `skill.yaml` 文件
6. 点击"启用"按钮
7. 按照提示完成配置

## 技术栈
- Python 3.x
- Trae IDE 技能系统
- GitHub API
- 图形界面库

## 许可证
本项目基于 MIT 许可协议，你可以自由使用和修改。

## 更新记录
- 2026-01-21：项目初始化和发布
- 2026-01-21：添加 Trae 技能设置指南
- 2026-01-21：完善项目文档

## 贡献
欢迎提交问题和建议，帮助改进这个项目。
