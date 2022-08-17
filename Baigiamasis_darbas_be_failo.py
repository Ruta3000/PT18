from tkinter import *
import sqlite3

langas = Tk()
langas.geometry("1500x900")

# scrollbaras = Scrollbar(langas)
# box = Listbox(langas, yscrollcommand=scrollbaras.set)
# scrollbaras.config(command=box.yview)
#
# scrollbaras.grid(column=0)
# sarasas = range(1, 47)
# box.grid(column=5)

def spausdinti():
    ivesta = laukas_slapyvardziui.get()
    rezultatas0["text"] = ivesta

def spausdinti1():
    ivesta1 = laukas1.get()
    rezultatas1["text"] = ivesta1

def spausdinti2():
    ivesta2 = laukas2.get()
    rezultatas2["text"] = ivesta2

def spausdinti3():
    ivesta3 = laukas3.get()
    rezultatas3["text"] = ivesta3

def spausdinti4():
    ivesta4 = laukas4.get()
    rezultatas4["text"] = ivesta4

def spausdinti5():
    ivesta5 = laukas5.get()
    rezultatas5["text"] = ivesta5

def spausdinti6():
    ivesta6 = laukas6.get()
    rezultatas6["text"] = ivesta6

def spausdinti7():
    ivesta7 = laukas7.get()
    rezultatas7["text"] = ivesta7

def spausdinti8():
    ivesta8 = laukas8.get()
    rezultatas8["text"] = ivesta8

def spausdinti9():
    ivesta9 = laukas9.get()
    rezultatas9["text"] = ivesta9

def spausdinti10():
    ivesta10 = laukas10.get()
    rezultatas10["text"] = ivesta10

def spausdinti11():
    ivesta11 = laukas11.get()
    rezultatas11["text"] = ivesta11

def spausdinti12():
    ivesta12 = laukas12.get()
    rezultatas12["text"] = ivesta12

def spausdinti13():
    ivesta13 = laukas13.get()
    rezultatas13["text"] = ivesta13

def spausdinti14():
    ivesta14 = laukas14.get()
    rezultatas14["text"] = ivesta14

def spausdinti15():
    ivesta15 = laukas15.get()
    rezultatas15["text"] = ivesta15

def spausdinti16():
    ivesta16 = laukas16.get()
    rezultatas16["text"] = ivesta16

def spausdinti17():
    ivesta17 = laukas17.get()
    rezultatas17["text"] = ivesta17

def spausdinti18():
    ivesta18 = laukas18.get()
    rezultatas18["text"] = ivesta18

def spausdinti19():
    ivesta19 = laukas19.get()
    rezultatas19["text"] = ivesta19

def spausdinti20():
    ivesta20 = laukas20.get()
    rezultatas20["text"] = ivesta20

def spausdinti21():
    ivesta21 = laukas21.get()
    rezultatas21["text"] = ivesta21

def spausdinti22():
    ivesta22 = laukas22.get()
    rezultatas22["text"] = ivesta22

def spausdinti23():
    ivesta23 = laukas23.get()
    rezultatas23["text"] = ivesta23

def spausdinti24():
    ivesta24 = laukas24.get()
    rezultatas24["text"] = ivesta24

def spausdinti25():
    ivesta25 = laukas25.get()
    rezultatas25["text"] = ivesta25

def spausdinti26():
    ivesta26 = laukas26.get()
    rezultatas26["text"] = ivesta26

def spausdinti27():
    ivesta27 = laukas27.get()
    rezultatas27["text"] = ivesta27

def spausdinti28():
    ivesta28 = laukas28.get()
    rezultatas28["text"] = ivesta28

def spausdinti29():
    ivesta29 = laukas29.get()
    rezultatas29["text"] = ivesta29

def spausdinti30():
    ivesta30 = laukas30.get()
    rezultatas30["text"] = ivesta30

def spausdinti31():
    ivesta31 = laukas31.get()
    rezultatas31["text"] = ivesta31

def spausdinti32():
    ivesta32 = laukas32.get()
    rezultatas32["text"] = ivesta32

def spausdinti33():
    ivesta33 = laukas33.get()
    rezultatas33["text"] = ivesta33

def spausdinti34():
    ivesta34 = laukas34.get()
    rezultatas34["text"] = ivesta34

def spausdinti35():
    ivesta35 = laukas35.get()
    rezultatas35["text"] = ivesta35

def spausdinti36():
    ivesta36 = laukas36.get()
    rezultatas36["text"] = ivesta36

def spausdinti37():
    ivesta37 = laukas37.get()
    rezultatas37["text"] = ivesta37

def spausdinti38():
    ivesta38 = laukas38.get()
    rezultatas38["text"] = ivesta38

