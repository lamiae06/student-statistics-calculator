from stats import   somme, moyenne, variance, ecart_type, coefficient_variation   


print("Enter les notes des 5 étudiants : \n")

note1 = int(input("note 1 : "))
note2 = int(input("note 2 : "))
note3 = int(input("note 3 : "))
note4 = int(input("note 4 : "))
note5 = int(input("note 5 : "))

print("\nRésultats :")


print("la somme de 5 étudiants est : ", somme(note1, note2, note3, note4, note5))
print("la moyenne de 5 étudiants est : ", moyenne(note1, note2, note3, note4, note5))
print("la variance de 5 étudiants est : ", variance(note1, note2, note3, note4, note5))
print("l'écart type de 5 étudiants est : ", ecart_type(note1, note2, note3, note4, note5))
print("le coefficient de variation de 5 étudiants est : ", coefficient_variation(note1, note2, note3, note4, note5))



