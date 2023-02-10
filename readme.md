# Python 101

rozsah: 5 dní

Kurz pre všetkých, ktorí sa chcú naučiť základy programovania v jazyku Python. Počas kurzu účastníci postupne
vytvoria jednoduchú textovú adventúru, ktorá bude mať rozsah zhruba 500 až 700 riadkov kódu. Popri tom sa prakticky
zoznámia so všetkými základnými konštrukciami jazyka, ako aj s organizáciou projektu do modulov a balíkov.

Textová adventúra, ktorá sa vytvára počas kurzu, je remake-om klasickej textovky [Indiana Jones 2](https://www.zx-spectrum.cz/index.php?cat1=3&cat2=3&game_id=indyjones.txt) od [Františka Fuku](https://www.fuxoft.cz/) z roku 1987.

Kurz sa priamo nevenuje základom algoritmizácie, takže sa od účastníkov očakáva, že majú skúsenosť aspoň so základmi
programovaní alebo skriptovania v inom jazyku.


## Preberané témy

* štandardný vstup a výstup
* riadenie toku programu pomocou vetvenia a cyklov
* tvorba vlastných funkcií
* dátové triedy pomocou balíka [Pydantic](https://pydantic-docs.helpmanual.io)
* vyvolávanie a ošetrovanie výnimiek
* práca s textovými súbormi
* práca so základnými údajovými typmi a kolekciami
* moduly a balíky
* type hints
* defenzívne programovanie


## Literatúra

* [Začínáme programovat v jazyku Python](https://www.martinus.sk/?uItem=1455785) - Kurz programovania v jazyku Python od [Ruda Pecinovského](http://rudolf.pecinovsky.cz/). Zhodou okolností tiež robí textovku, aj keď iným spôsobom.
* [Python – Kompletní příručka jazyka pro verzi 3.10](https://www.martinus.sk/?uItem=1429819) - Kniha venovaná jazyku Python verzie 3.10.
* [Make Your Own Python Text Adventure: A Guide to Learning Programming](https://www.amazon.com/Make-Your-Python-Text-Adventure/dp/1484232305) - Zrejme učebnica programovania v jazyku Python, v ktorej autor
  tvorí taktiež textovú adventúru. Ale úplne ináč, ako to robíme my (o dosť horšie :-))
* [The lexicon of Interactive Fiction](https://ifonlytefl.wordpress.com/2011/11/24/the-lexicon-of-interactive-fiction/) - krátky návod o tom, ako hrať textové adventúry


## World Map

```
                                         +--+
                                         |  v
+------------+                      +--------------+
| v lietadle |                   +->|     púšť     |<-+
+------------+                   |  +--------------+  |
      |                          |         ^          |
      v                          |         v          |
+------------+                   |  +--------------+  |
| voľný pád  |                   +--|     oáza     |--+
+------------+                      +--------------+
                                           ^
                                           v
                                    +--------------+
                                    | pred táborom |
                                    +--------------+
                                           ^
                                           v
                +--------------+    +--------------+    +----------------+
                |  malý stan   |<-->|   v tábore   |<-->| veliteľov stan |
                +--------------+    +--------------+    +----------------+
                                                                                    +---------------+
                                                                                    |    vyklenok   |
                                                                                    +---------------+
                                                                                            ^
                                                                                            v
+---------------+    +---------------+    +---------------+    +---------------+    +---------------+
|   žltá hmla   |<-->| koniec chodby |    |   podzemie    |<-->|  uzka chodba  |<-->|     oltar     |
+---------------+    +---------------+    +---------------+    +---------------+    +---------------+
        ^                                        ^
        v                                        v
+---------------+    +---------------+    +--------------+    +-------------------+
|   žltá hmla   |<-->|   žltá hmla   |<-->|    chodba    |<-->| prázdna miestnosť |
+---------------+    +---------------+    +--------------+    +-------------------+
                                                                       ^
                                                                       v
                                                               +---------------+
                                                               |    komôrka    |
                                                               +---------------+
```