def spausdinti39():
    ivesta39 = laukas39.get()
    rezultatas39["text"] = ivesta39

def spausdinti40():
    ivesta40 = laukas40.get()
    rezultatas40["text"] = ivesta40

def spausdinti41():
    ivesta41 = laukas41.get()
    rezultatas41["text"] = ivesta41

def spausdinti42():
    ivesta42 = laukas42.get()
    rezultatas42["text"] = ivesta42

def spausdinti43():
    ivesta43 = laukas43.get()
    rezultatas43["text"] = ivesta43

def spausdinti44():
    ivesta44 = laukas44.get()
    rezultatas44["text"] = ivesta44

def spausdinti45():
    ivesta45 = laukas45.get()
    rezultatas45["text"] = ivesta45

def spausdinti46():
    ivesta46 = laukas46.get()
    rezultatas46["text"] = ivesta46

def spausdinti47():
    ivesta47= laukas47.get()
    rezultatas47["text"] = ivesta47

def spausdinti48():
    ivesta48 = laukas48.get()
    rezultatas48["text"] = ivesta48

instrukcija = Label(langas, text="Įvertinkite kievieną teiginį skalėje nuo 0 iki 10, kur 0  - visiškai nesutinku, labai blogai ir  10 - visiškai sutinku, labai gerai.")
slapyvardis = Label(langas, text="Jūsų slapyvardis yra: ")
laukas_slapyvardziui = Entry(langas)
scrollbaras = Scrollbar(langas)

