prix_Eau=500
prix_Jus=1000
prix_Soda=1500
print("="*30)
print(f"1 :l'eau est à   :{prix_Eau} FCFA")
print(f"2 :le Jus est à  :{prix_Jus} FCFA")
print(f"3 :le Soda est à :{prix_Soda} FCFA")
print("="*30)

demande=input("Choisissez ce que vous voulez monsieur : 1-Eau ,2-Jus ,3-Soda  :")
if demande in ["1","2","3"]:
    mon_argent=int(input("Entrez votre argent :"))
    
    if demande=='1':
        if mon_argent>=prix_Eau:
            print("Eau distribué")
            monnaie=mon_argent-prix_Eau
        else:
            print("Argent insuffisent")
    elif demande=='2':  
        if mon_argent>=prix_Jus:
            print("Jus distribué")
            monnaie=mon_argent-prix_Jus
        else:
            print("Argent insuffisent")
    elif demande=='3':
        if mon_argent>=prix_Soda:
            print("Soda distribué")
            monnaie=mon_argent-prix_Soda
        else:
            print("Argent insuffisent")
    print("Solde restant :",monnaie)
else:
    print("Choix invalide")
