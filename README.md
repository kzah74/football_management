# Football Management application
The Football Management application allows users to create a database of desired football teams, manage them and schedule their matches. Adding a new team is made easy - only with a click of a button. The app lets users generate match schedules, by randomly picking the opponents from the available list, making sure that each team is scheduled for a game only once a day.
## User guide
-   To add a new team to the database click “Add a new team” under “Football Management”. 
-   Under “Teams” the user can see the list of all available teams at the moment.
-   In the “Generate Matches” tab the user can create a random match schedule by clicking the button.
-   Under “Match schedule” the user can see the already generated schedule.
-   Summary of all planed games can be found under “Match list”.

## Developers guide
### Prerequisites
-   Python
-   Django
### Run the project (Windows environment)
-   Navigate to the app folder
    ```sh
    mf_env\Scripts\activate
    ```
    ```sh
    python manage.py runserver
    ```
-   Open in browser http://localhost:8000/

    

The product is web-based, no additional installation is required. 

