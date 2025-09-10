# 🎮 Tic Tac Toe (Flask)

This is a simple **Tic Tac Toe game** built with **Python** using the **Flask** framework.  
The game runs on a local web server and allows two players to play against each other by choosing **X** or **O**.  

---

## 🚀 Technologies Used
- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- HTML (templates)

---

## 📂 Project Structure
```
.
├── app.py              # Main Flask application
├── check_winf.py       # Function that checks for a winner
├── check_impf.py       # Function that validates moves
├── templates/
│   └── index.html      # Game web interface
```

---

## 🕹️ How to Play
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-flask.git
   cd tic-tac-toe-flask
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Run the server:
   ```bash
   python app.py
   ```

4. Open in your browser:
   ```
   http://127.0.0.1:5000
   ```

## 📌 Future Improvements
- Add **CSS styling**.  
- Implement **player vs computer (AI)**.  
- Show a match history.  
- Improve move validation on the front-end.  
