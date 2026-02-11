def berechne_durchschnitt(notEN_liste):
    if len(notEN_liste) == 0:
        return 0
    return sum(notEN_liste) / len(notEN_liste)
    
def bewerte_note(durchschnitt):
    if durchschnitt <= 1.5:
        return "Sehr gut"
    elif durchschnitt <= 2.5:
        return "Gut"
    elif durchschnitt <= 3.5:
        return "Befriedigend"
    elif durchschnitt <= 4.5:
        return "Ausreichend"
    else:
        return "Nicht bestanden"
    
   
def main():
    print("Notenberechnung! (Schreibe ende für Programm beenden)")
    
    noten = []
    
    while True:
        benutzer_eingabe = input("Geben Sie ihre Note zwischen 1 - 6 ein!: ")
        
        if benutzer_eingabe.lower() == "ende":
            if noten:
                durchschnitt = berechne_durchschnitt(noten)
                bewertung = bewerte_note(durchschnitt)
                print(f"Durchschnitt: {durchschnitt:.2f}")
                print(f"Bewertung: {bewertung}")
            else:
                print("Es wurden keine Noten eingegeben")
            
            print("Programm beendet")
            break
        
        try:
            note = int(benutzer_eingabe)
            if note < 1 or note > 6:
                print("Bitte eine Note zwischen 1 und 6 eingeben")
                continue
          
            noten.append(note)
            
        except ValueError:
            print("Bitte eine gültige Zahl oder 'ende' eingeben!")
    


if __name__ == "__main__":
    main()