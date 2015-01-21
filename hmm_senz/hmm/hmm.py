__author__ = 'woodie'

class HMM:
    '''Base Class : HMM

    The base class is used to solve the basic HMM problem.
    '''
    def __init__(self,
                 visible_output,
                 hidden_state,
                 transition_init, # The Matrix of hidden states' transition probability
                 emission__init): # The Matrix of visible outputs' emission probability
        self.hVisibleOutput = visible_output
        self.hHiddenState   = hidden_state
        self.hSizeHmm       = {
            'visible output' : len(self.hVisibleOutput),
            'hidden state'   : len(self.hHiddenState)
        }
        # The initial of hTransitionP
        # - It's a 2-dimension dict
        # - { key1 : { key2 : value } }
        # - key1 is hidden states' name
        # - key2 is hidden states' name
        # - value is the transition probability from key1 to key2
        self.hTransitionP   = transition_init
        # The initial of hEmissionP
        # - It's a 2-dimension dict
        # - { key1 : { key2 : value } }
        # - key1 is hidden states' name
        # - key2 is visible outputs' name
        # - value is the transition probability from key1 to key2
        self.hEmissionP     = emission__init




