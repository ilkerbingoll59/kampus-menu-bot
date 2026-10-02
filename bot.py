import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
GRUP_ID = os.getenv("GRUP_ID")
ADMIN_SIFRE = os.getenv("ADMIN_SIFRE")

MENU = {
    0: ["Mercimek çorbası", "Tavuk sote", "Pilav", "Ayran"],
    1: ["Ezogelin çorbası", "Kuru fasulye", "Bulgur pilavı", "Turşu"],
    2: ["Yayla çorbası", "Fırın köfte", "Patates püresi", "Sütlaç"],
    3: ["Domates çorbası", "Etli nohut", "Pilav", "Cacık"],
    4: ["Tarhana çorbası", "Karnıyarık", "Makarna", "Kemalpaşa tatlısı"],
}

def bugunun_menusu():
    gun = date.today().weekday()
    if gun not in MENU:
        return "Hafta sonu yemekhane kapalı."
    return "Bugünün menüsü:\n- " + "\n- ".join(MENU[gun])

if __name__ == "__main__":
    print(bugunun_menusu())
