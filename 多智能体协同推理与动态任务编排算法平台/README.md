# 多智能体协同推理与动态任务编排算法平台

## 项目概述

基于 C++17 + Qt6 Widgets 的多智能体协同推理与动态任务编排桌面应用平台，内置五大核心引擎，提供从智能体画像到效能审计的全链路功能。

## 技术栈

| 项 | 内容 |
|----|------|
| 编程语言 | C++ (C++17) |
| UI框架 | Qt6 Widgets |
| 3D渲染 | QOpenGLWidget + OpenGL |
| 数据库 | SQLite3 |
| 图表 | QtCharts |
| 构建系统 | CMake + MinGW g++ |
| 视觉风格 | 华丽科技风 — 深色霓虹渐变 |

## 目录结构

```
多智能体协同推理与动态任务编排算法平台/
├── main.cpp                    # 程序入口
├── CMakeLists.txt              # CMake 构建配置
├── run.bat                     # 一键启动脚本
├── data/
│   └── platform.db             # SQLite 数据库
├── design/
│   └── design_doc.md           # 设计文档
├── src/
│   ├── core/                   # 五大核心引擎
│   │   ├── Database.h/.cpp
│   │   ├── RBACEngine.h/.cpp
│   │   ├── StateMachineEngine.h/.cpp
│   │   ├── RuleEngine.h/.cpp
│   │   ├── ConsistencyEngine.h/.cpp
│   │   └── AlgorithmEngine.h/.cpp
│   ├── ui/                     # 界面层
│   │   ├── GlobalStyle.h/.cpp
│   │   ├── LoginWindow.h/.cpp
│   │   ├── MainWindow.h/.cpp
│   │   ├── RadialMenu.h/.cpp
│   │   └── Toast.h/.cpp
│   ├── modules/                # 12个业务模块
│   │   ├── ModuleBase.h/.cpp
│   │   ├── Module01Matrix.h/.cpp      # 智能体画像矩阵舱
│   │   ├── Module02Reasoning3D.h/.cpp # 协同推理3D引擎
│   │   ├── Module03Orchestration.h/.cpp # 动态任务编排中枢
│   │   ├── Module04DispatchBus.h/.cpp # 多级分发总线
│   │   ├── Module05Assessment.h/.cpp  # 能力评估矩阵
│   │   ├── Module06Audit.h/.cpp       # 过程审计追踪舱
│   │   ├── Module07StateMonitor.h/.cpp # 状态机监控中枢
│   │   ├── Module08Conflict.h/.cpp     # 冲突消解引擎
│   │   ├── Module09CommMatrix.h/.cpp  # 通信矩阵审计
│   │   ├── Module10Aggregation.h/.cpp # 聚合校验舱
│   │   ├── Module11Simulation.h/.cpp  # 仿真推演引擎
│   │   └── Module12Efficacy.h/.cpp    # 效能审计舱
│   └── utils/
│       └── MathUtils.h/.cpp
├── screenshots/                # 全流程功能截图（83张）
├── generate_docs.py            # 软著申报文档生成器
├── capture_screenshots.py      # 截图自动化脚本
├── demo_steps.json             # 截图步骤定义
├── 代码文档.docx               # 软著代码文档
├── 操作手册.docx               # 软著操作手册
└── 申请表信息.txt              # 软著申请表信息
```

## 五大核心引擎

| 引擎 | 功能 |
|------|------|
| RBAC权限引擎 | 4级角色+7种操作粒度+会话状态流转+锁定策略 |
| 双状态机引擎 | 流程五态+任务七态+状态锁定+快照回滚 |
| 业务规则引擎 | 多条件组合+与或非逻辑+三大触发+冲突检测 |
| 数据一致性引擎 | MVCC事务+锁定回滚+多版本快照+checksum校验 |
| 核心算法集 | 3-5个项目特有算法 |

## 12个功能模块

1. 智能体画像矩阵舱 — 智能体注册、能力画像、批量启用
2. 协同推理3D引擎 — 3D推理可视化、多视角切换
3. 动态任务编排中枢 — 任务编排、拓扑排序、路径优化
4. 多级分发总线 — 任务调度、分发控制
5. 能力评估矩阵 — 能力评估、校验结果
6. 过程审计追踪舱 — 溯源分析、异常标记
7. 状态机监控中枢 — 状态转移、快照回滚
8. 冲突消解引擎 — 冲突检测、自动消解、手动仲裁
9. 通信矩阵审计 — 通道管理、连通测试
10. 聚合校验舱 — 结果融合、聚合校验
11. 仿真推演引擎 — 仿真控制（播放/暂停/停止/步进/重置）
12. 效能审计舱 — 报告生成、基线设定

## 默认账号

| 角色 | 账号 | 密码 |
|------|------|------|
| 系统管理员 | chen_admin | Admin@2024 |
| 高级主管 | wang_director | Dir@2024 |
| 操作员 | liu_operator | Op@2024 |
| 审计员 | zhao_auditor | Aud@2024 |

## 快速启动

双击 `run.bat` 即可自动编译并启动程序。首次运行需要完整编译，依赖：
- MinGW g++ (C++17)
- Qt 6.7.0 (mingw_64)
- CMake

支持 `--demo` 参数启动演示模式。
