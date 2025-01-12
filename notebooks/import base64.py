import base64
from pathlib import Path
import re

def embed_images_in_html(html_file):
    # HTML-Datei einlesen
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Suche nach Bildern in der HTML-Datei...")
    
    # Alle img-Tags mit src Attribut finden
    img_pattern = re.compile(r'<img[^>]+src="([^"]+)"')
    matches = img_pattern.finditer(content)
    
    found_images = False
    
    # Jeden Bildpfad durch Base64-kodiertes Bild ersetzen
    for match in matches:
        found_images = True
        img_path = match.group(1)
        print(f"\nGefundener Bildpfad: {img_path}")
        
        if img_path.startswith('data:'):
            print("Bild ist bereits Base64-kodiert, überspringe...")
            continue
            
        # Relativen Pfad in absoluten umwandeln
        full_path = img_path
        if img_path.startswith('..'):
            full_path = Path(html_file).parent / img_path
            print(f"Vollständiger Bildpfad: {full_path}")
        
        try:
            with open(full_path, 'rb') as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
                
            # Dateiendung bestimmen
            extension = Path(img_path).suffix.lower()[1:]  # '.jpg' -> 'jpg'
            img_type = f'image/{extension}'
            
            # Ursprünglichen Pfad durch Base64-Daten ersetzen
            base64_src = f'data:{img_type};base64,{img_data}'
            content = content.replace(match.group(1), base64_src)
            print(f'Bild erfolgreich eingebettet: {img_path}')
            
        except FileNotFoundError:
            print(f'FEHLER: Bild nicht gefunden: {full_path}')
        except Exception as e:
            print(f'FEHLER beim Verarbeiten von {img_path}: {str(e)}')
    
    if not found_images:
        print("WARNUNG: Keine Bilder in der HTML-Datei gefunden!")
    
    # Neue HTML-Datei mit eingebetteten Bildern speichern
    output_file = str(Path(html_file).parent / f"{Path(html_file).stem}_embedded.html")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'\nFertig! Neue Datei erstellt: {output_file}')

# Verwendung
html_file = r'C:\Users\laukat\OneDrive - Mediengruppe RTL\HDM Data Analyti\project\reports\report.html'
embed_images_in_html(html_file)