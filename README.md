# 🌍 EcoRoute & Logistique

EcoRoute est une application web de calcul d'itinéraires intelligents. Elle permet non seulement de trouver le chemin le plus court entre deux points, mais aussi d'estimer les coûts en carburant et d'optimiser les tournées de livraison complexes via des algorithmes de graphes.

## 🚀 Fonctionnalités (MVP)
- **Carte Interactive :** Affichage d'un fond de carte OpenStreetMap via Folium.
- **Calcul d'Itinéraire :** Utilisation de l'algorithme de Dijkstra pour trouver le chemin le plus court.
- **Sélection Flexible :** Choix des points par clic sur la carte ou via une barre de recherche.
- **Tableau de Bord :** Affichage en temps réel de la distance, du temps estimé et du coût du carburant.

## 🛠 Tech Stack
- **Backend :** Python, Flask
- **Cartographie :** Folium, Leaflet.js
- **Analyse de Réseau :** OSMnx, NetworkX
- **Géocodage :** Geopy (Nominatim API)
- **Frontend :** HTML5, CSS3 (Bootstrap), JavaScript

## 📦 Installation
1. **Cloner le projet :**
   ```bash
   git clone [https://github.com/votre-repo/ecoroute.git](https://github.com/votre-repo/ecoroute.git)
   cd ecoroute

   ---

## 👥 Répartition des tâches (Phase MVP)

Pour que vous puissiez avancer en parallèle sans vous marcher sur les pieds, voici une séparation **Backend/Data** et **Frontend/Intégration**.

### **Personne A : Le "Data Architect" (Backend & Algorithmes)**
*Responsable de la logique de calcul et de la manipulation des données géographiques.*

1.  **Configuration OSMnx :** Mettre en place la fonction pour télécharger et mettre en cache le graphe de la zone (ex: une ville) sous forme de graphe NetworkX.
2.  **Moteur de calcul :** Créer une fonction qui prend deux coordonnées $(lat, lon)$ et retourne le plus court chemin (liste de nœuds) en utilisant Dijkstra.
3.  **Logique Carburant :** Créer la fonction de calcul des coûts ($Distance \times Conso \times Prix$).
4.  **API Flask :** Créer les routes `/calculate` qui reçoivent les points A et B en JSON et renvoient les données du trajet (distance, temps, liste de coordonnées).

### **Personne B : Le "UX Developer" (Frontend & Interface)**
*Responsable de ce que l'utilisateur voit et de l'interactivité de la carte.*

1.  **Structure Flask & UI :** Créer le template `index.html` avec Flask et intégrer Bootstrap pour une barre latérale propre (inputs pour l'essence, affichage des résultats).
2.  **Intégration Folium/Leaflet :** Générer la carte de base et surtout, ajouter le script JavaScript nécessaire pour capturer les clics sur la carte et envoyer les coordonnées au backend.
3.  **Module de Recherche :** Implémenter la barre de recherche textuelle en utilisant `Geopy` pour convertir l'adresse en coordonnées GPS.
4.  **Affichage du Tracé :** Récupérer les données envoyées par **Personne A** et dessiner la "Polyline" (le trait du trajet) dynamiquement sur la carte.

---

### Pourquoi cette répartition ?
* **Personne A** peut travailler dans des scripts Python purs et tester ses calculs dans un terminal ou un Notebook avant de les intégrer à Flask.
* **Personne B** peut prototyper l'interface avec des données "en dur" (mock data) avant de brancher le vrai algorithme.

**Souhaites-tu que je te prépare le squelette du fichier `app.py` pour lancer la collaboration ?**