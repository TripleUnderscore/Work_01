
Bonjour,

Je me suis heurté à quelques difficultés, et n'ai donc pas pu aboutir au résultat attendu : je me suis rendu-compte un peu tard que mon serveur s'interrompt dès lors que le client se ferme, ce qui ne permet pas de conserver la sauvegarde du tableau de résultat (l'état de suivi_des_taches).

J'ai essayé de corriger le problème, sans succès à ce jour. Je tâcherai cependant de le faire à titre personnel. J'ai en effet plusieurs pistes pour cela :
  - utiliser la méthode SELECT afin d'autoriser le serveur à pouvoir considérer plusieurs clients en même temps.
  - utiliser un FORK de façon à ce qu'un fils du processus relatif au serveur se ferme, et non pas le processus père lui-même: il y aura donc la conservation de l'état de la variable suivi_des_taches.
  
Malgré le fait que le client et le serveur ne communiquent pas de façon optimale, j'ai cependant obtenu les résultats espérés dès lors que j'utilisais un interpréteur :
  - INTERPRETEUR <--> server.py : fonctionnement optimal.
  - INTERPRETEUR <--> client.py : fonctionnement optimal.

Je pense aussi que certains aspects, tels que la levée et le traitement des Exceptions, peuvent être optimisés.

Pour finir, le binaire .so traite correctement les indices variant de 0 à 93 - au delà duquel le nomrbe de Fibonacci correspondant ne peut pas être représenté sur 64 bits - ; cependant, ces valeurs, quand elles dépassent 32 bits, ne sont plus traitées correctement lors de l'appel du binaire par le serveur (je corrigerai aussi ce problème par la suite).

Merci encore, et bonne lecture !

PS : chacun des script fonctionne avec Python 3 (3.6.9 sur ma machine) et Python 2 (2.7.17 sur ma machine).
