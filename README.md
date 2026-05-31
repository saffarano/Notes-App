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
![Home Page](images/Notes_Homepage.png)
![Editing Note](images/Notes_Edit.png)
![Deleted Note](images/Note_Deleted.png)
![New Game](images/hangeman_new.png)
![Gameplay](images/hangman_gameplay.png)
![Win Game](images/hangman_win.png)
![Lose Game](images/hangman_lose.png)