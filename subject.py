import scipy.io

#contains meta-information for all pairs in data
meta = scipy.io.loadmat('Data/meta_info_6pairs.mat')
meta = meta["meta_info"]

class Subject():
    def __init__(self, player, game):
        self.player = player
        self.game = game
        self.p1_meta = meta[game][:][player]

    def number(self):
        subject_number = self.p1_meta["subject_number"][0][:][0][:][0][:][0]
        return subject_number

    def sex(self):
            subject_sex = self.p1_meta["subject_sex"][0][:][0][:][0]
            return subject_sex

    def age(self):
        subject_age = self.p1_meta["subject_age"][0][:][0][:][0][:][0]
        return subject_age

    def team_id(self):
            team_number = self.p1_meta["team_number"][0][:][0][:][0][:][0]
            return team_number

    def subject_id(self):
        player_number = self.p1_meta["player_number"][0][:][0][:][0][:][0]
        return player_number

    def nineHole(self):
            test_nineHolePeg = self.p1_meta["test_nineHolePeg"][0][:][0][:][0]
            return test_nineHolePeg

    def qa_empathy(self):
            QA_empathy_ATQ = self.p1_meta["QA_empathy_ATQ"][0][:][0][:][0]
            return QA_empathy_ATQ

    def qa_neo(self):
        QA_NEO = self.p1_meta["QA_NEO"][0][:][0][:][0]
        return QA_NEO

    def qa_general(self):
        QA_general = self.p1_meta["QA_general"][0][:][0][:][0]
        return QA_general






