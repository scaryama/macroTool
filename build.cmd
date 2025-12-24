call venv\Scripts\activate.bat
pyinstaller --onefile macro_tool.py --paths=venv\Lib\site-packages --hidden-import=pynput --hidden-import=pyperclip --hidden-import=pynput.keyboard --hidden-import=pynput.mouse
