__author__ = 'woodie'


def createVisibleBehaviorSet():
    '''
    CREATE VISIBLE BEHAVIOR SET

    This func will create a set of visible output for HMM.

    :return: behav(list of obj)
    '''
    # The following tuples are Evidences sets
    # - It is the key value, every behavior must have a time evidence
    # Time = ("MORNING", "NOON", "AFTERNOON", "NIGHT", "MIDNIGHT")
    Time = ("MORNING", "AFTERNOON", "NIGHT")
    # - It is location evidence
    # Location = ("ENTERTAINMENT", "COMMUNITY", "GOVERNMENT", "CATERING", "EDUCATION",
    #             "TRAFFIC", "FINANCE", "TRAVEL", "HOTEL", "COMPANY",
    #             "SHOPPING", "MEDICAL", "BUSINESS")
    Location = ("EDUCATION", "SHOPPING", "COMMUNITY")
    # - It is motion evidence
    # Motion = ("SITTING", "WALKING", "RUNNING", "RIDING", "DRIVING")
    Motion = ("SITTING", "WALKING", "RUNNING")
    # According to these sets, we instantiate a list of behavior obj.
    behav = []
    i = 0
    for t in Time:
        for l in Location:
            for m in Motion:
                behav.append(Behavior(motion = m,
                                      location = l,
                                      # no = i,
                                      time = t
                                      ))
                i += 1
    return behav

class Behavior:
    '''
    Class: BEHAVIOR

    It's a class to represent an user's behavior at some time.
    '''
    def __init__(self, **evidences):
        # The evidences
        self.bEvidences = evidences # It's a dict
        # The count of evidences
        self.bEviNum    = len(self.bEvidences)
        # The name of every evidence
        self.bEviName   = []
        for evi_name in self.bEvidences.keys():
            self.bEviName.append(evi_name)

    def getEvidenceName(self):
        return self.bEviName

    def getEvidenceCont(self, evi_name):
        return self.bEvidences[evi_name]

    def getEvidences(self):
        return self.bEvidences



