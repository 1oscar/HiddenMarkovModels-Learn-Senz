__author__ = 'woodie'

from hmm_senz.hmm import hmm

visible_output = ("HOT","COLD","FROZEN")
hidden_state   = ("WINDY","SUNNY","RAINNY")
transition_init = [[0.2,0.4,0.4],[0.3,0.3,0.4],[0.1,0.1,0.8]]
emission_init  = [[0.2,0.4,0.4],[0.3,0.3,0.4],[0.1,0.1,0.8]]
HMM = hmm.HMM(
    visible_output,
    hidden_state,
    transition_init,
    emission_init
)