klausimas1 = Label(langas, text="1. Apibendrintai, kiek esate patenkintas kaip darbuotojas, dirbdamas šioje kompanijoje? ")
klausimas2 = Label(langas, text="2. Įsivaizduokite tobulą darbo vietą: kaip arti tobulumo yra ši kompanija? ")
klausimas3 = Label(langas, text="3. Savo darbe aš jaučiuosi motyvuojamas ir motyvuotas. ")
klausimas4 = Label(langas, text="4. Aš visada pradedu darbą su džiaugsmu. ")
klausimas5 = Label(langas, text="5. Aš noriu dirbti šioje kompanijoje ateinančius 2 metus. ")
klausimas6 = Label(langas, text="6. Aš rekomenduočiau kitiems bandyti čia įsidarbinti. ")
klausimas7 = Label(langas, text="7. Aš esu iš tų, kuris(-i) visada deda papildomas pastangas darbui padaryti arba problemai išspręsti. ")
klausimas8 = Label(langas, text="8. Aš esu nusiteikęs(-usi) entuziastingai kompanijos ir savo užduočių atžvilgiu. ")
klausimas9 = Label(langas, text="9. Kompanija turi gerą vardą. ")
klausimas10 = Label(langas, text="10. Sakydamas(-a) kur dirbu - aš didžiuojuosi. ")
klausimas11 = Label(langas, text="11. Aplinkiniai žmonės įsivaizduoja šią kompaniją, kaip gerą vietą dirbti. ")
klausimas12 = Label(langas, text="12. Vadovybė aiškiai iškomunikuoja kompanijos strategiją ir tikslus. ")
klausimas13 = Label(langas, text="13. Vadovybė rodo gerą pavyzdį, kuriuo kiti nori sekti. ")
klausimas14 = Label(langas, text="14. Aš pasitikiu vadovybės sprendimais. ")
klausimas15 = Label(langas, text="15. Mano tiesioginis vadovas motyvuoja komandą viršyti lūkesčius. ")
klausimas16 = Label(langas, text="16. Mano tiesioginis vadovas sukuria darbo kultūrą komandoje, paremtą pasitikėjimu ir atvirumu. ")
klausimas17 = Label(langas, text="17. Mano tiesioginis vadovas pateikia konstruktyvias pastabas, kurios man padeda padaryti savo darbą gerai. ")
klausimas18 = Label(langas, text="18. Mano tiesioginis vadovas aiškiai paaiškino, koks turi būti mano indėlis komandai, kad pasiektume išsikeltus tikslus. ")
klausimas19 = Label(langas, text="19. Mano komandoje mes gerbiame ir pasitikime vienas kitu. ")
klausimas20 = Label(langas, text="20. Mano komandoje mes visi dirbame viena kryptimi, kad pasiektume tikslus. ")
klausimas21 = Label(langas, text="21. Mano komandoje visi rodo iniciatyvą, kad darbas būtų padarytas. ")
klausimas22 = Label(langas, text="22. Mano komanda puikiai sutaria su kitomis komandomis. ")
klausimas23 = Label(langas, text="23. Fizinės darbo sąlygos yra: ")
klausimas24 = Label(langas, text="24. Esu patenkinta(-s) darbo krūviu. ")
klausimas25 = Label(langas, text="25. Kompanija turi aiškius procesus ir suteikia geras priemones, padedančias dirbti efektyviau. ")
klausimas26 = Label(langas, text="26. Mano darbas man labai įdomus. ")
klausimas27 = Label(langas, text="27. Darbe susiduriu su įdomiais ir ne per sudėtingais įššūkiais. ")
klausimas28 = Label(langas, text="28. Šiame darbe geriausiai išnaudoju savo sugebėjimus. ")
klausimas29 = Label(langas, text="29. Esu motyvuota(-s)  priimti reikalingus sprendimus. ")
klausimas30 = Label(langas, text="30. Mano atlyginimas (įskaitant visus priedus), lyginant su tuo, ką galiu gauti kitur, yra: ")
klausimas31 = Label(langas, text="31. Mano kiti priedai (papildomos apmokamos atostogos, lankstus grafikas, motinystės/tėvystės atostogų lankstumas, ir kt.), lyginant su tuo, ką galiu gauti kitur, yra: ")
klausimas32 = Label(langas, text="32. Mano darbo vietos saugumas yra: ")
klausimas33 = Label(langas, text="33. Man yra aišku, kur savo darbe aš turiu tobulėti. ")
klausimas34 = Label(langas, text="34. Aš aktyviai ieškau tobulėjimo galimybių. ")
klausimas35 = Label(langas, text="35. Aš sulaukiu konstruktyvių pastabų iš savo komandos. ")
klausimas36 = Label(langas, text="36. Mano komandoje mes dažnai atvirai diskutuojame savo klaidas, tam, kad iš jų pasimokytume. ")
klausimas37 = Label(langas, text="37. Aš manau, kad kompanija man suteikia geras sąlygas tobulėti. ")
klausimas38 = Label(langas, text="38. Aš žinau kaip ir kur efektyviai pasidalinti savo abejonėmis ir įtarimais, jeigu įtariu kažką neteisingo ar neteisėto. ")
klausimas39 = Label(langas, text="39. Aš jaučiuosi ramiai, dalindamasi(-s) savo abejonėmis ir įtarimais, jeigu įtariu kažką neteisingo ar neteisėto. ")
klausimas40 = Label(langas, text="40. Aš visada pasidalinu savo abejonėmis ir įtarimais, jeigu įtariu kažką neteisingo ar neteisėto. ")
klausimas41 = Label(langas, text="41. Aš esu patenkinta(-s) darbo vietos lankstumu (darbas iš namų, ofiso, kitos lokacjos). ")
klausimas42 = Label(langas, text="42. Mano tiesioginis vadovas gerai subalansuoja darbuotojų asmeninius poreikius su darbo užduočių atlikimu. ")
klausimas43 = Label(langas, text="43. Aš turiu įgudžius ir galimybes dirbti iš betkurios lokacijos. ")
klausimas44 = Label(langas, text="44. Kompanijoje su manimi elgiamasi teisingai ir su pagarba, nepaisant mano lyties, tapatybės, amžiaus, tautybės, etniškumo, seksualinės pakraipos ir kt. ")
klausimas45 = Label(langas, text="45. Darbuotojų įvairovė yra vienas iš kompanijos prioritetų. ")
klausimas46 = Label(langas, text="46. Kompanijoje yra suteikiamos lygios galimybės visiems, nepaisant lyties, tapatybės, amžiaus, tautybės, etniškumo, seksualinės pakraipos ir kt.")
klausimas47 = Label(langas, text="47. Kompanijoje aš galiu būti savimi. ")

laukas1 = Entry(langas)
laukas2 = Entry(langas)
laukas3 = Entry(langas)
laukas4 = Entry(langas)
laukas5 = Entry(langas)
laukas6 = Entry(langas)
laukas7 = Entry(langas)
laukas8 = Entry(langas)
laukas9 = Entry(langas)
laukas10 = Entry(langas)
laukas11 = Entry(langas)
laukas12 = Entry(langas)
laukas13 = Entry(langas)
laukas14 = Entry(langas)
laukas15 = Entry(langas)
laukas16 = Entry(langas)
laukas17 = Entry(langas)
laukas18 = Entry(langas)
laukas19 = Entry(langas)
laukas20 = Entry(langas)
laukas21 = Entry(langas)
laukas22 = Entry(langas)
laukas23 = Entry(langas)
laukas24 = Entry(langas)
laukas25 = Entry(langas)
laukas26 = Entry(langas)
laukas27 = Entry(langas)
laukas28 = Entry(langas)
laukas29 = Entry(langas)
laukas30 = Entry(langas)
laukas31 = Entry(langas)
laukas32 = Entry(langas)
laukas33 = Entry(langas)
laukas34 = Entry(langas)
laukas35 = Entry(langas)
laukas36 = Entry(langas)
laukas37 = Entry(langas)
laukas38 = Entry(langas)
laukas39 = Entry(langas)
laukas40 = Entry(langas)
laukas41 = Entry(langas)
laukas42 = Entry(langas)
laukas43 = Entry(langas)
laukas44 = Entry(langas)
laukas45 = Entry(langas)
laukas46 = Entry(langas)
laukas47 = Entry(langas)
laukas48 = Entry(langas)

