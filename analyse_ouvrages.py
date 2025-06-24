import geopandas as gpd
import webbrowser
import os

# Demander le code de la route à l'utilisateur
route = input("Saisir le code de la route (ex. A33): ")

# Charger le fichier GeoPackage
input_file = f"output_{route}/selected_ouvrages.gpkg"
gdf = gpd.read_file(input_file)

# Split en remblai, deblai et rasant
remblai = gdf[gdf['classification'] == 'remblai']
deblai = gdf[gdf['classification'] == 'deblai']
rasant = gdf[gdf['classification'] == 'rasant']

# Statistiques générales tout
total_ouvrage = round(len(gdf), 2)
total_length = round(gdf['length'].sum(), 2)

# Statistiques sur la longueur tout
length_max = round(gdf['length'].max(), 2)
length_min = round(gdf['length'].min(), 2)
length_mean = round(gdf['length'].mean(), 2)
length_median = round(gdf['length'].median(), 2)

# Statistiques générales remblai
total_ouvrage_remblai = round(len(remblai), 2)
total_length_remblai = round(remblai['length'].sum(), 2)

# Statistiques sur la longueur remblai
length_max_remblai = round(remblai['length'].max(), 2)
length_min_remblai = round(remblai['length'].min(), 2)
length_mean_remblai = round(remblai['length'].mean(), 2)
length_median_remblai = round(remblai['length'].median(), 2)

# Statistiques sur hauteur_moyenne remblai
hauteur_moyenne_max_remblai = round(remblai['hauteur_moyenne'].max(), 2)
hauteur_moyenne_min_remblai = round(remblai['hauteur_moyenne'].min(), 2)
hauteur_moyenne_mean_remblai = round(remblai['hauteur_moyenne'].mean(), 2)
hauteur_moyenne_median_remblai = round(remblai['hauteur_moyenne'].median(), 2)

# Statistique sur hauteur_max remblai
hauteur_max_max_remblai = round(remblai['hauteur_max'].max(), 2)
hauteur_max_min_remblai = round(remblai['hauteur_max'].min(), 2)
hauteur_max_mean_remblai = round(remblai['hauteur_max'].mean(), 2)
hauteur_max_median_remblai = round(remblai['hauteur_max'].median(), 2)

# Statistiques sur pente_moyenne remblai
pente_moyenne_max_remblai = round(remblai['pente_moyenne'].max(), 2)
pente_moyenne_min_remblai = round(remblai['pente_moyenne'].min(), 2)
pente_moyenne_mean_remblai = round(remblai['pente_moyenne'].mean(), 2)
pente_moyenne_median_remblai = round(remblai['pente_moyenne'].median(), 2)

# Statistique sur pente_max remblai
pente_max_max_remblai = round(remblai['pente_max'].max(), 2)
pente_max_min_remblai = round(remblai['pente_max'].min(), 2)
pente_max_mean_remblai = round(remblai['pente_max'].mean(), 2)
pente_max_median_remblai = round(remblai['pente_max'].median(), 2)

# Statistiques générales deblai
total_ouvrage_deblai = round(len(deblai), 2)
total_length_deblai = round(deblai['length'].sum(), 2)

# Statistiques sur la longueur deblai
length_max_deblai = round(deblai['length'].max(), 2)
length_min_deblai = round(deblai['length'].min(), 2)
length_mean_deblai = round(deblai['length'].mean(), 2)
length_median_deblai = round(deblai['length'].median(), 2)

# Statistiques sur hauteur_moyenne deblai
hauteur_moyenne_max_deblai = round(deblai['hauteur_moyenne'].max(), 2)
hauteur_moyenne_min_deblai = round(deblai['hauteur_moyenne'].min(), 2)
hauteur_moyenne_mean_deblai = round(deblai['hauteur_moyenne'].mean(), 2)
hauteur_moyenne_median_deblai = round(deblai['hauteur_moyenne'].median(), 2)

# Statistique sur hauteur_max deblai
hauteur_max_max_deblai = round(deblai['hauteur_max'].max(), 2)
hauteur_max_min_deblai = round(deblai['hauteur_max'].min(), 2)
hauteur_max_mean_deblai = round(deblai['hauteur_max'].mean(), 2)
hauteur_max_median_deblai = round(deblai['hauteur_max'].median(), 2)

