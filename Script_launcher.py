import os
import subprocess

def display_menu():
    print("Select an option:")
    print("1. Launch Pathfinder app (pathfinder.py)")
    print("2. Log in to container (login.sh)")
    print("3. Delete container (delete_container.sh)")
    print("4. Exit")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                subprocess.run(["python3", "pathfinder.py"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error running pathfinder.py: {e}")

        elif choice == '2':
            try:
                subprocess.run(["./login.sh"], check=True, shell=True)
            except subprocess.CalledProcessError as e:
                print(f"Error running login.sh: {e}")

        elif choice == '3':
            try:
                subprocess.run(["./delete_container.sh"], check=True, shell=True)
            except subprocess.CalledProcessError as e:
                print(f"Error running delete_container.sh: {e}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
