# nonebot-plugin-bilinovel

> NoneBot2 哔哩轻小说爬虫插件，搜索小说并下载生成 EPUB 电子书

## 📦 安装

### 方式一：使用 nb‑cli


```bash
nb plugin install nonebot-plugin-bilinovel
```

### 方式二：pip 安装插件
```bash
pip install nonebot-plugin-bilinovel
```

### 安装 Playwright 浏览器内核

```bash
playwright install chromium
```

## 🎯 使用命令

### 参数标记约定

- `< >` 必填参数，不可省略
- `[ ]` 可选参数，可以省略

表格

| 指令 | 语法 | 说明 |
| --- | --- | --- |
| `/sear` | `/sear <小说名称>` | 搜索哔哩轻小说，返回书本 id |
| `/down` | `/down <书本id> <卷号> [下载格式]` | 下载小说并生成 EPUB 或 txt |

> 搜索示例：`/sear 关于我转生变成史莱姆这档事`
>           `/sear 游戏人生`
>
> 
> 下载示例：`/down 9 1 epub` 即下载书籍 id 为 9 的第一卷，导出格式为 epub
>
> 
> [下载格式不填默认txt]

## ⚙️ .env自定义参数配置


可调整参数列表：

```
# Playwright浏览器无头开关，True：无头 /False：有头
BROWSER_HEADLESS = True  #无头情况下epub模式可能获取不到图片
# 章节并发数，并发多容易限流
WORKER_COUNT = 2
```


## ⚠️ 使用须知

1. 本插件仅用于个人学习研究。
2. 请勿高频、大规模爬取网站，避免给目标站点造成压力。
3. 下载内容版权归原作者与平台所有。

## 📁 文件输出

生成的 EPUB 文件将会保存至插件运行目录下。

## 📝 更新日志

### v0.1.0

- 基础小说搜索功能
- 小说章节错峰并发爬取
- EPUB 电子书导出