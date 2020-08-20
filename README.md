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

Python est nécessaire et la libraie PySerial

## Usage

Usage du module :

```
./  from teleinfo import Parser
  from teleinfo.hw_vendors import RpiDom
  ti = Parser(RpiDom())
  print ti.get_frame()
```

Le parseur supporte aussi l'itération :

```
  from teleinfo import Parser
  from teleinfo.hw_vendors import RpiDom
  for frame in Parser(RpiDom()):
      do_something_with(frame)
```

## Example







# License

<img alt="Creative Commons Attribution-NonCommercial 4.0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png">   

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/)    

# Misc

See news and other projects on my [blog][2] 

 
[2]: https://hallard.me

