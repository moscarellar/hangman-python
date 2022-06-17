# Hangman Game

Student: Raymundo Castillo Moscarella

![Mock-up image](/doc/xxxx.png)

 [Live webpage](https://.herokuapp.com)

## Introduction

This is project milestone 3 of Code Institute program. I decided to develop a game based on Hangman. The purpose of the game is to guess letters of a random choosed word.

## Table of Content
* [User Experience](#user-experience)

* [Design](#design)
        -  [Flow Diagram](#flow-diagram)
* [Technologies](#technologies)
        - [Languages](#languages)
        - [Frameworks and Tools](#frameworks-and-tools)
        - [Libraries](#libraries)
* [Features](#features)
        - [User Login](#user-login)
        - [User Sign Up](#user-sign-up)
        - [How To Play](#how-to-play)
        - [Game Options](#game-options)
        - [Welcome Message](#welcome-message)
        - [Game](#game)
* [Validation](#validation)
* [Testing](#testing)
        - [Manual Testing](#manual-testing)
        - [Automated testing](#automated-testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)


## User Experience
 
### User Stories
 
* As a first time user, I want to understand the display easily.
* As a first time user, I want to receive clear instructions.
* As a game user, I want to relate with the game I already know as hangman.
* As a game user, I want a simple game and easy to follow and understand.
 
### Site Owner Stories
 
The purpose of the site is to create a minimalistic app so Users can play easily.
 
## Design
 
### Flow Diagram
This diagram shows the structure and flow of the game logic within the application.
 
<details><summary>Diagram</summary>
<img src="documentation/diagram.png">
</details>
 
[Back to Table Of Content](#table-of-content)

## Technologies

### Languages
- Python, language used to develop the app.
 
### Frameworks and Tools
- [Diagrams.net](https://app.diagrams.net/) use for creation of diagram.
- [GitHub](https://github.com/) used as recommended to store and backup projects and code as repository.
- [Google APIs](https://cloud.google.com/cloud-console/) used to acess spreadsheets and create credentials.
- [Google Sheets](https://www.google.co.uk/sheets/about/) speadsheets used to store information of guestbook.
- [Heroku Platform](https://dashboard.heroku.com/) used to deploy project.
 
 ### Libraries

 - Imported these libraries: 1. random 2. gspread 3. Credentials 4. time and 5. from datetime import date

 [Back to table](#table-of-content)

## Features
 
### Intro Message
 
![Logo and Intro Message](./assets/images/readme/hangman-feature-1.jpg)
 
* When the users reach the website, they will see this feature. The game logo and the intro message are displayed here.<br>

### Logo 
 
### Username
- Asks the player for their username.
- Asks the player for their city.
- Updates row (append) with input information.
 
<details>
<summary>Username and city asked</summary>
 

### Guestbook
![Leaderboard](guestbook.png)
* The Leaderboard shows the 15 players with the best scores.
 
<details>
<summary>Player Database Screenshot</summary>
 
![Player Database](documentation/guestbook.png)
</details>
 

 
### Game
- Displays the title created for the game.
- Displays the numbers of lives remaining for the player.
- Displays the Letters that have already been used within this game.
- Displays the status of the gallows and the man getting hung.
- Displays the status of the word being guessed.
- Displays a warning when an invalid character is entered.
- Tells the player when the enter a letter that is not in the word.
- Provides feedback when the game has been won.
- Gives the option to play again and prints the users total when the next game starts.
- User stories covered: 1, 5, 6, 7, 8, 12, 13
 
 

 
### Hangman Stage 1
![Game Feature](./assets/images/readme/hangman-feature-5.jpg)<br><br>
 
This feature displays where the main scene happens. Here the user can play and see the following information about the game:
* Numbers of letters chosen by the computer
* Hangman stages
* Letters guessed right
* Letters guessed wrong
* Current score
* Current number of attempts
* Input to guess a letter or a full word
* Input letters to either guess a letter only or the full word
 
<details>
<summary>Game Screenshot</summary>
 
![Game](documentation/hangmanstages.png)
</details>
<details>
 
[Back](#table-of-content)

## Testing

### Manual Testing
After testing user stories, I went ahead to run the program several times and asked close people to play it as well.

### Validator
 
The [PEP8](http://pep8online.com/) Validator Service was used to validate every Python file in the project to ensure there were no syntax errors in the project.
 
![PEP8](/hangman-pep8-results.png)
* No errors or warnings were found during the testing of the code in PEP8

## Bugs
 
debug
printint 2 times hanman image
deleted it from line 101 of code, it was repeated
 
issues with position of variable word
trying several times
 
[Back](#table-of-content)

## Deployment
 
### Heroku
This application has been deployed from GitHub to Heroku by following the steps:
 
 
[Back to Table Of Content](#table-of-content)

## Acknowledgements
I would like to thank everyone who supported me in the development of this project:
-
-
- Code Institute community on Slack for resources and support

[Back to Table Of Content](#table-of-content)


