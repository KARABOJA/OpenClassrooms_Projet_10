FROM alpine:3.22

# Notre répertoire de travail sera la racine du système de fichier du conteneur
WORKDIR /·

# copie des fichiers nécessaires
COPY /scripts /scripts
COPY /requirements.txt /requirements/requirements.txt

# On met à jour les dépendances système afin de limiter les risques 
RUN apk update
RUN apk upgrade

# install build dependencies and needed tools
RUN apk add $(cat /requirements/requirements.txt)

# lancer les scripts de migrations (commande remplacée par 'command: sh -c "tail -f /dev/null"' dans docker-compose pour la gestion via Kestra)
CMD ["bash", "/scripts/scripts.sh"]