import tkinter as tk

from config import OUT_OF_DATE_DASHBOARD, TODO_DASHBOARD
from dashboard import download_page, collect_team_TC_state, parse_table_for_dash, merge_tables


def get_data():
    # Itt történne az adatok lekérdezése (például adatbázisból vagy API-ból)
    ood_dash = download_page(OUT_OF_DATE_DASHBOARD)
    ood = collect_team_TC_state(parse_table_for_dash(ood_dash))

    todo_dash = download_page(TODO_DASHBOARD)
    todo = collect_team_TC_state(parse_table_for_dash(todo_dash))
    return merge_tables(ood, todo)


def refresh_table(data):
    # Töröljük a korábbi táblázat tartalmát
    for widget in table_frame.winfo_children():
        widget.destroy()

    headers = ["TC", "owner", "ToDo", "OutOfDate"]

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

    # Az oszlopok egyenlően kitöltik a rendelkezésre álló helyet
    for j in range(len(headers)):
        table_frame.grid_columnconfigure(j, weight=1)

    table_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def update_data():
    new_data = get_data()  # Lekérjük az új adatokat
    refresh_table(new_data)  # Frissítjük a táblázatot
    root.after(30000, update_data)  # 30 másodperc múlva újraindítjuk ezt a függvényt

if __name__ == '__main__':
    # Ablak és egyéb widgetek létrehozása
    root = tk.Tk()
    root.title("Adatok Táblázata")

    # Kontrollpanel a "Mindig az élöl" kapcsolóval
    control_frame = tk.Frame(root)
    control_frame.pack(fill=tk.X)

    always_on_top = tk.BooleanVar(value=False)


    def toggle_topmost():
        root.attributes("-topmost", always_on_top.get())


    check = tk.Checkbutton(control_frame, text="Mindig az élöl", variable=always_on_top, command=toggle_topmost)
    check.pack(side=tk.LEFT, padx=5, pady=5)

    # Fő konténer a canvas és scrollbarek számára
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

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

    # Belső frame, ahol a táblázat megjelenik
    table_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=table_frame, anchor="nw")

    # Első adatlekérdezés és a frissítési ciklus indítása
    update_data()

    root.mainloop()

