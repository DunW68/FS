# Set up on a local machine:
    1) create new folder with venv
    2) acticate venv
    2) git clone --branch main https://github.com/DunW68/FS.git (inside folder from step 1)
    3) cd FS ("./FS")
    4) pip install -r requirements.txt
    5) python manage.py makemigrations
    6) python manage.py migrate
    Project is ready to work
    
# Functionality for the system administrator:
     1) 127.0.0.1:8000/admin/polls/poll/
        endpoint for adding / changing / deleting polls.
     2) 127.0.0.1:8000/admin/polls/question/
        endpoint for adding / changing / deleting questions in the polls.

# Functionality for system users:
    1) GET 127.0.0.1:8000/api/polls/
    endpoint for getting a list of active polls
    2) GET 127.0.0.1:8000/api/polls/{int:pk}
    endpoint for getting a specific poll
    3) POST 127.0.0.1:8000/api/polls/{int:pk}
        endpoint for passing the poll
        *required parameters:
          question, choice
              Example:
                {
                "question":"1",
                "choice":"text"
                }
    4) POST 127.0.0.1:8000/api/polls/show_results
        endpoint for retrieving user-completed surveys with drilldown by response using user`s ip
          *required parameters:
              ip
              Example:
                {
                "ip":"1"
                }
     5) GET 127.0.0.1:8000/api/polls/show_results
         endpoint for retrieving user-completed surveys with drilldown by response for current user
