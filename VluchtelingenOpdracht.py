
import time

def Einde():
    print("Je hebt het einde berijkt! Zou je het verhaal nog een keer willen afspelen?")
    time.sleep(1)
    print("1. ja")
    time.sleep(1)
    print("2. nee")
    NogEenKeer = input()
    if NogEenKeer == "nee":
        exit()

def a1():
    print("Je blijft met je vrouw in Syrië. Maar dat maakt de situatie wel erg lastig dus je moet nu gaan beslissen.")
    time.sleep(1)
    print("1. Je gaat onderduiken bij het verset om in veiligheid te komen.")
    time.sleep(1)
    print("2. Je gaat naar je oude woonplaats in Allepo.")
    time.sleep(1)
    answera1 = input()
    if answera1 == "1":
        b2()
    elif answera1 == "2":
        b1()

def a2():
    print("Je gaat naar Turkije omdat je er in geloofd dat daar een beter leven is zonder oorlog. Je moet alleen wel al je geld uitgeven aan de smokkelaars en dan zit je 10 uur lag met 67 mensen in een kleine rubberen boot.")
    time.sleep(1)
    b3()

def b1():
    print("Je hebt besloten naar je oude woonplaats te gaan om daar te wonen. Ver bij de oorlog vandaan.")
    time.sleep(1)
    c1()

def b2():
    print("Om je vrouw en kinderen zo snel mogelijk in veiligheid te brengen kies je er voor om onder te duiken bij het verzet.")
    time.sleep(1)
    c2()

def b3():
    print("Omdat je illegaal naar Turkije bent gekomen en de kustwacht je op staat te wachten en wordt je dus gearresteerd.")
    time.sleep(1)
    print("Eenmaal op het bureau wordt je verteld dat je straks de gevangenis in moet om te wachten totdat je straf is uitgedeeld.")
    time.sleep(1)
    c3()

def c1():
    print("Nadat je naar je oude woonplaats was vertrokken kwam je daar een verlaten supermarkt tegen. In die supermarkt zat genoeg etem om jou en je familie te voeden voor de komende 2 jaar.")
    time.sleep(1)
    print("1. Ga door met naar je oude woonplaats te gaan en daar met familie te wonen.")
    time.sleep(1)
    print("2. Ga het eten delen met andere mensen die het ook hard nodig hebben.")
    time.sleep(1)
    answerc1 = input()
    if answerc1 == "1":
        d1()
    elif answerc1 == "2":
        d2()

def c2_1():
    print("Je bent eten gaan uitdelen aan mensen en je bent ze gaan helpen vlucht. Terwijl je dit doet ga je bij het verzet omdat je het vreschil uit wil maken.")
    time.sleep(1)
    d3()

def c2():
    print("Omdat je bent ondergedoken bij het verzet moet je betalen door te helpen met waar ze mee bezig waren. Dus je moet mee doen met het verzet.")
    time.sleep(1)
    print("1. Ga weg bij het verzet en besluit te verhuizen naar je oude woonplaats.")
    time.sleep(1)
    print("2. Ga het verzet helen en mee doen met de grote operaties.")
    time.sleep(1)
    answerc2 = input()
    if answerc2 == "1":
        d1()
    elif answerc2 == "2":
        d3()

def c3():
    print("Nu je in de gevangenis zit vraag je je af of je je familie nog wel gaat zien.")
    time.sleep(1)
    print("1. Begin gesprek met wachter die Russisch is en wordt vrienden.")
    time.sleep(1)
    print("2. Wacht gehoorzaam in de cel hopende dat je wordt overgeplaatst of je wordt vrij gelaten.")
    time.sleep(1)
    answerc3 = input()
    if answerc3 == "1":
        d5()
    elif answerc3 == "2":
        d4()
def d1():
    print("Nu je verder aan het vluchten ben naar je oude woonplaats kom je er achter dat er familie leden daar ook zijn heen vertrokken.")
    time.sleep(1)
    print("Nu je in je oude woonplaats bent moet je nog een huis zoeken.")
    time.sleep(1)
    e1()

def d2():
    print("Je stopt met naar je oude huis gaan en je gaat iedereen die je tegen komt een beetje eten geven en helpen waar je kan.")
    time.sleep(1)
    c2_1()


def d3():
    print("Omdat je bij het verset zit en er een binnenval werdt gedaan bij het hoofdquartier door de toenmalige dictator wordt je gevangen genomen")
    time.sleep(1)
    print("Ook worden je vrouw en kinderen meegenomen.")
    time.sleep(1)
    e2()

def d4():
    print("Na 3 maanden niks te horen krijgen over het proces en wat voor straf je krijgt komt er een wachter. Hij roept je naam. En toen riep hij dat je 12 jaar lang cels traf kreeg.")
    time.sleep(1)
    print("Je vroeg aan de wachter waarom dat zo was terwijl je je tranen achter probeerde te houden. hij vertelde dat de smokkelaars een wachter hadden vermoord in Syrië. Dus dat maakt hun een medeplichtige.")
    time.sleep(1)
    e3()

def d5():
    print("Omdat je vrienden bent geworden met de wachter had hij medeleiden en heeft hij met een aantal mensen gepraat die er voor gezorgd hebben dat hij overgeplaatst kon woden.")
    time.sleep(1)
    print("In de andere gevangenis is het veel schoner en hier heeft hij een kans op vrijheid. En de wachter is daar ook en gaat je helpen.")
    time.sleep(1)
    e4()

