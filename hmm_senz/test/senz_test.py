__author__ = 'woodie'

import hmm_senz.core.senz as senz
import hmm_senz.utility.utility as utility

# "WORK", "LIVE", "RELAX", "ENTERTAIN", "EXERCISE"
pi = [0.6, 0.05, 0.05, 0.2, 0.1]
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


s = senz.Senz()
s.initHMMParam(pi, transition_init, emission_init)

u = utility.Utility(s)
u.printTransitionMatrix()
u.printEmissionMatrix()
u.printHiddenState()
u.printVisibleOutput()

s.initTrainSample([{'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'}
                   ])

s.BaumWelchLearn(0.01)
s.ViterbiDecode()

u.printTransitionMatrix()
u.printEmissionMatrix()
u.printHiddenState()
u.printVisibleOutput()

print s.getQ()