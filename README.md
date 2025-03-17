# ood-todo_window
if you want to create your own user and tc list copy the actual cinerin_tc.py file and create the same structure, and modify the config.py (CONSTANTS_MODULE) to load this new file

replace in the ood_todo.bat this:
start "" "C:\Users\erkmiap\AppData\Local\Microsoft\WindowsApps\pythonw.exe" "C:\Users\erkmiap\PycharmProjects\ood-todo_window\main.py"

to your localisation

Ha szeretnéd, hogy az indító fájl automatikusan elinduljon a Windows bekapcsolásakor, helyezd el egy parancsikont a Windows "Startup" (Indítás) mappájába. Ehhez nyomd meg a Win+R billentyűkombinációt, írd be:

shell:startup

és másold be oda a létrehozott parancsikont.