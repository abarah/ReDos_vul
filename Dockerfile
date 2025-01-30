# Utiliser une image officielle Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requis dans l'image
COPY requirements.txt requirements.txt
COPY README.md README.md
COPY app.py app.py

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Commande de lancement de l'application
CMD ["python", "app.py"]
