#! /bin/bash
# Script pour creer un repertoire et manipuler un fichier
mkdir -p monScript
wc -wl fic1.txt | cat > monScript/fic2.txt
sort fic1.txt
chmod 644 fic1.txt
