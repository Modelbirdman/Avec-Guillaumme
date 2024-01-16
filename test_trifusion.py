import trifusion

L1=[1,4,5]
L2=[3,6,7]
def test_fusion():
    assert trifusion.trimerge(L1+L2)==[1,3,4,5,6,7]



L=[6,5,4,2]
def test_tri():
    assert trifusion.trimerge(L)==[2,4,5,6]


   
def lire_fichier_adn(chemin_fichier): # On extrait les lignes du fichierADN
    try:
        with open(chemin_fichier, 'r') as fichier:
            # Lire le contenu du fichier
            contenu = fichier.read()

            # Diviser le contenu en lignes
            lignes = contenu.split('\n')

            # Filtrer les lignes vides
            lignes_non_vides = [ligne.strip() for ligne in lignes if ligne.strip()]

            return lignes_non_vides
    except FileNotFoundError:
        print(f"Le fichier '{chemin_fichier}' n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return []

L_test=lire_fichier_adn('\Users\alexis\Documents\école\première année\projet maths\repo git\Avec-Guillaumme\wordstosort.txt' )
L_sortie=lire_fichier_adn('\Users\alexis\Documents\école\première année\projet maths\repo git\Avec-Guillaumme\sorted_words.txtcrdownload')
print(L_test)
print(L_sortie)
str='zeti'
def test_tri_str():
    assert trifusion.trimerge(list(str))==list('eitz')