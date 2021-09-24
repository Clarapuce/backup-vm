/*imbrication
select marque from vehicule v, personne p
where v.nump = p.num
and ville = "Paris"
and 2 = any
(select count(*) as nombre_vehicule
from vehicule
where nump is not null
group by nump)*/


/*Commande Exists
select nom, prenom
from personne p, vehicule v
where nump = num
and marque = 'Fiat'
And exists(select * from vehicule v2 where marque = 'Peugeot' and v.nump=v2.nump);*/


/*Personne ayant  la fois une fiat et une peugeot:
select p.nom, p.prenom
from personne p, (select nump from vehicule where marque='peugeot') as peugeot, 
(select nump from vehicule where marque ='fiat') as fiat
where peugeot.nump = fiat.nump
and peugeot.nump = p.num;*/

/*Marque de voiture etant  la fois  paris et  lyon
select v.marque from vehicule v, personne p, (select marque from vehicule, personne where nump = num
and ville = 'Paris') as paris
where v.nump = p.num
and p.ville = 'Lyon'
and v.marque = paris.marque;*/


/*Personne ayant  la fois une peugeot mais pas de fiat :
select p.nom, p.prenom  from personne p, vehicule v
where p.num = v.nump
and v.marque = 'peugeot'
and not exists (select nump from vehicule v2 where marque='fiat'and v.nump = v2.nump);*/

/*Personne qui ont le plus grand nombre de voiture 
select nom, prenom, nb.nb_voiture from personne p, (select nump, count(*) as nb_voiture from vehicule group by nump ) as nb
where p.num = nb.nump
and nb.nb_voiture in (select max(nb_voiture) from (select count(*) as nb_voiture from vehicule group by nump )as compte); */

/* avec utilisation des vues */
create or replace view compte_voiture as
select count(*) as nb_voiture, nump from vehicule group by nump;










