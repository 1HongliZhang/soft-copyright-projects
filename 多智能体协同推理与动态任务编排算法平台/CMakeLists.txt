cmake_minimum_required(VERSION 3.16)
project(MultiAgentPlatform CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Qt6路径 - aqtinstall安装位置
set(CMAKE_PREFIX_PATH "C:/Qt/6.7.0/mingw_64" ${CMAKE_PREFIX_PATH})

# 寻找Qt6
find_package(Qt6 REQUIRED COMPONENTS Widgets Charts OpenGL OpenGLWidgets)
qt_standard_project_setup()

# 中文显示与编码
if(MSVC)
    add_compile_options(/utf-8)
else()
    add_compile_options(-Wall -O2 -finput-charset=UTF-8 -fexec-charset=UTF-8)
endif()

# SQLite3 - 使用MinGW自带的或Qt的QtSql
find_library(SQLITE3_LIB sqlite3 PATHS "D:/ttt/trae/agent-learn/Adaptive_Production_Scheduling_Optimization/mingw64_root/mingw64/lib")
if(NOT SQLITE3_LIB)
    # 使用内置SQLite3实现（嵌入sqlite3.c amalgamation）
    set(SQLITE3_LIB "")
    set(USE_EMBEDDED_SQLITE ON)
endif()

# 收集源文件
set(CORE_SOURCES
    src/core/Database.cpp
    src/core/RBACEngine.cpp
    src/core/StateMachineEngine.cpp
    src/core/RuleEngine.cpp
    src/core/ConsistencyEngine.cpp
    src/core/AlgorithmEngine.cpp
)

set(UI_SOURCES
    src/ui/GlobalStyle.cpp
    src/ui/Toast.cpp
    src/ui/LoginWindow.cpp
    src/ui/MainWindow.cpp
    src/ui/RadialMenu.cpp
)

set(MODULE_SOURCES
    src/modules/ModuleBase.cpp
    src/modules/Module01Matrix.cpp
    src/modules/Module02Reasoning3D.cpp
    src/modules/Module03Orchestration.cpp
    src/modules/Module04DispatchBus.cpp
    src/modules/Module05Assessment.cpp
    src/modules/Module06Audit.cpp
    src/modules/Module07StateMonitor.cpp
    src/modules/Module08Conflict.cpp
    src/modules/Module09CommMatrix.cpp
    src/modules/Module10Aggregation.cpp
    src/modules/Module11Simulation.cpp
    src/modules/Module12Efficacy.cpp
)

set(UTIL_SOURCES
    src/utils/MathUtils.cpp
)

# 嵌入式SQLite3
if(USE_EMBEDDED_SQLITE)
    list(APPEND CORE_SOURCES src/core/sqlite3.c)
endif()

# 可执行文件
qt_add_executable(MultiAgentPlatform
    main.cpp
    ${CORE_SOURCES}
    ${UI_SOURCES}
    ${MODULE_SOURCES}
    ${UTIL_SOURCES}
)

# 包含路径
target_include_directories(MultiAgentPlatform PRIVATE
    src
    src/core
    src/ui
    src/modules
    src/utils
    include
)

# 链接库
target_link_libraries(MultiAgentPlatform PRIVATE
    Qt6::Widgets
    Qt6::Charts
    Qt6::OpenGL
    Qt6::OpenGLWidgets
)

if(SQLITE3_LIB)
    target_link_libraries(MultiAgentPlatform PRIVATE ${SQLITE3_LIB})
endif()

# Windows控制台隐藏
if(WIN32)
    set_target_properties(MultiAgentPlatform PROPERTIES
        WIN32_EXECUTABLE TRUE
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}
    )
endif()

# 安装规则
install(TARGETS MultiAgentPlatform RUNTIME DESTINATION bin)
