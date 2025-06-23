import geopandas as gpd
import pypandoc
import markdown
import pdfkit
import webbrowser
import os
pypandoc.download_pandoc()

# Charger le fichier GeoPackage
gdf = gpd.read_file("output_A33/selected_ouvrages.gpkg")

# Statistiques sur la longueur
length_max = gdf['length'].max()
length_min = gdf['length'].min()
length_mean = gdf['length'].mean()
length_median = gdf['length'].median()

# Statistiques sur hauteur_moyenne
hauteur_moyenne_max = gdf['hauteur_moyenne'].max()
hauteur_moyenne_min = gdf['hauteur_moyenne'].min()
hauteur_moyenne_mean = gdf['hauteur_moyenne'].mean()

# Statistique sur hauteur_max
hauteur_max_max = gdf['hauteur_max'].max()

# Affichage des résultats
report_md = f"""# Analyse Statistique des Ouvrages Sélectionnés

Ce document présente les statistiques descriptives calculées à partir du fichier **output_A33/selected_ouvrages.gpkg**.

## 1. Longueur des ouvrages (`length`)

| Statistique | Valeur        |
|-------------|--------------|
| **Maximum** | {length_max}  |
| **Minimum** | {length_min}  |
| **Moyenne** | {length_mean} |
| **Médiane** | {length_median} |

## 2. Hauteur moyenne (`hauteur_moyenne`)

| Statistique | Valeur                |
|-------------|----------------------|
| **Maximum** | {hauteur_moyenne_max} |
| **Minimum** | {hauteur_moyenne_min} |
| **Moyenne** | {hauteur_moyenne_mean} |

## 3. Hauteur maximale (`hauteur_max`)

| Statistique | Valeur            |
|-------------|------------------|
| **Maximum** | {hauteur_max_max} |

---

**Remarques :**
- Les valeurs sont extraites automatiquement du fichier GeoPackage.
- Pour obtenir les valeurs numériques, exécutez le script Python `analyse_ouvrages.py`.
"""

with open("output_A33/statistiques_ouvrages.md", "w", encoding="utf-8") as f:
    f.write(report_md)

md_path = "output_A33/statistiques_ouvrages.md"
pdf_path = "output_A33/statistiques_ouvrages.pdf"

# Convert markdown to PDF
with open("output_A33/statistiques_ouvrages.md", encoding="utf-8") as f:
    html = markdown.markdown(f.read())

with open("output_A33/statistiques_ouvrages.html", "w", encoding="utf-8") as f:
    f.write(html)

html_path = os.path.abspath("output_A33/statistiques_ouvrages.html")
webbrowser.open_new_tab(f"file:///{html_path}")

report_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Analyse Statistique des Ouvrages Sélectionnés</title>
</head>
<body>
<h1>Analyse Statistique des Ouvrages Sélectionnés</h1>
<p>Ce document présente les statistiques descriptives calculées à partir du fichier <strong>output_A33/selected_ouvrages.gpkg</strong>.</p>

<h2>1. Longueur des ouvrages (<code>length</code>)</h2>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{length_max}</td></tr>
<tr><td><strong>Minimum</strong></td><td>{length_min}</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{length_mean}</td></tr>
<tr><td><strong>Médiane</strong></td><td>{length_median}</td></tr>
</table>

<h2>2. Hauteur moyenne (<code>hauteur_moyenne</code>)</h2>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{hauteur_moyenne_max}</td></tr>
<tr><td><strong>Minimum</strong></td><td>{hauteur_moyenne_min}</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{hauteur_moyenne_mean}</td></tr>
</table>

<h2>3. Hauteur maximale (<code>hauteur_max</code>)</h2>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{hauteur_max_max}</td></tr>
</table>

<hr>
<p><strong>Remarques :</strong><br>
- Les valeurs sont extraites automatiquement du fichier GeoPackage.<br>
- Pour obtenir les valeurs numériques, exécutez le script Python <code>analyse_ouvrages.py</code>.
</p>
</body>
</html>
"""

with open("output_A33/statistiques_ouvrages.html", "w", encoding="utf-8") as f:
    f.write(report_html)

import webbrowser, os
html_path = os.path.abspath("output_A33/statistiques_ouvrages.html")
webbrowser.open_new_tab(f"file:///{html_path}")

