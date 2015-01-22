__author__ = 'woodie'

import hmm_senz.utility.decorator as decorator
import hmm_senz.utility.exception as exception

class HMM:
    '''Base Class : HMM

    The base class is used to solve the basic HMM problem.
    '''

    @decorator.SenzDecorator.logger
    def __init__(self,
                 visible_output,  # All kinds of visible outputs, it's a tuple, eg. ("wet", "dry")
                 hidden_state,    # All kinds of hidden states, it's a tuple, eg. ("sunny", "windy", "cloudy", "rainny")
                 pi,              # The initial probability of every states when started
                 transition_init, # The Matrix of hidden states' transition probability
                 emission__init): # The Matrix of visible outputs' emission probability
        self.hVisibleOutput = visible_output
        self.hHiddenState   = hidden_state
        self.hPi            = pi
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
        self.hTransitionP = transition_init
        # The initial of hEmissionP
        # - It's a 2-dimension dict
        # - { key1 : { key2 : value } }
        # - key1 is hidden states' name
        # - key2 is visible outputs' name
        # - value is the transition probability from key1 to key2
        self.hEmissionP = emission__init
        # The HMM's timestamp, default is 0
        self.hT      = 0
        # The HMM's visible output
        self.hOutput = []
        # forward variable
        # - t = 1 : alpha[1][Si] = pi[Si] * emission[Si][O1]
        # - other : alpha[t][Si] = emission[Si][Ot] * sum(N,j=1)(alpha(t-1)(Sj) * transition[Sj][Si])
        self.hAlpha  = []
        # backward variable
        self.hBeta   = []
        # Be at Si when t
        self.hGamma  = []
        # Be at Si when t and at Sj when t+1
        self.hXi     = []

    @decorator.SenzDecorator.funcLogger
    def giveInitTrainSample(self,
                output): # The HMM's visible output
        '''
        GIVE INITIAL TRAINNING SAMPLE
        If you have complete trainning sample,
        you can call this function to give your sample to HMM.
        Meanwhile, HMM will set HMM's timestamp according to the size of your sample.

        :param output: The HMM's visible output
        :return:       None
        '''

        self.hT = len(output)
        self.hOutput = output

    def forward(self):
        '''
        FORWARD

        :return: None
        '''

        # Check the output sample
        try:
            if self.hT == 0 :
                raise exception.SenzException("empty sample")
        except exception.SenzException, e:
            print "[SenzException] There is no trainning sample"
            return

        for t in range(0, self.hT):
            pass


    def backward(self):
        pass








