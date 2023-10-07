# course-manager api

- create a venv ativate it then install the requirements

`python -m venv myenv`

`myenv\Scripts\activate`

`pip install -r requirements.txt`


- then in the working directory run this command to run the uvicorn server

`foreman start`

- finally go to the following link to test the api

`http://localhost:5000/docs` 

- to populate the database with some sample data run populate.py

`python populate.py`

- if you want to view what was populated in the db run test_queries.py

`python test_queries.py`

# Testing variables
- student_id 1 is on 3 waitlists
- class_id 2 (with instructor_id 2) has 4 dropped students

# windows execution policy
- if you are running this on a windows machine you may have to set the execution policy to run your virutal enviroment

` Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
