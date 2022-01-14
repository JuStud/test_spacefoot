# test_spacefoot
<p>Pour lancer il suffit d'effectuer la commande selon ta version de python, du genre : 'py spacefoot.py'.</p>

<p>Pour la base de données j'ai choisi de mettre des inputs pour que tu puisse l'adapter à tes besoins, en attendant que je trouves le moyen avec les variables d'environnement.</p>

<p>Il faut juste que la table qui contiendra les informations, se nomme : 'jobs'.</p>
<h5>Avec les colonnes :</h5>
<ul>
    <li>type</li>
    <li>titre</li>
    <li>team</li>
    <li>localisation</li>
    <li>date_publication</li>
    <li>contenu</li>
</ul>

<p>Si jamais je dépose quand même un export de la base que j'ai créer pour les tests</p>

CREATE TABLE `jobs` (
  `id` int(11) NOT NULL,
  `type` varchar(255) NOT NULL,
  `titre` varchar(255) NOT NULL,
  `team` varchar(255) NOT NULL,
  `localisation` varchar(255) NOT NULL,
  `date_publication` varchar(255) NOT NULL,
  `contenu` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `jobs`
  ADD PRIMARY KEY (`id`);
  
 ALTER TABLE `jobs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;
COMMIT;

<h5>Requirement avec pip</h5>
<ul>
    <li>pip install requests</li>
    <li>pip install beautifulsoup4</li>
    <li>pip install mysql-connector-python</li>
    <li>pip install python-csv</li>
</ul>
