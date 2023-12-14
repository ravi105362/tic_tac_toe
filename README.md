# Tic Tac Toe
    This game does not requires manual intervention. It uses random generator to decide the position.

## Requirements

Python 3.9.10+
Docker

## Steps to run the application
1. Clone the repo locally
2. Run the following command -> pip install -r requirements.txt
3. Make sure docker is running
4. Run the command "docker run --pull always --publish 5000:5000 maguirebrendan/random:latest"
5. Run the command python src/main.py to run the game

## To run tests
1.  Repeat steps 1,2
2.  Run the command "pytest" to run all the tests

## Future improvements
1. Add more exhaustive tests
2. Add some e2e tests
3. Containerize the app and host it as per the requirement
