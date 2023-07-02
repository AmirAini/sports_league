from django.test import TestCase
from django.urls import reverse
from .models import Match, Team
from django.core.files.uploadedfile import SimpleUploadedFile
import pdb

class TestScoreApp(TestCase):

    def setUp(self):
        self.team_1 = Team.objects.create(name='FNC')
        self.team_2 = Team.objects.create(name='G2')
        self.match = Match.objects.create(
            team_1=self.team_1,
            team_2=self.team_2,
            team_1_score=2,
            team_2_score=1
        )

    def test_user_can_view_upload_csv(self):
        res = self.client.get(reverse('upload_csv'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'rank/upload_csv.html')

    def test_user_can_view_overview(self):
        res = self.client.get(reverse('overview'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'rank/overview.html')

    def test_user_can_view_match_list(self):
        res = self.client.get(reverse('match_list'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'rank/match_list.html')
    
    def test_user_can_view_edit_match(self):
        res = self.client.get(reverse('edit_match',args=[self.match.id]))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'rank/edit_match.html')


    def test_user_can_upload_csv(self):
        #Create a temporary CSV file
        data = (
            "team_1_name, team_1_score, team_2_name, team_2_score\n" 
            "G2, 2, FNC, 1\n"
            "MFC,2,SKT,3\n")
        
        # Make a POST request to the upload_csv
        csv_file = SimpleUploadedFile("test.csv", data.encode("utf-8"), content_type="text/csv")
        self.client.post(reverse("upload_csv"), {"file": csv_file})
        
        
        #on top of the setUp
        self.assertEqual(Team.objects.count(), 4)
        self.assertEqual(Match.objects.count(), 3)

    def test_user_can_delete_match(self):
        self.client.post(reverse('delete_match', args=[self.match.id]))
        self.assertEqual(Match.objects.filter(id=self.match.id).exists(), False)
    
    def test_user_can_edit_match(self):
        payload = {
            "team_1": self.team_1.id,
            "team_2": self.team_2.id,
            "team_1_score": 3,
            "team_2_score": 3,
        }
        self.client.post(reverse("edit_match", args=[self.match.id]), data=payload)
        
        # Retrieve the updated match from the database
        updated_match = Match.objects.get(id=self.match.id)
        
        # Assert the updated match's attributes
        self.assertEqual(updated_match.team_1, self.team_1)
        self.assertEqual(updated_match.team_2, self.team_2)
        self.assertEqual(updated_match.team_1_score, 3)
        self.assertEqual(updated_match.team_2_score, 3)
    

    def test_user_cannot_use_same_team(self):
        payload = {
            "team_1": self.team_1.id,
            "team_2": self.team_1.id,
            "team_1_score": 3,
            "team_2_score": 3,
        }
        self.client.post(reverse("edit_match", args=[self.match.id]), data=payload)
        
        # Retrieve the match from the database
        original_match = Match.objects.get(id=self.match.id)
        self.assertEqual(original_match.team_1, self.team_1)
        self.assertEqual(original_match.team_2, self.team_2)
        self.assertEqual(original_match.team_1_score, self.match.team_1_score)
        self.assertEqual(original_match.team_2_score, self.match.team_2_score)

    def test_user_cannot_enter_negative_score(self):
        payload = {
            "team_1": self.team_1.id,
            "team_2": self.team_1.id,
            "team_1_score": -3,
            "team_2_score": 3,
        }
        self.client.post(reverse("edit_match", args=[self.match.id]), data=payload)
        
        # Retrieve the match from the database
        original_match = Match.objects.get(id=self.match.id)
        self.assertEqual(original_match.team_1, self.team_1)
        self.assertEqual(original_match.team_2, self.team_2)
        self.assertEqual(original_match.team_1_score, self.match.team_1_score)
        self.assertEqual(original_match.team_2_score, self.match.team_2_score)