mygtukas1 = Button(langas, text="Patvirtinti", command=spausdinti)
mygtukas2 = Button(langas, text="Patvirtinti", command=spausdinti1)
mygtukas3 = Button(langas, text="Patvirtinti", command=spausdinti2)
mygtukas4 = Button(langas, text="Patvirtinti", command=spausdinti3)
mygtukas5 = Button(langas, text="Patvirtinti", command=spausdinti4)
mygtukas6 = Button(langas, text="Patvirtinti", command=spausdinti5)
mygtukas7 = Button(langas, text="Patvirtinti", command=spausdinti6)
mygtukas8 = Button(langas, text="Patvirtinti", command=spausdinti7)
mygtukas9 = Button(langas, text="Patvirtinti", command=spausdinti8)
mygtukas10 = Button(langas, text="Patvirtinti", command=spausdinti9)
mygtukas11 = Button(langas, text="Patvirtinti", command=spausdinti10)
mygtukas12 = Button(langas, text="Patvirtinti", command=spausdinti11)
mygtukas13 = Button(langas, text="Patvirtinti", command=spausdinti12)
mygtukas14 = Button(langas, text="Patvirtinti", command=spausdinti13)
mygtukas15 = Button(langas, text="Patvirtinti", command=spausdinti14)
mygtukas16 = Button(langas, text="Patvirtinti", command=spausdinti15)
mygtukas17 = Button(langas, text="Patvirtinti", command=spausdinti16)
mygtukas18 = Button(langas, text="Patvirtinti", command=spausdinti17)
mygtukas19 = Button(langas, text="Patvirtinti", command=spausdinti18)
mygtukas20 = Button(langas, text="Patvirtinti", command=spausdinti19)
mygtukas21 = Button(langas, text="Patvirtinti", command=spausdinti20)
mygtukas22 = Button(langas, text="Patvirtinti", command=spausdinti21)
mygtukas23 = Button(langas, text="Patvirtinti", command=spausdinti22)
mygtukas24 = Button(langas, text="Patvirtinti", command=spausdinti23)
mygtukas25 = Button(langas, text="Patvirtinti", command=spausdinti24)
mygtukas26 = Button(langas, text="Patvirtinti", command=spausdinti25)
mygtukas27 = Button(langas, text="Patvirtinti", command=spausdinti26)
mygtukas28 = Button(langas, text="Patvirtinti", command=spausdinti27)
mygtukas29 = Button(langas, text="Patvirtinti", command=spausdinti28)
mygtukas30 = Button(langas, text="Patvirtinti", command=spausdinti29)
mygtukas31 = Button(langas, text="Patvirtinti", command=spausdinti30)
mygtukas32 = Button(langas, text="Patvirtinti", command=spausdinti31)
mygtukas33 = Button(langas, text="Patvirtinti", command=spausdinti32)
mygtukas34 = Button(langas, text="Patvirtinti", command=spausdinti33)
mygtukas35 = Button(langas, text="Patvirtinti", command=spausdinti34)
mygtukas36 = Button(langas, text="Patvirtinti", command=spausdinti35)
mygtukas37 = Button(langas, text="Patvirtinti", command=spausdinti36)
mygtukas38 = Button(langas, text="Patvirtinti", command=spausdinti37)
mygtukas39 = Button(langas, text="Patvirtinti", command=spausdinti38)
mygtukas40 = Button(langas, text="Patvirtinti", command=spausdinti39)
mygtukas41 = Button(langas, text="Patvirtinti", command=spausdinti40)
mygtukas42 = Button(langas, text="Patvirtinti", command=spausdinti41)
mygtukas43 = Button(langas, text="Patvirtinti", command=spausdinti42)
mygtukas44 = Button(langas, text="Patvirtinti", command=spausdinti43)
mygtukas45 = Button(langas, text="Patvirtinti", command=spausdinti44)
mygtukas46 = Button(langas, text="Patvirtinti", command=spausdinti45)
mygtukas47 = Button(langas, text="Patvirtinti", command=spausdinti46)
mygtukas48 = Button(langas, text="Patvirtinti", command=spausdinti47)

