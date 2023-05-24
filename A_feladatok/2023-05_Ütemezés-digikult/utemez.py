#!/usr/bin/env python3
# utemez.py
# Érettségi feladat - digitális kultúra, emelt szint: 2023. május, Ütemezés
# Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
# Program: Koós Antal, 2023

fn_adatok= "taborok.txt"

Táborok= []
with open( fn_adatok) as ff:

    for sor in ff:

        sor= sor.strip()
        if not sor:
            continue

        hó1,nap1,hó2,nap2,nevek,téma = sor.split()
        Táborok.append( [ int(hó1), int(nap1), int(hó2), int(nap2), nevek, téma ] )

#print( *Táborok, sep="\n")    # szemrevételezés


#--- 2. feladat
print( "\n2. feladat\nAz adatsorok száma:", len(Táborok) )
print( "Az először rögzített tábor témája:", Táborok[0][-1] )
print( "Az utoljára rögzített tábor témája:",  Táborok[-1][-1] )


#--- 3. feladat
print( "\n3. feladat")
van_zenei= False
for hó1,nap1,hó2,nap2,nevek,téma in Táborok:

    if "zenei" in téma:
        print( f"Zenei tábor kezdődik {hó1}. hó {nap1}. napján.")
        van_zenei= True

if not van_zenei:
    print( "Nem volt zenei tábor.")


#--- 4. feladat
print( "\n4. feladat")
print( "Legnépszerűbbek:")
legNépszerűbb= max( Táborok, key= lambda bejegyzés: len( bejegyzés[-2]) )
maxJelentkező= len( legNépszerűbb[-2])

for hó1,nap1,hó2,nap2,nevek,téma in Táborok:

    if maxJelentkező == len(nevek):
        print( hó1, nap1, téma )


#--- 5. feladat
def sorszám( hónap, nap):
    # jún. 16-tól aug. 31-ig
    hó_napjai= ( 30-16+1, 31, 31)
    if hónap == 6:
        return nap - 16 +1

    return sum( hó_napjai[ :hónap-6] ) + nap

# teszt
#print( "\nteszt", sorszám( 6,16), sorszám( 8,31))


#--- 6. feladat
print( "\n6. feladat")
bekértHó= int( input( "hó: "))
bekértNap= int( input( "nap: "))
sorszIdőpont= sorszám( bekértHó, bekértNap)

táborok_száma= 0
for hó1,nap1,hó2,nap2,nevek,téma  in Táborok:
    if sorszám( hó1,nap1) <= sorszIdőpont <= sorszám( hó2,nap2):
        táborok_száma += 1

print( f"Ekkor éppen {táborok_száma} tábor tart.")


#--- 7. feladat
fn_tanuló= "egytanulo.txt"
print( "\n7. feladat")

tanuló= input( "Adja meg egy tanuló betűjelét: ").strip().upper()

camps= [ [hó1,nap1,hó2,nap2,téma]  for hó1,nap1,hó2,nap2,nevek,téma in Táborok if tanuló in nevek ]
camps= sorted( camps, key= lambda t: sorszám( t[0],t[1]) )

#print( *camps, sep="\n")    # szemrevételezés

átfedés= False
sorszElőzőVége= 0
with open( fn_tanuló, "w") as ff:

    for hó1,nap1,hó2,nap2,téma in camps:

        if not átfedés:
            if sorszám( hó1,nap1) <= sorszElőzőVége:
                átfedés= True
            else:
                sorszElőzőVége= sorszám(hó2,nap2)

        ff.write( f"{hó1}.{nap1}-{hó2}.{nap2}. {téma}\n")

if not átfedés:
    print( "Mindegyik táborba elmehet")
else:
    print( "Nem mehet el mindegyik táborba.")


#---------------------------------------------------------------------------
# További feladatok: https://github.com/kantal/kozepiskolai_inf_feladatok
# Ajánlott könyv:    Koós Antal: Python a gépben

