




## Aksel PAULET
RT1 : B1

<br>

# <center> **SAE 12**</center>
## <center> *S’initier aux réseaux informatiques* </center>
---
<br><br><br>

# Sommaire :
- ## <a href="documentation-linux--windows">Documentation Linux &larr;&rarr; Windows</a>
- ## <a href="#installation-dune-machine-virtuel"> Installation de la machine virtuel</a>
-  ## <a href="#les-bases-pour-utiliser-vim-"> Documentation VIM</a>
  
<br><br><br>

# Documentation Linux &larr;&rarr; Windows

- Utilisation de la documentation :   

    Vous retrouverez en premier lieu la documentation Linux puis celle de Windows. Si vous connaissez une commande Windows vous aurez un lien clickable pour vous amener a la commande Linux et vice versa.  <br>
    Si la documentation suivante ne suffit pas, les commandes "helps" sont: man { commande } ( pour Linux ) et { commande } ? ( pour Windows ).

- ## <a href="#commande-linux-"> Allez directement à la documentation Linux</a>
- ## <a href="#commande-windows-"> Allez directement à la documentation Windows</a>


<br><br>

# Commande linux : 

## Attention !
- #### Si une commande vous résiste vous pouvez toujours   écrire devant votre commande " sudo " ce dernier vous permet de temporairement tous faire sur l'ordinateur si votre utilisateur a les droits administrateurs . Attention a ne pas utiliser l'utilisateur "Root", se dernier peut mettre des droits trop importants sur certain fichier si mal utilisé ainsi que lancer une application avec ce dernier peut représenter une faille de sécurité très importante.
  
  Certaines commandes nécessitent d'être installées. si jamais la commande " existe pas " faire : __apt install { nom de la commande }__ <strong>/!\ </strong> 

</br> </br>

- # ip { argument } : 

<br>

- ## ip link { argument } <a href="#netsh--argument----commande-linux-"> commande Windows</a> <br><br>

    - ## ip link show { nom du device } : <a href="#interface--ipv4--ipv6--show-interfaces--commande-linux-"> commande Windows</a> <br><br>

            Cette commande va pourvoir permettre d'afficher la carte réseau sélectionnée avec son état ainsi que diverses informations.

        - #### *Note :* <br>
        
            *Si toutefois l'on ne met pas le nom du service, on aura l'affichage de toutes les cartes réseaux avec leurs informations.*

        <img class="image" src=".\capture d'écran commande linux\ip_link_show.PNG" />

    - ## ip link set { argument } { nom du device } : <a href="#interface-set-interface--nom-de-linterface--option--commande-linux-"> commande Windows</a> <br><br>

      -  ## up : 
                Allume la carte réseau
        <img class="image" src=".\capture d'écran commande linux\ip_link_set_up.PNG" />

      -   ## down :
                Eteint la carte réseau
        <img class="image" src=".\capture d'écran commande linux\ip_link_set_down.PNG" />

<br><br>

  - ## ip address { argument } : 

    - #### *Note :* <br>
        
        *Si toute fois l'on ne met pas le nom du servise l'on aura l'affichage de toute les cartes réseaux avec leur informations.*


    - ##  add { ip/masque } dev { device } : <a href="#interface--ipv4--ipv6--set-address-name-interface--static--ip---masque-sur-4octets--passerelle--commande-linux-"> commande Windows</a>
            Ajoute l'adresse donnée.

        <img class="image" src=".\capture d'écran commande linux\ip_address_add.PNG" />

    - ## flush dev { device } : 
            Enlève toutes les addresses réseaux de la carte réseau. 

        <img class="image" src=".\capture d'écran commande linux\ip_address_flush.PNG" />
        
    - ## del { ip } dev { device } :
            supprime une adresse ip spécifique.

        <img class="image" src=".\capture d'écran commande linux\ip_address_del.PNG" />

    - ## show { device } : <a href="#all--commande-linux-"> commande Windows </a> <br><br>
            Permet de voir toute les informations d'une adresse. 

        <img class="image" src=".\capture d'écran commande linux\ip_address_show.PNG" />

<br><br>