rezultatas0 = Label(langas, text='')
rezultatas1 = Label(langas, text='')
rezultatas2 = Label(langas, text='')
rezultatas3 = Label(langas, text='')
rezultatas4 = Label(langas, text='')
rezultatas5 = Label(langas, text='')
rezultatas6 = Label(langas, text='')
rezultatas7 = Label(langas, text='')
rezultatas8 = Label(langas, text='')
rezultatas9 = Label(langas, text='')
rezultatas10 = Label(langas, text='')
rezultatas11 = Label(langas, text='')
rezultatas12 = Label(langas, text='')
rezultatas13 = Label(langas, text='')
rezultatas14 = Label(langas, text='')
rezultatas15 = Label(langas, text='')
rezultatas16 = Label(langas, text='')
rezultatas17 = Label(langas, text='')
rezultatas18 = Label(langas, text='')
rezultatas19 = Label(langas, text='')
rezultatas20 = Label(langas, text='')
rezultatas21 = Label(langas, text='')
rezultatas22 = Label(langas, text='')
rezultatas23 = Label(langas, text='')
rezultatas24 = Label(langas, text='')
rezultatas25 = Label(langas, text='')
rezultatas26 = Label(langas, text='')
rezultatas27 = Label(langas, text='')
rezultatas28 = Label(langas, text='')
rezultatas29 = Label(langas, text='')
rezultatas30 = Label(langas, text='')
rezultatas31 = Label(langas, text='')
rezultatas32 = Label(langas, text='')
rezultatas33 = Label(langas, text='')
rezultatas34 = Label(langas, text='')
rezultatas35 = Label(langas, text='')
rezultatas36 = Label(langas, text='')
rezultatas37 = Label(langas, text='')
rezultatas38 = Label(langas, text='')
rezultatas39 = Label(langas, text='')
rezultatas40 = Label(langas, text='')
rezultatas41 = Label(langas, text='')
rezultatas42 = Label(langas, text='')
rezultatas43 = Label(langas, text='')
rezultatas44 = Label(langas, text='')
rezultatas45 = Label(langas, text='')
rezultatas46 = Label(langas, text='')
rezultatas47 = Label(langas, text='')
rezultatas48 = Label(langas, text='')

uzrasas_aciu = Label(langas, text="Ačiū už atsakymus!")

instrukcija.grid(row=0, column=0)
slapyvardis.grid(row=1, column=0)
laukas_slapyvardziui.grid(row=1, column=1)

klausimas1.grid(row=2, column=0, sticky=W)
klausimas2.grid(row=3, column=0, sticky=W)
klausimas3.grid(row=4, column=0, sticky=W)
klausimas4.grid(row=5, column=0, sticky=W)
klausimas5.grid(row=6, column=0, sticky=W)
klausimas6.grid(row=7, column=0, sticky=W)
klausimas7.grid(row=8, column=0, sticky=W)
klausimas8.grid(row=9, column=0, sticky=W)
klausimas9.grid(row=10, column=0, sticky=W)
klausimas10.grid(row=11, column=0, sticky=W)
klausimas11.grid(row=12, column=0, sticky=W)
klausimas12.grid(row=13, column=0, sticky=W)
klausimas13.grid(row=14, column=0, sticky=W)
klausimas14.grid(row=15, column=0, sticky=W)
klausimas15.grid(row=16, column=0, sticky=W)
klausimas16.grid(row=17, column=0, sticky=W)
klausimas17.grid(row=18, column=0, sticky=W)
klausimas18.grid(row=19, column=0, sticky=W)
klausimas19.grid(row=20, column=0, sticky=W)
klausimas20.grid(row=21, column=0, sticky=W)
klausimas21.grid(row=22, column=0, sticky=W)
klausimas22.grid(row=23, column=0, sticky=W)
klausimas23.grid(row=24, column=0, sticky=W)
klausimas24.grid(row=25, column=0, sticky=W)
klausimas25.grid(row=26, column=0, sticky=W)
klausimas26.grid(row=27, column=0, sticky=W)
klausimas27.grid(row=28, column=0, sticky=W)
klausimas28.grid(row=29, column=0, sticky=W)
klausimas29.grid(row=30, column=0, sticky=W)
klausimas30.grid(row=31, column=0, sticky=W)
klausimas31.grid(row=32, column=0, sticky=W)
klausimas32.grid(row=33, column=0, sticky=W)
klausimas33.grid(row=34, column=0, sticky=W)
klausimas34.grid(row=35, column=0, sticky=W)
klausimas35.grid(row=36, column=0, sticky=W)
klausimas36.grid(row=37, column=0, sticky=W)
klausimas37.grid(row=38, column=0, sticky=W)
klausimas38.grid(row=39, column=0, sticky=W)
klausimas39.grid(row=40, column=0, sticky=W)
klausimas40.grid(row=41, column=0, sticky=W)
klausimas41.grid(row=42, column=0, sticky=W)
klausimas42.grid(row=43, column=0, sticky=W)
klausimas43.grid(row=44, column=0, sticky=W)
klausimas44.grid(row=45, column=0, sticky=W)
klausimas45.grid(row=46, column=0, sticky=W)
klausimas46.grid(row=47, column=0, sticky=W)
klausimas47.grid(row=48, column=0, sticky=W)

