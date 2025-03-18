import tkinter as tk

from config import OUT_OF_DATE_DASHBOARD, TODO_DASHBOARD, UPDATE_INTERVAL
from dashboard import download_page, collect_team_tc_state, parse_table_for_dash, merge_tables

global_text = ""


def get_data():
    # Itt történik az adatok lekérdezése (például adatbázisból vagy API-ból)
    ood_dash = download_page(OUT_OF_DATE_DASHBOARD)
    ood = collect_team_tc_state(parse_table_for_dash(ood_dash))

    todo_dash = download_page(TODO_DASHBOARD)
    todo = collect_team_tc_state(parse_table_for_dash(todo_dash))
    return merge_tables(ood, todo, global_text)


def refresh_table(data):
    # Töröljük a korábbi táblázat tartalmát
    for widget in table_frame.winfo_children():
        widget.destroy()

    headers = ["Owner", "TC", "ToDo", "OutOfDate"]

    # Fejléc létrehozása (a "TC" balra, a többi középre igazítva)
    for j, header in enumerate(headers):
        anchor = "w" if header == "TC" else "center"
        label = tk.Label(table_frame, text=header, borderwidth=1, relief="solid",
                         padx=5, pady=5, anchor=anchor)
        label.grid(row=0, column=j, sticky="nsew")

    # Adatsorok létrehozása (boolean értékeknél az "X" jelenik meg, ha True)
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
    try:
        new_data = get_data()  # Lekérjük az aktuális adatokat
    except Exception as e:
        # Ha kivétel történik, állítsuk a jelzőt pirosra és írjuk ki a hibaüzenetet a konzolra
        status_indicator.config(bg="red")
        print("Hiba történt az adatok lekérésekor:", e)
    else:
        # Sikeres lekérés esetén állítsuk a jelzőt zöldre
        status_indicator.config(bg="green")
        refresh_table(new_data)  # Frissítjük a táblázatot
    root.after(UPDATE_INTERVAL, update_data)  # megadott másodperc múlva újraindítja ezt a függvényt


def manual_refresh():
    global global_text
    # Frissítjük a global_text értékét a szövegdoboz tartalmával
    global_text = text_var.get()
    # Újrabetöltjük a táblázatot az aktuális adatokkal
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

# Szabadszöveges szövegdoboz, amelynek tartalma a global_text változóból kerül betöltésre
text_var = tk.StringVar(value=global_text)
entry = tk.Entry(control_frame, textvariable=text_var)
entry.pack(side=tk.LEFT, padx=5, pady=5)

# "frissítés" gomb, ami frissíti a global_text értékét és újrabetölti a táblázatot
button = tk.Button(control_frame, text="Update", command=manual_refresh)
button.pack(side=tk.LEFT, padx=5, pady=5)

# Status frame a státuszjelzőnek, ez a keresőmező alá, de a táblázat fölé kerül
status_frame = tk.Frame(root)
status_frame.pack(fill=tk.X)
status_text_label = tk.Label(status_frame, text="lekérdezés eredménye:")
status_text_label.pack(side=tk.LEFT, padx=5, pady=5)
status_indicator = tk.Label(status_frame, text=" ", bg="gray", width=2, height=1, relief="sunken")
status_indicator.pack(side=tk.LEFT, padx=5, pady=5)

# Fő konténer a görgethető tartalomhoz
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

# Canvas létrehozása, melybe a táblázatot tesszük
canvas = tk.Canvas(main_frame)
canvas.grid(row=0, column=0, sticky="nsew")

# Függőleges és vízszintes görgetősávok
v_scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
v_scrollbar.grid(row=0, column=1, sticky="ns")
h_scrollbar = tk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
h_scrollbar.grid(row=1, column=0, sticky="ew")

canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Belső frame, ahol a táblázat megjelenik a canvas-on belül
table_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=table_frame, anchor="nw")

# Az adatfrissítés ciklikusan indul el
update_data()

root.mainloop()
