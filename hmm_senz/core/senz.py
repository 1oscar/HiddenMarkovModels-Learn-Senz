__author__ = 'woodie'

import hmm_senz.core.behavior as behavior
import hmm_senz.hmm.hmm as hmm

class Senz(hmm.HMM):
    '''
    SENZ


    '''
    # Override base func
    def __init__(self, pi_init, transition_init, emission_init):
        # senz's visible output for hmm
        self.visible_output_obj = behavior.createVisibleBehaviorSet()
        # senz's hidden state for hmm
        hidden_state   = ("WORK", "LIVE", "RELAX", "ENTERTAIN", "EXERCISE")
        # Transfer matrix to dict
        transition = self.matrixToDict(transition_init, hidden_state, hidden_state)
        emission   = self.matrixToDict(emission_init, hidden_state, self.visible_output_obj)
        pi         = self.matrixToDict(pi_init, 0, hidden_state)
        # Invoke base class
        hmm.HMM.__init__(self, self.visible_output_obj, hidden_state, pi, transition, emission)

    # Override base func
    def initTrainSample(self, output): # The Senz's visible output
        # Transfer train sample from dict to obj
        output_obj = []
        for o in output:
            # For every element in output,
            # which is same with in visible_output_obj
            output_obj.append(self.outputDictToObj(o))
        # init train sample
        hmm.HMM.initTrainSample(self, output_obj)

    def outputDictToObj(self, output_dict):
        '''
        OUTPUT DICT TO OBJ



        :param output_dict:
        :return:
        '''
        for b in self.visible_output_obj:
            if output_dict == b.getEvidences():
                return b

    def matrixToDict(self, matrix, row, col):
        '''
        MATRIX TO DICT

        The method helps __init__ func transfer param (transition, emission, pi) from
        num matrix to dict. the dict data structure is good at data processing.

        :param matrix: It is the matrix that need to be transfered to dict
        :param row: the list of matrix's row
        :param col: the list of matrix's col
        :return: the dict which is transfered from matrix
        '''
        dict = {}
        i = 0 # index of row/col of matrix
        # If matrix has no row
        if row == 0:
            for c in col:
                dict[c] = matrix[i]
                i += 1
            return dict
        # Else if matrix is two-dimension
        for r in row:
            j = 0 # index of col of matrix
            dict[r] = {}
            for c in col:
                dict[r][c] = matrix[i][j]
                j += 1
            i += 1
        return dict