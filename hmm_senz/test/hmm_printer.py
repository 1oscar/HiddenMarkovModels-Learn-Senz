__author__ = 'woodie'

import hmm_senz.hmm.hmm as hmm

pi = {"WINDY" : 0.2, "SUNNY" : 0.2, "RAINNY" : 0.6}
visible_output = ("HOT","COLD")
hidden_state   = ("WINDY","SUNNY","RAINNY")
transition_init = {'WINDY': {'WINDY': 0.2, 'SUNNY': 0.4, 'RAINNY': 0.4}, 'SUNNY': {'WINDY': 0.3, 'SUNNY': 0.3, 'RAINNY': 0.4}, 'RAINNY': {'WINDY': 0.1, 'SUNNY': 0.1, 'RAINNY': 0.8}}
emission_init  = {'WINDY': {'HOT': 0.2, 'COLD': 0.8}, 'SUNNY': {'HOT': 0.7, 'COLD': 0.3}, 'RAINNY': {'HOT': 0.1, 'COLD': 0.9}}

HMM = hmm.HMM(
    visible_output,
    hidden_state,
    pi,
    transition_init,
    emission_init
)

HMM.initTrainSample(["COLD", "COLD", "HOT", "COLD"])
print HMM.forward()
#print HMM.estimateValue()
print HMM.backward()
print HMM.computeGamma()
print HMM.computeXi()
#print HMM.hBeta