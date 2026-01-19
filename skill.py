import os
import subprocess
import json
import sys
from pathlib import Path

def load_config():
    """加载配置文件"""
    try:
        # 获取脚本所在目录的绝对路径
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, 'config.json')
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def get_github_client_path(client_type='default'):
    """根据操作系统和客户端类型获取GitHub GUI客户端路径"""
    config = load_config()
    client_paths = config.get('client_paths', {})
    system_defaults = config.get('system_defaults', {})
    
    # 优先使用配置的客户端路径
    if client_type in client_paths:
        return client_paths[client_type]
    
    # 获取系统类型
    if sys.platform == 'win32':
        system_key = 'windows'
    elif sys.platform == 'darwin':
        system_key = 'macos'
    else:
        system_key = 'linux'
    
    # 使用系统默认路径
    system_paths = system_defaults.get(system_key, {})
    if client_type in system_paths:
        default_path = system_paths[client_type]
        if os.path.exists(default_path):
            return default_path
    
    # 系统默认路径列表
    if sys.platform == 'win32':
        # Windows
        default_paths = [
            r'C:\Program Files\GitHub Desktop\GitHubDesktop.exe',
            r'C:\Program Files (x86)\GitHub Desktop\GitHubDesktop.exe',
            os.path.expanduser(r'~\AppData\Local\GitHubDesktop\GitHubDesktop.exe')
        ]
    elif sys.platform == 'darwin':
        # macOS
        default_paths = [
            '/Applications/GitHub Desktop.app/Contents/MacOS/GitHub Desktop'
        ]
    else:
        # Linux
        default_paths = [
            '/usr/bin/github-desktop',
            '/usr/local/bin/github-desktop'
        ]
    
    for path in default_paths:
        if os.path.exists(path):
            return path
    
    return None

def get_trendradar_info():
    """获取TrendRadar项目信息"""
    # 尝试获取TrendRadar项目的根目录
    skill_dir = os.path.dirname(os.path.abspath(__file__))
    trendradar_dir = os.path.abspath(os.path.join(skill_dir, '..', '..'))
    
    # 检查是否为TrendRadar项目目录
    if os.path.exists(os.path.join(trendradar_dir, 'trendradar')):
        return {
            'root_dir': trendradar_dir,
            'is_trendradar': True,
            'version_file': os.path.join(trendradar_dir, 'version'),
            'output_dir': os.path.join(trendradar_dir, 'output')
        }
    return {
        'is_trendradar': False
    }

def check_trendradar_status():
    """检查TrendRadar项目状态"""
    info = get_trendradar_info()
    if not info['is_trendradar']:
        return None
    
    status = {
        'root_dir': info['root_dir'],
        'is_trendradar': True,
        'has_version': os.path.exists(info['version_file']),
        'has_output': os.path.exists(info['output_dir']),
        'news_files': []
    }
    
    # 检查新闻数据库文件
    news_dir = os.path.join(info['output_dir'], 'news')
    if os.path.exists(news_dir):
        news_files = list(Path(news_dir).glob('*.db'))
        status['news_files'] = [str(f) for f in news_files]
        status['latest_news_file'] = str(news_files[-1]) if news_files else None
    
    return status

def launch_github_gui(github_path='', client_type='default'):
    """启动GitHub GUI客户端"""
    client_path = get_github_client_path(client_type)
    
    if not client_path:
        config = load_config()
        installation_guide = config.get('installation_guide', {})
        
        # 获取系统对应的下载链接
        if sys.platform == 'win32':
            system_key = 'windows'
            system_name = 'Windows'
        elif sys.platform == 'darwin':
            system_key = 'macos'
            system_name = 'macOS'
        else:
            system_key = 'linux'
            system_name = 'Linux'
        
        # 根据客户端类型选择下载链接
        if client_type == 'fork':
            fork_guide = installation_guide.get('fork', {})
            download_link = fork_guide.get(system_key, 'https://git-fork.com/download')
            client_name = 'Fork'
        else:
            github_desktop_guide = installation_guide.get('github_desktop', {})
            download_link = github_desktop_guide.get(system_key, 'https://desktop.github.com/download')
            client_name = 'GitHub Desktop'
        
        return {
            'status': 'error',
            'message': f'未找到{client_name}客户端，请按照以下步骤安装：\n' +
                      f'1. 访问{client_name}下载页面: {download_link}\n' +
                      f'2. 下载并安装适合{system_name}系统的{client_name}\n' +
                      f'3. 安装完成后，再次运行此技能\n' +
                      f'\n系统: {sys.platform}'
        }
    
    try:
        # 构建命令参数
        args = [client_path]
        
        # 处理特殊情况：如果未提供路径且在TrendRadar目录中
        if not github_path:
            trendradar_status = check_trendradar_status()
            if trendradar_status and trendradar_status['is_trendradar']:
                # 使用TrendRadar的GitHub仓库URL
                github_path = 'https://github.com/sansan0/TrendRadar'
        
        if github_path:
            # 检查是否为URL
            if github_path.startswith('http://') or github_path.startswith('https://'):
                # 是URL，直接传递给客户端
                args.append(github_path)
            else:
                # 是本地路径，检查是否存在
                if os.path.exists(github_path):
                    args.append(github_path)
                else:
                    return {
                        'status': 'warning',
                        'message': f'指定的GitHub仓库路径不存在: {github_path}'
                    }
        
        # 启动客户端
        subprocess.Popen(args, shell=True)
        
        # 构建返回消息
        message = f'成功启动GitHub GUI客户端: {os.path.basename(client_path)}'
        if github_path:
            message += f'，打开仓库: {github_path}'
        
        # 添加TrendRadar项目状态信息
        trendradar_status = check_trendradar_status()
        if trendradar_status:
            message += f'\n\nTrendRadar项目状态:\n'
            message += f'- 项目目录: {trendradar_status["root_dir"]}\n'
            if trendradar_status.get('latest_news_file'):
                message += f'- 最新新闻数据: {os.path.basename(trendradar_status["latest_news_file"])}\n'
            message += f'- 新闻文件数量: {len(trendradar_status.get("news_files", []))}'
        
        return {
            'status': 'success',
            'message': message
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'启动GitHub GUI客户端失败: {str(e)}'
        }

def main():
    """主函数"""
    # 解析命令行参数
    import argparse
    parser = argparse.ArgumentParser(description='GitHub GUI客户端启动器')
    parser.add_argument('--github_path', type=str, default='', help='GitHub仓库路径')
    parser.add_argument('--client_type', type=str, default='default', help='GUI客户端类型')
    parser.add_argument('--trendradar', action='store_true', help='使用TrendRadar项目信息')
    
    args = parser.parse_args()
    
    # 执行启动
    result = launch_github_gui(args.github_path, args.client_type)
    
    # 输出结果
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result

if __name__ == '__main__':
    main()
