__author__ = 'woodie'

import hmm_senz.core.senz as senz
import hmm_senz.utility.utility as utility

# "WORK", "LIVE", "RELAX", "ENTERTAIN", "EXERCISE"
pi = [0.6, 0.25, 0.1, 0.04, 0.01]
#
transition_init = [[0.2, 0.2, 0.2, 0.2, 0.2],
                   [0.2, 0.2, 0.2, 0.2, 0.2],
                   [0.2, 0.2, 0.2, 0.2, 0.2],
                   [0.2, 0.2, 0.2, 0.2, 0.2],
                   [0.2, 0.2, 0.2, 0.2, 0.2]]
emission_init   = [[0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037],
                   [0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037],
                   [0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037],
                   [0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037],
                   [0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037, 0.037]]

s = senz.Senz(pi, transition_init, emission_init)

u = utility.Utility(s)
u.printTransitionMatrix()
u.printEmissionMatrix()
u.printHiddenState()
u.printVisibleOutput()

s.initTrainSample([{'motion': 'RUNNING', 'location': 'COMMUNITY', 'time': 'AFTERNOON'},
                   {'motion': 'SITTING', 'location': 'SHOPPING', 'time': 'AFTERNOON'}])

s.BaumWelchLearn(0.01)
s.ViterbiDecode()

u.printTransitionMatrix()
u.printEmissionMatrix()
u.printHiddenState()
u.printVisibleOutput()

print s.getQ()