# 🎬 AI Video Tools

AI视频工具，支持视频脚本、分镜、字幕生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 视频脚本生成
- 📝 SRT字幕生成
- 📺 视频描述生成
- 🎣 开头钩子建议
- 📋 章节生成
- 🎬 分镜脚本生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_video_tools import create_tools

tools = create_tools()

# 视频脚本
script = tools.generate_script("Python教程", "10分钟", "教育")

# 字幕
subtitles = tools.generate_subtitles(transcript, "简洁")

# 视频描述
description = tools.generate_video_description("Python入门", "YouTube")

# 开头钩子
hooks = tools.suggest_hooks("Python编程", 5)

# 章节
chapters = tools.generate_chapters(video_content)

# 分镜
storyboard = tools.generate_storyboard(script)
```

## 📁 项目结构

```
ai-video-tools/
├── tools.py       # 视频工具核心
└── README.md
```

## 📄 许可证

MIT License
