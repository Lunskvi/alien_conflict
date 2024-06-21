#rozšíření
from random import *
from time import sleep

#začátek hry
def main():
    while True:
        moznosti = input("Zadej start, konec nebo info: ")  
        if moznosti == "start":
            start_game()
        elif moznosti == "konec":
            print("Konec hry.")
            sleep(2)
            exit()
        elif moznosti == "info":
            info()
        else:
            print("Neplatná volba, zkuste to znovu.")

def info():
    print("     Ovládání:")
    sleep(2)
    print("         Spuštění:")
    sleep(2)
    print("             - Hra se spustí, když do konzole napíšete 'start'")
    sleep(2)
    print("         Volby a rozhodování:")
    sleep(2)
    print("             - Po každém scénáři vám budou nabídnuty různé volby")
    sleep(2)
    print("             - Každá volba je očíslována (např. 1, 2)")
    sleep(2)
    print("             - Pro volbu, kterou chcete učinit, zadejte odpovídající číslo a stiskněte Enter")
    sleep(2)
    print("         Navigace mezi sektory:")
    sleep(2)
    print("             - Po vyřešení situace v sektoru E12 se přesunete do sektoru E13")
    sleep(2)
    print("             - V sektoru E13 budete čelit dalším rozhodnutím, které vás mohou vést do různých scénářů")
    sleep(2)
    print("         Scénáře:")
    sleep(2)
    print("             - Po každém rozhodnutí se hra bude ubírat podle zvolené cesty, buď budete pokračovat v dalším sektoru, nebo řešit specifické úkoly a situace.")
    sleep(2)
    print("         Kontrola hry:")
    sleep(2)
    print("             - Pokud zvolíte neplatnou možnost, hra vás vyzve, abyste volbu opakovali")
    sleep(2)
    print("         Závěr hry:")
    sleep(2)
    print("             - Hra může končit různými scénáři v závislosti na vašich rozhodnutích")

def start_game():
    print("Vítej v Alien Conflict.")
    sleep(2)
    print("Píše se datum / 21.11. / rok 3047 / 5:47 / zemského času, kde vesmírná loď jménem Prometheus právě prolétá skrz neznámou oblast.")
    sleep(2)
    print("Cíl je najít nějaké známky života na zdejších planetách v galaxii B-42.")
    novy_den()

def novy_den():
    print("---------------")
    print("Probouzíš se nevyspalý a naštvaný v 6:15, protože tě probudily hlasité rány a vřískot z vedlejší místnosti.")
    sleep(2)
    print("Zde se nachází hlavní sklad na jídlo a na uniformy.")
    sleep(2)
    print("Převlékáš se do pracovní uniformy se jmenovkou Aron Voss.")

    print("---------------")
    print("1. Aron půjde zjistit co se děje.")
    sleep(2)
    print("2. Aron se vyrazí najíst.")
    print("---------------")
    
    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        omrkni_to()
    elif choice == "2":
        ser_nato()
    else:
        print("Neplatná volba, zkuste to znovu.")
        novy_den()

def omrkni_to():
    print("---------------")
    print("Vstoupil jsi do místnosti, ale po nikom ani stopa.")
    sleep(2)
    print("Procházíš místností a všimneš si, žeje  podstoleme baterka, která jerozdrcená na kousky..") 
    sleep(2)
    print("Najednou uslyšíš skřípání ve ventilaci a chceš se tam podívat.")
    sleep(2)
    print("Než to ale stihneš, tak tam dorazí hlídač co tě vyvede ven a řekne ti, že za 10 minut je porada a musí tam být všichni pracovníci ze sektoru 21.")
    
    print("---------------")
    print("1. Aron půjde na poradu.")
    sleep(2)
    print("2. Aron se vrátí zpět do kajuty.")
    print("---------------")
    
    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        porada()
    elif choice == "2":
        kajuta()
    else:
        print("Neplatná volba, zkuste to znovu.")
        omrkni_to()

def ser_nato():
    print("---------------")
    print("Šel jsi se najíst do jídelny a hned vedle zaslechneš konverzaci u stolu dvou kolegů. Baví se o hlídači, který zmizel a doteď ho nikdo nenašel.")
    sleep(2)
    print("Po chvíli se z rozhlasu dozvíš, že se zachvíli koná porada, a musí tam být všichni pracovníci ze sektoru 21.")
    
    print("---------------")
    print("1. Aron půjde rovnou čekat na poradu.")
    sleep(2)
    print("2. Aron se vrátí zpět do kajuty.")
    print("---------------")
    
    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        porada()
    elif choice == "2":
        kajuta()
    else:
        print("Neplatná volba, zkuste to znovu.")
        ser_nato()

