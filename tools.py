"""
AI Video Tools - AI视频工具
支持视频脚本、分镜、字幕生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIVideoTools:
    """
    AI视频工具
    支持：脚本、分镜、字幕
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_script(self, topic: str, duration: str, style: str) -> Dict:
        """生成视频脚本"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请生成{topic}的{style}风格视频脚本：

时长：{duration}

请返回JSON格式：
{{
    "title": "标题",
    "scenes": [
        {{"timestamp": "时间", "visual": "画面", "narration": "旁白", "text": "字幕"}}
    ],
    "tags": ["标签"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"script": content}

    def generate_subtitles(self, transcript: str, style: str = "简洁") -> str:
        """生成字幕"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据以下转录生成SRT字幕：

{transcript[:2000]}

风格：{style}

要求：
1. SRT格式
2. 每行不超过20字
3. 时间轴准确"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_video_description(self, content: str, platform: str) -> Dict:
        """生成视频描述"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{platform}生成视频描述：

内容：{content[:500]}

请返回JSON格式：
{{
    "title": "标题",
    "description": "描述",
    "tags": ["标签"],
    "thumbnail_text": "缩略图文字"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"description": content}

    def suggest_hooks(self, topic: str, count: int = 5) -> List[str]:
        """建议视频开头钩子"""
        if not self.client:
            return ["LLM客户端未配置"]

        prompt = f"""请为{topic}视频建议{count}个开头钩子：

要求：
1. 吸引注意力
2. 引发好奇心
3. 10秒内

请返回JSON数组格式：["钩子1", "钩子2", ...]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [response.choices[0].message.content]

    def generate_chapters(self, content: str) -> List[Dict]:
        """生成视频章节"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请根据以下内容生成视频章节：

{content[:1000]}

请返回JSON格式：
[
    {{"timestamp": "00:00", "title": "标题", "description": "描述"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"chapters": content}]

    def generate_storyboard(self, script: Dict) -> List[Dict]:
        """生成分镜脚本"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        script_text = json.dumps(script, ensure_ascii=False)

        prompt = f"""请根据以下脚本生成分镜：

{script_text[:1000]}

请返回JSON格式：
[
    {{"scene": 1, "shot": "镜头", "description": "描述", "duration": "时长"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"storyboard": content}]


def create_tools(**kwargs) -> AIVideoTools:
    """创建视频工具"""
    return AIVideoTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Video Tools")
    print()

    # 测试
    hooks = tools.suggest_hooks("Python教程", 3)
    print("Hooks:", hooks)
