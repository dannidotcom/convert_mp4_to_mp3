
# Script de Conversion MP4 en MP3

## Description
Ce script Python parcourt un dossier contenant plusieurs fichiers `.mp4`, les convertit en fichiers `.mp3` . Il utilise la bibliothèque `pydub` 

## Prérequis
- Python installé (version 3.x recommandée)
- Bibliothèque `pydub`

### Installation des dépendances
Installez `pydub` en utilisant pip :
```bash
pip install pydub
```


## Fonctionnement
1. Le script parcourt tous les fichiers dans le dossier spécifié.
2. Il vérifie si chaque fichier a l'extension `.mp4`.
3. Il charge chaque fichier `.mp4` et l'exporte en tant que fichier `.mp3` en conservant le même nom.
4. Un message est affiché pour chaque fichier converti.

## Notes
- Assurez-vous que `ffmpeg` est correctement installé et configuré dans le `PATH` de votre système.
- Les fichiers de sortie `.mp3` seront stockés dans le même dossier que les fichiers `.mp4`.

## Exécution
Exécutez le script Python à partir de la ligne de commande :
```bash
python convert.py
```


## Références
- [Documentation de pydub](https://pydub.com/)
- [Téléchargement de ffmpeg](https://ffmpeg.org/download.html)