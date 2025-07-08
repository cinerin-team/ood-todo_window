import tkinter as tk
import importlib
import config
import dashboard
from config import OUT_OF_DATE_DASHBOARD, TODO_DASHBOARD, UPDATE_INTERVAL
from dashboard import download_page, collect_team_tc_state, parse_table_for_dash, merge_tables

global_text = ""
# Collect unique owners from constants module
owners = sorted({v["owner"] for v in dashboard.tc_const.TCS.values()})

def get_data():
    # Itt történik az adatok lekérdezése (például adatbázisból vagy API-ból)
    ood_dash = download_page(OUT_OF_DATE_DASHBOARD)[0]
    result = download_page(OUT_OF_DATE_DASHBOARD)[1]
    parsed_ood = parse_table_for_dash(ood_dash)
    if parsed_ood[0][0] == True and result:
        ood = collect_team_tc_state(parsed_ood[0][1])
        status_indicator_ood.config(bg="green")
    else:
        ood = []
        status_indicator_ood.config(bg="red")

    todo_dash = download_page(TODO_DASHBOARD)[0]
    result = download_page(TODO_DASHBOARD)[1]
    parsed_todo = parse_table_for_dash(todo_dash)
    if parsed_todo[0][0] == True and result:
        todo = collect_team_tc_state(parsed_todo[0][1])
        status_indicator_todo.config(bg="green")
    else:
        todo = []
        status_indicator_todo.config(bg="red")

    return merge_tables(ood, todo, global_text)

def refresh_table(data):
    # Töröljük a korábbi táblázat tartalmát
    for widget in table_frame.winfo_children():
        widget.destroy()

    headers = ["Owner", "TC", "ToDo", "OutOfDate"]
    # Fejléc létrehozása
    for j, header in enumerate(headers):
        anchor = "w" if header == "TC" else "center"
        label = tk.Label(table_frame, text=header, borderwidth=1, relief="solid",
                         padx=5, pady=5, anchor=anchor)
        label.grid(row=0, column=j, sticky="nsew")

    # Adatsorok létrehozása
    for i, row in enumerate(data, start=1):
        processed_row = row[:2] + [('X' if row[2] else ''), ('X' if row[3] else '')]
        for j, value in enumerate(processed_row):
            anchor = "w" if headers[j] == "TC" else "center"
            label = tk.Label(table_frame, text=value, borderwidth=1, relief="solid",
                             padx=5, pady=5, anchor=anchor)
            label.grid(row=i, column=j, sticky="nsew")

    # Oszlopok egyenlő kitöltése
    for j in range(len(headers)):
        table_frame.grid_columnconfigure(j, weight=1)

    table_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def update_data():
    new_data = get_data()
    refresh_table(new_data)
    root.after(UPDATE_INTERVAL, update_data)

def manual_refresh():
    global global_text
    global_text = text_var.get()
    refresh_table(get_data())

# Új: filter function to apply owner filter
def filter_owner(owner):
    global global_text
    global_text = owner
    text_var.set(owner)
    refresh_table(get_data())

# Ablak létrehozása
root = tk.Tk()
root.title("Adatok Táblázata")

# Kontrollpanel létrehozása a kapcsolókhoz és vezérlőkhöz
control_frame = tk.Frame(root)
control_frame.pack(fill=tk.X)

# "Mindig az élöl" kapcsoló
always_on_top = tk.BooleanVar(value=False)
def toggle_topmost():
    root.attributes("-topmost", always_on_top.get())
check = tk.Checkbutton(control_frame, text="Always on top", variable=always_on_top, command=toggle_topmost)
check.pack(side=tk.LEFT, padx=5, pady=5)

# Szabadszöveges szövegdoboz
text_var = tk.StringVar(value=global_text)
entry = tk.Entry(control_frame, textvariable=text_var)
entry.pack(side=tk.LEFT, padx=5, pady=5)

# "Update" gomb
button = tk.Button(control_frame, text="Update", command=manual_refresh)
button.pack(side=tk.LEFT, padx=5, pady=5)

# Új: owner filter gombok
filter_frame = tk.Frame(root)
filter_frame.pack(fill=tk.X, padx=5, pady=(0,10))

# "All" gomb minden tulajdonos megjelenítéséhez
all_button = tk.Button(filter_frame, text="All", command=lambda: filter_owner(""))
all_button.pack(side=tk.LEFT, padx=2)

# Dinamikus gombok az egyes tulajdonosokhoz
for owner in owners:
    btn = tk.Button(filter_frame, text=owner, command=lambda o=owner: filter_owner(o))
    btn.pack(side=tk.LEFT, padx=2)

# Status frame a státuszjelzőknek
status_frame_todo = tk.Frame(root)
status_frame_todo.pack(fill=tk.X)
status_text_label = tk.Label(status_frame_todo, text="todo lekérdezés eredménye:")
status_text_label.pack(side=tk.LEFT, padx=5, pady=5)
status_indicator_todo = tk.Label(status_frame_todo, text=" ", bg="gray", width=2, height=1, relief="sunken")
status_indicator_todo.pack(side=tk.LEFT, padx=5, pady=5)

status_frame_ood = tk.Frame(root)
status_frame_ood.pack(fill=tk.X)
status_text_label2 = tk.Label(status_frame_ood, text="ood lekérdezés eredménye:")
status_text_label2.pack(side=tk.LEFT, padx=5, pady=5)
status_indicator_ood = tk.Label(status_frame_ood, text=" ", bg="gray", width=2, height=1, relief="sunken")
status_indicator_ood.pack(side=tk.LEFT, padx=5, pady=5)

# Fő konténer a görgethető tartalomhoz
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

canvas = tk.Canvas(main_frame)
canvas.grid(row=0, column=0, sticky="nsew")

# Scrollbarok
v_scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
v_scrollbar.grid(row=0, column=1, sticky="ns")
h_scrollbar = tk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
h_scrollbar.grid(row=1, column=0, sticky="ew")

canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
def _on_mousewheel(event):
    canvas.yview_scroll(-1 * int(event.delta/120), "units")

# Amikor az egér a canvas fölé ér, bind-oljuk a görgőt...
canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
# …és amikor elhagyja, le is oldjuk
canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Belső frame a táblázathoz
table_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=table_frame, anchor="nw")

# Indítás\ nupdate_data()
root.mainloop()
