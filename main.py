import tkinter as tk
from tkinter import ttk, messagebox
import requests

# ==========================
# Configuration de l'API
# ==========================
API_KEY = "YOUR_API_KEY"  # 🔑 Remplace ça par ta clé OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_temperature(country):
    params = {
        'q': country,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'fr'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            return data['main']['temp']
        else:
            return None
    except Exception:
        return None

def show_temperature():
    if check_var.get():
        country = entry_country.get()
        if country:
            temp = get_temperature(country)
            if temp is not None:
                messagebox.showinfo("Température", f"🌡 La température actuelle à {country} est de {temp}°C.")
            else:
                messagebox.showerror("Erreur", "❌ Impossible de récupérer les données météo.")
        else:
            messagebox.showwarning("Champ vide", "✏️ Veuillez entrer le nom de votre pays.")
    else:
        messagebox.showwarning("Case non cochée", "✅ Veuillez cocher la case pour activer la recherche.")

# ==========================
# Interface Graphique
# ==========================
root = tk.Tk()
root.title("🌍 Temperature Checker by Hani TAHER")
root.geometry("400x250")
root.resizable(False, False)

# Style
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10, "bold"), foreground="#ffffff", background="#007ACC")
style.map("TButton", background=[("active", "#005F99")])
style.configure("TCheckbutton", font=("Segoe UI", 10))

# Frame
frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

# Titre
label_title = ttk.Label(frame, text="Développé par Hani TAHER", font=("Segoe UI", 12, "italic"), foreground="#555")
label_title.pack(pady=(0, 10))

# Checkbox
check_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(frame, text="Entrer le nom de votre pays", variable=check_var)
checkbox.pack(pady=(0, 10))

# Champ texte
entry_country = ttk.Entry(frame, width=30)
entry_country.pack(pady=5)

# Bouton
btn = ttk.Button(frame, text="Afficher la température", command=show_temperature)
btn.pack(pady=20)

root.mainloop()
