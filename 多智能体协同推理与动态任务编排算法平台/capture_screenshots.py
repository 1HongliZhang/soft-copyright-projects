"""
多智能体协同推理与动态任务编排算法平台 - 桌面应用截图自动化引擎
使用 pywinauto + pyautogui 驱动 Qt6 桌面应用自动截图
"""
import json
import os
import sys
import time
import subprocess
import keyboard
from pathlib import Path

# 截图依赖
try:
    from pywinauto import Application, Desktop
    from pywinauto.findwindows import ElementNotFoundError
    import pyautogui
    from PIL import Image
except ImportError:
    print("安装依赖: pip install pywinauto pyautogui Pillow keyboard")
    sys.exit(1)

# 禁用 pyautogui 的安全机制（防止鼠标移到角落触发异常）
pyautogui.FAILSAFE = False


class ScreenshotEngine:
    """桌面应用截图自动化引擎"""

    def __init__(self, config_path="demo_steps.json"):
        self.config = None
        self.steps = []
        self.app_process = None
        self.app = None
        self.main_window = None
        self.screenshot_dir = "screenshots"
        self.config_path = config_path
        self.step_count = 0
        self.total_steps = 0
        self.window_title = ""

    def load_config(self):
        """加载 demo_steps.json 配置"""
        with open(self.config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)
        self.steps = self.config["steps"]
        self.total_steps = len(self.steps)
        self.window_title = self.config["app"]["window_title"]
        self.screenshot_dir = self.config["app"].get("screenshot_dir", "screenshots")
        os.makedirs(self.screenshot_dir, exist_ok=True)
        print(f"[配置] 加载 {self.total_steps} 个步骤, 截图目录: {self.screenshot_dir}")

    def start_app(self):
        """启动桌面应用"""
        exe_path = self.config["app"]["executable"]
        demo_arg = self.config["app"].get("demo_mode_arg", "--demo")
        startup_delay = self.config["app"].get("startup_delay", 8)

        # 设置 Qt6 DLL 路径
        env = os.environ.copy()
        qt_bin = r"C:\Qt\6.7.0\mingw_64\bin"
        if os.path.isdir(qt_bin):
            env["PATH"] = qt_bin + ";" + env.get("PATH", "")

        print(f"[启动] {exe_path} {demo_arg}")
        self.app_process = subprocess.Popen(
            [exe_path, demo_arg],
            env=env,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

        # 等待窗口出现
        print(f"[等待] {startup_delay} 秒等待窗口启动...")
        time.sleep(startup_delay)

        # 连接到窗口
        self._connect_window()

    def _connect_window(self):
        """连接到应用窗口"""
        try:
            # 使用 UIA 后端连接
            self.app = Application(backend="uia").connect(
                title_re=f".*{self.window_title}.*",
                timeout=10
            )
            self.main_window = self.app.window(title_re=f".*{self.window_title}.*")
            self.main_window.wait("visible", timeout=10)
            print(f"[连接] 成功连接到窗口: {self.window_title}")
        except Exception as e:
            print(f"[连接失败] 尝试 win32 后端: {e}")
            try:
                self.app = Application(backend="win32").connect(
                    title_re=f".*{self.window_title}.*",
                    timeout=10
                )
                self.main_window = self.app.window(title_re=f".*{self.window_title}.*")
                self.main_window.wait("visible", timeout=10)
                print(f"[连接] win32 后端连接成功")
            except Exception as e2:
                print(f"[连接失败] 无法连接到窗口: {e2}")
                raise

    def take_screenshot(self, name):
        """截取当前窗口截图"""
        filepath = os.path.join(self.screenshot_dir, f"{name}.png")
        try:
            # 方法1: 用 pywinauto 截取窗口
            try:
                self.main_window.set_focus()
                time.sleep(0.3)
                rect = self.main_window.rectangle()
                img = pyautogui.screenshot(
                    region=(rect.left, rect.top, rect.width(), rect.height())
                )
                img.save(filepath)
            except Exception:
                # 方法2: 全屏截图
                img = pyautogui.screenshot()
                img.save(filepath)
            print(f"  [截图] 已保存: {name}.png")
        except Exception as e:
            print(f"  [截图失败] {name}: {e}")
            # 仍然尝试全屏截图
            try:
                img = pyautogui.screenshot()
                img.save(filepath)
                print(f"  [截图] 全屏保存: {name}.png")
            except:
                pass

    def click_button_by_name(self, button_name, timeout=5):
        """通过 objectName 点击按钮"""
        try:
            # 尝试通过 UIA 查找控件
            btn = self.main_window.child_window(auto_id=button_name, control_type="Button")
            btn.wait("visible", timeout=timeout)
            btn.click_input()
            return True
        except Exception:
            try:
                # 尝试通过名称查找
                btn = self.main_window.child_window(title=button_name, control_type="Button")
                btn.wait("visible", timeout=timeout)
                btn.click_input()
                return True
            except Exception:
                # 尝试遍历所有按钮
                try:
                    buttons = self.main_window.descendants(control_type="Button")
                    for b in buttons:
                        try:
                            if button_name.lower() in str(b.window_text()).lower() or \
                               button_name.lower() in str(b.element_info.auto_id).lower():
                                b.click_input()
                                return True
                        except:
                            continue
                except:
                    pass
        print(f"  [警告] 未找到按钮: {button_name}")
        return False

    def click_nav_item(self, nav_name, timeout=5):
        """点击导航树项"""
        try:
            # 尝试通过 auto_id 找到树项
            item = self.main_window.child_window(auto_id=nav_name, control_type="TreeItem")
            item.wait("visible", timeout=timeout)
            item.click_input()
            return True
        except Exception:
            try:
                # 尝试通过名称找到树项
                # 从配置中查找模块名
                for mod in self.config.get("modules", []):
                    if mod["nav_control"] == nav_name:
                        item = self.main_window.child_window(
                            title=mod["name"], control_type="TreeItem"
                        )
                        item.wait("visible", timeout=timeout)
                        item.click_input()
                        return True
            except:
                pass
            # 尝试遍历树项
            try:
                items = self.main_window.descendants(control_type="TreeItem")
                for it in items:
                    try:
                        if nav_name.lower() in str(it.element_info.auto_id).lower():
                            it.click_input()
                            return True
                    except:
                        continue
            except:
                pass
        print(f"  [警告] 未找到导航项: {nav_name}")
        return False

    def close_modal_dialog(self):
        """关闭模态弹窗（按ESC或点击确定按钮）"""
        time.sleep(0.5)
        # 尝试按 ESC
        try:
            keyboard.send("esc")
            time.sleep(0.3)
        except:
            pass

        # 尝试点击"确定"或"OK"按钮
        try:
            desktop = Desktop(backend="uia")
            dialogs = desktop.windows()
            for dlg in dialogs:
                try:
                    if dlg.element_info.class_name == "#32770" or "dialog" in str(dlg.window_text()).lower():
                        for btn_text in ["确定", "OK", "关闭", "Close", "取消", "Cancel"]:
                            try:
                                btn = dlg.child_window(title=btn_text, control_type="Button")
                                if btn.exists(timeout=1):
                                    btn.click_input()
                                    time.sleep(0.3)
                                    return
                            except:
                                continue
                except:
                    continue
        except:
            pass

        # 再次按 ESC
        try:
            keyboard.send("esc")
            time.sleep(0.2)
        except:
            pass

    def run(self):
        """执行所有截图步骤"""
        print(f"\n{'='*60}")
        print(f"  桌面应用截图自动化引擎")
        print(f"  共 {self.total_steps} 个步骤")
        print(f"{'='*60}\n")

        for i, step in enumerate(self.steps):
            self.step_count = i + 1
            name = step["name"]
            action = step["action"]
            wait_time = step.get("wait", self.config["app"].get("action_delay", 1.5))

            print(f"\n[步骤 {self.step_count}/{self.total_steps}] {name}")

            try:
                if action == "screenshot":
                    self.take_screenshot(name)

                elif action == "click_button":
                    control = step["control"]
                    print(f"  -> 点击按钮: {control}")
                    self.click_button_by_name(control)
                    time.sleep(wait_time)
                    self.take_screenshot(name)
                    # 关闭可能出现的弹窗
                    self.close_modal_dialog()

                elif action == "click_nav":
                    control = step["control"]
                    print(f"  -> 导航到: {control}")
                    self.click_nav_item(control)
                    time.sleep(wait_time)
                    self.take_screenshot(name)

            except Exception as e:
                print(f"  [错误] 步骤执行失败: {e}")
                # 继续执行下一步

        print(f"\n{'='*60}")
        print(f"  截图完成! 共 {self.step_count} 个步骤")
        print(f"  截图保存目录: {os.path.abspath(self.screenshot_dir)}")
        print(f"{'='*60}")

        # 生成索引页
        self.generate_index_page()

        # 关闭应用
        self.stop_app()

    def generate_index_page(self):
        """生成截图索引HTML页面"""
        html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>截图索引 - 多智能体协同推理与动态任务编排算法平台</title>
<style>
body { background: #0a0e27; color: #e8ecff; font-family: 'Microsoft YaHei', sans-serif; margin: 20px; }
h1 { color: #00f0ff; text-align: center; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 15px; }
.item { background: #141938; border: 1px solid #2a3550; border-radius: 8px; padding: 10px; }
.item:hover { border-color: #00f0ff; }
.item img { width: 100%; border-radius: 4px; }
.item .name { color: #00f0ff; font-size: 14px; margin-top: 8px; }
</style>
</head>
<body>
<h1>多智能体协同推理与动态任务编排算法平台 - 截图索引</h1>
<div class="grid">
"""
        screenshots = sorted(Path(self.screenshot_dir).glob("*.png"))
        for ss in screenshots:
            html += f'<div class="item"><img src="{ss.name}" alt="{ss.stem}"><div class="name">{ss.stem}</div></div>\n'

        html += """</div>
</body>
</html>"""

        index_path = os.path.join(self.screenshot_dir, "index.html")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[索引] 已生成: {index_path}")

    def stop_app(self):
        """关闭应用"""
        try:
            if self.app_process:
                self.app_process.terminate()
                self.app_process.wait(timeout=5)
                print("[关闭] 应用已退出")
        except:
            try:
                self.app_process.kill()
            except:
                pass


def main():
    engine = ScreenshotEngine()
    engine.load_config()
    engine.start_app()
    engine.run()


if __name__ == "__main__":
    main()
