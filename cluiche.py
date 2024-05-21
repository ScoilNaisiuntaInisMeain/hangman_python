import uirlisi
import random

tomhais_iomlan = 6

# cuirfimid na feidhmeanna don chluiche anseo
# # 1. cuir fáilte rompu, tóg a ainm
# # 2. ríomhaire ag piocadh focal (plainéad) [p,l,a,i,n,é,a,d]
# # 3. tóg focal ón imreoir (capalíní) [c,a,p,a,l,í,n,í]
# 3+.déan scrúdú ar an bhfocal roghnaithe
# 4. déan comparáid leis an focal atá roghnaithe ag an gcluiche
# 5. _ _ _ _ _ _ _ _ ->
# a) áit ceart, b) áit mícheart, c) mícheart
# focal ró-ghearr/ró-fhada -> micheart, iontráil focal leis an méid ceart (len(focal))
# 6. * (a) (p) (a) (l) * (n) *
# 7. tomhais_togtha + 1
# 8. print amach tomhais_iomlan - tomhais_togtha = céim hangman
#

focail = ["úlla", "mucín", "séabra", "focal", "bó", "nóinín", "pabhsaer", "cnaipíní", "sicín"]


def faigh_focal() -> str:
    max = len(focail) - 1
    uimhir_random = random.randint(0, max)
    focal = focail[uimhir_random]
    return focal


def imir(focal: str):
    tomhas = faigh_tomhas(focal)
    comhar = 0
    ceart = False
    tomhais_fagtha = tomhais_iomlan - comhar
    print(uirlisi.taispean_crochadoir(tomhais_fagtha))
    while not ceart and comhar < tomhais_iomlan:
        ceart = comparaid(tomhas, focal)
        if (ceart):
            print("Maith thú!")
        else:
            tomhais_fagtha = tomhais_iomlan - comhar
            print(uirlisi.taispean_crochadoir(tomhais_fagtha))
            comhar = comhar + 1
            tomhas = faigh_tomhas(focal)
    if (not ceart):
        print("Mí-ádh! Té ar ais ar scoil!")


def comparaid(tomhas: str, focal: str):
    print(f"do thomhas: {tomhas}")
    litreacha_tomhas = list(tomhas)
    litreacha_focal = list(focal)
    comhar_ceart = 0
    eolas = ""
    # do gach litir sa bhfocal tomhas, abair leis an úsadóir an raibh sé ceart/micheart/san áit micheart
    for rud in litreacha_tomhas:
        try:
            ait = litreacha_focal.index(rud)
        except:
            ait = -1
        tomhas_ait = litreacha_tomhas.index(rud)
        if (ait < 0):
            eolas = eolas +"*"
        elif (ait == tomhas_ait):
            eolas = eolas +rud
            comhar_ceart += 1
        elif (ait != tomhas_ait):
            eolas = eolas +rud.upper()
    print(eolas)
    if (len(focal) == comhar_ceart):
        return True
    return False

def faigh_tomhas(focal_roghnaithe: str) -> str:
    focal = focal_roghnaithe
    print("Cad é do thomhais?")
    passail = False
    tomhas = ""
    while (passail == False):
        tomhas = input()
        passail = scrudaigh(focal, tomhas)
        if (passail != True):
            print("Tomhais arís!")
    return tomhas


def scrudaigh(focal: str, tomhas: str) -> bool:
    fad_tomhais = len(tomhas)
    fad_focal = len(focal)
    if (fad_tomhais < fad_focal):
        difriocht = fad_focal - fad_tomhais
        print(f"Roghnaigh focal atá {difriocht} níos faide")
        return False
    elif (fad_tomhais > fad_focal):
        difriocht = fad_tomhais - fad_focal
        print(f"Roghnaigh focal atá {difriocht} níos lú")
        return False
    return True
