Steps to get it running.

1. Please clone repo
   https://github.com/AmirAini/sports_league.git
2. Enter project directory on local machine
   cd sports_league
3. Build docker image (via Dockerfile provided)
   docker build -t leagueapp:1.0 .
4. Check if image was successful (should be listed)
   docker images
5. Run the project on local machine (make sure port 80 is not used)
   docker run -p 8000:8000 leagueapp:1.0

   ##todo:
7. Run test
   docker exec -it <container_id> bash
8. python manage.py test
   runs test
