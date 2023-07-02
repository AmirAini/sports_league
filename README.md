<h1>Sports League</h1>

<h2>Steps to Get It Running</h2>

<ol>
  <li>Clone the repository:<br>
    <code>git clone https://github.com/AmirAini/sports_league.git</code></li>
<li>
   To install docker on local machine:<br>
   <a href="https://docs.docker.com/engine/install/">Docker Installation Guide</a></li>
</li>
  
  <li>Enter the project directory on your local machine:<br>
    <code>cd sports_league</code></li>
  
  <li>Build the Docker image using the provided Dockerfile:<br>
    <code>docker build -t leagueapp:1.0 .</code></li>
  
  <li>Check if the image was built successfully:<br>
    <code>docker images</code></li>
  
  <li>Run the project on your local machine (make sure port 80 is not being used):<br>
    <code>docker run -p 8000:8000 leagueapp:1.0</code></li>
  
  <li>Open your web browser and go to the following URL:<br>
    <code>http://localhost:8000/</code></li>
  
  <li>On the first visit, there won't be any data. You can try uploading a CSV file. <a href="https://drive.google.com/file/d/1BmCn46fWBqYdOOQwUKqycgTBdUm7AUks/view?usp=sharing">Download Sample CSV</a></li>
</ol>

<h2>Additional Steps:</h2>

<ol start="8">
  <li>Run tests:</li>
</ol>

<pre><code>docker exec -it &lt;container_id&gt; python manage.py test
</code></pre>

<p><em>Note: Replace &lt;container_id&gt; in step 8 with the actual container ID you get when running the Docker container.</em></p>
