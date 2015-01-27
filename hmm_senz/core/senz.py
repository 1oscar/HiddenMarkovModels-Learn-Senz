__author__ = 'woodie'

import hmm_senz.core.behavior as behavior
import hmm_senz.hmm.hmm as hmm

class Senz(hmm.HMM):
    '''

    '''
    def __init__(self, pi, transition_init, emission_init):
        # # senz's visible output for hmm
        # visible_output = behavior.createVisibleBehaviorSet()
        # # senz's hidden state for hmm
        # hidden_state   = ("WORK", "LIVE", "RELAX", "ENTERTAIN", "EXERCISE")
        visible_output  = ("HOT", "COLD")
        hidden_state    = ("WINDY", "SUNNY", "RAINNY")
        hmm.HMM.__init__(self, visible_output, hidden_state, pi, transition_init, emission_init)



