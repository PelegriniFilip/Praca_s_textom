import tkinter #vytvorím si tkinter
from random import * #vytvorím možnosť vytvárať náhodu
canvas = tkinter.Canvas() #vytvorím si plátno
canvas.pack() #pri zapnutí programu sa plátno objaví na obrazovke

slovo1 = 'veľké' #do slovo1 sa vloží tex
slovo2 = 'tajomstvo' #do slovo2 sa vloži text
spojene = slovo1 + slovo2 #do spojenia sa vloží text zo slovo1 plus text zo slovo2
print(spojene) #do shellu sa vypíše spojenie

ake = choice(('veľké','malé','obrovské','drobné','smutné','veselé', 'sklamané', 'mŕtve', 'úbohé')) #do ake sa vloží náhodné slovo zoi zátvoriek
co = choice(('tajomstvo','prekvapenie','predsavzatie', 'prísaha', 'zrada', 'náhoda')) #do co sa vloží náhodné slovo zo zátvoriek
spojene = ake +' '+co #do spojenia sa vloží slovo s ake plus medzera a plus slovo s co
print(spojene) #do shellu sa vypíše spojenie

def nahodna_veta(): #vytvorím si funkciu s názvom nahodna_veta
    kto = choice(('Kamarát','Spolužiak','Andrej','Roman', 'Filip', 'Peter', 'JOU JOU')) #do kto sa vloží náhodné slovo zo zátvoriek
    corobil = choice(('videl','prezradil','povedal','napísal','zistil','nakreslil', 'poslal')) #do corobil sa vloží náhodné slovo zo zátvoriek
    ake = choice(('veľké','malé','obrovské','drobné','smutné','veselé', 'oklamané', 'zabité', 'obrátené na správnu cestu')) #do ake sa vloží náhodné slovo zo zátvoriek
    co = choice(('tajomstvo','prekvapenie','predsavzatie', 'krivá prísaha', 'králo kat', 'osud')) #do co sa vloží náhodné slovo zo zátvoriek
    spojene = kto +' '+corobil+' '+ake+' '+co+'.' #do spojenia sa vloží slovo s kto plus medzera a plus slovo s corobil plus medzera plus slovo s ake plus medzera plus slovo s co a  nakoniec sa pripokí bodka
    print(spojene) #do shelle sa vypíše spojenie
for i in range(1,21): #vytvorím opakovanie, všetko co je napísane pod týmto a je odsadené tabom tak sa zopakuje 20 krát
    nahodna_veta() #funkcia náhodná veta sa zavolá aby sa mohla vykonať