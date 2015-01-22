__author__ = 'woodie'

from hmm_senz.hmm import hmm

pi = (0.2, 0.3, 0.5)
visible_output = ("HOT","COLD","FROZEN")
hidden_state   = ("WINDY","SUNNY","RAINNY")
transition_init = {'WINDY': {'WINDY': 0.2, 'SUNNY': 0.4, 'RAINNY': 0.4}, 'SUNNY': {'WINDY': 0.3, 'SUNNY': 0.3, 'RAINNY': 0.4}, 'RAINNY': {'WINDY': 0.1, 'SUNNY': 0.1, 'RAINNY': 0.8}}
emission_init  = {'WINDY': {'WINDY': 0.2, 'SUNNY': 0.4, 'RAINNY': 0.4}, 'SUNNY': {'WINDY': 0.3, 'SUNNY': 0.3, 'RAINNY': 0.4}, 'RAINNY': {'WINDY': 0.1, 'SUNNY': 0.1, 'RAINNY': 0.8}}

HMM = hmm.HMM(
    visible_output,
    hidden_state,
    pi,
    transition_init,
    emission_init
)
print HMM.hTransitionP
print HMM.hHiddenState
print HMM.hVisibleOutput

#HMM.giveInitTrainSample(["HOT", "COLD", "COLD", "FROZEN"])

HMM.forward()


