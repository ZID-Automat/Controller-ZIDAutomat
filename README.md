# Controller-ZIDAutomat
The Controller for the actuall hardware

## Projekt 
Das Projekt ist in 4 teile Geteilt. Es besteht aus 3 Teilen, dem API Teil(der API Client, welche die Methoden bereitstellt um mit dem Backend zu kommunizieren), den DataCollection Teil(dort finden sich Funktionen, die Daten sammeln(Historie...)) und dem Borrow Teil(Das ist der Core des Controllers. Dort finden sich Funktionen zum ausgeben von Artikeln und QR Code Scannen...)

Der Vierte Teil ist der Main Teil, dieser verwaltet die anderen Teile.

![](Readme/Architectue.png)  

## Requrered Packages
pip install requests

pip install json