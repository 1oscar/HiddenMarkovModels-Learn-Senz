from __future__ import division
import hmm_senz.core.behavior as behavior
import hmm_senz.utility.utility as utility

__author__ = 'woodie'

# Hidden state set
DEFAULT_HIDDEN_STATE = ("WORK", "LIVE", "RELAX", "ENTERTAIN", "EXERCISE")
# Visible output set

# - Location = ("ENTERTAINMENT", "COMMUNITY", "GOVERNMENT", "CATERING", "EDUCATION",
#               "TRAFFIC", "FINANCE", "TRAVEL", "HOTEL", "COMPANY",
#               "SHOPPING", "MEDICAL", "BUSINESS")
DEFAULT_LOCATION     = ("EDUCATION", "SHOPPING", "COMMUNITY")
# - Motion   = ("SITTING", "WALKING", "RUNNING", "RIDING", "DRIVING")
DEFAULT_MOTION       = ("SITTING", "WALKING", "RUNNING")
# - Sound    = ("")
DEFAULT_SOUND        = ()

# The class of senz model
class SenzModel:

    def __init__(self,
                 hidden_state = DEFAULT_HIDDEN_STATE,  # The Hidden State Set
                 location = DEFAULT_LOCATION, motion = DEFAULT_MOTION, sound = DEFAULT_SOUND): # The Visible Output Set
        # - It is location evidence
        self.mDefaultLocation = location
        # - It is motion evidence
        self.mDefaultMotion = motion
        # - It is sound evidence
        # self.mDefaultSound = sound
        # - It's visible output set
        #   It is made up of element above-mentioned
        self.mDefaultVisibleOutputSet = self.createDefaultVisibleBehaviorSet()

        # - It's hidden state set
        self.mDefaultHiddenStateSet = hidden_state

        # - It's the prior probability of hidden states
        self.mDefaultPi = self.createDefaultPi()
        # - Transition Matrix
        self.mDefaultTransitionMatrix = self.createDefaultTransitionMatrix()
        # - Emission Matrix
        self.mDefaultEmissionMatrix = self.createDefaultEmissionMatrix()

        # - Condition Motion Matrix
        self.mMotionConditionMatrix = self.createDefaultConditionMatrix(self.mDefaultMotion)
        # - Condition Location Matrix
        self.mLocationConditionMatrix = self.createDefaultConditionMatrix(self.mDefaultLocation)
        # - Condition Location Matrix
        # self.mSoundConditionMatrix = self.createDefaultConditionMatrix(self.mDefaultSound)


    def createDefaultPi(self):
        pi    = []
        size  = len(self.mDefaultHiddenStateSet)
        value = 1/size
        for i in range(0, size):
            pi.append(value)
        return pi

    # The construction of Condition Matrix
    # - Motion Condition Matrix
    def createDefaultConditionMatrix(self, condition):
        size       = len(self.mDefaultHiddenStateSet)
        value      = 1/size
        # the return value
        condition_matrix = {}
        for c in condition:
            condition_matrix[c] = {}
            for state in self.mDefaultHiddenStateSet:
                condition_matrix[c][state] = value
        return condition_matrix

    def createDefaultTransitionMatrix(self):
        transition = []
        size       = len(self.mDefaultHiddenStateSet)
        value      = 1/size
        for i in range(0, size):
            tmp = []
            for j in range(0, size):
                tmp.append(value)
            transition.append(tmp)
        return transition

    def createDefaultEmissionMatrix(self):
        emission = []
        row      = len(self.mDefaultHiddenStateSet)
        col      = len(self.mDefaultVisibleOutputSet)
        value    = 1/col
        for r in range(0, row):
            tmp = []
            for j in range(0, col):
                tmp.append(value)
            emission.append(tmp)
        return emission

    # def createDefaultEmissionMatrix(self):
    #     emission = []
    #     row      = len(self.mDefaultHiddenStateSet)
    #     col      = len(self.mDefaultVisibleOutputSet)
    #     value    = 1/col
    #     for r in range(0, row):
    #         tmp = []
    #         for j in range(0, col):
    #             tmp.append(value)
    #         emission.append(tmp)
    #     return emission

    def createDefaultVisibleBehaviorSet(self):
        '''
        CREATE VISIBLE BEHAVIOR SET

        This func will create a set of visible output for HMM.

        :return: behav(list of obj)
        '''
        # According to these sets, we instantiate a list of behavior obj.
        behav = []
        i = 0
        # for t in self.mDefaultTime:
        for l in self.mDefaultLocation:
            for m in self.mDefaultMotion:
                # for s in self.mDefaultSound
                behav.append(behavior.Behavior(motion = m,
                                               location = l
                                               # no = i,
                                               # sound = s
                ))
                i += 1
        return behav

