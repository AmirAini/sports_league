Steps to get it running.

1. Please clone repo
   <br>https://github.com/AmirAini/sports_league.git
2. Enter project directory on local machine
   <br>cd sports_league
3. Build docker image (via Dockerfile provided)
   <br>docker build -t leagueapp:1.0 .
4. Check if image was successful (should be listed)
   <br>docker images
5. Run the project on local machine (make sure port 80 is not used)
   <br>docker run -p 8000:8000 leagueapp:1.0
6. Go to web-browser and type
   <br>http://localhost:8000/  
8. First time visit, there's no data. Try uploading a csv file (template given below)
   <br>[Download Sample CSV](https://drive.google.com/file/d/1BmCn46fWBqYdOOQwUKqycgTBdUm7AUks/view?usp=sharing)

   ##todo:
9. Run test
   <br>docker exec -it <container_id> bash
10. python manage.py test
   <br>runs test