laukas1.grid(row=2, column=1)
laukas2.grid(row=3, column=1)
laukas3.grid(row=4, column=1)
laukas4.grid(row=5, column=1)
laukas5.grid(row=6, column=1)
laukas6.grid(row=7, column=1)
laukas7.grid(row=8, column=1)
laukas8.grid(row=9, column=1)
laukas9.grid(row=10, column=1)
laukas10.grid(row=11, column=1)
laukas11.grid(row=12, column=1)
laukas12.grid(row=13, column=1)
laukas13.grid(row=14, column=1)
laukas14.grid(row=15, column=1)
laukas15.grid(row=16, column=1)
laukas16.grid(row=17, column=1)
laukas17.grid(row=18, column=1)
laukas18.grid(row=19, column=1)
laukas19.grid(row=20, column=1)
laukas20.grid(row=21, column=1)
laukas21.grid(row=22, column=1)
laukas22.grid(row=23, column=1)
laukas23.grid(row=24, column=1)
laukas24.grid(row=25, column=1)
laukas25.grid(row=26, column=1)
laukas26.grid(row=27, column=1)
laukas27.grid(row=28, column=1)
laukas28.grid(row=29, column=1)
laukas29.grid(row=30, column=1)
laukas30.grid(row=31, column=1)
laukas31.grid(row=32, column=1)
laukas32.grid(row=33, column=1)
laukas33.grid(row=34, column=1)
laukas34.grid(row=35, column=1)
laukas35.grid(row=36, column=1)
laukas36.grid(row=37, column=1)
laukas37.grid(row=38, column=1)
laukas38.grid(row=39, column=1)
laukas39.grid(row=40, column=1)
laukas40.grid(row=41, column=1)
laukas41.grid(row=42, column=1)
laukas42.grid(row=43, column=1)
laukas43.grid(row=44, column=1)
laukas44.grid(row=45, column=1)
laukas45.grid(row=46, column=1)
laukas46.grid(row=47, column=1)
laukas47.grid(row=48, column=1)
laukas48.grid(row=49, column=1)

mygtukas1.grid(row=1, column=2)
mygtukas2.grid(row=2, column=2)
mygtukas3.grid(row=3, column=2)
mygtukas4.grid(row=4, column=2)
mygtukas5.grid(row=5, column=2)
mygtukas6.grid(row=6, column=2)
mygtukas7.grid(row=7, column=2)
mygtukas8.grid(row=8, column=2)
mygtukas9.grid(row=9, column=2)
mygtukas10.grid(row=10,	column=2)
mygtukas11.grid(row=11,	column=2)
mygtukas12.grid(row=12,	column=2)
mygtukas13.grid(row=13,	column=2)
mygtukas14.grid(row=14,	column=2)
mygtukas15.grid(row=15,	column=2)
mygtukas16.grid(row=16,	column=2)
mygtukas17.grid(row=17,	column=2)
mygtukas18.grid(row=18,	column=2)
mygtukas19.grid(row=19,	column=2)
mygtukas20.grid(row=20,	column=2)
mygtukas21.grid(row=21,	column=2)
mygtukas22.grid(row=22,	column=2)
mygtukas23.grid(row=23,	column=2)
mygtukas24.grid(row=24,	column=2)
mygtukas25.grid(row=25,	column=2)
mygtukas26.grid(row=26,	column=2)
mygtukas27.grid(row=27,	column=2)
mygtukas28.grid(row=28,	column=2)
mygtukas29.grid(row=29,	column=2)
mygtukas30.grid(row=30,	column=2)
mygtukas31.grid(row=31,	column=2)
mygtukas32.grid(row=32,	column=2)
mygtukas33.grid(row=33,	column=2)
mygtukas34.grid(row=34,	column=2)
mygtukas35.grid(row=35,	column=2)
mygtukas36.grid(row=36,	column=2)
mygtukas37.grid(row=37,	column=2)
mygtukas38.grid(row=38,	column=2)
mygtukas39.grid(row=39,	column=2)
mygtukas40.grid(row=40,	column=2)
mygtukas41.grid(row=41,	column=2)
mygtukas42.grid(row=42,	column=2)
mygtukas43.grid(row=43,	column=2)
mygtukas44.grid(row=44,	column=2)
mygtukas45.grid(row=45,	column=2)
mygtukas46.grid(row=46,	column=2)
mygtukas47.grid(row=47,	column=2)
mygtukas48.grid(row=48,	column=2)

