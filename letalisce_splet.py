import modeli as modeli
from bottle import *
from datetime import datetime


def pretvoriDatum(x):
    if x is None:
        return None
    if isinstance(x, str):
        return time.strftime("%d.%m.%Y", time.strptime(x, '%Y-%m-%d %H:%M:%S'))
    else:
        return datetime.strftime(x, "%d.%m.%Y")

def dobiSeznamOdhodnihLetalisc():
    odhodnaLetalisca = modeli.OdhodnaLetalisca()
    mesta = []
    for elt in odhodnaLetalisca:
        mesta.append(elt[0])
    return mesta

def dobiSeznamPrihodnihLetalisc(izhodisce):
    prihodnaLetalisca = modeli.PrihodnaLetalisca(izhodisce)
    mesta = []
    for elt in prihodnaLetalisca:
        mesta.append(elt[0])
    return mesta


@get('/')
def glavniMenu():
    odhodnaLetalisca = dobiSeznamOdhodnihLetalisc()
    odhodnaLetalisca.insert(0, "Izberi")
    return template('glavni.html', odhodnaLetalisca=odhodnaLetalisca, prihodnaLetalisca=["Prihodno letališče"])

@post('/')
def glavniMenu2():
    odhodnoLetalisce = request.forms.get('odhodnoLetalisce')

    odhodnaLetalisca = dobiSeznamOdhodnihLetalisc()
    prihodnaLetalisca = dobiSeznamPrihodnihLetalisc(odhodnoLetalisce)
    return template('glavni.html', prihodoLetalisceOmogoceno=True, izbranoLetalisce=odhodnoLetalisce, odhodnaLetalisca=odhodnaLetalisca, prihodnaLetalisca=prihodnaLetalisca)

@get('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')


        
##@get('/oseba/<emso>')
##def oOsebi(emso):
##    napaka = request.query.napaka
##    if not napaka:
##        napaka = None
##    emso, ime, priimek, ulica, hisna_st, postna_st, posta = modeli.poisciEMSO(emso)
##    racuni = modeli.racunEMSO(emso)
##    return template('oseba.html', emso = emso, ime = ime, priimek = priimek,
##                    ulica = ulica, hisna_st = hisna_st, postna_st = postna_st,
##                    posta = posta, racuni = racuni, pretvori = pretvoriDatum,
##                    napaka = napaka)
##
##@get('/isci')
##def isci():
##    priimek = request.query.iskalniNiz
##    rezultat = modeli.poisciPriimek(priimek)
##    return template('isci.html', rezultat = rezultat)
##
##@post('/dodaj')
##def dodaj():
##    emso = request.forms.emso
##    ime = request.forms.ime
##    priimek = request.forms.priimek
##    ulica = request.forms.ulica
##    hisna_st = request.forms.hisna_st
##    postna_st = request.forms.postna_st
##    kraj = request.forms.kraj
##    try:
##        if not modeli.dodajOsebo(ime, priimek, emso, ulica, hisna_st, postna_st):
##            modeli.dodajKraj(postna_st, kraj)
##            modeli.dodajOsebo(ime, priimek, emso, ulica, hisna_st, postna_st)
##    except Exception as e:
##        return template('glavni.html', ime = ime, priimek = priimek, emso = emso,
##                        ulica = ulica, hisna_st = hisna_st, postna_st = postna_st,
##                        kraj = kraj, napaka = e)
##    redirect('/oseba/' + emso)
##
##@post('/polog/<racun>')
##def polog(racun):
##    emso, = modeli.emsoRacun(racun)
##    try:
##        znesek = int(request.forms.znesek)
##    except Exception as e:
##        redirect('/oseba/' + emso + '?napaka=Neveljaven znesek!')
##    if znesek <= 0:
##        redirect('/oseba/' + emso + '?napaka=Znesek mora biti pozitiven!')
##    else:
##        modeli.dodajTransakcijo(racun, znesek)
##        redirect('/oseba/' + emso)
##
##@post('/dvig/<racun>')
##def dvig(racun):
##    emso, = modeli.emsoRacun(racun)
##    try:
##        znesek = int(request.forms.znesek)
##    except Exception as e:
##        redirect('/oseba/' + emso + '?napaka=Neveljaven znesek!')
##    if znesek <= 0:
##        redirect('/oseba/' + emso + '?napaka=Znesek mora biti pozitiven!')
##    else:
##        modeli.dodajTransakcijo(racun, -znesek)
##        redirect('/oseba/' + emso)

# poženemo strežnik na portu 8080, glej http://localhost:8080/
run(host='localhost', port=8080, reloader=False)