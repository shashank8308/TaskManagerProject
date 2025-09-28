# TaskManagerProject
ask Manager with User Authentication & Expense Tracker
📌 Overview

This is a Python-based menu-driven application that helps users manage their tasks and track expenses.
Each user has a secure login, and all tasks/expenses are stored separately per user using file handling.

🚀 Features
🔐 User Authentication

Register new users with SHA-256 password hashing.

Login validation before accessing personal data.

✅ Task Manager

Add new tasks with a unique ID.

View all tasks (Pending & Completed).

Mark tasks as completed.

Delete tasks.

💰 Expense Tracker

Add expenses with date, category, amount, and description.

View all expenses saved in CSV format.

Set and track monthly budget (get warnings if exceeded).

📂 File Handling

users.txt → Stores usernames & password hashes.

tasks/<username>_tasks.txt → Stores tasks for each user.

expenses/<username>_expenses.csv → Stores expenses for each user.

🏗️ Project Structure
TaskManagerProject/
│── app.py                  # Main application file
│── users.txt               # User credentials (username + hashed password)
│── tasks/                  # Task files (created per user)
│    └── john_tasks.txt
│── expenses/               # Expense files (created per user)
     └── john_expenses.csv

⚙️ Installation & Usage

Clone the repo

git clone https://github.com/your-username/TaskManagerProject.git
cd TaskManagerProject


Run the application

python app.py


or (if using Python 3):

python3 app.py


Use the menus

Register a new account

Login with your credentials

Manage tasks and expenses

📖 Example Flow
--- Main Menu ---
1. Register
2. Login
3. Exit
Choose: 1
Enter username: john
Enter password: 12345
✅ Registration successful!

--- Main Menu ---
1. Register
2. Login
3. Exit
Choose: 2
Enter username: john
Enter password: 12345
✅ Login successful!

--- Task Manager ---
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Expense Tracker
6. Logout

🔮 Future Enhancements

Add task due dates and priorities.

Store budget limits per user permanently.

Search & filter for expenses.

Create a GUI (Tkinter/PyQt) or convert to a web app (Flask/Django).

🛠️ Tech Stack

Python 3

File handling (TXT & CSV)

Hashlib (for password hashing)