# Statistiques sur pente_moyenne deblai
pente_moyenne_max_deblai = round(deblai['pente_moyenne'].max(), 2)
pente_moyenne_min_deblai = round(deblai['pente_moyenne'].min(), 2)
pente_moyenne_mean_deblai = round(deblai['pente_moyenne'].mean(), 2)
pente_moyenne_median_deblai = round(deblai['pente_moyenne'].median(), 2)

# Statistique sur pente_max deblai
pente_max_max_deblai = round(deblai['pente_max'].max(), 2)
pente_max_min_deblai = round(deblai['pente_max'].min(), 2)
pente_max_mean_deblai = round(deblai['pente_max'].mean(), 2)
pente_max_median_deblai = round(deblai['pente_max'].median(), 2)

# Statistiques générales rasant
total_ouvrage_rasant = round(len(rasant), 2)
total_length_rasant = round(rasant['length'].sum(), 2)

# Statistiques sur la longueur rasant
length_max_rasant = round(rasant['length'].max(), 2)
length_min_rasant = round(rasant['length'].min(), 2)
length_mean_rasant = round(rasant['length'].mean(), 2)
length_median_rasant = round(rasant['length'].median(), 2)

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
output_folder_css = f"output_{route}/statistiques_ouvrages.css"
with open(output_folder_css, "w", encoding="utf-8") as f:
    f.write(css_content)

# HTML content with CSS link and container
report_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Analyse statistique des ouvrages de la route {route}</title>
    <link rel="stylesheet" href="statistiques_ouvrages.css">
</head>
<body>
<div class="container">
<h1>Analyse statistique des ouvrages de la route {route}</h1>
<p>Ce document présente les statistiques descriptives calculées à partir du fichier <strong>output_{route}/selected_ouvrages.gpkg</strong>.</p>

<h2>Statistiques globales</h2>
<p>Le fichier contient des informations sur les ouvrages de la route, classés en trois catégories : <strong>remblai</strong>, <strong>déblai</strong> et <strong>rasant</strong>.</p>

<h3>1. Statistiques générales</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Nombre total des ouvrages (somme des deux directions)</strong></td><td>{total_ouvrage}</td></tr>
<tr><td><strong>Longueur totale des ouvrages (somme des deux directions)</strong></td><td>{total_length} m</td></tr>
</table>