- ## ip neigh { argument } : <a href="#arp--argument--commande-linux-"> commande Windows</a> <br><br>
    - ## *utilisation* :
            On utilise ip neigh pour manager / connaître la table ARP du poste sur lequel vous êtes.
            Plusieur stade de liaison possible, les principales :

            Stale : Connexion valide mais suspicieuse.

            Permanent : Connexion statique, se supprime uniquement manuellement.

            Reachable : Connexion valide mais périmable. 

            Delay : pas de connexion depuis les 30 dernières seconde.

            Probe : Une tentative de connexion a eu lieu, pas de réponse.

            Failed : Connexion impossible. 


  
  - ## get { ip } dev { device } : <a href="#-a--argument--ou--g--argument----commande-linux-"> commande Windows</a> <br><br>
            Permet de connaître le status de connection de l'ip. Permet également de savoir si elle se trouve dans la table.

      <img class="image" src=".\capture d'écran commande linux\ip_neigh_get.PNG" />    

  - ## add { ip } { addresse MAC} :
            Ajoute manuellement une addresse MAC liée à une addresse ip.
    

  - ## flush { ip } dev { device } : <a href="#-d--ip----commande-linux-"> commande Windows</a> <br><br>
            Efface les données liée a l'adresse ip de la table ARP. 
            Si aucune ip est entrée, supprime tout ce qui est relié au device.

     <img class="image" src=".\capture d'écran commande linux\ip_neigh_flush.PNG" /> 

<br>

- ##  ip route { argument } : <a href="#route--argument---commande-linux-"> commande Windows</a> <br><br><br>

-  ### *Note:*

         Lors de l'affectation d'une adresse ip avec son masque,
         une route faire le réseau est automatiquement crée pour pour le { device } d'affectation. 
         On peut toujours en rajouter une avec la commande suivante.

- ### *utilisation* : 
        On utilise cette commande pour pouvoir avoir une route vers notre réseau local ainsi que savoir qui est notre passerelle et ainsi avoir accès à Internet.


  - ## show : <a href="#print---commande-linux-"> commande Windows</a> <br><br>
        Cette argument permet de pouvoir voir toutes les routes definies ainsi que celles qui sont par défaut.

        Chaque route est reliée à une carte réseau.

    <img class="image" src=".\capture d'écran commande linux\ip_route_show.PNG" />     

  - ##  add { ip } : <a href="#-p---a-utilisé-à-lajout-dune-route-afin-de-la-rendre-persistante-au-redémarrage-système"> commande Windows</a> <br><br>
        Permet de rajouter une route vers un réseau.
            
    <img class="image" src=".\capture d'écran commande linux\ip_route_add.PNG" />        
            
  - ## add default via { ip } dev { device } : <a href="#add--adresse-réseau--mask--masque-sur-4octets---via-quelle-ip--metric--valeur-de-priorité---commande-linux-"> commande Windows</a> <br><br>
        Permet d'ajouter une route de sortie par defaut vers le routeur.

   <img class="image" src=".\capture d'écran commande linux\ip_route_add_default.PNG" />

  - ## flush { ip } dev { device }<a href="#delete--adresse-réseau--mask--masque-sur-4octets---via-quelle-ip--metric--valeur-de-priorité---commande-linux-"> commande Windows</a> <br><br>
        Cela permet de supprimer cette adresse ip des routes connues, si aucune ip est donnée : supprime tout ce qui est liée à la carte réseau.

   <img class="image" src=".\capture d'écran commande linux\ip_route_flush.PNG" />

<br><br>

