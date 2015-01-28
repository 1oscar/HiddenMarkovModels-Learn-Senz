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

# print s.hHiddenState
# print len(s.hHiddenState)
# print s.hVisibleOutput
# print len(s.hVisibleOutput)
# print s.hTransitionP
# print s.hEmissionP
# print s.hPi

utility.Utility.printEmissionMatrix(s.getEmission())
utility.Utility.printTransitionMatrix(s.getTransition())


s.initTrainSample([{'motion': 'RUNNING', 'no': 17, 'location': 'COMMUNITY', 'time': 'AFTERNOON'},
                   {'motion': 'SITTING', 'no': 12, 'location': 'SHOPPING', 'time': 'AFTERNOON'}])

s.BaumWelchLearn(0.01)
s.ViterbiDecode()

utility.Utility.printEmissionMatrix(s.getEmission())
utility.Utility.printTransitionMatrix(s.getTransition())

print s.getQ()