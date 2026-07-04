import requests
import os

# CONFIGURAZIONE SORGENTI
SOURCES = [
    # Sorgente 1: La base principale (Vitftopuptop)
    'http://vitftopuptop.xubi.org:25461/get.php?username=Pluto&password=m3WxRfR&type=m3u_plus&output=ts',
    
    # Sorgente 2: Il nuovo link aggiunto (Bl4ck - Slovenia/User)
    'http://bl4ck.loseyourip.com/get.php?username=Slovenia&password=mHHNJtW&type=m3u_plus&output=mpegts'
]

def main():
    combined_content = "#EXTM3U\n"
    
    for source in SOURCES:
        try:
            # Timeout di 10 secondi
            response = requests.get(source, timeout=10)
            if response.status_code == 200:
                lines = response.text.split('\n')
                for line in lines:
                    # Filtra solo linee valide M3U
                    if line.startswith('#') or line.startswith('http'):
                        combined_content += line + '\n'
                print(f"[OK] Sorgente OK: {source[:60]}...")
            else:
                print(f"[WARN] Status {response.status_code} su: {source[:60]}...")
                
        except Exception as e:
            print(f"[ERR] Sorgente FALLITA: {source[:60]}... Errore: {str(e)[:50]}")

    # Scrivi la playlist combinata nel file locale
    # Assicurati che la cartella public esista o usa la radice
    if not os.path.exists('public'):
        os.makedirs('public')
        
    # Scrivi nella cartella che Netlify preferisce spesso
    with open('public/playlist.m3u', 'w', encoding='utf-8') as f:
        f.write(combined_content)
        f.write(combined_content)
        
    total_channels = combined_content.count('http')
    print(f"\n>>> PLAYLIST AGGIORNATA. CANALI TOTALI: {total_channels}\n")

if __name__ == '__main__':
    main()