- # Outils de teste de connection :


  - ## mii-tool { nom du device } : 

    
        Si câblé en E-thernet cette commande permet de chercher si le câble est bien branché de bout en bout.

     <img class="image" src=".\capture d'écran commande linux\mii-tool.PNG" />

  - ## ping { ip } OU { nom de domaine } : <a href="#ping--ip--ou--nom-de-domaine---commande-linux-"> commande Windows</a> <br><br>

        Permet de tester la connection a une machine. 
        
        Dans le cas d'une connexion filaire, on peut déduire;  
        Si un certain nombre de paquet est perdu que le câble Ethernet est défectueux.

        Dans le cas où on arrive à faire un ping vers une adresse ip mais pas vers un nom de domaine:
        Alors, on a un problème de DNS.

        Ping utilise le protocole echo-request ICMP

    <img class="image" src=".\capture d'écran commande linux\ping_ip.PNG" /> 
    <img class="image" src=".\capture d'écran commande linux\ping_domain.PNG" />

  - ## traceroute { ip } OU { nom de domaine } :<a href="#tracert--ip--ou--nom-de-domaine---commande-linux-"> commande Windows</a> <br><br>

        Permet de lister le nombre de saut à effectuer pour rejoindre une machine.
        Renvoie également les noms / ip des routeurs par lequel le paquet passe. 
        Traceroute est utilisé principalement via le protocol ICMP pour éviter des échecs liés à des firewalls
   <img class="image" src=".\capture d'écran commande linux\traceroute.PNG" /> <br>
   Dans cette capture d'écran, on remarque des étoiles sur les lignes précédentes la gateway, c'est dernier sont des erreurs. Probablement dû à un problème de translation d'adresse ( NAT ).


  - ## lshw :
        permet de lister les périphériques réseaux connectés à l'ordinateur

 <br> <br>

- # Fichier de configuration utile à connaître :

  - ## DNS : <a href="#dns---commande-linux-"> commande Windows</a> <br><br>

        Le serveur DNS permet de faire le lien entre les adresses ip et les noms symboliques.
        Ces derniers étant plus facile à retenir que les adresses ip. 
        Exemple : 8.8.8.8 = www.google.com

        On peut modifier les informations relatives aux serveurs DNS dans le fichier :
        /etc/network/interfaces

  - ## DHCLIENT : <a href="#dhclient---commande-linux-"> commande Windows</a> <br><br>
        Le DHCLIENT permet de faire un adressage dynamique, 
        attribuer automatiquement à la connexion l'adresse ip / la table de routage d'un ordinateur client. 
        On peut également faire un paramétrage ciblé par rapport aux adresses mac. 

        Pour faire intervenir le DHCLIENT il suffit de taper : dhclient 
        avec des droits super-utilisateurs.

        pour accèder au fichier de configuration :
        /etc/netplan/

        cette dernière peut avoir des noms variables mais il sera retrouvable avec une tabulation dans ce répertoire.

     <img class="image" src=".\capture d'écran commande linux\DHCLIENT.PNG" />

  - ## droit super-utilisateur :

        les droits super-utilisateur alias sudoers,
        Permettent d'exécuter des commandes qu'un simple utilisateur ne pourrait pas exécuter. 
        Notamment pour la modification des adresses.

        /etc/sudoers

     <img class="image" src=".\capture d'écran commande linux\sudoers.PNG" />

<br> <br> <br>

# Commande Windows : 

<strong>/!\ </strong> Lancez un cmd avec des droits administrateur ( clique droit )
Si jamais cette documentation ne suffit pas, on peut taper dans le cmd:
{ commande } ?

