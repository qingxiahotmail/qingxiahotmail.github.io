# GitHub GUI Launcher - trae.cn专用说明

## 项目概述

GitHub GUI Launcher 是一个用于快速启动 GitHub GUI 客户端的工具，支持多种操作系统和客户端类型。该工具可以帮助用户更方便地管理和操作 GitHub 仓库。

## 功能特点

- 支持 Windows、macOS 和 Linux 操作系统
- 自动检测系统中已安装的 GitHub GUI 客户端
- 支持自定义客户端路径和类型
- 可以直接打开指定的 GitHub 仓库
- 提供详细的状态和错误信息

## 支持的客户端

- GitHub Desktop (默认)
- Fork
- 自定义客户端

## 使用方法

### 命令行使用

```bash
python skill.py --github_path "path/to/your/repo" --client_type "default"
```

### 参数说明

| 参数名称 | 类型 | 必需 | 默认值 | 描述 |
|---------|------|------|-------|------|
| github_path | string | 否 | "" | GitHub 仓库路径 |
| client_type | string | 否 | "default" | GUI 客户端类型 |

### 配置文件

可以通过修改 `config.json` 文件来自定义客户端路径和其他设置：

```json
{
  "client_paths": {
    "default": "C:\\Program Files\\GitHub Desktop\\GitHubDesktop.exe",
    "fork": "C:\\Program Files\\Fork\\Fork.exe"
  }
}
```

## 输入输出示例

### 输入

```json
{
  "github_path": "C:\\Users\\user\\Documents\\my-repo",
  "client_type": "default"
}
```

### 输出

```json
{
  "status": "success",
  "message": "成功启动GitHub GUI客户端: C:\\Program Files\\GitHub Desktop\\GitHubDesktop.exe，打开仓库: C:\\Users\\user\\Documents\\my-repo"
}
```

## 注意事项

1. 确保已安装至少一种 GitHub GUI 客户端
2. 对于自定义客户端路径，请确保路径正确且具有执行权限
3. 仓库路径必须是本地已存在的 Git 仓库
4. 在 Windows 系统中，路径分隔符请使用双反斜杠 (\\) 或正斜杠 ()

## 故障排除

### 客户端未找到

如果出现 "未找到GitHub GUI客户端" 错误，请：
1. 检查是否已安装 GitHub GUI 客户端
2. 在 `config.json` 中手动指定客户端路径
3. 确保路径中没有拼写错误

### 仓库路径无效

如果出现 "指定的GitHub仓库路径不存在" 警告，请：
1. 检查仓库路径是否正确
2. 确保该路径是本地已存在的 Git 仓库
3. 确保您有访问该路径的权限

## 平台兼容性

| 操作系统 | 支持状态 | 测试版本 |
|---------|---------|---------|
| Windows | ✅ 完全支持 | Windows 10/11 |
| macOS | ✅ 完全支持 | macOS 10.15+ |
| Linux | ✅ 完全支持 | Ubuntu 20.04+ |

## 版本信息

- 版本: 1.0.0
- 发布日期: 2024-01-19
- 开发者: trae.cn

## 更新日志

### v1.0.0 (2024-01-19)
- 初始版本发布
- 支持三种操作系统
- 支持多种 GitHub GUI 客户端
- 提供详细的错误处理和状态信息

## 联系方式

如有问题或建议，请联系 trae.cn 平台支持