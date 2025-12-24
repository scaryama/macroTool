# pip install pyinstaller

from pynput import keyboard
import pyperclip
import subprocess
import winsound
import json
import os


# Config 파일 로드
def load_config():
    config_path = "config.json"
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        print("config.json 파일을 찾을 수 없습니다.")
        return None

config = load_config()
keyboard_controller = keyboard.Controller()
cmd_directory = config["cmd_directory"]

def type_text(text):
    # 텍스트를 클립보드에 복사
    pyperclip.copy(text)

    # 잠시 대기 (필요에 따라 조정 가능)
    #time.sleep(0.1)

    # Ctrl + V 를 사용하여 텍스트 붙여넣기
    keyboard_controller.press(keyboard.Key.ctrl)
    keyboard_controller.press('v')
    keyboard_controller.release('v')
    keyboard_controller.release(keyboard.Key.ctrl)

def play_sound():
    winsound.Beep(600, 100)
    winsound.Beep(800, 100)
    winsound.Beep(1000, 200)

def create_func(func_name):
    def func():
        if not config or func_name not in config["commands"]:
            return
        
        command = config["commands"][func_name]
        if len(command) > 0:
            play_sound()
        if command.startswith("cmd:"):
            cmd_path = command[4:]  # "cmd:" 제거
            subprocess.Popen(cmd_path, shell=True, cwd=cmd_directory, encoding='cp949')
            return
        
        if command.startswith("text:"):
            text = command[5:]  # "text:" 제거
            if text:
                type_text(text)
    return func

# 모든 함수 생성
on_func1 = create_func("func1")
on_func2 = create_func("func2")
on_func3 = create_func("func3")
on_func4 = create_func("func4")
on_func5 = create_func("func5")
on_func6 = create_func("func6")
on_func7 = create_func("func7")
on_func8 = create_func("func8")
on_func9 = create_func("func9")
on_func10 = create_func("func10")
on_func11 = create_func("func11")
on_func12 = create_func("func12")

key_actions = {
    keyboard.Key.f13: on_func1,
    keyboard.Key.f14: on_func2,
    keyboard.Key.f15: on_func3,
    keyboard.Key.f16: on_func4,
    keyboard.Key.f17: on_func5,
    keyboard.Key.f18: on_func6,
    keyboard.Key.f19: on_func7,
    keyboard.Key.f20: on_func8,
    keyboard.Key.f21: on_func9,
    keyboard.Key.f22: on_func10,
    keyboard.Key.f23: on_func11,
    keyboard.Key.f24: on_func12,
}
key_short = {
    keyboard.Key.f1: on_func1,
    keyboard.Key.f2: on_func2,
    keyboard.Key.f3: on_func3,
    keyboard.Key.f4: on_func4,
    keyboard.Key.f5: on_func5,
    keyboard.Key.f6: on_func6,
    keyboard.Key.f7: on_func7,
    keyboard.Key.f8: on_func8,
    keyboard.Key.f9: on_func9,
    keyboard.Key.f10: on_func10,
    keyboard.Key.f11: on_func11,
    keyboard.Key.f12: on_func12,
}

# 키 상태 추적 set
last_short_key = None
pressed_keys = set()
key_combination = {keyboard.Key.ctrl_l, keyboard.Key.alt_l}
isCombination = False

def on_press(key):
    global last_short_key
    global isCombination
    if isCombination and key in key_short:
        last_short_key = key

    if key in key_combination and key not in pressed_keys:
        pressed_keys.add(key)
        #print(f"{key} 눌림: {pressed_keys}")

        if pressed_keys == key_combination:
            isCombination = True
            last_short_key = None
            #print("모두 누름")

def on_release(key):
    global isCombination
    global last_short_key
    if key in key_combination and key in pressed_keys:
        pressed_keys.remove(key)
        #print(f"{key} 뗌: {pressed_keys}")

    # 모든 키가 눌렸다가 떼어진 경우 조건 확인
    if isCombination and len(pressed_keys) == 0:
        isCombination = False
        #print(f"모두 땜, 마지막 눌린 키: {last_short_key}")
        if last_short_key in key_short:
            key_short[last_short_key]()
        last_short_key = None

    if key in key_actions:
        key_actions[key]()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 