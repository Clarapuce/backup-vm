#! /bin/bash
if [ $# = 1 ]
then
	fichierExist()
	{
		if [[ ! -e $1 ]]
		then 
			exit 1
			echo $line
		fi
	}
	
	somme()
	{
		s=0
		while read line 
		do
			if [[ "$line"="^[0-9\+$]" ]]
			then
				echo "$line est un int"
				s=$(( $s + $line ))
			fi
			
		done < $1
		echo "somme = " $s
	}
	
	nbLigne()
	{
		l=0
		while read line 
		do
			l=$(( $l+1 ))
			
		done < $1
		echo "nombre de ligne : " $l
	}
	fichierExist $1
	somme $1
	nbLigne $1
	
		
	
else
	echo "Mauvais nombre d'arguments"
fi
