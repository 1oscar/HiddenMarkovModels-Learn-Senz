__author__ = 'woodie'

class HMM:
    '''Base Class : HMM

    The base class is used to solve the HMM problem
    '''
    def __init__(self,
                 visible_output,
                 hidden_state,
                 transition_init,
                 emission__init):
        self.hVisibleOutput = visible_output
        self.hHiddenState   = hidden_state
        self.hTransitionP   = {}
        self.hEmissionP     = {}
        self.hSizeHmm       = {
            'visible state' : len(self.hVisibleOutput),
            'hidden state'  : len(self.hHiddenState)
        }

        for vi in self.hVisibleOutput:
            for vj in self.hVisibleOutput:
                self.hTransitionP[vi][vj] = transition_init[i][j]

