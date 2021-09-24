#! /bin/bash
#welcome, user

echo -n "Bonjour "
echo -n $USER
echo -n " bienvenue sur "
echo -n $HOSTNAME
echo -n " nous sommes le "
echo -n (date + %D)
echo " et il est : "
echo -n (date + %H)

exit 0
