import geopandas as gpd
#import pypandoc
import webbrowser
import os
#pypandoc.download_pandoc()

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

# CSS
css_content = """
body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #f7f7f9;
    color: #222;
    margin: 0;
    padding: 0;
}
.container {
    max-width: 800px;
    margin: 40px auto;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    padding: 32px 40px 40px 40px;
}
h1, h2 {
    color: #2c3e50;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 32px;
    background: #fafbfc;
}
th, td {
    border: 1px solid #d1d5db;
    padding: 10px 16px;
    text-align: left;
}
th {
    background: #e5e7eb;
    color: #222;
}
tr:nth-child(even) td {
    background: #f3f4f6;
}
hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 32px 0;
}
.remark {
    font-size: 0.95em;
    color: #555;
    background: #f9fafb;
    border-left: 4px solid #4f8ef7;
    padding: 12px 18px;
    margin-top: 24px;
    border-radius: 4px;
}
"""

# Write the CSS file
with open("output_A33/statistiques_ouvrages.css", "w", encoding="utf-8") as f:
    f.write(css_content)

# HTML content with CSS link and container
report_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Analyse Statistique des Ouvrages Sélectionnés</title>
    <link rel="stylesheet" href="statistiques_ouvrages.css">
</head>
<body>
<div class="container">
<h1>Analyse Statistique des Ouvrages Sélectionnés</h1>
<p>Ce document présente les statistiques descriptives calculées à partir du fichier <strong>output_A33/selected_ouvrages.gpkg</strong>.</p>

<h2>1. Longueur des ouvrages (<code>length</code>)</h2>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{length_max}</td></tr>
<tr><td><strong>Minimum</strong></td><td>{length_min}</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{length_mean}</td></tr>
<tr><td><strong>Médiane</strong></td><td>{length_median}</td></tr>
</table>

<h2>2. Hauteur moyenne (<code>hauteur_moyenne</code>)</h2>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{hauteur_moyenne_max}</td></tr>
<tr><td><strong>Minimum</strong></td><td>{hauteur_moyenne_min}</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{hauteur_moyenne_mean}</td></tr>
</table>

<h2>3. Hauteur maximale (<code>hauteur_max</code>)</h2>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{hauteur_max_max}</td></tr>
</table>

<hr>
<div class="remark">
<strong>Remarques :</strong><br>
- Les valeurs sont extraites automatiquement du fichier GeoPackage.<br>
- Pour obtenir les valeurs numériques, exécutez le script Python <code>analyse_ouvrages.py</code>.
</div>
</div>
</body>
</html>
"""

with open("output_A33/statistiques_ouvrages.html", "w", encoding="utf-8") as f:
    f.write(report_html)

import webbrowser, os
html_path = os.path.abspath("output_A33/statistiques_ouvrages.html")
webbrowser.open_new_tab(f"file:///{html_path}")

