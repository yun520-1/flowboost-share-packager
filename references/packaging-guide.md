---
name: flowboost-share-packager
version: 1.0.1
description: 生成 FlowBoost 的可分享技能包，清理内部文件并输出适合发布的 SKILL.md/ZIP 结构。
author: HeartFlow
homepage: https://github.com/yun520-1/mark-heartflow-skill
tags:
  - flowboost
  - skill-packaging
  - zip
  - sharing
metadata:
  openclaw:
    emoji: "📦"
    requires:
      bins: ["zip", "python3"]
    os:
      - darwin
      - linux
---

# FlowBoost 分享打包器

将 FlowBoost 插件整理为**可分享的 skill 包**。目标不是保留完整开发仓库，而是生成一个适合上传、转发和复用的最小可用技能包。

## When to Use

- 用户要把 FlowBoost 分享给别人
- 用户要把 FlowBoost 打包成 skill/ZIP
- 用户希望把插件改写成更标准的公开技能
- 需要移除内部实现、缓存、日志、私有文件后再发布

## When NOT to Use

- 只是本地继续开发 FlowBoost
- 需要保留完整仓库历史或调试信息
- 用户只想做一次性的临时压缩

## Quick Start

1. 找到 FlowBoost 的真实源目录
2. 提取对外可见的技能说明
3. 保留最小发布集：`SKILL.md`、必要的 `references/`、必要脚本
4. 删除内部文件、缓存、日志、测试工件
5. 重新打包并检查文件数与大小

## 发布原则

### 1. 保留什么

优先保留：
- `SKILL.md`
- 少量必要的 `scripts/`
- 少量必要的 `references/`
- 发布所需的 README（若平台允许）

### 2. 删除什么

应删除或不打包：
- `.git/`
- `__pycache__/`
- `.pyc`
- 日志、缓存、临时输出
- 个人备注、对话记录、内部 identity 文档
- 无关历史版本和备份

### 3. 结构要求

技能包应遵循渐进式披露：
- 顶层 `SKILL.md` 说明用途和启动方式
- 复杂细节放入 `references/`
- 具体流程放入 `scripts/` 或 `workflows/`

## 标准化写法

建议将 FlowBoost 技能描述成“终端输出优化器”而非内部插件实现细节。这样更利于分享和复用。

### 推荐能力描述

- 压缩重复输出
- 合并相似日志
- 提取错误上下文
- 智能截断大输出
- 保留关键诊断信息

### 推荐触发场景

- 构建日志过长
- 重复警告/错误过多
- 命令行输出爆炸
- 需要节省 token 和阅读成本

## 打包检查

发布前至少检查：

- 文件数是否控制在平台限制内
- ZIP 大小是否符合要求
- 是否包含 `SKILL.md`
- 是否混入私有文件或缓存
- 是否删除了调试产物

## 交付建议

如果用户要分享给别人，优先输出两份内容：

1. **可读版 SKILL.md**：用于展示和复用
2. **可上传 ZIP**：用于技能市场或直接分发

## 安全提示

不要把以下内容放入分享包：
- API key
- 内部日志
- 私人记忆
- 个人配置文件
- 未脱敏的测试样本

## 输出风格

尽量把技能写成可直接理解、可直接部署的模块，而不是开发备忘录。
