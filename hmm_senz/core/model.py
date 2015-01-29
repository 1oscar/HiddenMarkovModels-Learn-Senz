from __future__ import division
import hmm_senz.core.behavior as behavior
import hmm_senz.utility.utility as utility

__author__ = 'woodie'

class SenzModel:

    def __init__(self):
        # The following tuples are Evidences sets
        # - It is the key value, every behavior must have a time evidence
        # Time = ("MORNING", "NOON", "AFTERNOON", "NIGHT", "MIDNIGHT")
        self.mDefaultTime = ("MORNING", "AFTERNOON", "NIGHT")
        # - It is location evidence
        # Location = ("ENTERTAINMENT", "COMMUNITY", "GOVERNMENT", "CATERING", "EDUCATION",
        #             "TRAFFIC", "FINANCE", "TRAVEL", "HOTEL", "COMPANY",
        #             "SHOPPING", "MEDICAL", "BUSINESS")
        self.mDefaultLocation = ("EDUCATION", "SHOPPING", "COMMUNITY")
        # - It is motion evidence
        # Motion = ("SITTING", "WALKING", "RUNNING", "RIDING", "DRIVING")
        self.mDefaultMotion = ("SITTING", "WALKING", "RUNNING")

        self.mDefaultHiddenStateSet = ("WORK", "LIVE", "RELAX", "ENTERTAIN", "EXERCISE")

        self.mDefaultVisibleOutputSet = self.createDefaultVisibleBehaviorSet()

        self.mDefaultPi = self.createDefaultPi()

        self.mDefaultTransitionMatrix = self.createDefaultTransitionMatrix()

        self.mDefaultEmissionMatrix = self.createDefaultEmissionMatrix()

    def createDefaultPi(self):
        pi    = []
        size  = len(self.mDefaultHiddenStateSet)
        value = 1/size
        for i in range(0, size):
            pi.append(value)
        return pi

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

    def createDefaultVisibleBehaviorSet(self):
        '''
        CREATE VISIBLE BEHAVIOR SET

        This func will create a set of visible output for HMM.

        :return: behav(list of obj)
        '''
        # According to these sets, we instantiate a list of behavior obj.
        behav = []
        i = 0
        for t in self.mDefaultTime:
            for l in self.mDefaultLocation:
                for m in self.mDefaultMotion:
                    behav.append(behavior.Behavior(motion = m,
                                                   location = l,
                                                   # no = i,
                                                   time = t
                    ))
                    i += 1
        return behav