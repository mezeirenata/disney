import random
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

def egyenes1():
    prPurple('Egyenesen mentél volna tovább, azonban valaki megbotlott benned és elestetek mindketten.')

def egyenes2():
    prPurple('Tovább mentél egyenesen, azonban elakadtál egy nagy pocsolyánál.')
    prPurple('Mielőtt elgondolkozhattál volna, hogyan is kerüld ki, elvesztetted az egyensúlyod és beleestél')
    prPurple('a pocsolyába.')

def egyenes3():
    prPurple('Egyenesen mentél tovább, és mielőtt a szökőkúthoz értél volna, megcsúszott a lábad és')
    prPurple('szerencsétlenül az arcodra estél.')

def bohoc1():
    prPurple('Találkoztál egy bohóccal, aki kedves volt veled.')
    prPurple('Kaptál 1 db cukrot.')

def bohoc2():
    prPurple('Találkoztál egy bohóccal, aki gonosz volt veled.') 
    prRed('Elvesztettél 1 HP-t')

def donaldkacsa():
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Találkoztál Donald kacsával, aki felajánlott neked egy közös képet, ez jó kedvre derített.')

def shrek():
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Találkoztál Shrek-kel. Közölted vele hogy fotózkodni szeretnél vele, ')
    prPurple('de ő csak öt aranyadért cserébe egyezett bele.')
    print('\t-------------')
    prRed(f'\t -5 arany')
    print('\t-------------')

def mikieger():
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Találkoztál Miki egérrel, akitől kértél egy közös képet, azonban ellopta az összes cukrod.')

def szk1():
    prPurple('Beálltál játszani a szerencsekeréken, azonban nem volt szerencséd és ')
    prPurple('elvesztettél egy kevés pénzt.')
    print('\t-----------')
    prRed('\t -15 arany ')
    print('\t-----------')

def szk2():
    prPurple('Beálltál játszani és szerencsétlenséged okán elvesztetted az összes aranyad. ')

def szk3():
        prPurple('Beálltál szerencsekerekezni, és nyertél egy kevés aranyat')
        print('\t----------')
        prGreen('\t +15 arany ')
        print('\t----------')

def szk4():
    prPurple('Beálltál játszani és rengeteg aranyat nyertél. Most nagyon szerencsés voltál.')
    print('\t----------')
    prGreen('\t "+50 arany ')
    print('\t----------')

def szk5():
    prPurple('Beálltál játszani a szerencsekeréken, azonban nem volt szerencséd és ')
    prPurple('elvesztettél egy kevés pénzt.')
    print('\t-----------')
    prRed('\t -15 arany ')
    print('\t-----------')

def szk6():
    prPurple('Hiába álltál be játszani, sajnos nem nyertél semmit.')
    prPurple('Tessék egy kastélyjegy, kiengesztelésből!')
    print('\t---------------')
    prGreen('\t + kastélyjegy ')
    print('\t---------------')

def szk0():
    prPurple('Mivel úgy döntöttél, hogy kihagyod a szerencsekerekezést, ezért elindultál tovább, ')
    prPurple('azonban megláttál a földön valamit.')
    prPurple('Jobban megnézted, és kiderült, hogy 15 arany volt a földön. Ez aztán a szerencse! ')
    print('\t-----------')
    prGreen('\t +15 arany ')
    print('\t-----------')

def elszakad():
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Vettél sikeresen egy kastély belépőt, azonban kiejtetted a kezedből.')
    prPurple('A jegyet soha nem találtad meg ')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    print('\n')
    prRed('Sajnos a játéknak vége!')

def nemszakad():
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Vettél sikeresen egy kastély belépőt.')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    print('\n')
    prGreen('Kijátszottad a játékot, az utadat szabadon folytathatod a kastélyban!') 

def nemvesz():
    prRed('Az őrök eltávolítottak a kastélyból, a játéknak vége.')

def kileptel():
    print('\n')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prRed('\tKiléptél a kastélyból.')
    prRed('\tA játéknak vége.')
    print('──────────────────────────────────────────────────────────────────────────────────────────')

def orok():
    print('\n')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prRed('Mivel úgy döntöttél, hogy beljebb mész a kastélyba jegy nélkül ')
    prRed('az őrök eltávolítottak a kastélyból.')
    prRed('\t A játéknak vége.')
    print('──────────────────────────────────────────────────────────────────────────────────────────')

def kedvesember():

    print('\n')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prGreen('Úgy döntöttél, hogy beljebb mész a kastélyba jegy nélkül, azonban őrök kezdtek haladni feléd.')
    prGreen('Szerencsére egy másik ember észrevette az őröket, és kedvességből adott neked egy kastélyjegyet. ')
    prGreen('\t Kijátszottad a játékot, az utadat szabadon folytathatod a kastélyban!')
    print('──────────────────────────────────────────────────────────────────────────────────────────')