rezultatas0.grid(row=1, column=3)
rezultatas1.grid(row=2, column=3)
rezultatas2.grid(row=3, column=3)
rezultatas3.grid(row=4, column=3)
rezultatas4.grid(row=5, column=3)
rezultatas5.grid(row=6, column=3)
rezultatas6.grid(row=7, column=3)
rezultatas7.grid(row=8, column=3)
rezultatas8.grid(row=9, column=3)
rezultatas9.grid(row=10, column=3)
rezultatas10.grid(row=11, column=3)
rezultatas11.grid(row=12, column=3)
rezultatas12.grid(row=13, column=3)
rezultatas13.grid(row=14, column=3)
rezultatas14.grid(row=15, column=3)
rezultatas15.grid(row=16, column=3)
rezultatas16.grid(row=17, column=3)
rezultatas17.grid(row=18, column=3)
rezultatas18.grid(row=19, column=3)
rezultatas19.grid(row=20, column=3)
rezultatas20.grid(row=21, column=3)
rezultatas21.grid(row=22, column=3)
rezultatas22.grid(row=23, column=3)
rezultatas23.grid(row=24, column=3)
rezultatas24.grid(row=25, column=3)
rezultatas25.grid(row=26, column=3)
rezultatas26.grid(row=27, column=3)
rezultatas27.grid(row=28, column=3)
rezultatas28.grid(row=29, column=3)
rezultatas29.grid(row=30, column=3)
rezultatas30.grid(row=31, column=3)
rezultatas31.grid(row=32, column=3)
rezultatas32.grid(row=33, column=3)
rezultatas33.grid(row=34, column=3)
rezultatas34.grid(row=35, column=3)
rezultatas35.grid(row=36, column=3)
rezultatas36.grid(row=37, column=3)
rezultatas37.grid(row=38, column=3)
rezultatas38.grid(row=39, column=3)
rezultatas39.grid(row=40, column=3)
rezultatas40.grid(row=41, column=3)
rezultatas41.grid(row=42, column=3)
rezultatas42.grid(row=43, column=3)
rezultatas43.grid(row=44, column=3)
rezultatas44.grid(row=45, column=3)
rezultatas45.grid(row=46, column=3)
rezultatas46.grid(row=47, column=3)
rezultatas47.grid(row=48, column=3)
rezultatas48.grid(row=49, column=3)


langas.mainloop()


conn = sqlite3.connect("Rezultatai2.db")

c = conn.cursor()

print("Įvertinkite kievieną teiginį skalėje nuo 0 iki 10, kur 0  - visiškai nesutinku, labai blogai ir  10 - visiškai sutinku, labai gerai.")
Slapyvardis = input("Jūsų slapyvardis yra: ")

