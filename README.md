<a href="https://iguanodon.ai"><img src="img/iguanodon.ai.png" width="125" height="125" align="right" /></a>

# Scraping et mise en forme ALCESTE de données web

## Description

Ce repository contient le code créé dans le cadre d'une mission de récupération et de mise en forme d'un corpus web au format [ALCESTE [pdf]](http://www.image-zafar.com/images/formatage_alceste.pdf). 

## Étapes

Ce projet comporte deux grandes étapes : la récupération des données sur le site de presse (_web scraping_), et le formattage de ces données en format ALCESTE. 

### Récupérer les données

1. Installer l'extension Chrome [webscraper.io](https://webscraper.io)
2. Importer un `sitemap` : le fichier `sitemap.txt` décrit la structure des données à récupérer sur le site
3. Lancer le scraping et placer l'export du scraping en format `csv` dans `data/work`. Si `data/work` n'existe pas, le créer. L'export doit se nommer `scraped.csv`. Soit le renommer, soit changer la valeur de la variable `DATA` en ligne 5 de `main.py`

### Formatter les données

`main.py` fait appel à différentes fonctions dans `utils.py`. Le script ne prend pas d'arguments et lance le formattage. Une fois les données traitées, elles sont disponibles en format ALCESTE dans `data/final`. Les métadonnées récupérées sont les suivantes : 

- article, avec un identifiant unique. Eg: `article_e0ebb83e4b69327ee5acacebf1f49b88`
- date, en format YYYY/MM/JJ. Eg: `date_2019/09/09`
- date-mois, en format YYYY/MM. Eg: `date-mois_2019/09` 
- auteur, le média. Dans le cas où le nom de l'auteur.trice est mentionné, ce dernier a été remplacé.e par son média. Eg: `auteur_DW`
- pays, catégorie présente sur le site. Eg: `pays_Zimbabwe`
- catégorie, selon la classification sur le site. Eg: `catégorie_Features`
- URL, l'adresse web de l'article. Eg: `URL_http://www.infomigrants.net/en/post/19375/moscow-refugees-locals-dance-to-the-same-tune`



## Licence et contact

Ce code a été écrit par Simon Hengchen ([https://iguanodon.ai](https://iguanodon.ai)) à la commande de Dr Amandine Van Neste-Gottignies ([Université libre de Bruxelles](https://germe.centresphisoc.ulb.be/fr/user/1579)). Ce code est mis à disposition du public <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">sous licence permissive CC BY-SA 4.0</a>. 


 <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>