Afin d'éviter de casser mon ordinateur personnel il y aura uniquement des captures d'écran pour les commandes ne changeant pas les configurations. *( les VM Windows n'étant pas opérationnel sur le store.iutbéziers )*

Si la commande recherchée n'est pas ici, chercher du côté de netsh ( regroupant les commandes réseaux sous windows ).

<strong>/!\ </strong>

- # netsh { argument } : <a href="#ip-link--argument---commande-windows-"> commande Linux</a> <br><br>

  - ## interface { ipv4 / ipv6 } show interfaces :<a href="#ip-link-show--nom-du-device----commande-windows-"> commande Linux</a> <br><br>
        Permet de voir toute les interfaces réseaux / leur état / leur priorité et leur transport d'octect maximal ( MTU ).

    <img class="image" src=".\capture d'écran commande windows\netsh_show_interfaces.PNG" />

  - ## interface set interface { nom de l'interface } {option} :<a href="#ip-link-set--argument---nom-du-device----commande-windows-"> commande Linux</a> <br><br>
  
    - ## disable
        Eteint l'interface donnée <br>
    <img class="image" src=".\capture d'écran commande windows\netsh_interface_set_disable.PNG" />

    - ## enable 
        Allume l'interface donnée <br>
    <img class="image" src=".\capture d'écran commande windows\netsh_interface_set_enable.PNG" />
  - ## interface { ipv4 / ipv6 } set address name="{ interface }" static { ip } { masque sur 4octets } {passerelle} :<a href="#add--ipmasque--dev--device----commande-windows"> commande Linux</a> <br><br>
        Ajoute une adresse ipv4 / ipv6 a l'interface donnée

- # ipconfig { argument }:
  
  - ## sans argument
        Permet d'afficher les paramètres réseaux de votre ordinateur.
    <img class="image" src=".\capture d'écran commande windows\ipconfig.PNG" />

  - ## /all :<a href="#show--device----commande-windows--"> commande Linux</a> <br><br>
        Permet d'afficher tous les paramètres réseaux de votre ordinateur.
    <img class="image" src=".\capture d'écran commande windows\ipconfig.PNG" />
  - ## /renew 
        prend la dernière configuration dhclient connu 
    <img class="image" src=".\capture d'écran commande windows\ipconfig_renew.PNG" />
  - ## /flushdns
        Supprime le cache DNS
  
  - ## /release 
        renouvèle les ip de la carte réseau 

- # arp { argument }:<a href="#ip-neigh--argument----commande-windows-"> commande Linux</a> <br><br>
  
  - ## -s { ip } { mac [ délimiter = - ] }
        Ajoute une entrée statique dans la table d'arp.

  - ## -a { argument } OU -g { argument } : <a href="#get--ip--dev--device----commande-windows-"> commande Linux</a> <br><br>
  
    - ## pas d'argument
        Affiche le contenu de la table ARP <br>
    <img class="image" src=".\capture d'écran commande windows\arp-a.PNG" /> <br><br>
    - ## { adresse interface } -N { adresse recherchée } : <a href="#get--ip--dev--device----commande-windows-"> commande Linux</a> <br><br>
        Affiche l'adresse ip, la mac ainsi que le type d'adressage de l'adresse demandée.
    <img class="image" src=".\capture d'écran commande windows\arp-a-N.PNG" />
  - ## -d { ip } : <a href="#flush--ip--dev--device----commande-windows-"> commande Linux</a> <br><br>
        Supprime l'adresse ip ainsi que sa mac. 
        Si l'on remplace l'adresse ip par " * " alors toute la table arp est supprimée 

- # route { argument }: <a href="#ip-route--argument----commande-windows-"> commande Linux</a> <br><br>
  
  - ## Option possible :
    - ## -f  | Efface entièrement les tables de routage
    - ## -p  | A utilisé à l'ajout d'une route, afin de la rendre persistante au redémarrage système.
    - ## -4  | Force l'utilisation de la notation IPv4
    - ## -6  | Force l'utilisation de la notation IPv6
  
  - ## print : <a href="#show---commande-windows-"> commande Linux</a> <br><br>
        Affiche toutes les routes réseaux de l'ordinateur.
    <img class="image" src=".\capture d'écran commande windows\route_print.PNG" />

  - ##  ADD { adresse réseau } MASK { masque sur 4octets } { via quelle ip } METRIC { valeur de priorité } :<a href="#add--ip----commande-windows-"> commande Linux</a> <br><br>
        Ajoute une route réseau.

  - ##  DELETE { adresse réseau } MASK { masque sur 4octets } { via quelle ip } METRIC { valeur de priorité } :<a href="#flush--ip--dev--device--commande-windows-"> commande Linux</a> <br><br>
        Supprime une route réseau

- # Outils de teste de connection :
  - ## ping { ip } OU { nom de domaine } :<a href="#ping--ip--ou--nom-de-domaine----commande-windows-"> commande Linux</a> <br><br>

        Permet de tester la connection à une machine. 
        
        Dans le cas d'une connexion filaire l'on peut déduire;  
        Si un certain nombre de paquet est perdu que le câble Ethernet est défectueux.

        Dans le cas ou on arrive a faire un ping vers une adresse ip mais pas vers un nom de domaine:
        Alors on a un problème de DNS.

        Ping utilise le protocole echo-request ICMP
    <img class="image" src=".\capture d'écran commande windows\ping_ip.PNG" />
    <img class="image" src=".\capture d'écran commande windows\ping_domaine.PNG" />

  - ## tracert { ip } OU { nom de domaine } :<a href="#traceroute--ip--ou--nom-de-domaine---commande-windows-"> commande Linux</a> <br><br>
        Si on utilise une adresse ipv4 alors on récupèrera les informations routeur en ipv4. 
        Si l'on utilise un nom de domaine, on aura des adresses ipv6.

       Permet de lister le nombre de saut à effectuer pour rejoindre une machine.
        Renvoie également les noms / ip des routeurs par lequel le paquet passe. 
        tracert est utilisé principalement via le protocol ICMP pour éviter des échecs lié a des firewalls 
    <img class="image" src=".\capture d'écran commande windows\tracert_ip.PNG" />
    <img class="image" src=".\capture d'écran commande windows\tracert_domaine.PNG" /> <br>
    Sans savoir pouquoi à chaque lancement de la commande vers un nom de domaine, le deuxième saut a un délai trop long. Blocage du fournisseur d'accès internet (FAI) ? 


- # service extérieur :
  - ## DNS : <a href="#dns---commande-windows-"> commande Linux</a> <br><br>
    - Pour mettre un DNS :
      - netsh interface ipv4 set DNS name = { interface } static { ip } index = { ordre de priorité (1 = premier DNS etc...) } 
  
  - ## DHCLIENT : <a href="#dhclient---commande-windows-"> commande Linux</a> <br><br>
    - ### procédure de remise a jour dhclient :
        netsh interface { ipv4 / ipv6 } set address name="{ interface }" source=dhcp
</html>
 <br><br><br><br><br>

 # Installation d'une machine virtuel.

 ## Comme machine virtuelle, j'ai choisi sur le site store.iutbéziers une Ubuntu car cette dernière est celle qui correspond à mes besoins actuels. Ces derniers sont une machine rapidement bootable, une interface en ligne de commande pour faire des tests divers.

 - ### Pour se faire j'ai donc importé depuis Oracle Visual Box mon .ova :

<img src=".\capture d'écran VM\importation.PNG">

Il n'y a aucune option à changer.

- ### Une fois la VM importée, l'on peut directement la démarrer: 

<img src=".\capture d'écran VM\ubuntu boot.PNG">

- ### On teste la connectivité de la VM avec la commande ping :

<img src=".\capture d'écran VM\ping VM - google.PNG">
<img src=".\capture d'écran VM\ping VM - moi.PNG">

## Le tour est joué l'on peut utiliser notre machine virtuelle sans crainte !


<br><br><br><br><br>

# Les bases pour utiliser VIM :

## Il existe plusieurs modes. Pour naviguer entre eux il suffit d'appuyer sur des touches "actions" ou bien de rentrée des commandes directement. Pour quitter un mode, appuyer sur "escape" :


- ### Normal :
  - ### Ce dernier n'a pas de particularité, il permet une lecture simple.
  
- ### Visual ( activable en appuyant sur "v" ):
  - ### Mode permettant de faire des sélections multiples en bloc ou bien par ligne.

- ### Insertion ( activable en appuyant sur "i" ):
  - ### Mode permettant de modifier le texte

## Il y a également des commandes / touches spéciales :

- ### escape puis ":q!" permet de quitter immédiatement l'interpréteur.
- ### escape puis ":wq!" permet de forcer l'enregistrement et quitter l'interpréteur.
- ### escape puis ":w" permet d'enregistrer le fichier
- ### double "y" permet de copier l'élément sélectionné, si aucun élément est sélectionné : copie la ligne.
- ### double "p" permet de copier l'élément sélectionnée.
- ### double "z" permet de sauvegardé et forcer la sortie de l'interpréteur.
- ### double "d" permet d'effacer l'élément sélectionné, si aucun élément est sélectionné : supprime la ligne.
- ### escape puis "!{commande}" permet d'exécuter du bash depuis l'interpréteur.