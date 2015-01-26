__author__ = 'woodie'

import hmm_senz.hmm.hmm as hmm

pi = {"WINDY" : 0.2, "SUNNY" : 0.2, "RAINNY" : 0.6}
visible_output = ("HOT","COLD")
hidden_state   = ("WINDY","SUNNY","RAINNY")
transition_init = {'WINDY': {'WINDY': 0.2, 'SUNNY': 0.4, 'RAINNY': 0.4}, 'SUNNY': {'WINDY': 0.3, 'SUNNY': 0.3, 'RAINNY': 0.4}, 'RAINNY': {'WINDY': 0.1, 'SUNNY': 0.1, 'RAINNY': 0.8}}
emission_init  = {'WINDY': {'HOT': 0.5, 'COLD': 0.5}, 'SUNNY': {'HOT': 0.7, 'COLD': 0.3}, 'RAINNY': {'HOT': 0.1, 'COLD': 0.9}}

HMM = hmm.HMM(
    visible_output,
    hidden_state,
    pi,
    transition_init,
    emission_init
)

HMM.initTrainSample(["COLD", "COLD", "COLD", "COLD", "COLD", "COLD", "COLD", "COLD", "HOT"])

HMM.BaumWelchLearn(0.01)

print "transition matrix:"
print HMM.hTransitionP
print "emission matrix:"
print HMM.hEmissionP

HMM.ViterbiDecode()

# sum = 0
# for i in HMM.hHiddenState:
#     sum = 0
#     for j in HMM.hHiddenState:
#         sum += HMM.hTransitionP[i][j]
#     print sum
#
# sum = 0
# for i in HMM.hHiddenState:
#     sum = 0
#     for j in HMM.hVisibleOutput:
#         sum += HMM.hEmissionP[i][j]
#     print sum
