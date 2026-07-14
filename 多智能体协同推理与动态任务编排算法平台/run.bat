@echo off
chcp 65001 >nul 2>&1
title 多智能体协同推理与动态任务编排算法平台

echo ============================================================
echo  多智能体协同推理与动态任务编排算法平台
echo  Multi-Agent Collaborative Reasoning and Dynamic
echo  Task Orchestration Algorithm Platform
echo ============================================================
echo.

REM MinGW路径（来自Adaptive项目的便携MinGW）
set MINGW_BIN=D:\ttt\trae\agent-learn\Adaptive_Production_Scheduling_Optimization\mingw64_root\mingw64\bin
set QT_BIN=C:\Qt\6.7.0\mingw_64\bin

REM 将MinGW和Qt加入PATH
set PATH=%MINGW_BIN%;%QT_BIN%;%PATH%

REM 设置CMAKE_PREFIX_PATH
set CMAKE_PREFIX_PATH=C:\Qt\6.7.0\mingw_64

REM 演示模式检测
set DEMO_ARGS=
if "%1"=="--demo" set DEMO_ARGS=--demo

REM 如果exe已存在直接运行
if exist "build\MultiAgentPlatform.exe" (
    echo [启动] 已编译，直接运行...
    set PATH=%QT_BIN%;%PATH%
    cd build
    MultiAgentPlatform.exe %DEMO_ARGS%
    if errorlevel 1 (
        echo.
        echo [错误] 程序异常退出，按任意键关闭...
        pause >nul
    )
    exit /b
)

REM 检查g++
where g++ >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到g++编译器，请检查MinGW路径: %MINGW_BIN%
    pause
    exit /b 1
)

echo [1/3] CMake 配置...
cmake -B build -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=C:\Qt\6.7.0\mingw_64
if errorlevel 1 (
    echo [错误] CMake配置失败
    pause
    exit /b 1
)

echo.
echo [2/3] 编译中（首次编译需要较长时间）...
cmake --build build --config Release -j
if errorlevel 1 (
    echo [错误] 编译失败
    pause
    exit /b 1
)

echo.
echo [3/3] 启动程序...
set PATH=%QT_BIN%;%PATH%
cd build
MultiAgentPlatform.exe %DEMO_ARGS%
if errorlevel 1 (
    echo.
    echo [错误] 程序异常退出，按任意键关闭...
    pause >nul
)
