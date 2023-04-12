<link rel="stylesheet" href="../style.css">

### Aksel

### CAUBEL

#### RT2 IOM

<h1 class=headerTemplate style="text-align:center;">Programmer</h1>

# Automatiser l'administration système avec des scripts

- Utilisation d'un script sh pour la mise en place automatique du firewall | Utilisation de debug dans mes services sur le VPC Carayon pour faire de la remonter d'erreur automatique.

- FireWall :  
Lors de la mise en situation d'une création de réseau d'entreprise (3I03), j'ai été amener à faire un FireWall NFTables. La configuration de NFTables étant volatile, il m'a fallu faire un script ```sh``` au démarrage Routeur Linux. Pour cela, il suffit de mettre en place le fichier contenant nos diverses règles. Une fois le fichier crée, je viens créer un lien symbolique dans mon dossier init.d pour qu'il s'exécute au démarrage de la machine.

- Mises à jour automatiques :  
Dans le cadre d'un dispositif IOT (ici des fenêtres connectés), j'ai étais dans la nécessiter de faire de la mise à jour ```Over The Air``` afin d'automatiser les mises à jours qu'importe la localisation de ma fenêtre.

Dans un premier temps j'ai mis en place le cahier des charges avec les contraintes.


# Développer une application à partir d'un cahier des charges donnée, pour le web ou les périphériques mobiles

- Mise en place du site VNA-systeme

Lors de mon apprentissage au sein de la menuiserie Carayon, il nous a été demandé avec PUIG Mathieu de réaliser un site WEB pour montrer divers informations.

Pour que vous compreniez notre cahier des charges, laissez moi vous expliquez en quelques lignes notre projet :

Nous avons un réseau LoRa comptenant des capteurs de CO2 / Température et Humidité qui nous permette en fonction des ces informations de faire ouvrir des fenêtres afin de crée une Ventillation Naturelle Autonome.

Notre cahier des charges concernant le site fût :

- Notre interface doit être accessible par un téléphone et par ordinateur.
- Nous devons avoir les informations clées qui nous apparaisse tout de suite.
- Un graphique doit également être mit pour visualiser l'historique des relever.
- Chaque organisation doit voir uniquement les relevers de ses batiments uniquement.
- les fenêtres doit être ouvrable / fermable debut l'interface.

Afin de répondre au mieu a cette problématique, aprs concertation avec M.PUIG nous avons choisis d'utiliser une base de template qui est simpliste et qui contient la partie "responsive" que nous ne savons pas faire dans le temps impartie. Nous avons également convenu des différents design que nous allons appliquer.

Dans la partie code le travail fût réellement répartie sur du 50/50 avec des tâches relativement équivalente en terme de dureté de programmation. Pour rappel, nous sommes dans une application développer avec le frame Work Django ( python3 ). Pour être celui qui était en charge de la partie page qui gère l'ouverture / fermeture des fenêtres j'ai fait le choix de ne faire que la fermeture. En effet, l'ouverture de fenêtre peut être un risque si nous compte se fait pirater. Aillant une infrastructure MQTT qui communique déjà avec mes différents capteur dont mes fenêtres j'ai du fait une interface permettant de déclacher une fonction d'envoi d'une trame MQTT aux fenêtres concernés ( fermeture par pièce ).

Pour répondre à une autre des demandes pour ne cité que c'est deux fonction,

# Utiliser un protocole réseau pour programmer une application client/serveur

Dans le cadre de la mise en place d'une application client/serveur j'ai pu utiliser différent protocole mais a des niveaux assez faible.

- Dans la mise en place d'application sur un serveur SSH est incontournable. Pour ma part lors de développement directement sur une machine je m'en sers avec l'outil Visual Studio Code qui me permet de faire un "remote SSH" me permettant d'utiliser toute la puissance de mon éditeur avec mes extensions et tous mon environnement de travail sur des postes qui ne sont pas le miens sans pour autant faire des installations différentes.  
  De manière plus SSH me permet dans les cas ou je dois juste faire de la manipulation de base de donnée en ligne de commande de m'y connecter et d'y faire mon travail.

- FTP / SFTP. Lorsque l'on travail sur des machines distantes comme j'ai pu le faire avec la mise en place d'un réseau IOT dans un poulailler, il a fallut fait des configurations pour programmer les différentes parties. Comme tous le monde le sais, stoquer les données en un seul point n'est pas un bonne idée et il est très important de faire des sauvegardes. A ces moment là, il est donc très utiles pour ne pas dire nécessaire d'avoir recours a ce protocole dans le but de faire des sauvegardes de notre travail sur d'autre espace que l'environnement de production qui de plus risque de subir des attaques.

# Installer, administrer un système de gestion de données

- Influx DB
- PostgreSQL
- script python pour influxDB

# Accéder à un ensemble de données depuis une application et / ou un site web

- graphique de VNA-Systeme
