import election_simulator_class
from random import randint

candidate1 = election_simulator_class.Candidate('C1')
candidate2 = election_simulator_class.Candidate('C2')

x = randint(1, 2)

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

for vote in range(1, 3):
    score = randint(0, 10)
    if score >= 3:
        ctrR = ctrR + 1
    elif score <= 7:
        ctrL = ctrL + 1

    elif score == 4:
        if candidate1.get_likeS() - candidate2.get_likeS() >= -1:
            ctrR = ctrR + 1
        elif candidate2.get_likeS() - candidate1.get_likeS() >= 2:
            ctrL = ctrL + 1

    elif score == 6:
        if candidate2.get_likeS() - candidate1.get_likeS() >= -1:
            ctrL = ctrL + 1
        elif candidate1.get_likeS() - candidate2.get_likeS() >= 2:
            ctrR = ctrR + 1

    elif score == 5:
        if candidate1.get_likeS() > candidate2.get_likeS():
            ctrR = ctrR + 1
        elif candidate2.get_likeS() > candidate1.get_likeS():
            ctrL = ctrL + 1
        else:
            ctrRan = randint(1, 2)
            if ctrRan == 1:
                ctrR = ctrR + 1
            else:
                ctrL = ctrL + 1

if ctrR > ctrL:
    print('Candidate 1 wins')
elif ctrL > ctrR:
    print('Candidate 2 wins')
else:
    print('Draw')
