
from project.formula_teams.formula_team import FormulaTeam
class RedBullTeam(FormulaTeam):


    @property
    def team_data(self):
        expenses = 250000
        sponsors = {'Oracle':{1:1_500_000,2:800_000},
                    'Honda':{8:20_000,10:10_000}}
        return expenses,sponsors



