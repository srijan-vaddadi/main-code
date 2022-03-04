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


