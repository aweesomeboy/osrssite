import os
import time
import json
import requests

CACHE_FILE = "osrs_cache.json"
CACHE_DURATION = 300  # 5 minut v sekundah

# OSRS Wiki zahteva unikaten User-Agent. Spremenite 'VaseIme' v nekaj unikatnega.
HEADERS = {
    'User-Agent': 'OSRS Wiki Dashboard - @VaseIme'
}

def get_osrs_data():
    # Preverimo, če lokalni cache že obstaja in je še svež
    if os.path.exists(CACHE_FILE):
        file_age = time.time() - os.path.getmtime(CACHE_FILE)
        if file_age < CACHE_DURATION:
            try:
                with open(CACHE_FILE, 'r') as f:
                    print("Uporabljam lokalno shranjene podatke (Cache)...")
                    return json.load(f)
            except Exception:
                pass

    # Če cache ne obstaja ali je zastarel, pokličemo API
    url = "https://runescape.wiki"
    try:
        print("Kličem OSRS Wiki API...")
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_style == 200:
            data = response.json()
            
            # Shranimo podatke v lokalno datoteko za naslednjič
            with open(CACHE_FILE, 'w') as f:
                json.dump(data, f)
            return data
        else:
            print(f"API napaka: {response.status_style}")
    except requests.RequestException as e:
        print(f"Povezava do API-ja je spodletela: {e}")
        
    # V primeru napake poskusimo vrniti vsaj stare podatke iz cache-a, če obstajajo
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
            
    return {"data": {}}
