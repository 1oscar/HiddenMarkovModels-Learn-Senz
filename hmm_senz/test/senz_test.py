__author__ = 'woodie'

import hmm_senz.core.senz as senz
import hmm_senz.utility.utility as utility

# "WORK", "LIVE", "RELAX", "ENTERTAIN", "EXERCISE"
pi = [0.2, 0.2, 0.2, 0.2, 0.2]
#
transition_init = [[0.1, 0.2, 0.2, 0.2, 0.2],
                   [0.2, 0.2, 0.2, 0.2, 0.2],
                   [0.3, 0.2, 0.2, 0.2, 0.2],
                   [0.4, 0.2, 0.2, 0.2, 0.2],
                   [0.5, 0.2, 0.2, 0.2, 0.2]]
emission_init   = [[0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037],
                   [0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037],
                   [0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037],
                   [0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037],
                   [0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037]]


s = senz.Senz()

u = utility.Utility(s)
u.printTransitionMatrix()
u.printEmissionMatrix()
u.printHiddenState()
u.printVisibleOutput()

s.initHMMParam(pi, transition_init, emission_init)




s.initTrainSample([{'motion': 'RUNNING', 'location': 'COMMUNITY', 'time': 'AFTERNOON'},
                   {'motion': 'SITTING', 'location': 'SHOPPING', 'time': 'AFTERNOON'}])

s.BaumWelchLearn(0.01)
s.ViterbiDecode()

u.printTransitionMatrix()
u.printEmissionMatrix()
u.printHiddenState()
u.printVisibleOutput()

print s.getQ()