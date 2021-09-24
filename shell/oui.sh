#! /bin/bash
echo "Entrez O ou N : "
read reponse
echo $reponse
if [ $reponse = "O" ] || [ $reponse = "o" ]
then
	echo "OUI"
elif [ $reponse = "N" -o $reponse = "n" ]
then 
	echo "NON"
else
	echo "reponse incorrecte"
fi
exit 0
