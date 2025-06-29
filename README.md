# quiz_quest
Tkinter-based quiz app for OSSD final project
# 🧠 Quiz Quest – Educational Quiz Game

Quiz Quest is a collaborative Tkinter-based GUI application designed to provide users with an interactive quiz experience across multiple topics. Developed as part of our **Open Source Software Development (OSSD)** final term project, this application demonstrates the power of teamwork, GUI programming, and version-controlled development.

---

##  Features

- ✨ Graphical user interface using **Tkinter**
- 📚 Multiple quiz topics like **General Knowledge** and **Math**
- 📂 Dynamic question loading via a **JSON backend**
- 📝 How-to-Play instructions screen
- ✅ Score calculation with a results window
- 🔄 Modular design with 5 separate components
- 🛠 GitHub-based collaboration using branches, issues & pull requests

---

## 💡 Technologies Used

| Layer       | Technology        |
|-------------|-------------------|
| Frontend    | Python with Tkinter |
| Backend     | JSON file (`questions.json`) |
| Version Control | Git & GitHub (Public Repo) |

---

## 🚀 How to Run the App

### 🔧 Requirements
- Python 3.x
- `tkinter` (comes pre-installed with Python)

### 📂 File Structure
quiz-quest/
├── main.py
├── quiz.py
├── topic_selector.py
├── result.py
├── instructions.py
├── questions.json


<img width="602" alt="main" src="https://github.com/user-attachments/assets/be0c26f3-0b40-40bb-bc9c-28a0c38ddb31" />


<img width="453" alt="quiz" src="https://github.com/user-attachments/assets/28e16727-88e1-42fb-bbce-fa23d26e640e" />


<img width="679" alt="topic" src="https://github.com/user-attachments/assets/98a4761f-4c82-47d4-a601-64871316c494" />


<img width="679" alt="result" src="https://github.com/user-attachments/assets/b0e1e71a-0e57-40a7-bcb5-7ba5ce422fcb" />


<img width="595" alt="instructions" src="https://github.com/user-attachments/assets/4cdff2e3-bb6c-4b45-914a-66254ab7589d" />


<img width="308" alt="quest" src="https://github.com/user-attachments/assets/af50e688-1526-4cc8-a94b-22b74dbda40e" />


### ▶️ Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Tooba0803/quiz_quest.git
   cd quiz_quest
Run the app:

Bash
python main.py

📸 Screenshots

<img width="960" alt="aa" src="https://github.com/user-attachments/assets/f86acc72-c8b7-4f20-b9b2-41f4d265f078" />

![094b4b81-deff-4ed1-9d15-6cd1a4f12c9e](https://github.com/user-attachments/assets/e2f11663-624e-4501-97c9-eabaf16321d5)

![WhatsApp Image 2025-06-29 at 4 28 14 PM](https://github.com/user-attachments/assets/22095e07-9821-4e92-ba6e-45fa24a92f74)

![02347c01-0e65-4009-89bc-22d8c4a25070](https://github.com/user-attachments/assets/925554e6-cc28-4945-b7ed-1707c09d084e)

![fefccb3e-ff9b-42fb-ba62-5c59d6e88385](https://github.com/user-attachments/assets/4d96310d-da5f-4ece-9fac-8abc8387f740)

![dff73485-bf7f-4e8f-9823-87a2641b8a42](https://github.com/user-attachments/assets/7e9e6308-ec07-4108-b18e-de425c8c2493)

![6daab43a-5b25-46d3-a389-7e861d957512](https://github.com/user-attachments/assets/ab098153-e835-4ba0-9314-f7568d10fca7)

![397dff0d-4669-4bcd-94f3-eb2e7576283d](https://github.com/user-attachments/assets/732f325a-c84b-47dc-9c70-d288a8badd8d)


👥 Team Contributions
| Member      | GitHub Branch          | Responsibility                        |
| ----------- | ---------------------- | ------------------------------------- |
| **Tooba**   | `tooba-main`           | Project lead, `main.py`, coordination |
| **Ahmad**   | `ahmad-quiz`           | `quiz.py`, quiz logic and interface   |
| **Nafeesa** | `nafeesa-instructions` | `instructions.py`, how-to window      |
| **Zoha**    | `zoha-result`          | `result.py`, result popup             |
| **Kashaf**  | `kashaf-topic`         | `topic_selector.py`, topic handling   |


📌 Issues & Pull Requests
🔧 Major PRs

#1 Ahmad - Quiz logic

#2 Kashaf - Topic selection

#3 Nafeesa - Instructions module

#4 Zoha - Result window

#5 Tooba - Main window

📌 Issues Created
 Implement quiz logic

 Add topic selection

 Add instructions window

 Change bg color

 Connect all files from main UI

📦 Backend Details
All quiz data is stored in a JSON file questions.json

Structure includes multiple topics and default quiz

Easily expandable for more subjects or questions

