#! /bin/bash
#Commandes  utiliser : ps

if [ $# = 1 ]
then
	if [[ ${1} = *.ps ]] 
		then gv $1 
		echo "visualisation du ps"
	elif [[ $1 = *.pdf ]]
		then evince $1 
		echo "visualisation du pdf"
	elif [[ $1 = *.txt ]]
		then echo "visualisation du txt"
		less -e $1
		echo "fin visualisation"
	elif [[ $1 = *.txt.gz ]] || [[ $1 = *.pdf.gz ]] || [[ $1 = *.ps.gz ]]
		then echo "visualisation de l'archive"
		gunzip -c $1
	else echo "Extension non-prise en charge"
	fi
else echo "Nombre d\'arguments en entree incorrect"
fi
