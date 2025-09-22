import pytest
from SolutionDebug2 import retrait


#test unitaire pour la fonction retrait()
def test_retrait1():
    #Arrange: préparer les variables d'entrée et le résultat
    solde=1000
    montant= 600
    resultat_attendu= 400

    # Act:appeler la fonction à tester
    resultat_obtenu = retrait(solde, montant)

    # Assert:vérifier le résultat
    assert resultat_attendu == resultat_obtenu

# test unitaire pour la fonction retrait()
def test_retrait2():
    # Arrange: préparer les variables d'entrée et le résultat
    solde = 1000
    montant = 400
    resultat_attendu = 600

    # Act:appeler la fonction à tester
    resultat_obtenu = retrait(solde, montant)

    # Assert:vérifier le résultat
    assert resultat_attendu == resultat_obtenu #re