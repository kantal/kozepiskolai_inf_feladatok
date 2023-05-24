#!/usr/bin/env python3
# utemez_extra.py
# Érettségi feladat - digitális kultúra, emelt szint: 2023. május, Ütemezés
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023


fn_adatok= "taborok.txt"

#--- 5. feladat
def sorszám( hónap, nap):
    # jún. 16-tól aug. 31-ig
    hó_napjai= ( 30-16+1, 31, 31)
    if hónap == 6:
        return nap - 16 +1

    return sum( hó_napjai[ :hónap-6] ) + nap

# teszt
#print( "\nteszt", sorszám( 6,16), sorszám( 8,31))


#--- 1. feladat
Táborok= []
zeneiTáborok= []
maxJelentkező= 0

with open( fn_adatok) as ff:

    for sor in ff:

        sor= sor.strip()
        if not sor:
            continue

        hó1,nap1,hó2,nap2,nevek,téma = sor.split()
        ts1= sorszám( int(hó1), int(nap1) )
        ts2= sorszám( int(hó2), int(nap2) )
        Táborok.append( [ ts1, ts2, hó1, nap1, hó2, nap2, nevek, téma ] )

        if "zenei" in téma:
            zeneiTáborok.append( (hó1,nap1) )

        maxjel= len( nevek)
        if maxjel > maxJelentkező:
            maxJelentkező= maxjel


#print( *Táborok, sep="\n")    # szemrevételezés


#--- 2. feladat
print( "\n2. feladat\nAz adatsorok száma:", len(Táborok) )
print( "Az először rögzített tábor témája:", Táborok[0][-1] )
print( "Az utoljára rögzített tábor témája:",  Táborok[-1][-1] )


#--- 3. feladat
print( "\n3. feladat")
if zeneiTáborok:
    for hó, nap in zeneiTáborok:
        print( f"Zenei tábor kezdődik {hó}. hó {nap}. napján.")
else:
    print( "Nem volt zenei tábor.")


#--- 4. feladat
print( "\n4. feladat")
print( "Legnépszerűbbek:")

for ts1, ts2, hó1,nap1,hó2,nap2,nevek,téma in Táborok:

    if maxJelentkező == len(nevek):
        print( hó1, nap1, téma )


#--- 6. feladat
print( "\n6. feladat")
bekértHó= int( input( "hó: "))
bekértNap= int( input( "nap: "))
sorszIdőpont= sorszám( bekértHó, bekértNap)

táborok_száma= 0
for ts1,ts2,hó1,nap1,hó2,nap2,nevek,téma  in Táborok:
    if ts1 <= sorszIdőpont <= ts2:
        táborok_száma += 1

print( f"Ekkor éppen {táborok_száma} tábor tart.")


#--- 7. feladat
fn_tanuló= "egytanulo.txt"
print( "\n7. feladat")

tanuló= input( "Adja meg egy tanuló betűjelét: ").strip().upper()

# ts1,ts2,hó1,nap1,hó2,nap2,nevek,téma
camps= [ bejegyzés  for bejegyzés in Táborok if tanuló in bejegyzés[-2] ]
camps= sorted( camps, key= lambda bejegyzés: bejegyzés[0] )

#print( *camps, sep="\n")    # szemrevételezés

átfedés= False
sorszElőzőVége= 0
with open( fn_tanuló, "w") as ff:

    for ts1,ts2,hó1,nap1,hó2,nap2,nevek,téma in camps:

        if not átfedés:
            if ts1 <= sorszElőzőVége:
                átfedés= True
            else:
                sorszElőzőVége= ts2

        ff.write( f"{hó1}.{nap1}-{hó2}.{nap2}. {téma}\n")

if not átfedés:
    print( "Mindegyik táborba elmehet")
else:
    print( "Nem mehet el mindegyik táborba.")

#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben

