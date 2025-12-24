call venv/Scripts/activate
pyinstaller --onefile macro_tool.py --paths=venv/Lib/site-packages --hidden-import=pyperclip
