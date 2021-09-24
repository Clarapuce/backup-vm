#! /bin/bash
if [ $# -eq 1 ]
then
	if [ -e $1 ] ; then
		#Nature du fichier
		if [ -L $1 ] 
		then 
			echo -n $1 "est un lien symbolique. "
		elif [ -f $1 ] 
		then
			echo -n $1 "est un fichier. "
		elif [ -d $1 ] 
		then
			echo -n $1 "est un dossier. "
 		elif [ -c $1 ] 
		then
			echo -n $1 "est un caracter device. "
 		elif [ -b $1 ] 
		then
			echo -n $1 "est un block device. "
 		fi
	 	
	 	#Affichage des permissions	
		p="("
		if [ -r $1 ] ; then p="${p}r"
		else p="${p}-"
		fi
		if [ -w $1 ] ; then p="${p}w"
		else p="${p}-"
		fi
		if [ -x $1 ] ; then p="${p}x"
		else p="${p}-"
		fi
		echo $p")"
		
	else echo -n $1 "n'existe pas. "
	fi
	
else echo "Nombre d'arguments incorrects."
fi