def furaillat():

    prPurple('Odamentél és megszagoltad a virágokat.')
    prPurple('Egy pillanatra fura illatot éreztél, a következő pillanatban pedig el kezdtél émelyegni.')
    prPurple('Szerencsére hamar elmúlt az émelygés, de fáradtabbnak érzed magad.')
    print('\t-------------')
    prRed('\t - 5 energia')
    print('\t-------------')

def furaillat2():

    prPurple('Odamentél megcsodálni a virágokat, és kíváncsiságból megszagoltad az egyiket.')
    prPurple('Egyszer csak rossz lett a közérzeted, és a földre kerültél.')
    print('\t-------------')
    prRed('\t - 5 HP')
    print('\t-------------')
    print('\n')
    prPurple('Pár perc földönfekvés után feleszméltél, és visszaemlékeztél arra, hogy mi történt.')

def normalisillat():
    prPurple('Odamentél megcsodálni a virágokat, majd egy hosszú perc után visszatértél utadra.')

def magdi1():
    print('\n')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Elfogadtad a meghívást, azonban nem túl boldogan távoztál a sátrából,')
    prPurple('mert Magdi néni átvert 15 arannyal. ')
    print('\t----------')
    prRed('\t -15 arany')
    print('\t----------')
    print('──────────────────────────────────────────────────────────────────────────────────────────')

def magdi2():
        print('\n')
        print('──────────────────────────────────────────────────────────────────────────────────────────')
        prPurple('Elfogadtad a meghívást, és fülig érő mosollyal hagytad el a jóslás után a sátrat,')
        prPurple('mert remek jövőt jósolt neked Magdi néni')
        print('\t------')
        prGreen(f'\t + 1 HP')
        print('\t------')
        print('──────────────────────────────────────────────────────────────────────────────────────────')

def magdi3():
    print('\n')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Elutasítottad Magdi néni meghívását, és szerencsédre most nem haragudott meg rád.')
    prPurple('Szabadon mehetsz tovább.')
    print('──────────────────────────────────────────────────────────────────────────────────────────')

def magdi4():

    print('\n')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Elutasítottad Magdi néni meghívását, és ő ezt nem hagyta annyiban. ')
    prPurple('Elátkozott téged.')
    print('\t-------')
    prRed('\t - 5 HP')
    print('\t-------')
    print('──────────────────────────────────────────────────────────────────────────────────────────')

def unikornis():
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Miután elhagytad a virágokat, az egyenes utat járva')
    prPurple('egy varázs póni szállt le hozzád az égből.')

def szel():
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Miután elhagytad a virágokat, az egyenes utat járva')
    prPurple('Hirtelen erősen kezdett el fújni a szél.')

def unikornis1():
    prPurple('A varázspóni habozás nélkül felvarázsolt a hátára, majd elrepített téged')
    prPurple('Varázsországba, ahonnan soha nem térsz vissza.')
    prRed('A játéknak vége.')
    print('──────────────────────────────────────────────────────────────────────────────────────────')

def unikornis2():
    prPurple('A varázspóni közelebb jött hozzád, majd elvarázsolt egy időre.')

def kastely1():
    prPurple('Beléptél a kastélyba.')
    prPurple('Mivel volt egy korábbról szerzett jegyed, ezért a kastélyban jegyváráslás nélkül továbbmehetsz.')

def kastely2():
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Vettél sikeresen egy kastély belépőt.')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    print('\n')
    prGreen('Kijátszottad a játékot, az utadat szabadon folytathatod a kastélyban!') 

def kastely3():
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('Vettél sikeresen egy kastély belépőt, azonban kiejtetted a kezedből.')
    prPurple('A jegyet soha nem találtad meg ')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    print('\n')
    prRed('Sajnos a játéknak vége!')

def kastely4():
    print('\n')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prRed('Mivel úgy döntöttél, hogy maradsz a kastélyban és beljebb mész jegy nélkül, az őrök') 
    prRed('eltávolítottak a kastélyból.')
    prRed('\t A játéknak vége.')
    print('──────────────────────────────────────────────────────────────────────────────────────────')

def kastely5():
    print('\n')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prGreen('Úgy döntöttél, hogy beljebb mész a kastélyba jegy nélkül, azonban őrök kezdtek haladni feléd.')
    prGreen('Szerencsére egy másik ember észrevette az őröket, és kedvességből adott neked egy kastélyjegyet. ')
    prGreen('\t Kijátszottad a játékot, az utadat szabadon folytathatod a kastélyban!')
    print('──────────────────────────────────────────────────────────────────────────────────────────')

def elesik():
    prPurple('Az erős szél miatt elestél, és lehorzsoltad a könyököd.')
    print('\t----------')
    prRed('\t - 5 HP')
    print('\t----------')
    print('──────────────────────────────────────────────────────────────────────────────────────────')

def kastelyjegy():
    prPurple('Miközben próbáltál ellenálni az erős szélnek, egy kastélyjegyet fújt a szél az arcodba.')
    print('\t------------------')
    prGreen('\t + 1 kastélyjegy')
    print('\t------------------')
    print('──────────────────────────────────────────────────────────────────────────────────────────')