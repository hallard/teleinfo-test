# teleinfo

Programme de test de la téléinfo pour les modules 

- [uTeleinfo](https://www.tindie.com/products/hallard/pitinfo/)
- [PITinfo](https://www.tindie.com/products/hallard/micro-teleinfo-v20/)
- Tout autre module compatible serie


## Installation

Python est nécessaire et la libraie Pythob Serial. 

Exemple sur Raspbery Pi

```
sudo apt-get install git-core python-serial
git clone https://github.com/hallard/teleinfo-test
cd teleinfo-test
```

Par defaut le programme essaie de trouver le port série correspondant à la téléinfo. Si c'est un module MicroTeleinfo il sera automatiquement detecté avec son numéro de série. 

Si le port `/dev/ttyAMA0` existe (Raspberry Pi) il sera aussi automatiquement utilisé.

## Usage

Aide

`./teleinfo.py -h` ou `./teleinfo.py --help`

```
./teleinfo.py -p|--port <serial_port>
./teleinfo.py -s|--standard
./teleinfo.py -l|--list
./teleinfo.py [-h|--help]
```

Affichage de la liste des ports séries dispobibles

`./teleinfo.py -l` ou `./teleinfo.py --list`

```
./teleinfo.py -l
/dev/cu.Bluetooth-Incoming-Port: n/a [n/a]
/dev/cu.usbserial-TINFO_1036: FT230X Basic UART - FT230X Basic UART [USB VID:PID=0403:6015 SER=TINFO-1036 LOCATION=20-1.4]
```

Lancement du module avec choix manuel du port

`./teleinfo.py -p /dev/ttyUSB0` ou `./teleinfo.py --port /dev/ttyUSB0`

```
/dev/cu.Bluetooth-Incoming-Port: n/a [n/a]
/dev/cu.usbserial-TINFO_1036: FT230X Basic UART - FT230X Basic UART [USB VID:PID=0403:6015 SER=TINFO-1036 LOCATION=20-1.4]
```

Lancement du module avec choix automatique du port (ici sur un Pi avec PITinfo)

`./teleinfo.py`


```
Missing serial port argument trying to find Teleinfo
Teleinfo : Mode Historique
Port     : /dev/ttyAMA0
Vitesse  : 1200

5
ADCO 021528603314 :
OPTARIF HC.. <
ISOUSC 15 <
HCHC 000723392  
HCHP 001742204 '
PTEC HP..  
IINST 001 X
IMAX 002 A
PAPP 00180 *
HHPHC A ,
MOTDETAT 000000 B
ADCO 021528603314 :
OPTARIF HC.. <
ISOUSC 15 <
HCHC 000723392  
HCHP 001742204 '
PTEC HP..  
IINST 001 X
```

Lancement du module avec choix automatique du port (ici sur un Mac avec un module MicroTeleinfo)
`./teleinfo.py`

```
Missing serial port argument trying to find Teleinfo
Teleinfo : Mode Historique
Port     : /dev/cu.usbserial-TINFO_1036
Vitesse  : 1200


MOTDETAT 000000 B
ADCO 021528603314 :
OPTARIF HC.. <
ISOUSC 15 <
HCHC 000723392  
HCHP 001742220 %
PTEC HP..  
IINST 001 X
IMAX 002 A
PAPP 00190 +
HHPHC A ,
MOTDETAT 000000 B
ADCO 021528603314 :
OPTARIF HC.. <
ISOUSC 15 <
HCHC 000723392  
HCHP 001742220 %
PTEC HP..  
IINST 001 X
IMAX 002 A
PAPP 00190 +
HHPHC A ,
MOTDETAT 000000 B
```

# License

<img alt="Creative Commons Attribution-NonCommercial 4.0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png">   

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/)    

# Misc

See news and other projects on my [blog][1] 

[A]: https://hallard.me

