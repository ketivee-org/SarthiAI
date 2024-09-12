import os

class SarthiInteraction:
    def __init__(self):
        self.greet_user()

    def greet_user(self):
        print("Hello! I am Sarthi, your assistant. How can I help you today?")

    def get_user_input(self):
        return input("You: ")

    def respond_to_user(self, user_input):
        if "create file" in user_input.lower():
            self.create_file()
        elif "read file" in user_input.lower():
            self.read_file()
        elif "write to file" in user_input.lower():
            self.write_to_file()
        elif "exit" in user_input.lower():
            print("Goodbye!")
            exit()
        else:
            print("I'm sorry, I didn't understand that. Can you please repeat?")

    def create_file(self):
        file_name = input("Enter the name of the file to create: ")
        with open(file_name, 'w') as file:
            print(f"File '{file_name}' created successfully.")

    def read_file(self):
        file_name = input("Enter the name of the file to read: ")
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                print(file.read())
        else:
            print(f"File '{file_name}' does not exist.")

    def write_to_file(self):
        file_name = input("Enter the name of the file to write to: ")
        if os.path.exists(file_name):
            content = input("Enter the content to write: ")
            with open(file_name, 'a') as file:
                file.write(content + "\n")
            print(f"Content written to '{file_name}' successfully.")
        else:
            print(f"File '{file_name}' does not exist.")

if __name__ == "__main__":
    sarthi = SarthiInteraction()
    while True:
        user_input = sarthi.get_user_input()
        sarthi.respond_to_user(user_input)