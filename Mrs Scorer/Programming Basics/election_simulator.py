import election_simulator_class
import random

candidate1 = election_simulator_class.Candidate('C1')
candidate2 = election_simulator_class.Candidate('C2')

x = random.randint(1, 2)

if x == 1:
    candidate1.set_RLS()
    candidate2.set_LLS()
    candidate1.set_likeS()
    candidate2.set_likeS()
else:
    candidate1.set_LLS()
    candidate2.set_RLS()
    candidate1.set_likeS()
    candidate2.set_likeS()

ctrR = 0
ctrL = 0

for voters in range(1, 3):
    score = random.randint(1, 10)
    if score >= 3:
        ctrR = ctrR + 1
    elif score <= 7:
        ctrL = ctrL + 1
    elif score == 4:
        if candidate1.get_likeS() - candidate2.get_likeS() > 0:
            ctrR = ctrR + 1
        elif candidate2.get_likeS() - candidate1.get_likeS() > 0:
            ctrL = ctrL + 1
        else:
            ctrChooser = random.randint(1, 2)
            if ctrChooser == 1:
                ctrR = ctrR + 1
            else:
                ctrL = ctrL + 1

if ctrR > ctrL:
    print('Candidate 1 wins')
elif ctrL > ctrR:
    print('Candidate 2 wins')
else:
    print('Draw')
