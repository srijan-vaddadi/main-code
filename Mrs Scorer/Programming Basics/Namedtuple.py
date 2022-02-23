from collections import namedtuple

Pet_nt = namedtuple('Pet_nt','id name species owner snack')

my_pet = Pet_nt(1,'Escanor','Pegasus','Zeus','Cheese')
other_pet = Pet_nt(2,'Aragog','Spider','Hagrid','Humans')
other_pet2 = Pet_nt(3,'Squish','Unknown','Unknown','Human')

print(my_pet.name, 'is owned by', my_pet.owner)

def printout():
    layout = '|{0:<10}|{1:10}|{2:10}|{3:10}|{4:10}|'
    print(layout.format('ID','Name','Species','Owner','Food'))
    print(layout.format('-'*10,'-'*10,'-'*10,'-'*10,'-'*10))
    for pet in (my_pet, other_pet, other_pet2):
        print(layout.format(pet.id,pet.name,pet.species,pet.owner,pet.snack))
printout()