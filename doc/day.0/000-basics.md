# The Basics

Základy jazyka Python vo forme jednoduchej hry "Uhádni číslo, ktoré si myslím."

## Goals

1. Nainštalovať a nastaviť si prostredie
2. Naučiť sa pracovať so štandardným vstupom a štandardným výstupom v jazyku *Python*
3. Spúšťanie skriptov

## TODO

* zahrnut aj `__name__`?
* nezabudnut ukazat ladenie a pouzitie debuggera

## Content

### Basic Input and Output

1. Vytvorte spustiteľný skript, v ktorom si "vygenerujete" tajné číslo a vypíšete na obrazovku text:

   `Myslím si číslo od 1 do 20`

   ```python
   #!/usr/bin/env python

   print("Myslim si cislo od 1 do 20")
   secret = 13
   ```

2. Načítajte tip od používateľa z príkazového riadku, pričom prompt umiestnite za výzvu v tvare:

   `Tvoj tip: _`

   ```python
   tip = input("Tvoj tip: ")
   ```

### Conditional Execution

1. Vyhodnoťte tip od používateľa jednou z nasledujúcich správ:

    - *Hmm... Moje cislo je mensie ako X* - ak `secret < tip`
    - *Hmm... Moje cislo je vacsie ako X* - ak `secret > tip`
    - *Ty si genius.* - ak `secret == tip`

   Pričom `X` reprezentuje hráčov tip.

   ```python
   tip = int(tip)

   if secret < tip:
       print("Hmm... Moje cislo je mensie ako ", tip)
   elif secret > tip:
       print("Hmm... Moje cislo je vacsie ako ", tip)
   else:
       print("Ta ty genius")
   ```


### Loops

1. Hrajte hru, až kým hráč tajné číslo neuhádne.

   ```python
   # !/usr/bin/env python
   print("Myslim si cislo od 1 do 20")
   secret = 13

   tip = input("Tvoj tip: ")
   tip = int(tip)

   while tip != secret:
       if secret < tip:
           print("Hmm... Moje cislo je mensie ako ", tip)
       elif secret > tip:
           print("Hmm... Moje cislo je vacsie ako ", tip)
       else:
           print("Ta ty genius")
   ```

2. Dajte hráčovi na uhádnutie 5 pokusov. Ak hru uhádne, pogratulujte mu. Ak neuhádne, vynadajte mu.

   ```python
   # !/usr/bin/env python
   print("Myslim si cislo od 1 do 20")
   secret = 13

   for counter in range(5, 0, -1):
       print('Zostava ti este', counter, 'pokusov.')
       tip = input("Tvoj tip: ")
       tip = int(tip)

       if secret < tip:
           print("Hmm... Moje cislo je mensie ako ", tip)
       elif secret > tip:
           print("Hmm... Moje cislo je vacsie ako ", tip)
       else:
           print("Ta ty genius")
           break
   else:
       print('Smola. Nepodarilo sa ti uhadnut tajne cislo', secret)
   ```

3. Keď hráč dohrá, opýtajte sa ho, či si nechce zahrať ešte raz. Ak áno, spustite hru od začiatku. Ak nie, poďakujte sa,
   zobrazte kredity a ukončite program.

   ```python
   #!/usr/bin/env python

   playing = True

   while playing:
       print("Myslim si cislo od 1 do 20")
       secret = 13

       for counter in range(5, 0, -1):
           print('Zostava ti este', counter, 'pokusov.')
           tip = input("Tvoj tip: ")
           tip = int(tip)

           if secret < tip:
               print("Hmm... Moje cislo je mensie ako ", tip)
           elif secret > tip:
               print("Hmm... Moje cislo je vacsie ako ", tip)
           else:
               print("Ta ty genius")
               break
       else:
           print('Smola. Nepodarilo sa ti uhadnut tajne cislo', secret)

       choice = input('Chces hrat znova? (a/n) ')
       if choice.upper() not in ('A', 'Y', 'ANO', 'YES'):
           playing = False

   print('Dakujem, ze si si zahrul tuto skvelu hru.\n'
         'Stav sa aj nabuduce')
   ```


### Functions

1. Vytvor funkciu `play_game()`, ktorá bude mať jeden parameter s názvom `secret`. Tento parameter bude reprezentovať
   tajné číslo, ktoré má byť uhádnuté.

   ```python
   # !/usr/bin/env python

   def play_game(secret):
       print("Myslim si cislo od 1 do 20")

       for counter in range(5, 0, -1):
           print('Zostava ti este', counter, 'pokusov.')
           tip = input("Tvoj tip: ")
           tip = int(tip)

           if secret < tip:
               print("Hmm... Moje cislo je mensie ako ", tip)
           elif secret > tip:
               print("Hmm... Moje cislo je vacsie ako ", tip)
           else:
               print("Ta ty genius")
               break
       else:
           print('Smola. Nepodarilo sa ti uhadnut tajne cislo', secret)

   playing = True

   while playing:
       play_game(13)

       choice = input('Chces hrat znova? (a/n) ')
       if choice.upper() not in ('A', 'Y', 'ANO', 'YES'):
           playing = False

   print('Dakujem, ze si si zahrul tuto skvelu hru.\n'
         'Stav sa aj nabuduce')
   ```

2. Z parametra `secret` spravte nepovinný parameter, ktorý ak nie je zadaný, bude nastavený na predvolenú hodnotu `13`.

   ```python
   def play_game(secret=13):
       ...

   # volanie je potom mozne bez povinného parametra
   play_game()
   ```


### Extending Basic Python

1. Zabezpečte, aby sa hra zakaždým spustila s náhodne vygenerovaným číslom z rozrahu *1* až *20*.

   ```python
    #!/usr/bin/env python

   import random


   def play_game(secret=13):
       print("Myslim si cislo od 1 do 20")

       for counter in range(5, 0, -1):
           print('Zostava ti este', counter, 'pokusov.')
           tip = input("Tvoj tip: ")
           tip = int(tip)

           if secret < tip:
               print("Hmm... Moje cislo je mensie ako ", tip)
           elif secret > tip:
               print("Hmm... Moje cislo je vacsie ako ", tip)
           else:
               print("Ta ty genius")
               break
       else:
           print('Smola. Nepodarilo sa ti uhadnut tajne cislo', secret)


   playing = True

   while playing:
       play_game(random.randint(1, 20))

       choice = input('Chces hrat znova? (a/n) ')
       if choice.upper() not in ('A', 'Y', 'ANO', 'YES'):
           playing = False

   print('Dakujem, ze si si zahrul tuto skvelu hru.\n'
         'Stav sa aj nabuduce')
   ```


## Additional Tasks

1. Ošetrite vzniknutú výnimku v prípade, ak hráč nezadal vstup ako celé číslo. Neumožnitu mu pokračovať v programe, kým
   nezadá správny vstup.
