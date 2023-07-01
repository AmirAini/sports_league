from django.shortcuts import render,redirect
from .models import Team, Match
from .forms import FormUpload
import pdb
from django.contrib import messages

def uploadCsv(request):
    if request.method == 'GET':
        form = FormUpload()
        return render(request, 'rank/upload_csv.html', {'form': form})

    else:
        form = FormUpload(request.POST, request.FILES)
        if form.is_valid():
            try:
                csv_file = form.cleaned_data['file']
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                data_rows = decoded_file[1:]

                for row in data_rows:
                    
                    values = row.split(',')
                    values = [value.strip() for value in values if value.strip()]
                    
                    team_1_name, team_1_score, team_2_name, team_2_score = values
                    team_1_name, _ = Team.objects.get_or_create(name=team_1_name)
                    team_2_name, _ = Team.objects.get_or_create(name=team_2_name)
                    
                    # Create records
                    Match.objects.create(
                        team_1=team_1_name, 
                        team_1_score=team_1_score,
                        team_2=team_2_name, 
                        team_2_score=team_2_score
                    )

                return redirect('overview')
            
            except Exception as e:
                error=("Error occurred:" + str(e))
                return render(request, 'rank/upload_csv.html', {'form': form, 'error': error})

def overview(request):
    teams = Team.objects.all()
    teamScores = {}

    for team in teams:
        totalPoints = 0
        # Retrieve matches where the team is the home team
        homeMatches = Match.objects.filter(team_1=team)
        for homeMatch in homeMatches:
            if homeMatch.team_1_score > homeMatch.team_2_score:
                totalPoints += 3
            elif homeMatch.team_1_score == homeMatch.team_2_score:
                totalPoints += 1
        
        awayMatches = Match.objects.filter(team_2=team)
        for awayMatch in awayMatches:
            if awayMatch.team_2_score > awayMatch.team_1_score:
                totalPoints += 3
            elif awayMatch.team_1_score == awayMatch.team_2_score:
                totalPoints += 1

        # Push to object
        teamScores[team] = totalPoints
        
    teamScores = {team: points for team, points in sorted(teamScores.items(), key=lambda x: (-x[1], x[0].name))}

    return render(request, 'rank/overview.html', {'team_score': teamScores})


def delete(request, match_id):
    try:
        game = Match.objects.get(id=match_id)
        game.delete()
        messages.success(request, 'Match successfully deleted.')
    except Match.DoesNotExist:
        messages.error(request, 'Match does not exist.')
    except Exception as e:
        messages.error(request, 'An error occurred: {err}'.format(str(e)))
    
    return redirect('overview')


def match_list(request):
    matches = Match.objects.all()
    return render(request, 'rank/match_list.html', {'matches': matches})




def edit(request, match_id):
    
    if request.method == 'GET':
        teams = Team.objects.all()
        match = Match.objects.get(id=match_id)
        return render(request, 'rank/edit_match.html', {'match': match,'teams':teams})

    try: 
        match = Match.objects.get(id=match_id)
        
        if request.method == 'POST':
            team_1_id = request.POST.get('team_1')
            team_2_id = request.POST.get('team_2')
            team_1_score = request.POST.get('team_1_score')
            team_2_score = request.POST.get('team_2_score')

            # Validate team IDs and scores
            if team_1_id == team_2_id:
                teams = Team.objects.all()
                return render(request, 'rank/edit_match.html', {'match': match, 'error': 'Team 1 and Team 2 must be different.','teams':teams})

            try:
                team_1 = Team.objects.get(id=team_1_id)
                team_2 = Team.objects.get(id=team_2_id)
            except Team.DoesNotExist:
                return render(request, 'rank/edit_match.html', {'match': match, 'error': 'Selected teams do not exist.'})

            # Update match data
            match.team_1 = team_1
            match.team_2 = team_2
            match.team_1_score = team_1_score
            match.team_2_score = team_2_score
            match.save()

            # Redirect to overview page
            return redirect('overview')
    
    except Match.DoesNotExist:
        messages.error(request, {'error':'Match does not exist.'})
    except Exception as e:
        messages.error(request, {'error':'An error occurred: {err}'.format(str(e))})
    
    return redirect('overview')


