#! /bin/bash
touch fic1.txt fic2.txt fic3.txt
chmod 444 fic2.txt
chmod 600 fic3.txt
for I in fic1.txt fic2.txt fic3.txt
do
	echo "I= $I"
	ls -ld $I
done
exit 0 
