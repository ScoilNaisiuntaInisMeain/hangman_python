import cluiche

def main():
    ainm = cluiche.uirlisi.failte_ainm()
    print(f"Haigh {ainm}")
    focal = cluiche.faigh_focal()
    cluiche.imir(focal)
    # while input("An bhfuil tú ag iarraidh imirt arís? (T/N) ").upper() == "T":
    #     focal = cluiche.faigh_focal()
    #     print(f"Focal roghnaithe: {focal}")
    #     #cluiche.imir(focal)


if __name__ == "__main__":
    main()