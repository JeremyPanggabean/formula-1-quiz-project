#  Formula 1 True/False Quiz in Python 🏎️

As someone who just recently got into the world of Formula 1, I decided to combine my interest in F1 with my journey in learning Python.

This project is a **terminal-based True/False quiz** about Formula 1 — covering drivers, teams, race history, and general F1 knowledge. It's built using **Object-Oriented Programming (OOP)** in Python and is a great exercise for beginners learning about classes, functions, and modular programming.

---

## 🎯 Features

- ✅ 30 curated True/False questions about Formula 1
- ✅ Tracks score and gives instant feedback
- ✅ Uses OOP: `Question`, `QuizBrain`, and a main loop
- ✅ Includes a custom ASCII intro for F1 vibes

---

## 🛠️ How It Works

The project has the following modules:

- **`main.py`** — Main loop, game flow control
- **`data.py`** — Contains F1 questions and show_f1_intro function
- **`question_model.py`** — Defines the `Question` class
- **`quiz_brain.py`** — Contains the quiz logic (`QuizBrain` class)

---

## 🖼️ Sample Output


```text
🏁 Welcome to the Ultimate Formula 1 Quiz! 🏎️🏎️
Test your knowledge of F1 legends, races, and records!

⠀⢀⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⡿⢀⣠⣴⣾⣿⣿⣿⣿⣇⡀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⠟⢋⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⡿⠓⡐⠒⢶⣤⣄⡀⠀⠀
⠀⠸⠿⠇⢰⣿⣿⡆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⡷⠈⣿⣿⣉⠁⠀
⠀⠀⠀⠀⠀⠈⠉⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠈⠉⠁⠀⠈⠉⠉⠀⠀

Q.1: Lewis Hamilton has won more than 7 World Drivers' Championships. (True/False)?: false  
You got it right!  
The correct answer was: False.  
Your current score is: 1/1 Quiz.  

Q.2: Sebastian Vettel started his F1 career with BMW Sauber. (True/False)?: true  
You got it right!  
The correct answer was: True.  
Your current score is: 2/2 Quiz.  

...

Q.30: Spa-Francorchamps is located in Belgium. (True/False)?: true  
You got it right!  
The correct answer was: True.  
Your current score is: 18/30 Quiz.  


You've completed the quiz  
Your final score was: 18/30


```

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/JeremyPanggabean/formula-1-quiz-project.git
   
2. Change the directory project:
    ```bash
   cd formula-1-quiz-project
3. Run the main script:
    ```bash
   python main.py

# 🏁 Credits
Quiz logic inspired by beginner object oriented programming (OOP) Python practice projects.

Formula 1 trivia sourced and verified from public F1 records and fan sources.

ASCII car art from creative commons and adapted manually.
