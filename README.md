# CloudComputing_Lab1
Creating a FastAPI Service that contains at minimum of 10 different routes with at least 1 simple route, query string route, and path route. <br />
Routes all return information related to route description. <br />

Route 1. /root_route: Simple route that returns "Hello World." <br />
Route 2. /time: Simple route that returns the current local time when executed using a python time library. <br />
Route 3. /animal/{name}: Path route that takes input from the user for their favourite animal and completes the path. <br />
Route 4. /color/{name}: Path route that takes input from the user for their favourite color and completes the path. <br />
Route 5. /college-student: Post route that takes input from the user with 4 variables, name, age, year, major. <br />
Route 6. /query: Query route that takes input from the user, name, age, country into a query string. <br />
Route 7. /car: Post route that takes input from the user with 3 variables for the make, model and year of their car<br />
Route 8. /sports: Path route that takes input from the user for the users favourite sport <br />
Route 9. /book: Path route that takes input from the user for the user's favourite genre and book <br />
Route 10. /hometown: Path route that takes input from the user for the user's hometown and high school <br />


How to run: <br />
1.Download or clone the git repository. <br />
2.Open the project with pycharm(or another text editor). <br />
3.Install uvicorn and fastapi with pip. <br />
4.In the terminal enter: uvicorn main:app --port 8080 --reload <br />
5.Open your browser and go to: http://localhost:8080/docs to see all routes with fastapi <br />


# CloudComputing_Lab2
Creating a Python Command Line Driver Program that accesses all route services <br/>
Using Python unittest library create unit tests for all of your routes <br/>
Add routes that contain: Header parameters, Cookie Parameters <br/>
Add routes to Command Line Driver<br/>

Added Header and Cookie parameters aswell as routes and unittests for those two new routes<br/>
Added Unittests for previous routes<br/>

How to run: <br />
1.Download or clone the git repository. <br />
2.Open the project with pycharm(or another text editor). <br />
3.Install uvicorn and fastapi with pip. <br />
4.In the terminal enter: uvicorn main:app --port 8080 --reload <br />
5.Run the Python Command Line Driver Program in your ide or text editor <br />
6.Run the Unit tests by running the "httpRequestTests.py" in your ide <br />


# CloudComputing_Lab3 <br/>
Creating a NODEJS Service using Express <br/>
Created 10 routes with: <br />
-A minimum of 5 routes should return HTML content <br/>
-A minimum of 5 routes should have query parameters <br/>
-A minimum of 1 route should have header parameters <br/>
-A minimum of 1 route should have body inputs <br/>
<br/>

How to run: <br/>
1.Download or clone the git repository. <br />
2.Open the project with pycharm(or another text editor). <br />
3.Install express<br />
4.Navigate to the Lab3 folder using "cd Lab3/" in the terminal <br/>
5.Run the NodeJS service by typing "node lab3Main.js"<br/>
6.Change the route URL based on the routes shown in the Lab3/Lab3Main.js file<br/>


# CloudComputing_Lab4 <br/>
Containerize your FastAPI Service<br/>
Remote Access into your container<br/>
<br/>

How to run: <br/>
1.Download or clone the git repository. <br/>
2.Open the project with pycharm(or another text editor). <br/>
3.Navigate to the Lab4 folder using "cd Lab4/" in the terminal<br/>
4.In the terminal build the docker container using "docker compose up --build"<br/>
5.Visit "http://localhost:8080" to reach the fastapi container, do "http://localhost:8080/docs" to see all available routes<br/>
6.Remote access into the container by opening a new terminal, navigating again to the Lab4 folder("cd Lab4/", then entering "docker compose exec lab4 sh
"<br/>

# CloudComputing_Lab5 <br/>
Create the Guitar Database<br/>

Using the provided .sql file<br/>

Create the tables<br/>

Load the data<br/>

Develop 10 Queries:<br/>

Simple Single Table Queries<br/>

At least 5 Queries with Inner Joins<br/>

At least 5 Queries with functions or Group By clauses<br/>

How to run: <br/>
1.Install mySQL using "brew install mysql". <br/>
2.Login to mysql and create a password through the terminal using mysql -u root -p".  <br/>
3.Create the database while in mysql, "CREATE DATABASE my_guitar_shop;
USE my_guitar_shop;" and quit mysql after using "quit<br/>
4.In the terminal use this command to create the sql database from the guitar shop file, "mysql -u root -p my_guitar_shop < ~/createguitar.sql", make sure the directory is correct.<br/>
5.Open Dbeaver and add the new database connection using mySQL and fill in the required information and press finish<br/>
6.Add a the SQL script of the queries by right clicking the database, selecting SQL editor, then open sql script and use the Lab5Query script that you can download from the lab5 folder in this repo<br/>
7.Execute the SQL script. <br/>

# CloudComputing_Lab6 <br/>
Repeat lab5 to create a containerized implementation of MySQL<br/>
Use Docker Compose to create an implementation<br/>

How to run: <br/>
1.Install mySQL using "brew install mysql". <br/>
2.Login to mysql and create a password through the terminal using "mysql -u root -p".  <br/>
3.Create the database while in mysql, "CREATE DATABASE my_guitar_shop;
USE my_guitar_shop;" and quit mysql after using "quit<br/>
4.In the terminal use this command to create the sql database from the guitar shop file, "mysql -u root -p my_guitar_shop < ~/createguitar.sql", make sure the directory is correct.<br/>
5.Run the container from your pycharm terminal by moving to the lab6 folder, "cd Lab6" then "docker-compose up -d   "<br/>
5.Open Dbeaver and add the new database connection using mySQL and fill in the required information and press finish<br/>
5.5.For user and password, use "root", and "password"<br/>
6.Add a the SQL script of the queries by right clicking the database, selecting SQL editor, then open sql script and use the Lab5Query script that you can download from the lab5 folder in this repo<br/>
7.Execute the SQL script. <br/>

# CloudComputing_Lab7 <br/>
Implement your queries in Python<br/>

Add Options to your Python Command Line Driver to Execute your queries and display the results<br/>

Augment your unittests to cover your new functionality<br/>

How to run: <br/>
1.Download or clone the git repository. <br/>
2.Open the project with pycharm(or another text editor), and ensure docker is open. <br/>
3.Navigate to the Lab7 folder using "cd Lab7/" in the terminal<br/>
4.In the terminal build the docker container using "docker compose up --build"<br/>
5.Open a new terminal and and enter "python cli.py".<br/>
6.Enter in the terminal the query that you would like to try out, e.g. "q3" or any "q#" up to 15.<br/>
