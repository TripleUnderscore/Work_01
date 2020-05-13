Bonjour,

Je vous remercie tout d'abord pour m'avoir donné l'occasion d'écrire ces trois programmes.

Je me suis malheureusement heurté à quelques difficultés, ce qui fait que je n'ai pas pu aboutir au résultat que j'attendais : je me sus rendu-compte un peu tard que mon serveur s'interrompait dès lors que le client se fermait, ce qui, malheureusement, ne permet pas de conserver la sauvegarde du tableau de résultat (l'état de suivi_des_taches).

J'ai donc essayé de corriger le problème, sans succès à ce jour. En ce qui me concerne, je tâcherai de résoudre le problème dans les jours à venir. J'ai en effet plusieurs pistes pour cela :
  - utiliser la méthode SELECT afin d'autoriser le serveur à pouvoir considérer plusieurs clients en même temps.
  - utiliser un FORK de façon à ce qu'un fils du processus relatif au serveur se ferme : il y aura donc la conservation de l'état de la variable suivi_des_taches.
  
Malgré le fait que le client et le serveur ne communiquent pas de façon optimale, j'ai cependant obtenu les résultats espérés dès lors que je communiquais avec un interpréteur :
    - INTERPRETEUR <--> server.py : fonctionnement optimal.
    - INTERPRETEUR <--> client.py : fonctionnement optimal.

Pour finir, je pense aussi que certaines choses, comme par exemple la levée et le traitement des Exceptions, peuvent être optimisées.

Merci encore, et bonne lecture !
