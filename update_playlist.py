import requests
import os

# CONFIGURAZIONE SORGENTI
SOURCES = [
    'http://vitftopuptop.xubi.org:25461/get.php?username=Pluto&password=m3WxRfR&type=m3u_plus&output=ts',
    'http://bl4ck.loseyourip.com/get.php?username=Slovenia&password=mHHNJtW&type=m3u_plus&output=mpegts'
]

def main():
    combined_content = "#EXTM3U\n"
    
    for source in SOURCES:
        try:
            response = requests.get(source, timeout=10)
            if response.status_code == 200:
                lines = response.text.split('\n')
                for line in lines:
                    if line.startswith('#') or line.startswith('http'):
                        combined_content += line + '\n'
                print(f"[OK] Sorgente OK: {source[:60]}...")
            else:
                print(f"[WARN] Status {response.status_code} su: {source}")
                
        except Exception as e:
            print(f"[ERR] Errore: {str(e)[:50]}")

    # Scrive nella radice (Netlify pubplica la radice se publish=".")
    with open('playlist.m3u', 'w', encoding='utf-8') as f:
        f.write(combined_content)
        
    total_channels = combined_content.count('http')
    print(f">>> PLAYLIST AGGIORNATA. CANALI TOTALI: {total_channels}")

if __name__ == '__main__':
    main()
