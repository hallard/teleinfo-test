# teleinfo

Programme de test de la téléinfo pour les modules 

- [uTeleinfo](https://www.tindie.com/products/hallard/pitinfo/)
- [PITinfo](https://www.tindie.com/products/hallard/micro-teleinfo-v20/)
- Tout autre module compatible serie


<img src="https://cdn.tindiemedia.com/images/resize/ig_pbCZIjoLemqZR6qATQbuCH_s=/p/full-fit-in/1782x1336/i/5857/products/2018-06-08T13%3A23%3A25.397Z-MicroTeleinfo_Top_V2.png
" alt="Micro Teleinfo">

<img src="https://cdn.tindiemedia.com/images/resize/_NEi1vA81_oZqI7M_-sKng3BLoA=/p/full-fit-in/1782x1336/i/5857/products/2018-06-08T13%3A11%3A25.054Z-PITinfo.png
" alt="PITinfo">

## Installation

Python est nécessaire et la libraie PySerial. PAr defaut le programme essaie de trouver le port série correspondant à la téléinfo. Si c'est un module MicroTeleinfo il sera automatiquement detecté avec son numéro de série. 

Si le port `/dev/ttyAMA0` existe (Raspberry PI) il sera aussi automatiquement utilisé.

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


# License

<img alt="Creative Commons Attribution-NonCommercial 4.0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png">   

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/)    

# Misc

See news and other projects on my [blog][1] 

[A]: https://hallard.me