def e1():
    print("Je hebt besloten om te gaan verhuizen nog verder van de oorlog vandaan want je wil geen risico lopen da je weer meot vluchten.")
    time.sleep(1)
    print("1. Neem het risico en blijf in je oude woonplaats.")
    time.sleep(1)
    print("2. Ga nog verder naar het noorden om daar erg afgelegen te wonen.")
    time.sleep(1)
    answere1 = input()
    if answere1 == "1":
        f1()
    elif answere1 == "2":
        f2()

def e2():
    print("Toen je gevangen werdt genomen door de dictator heb je geen eerlijk proces gehad en dus moest je 6 jaar de gevangens in zonder parol.")
    time.sleep(1)
    print("Na 6 jaar lang wachten tot dat je weer er uit kon zonder contact met je familie en gezin kom je er achter dat je vrouw en kinderen er niet meer zijn. Je vrouw was verkocht en vermoord en je kinderen zijn ook weg.")
    time.sleep(1)
    print("Na dat je dit verschrikkelijke nieuws kreeg raakte je in een zware depressie. Het was alsof het enige waar jij op wachte en wat het wachten waard maakte jou meteen was ontnomen.")
    time.sleep(1)
    print("3 maanden gaan voorbij... Je eet niet goed en je verzorcht jezelf niet. Uiteindelijk ben je het zat en spring je voor een trein.")
    time.sleep(1)
    print("Einde.")
    time.sleep(3)
    Einde()

def e3():
    print("Je komt uit de gevangenis na 12 jaar lang vast zitten. Je kinderen en vrouw wachten op je en je kan terug naar Syrië.")
    time.sleep(1)
    print("Alleen je het geen geld en ook geen huis. Maar wel je gezin")
    time.sleep(1)
    print("Nu je terug bent in Syrië krijg je het nieuws te horen dat je moeder is overleden en een aantal vrienden. Maar je bent blij dat er no mensen zijn waar je van kan houden.")
    time.sleep(1)
    print("Einde.")
    time.sleep(1)
    Einde()

def e4():
    print("Omdat die wachter je wilde helpen is alles heel goed gegaan. Je hebt met je gezin gesproken en je gaat naar Nederland voor geld en onderdak.")
    time.sleep(1)
    print("Je woont in nederland en je hebt een huis en werk dus je laat met behulp van een organisatie je vrouw en kinderen over vliegen.")
    time.sleep(1)
    print("Nu ben je met je hele gezin weer samen en je heb een stabiel bestaan.")
    time.sleep(1)
    print("1. Ga terug naar Syrië zodra de kust veilig is en je er weer kan wonen met werk.")
    time.sleep(1)
    print("2. Blijf in Nederland en bouw hier een bestaan op.")
    time.sleep(1)
    asnwere4 = input()
    if asnwere4 == "1":
        f1()
    elif asnwere4 == "2":
        f3()

def f1(): 
    print("Na lang zoeken heb je toch er voor gekozen om in de oude woonplaats te wonen.")
    time.sleep(1)
    print("Daar heb je nu een mooi huis en een het is een veilige plek voor je vrouw en kinderen.")
    time.sleep(1)
    print("Het huis is groot genoeg om een aantal familie leden in te laten leven dus uiteindelijk komen je twee neefen en je moeder bij je wonen.")
    time.sleep(1)
    f3()

def f2():
    print("Omdat je ging door zoeken duurde het erg lang voordat je een goeie plek had gevonden maar een heel stuk naar het oosten vondt je een mooi huis om in te wonen.")
    time.sleep(1)
    print("Je moeder is daar nu ook naar toe gekomen. Dus nu kan je haar ook verzorgen.")
    time.sleep(1)
    f3()

def f3():
    print("Alles komt goed en je leeft een liefdevol en rijk leven met je moede ren gezin. Je geniet van leven en je kinderen groeien goed op. Uiteindelijk verhuizen zij naar europa op de hoop succesvol te worden.")
    time.sleep(1)
    print("Einde.")
    time.sleep(3)
    Einde()

while True:
    print("Oke even om uit te leggen hoe het werkt.")
    time.sleep(1)
    print("Als je een keuze krijgt moet je 1 of 2 typen in cijfers niet letters. Ook geen punt er achter of iets dergelijks.")
    time.sleep(1)
    print("Oke nu je dat weet wens ik je veel succes!")
    time.sleep(1)
    print("Het verhaal begint in Syrie. De hoofdstad Demascus is overgenomen door een dictator.")
    time.sleep(1)
    print("Daar woon jij Naghmar Abdhul, maar je heb took een vrouw, 3 kinderen en een moeder waar je voor meot zorgen.")
    time.sleep(1)
    print("Er breekt een burger oorlog uit en er komen absurt veel mensen om in het gevecht.")
    time.sleep(1)
    print("Omdat je een beter leven voor je vrouw, moeder en kinderen wil moet je een beslissing maken.")
    time.sleep(1)
    print("1. Blijf met je vrouw, moede ren kinderen in Syrië.")
    time.sleep(1)
    print("2. Ga naar Turkijen om een betere plek om te wonen te vinden.")
    time.sleep(1)
    answerBegin = input()
    if answerBegin == "1":
        a1()
    elif answerBegin == "2":
        a2()