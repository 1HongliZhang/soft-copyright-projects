// ============================================================
// 模块质量标签: [MAIN-ENTRY] 程序入口 / S级样板
// 依赖: Qt6 Widgets, 全部UI组件, 核心引擎
// 功能: 应用程序初始化 / 数据库初始化 / 登录流程 / 主窗口启动
// 说明: 支持 --demo 参数自动填充登录信息
// ============================================================
#include <QApplication>
#include <QFontDatabase>
#include <QDir>
#include <QFileInfo>
#include <QString>
#include <QDialog>

#include "ui/LoginWindow.h"
#include "ui/MainWindow.h"
#include "ui/GlobalStyle.h"
#include "core/Database.h"

// 尝试打开数据库 (兼容从 build 目录或项目根目录运行)
static bool openDatabase() {
    // 优先尝试: 项目根目录下的 data/platform.db
    // 当从 build/ 目录运行时, 使用 ../data/platform.db
    // 当从项目根运行时, 使用 data/platform.db
    QStringList candidates = {
        QStringLiteral("../data/platform.db"),
        QStringLiteral("data/platform.db"),
        QStringLiteral("platform.db")
    };

    for (const QString& path : candidates) {
        // 确保目录存在
        QFileInfo fi(path);
        QDir().mkpath(fi.absolutePath());

        if (Database::getInstance().open(path.toStdString())) {
            return true;
        }
    }
    return false;
}

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);
    app.setApplicationName(QStringLiteral("多智能体协同推理与动态任务编排算法平台"));
    app.setStyleSheet(GlobalStyle::getGlobalStyleSheet());

    // 初始化数据库
    if (!openDatabase()) {
        // 数据库打开失败, 继续运行(部分功能可能不可用)
    }
    Database::getInstance().initSchema();
    Database::getInstance().seedData();

    // 检测演示模式
    bool demoMode = false;
    for (int i = 1; i < argc; i++) {
        if (QString(argv[i]) == "--demo") demoMode = true;
    }

    // 登录窗口
    LoginWindow login(demoMode);
    if (login.exec() != QDialog::Accepted) return 0;

    // 主窗口
    MainWindow mainWin;
    mainWin.setUser(login.getSelectedUser());
    mainWin.show();

    return app.exec();
}
