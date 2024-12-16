# Docker-Final-Khamida

1. Install Docker and Start PostgreSQL in Docker
docker pull postgres:latest

docker run --name university-db -e POSTGRES_USER=Khamida -e POSTGRES_PASSWORD=Khamida13 -d -p 5432:5432 postgres:latest

docker ps

docker exec -it university-db psql -U Khamida

2. Set Up the PostgreSQL Database and Tables
psql -U Khamida

CREATE TABLE Timetable (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(255),
    day VARCHAR(50),
    time VARCHAR(50),
    room VARCHAR(50),
    level INT
);
INSERT INTO Timetable (course_name, day, time, room, level) VALUES
('Operating Systems', 'Tuesday', '2:00 PM', 'Room 114', 2),
('Culture and Communication', 'Tuesday', '4:30 AM', 'Webnet+', 1),
('Computer Languages', 'Wednesday', '2:00 PM', 'Room 114', 1),
('Discrete Mathematics', 'Thursday', '2:00 PM', 'Room 403', 2),
('Computer and Information Security ', 'Thursday', '4:30 PM', 'Room 114', 1),
('Introduction to Sustainability', 'Friday', '2:00 PM', 'Room 408', 1);

3. Install Python and Flask Dependencies
python -m venv venv
source venv/bin/activate 
pip install flask pg8000

4. Create Flask Application

5. HTML Templates for Flask
index.html
timetable.html

6. Running the Flask Application
python app.py

7. Accessing the Application
http://127.0.0.1:5000/
(import Flask did not work, I tried to fix it through video)

8. Stop the Docker Container
docker stop university-db
