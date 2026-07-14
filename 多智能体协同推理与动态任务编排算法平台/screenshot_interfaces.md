# 截图接口清单

> 多智能体协同推理与动态任务编排算法平台
> 编程语言：PHP (Web) | 截图方案：Selenium WebDriver

## 全局控件

| 控件名 | ID | 说明 |
|--------|-----|------|
| 登录按钮 | `btn-login` | 登录页提交 |
| 刷新概览 | `btn-refresh-overview` | 首页刷新 |
| 切换账号 | `btn-switch-account` | 顶栏切换 |
| 退出登录 | `btn-logout` | 顶栏退出 |
| 径向菜单切换 | `btn-radial-toggle` | 导航栏径向菜单 |
| 日志清空 | `btn-log-clear` | 底部日志区 |
| 模态确定 | `modal-ok` | 弹窗确认按钮 |
| 切换取消 | `switch-cancel` | 切换账号取消 |
| 切换确认 | `switch-confirm` | 切换账号确认 |

## 导航树控件

| 模块 | 导航ID | 模块名 |
|------|--------|--------|
| 1 | `nav-btn-1` | 智能体注册与画像矩阵 |
| 2 | `nav-btn-2` | 多智能体协同推理引擎 |
| 3 | `nav-btn-3` | 动态任务编排中枢 |
| 4 | `nav-btn-4` | 任务调度与分发总线 |
| 5 | `nav-btn-5` | 智能体能力评估校验 |
| 6 | `nav-btn-6` | 协同推理过程审计 |
| 7 | `nav-btn-7` | 任务状态机监控舱 |
| 8 | `nav-btn-8` | 冲突检测与消解引擎 |
| 9 | `nav-btn-9` | 智能体通信通道矩阵 |
| 10 | `nav-btn-10` | 推理结果聚合校验 |
| 11 | `nav-btn-11` | 编排策略仿真推演舱 |
| 12 | `nav-btn-12` | 系统运行效能审计 |

## 模块1：智能体注册与画像矩阵

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-refresh-matrix` | 刷新矩阵 | card_highlight |
| `btn-register-agent` | 注册智能体 | modal（弹窗） |
| `btn-export-profile` | 导出画像 | toast |
| `btn-batch-enable` | 批量启用 | table_flash |

## 模块2：多智能体协同推理引擎（3D）

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-start-reasoning` | 启动推理 | background_pulse |
| `btn-stop-reasoning` | 停止推理 | background_pulse |
| `btn-view-top` | 俯视 | panel_switch |
| `btn-view-side` | 侧视 | panel_switch |
| `btn-view-free` | 自由 | panel_switch |
| `btn-refresh-3d` | 刷新状态 | card_highlight |

## 模块3：动态任务编排中枢

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-add-task` | 添加任务 | modal（弹窗） |
| `btn-topo-sort` | 拓扑排序 | table_flash |
| `btn-optimize-path` | 优化路径 | toast |
| `btn-refresh-dag` | 刷新图 | card_highlight |

## 模块4：任务调度与分发总线

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-start-dispatch` | 开始调度 | background_pulse |
| `btn-pause-dispatch` | 暂停调度 | panel_switch |
| `btn-clear-dispatch-log` | 清空日志 | table_flash |
| `btn-export-dispatch` | 导出报告 | modal（弹窗） |

## 模块5：智能体能力评估校验

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-run-assessment` | 运行评估 | table_flash |
| `btn-validate-result` | 校验结果 | modal（弹窗） |
| `btn-export-assessment` | 导出报告 | toast |
| `btn-refresh-assessment` | 刷新数据 | card_highlight |

## 模块6：协同推理过程审计

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-trace-chain` | 溯源分析 | modal（弹窗） |
| `btn-export-audit` | 导出审计 | toast |
| `btn-mark-anomaly` | 标记异常 | background_pulse |
| `btn-refresh-tree` | 刷新树 | card_highlight |

## 模块7：任务状态机监控舱

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-refresh-state` | 刷新状态 | card_highlight |
| `btn-force-transition` | 强制转移 | modal（弹窗） |
| `btn-snapshot-rollback` | 快照回滚 | toast |
| `btn-export-state` | 导出状态 | toast |

## 模块8：冲突检测与消解引擎

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-detect-conflict` | 检测冲突 | table_flash |
| `btn-auto-resolve` | 自动消解 | toast |
| `btn-manual-arbitrate` | 手动仲裁 | modal（弹窗） |
| `btn-refresh-heatmap` | 刷新热力图 | card_highlight |

## 模块9：智能体通信通道矩阵

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-create-channel` | 创建通道 | modal（弹窗） |
| `btn-batch-channel` | 批量通道 | table_flash |
| `btn-test-ping` | 连通测试 | toast |
| `btn-refresh-comm` | 刷新通信 | card_highlight |

## 模块10：推理结果聚合校验

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-execute-fusion` | 执行融合 | modal（弹窗） |
| `btn-validate-aggregation` | 校验聚合 | toast |
| `btn-export-aggregation` | 导出聚合 | toast |
| `btn-refresh-aggregation` | 刷新聚合 | card_highlight |

## 模块11：编排策略仿真推演舱

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-config-sim` | 配置仿真 | panel_switch |
| `btn-run-simulation` | 运行仿真 | background_pulse |
| `btn-compare-strategy` | 策略对比 | modal（弹窗） |
| `btn-refresh-sim` | 刷新仿真 | card_highlight |
| `btn-sim-play` | 播放 | background_pulse |
| `btn-sim-pause` | 暂停 | panel_switch |
| `btn-sim-stop` | 停止 | panel_switch |
| `btn-sim-step` | 步进 | toast |
| `btn-sim-reset` | 重置 | table_flash |

## 模块12：系统运行效能审计

| 按钮ID | 按钮文本 | 反馈类型 |
|--------|---------|---------|
| `btn-generate-report` | 生成报告 | modal（弹窗） |
| `btn-export-audit` | 导出审计 | toast |
| `btn-set-baseline` | 设定基线 | toast |
| `btn-refresh-audit` | 刷新审计 | card_highlight |

## 默认账号体系

| 账号 | 密码 | 角色 | 姓名 |
|------|------|------|------|
| chen_admin | Admin@2024 | admin（管理员） | 陈志远 |
| wang_director | Dir@2024 | director（主管） | 王慧敏 |
| liu_operator | Op@2024 | operator（操作员） | 刘建国 |
| zhao_auditor | Aud@2024 | auditor（审计员） | 赵雅琴 |
