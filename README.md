# ood-todo_window

in the config.py modify:
USER = "ALL" # username as below or "ALL" if everybody should be seen

replace in the ood_todo.bat this:
start "" "C:\Users\erkmiap\AppData\Local\Microsoft\WindowsApps\pythonw.exe" "C:\Users\erkmiap\PycharmProjects\ood-todo_window\main.py"

to your localisation

Ha szeretnéd, hogy az indító fájl automatikusan elinduljon a Windows bekapcsolásakor, helyezd el egy parancsikont a Windows "Startup" (Indítás) mappájába. Ehhez nyomd meg a Win+R billentyűkombinációt, írd be:

shell:startup

és másold be oda a létrehozott parancsikont.