<h3>2. Longueur des ouvrages (<code>length</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{length_max} m</td></tr>
<tr><td><strong>Minimum</strong></td><td>{length_min} m</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{length_mean} m</td></tr>
<tr><td><strong>Médiane</strong></td><td>{length_median} m</td></tr>
</table>

<h1>Analyse par type d'ouvrage</h1>
<h2>Ouvrage de type <strong>remblai</strong></h2>

<h3>1. Statistiques générales des ouvrages de remblai</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Nombre total des ouvrages (somme des deux directions)</strong></td><td>{total_ouvrage_remblai}</td></tr>
<tr><td><strong>Longueur totale des ouvrages (somme des deux directions)</strong></td><td>{total_length_remblai} m</td></tr>
</table>

<h3>2. Longueur des ouvrages de remblai (<code>length</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{length_max_remblai} m</td></tr>
<tr><td><strong>Minimum</strong></td><td>{length_min_remblai} m</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{length_mean_remblai} m</td></tr>
<tr><td><strong>Médiane</strong></td><td>{length_median_remblai} m</td></tr>
</table>

<h3>3. Hauteur moyenne (remblai) (<code>hauteur_moyenne</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{hauteur_moyenne_max_remblai} m</td></tr>
<tr><td><strong>Minimum</strong></td><td>{hauteur_moyenne_min_remblai} m</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{hauteur_moyenne_mean_remblai} m</td></tr>
<tr><td><strong>Médiane</strong></td><td>{hauteur_moyenne_median_remblai} m</td></tr>
</table>

<h3>4. Hauteur maximale (remblai) (<code>hauteur_max</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{hauteur_max_max_remblai} m</td></tr>
<tr><td><strong>Minimum</strong></td><td>{hauteur_max_min_remblai} m</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{hauteur_max_mean_remblai} m</td></tr>
<tr><td><strong>Médiane</strong></td><td>{hauteur_max_median_remblai} m</td></tr>
</table>

<h3>5. pente moyenne (remblai) (<code>pente_moyenne</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{pente_moyenne_max_remblai}</td></tr>
<tr><td><strong>Minimum</strong></td><td>{pente_moyenne_min_remblai}</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{pente_moyenne_mean_remblai}</td></tr>
<tr><td><strong>Médiane</strong></td><td>{pente_moyenne_median_remblai}</td></tr>
</table>

<h3>6. pente maximale (remblai) (<code>pente_max</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{pente_max_max_remblai}</td></tr>
<tr><td><strong>Minimum</strong></td><td>{pente_max_min_remblai}</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{pente_max_mean_remblai}</td></tr>
<tr><td><strong>Médiane</strong></td><td>{pente_max_median_remblai}</td></tr>
</table>

<h2>Ouvrage de type <strong>déblai</strong></h2>

<h3>1. Statistiques générales des ouvrages de déblai</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Nombre total des ouvrages (somme des deux directions)</strong></td><td>{total_ouvrage_deblai}</td></tr>
<tr><td><strong>Longueur totale des ouvrages (somme des deux directions)</strong></td><td>{total_length_deblai} m</td></tr>
</table>

<h3>2. Longueur des ouvrages de déblai (<code>length</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{length_max_deblai} m</td></tr>
<tr><td><strong>Minimum</strong></td><td>{length_min_deblai} m</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{length_mean_deblai} m</td></tr>
<tr><td><strong>Médiane</strong></td><td>{length_median_deblai} m</td></tr>
</table>

<h3>3. Hauteur moyenne (déblai) (<code>hauteur_moyenne</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{hauteur_moyenne_max_deblai} m</td></tr>
<tr><td><strong>Minimum</strong></td><td>{hauteur_moyenne_min_deblai} m</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{hauteur_moyenne_mean_deblai} m</td></tr>
<tr><td><strong>Médiane</strong></td><td>{hauteur_moyenne_median_deblai} m</td></tr>
</table>

<h3>4. Hauteur maximale (déblai) (<code>hauteur_max</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{hauteur_max_max_deblai} m</td></tr>
<tr><td><strong>Minimum</strong></td><td>{hauteur_max_min_deblai} m</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{hauteur_max_mean_deblai} m</td></tr>
<tr><td><strong>Médiane</strong></td><td>{hauteur_max_median_deblai} m</td></tr>
</table>

<h3>5. pente moyenne (déblai) (<code>pente_moyenne</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{pente_moyenne_max_deblai}</td></tr>
<tr><td><strong>Minimum</strong></td><td>{pente_moyenne_min_deblai}</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{pente_moyenne_mean_deblai}</td></tr>
<tr><td><strong>Médiane</strong></td><td>{pente_moyenne_median_deblai}</td></tr>
</table>

<h3>6. pente maximale (déblai) (<code>pente_max</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{pente_max_max_deblai}</td></tr>
<tr><td><strong>Minimum</strong></td><td>{pente_max_min_deblai}</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{pente_max_mean_deblai}</td></tr>
<tr><td><strong>Médiane</strong></td><td>{pente_max_median_deblai}</td></tr>
</table>

<h2>Profils de type <strong>rasant</strong></h2>

<h3>1. Statistiques générales des profils rasants</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Nombre total des ouvrages (somme des deux directions)</strong></td><td>{total_ouvrage_rasant}</td></tr>
<tr><td><strong>Longueur totale des ouvrages (somme des deux directions)</strong></td><td>{total_length_rasant} m</td></tr>
</table>

<h3>2. Longueur des ouvrages des profils rasants (<code>length</code>)</h3>
<table>
<tr><th>Statistique</th><th>Valeur</th></tr>
<tr><td><strong>Maximum</strong></td><td>{length_max_rasant} m</td></tr>
<tr><td><strong>Minimum</strong></td><td>{length_min_rasant} m</td></tr>
<tr><td><strong>Moyenne</strong></td><td>{length_mean_rasant} m</td></tr>
<tr><td><strong>Médiane</strong></td><td>{length_median_rasant} m</td></tr>
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
output_html = f"output_{route}/statistiques_ouvrages.html"
with open(output_html, "w", encoding="utf-8") as f:
    f.write(report_html)

# Open the HTML report in the default web browser
html_path = os.path.abspath(output_html)
webbrowser.open_new_tab(f"file:///{html_path}")

