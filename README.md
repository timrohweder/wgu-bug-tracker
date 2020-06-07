# Bug Tracking Web App

- This is a Django app for tracking and discussing software bugs
- It was created for WGU's C868 class
- Live site: https://wgu-bugtracker-project.herokuapp.com/

## How to Install and Run Locally

1. **Install Docker**\
   Download links and instructions can be found at https://www.docker.com/

2. **Install PostgreSQL**\
   Download links and instructions can be found at https://www.postgresql.org/

3. **Get a local copy of the source code**\
   Enter the following into a console:\
   `git clone https://github.com/timrohweder/wgu-bug-tracker.git directory-name`\
   Replace directory-name with a directory name of your choosing.

4. **Navigate into the root directory of the source files**\
   There should be a file titled `docker-compose.yml`

5. **Run the following command in a shell to spin up the docker container:**\
   `docker-compose up --build -d`\
   The Docker desktop application must be running to execute this command. This will start the docker container in a detached state, meaning it is running in the background. If you need to stop the docker container, run `docker-compose down` - if you need to troubleshoot the docker container, type `docker-compose logs`

6. **Open a web browser and navigate to localhost:8000 to view the website**\
   It may take several seconds or minutes for the site to be available after spinning up the docker container for the first time. Run the `docker-compose up --build` command WITHOUT the -d flag to see what is happening in real-time.

7. **Run the following command in a shell to run unit tests:**\
   `docker-compose exec web python manage.py test`

## Built With

- Python
- Django
- Docker
- Postgres
- Bootstrap
- HTML / CSS
- Deployed on Heroku

## To Do

- Improve the aesthetics
- Add more unit testing
- Add the ability to edit / delete comments

## License

[MIT License](https://choosealicense.com/licenses/mit/)