def porada():
    print("---------------")
    print("Je 7:45 a čekáš s dalšími pěti pracovníky, než budete moct vstoupit do zasedací místnosti.")
    sleep(2)
    print("Čas ti utíká, a tak většinu zasedání jen mluvíte o údržbě lodi a denních prohlídkách.")
    sleep(2)
    print("Poté co na tebe přijde řada se rozhodneš, že řekneš o těch hlasitých ránách co jsi slyšel.")
    sleep(2)
    print("Také zdůrazníš, že ve skladu zmizely krabice se zásobami, a že hlídač co tam měl být zmizel také.")
    sleep(2)
    print("Po nějaké době si vyšel ven a pořád si lámeš hlavu, co se mohlo ve skladu odehrát.")

    print("---------------")
    print("1. Aron si půjde odpočninout.")
    sleep(2)
    print("2. Aron se půjde podívat do skladu, ze kterého byl předtím vyveden.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        odpocinek()
    elif choice == "2":
        vyveden_ze_skladu()
    else:
        print("Neplatná volba, zkuste to znovu.")
        porada()

def kajuta():
    print("---------------")
    print("Vrátil jsi se do své kajuty a přemýšlíš o tom, co se asi stalo ve skladu.")
    sleep(2)
    print("Pak tě napadne, že by jsi mohl do skladu po poradě, až tam nikdo nebude.")
    sleep(2)
    print("Víš, že co se ve skladu odehrálo nebylo provedeno člověkem, protože na zemi byla rozdrcená baterka.")
    sleep(2)
    print("Už je 7:40, tak vyrážíš na poradu.")
    sleep(2)
    print("Na cestě potkáš Jakea Trenta, což je tvůj kamarád ze sektoru E7.")
    sleep(2)
    print("Zeptáš se ho, jestli něco neví o této nehodě, ale řekne ti jen to, že se na lodi mluví o nějáké jiné známce života.")
    porada()

def odpocinek():
    print("---------------")
    print("Přišel jsi do své kajuty a vysprchoval jsi se.")
    sleep(2)
    print("Lehl jsi si do postele a usnul.")
    sleep(2)
    print("Ráno jsi vstal a vzal si snídani v jídelně.")
    sleep(2)
    print("Poté si chtěl jít pracovat do tvého sektoru, ale všiml jsi si, že ve skladu nikdo není.")
    sleep(2)
    print("Tak si rychle zareagoval a vešel potichu dovnitř, aby tě nikdo neviděl.")
    vyveden_ze_skladu()

def vyveden_ze_skladu():
    print("---------------")
    print("Vstoupíš do skladu a všude blikají světla.")
    sleep(2)
    print("Vidíš dlouhé stíny, ale jsou to jen regály se zásobami.")
    sleep(2)
    print("Zase zaslechneš zvuky a vydáš se do vedlejší místnosti k šachtě odkud vychází.")
    sleep(2)
    print("Přiblížíš se k šachtě a začneš jí zkoumat.")
    sleep(2)
    print("Pak si všimneš, že je šachta pootevřená a nakloníš se blíž, aby si lépe viděl dovnitř.")
    sleep(2)
    print("Vidíš, že se v šachtě něco pohne a ucítíš na břiše ohromnou bolest.")
    print("Mimozemšťan tě odkopne a vyleze ze šachty.")
    sleep(2)
    print("Vstaneš a vzpamatuješ se, co se vlastně stalo.")
    sleep(2)
    print("Víš, že se musíš bránit, aby jsi přežil, ale na druhou stranu máš šanci na útěk.")   

    print("---------------")
    print("1. Aron se rozhodne postavit Mimozemšťanovi a bojovat.")
    sleep(2)
    print("2. Aron se rozhodne utéct k výtahu a pokusit se uniknout")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        boj_s_xenobitem()
    elif choice == "2":
        utek()
    else:
        print("Neplatná volba, zkuste to znovu.")
        odpocinek()

def boj_s_xenobitem():
    print("---------------")
    print("Aron se postaví mimozemšťanovi, jeho jediná zbraň je baterka, ale je připraven na boj.")
    sleep(2)
    print("Mimozemšťan je rychlý a silný, má neuvěřitelnou odolnost a schopnost regenerace.")
    sleep(2)
    print("Po několika minutách boje si Aron uvědomí, že monstrum, proti kterému stojí je příliš silný.")
    sleep(2)
    print("Mimozemšťan zaútočí na Arona ocasem.")
    prvni_smrt_jedna()
    end_game()

def utek():
    print("---------------")
    print("Rozhodneš se utéct a běžíš k výtahu.")
    sleep(2)
    print("Slyšíš, jak monstrum běží za tebou.")
    sleep(2)
    print("Jeho kroky jsou rychlé a děsivé.")
    sleep(2)
    print("Přiběhneš k výtahu a rychle stiskneš tlačítko pro sektor E3.")
    sleep(2)
    print("Dveře se pomalu zavírají a monstrum se blíží.")
    sleep(2)
    print("V poslední chvíli dveře výtahu zaklapnou.")
    sleep(2)
    print("Výtah se rozjíždí.")
    sleep(2)
    print("Rozdýcháváš se a uvědomuješ si, že jsi měl štěstí.")
    druha_cast()
    
def druha_cast():
    print("---------------")
    print("Přemýšlíš, jak si vlastně utekl a mezi tím dojedeš do sektoru E3.")
    sleep(2)
    print("E3 je chladné a tiché místo, osvětlené pouze tlumeným nouzovým osvětlením.")
    sleep(2)
    print("Kolegové ti dříve naznačovali, že tento sektor je opuštěný už dlouho.")
    sleep(2)
    print("Otevřeli se dveře výtahu a ucítíš chlad na tváři.")
    sleep(2)
    print("Po dlouhé době procházení prázdnými chodbami a místnostmi narazíš na zabezpečovací místnost.")

    print("---------------")
    print("1. Aron se pokusí zkontrolovat počítač a záznamy.")
    sleep(2)
    print("2. Aron půjde dál a pokusí se najít další sektor.")
    print("---------------")
    
    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        kamera_zanzam()
    elif choice == "2":
        sektor_E6()
    else:
        print("Neplatná volba, zkuste to znovu.")
        druha_cast()

def kamera_zanzam():
    print("---------------")
    print("Otevřeš dveře a uvnitř objevíš starý monitor a řadu kamerových záznamů.")
    sleep(2)
    print("Začneš procházet záznamy a s hrůzou sleduješ, jak v sektoru E7 to stvoření brutálně likviduje tvoje kolegy a obyvatelé lodi.")
    sleep(2)
    print("Zkontroluješ na stole papíry a záznamy z laboratoře ze sektoru E7.")
    sleep(2)
    print("Zjistíš, že to stvoření má název Xenobitus.")
    sleep(2)
    print("Xenobitus utekl včera z laboratoře a nikdo o tom ani neví...")
    sleep(2)
    print("Proto se rozhodneš rychle přesunout do sektoru E7.")
    sektor_E6()
    
def sektor_E6():
    print("---------------")
    print("Vstoupil jsi do sektoru E6, ale nefunguje proud a vše je zničené.")
    sleep(2)
    print("Dveře od sektoru E7 jsou vyhozené a nezbývá ti nic jiného, než najít jinou cestu.")
    sleep(2)
    print("Rozhodneš se najít místnost s údržbou, aby jsi mohl jít skrze šachtu.")
    sleep(2)
    print("Procházíš další prázdné chodby a místnosti, mezitím slyšíš vzdálené kroky a zvuky, které naznačují, že Xenobitus je někde poblíž.")
    sleep(2)
    print("Musíš být opatrný a rychlý, protože nebezpečí číhá všude kolem.")
    sleep(2)
    print("Po dlouhém hledání konečně najdeš místnost s ventilační údržbou.")
    sleep(2)
    print("Přístup do šachet je otevřený, ale šachty jsou úzké a temné.")
    sleep(2)
    print("Vezmeš si nářadí a vydáváš se do šachet.")
    sleep(2)
    print("Pohybuješ se opatrně, aby jsi neupoutal pozornost Xenobita, který stále prochází sektorem E7.")
    sleep(2)
    print("Šachty jsou plné prachu a občas narazíš na překážky, které musíš odstranit.")
    sleep(2)
    print("Monstrum je blízko, slyšíš dupání a řev mimozemšťana.")
    print("Musíš se rozhodnout, zda zůstaneš potichu a počkáš, až Xenobitus odejde, nebo se pokusíš proběhnout kolem něj.")
    
    print("---------------")
    print("1. Aron počká, až Xenobitus odejde.")
    sleep(2)
    print("2. Aron proběhne kolem monstra a bude doufat, že uteče do sektoru E7.")
    print("---------------")
    
    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        pockat_naodchod()
    elif choice == "2":
        druha_smrt()
    else:
        print("Neplatná volba, zkuste to znovu.")
        sektor_E6()


def pockat_naodchod():
    print("---------------")
    print("Po nějaké době jsi se nakonec rozhodl, že je čas se dostat k šachtě vedoucí do sektoru E7.")
    sleep(2)
    print("Otevřeš poklop ventilace a vlezeš do sektoru E7, který je stejně opuštěný a temný jako sektor E3.")
    sleep(2)
    print("Uvědomíš si, že monstrum zabilo skoro celou posátku a už jsou na palubě jen roboti.")
    sleep(2)
    print("I tak cítíš úlevu, že jsi utekl a přežil.")
    sleep(2)
    print("Nevíš co máš dělat, ale jedna možnost je únikový modul a druhá porazit Xenobita.")
    treti_cast()

def druha_smrt():
    print("---------------")
    print("Aron utíká ze všech svých sil kolem monstra, ale mimozemšťan je rychlejší a pohyblivější.")
    sleep(2)
    print("Už je skoro u sektoru E7, ale zakopne o staré krabice a monstrum ho ihned dožene.")
    sleep(2)
    print("Aron se snaží bránit, ale je pozdě.")
    sleep(2)
    print("Monstrum do něj zarazí nohu a poté ho vyzdvihne nahoru.")
    druha_smrt_dva()
    end_game()

def treti_cast():
    print("---------------")
    print("Rychle běžíš do sektoru E1, kde je řídící středisko, ale nikoho nenacházíš.")
    sleep(2)
    print("Najednou k tobě příjde droid a začne se ptát co chceš.")
    sleep(2)
    print("Celá loď problikává, protože Xenobitus vyřadil elektriku a motory.")
    sleep(2)
    print("Droida odstrčíš, ale začne se bránit a chytne tě za ruku.")
    sleep(2)
    print("Dojde ti, že je asi porouchaný a musíš ho vypnout.")
    sleep(2)
    print("Droida po trápení a boji nakonec vypneš na zadním panelu.")
    sleep(2)
    print("Teď se rozhoduješ, jestli Xenobita zlikvidovat nebo se vydat k modulům.")
    sleep(2)
    print("Problém je, že moduly jsou až v sektoru E13 a cesta bude dlouhá a riskantní přes celou loď.")
    sleep(2)
    print("Zabít Xenobita také bude hodně obtížné, už jsi málem umřel několikrát.")

    print("---------------")
    print("1. Aron zvolí zlikvidování Xenobita.")
    sleep(2)
    print("2. Aron se rozhodne pro cestu k modulům.")
    print("---------------")
    
    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        likvidace()
    elif choice == "2":
        moduly()
    else:
        print("Neplatná volba, zkuste to znovu.")
        treti_cast()

def likvidace():
    print("---------------")
    print("Rozhodl jsi se pro zničení Xenobita.")
    sleep(2)
    print("Musíš to monstrum najít a nastavit past.")
    sleep(2)
    print("Vracíš se rychle do sektoru E3, aby jsi zjistil na kamerovém záznamu, kde je to monstrum.")
    sleep(2)
    print("Na kameře vidíš mrtvé spolupracovníky a nad sebou slyšíš kroky v šachtě.")
    sleep(2)
    print("Došlo ti, že Xenobitus je nad tebou a že by jsi měl rychle zmizet.")
    sleep(2)
    print("Utíkáš do sektoru E7, kde se schováš na svém pokoji a promýšlíš plán.")
    sleep(2)
    print("Máš na výběr mezi pastí v šachtě nebo ve skladu.")

    print("---------------")
    print("1. Aron si zvolí past ve ventilaci.")
    sleep(2)
    print("2. Aron se rozhodne udělat past ve skladu.")
    print("---------------")
    
    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        past_ventilace()
    elif choice == "2":
        past_sklad()
    else:
        print("Neplatná volba, zkuste to znovu.")
        likvidace()

def past_ventilace():
    print("---------------")
    print("Vyrážíš do skladu, aby jsi nastražil výbušnou past do ventilace, která ve správný moment zlikviduje mimozemšťana.")
    sleep(2)
    print("Vytáhl jsi žebřík a lezeš do šachty na stropě.")
    sleep(2)
    print("Ve ventilaci jsi přilepil výbušninu a vlzel jsi dovnitř.")
    sleep(2)
    print("Xenobit je blízko, slyšíš kroky a dupání.")
    sleep(2)
    print("Napadne tě, že když vystřelíš elektrickou pistolí co jsi sebral ve velitelské místnosti, tak nalákáš monstrum k sobě.")
    sleep(2)
    print("Ujistíš se, že jsi dostatečně daleko od šachty a máš pod sebou další poklop na útěk.")
    sleep(2)
    print("Začneš dupat a dělat rámus, poté vystřelíš z pistole a slyšíš zvuky mimozemce, které se blíží k tobě.")
    sleep(2)
    print("Je to těsné, protože Xenobit je rychlejší než ty a lekneš se když vystřelí velkou rychlostí v šachtě k tobě.")
    sleep(2)
    print("Rychle jsi vylezl šachtou nahoru a zmáčkl tlačítko na spínači a celá šachta se zřítila.")
    sleep(2)
    print("Mimozemšťan začal řvát a byl zavalen šachtou a železem.")
    sleep(2)
    print("Teď ho musíš jít zabít pistolí, protože tohle je tvoje jediná šance.")
    sleep(2)
    print("Vyběhneš za ním, ale nevšimneš si, že otřesy shodili regály a krabice.")
    
    print("---------------")
    print("1. Aron se rozhodne běžet v levo, kde je spadlý regál.")
    sleep(2)
    print("2. Aron se rozhodne běžet v pravo, kde je rozbitý stůl.")
    print("---------------")
    
    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        treti_smrt()
    elif choice == "2":
        konec_hry_past_ventilace()
    else:
        print("Neplatná volba, zkuste to znovu.")
        past_ventilace()

def  konec_hry_past_ventilace():
    print("---------------")
    print("Běžíš v pravo a podlezeš stůl.")
    sleep(2)
    print("Už jsi u Xenobita a na tuhle možnost jsi čekal celou dobu.")
    sleep(2)
    print("Vytáhneš zbraň a vystřelíš několik střel, dokud Xenobita neusmažíš k smrti.")
    sleep(2)
    print("Mimozemšťan hodně vydrží, ale nakonec se ti povede vyhrát tento veliký boj.")
    sleep(2)
    print("Vracíš se zpátky do řídící místnosti a startuješ motory.")
    sleep(2)
    print("Už jsi skoro u některých z planet a brzy se vydáš na průzkum, i když sám.")
    sleep(2)
    print("Kdo ví, co tě ještě čeká, důležité je, že jsi přežil.")
    end_game()

def past_sklad():
    print("---------------")
    print("Vyrážíš do skladu, aby jsi nastražil regál, který ve správný moment spadne na mimozemšťana.")
    sleep(2)
    print("Regál je velice težký, ale použiješ moderní technologii k jeho přesunu ke dveřím.")
    sleep(2)
    print("Musíš se také vyzbrojit, proto zajdeš do velitelské místnosti poblíž a vezmeš si elektrickou pistoli.")
    sleep(2)
    print("Najednou slyšíš hlasité zvuky Xenobita a víš, že nemáš moc času.")
    sleep(2)
    print("Nic jiného než past a boj ti nezbívá, protože na útěk modulem je pozdě.")
    sleep(2)
    print("Vysoký regál je nastražený a až mimozemšťan vejde dovnitř, tak to celé spadne.")
    sleep(2)
    print("Vyběhneš ho nalákat zvuky výstřelů a rychle utíkáš zpátky, protože je všude rychle.")
    sleep(2)
    print("Schováš se za regál a Xenobit vejde dosvnitř.")
    sleep(2)
    print("Zakopne o drát, který si nastražil a spadne na něj regál.")
    sleep(2)
    print("Teď ho musíš jít zabít pistolí, protože tohle je tvoje jediná šance.")
    sleep(2)
    print("Vyběhneš za ním, ale nevšimneš si, že otřesy shodili i další regály.")

    print("---------------")
    print("1. Aron se rozhodne běžet v levo, kde je spadlý regál.")
    sleep(2)
    print("2. Aron se rozhodne běžet v pravo, kde jsou staré krabice.")
    print("---------------")
    
    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        treti_smrt()
    elif choice == "2":
        konec_hry_past()
    else:
        print("Neplatná volba, zkuste to znovu.")
        past_sklad()

def treti_smrt():
    print("---------------")
    print("Aron běží k regálu, ale na zemi jsou ostré střepy, po kterých uklouzne.")
    sleep(2)
    print("Xenobitus se mezitím zvedne a začne utíkat proti Aronovi.")
    sleep(2)
    print("Zvedne Arona ze země a blíží se k regálu se stavebním materiálem.")
    treti_smrt_tri()
    end_game()

def konec_hry_past():
    print("---------------")
    print("Běžíš v pravo a přeskočíš krabice.")
    sleep(2)
    print("Už jsi u Xenobita a na tuhle možnost jsi čekal celou dobu.")
    sleep(2)
    print("Vytáhneš zbraň a vystřelíš několik střel, dokud Xenobita neusmažíš k smrti.")
    sleep(2)
    print("Mimozemšťan hodně vydrží, ale nakonec se ti povede vyhrát tento veliký boj.")
    sleep(2)
    print("Vracíš se zpátky do řídící místnosti a startuješ motory.")
    sleep(2)
    print("Už jsi skoro u některých z planet a brzy se vydáš na průzkum, i když sám.")
    sleep(2)
    print("Kdo ví, co tě ještě čeká, důležité je, že jsi přežil.")
    end_game()

def moduly():
    print("Rozhodl jsi se pro cestu k modulům.")
    sleep(2)
    print("Musíš se dostat do sektoru E13, což je značně vzdálené a nebezpečné.")
    sleep(2)
    print("Předtím ale musíš projít sektory E10, E11, a E12, kde se mohou nacházet další nebezpečí.")
    sleep(2)
    print("Vydáváš se na cestu, doufaje, že unikneš hrozbám, které zanechal Xenobitus.")
    sleep(2)
    print("Cestou procházíš sektorem E10, kde slyšíš podivné zvuky, jako by někdo (nebo něco) škrábal/o stěny.")
    sleep(2)
    print("Zastavíš se, aby sis rozmyslel, co dál.")
    sleep(2)
    print("Zvuky se blíží a musíš rychle jednat.")
    
    
    print("---------------")
    print("1. Aron se rozhodne prozkoumat zvuky a zjistit, co je jejich zdrojem.")
    sleep(2)
    print("2. Aron se rozhodne pokračovat dál, ignorujíc zvuky.")
    print("---------------")
    
    choice = input("Zadejte číslo vaší volby: ")
    
    if choice == "1":
        prozkoumat_zvuky()
    elif choice == "2":
        pokracovat_dal()
    else:
        print("Neplatná volba, zkuste to znovu.")
        moduly()
        
def prozkoumat_zvuky():
    print("Aron se rozhodne prozkoumat zdroj zvuků.")
    sleep(2)
    print("Pomalu a opatrně se blížíš k místu, odkud zvuky vycházejí.")
    sleep(2)
    print("Když dorazíš ke zdroji zvuků, zjistíš, že to jsou jen uvolněné plechy, které se třesou v průvanu.")
    sleep(2)
    print("Uklidníš se a pokračuješ dál směrem k sektoru E11.")
    sektor_E11()

def pokracovat_dal():
    print("Ignoruješ zvuky a pokračuješ dál.")
    sleep(2)
    print("Cesta je dlouhá a napětí stoupá.")
    sleep(2)
    print("Konečně dorazíš do sektoru E11, ale uvědomíš si, že tu je problém.")
    sektor_E11()

def sektor_E11():
    print("Sektor E11 je temný a plný trosek a suti.")
    sleep(2)
    print("Musíš najít cestu skrz trosky a suť, abys mohl pokračovat do sektoru E12.")
    sleep(2)
    print("Náhle uslyšíš vzdálené kroky, které se rychle blíží.")
    sleep(2)
    print("Musíš se rozhodnout zda se schováš nebo se pokusíš utéct.")
    
    print("---------------")
    print("1. Aron se rozhodne schovat mezi troskami a sutí.")
    sleep(2)
    print("2. Aron se pokusí o útěk.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        schovat_se()
    elif choice == "2":
        utek_v_sektoru()
    else:
        print("Neplatná volba, zkuste to znovu.")
        sektor_E11()
    
def schovat_se():
    print("Aron se rychle schová mezi troskami.")
    sleep(2)
    print("Skrčený a téměř bez dechu čeká, až kroky pominou.")
    sleep(2)
    print("Po chvíli kroky utichnou a ty se rozhodneš pokračovat dál.")
    sektor_E12()
    
def utek_v_sektoru():
    print("Aron se rozhodne utéct a běží co nejrychleji dokáže.")
    sleep(2)
    print("Kroky za ním zesílí a cítí, že ho něco pronásleduje.")
    sleep(2)
    print("Nakonec se mu podaří uniknout a dorazí do sektoru E12.")
    sektor_E12()

def sektor_E12():
    print("Sektor E12 je ještě nebezpečnější než předchozí sektory.")
    sleep(2)
    print("Prostor je plný toxických plynů, tak musíš ihned najít ochranný oblek, abys mohl pokračovat.") 
    sleep(2)
    print("Prohledáváš okolí a nacházíš starou skříňku označenou jako 'Ochranné vybavení'.")
    sleep(2)
    print("Nacházíš ochranný oblek, a rychle si ho oblékáš, aby ses ochránil před toxickými plyny.")
    sleep(2)
    print("Cítíš se o něco bezpečněji, ale víš, že tady čas nehraje ve tvůj prospěch.")
    sleep(2)
    print("Pokračuješ dál chodbou, kde vidíš značky směřující k místnosti s náhradními filtry pro čistění vzduchu.")
    sleep(2)
    print("Cesta je velmi dlouhá a obtížná, ale bez ochranného obleku bys byl vystaven velkému riziku.")
    sleep(2)    
    print("Konečně po dlouhé a vysilující cestě dorazíš do místnosti s filtry, kde rychle vyměňuješ staré filtry za nové.")
    sleep(2)
    print("Nyní máš ochranný oblek a čistý vzduch, takže můžeš pokračovat dál.")
    sleep(2)
    print("Další místností co spatříš je laboratoř, kde vidíš značky k výzkumu mimozemských forem života.")
    sleep(2)
    print("Rozhodneš se prozkoumat laboratoř, abys zjistil, co se zde děje.")
    sleep(2)
    print("Cítíš, že jsi blízko cíle, ale musíš být stále na pozoru před nebezpečím.")
    sleep(2)
    print("Jaký bude tvůj další krok...?")


    print("---------------")
    print("1. Aron se rozhodne prozkoumat laboratoř.")
    sleep(2)
    print("2. Aron pokračuje dál bez prozkoumání laboratoře.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        prozkoumat_laborator()
    elif choice == "2":
        pokracovat_bez_laboratore()
    else:
        print("Neplatná volba, zkuste to znovu.")
        sektor_E12

def prozkoumat_laborator():
    print("Aron se rozhodne prozkoumat laboratoř.")
    sleep(2)
    print("Vcházíš do laboratoře, kde vidíš různé zkumavky a přístroje, které studují mimozemské organismy.")
    sleep(2)
    print("Najdednou spatříš temný kout místnoti a zajímá tě, co se tam nachází.")
    sleep(2)
    print("Přijdeš k tmavému rohu místonsti, ale stále nic nevidíš, kvůli špatnému světlu v místnosti.")
    sleep(2)
    print("V tom si vzpomeneš, že u sebe máš záložní zdroj světla, který sis vzal před tím než jsi přišel na loď.")
    sleep(2)
    print("Svítilna je už velice stará a zrezivělá s malou svítivostí a skoro i vybitá, ale i tak ti to postačí na osvícení temného koutu v zádu místnosti.")    
    sleep(2)
    print("Když se ti konečně podaří osvětlit tmavý roh laboratoře, tak si prohlížíš, co tam je.")
    sleep(2)
    print("V tmavém koutě najdeš spoustu sešitů a zápisníků vědců, kteří zkoumali Xenonita.")
    sleep(2)
    print("Zjistíš, že Xenobitus je velmi inteligentní a že zde mohou být i jiné další exempláře.")
    sleep(2)
    print("Rozhoduješ se, co dál, protože cítíš, že zdaleka nejsi na této lodi sám.")
    sleep(2)
    print("Po chvilce váhání ses rozhodnul pro cestu do sektoru E13.")
    sektor_E13()

def pokracovat_bez_laboratore():
    print("Aron se rozhodne pokračovat dál bez prozkoumání laboratoře.")
    sleep(2)
    print("Vydáváš se dál na chodbu, cítíš se o něco rychlejší, ale nevíš, co se děje v laboratoři.")
    sleep(2)
    print("Cesta je plná nebezpečí, a tak musíš být stále ostražitý.")
    sleep(2)
    print("Dorazíš k roscestníku, kde si musíš vybrat cestu, zda zůstaneš v sektoru E12, nebo budeš pokračovat do sektoru E13.")
    sleep(2)
    print("Nyní je to na tobě, jaké bude tvoje rozhodnutí.")

    print("---------------")
    print("1. Aron se rozhodne podrobněji prozkoumat sektor E12.")
    sleep(2)
    print("2. Aron se rozhodne pro cestu do sektoru E13.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        sektror_E12_podrobneji()
    elif choice == "2":
        sektor_E13()
    else:
        print("Neplatná volba, zkuste to znovu.")
        sektor_E12

def sektror_E12_podrobneji():
    print("Aron se nacházel uprostřed laboratoře sektoru E12, přemýšleje nad svými dalšími kroky.")
    sleep(2)
    print("Okolo něj byly hromady zápisníků a zkumavek, všechno opuštěné a zdálo se, že nikdo nebyl na lodi už dlouho.")
    sleep(2)
    print("Tvojí pozornost poutá nejnovější zápis, který naznačoval možnost komunikace s Xenonitem pomocí speciálního zařízení.")
    sleep(2)
    print("Při hledání dalších informací jsi najednou zaslechl kroky za dveřmi laboratoře.")
    sleep(2)
    print("Okamžitě zhasneš světlo a schováš se za stůl.")
    sleep(2)
    print("Hlasy a zvuky kroků naznačovaly, že na lodi nejsi sám.")
    sleep(2)
    print("Srdce ti buší a urychleně přemýšlíš, co máš dělat.")
    sleep(2)
    print("Máš riskovat a pokračovat v prozkoumávání laboratoře a celého sektoru E12, nebo se pokusit uniknout do sektoru E13?")
    sleep(2)
    print("Přitisknutý ke stolu zvažuješ své možnosti. 'Musím to zjistit', šeptal si pro sebe.")
    sleep(2)
    print("Uvědomuješ si, že riziko odhalení je příliš velké.")
    sleep(2)
    print("S potlačeným dechem ses rozhodl: Že se musíš dostat se do sektoru E13 a získat lepší přehled o situaci.")
    sleep(2)
    print("Zmáčkneš tlačítko na svém komunikačním zařízení a kontroluješ, zda je cesta volná.")
    sleep(2)
    print("Když sis byl jist, že je připravený, zasunul zápisník do kapsy a tiše vykročil směrem k východu.")
    sleep(2)
    print("Musel být opatrný a rychlý zároveň.")
    sleep(2)
    print("Vydal ses tedy na cestu.")
    sleep(2)
    print("Chodby sektoru E12 jsou úzké a chladné, zatímco stěny zdobí šedé panely, které vypadají, že je nikdo už roky nevyčistil.")
    sleep(2)
    print("Tvá cesta vpřed byla plná nejistoty, ale věděl jsi, že jediným způsobem, jak to přežít, bylo pokračovat dál.")
    sektor_E13()

def sektor_E13():
    print("Rozhodl ses směřovat svou cestu do sektoru E13.")
    sleep(2)
    print("Chodby jsou zde ještě tajemnější a chladnější, jako by zde čas zastavil svůj běh.")
    sleep(2)
    print("'Co tu asi mohu najít?', ptáš se sám sebe, zatímco pokračuješ vpřed.")
    sleep(2)
    print("Cítíš, že je to správný směr, ale nevíš, co tě čeká.")
    sleep(2)
    print("Po několika metrech zahlédneš za otevřenými dveřmi místnost plnou podivných přístrojů a světel.")
    sleep(2)
    print("Vstoupíš dovnitř a začneš zkoumat, co se zde nachází.")
    sleep(2)
    print("Přístroje a monitory na stěnách indikují nějaké složité experimenty.")
    sleep(2)
    print("'Kdo sem mohl takové věci instalovat?' ptáš se v duchu, zatímco pokračuješ v prohlížení místnosti.")
    sleep(2)
    print("Najednou zahlédneš na stole poznámky a výkresy.")
    sleep(2)
    print("Vypadají jako plány na nějaký nový technologický systém.")
    sleep(2)
    print("Přibližuješ se a začínáš si prohlížet jednotlivé stránky, když najednou uslyšíš podezřelé zvuky.")
    sleep(2)
    print("Srdce ti začne bušit rychleji a instinktivně se kryješ za jedním z přístrojů.")
    sleep(2)
    print("Slyšíš kroky a hlasité mluvení.")
    sleep(2)
    print("'Musíme to dokončit, než nás někdo najde,' ozve se hlas za dveřmi.")
    sleep(2)
    print("Zadržuješ dech a snažíš se rozhodnout, co máš teď udělat. Máš na výběr: ")


    print("---------------")
    print("1. Zůstat skrytý a sledovat, co se děje.")
    sleep(2)
    print("2. Pokračovat dál mimo místnost a hledat další cesty.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
       sledovani_situace()
    elif choice == "2":
        hledat_cesty()
    else:
        print("Neplatná volba, zkuste to znovu.")
        sektor_E13()

def sledovani_situace():
    print("Rozhodl ses zůstat skrytý a sledovat, co se děje.")
    sleep(2)
    print("Zpoza skrýše jsi pozoroval, jak do laboratoře vstoupila skupina ozbrojených vojáků, jejichž uniformy jsem nepoznával.")
    sleep(2)
    print("Každý jejich pohyb byl pečlivě organizovaný, což svědčilo o jejich vojenském výcviku.")
    sleep(2)
    print("„Musíme to tu prohledat,“ zaslechl jsi jednoho z nich říct.")
    sleep(2)
    print("„Máme informace, že se tady nachází důležité materiály o Xenobitu.“")
    sleep(2)
    print("Zatajil jsi dech, když se začali procházet po místnosti, prohledávat stoly a skříně.")
    sleep(2)
    print("Jeden z vojáků se přiblížil k mé skrýši, ale naštěstí si mě nevšiml.")
    sleep(2)
    print("Bylo jasné, že jejich přítomnost nebyla náhodná a že hledají něco konkrétního.")
    sleep(2)
    print("Náhle jeden z vojáků narazil na zápisník, který jsem před chvílí odložil.")
    sleep(2)
    print("„Tady něco máme,“ řekl a začal si číst poznámky.")
    sleep(2)
    print("„To je ono,“ odpověděl mu jeho nadřízený.")
    sleep(2)
    print("„Musíme se vrátit s tímhle materiálem na základnu. Velitel bude chtít vědět všechno o Xenobitu.“")
    sleep(2)
    print("Čekal jsi, dokud všichni vojáci neodešli z laboratoře, než jsi se opatrně vynořil ze skrýše.")
    sleep(2)
    print("Měl jsi štěstí, že tě neodhalili, ale bylo jasné, že situace se stává čím dál nebezpečnější.")
    sleep(2)
    print("Musíš najít způsob, jak se dostat ven a varovat ostatní před tím, co jsi právě zjistil.")
    sleep(2)
    print("Vyrazíš směrem k sektoru E13 s vědomím, že musíš být ještě opatrnější.")
    sleep(2)
    print("Nevíš, kdo tito vojáci byli, ale jedno bylo jisté – nebyli přátelé.")
    prozkoumavani_E13()
def hledat_cesty():
    print("Rozhodl ses nepokoušet štěstí a pokračovat dál mimo místnost.")
    sleep(2)
    print("Opatrně vykročíš z laboratoře a rychle se přesuneš do dalšího koridoru, který vede směrem k sektoru E13.")
    sleep(2)
    print("Při každém kroku cítíš, jak ti adrenalin pumpuje v žilách.")
    sleep(2)
    print("Chodba je temná a úzká, osvětlovaná pouze slabými nouzovými světly.")
    sleep(2)
    print("Každý zvuk ozvěny tvých kroků ti připomíná, že jsi na nepřátelském území.")
    sleep(2)
    print("Když dorazíš na rozcestí, rozhodneš se vydat vlevo, kde vidíš nápis „Strojovna“.")
    sleep(2)
    print("Možná tam najdeš něco užitečného, nebo alespoň bezpečné místo na odpočinek.")
    sleep(2)
    print("Při průchodu strojovnou narazíš na starý terminál, který je ještě funkční.")
    sleep(2)
    print("Pokusíš se získat přístup k lodním záznamům, ale systém je chráněný silnými bezpečnostními opatřeními.")
    sleep(2)
    print("Po několika neúspěšných pokusech si uvědomíš, že to nebude tak jednoduché.")
    sleep(2)
    print("Náhle zaslechneš kroky blížící se k tobě.")
    sleep(2)
    print("Okamžitě se schováš za velkou strojní součástku a zatajíš dech.")
    sleep(2)
    print("Když se kroky přiblíží, vidíš, jak kolem tebe prochází skupina ozbrojených vojáků.")
    sleep(2)
    print("Mluví mezi sebou, ale nerozumíš jim kvůli hluku strojů.")
    sleep(2)
    print("Jakmile vojáci zmizí z dohledu, rychle se vrátíš k terminálu a pokusíš se získat přístup k mapě lodi.")
    sleep(2)
    print("Po několika minutách konečně najdeš cestu, která tě může vést přímo do sektoru E13.")
    sleep(2)
    print("Je to riskantní, ale musíš to zkusit.")
    sleep(2)
    print("Vyrážíš na cestu, pevně odhodlaný najít odpovědi a přitom se vyhnout nebezpečí.")
    sleep(2)
    print("Víš, že další krok bude rozhodující pro tvé přežití i pro odhalení pravdy o Xenobitu a této záhadné lodi.")
    prozkoumavani_E13()

def prozkoumavani_E13():
    print("Pokračuješ v prozkoumávání sektoru E13.")
    sleep(2)
    print("Přístroje a monitory na stěnách vypadají stále více složitě a tajemně.")
    sleep(2)
    print("Najednou tvou pozornost upoutá jeden z monitorů.")
    sleep(2)
    print("Na obrazovce se zobrazuje sériový přenos dat, což indikuje, že něco na lodi je stále aktivní.")
    sleep(2)
    print("Přibližuješ se blíže a zjišťuješ, že se jedná o nějakou formu experimentálního výzkumu.")
    sleep(2)
    print("Po několika minutách procházení záznamů zjistíš, že experimenty se týkají molekulární struktury neznámé látky, pravděpodobně Xenonitu.")
    sleep(2)
    print("Najednou obrazovka zčerná a objeví se na ní nápis: 'Varování: Neoprávněný přístup'.")
    sleep(2)
    print("Znepokojený se rozhoduješ, co dál.")
    sleep(2)


    print("---------------")
    print("1. Pokusit se hacknout systém a získat více informací.")
    sleep(2)
    print("2. Pokračovat v prozkoumávání sektoru a najít další stopy.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        hackovani_systemu()
    elif choice == "2":
        hledani_stop()
    else:
        print("Neplatná volba, zkuste to znovu.")
        prozkoumavani_E13()

def hackovani_systemu():
    print("Rozhodl ses pokusit se hacknout systém a získat více informací.")
    sleep(2)
    print("Po několika minutách práce s klávesnicí se ti podaří proniknout do zabezpečeného systému.")
    sleep(2)
    print("Na obrazovce se objeví zpráva, která tě překvapí:")
    sleep(2)
    print("'Projekt Xenonit – Fáze III: Zajištění přístupu k základní struktuře pro další výzkum. Testovací subjekty jsou stabilní, ale vyžadují další monitorování.'")
    sleep(2)
    print("Zjistíš, že sektor E13 je jen částí většího výzkumného komplexu, a že klíčové informace mohou být skryty v sektoru E14.")
    sleep(2)
    print("Rozhoduješ se, co dál.")
    sleep(2)


    print("---------------")
    print("1. Pokračovat v prozkoumávání sektoru E13.")
    sleep(2)
    print("2. Vydat se do sektoru E14.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        hledani_stop()
    elif choice == "2":
        sektor_E14()
    else:
        print("Neplatná volba, zkuste to znovu.")
        hackovani_systemu()

def hledani_stop():
    print("Pokračuješ v prozkoumávání sektoru E13.")
    sleep(2)
    print("Najednou tvou pozornost upoutá malý droid, který se přibližuje.")
    sleep(2)
    print("Droid zastaví a z jeho reproduktoru zazní mechanický hlas: 'Identifikujte se.'")
    sleep(2)
    print("Máš několik vteřin na rozhodnutí:")
    sleep(2)


    print("---------------")
    print("1. Identifikovat se a zkusit komunikovat s droidem.")
    sleep(2)
    print("2. Pokračovat v hledání a ignorovat droida.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        komunikace_s_droidem()
    elif choice == "2":
        ignorovat_droida()
    else:
        print("Neplatná volba, zkuste to znovu.")
        hledani_stop()

def komunikace_s_droidem():
    print("Rozhodl ses identifikovat se a zkusit komunikovat s droidem.")
    sleep(2)
    print("Zadáš své identifikační údaje a čekáš na odpověď.")
    sleep(2)
    print("Droid přehrává zprávu: 'Přístup udělen. Prosím, následujte mě do sektoru E14.'")
    sleep(2)
    print("Následuješ droida, který tě vede k uzamčeným dveřím sektoru E14.")
    sleep(2)
    print("Po několika minutách cesty se ocitneš před těžkými ocelovými dveřmi označenými 'E14'.")
    sleep(2)
    print("Droid zadá kód a dveře se otevřou.")
    sleep(2)
    sektor_E14()

def ignorovat_droida():
    print("Rozhodl ses ignorovat droida a pokračovat v hledání.")
    sleep(2)
    print("Opatrně se pohybuješ kolem droida a pokračuješ v prozkoumávání místnosti.")
    sleep(2)
    print("Najdeš několik dalších poznámek a výkresů, které vypadají důležité.")
    sleep(2)
    print("V jednom z poznámek je zmínka o tajném výzkumném zařízení v sektoru E14.")
    sleep(2)
    print("Rozhoduješ se, že se tam musíš dostat.")
    sleep(2)
    sektor_E14()

def sektor_E14():
    print("Vydal ses do sektoru E14.")
    sleep(2)
    print("Opatrně se pohybuješ chodbami a kontroluješ každý roh.")
    sleep(2)
    print("Když dorazíš k těžkým ocelovým dveřím označeným 'E14', zjistíš, že jsou uzamčené.")
    sleep(2)
    print("Vidíš vedle dveří panel s numerickým kódem.")
    sleep(2)
    print("Můžeš buď zkusit hacknout panel, nebo se pokusit najít jiný vstup.")
    sleep(2)

    print("---------------")
    print("1. Zkusit hacknout panel.")
    sleep(2)
    print("2. Najít jiný vstup.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        hacknout_panel()
    elif choice == "2":
        najit_jiny_vstup()
    else:
        print("Neplatná volba, zkuste to znovu.")
        sektor_E14()

def hacknout_panel():
    print("Rozhodl ses zkusit hacknout panel.")
    sleep(2)
    print("Po několika minutách práce se ti podaří prolomit zabezpečení a dveře se otevřou.")
    sleep(2)
    print("Vstoupíš do sektoru E14 a okamžitě cítíš, že jsi objevil něco významného.")
    sleep(2)
    print("Laboratoř je plná moderního vybavení a podivných přístrojů.")
    sleep(2)
    print("Všechny monitory a obrazovky ukazují složité grafy a data týkající se Xenonitu.")
    sleep(2)
    print("Přibližuješ se k jednomu z monitorů a zjišťuješ, že zde probíhají experimenty na živých organismech.")
    sleep(2)
    print("Musíš zjistit více.")
    sleep(2)

    print("---------------")
    print("1. Pokračovat v prozkoumávání laboratoře.")
    sleep(2)
    print("2. Pokusit se získat data z hlavního počítače.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        prozkoumat_laboratore()
    elif choice == "2":
        ziskat_data()
    else:
        print("Neplatná volba, zkuste to znovu.")
        hacknout_panel()

def najit_jiny_vstup():
    print("Rozhodl ses najít jiný vstup.")
    sleep(2)
    print("Pohybuješ se kolem sektoru a hledáš možné alternativy.")
    sleep(2)
    print("Po několika minutách najdeš servisní šachtu, která by mohla vést do sektoru E14.")
    sleep(2)
    print("Vstoupíš do šachty a pomalu se proplétáš úzkými chodbami.")
    sleep(2)
    print("Po několika minutách se ocitneš uvnitř sektoru E14.")
    sleep(2)
    print("Laboratoř je plná moderního vybavení a podivných přístrojů.")
    sleep(2)
    print("Všechny monitory a obrazovky ukazují složité grafy a data týkající se Xenonitu.")
    sleep(2)
    print("Přibližuješ se k jednomu z monitorů a zjišťuješ, že zde probíhají experimenty na živých organismech.")
    sleep(2)
    print("Musíš zjistit více.")
    sleep(2)

    print("---------------")
    print("1. Pokračovat v prozkoumávání laboratoře.")
    sleep(2)
    print("2. Pokusit se získat data z hlavního počítače.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        prozkoumat_laboratore()
    elif choice == "2":
        ziskat_data()
    else:
        print("Neplatná volba, zkuste to znovu.")
        najit_jiny_vstup()

def prozkoumat_laboratore():
    print("Pokračuješ v prozkoumávání laboratoře.")
    sleep(2)
    print("Nacházíš řadu zajímavých experimentů a poznámek.")
    sleep(2)
    print("Zjistíš, že Xenonit má potenciál být využit jako neuvěřitelně silný zdroj energie.")
    sleep(2)
    print("Nebo jako zbraň neuvěřitelné ničivé síly.")
    sleep(2)
    print("Musíš se rozhodnout, jak s těmito informacemi naložíš.")
    sleep(2)
    print("Můžeš se pokusit najít způsob, jak zničit laboratoř a zastavit experimenty.")
    sleep(2)
    print("Nebo zkusit kontaktovat někoho mimo loď a varovat je před tím, co jsi objevil.")
    sleep(2)

    print("---------------")
    print("1. Pokusit se zničit laboratoř.")
    sleep(2)
    print("2. Kontaktovat někoho mimo loď.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        znicit_laborator()
    elif choice == "2":
        kontaktovat_venek()
    else:
        print("Neplatná volba, zkuste to znovu.")
        prozkoumat_laboratore()

def ziskat_data():
    print("Pokusíš se získat data z hlavního počítače.")
    sleep(2)
    print("Po několika minutách práce se ti podaří přístup k systému.")
    sleep(2)
    print("Získáš všechny potřebné informace o experimentech a potenciálu Xenonitu.")
    sleep(2)
    print("Nyní musíš rozhodnout, jak s těmito informacemi naložíš.")
    sleep(2)
    print("Můžeš se pokusit najít způsob, jak zničit laboratoř a zastavit experimenty.")
    sleep(2)
    print("Nebo zkusit kontaktovat někoho mimo loď a varovat je před tím, co jsi objevil.")
    sleep(2)

    print("---------------")
    print("1. Pokusit se zničit laboratoř.")
    sleep(2)
    print("2. Kontaktovat někoho mimo loď.")
    print("---------------")

    choice = input("Zadejte číslo vaší volby: ")

    if choice == "1":
        znicit_laborator()
    elif choice == "2":
        kontaktovat_venek()
    else:
        print("Neplatná volba, zkuste to znovu.")
        ziskat_data()

def znicit_laborator():
    print("Rozhodl ses pokusit zničit laboratoř a zastavit experimenty.")
    sleep(2)
    print("Hledáš způsob, jak iniciovat autodestrukční sekvenci nebo způsobit přetížení systému.")
    sleep(2)
    print("Po několika minutách nacházíš hlavní kontrolní panel.")
    sleep(2)
    print("Zadáš sekvenci pro autodestrukci a začneš odpočítávat.")
    sleep(2)
    print("Máš jen několik minut na útěk.")
    sleep(2)
    print("Běžíš chodbami, zatímco alarmy houkají a červená světla blikají.")
    sleep(2)
    print("Musíš se dostat ven, než dojde k výbuchu.")
    sleep(2)
    print("Po několika minutách se ti podaří dostat na bezpečné místo.")
    sleep(2)
    print("Ohlédneš se zpět a vidíš, jak sektor E14 exploduje a pohlcuje vše kolem.")
    sleep(2)
    print("Dokázal jsi to, laboratoř je zničena a experimenty jsou zastaveny.")
    sleep(2)
    print("Ale věděl jsi, že tohle je teprve začátek.")
    sleep(2)
    print("Konec příběhu.")
    end_game()

def kontaktovat_venek():
    print("Rozhodl ses pokusit kontaktovat někoho mimo loď a varovat je před tím, co jsi objevil.")
    sleep(2)
    print("Najdeš komunikační zařízení a zadáš kódy pro nouzový přenos.")
    sleep(2)
    print("Po několika minutách se ti podaří navázat spojení.")
    sleep(2)
    print("„Tady Aron, jsem na lodi a objevil jsem něco neuvěřitelného.“")
    sleep(2)
    print("„Musíte poslat pomoc a zastavit tyto experimenty.“")
    sleep(2)
    print("„Rozumíme, Arone. Posíláme záchranný tým. Drž se!“ ozve se z reproduktoru.")
    sleep(2)
    print("Nyní musíš čekat na záchranný tým a doufat, že dorazí včas.")
    sleep(2)
    print("Skrýváš se a sleduješ každé hnutí, zatímco alarmy stále houkají.")
    sleep(2)
    print("Po několika hodinách dorazí záchranný tým a dostane tě do bezpečí.")
    sleep(2)
    print("Podařilo se ti varovat ostatní a zastavit experimenty.")
    sleep(2)
    print("Ale věděl jsi, že tohle je teprve začátek.")
    sleep(2)
    print("Konec příběhu.")
    end_game()
    
def end_game():
    print("---------------")
    repeater = input("Chceš začít znovu? (ano/ne): ")
    if repeater == "ano":
        start_game()
    elif repeater == "ne":
        exit()
    else:
        print("Neplatná volba, zkuste to znovu.")
        return end_game()
         
def prvni_smrt_jedna():
    print("---------------")
    print("Aron zemřel probodnutím.")

def druha_smrt_dva():
    print("---------------")
    print("Aron zemřel roztrhnutím.")

def treti_smrt_tri():
    print("---------------")
    print("Aron zemřel poté, co ho Xenobitus napíchl na ocelovou tyč.")

if __name__ == "__main__":
    main()