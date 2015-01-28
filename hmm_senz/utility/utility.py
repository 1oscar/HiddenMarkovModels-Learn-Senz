__author__ = 'woodie'

#import hmm_senz.utility.senz_exception as exception
import hmm_senz.core.behavior as behavior

class Utility:

    @classmethod
    def printOver(cls):
        print "\n"

    @classmethod
    # need type check!
    def printEmissionMatrix(cls, matrix):
        print "   ---- HMM's Emission Matrix ----"
        for state in matrix:
            print "   * [", state, "] ->"
            for output in matrix[state]:
                print "    ", output.getEvidences(), "=", matrix[state][output]
        cls.printOver()


    @classmethod
    def printTransitionMatrix(cls, matrix):
        print "   ---- HMM's Transition Matrix ----"
        for state_i in matrix:
            print "   * [", state_i, "] -> {",
            for state_j in matrix[state_i]:
                print "[", state_j, "] =", matrix[state_i][state_j],
            print "}"
        cls.printOver()
