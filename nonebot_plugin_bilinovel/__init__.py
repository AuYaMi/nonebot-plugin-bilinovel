from nonebot.plugin import PluginMetadata
from . import novel

__plugin_meta__ = PluginMetadata(
    name="哔哩轻小说爬虫",
    description="搜索并下载哔哩轻小说，生成EPUB电子书",
    usage="/sear 小说名",
    supported_adapters={"~onebot.v11"},
)
