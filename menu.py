# importolni - > statok
import random
eletero = 10
energia = 10
arany = 50
def fomenu():
        valasztas = 7
        print ('1 - Menj egyenesen')
        print ('2 - Menj balra')
        print ('3 - Menj jobbra')
        print ('4 - Egyél édességet (növeld meg az energiaszinted)')
        print ('5 - Édesség bolt meglátogatása')
        print ('6 - Kilépés')
        while valasztas >6 or valasztas <1:
            valasztas = int(input('Válassz! '))
        match valasztas:
            case 1: 
                valasztas_case_1 = 7
                eloszoregyenesen = 1
                szokokut = 1
                print('1 - Balra mész')
                print('2 - Jobbra mész')
                print('3 - Egyél édességet (növeld meg az energiaszinted)')
                print ('4 - Édesség bolt meglátogatása')
                print ('5 - Kilépés')
                while valasztas_case_1 >6 or valasztas <1:
                    valasztas_case_1 = int(input('Válassz!'))
                match valasztas_case_1:
                    case 1:
                        ## Artúr dolga:
                        kedvesvagyelijeszt = random.randint(1,2)
                        if kedvesvagyelijeszt = 1:
                            bohoc = 'kedves volt veled'
                        else:
                            bohoc = 'gonosz volt veled'
                            
                        print(f'Találkozol egy kedves  bohóccal és {bohoc}.')
                        if bohoc = 'kedves volt veled':
                            print('Kaptál 1 db cukrot.')
                        else:
                            print('Fogyott az életerőd 1-el.')
            case 2:
                eloszorbalra = 1
                    # 3 esemény történhet
            case 6:
                print('Játék vége')
               # z kategóriából 3 féle esemény közül generálódjon 1
    
     