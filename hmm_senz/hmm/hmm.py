__author__ = 'woodie'

import hmm_senz.utility.decorator as decorator
import hmm_senz.utility.exception as exception

class HMM:
    '''Base Class : HMM

    The base class is used to solve the basic HMM problem.
    '''

    @decorator.SenzDecorator.funcLogger
    def __init__(self,
                 visible_output,  # All kinds of visible outputs, it's a tuple, eg. ("wet", "dry")
                 hidden_state,    # All kinds of hidden states, it's a tuple, eg. ("sunny", "windy", "cloudy", "rainny")
                 pi,              # The initial probability of every states when started
                 transition_init, # The Matrix of hidden states' transition probability
                 emission_init): # The Matrix of visible outputs' emission probability
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
        self.hTransitionP = transition_init
        # The initial of hEmissionP
        # - It's a 2-dimension dict
        # - { key1 : { key2 : value } }
        # - key1 is hidden states' name
        # - key2 is visible outputs' name
        # - value is the transition probability from key1 to key2
        self.hEmissionP   = emission_init
        # The initial probablility of every hidden state
        # - eg. pi = {"sunny" : 0.2, "windy" : 0.3, "cloudy" : 0.1, "rainny" : 0.4}
        self.hPi          = pi

        # The HMM's timestamp, default is 0
        self.hT       = 0
        # The HMM's visible output
        self.hOutput  = []
        # The probability of evety output
        self.hOutputP = []

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
    def initTrainSample(self, output): # The HMM's visible output
        '''
        GIVE INITIAL TRAINNING SAMPLE

        If you have complete trainning sample,
        you can call this function to give your sample to HMM.
        Meanwhile, HMM will set HMM's timestamp according to the size of your sample.
        And init the related variable.

        :param output: The HMM's visible output
        :return:       None
        '''

        self.hT = len(output)
        self.hOutput = output

        # Init hOutputP by hT
        for t in range(0, self.hT):
            self.hOutputP.append(0)

        # Init hAlpha by hT
        for t in range(0, self.hT):
            alpha_t = {}
            for state in self.hHiddenState:
                alpha_t[state] = 0
            self.hAlpha.append(alpha_t)
        # ---INTERESTING PROBLEM---
        # If I write like this:
        #  1 alpha_t = {}
        #  2 for state in self.hHiddenState:
        #  3     alpha_t[state] = 0
        #  4 for t in range(0, self.hT):
        #  5    self.hAlpha.append(alpha_t)
        # all member of self.hAlpha will stay the same with each other all the time,
        # because they are the same object named alpha_t

    @decorator.SenzDecorator.funcLogger
    def forward(self):
        '''
        FORWARD

        It used to excute forward algorithm.
        It will calculate HMM's forward variable(alpha).
        And store in HMM.hAlpha.

        :return: None
        '''

        # Check the output sample
        # try:
        #     if self.hT == 0 :
        #         raise exception.SenzException("empty sample")
        # except exception.SenzException, e:
        #     print "[SenzException] There is no trainning sample"
        #     return

        # Initialization:
        # - Calculate the every hidden state's alpha(forward variable) at t=1
        for state in self.hHiddenState:
            self.hAlpha[0][state] = self.hPi[state] * self.hEmissionP[state][self.hOutput[0]]
            print "alpha t=", 0, " state=", state, "val=", self.hAlpha[0][state]
        # Induction:
        # - Compute all alpha at every t
        for t in range(0, self.hT - 1):
            for state_j in self.hHiddenState:
                sum = 0
                for state_i in self.hHiddenState:
                    sum += self.hAlpha[t][state_i] * self.hTransitionP[state_i][state_j]
                self.hAlpha[t+1][state_j] = sum * self.hEmissionP[state_j][self.hOutput[t+1]]
                print "alpha t=", t+1, " state=", state_j, "val=", self.hAlpha[t+1][state_j]

    @decorator.SenzDecorator.funcLogger
    def estimateValue(self):
        '''
        ESTIMATE VALUE

        It used to estimate the probability of current output.

        :return:  estimate_p(float)  the probability of current output
        '''
        # Forward:
        # - Calculate the HMM's forward variable(alpha).
        self.forward()
        # Termination:
        # - The probability of output at t = sum of every state's probability at t (that is alpha[t][state])
        estimate_p = 0
        for state in self.hHiddenState:
            estimate_p += self.hAlpha[self.hT - 1][state]
        return estimate_p


    def backward(self):
        pass








