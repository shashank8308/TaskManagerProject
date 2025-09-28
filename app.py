import os
import csv
import hashlib
from datetime import datetime

# ---------------- Utility ----------------
def hash_password(password: str) -> str:
    """Return SHA-256 hash of a password."""
    return hashlib.sha256(password.encode()).hexdigest()


# ---------------- User Authentication ----------------
class UserAuth:
    USERS_FILE = "users.txt"

    def __init__(self):
        os.makedirs("tasks", exist_ok=True)
        os.makedirs("expenses", exist_ok=True)

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if os.path.exists(self.USERS_FILE):
            with open(self.USERS_FILE, "r") as f:
                for line in f:
                    if line.split(",")[0] == username:
                        print("❌ Username already exists. Try again.")
                        return None

        with open(self.USERS_FILE, "a") as f:
            f.write(f"{username},{hash_password(password)}\n")

        print("✅ Registration successful!")
        return None

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if not os.path.exists(self.USERS_FILE):
            print("❌ No users registered yet.")
            return None

        with open(self.USERS_FILE, "r") as f:
            for line in f:
                stored_user, stored_hash = line.strip().split(",")
                if stored_user == username and stored_hash == hash_password(password):
                    print("✅ Login successful!")
                    return username

        print("❌ Invalid credentials.")
        return None


# ---------------- Task Manager ----------------
class TaskManager:
    def __init__(self, username: str):
        self.username = username
        self.file = os.path.join("tasks", f"{username}_tasks.txt")

    def add_task(self):
        desc = input("Enter task description: ")
        task_id = str(int(datetime.now().timestamp()))
        with open(self.file, "a") as f:
            f.write(f"{task_id},{desc},Pending\n")
        print("✅ Task added successfully!")

    def view_tasks(self):
        if not os.path.exists(self.file):
            print("No tasks yet.")
            return
        with open(self.file, "r") as f:
            tasks = f.readlines()
        print("\nYour Tasks:")
        for t in tasks:
            tid, desc, status = t.strip().split(",")
            print(f"[{tid}] {desc} - {status}")

    def mark_completed(self):
        tid = input("Enter Task ID to mark completed: ")
        if not os.path.exists(self.file):
            print("No tasks available.")
            return
        updated, found = [], False
        with open(self.file, "r") as f:
            for line in f:
                task_id, desc, status = line.strip().split(",")
                if task_id == tid:
                    updated.append(f"{task_id},{desc},Completed\n")
                    found = True
                else:
                    updated.append(line)
        with open(self.file, "w") as f:
            f.writelines(updated)
        print("✅ Task updated!" if found else "❌ Task not found.")

    def delete_task(self):
        tid = input("Enter Task ID to delete: ")
        if not os.path.exists(self.file):
            print("No tasks available.")
            return
        updated, found = [], False
        with open(self.file, "r") as f:
            for line in f:
                task_id, desc, status = line.strip().split(",")
                if task_id == tid:
                    found = True
                else:
                    updated.append(line)
        with open(self.file, "w") as f:
            f.writelines(updated)
        print("✅ Task deleted!" if found else "❌ Task not found.")


# ---------------- Expense Tracker ----------------
class ExpenseTracker:
    def __init__(self, username: str):
        self.username = username
        self.file = os.path.join("expenses", f"{username}_expenses.csv")

    def _load_expenses(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return list(csv.reader(f))
        return []

    def _save_expenses(self, expenses):
        with open(self.file, "w", newline="") as f:
            csv.writer(f).writerows(expenses)

    def add_expense(self):
        date = datetime.now().strftime("%Y-%m-%d")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        desc = input("Enter description: ")

        expenses = self._load_expenses()
        expenses.append([date, category, amount, desc])
        self._save_expenses(expenses)
        print("✅ Expense added successfully!")

    def view_expenses(self):
        expenses = self._load_expenses()
        if not expenses:
            print("No expenses yet.")
            return
        print("\nYour Expenses:")
        for e in expenses:
            print(f"{e[0]} | {e[1]} | ${e[2]} | {e[3]}")

    def track_budget(self):
        budget = float(input("Enter your monthly budget: "))
        expenses = self._load_expenses()
        total = sum(float(e[2]) for e in expenses)

        if total > budget:
            print(f"⚠ Budget exceeded! Spent ${total} / Budget ${budget}")
        else:
            print(f"Remaining balance: ${budget - total}")


# ---------------- Main App ----------------
class App:
    def __init__(self):
        self.auth = UserAuth()
        self.current_user = None
        self.task_manager = None
        self.expense_tracker = None

    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose: ")

            if choice == "1":
                self.auth.register()
            elif choice == "2":
                user = self.auth.login()
                if user:
                    self.current_user = user
                    self.task_manager = TaskManager(user)
                    self.expense_tracker = ExpenseTracker(user)
                    self.task_menu()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    def task_menu(self):
        while True:
            print("\n--- Task Manager ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Expense Tracker")
            print("6. Logout")
            choice = input("Choose: ")

            if choice == "1":
                self.task_manager.add_task()
            elif choice == "2":
                self.task_manager.view_tasks()
            elif choice == "3":
                self.task_manager.mark_completed()
            elif choice == "4":
                self.task_manager.delete_task()
            elif choice == "5":
                self.expense_menu()
            elif choice == "6":
                print("Logged out.")
                break
            else:
                print("Invalid choice.")

    def expense_menu(self):
        while True:
            print("\n--- Expense Tracker ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Track Budget")
            print("4. Back")
            choice = input("Choose: ")

            if choice == "1":
                self.expense_tracker.add_expense()
            elif choice == "2":
                self.expense_tracker.view_expenses()
            elif choice == "3":
                self.expense_tracker.track_budget()
            elif choice == "4":
                break
            else:
                print("Invalid choice.")


# ---------------- Run ----------------
if __name__ == "__main__":
    App().main_menu()
