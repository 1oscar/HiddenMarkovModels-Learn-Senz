__author__ = 'woodie'

import hmm_senz.core.senz as senz
import hmm_senz.hmm.hmm as hmm

pi = [0.2, 0.3, 0.5]

visible_output  = ("HOT", "COLD")
hidden_state    = ("WINDY", "SUNNY", "RAINNY")

transition_init = [[0.333, 0.666, 0], [0.2, 0.3, 0.5], [0.333, 0.333, 0.333]]
emission_init   = [[0.5, 0.5], [0.75, 0.25], [0.25, 0.75]]

s = senz.Senz(pi, transition_init, emission_init)

print s.hHiddenState
print s.hVisibleOutput
print s.hTransitionP
print s.hEmissionP
print s.hPi
# HMM = hmm.HMM(
#     visible_output,
#     hidden_state,
#     pi,
#     transition_init,
#     emission_init
# )