klausimu_sarasas = [
"1. Apibendrintai, kiek esate patenkintas kaip darbuotojas, dirbdamas šioje kompanijoje? ",
"2. Įsivaizduokite tobulą darbo vietą: kaip arti tobulumo yra ši kompanija? ",
"3. Savo darbe aš jaučiuosi motyvuojamas ir motyvuotas. ",
"4. Aš visada pradedu darbą su džiaugsmu. ",
"5. Aš noriu dirbti šioje kompanijoje ateinančius 2 metus. ",
"6. Aš rekomenduočiau kitiems bandyti čia įsidarbinti. ",
"7. Aš esu iš tų, kuris(-i) visada deda papildomas pastangas darbui padaryti arba problemai išspręsti. ",
"8. Aš esu nusiteikęs(-usi) entuziastingai kompanijos ir savo užduočių atžvilgiu. ",
"9. Kompanija turi gerą vardą. ",
"10. Sakydamas(-a) kur dirbu - aš didžiuojuosi. ",
"11. Aplinkiniai žmonės įsivaizduoja šią kompaniją, kaip gerą vietą dirbti. ",
"12. Vadovybė aiškiai iškomunikuoja kompanijos strategiją ir tikslus. ",
"13. Vadovybė rodo gerą pavyzdį, kuriuo kiti nori sekti. ",
"14. Aš pasitikiu vadovybės sprendimais. ",
"15. Mano tiesioginis vadovas motyvuoja komandą viršyti lūkesčius. ",
"16. Mano tiesioginis vadovas sukuria darbo kultūrą komandoje, paremtą pasitikėjimu ir atvirumu. ",
"17. Mano tiesioginis vadovas pateikia konstruktyvias pastabas, kurios man padeda padaryti savo darbą gerai. ",
"18. Mano tiesioginis vadovas aiškiai paaiškino, koks turi būti mano indėlis komandai, kad pasiektume išsikeltus tikslus. ",
"19. Mano komandoje mes gerbiame ir pasitikime vienas kitu. ",
"20. Mano komandoje mes visi dirbame viena kryptimi, kad pasiektume tikslus. ",
"21. Mano komandoje visi rodo iniciatyvą, kad darbas būtų padarytas. ",
"22. Mano komanda puikiai sutaria su kitomis komandomis. ",
"23. Fizinės darbo sąlygos yra: ",
"24. Esu patenkinta(-s) darbo krūviu. ",
"25. Kompanija turi aiškius procesus ir suteikia geras priemones, padedančias dirbti efektyviau. ",
"26. Mano darbas man labai įdomus. ",
"27. Darbe susiduriu su įdomiais ir ne per sudėtingais įššūkiais. ",
"28. Šiame darbe geriausiai išnaudoju savo sugebėjimus. ",
"29. Esu motyvuota(-s)  priimti reikalingus sprendimus. ",
"30. Mano atlyginimas (įskaitant visus priedus), lyginant su tuo, ką galiu gauti kitur, yra: ",
"31. Mano kiti priedai (papildomos apmokamos atostogos, lankstus grafikas, motinystės/tėvystės atostogų lankstumas, ir kt.), lyginant su tuo, ką galiu gauti kitur, yra: ",
"32. Mano darbo vietos saugumas yra: ",
"33. Man yra aišku, kur savo darbe aš turiu tobulėti. ",
"34. Aš aktyviai ieškau tobulėjimo galimybių. ",
"35. Aš sulaukiu konstruktyvių pastabų iš savo komandos. ",
"36. Mano komandoje mes dažnai atvirai diskutuojame savo klaidas, tam, kad iš jų pasimokytume. ",
"37. Aš manau, kad kompanija man suteikia geras sąlygas tobulėti. ",
"38. Aš žinau kaip ir kur efektyviai pasidalinti savo abejonėmis ir įtarimais, jeigu įtariu kažką neteisingo ar neteisėto. ",
"39. Aš jaučiuosi ramiai, dalindamasi(-s) savo abejonėmis ir įtarimais, jeigu įtariu kažką neteisingo ar neteisėto. ",
"40. Aš visada pasidalinu savo abejonėmis ir įtarimais, jeigu įtariu kažką neteisingo ar neteisėto. ",
"41. Aš esu patenkinta(-s) darbo vietos lankstumu (darbas iš namų, ofiso, kitos lokacjos). ",
"42. Mano tiesioginis vadovas gerai subalansuoja darbuotojų asmeninius poreikius su darbo užduočių atlikimu. ",
"43. Aš turiu įgudžius ir galimybes dirbti iš betkurios lokacijos. ",
"44. Kompanijoje su manimi elgiamasi teisingai ir su pagarba, nepaisant mano lyties, tapatybės, amžiaus, tautybės, etniškumo, seksualinės pakraipos ir kt. ",
"45. Darbuotojų įvairovė yra vienas iš kompanijos prioritetų. ",
"46. Kompanijoje yra suteikiamos lygios galimybės visiems, nepaisant lyties, tapatybės, amžiaus, tautybės, etniškumo, seksualinės pakraipos ir kt.",
"47. Kompanijoje aš galiu būti savimi. "]


with conn:
    c.execute("CREATE TABLE IF NOT EXISTS Rezultatai (Slapyvardis TEXT, Atsakymai INTEGER)")

    for a in klausimu_sarasas:
        print(a)
        while True:
            atsakymas = int(input("Įveskite skaičių nuo 0 iki 10: "))
            if atsakymas < 10 and atsakymas > 0:
            # print("Keliaukime toliau")
                break
        #kaip padaryti, kad nieko neivedus prasytu bandyti dar karta?
        # and not atsakymas:
        #     raise ValueError
        #     print("Nieko")
        # except ValueError:
        #     print("Nieko")
            else:
                print("Įvedėte negalimą vertę. Bandykite dar kartą.")

        with conn:
            c.execute(f"INSERT INTO Rezultatai VALUES ('{Slapyvardis}', '{atsakymas}')")

        with conn: #atsispausdinam visa lentele
            c.execute("SELECT * FROM Rezultatai")
            print(c.fetchall())

    # with conn: #atsispausdinam tik konkretu irasa
    #     c.execute("SELECT * FROM Rezultatai WHERE Slapyvardis = 'dfghfhgf'")
    #     print(c.fetchall())


print("Ačiū už atsakymus!")