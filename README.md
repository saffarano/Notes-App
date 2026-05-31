 Notes-App
Simple CRUD notes application that uses Flask and SQLAlchemy. Users are able to perform all CRUD operations for notes within the main page. Additional functionality added to play Hangman. Game logic stored in Python class that Flask references and stores in sessions. Jinja templates used to show game state.

#Tech Stack:
- Flask
- Python
- SQLAlchemy
- Jinja2
- HTML / CSS

#CRUD Features:
- Create New Notes
- Read Notes
- Update (Modify) Notes
- Delete Notes

#Game Features:
- New Game
- Session Based Game State
- Prompt Messages Based on Inputs (Win/Lose/Duplicate/Invalid)

#How to run:
- python -m venv venv
- source venv/bin/activate   # or venv\Scripts\activate on Windows
- pip install -r requirements.txt
- python notesapp.py

#Screenshots:

- Home Page:
![Home Page](https://github.com/saffarano/Notes-App/blob/main/Images/Notes_Homepage.png)

- Editing Note:
![Editing Note](https://github.com/saffarano/Notes-App/blob/main/Images/Notes_Edit.png)

- Deleted Note:
![Deleted Note](https://github.com/saffarano/Notes-App/blob/main/Images/Note_Deleted.png)

- New Hangman Game:
![New Game](https://github.com/saffarano/Notes-App/blob/main/Images/hangman_new.png)

- Hangman Gameplay:
![Gameplay](https://github.com/saffarano/Notes-App/blob/main/Images/hangman_gameplay.png)

- Won Hangman Game:
![Win Game](https://github.com/saffarano/Notes-App/blob/main/Images/hangman_win.png)

- Lost Hangman Game:
![Lose Game](https://github.com/saffarano/Notes-App/blob/main/Images/hangman_lose.png)
