__author__ = 'woodie'

import hmm_senz.core.senz as senz
import hmm_senz.utility.utility as utility
import hmm_senz.core.model as model


pi = {"WORK": 0.6, "LIVE": 0.1, "RELAX": 0.05, "ENTERTAIN": 0.2, "EXERCISE": 0.05}
motion_condition = {
    "SITTING": {"WORK": 0.7, "LIVE": 0.1, "RELAX": 0.15, "ENTERTAIN": 0.04, "EXERCISE": 0.01},
    "WALKING": {"WORK": 0.01, "LIVE": 0.3, "RELAX": 0.09, "ENTERTAIN": 0.59, "EXERCISE": 0.01},
    "RUNNING": {"WORK": 0.01, "LIVE": 0.01, "RELAX": 0.01, "ENTERTAIN": 0.05, "EXERCISE": 0.92}
}
location_condition = {
    "EDUCATION": {"WORK": 0.5, "LIVE": 0.3, "RELAX": 0.18, "ENTERTAIN": 0.01, "EXERCISE": 0.01},
    "SHOPPING": {"WORK": 0.01, "LIVE": 0.01, "RELAX": 0.2, "ENTERTAIN": 0.75, "EXERCISE": 0.03},
    "COMMUNITY": {"WORK": 0.2, "LIVE": 0.4, "RELAX": 0.15, "ENTERTAIN": 0.05, "EXERCISE": 0.2}
}

m = model.SenzModel()
m.setPi(pi)
m.setMotionConditionP(motion_condition)

s = senz.Senz(m)

u = utility.Utility(s)
u.printTransitionMatrix()
u.printEmissionMatrix()
u.printHiddenState()
u.printVisibleOutput()

s.initTrainSample([{'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},

                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},

                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},

                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},

                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'RUNNING', 'location': 'COMMUNITY'},
                   {'motion': 'RUNNING', 'location': 'COMMUNITY'}
                   ])

s.BaumWelchLearn(0.01)
s.ViterbiDecode()

u.printTransitionMatrix()
u.printEmissionMatrix()
u.printHiddenState()
u.printVisibleOutput()

print "The outcome:", s.getQ()