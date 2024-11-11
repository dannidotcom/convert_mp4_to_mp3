import os
from pydub import AudioSegment

# Spécifiez le chemin du dossier contenant les fichiers vidéo
chemin_dossier = "/home/danni/Videos"

# Parcourir tous les fichiers du dossier
for fichier in os.listdir(chemin_dossier):
    # Vérifier si le fichier a l'extension .mp4
    if fichier.endswith(".mp4"):
        # Chemin complet du fichier vidéo
        chemin_fichier_mp4 = os.path.join(chemin_dossier, fichier)
        
        # Charger la vidéo
        audio = AudioSegment.from_file(chemin_fichier_mp4, format="mp4")
        
        # Obtenir le nom du fichier sans l'extension
        nom_fichier_sans_extension = os.path.splitext(fichier)[0]
        
        # Chemin complet du fichier audio de sortie
        chemin_fichier_mp3 = os.path.join(chemin_dossier, f"{nom_fichier_sans_extension}.mp3")
        
        # Exporter en MP3
        audio.export(chemin_fichier_mp3, format="mp3")
        
        print(f"Converti : {fichier} -> {nom_fichier_sans_extension}.mp3")

print("Conversion terminée !")
