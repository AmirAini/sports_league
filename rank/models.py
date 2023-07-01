from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Match(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home', null=True, blank=True)
    team_1_score = models.PositiveSmallIntegerField(null=True, blank=True)
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away', null=True, blank=True)
    team_2_score = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return "{team1} {team_1_score} - {team2} {team_2_score}".format(
            team1=self.team_1.name,
            team_1_score=self.team_1_score,
            team2=self.team_2.name,
            team_2_score=self.team_2_score
        )

class Rank(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, primary_key=True)
    points = models.IntegerField(default=0)
