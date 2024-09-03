
from colorama import Fore, Back, Style, init

init(autoreset=True)

tasks = []

def add():
    global tasks
    while True:
        title = input("\tEnter a task to add: ").strip().lower()
        status = "Incomplete"
        task = title, status
        if task not in tasks:
            tasks.append(task)
            print(f"\n\t{Style.BRIGHT}{Fore.BLUE}Task added: '{task[0]}', Status: {task[1]}\n")
        else:
            print(f"\n\t{Style.BRIGHT}'{title}' already exists.")

        add_more = input("\tAdd another task? (Y/N): ").strip().lower()
        if add_more != 'y':    
            print("\n")    
            break        


def delete():
    global tasks
    view()

    while True:
        if not tasks:
            print(f"\n\t{Style.BRIGHT}No tasks to delete.\n")
            break
        try:
            title = input("\n\tChoose a task to delete: ").strip().lower()
            important = False
            line_len = 20
            important = title.center(line_len,'*')
            complete = False

            for i, task in enumerate(tasks):
                if title in task and "Complete" in task:
                    status = "Complete"
                    tasks[i] = title, status
                    tasks.remove(task)
                    print(f"\n\t{Style.BRIGHT}{Fore.MAGENTA}'{title}' Deleted.")
                    complete = True
                    break
                elif title in task and "Incomplete" in task:
                    status = "Incomplete"
                    tasks[i] = title, status
                    tasks.remove(task)
                    print(f"\n\t{Style.BRIGHT}{Fore.MAGENTA}'{title}' Deleted.")
                    break
                elif important in task and "Incomplete" in task:
                    status = "Incomplete"
                    tasks[i] = important, status
                    tasks.remove(task)
                    print(f"\n\t{Style.BRIGHT}{Fore.MAGENTA}'{title}' Deleted.")
                    important = True
                    break
                elif important in task and "Complete" in task:
                    status = "Complete"
                    tasks[i] = important, status
                    tasks.remove(task)
                    print(f"\n\t{Style.BRIGHT}{Fore.MAGENTA}'{title}' Deleted.")
                    important = True
                    complete = True
                    break
            else:
                raise KeyError

        except KeyError:
            print(f"\n\t{Style.BRIGHT}'{title}' does not exist.")
    
        delete_more = input("\tDelete another task? (Y/N): ").strip().lower()
        if delete_more != 'y':
            print("\n")
            break

def view():
    global tasks
    if not tasks:
        print(f"\n\t{Style.BRIGHT}Your TO-DO List is Empty!\n")
    else:
        print(f"\n\t{Style.BRIGHT}{'Task Titles':<20} {'Current Status':<10}")

        for task in tasks:
            if task[1] == "Complete":
                print(f"\t{Fore.GREEN}{task[0]:<20} {task[1]:<10}")
            elif task[1] == "Incomplete":
                print(f"\t{Fore.CYAN}{task[0]:<20} {task[1]:<10}")
    print("\n")

def complete():
    global tasks
    if not tasks:
        print(f"\n\t{Style.BRIGHT}No tasks in TO-DO list to mark as complete.\n")
    else:
        view()

    while True:
        try:
            title = input("\tChoose a task to mark as complete: ").strip().lower()
            complete = False #Incomplete
            line_len = 20
            important = False
            important = title.center(line_len,'*')
        
            for i, task in enumerate(tasks):    
                if title in task and "Complete" in task:
                    status = "Complete"
                    tasks[i] = title, status
                    print(f"\n\t{Style.BRIGHT}{Fore.GREEN}'{title}' already marked as complete")
                    complete = True
                    break
                elif important in task and "Complete" in task:
                    status = "Complete"
                    tasks[i] = important, status
                    print(f"\n\t{Style.BRIGHT}{Fore.GREEN}'{title}' already marked as complete")
                    important = True
                    complete = True 
                    break
                if not complete:
                    if title in task:
                        status = "Complete"
                        tasks[i] = title, status
                        print(f"\n\t{Style.BRIGHT}{Fore.GREEN}'{title}' marked as Complete")
                        complete = True
                        break
                    elif important in task:
                        status = "Complete"
                        tasks[i] = important, status
                        print(f"\n\t{Style.BRIGHT}{Fore.GREEN}'{title}' marked as Complete")
                        important = True
                        complete = True
                        break
            else:
                raise KeyError
        except KeyError:
            print(f"\n\t{Style.BRIGHT}'{title}' does not exist.")

        complete_more = input("\tMark another task as complete? (Y/N): ").strip().lower()
        if complete_more != 'y':
            print("\n")
            break

def important():
    global tasks
    if not tasks:
        print(f"\n\t{Style.BRIGHT}No tasks in TO-DO list to mark as important.\n")
    else:
        view() 

    while True:
        title = input("\tChoose a task to mark as important: ").strip().lower()
        mark_important = False
        line_len = 20
        important = title.center(line_len,'*')
        try:
            for i, task in enumerate(tasks):
                if important in task and title in important:
                    line_len = 20
                    important = title.center(line_len,'*')
                    tasks[i] = important, task[1]
                    print(f"\n\t{Style.BRIGHT}{Fore.CYAN}'{title}' already marked as Important.")
                    mark_important = True
                    break
                elif important in task and title in important and "Complete" in task:
                    status = "Complete"
                    line_len = 20
                    important = title.center(line_len,'*')
                    tasks[i] = important, status
                    print(f"\n\t{Style.BRIGHT}{Fore.CYAN}'{title}' already marked as Important.")
                    important = True
                    break
                if not mark_important:
                    if title in task:
                        line_len = 20
                        important = title.center(line_len,'*')
                        tasks[i] = important, task[1]
                        print(f"\n\t{Style.BRIGHT}{Fore.CYAN}'{title}' marked as Important.")
                        mark_important = True
                        break
                    elif title in task and "Complete" in task:
                        line_len = 20
                        status = "Complete"
                        important = title.center(line_len,'*')
                        tasks[i] = important, status
                        print(f"\n\t{Style.BRIGHT}{Fore.CYAN}'{title}' marked as Important.")
                        important = True
                        break
            else:
                raise KeyError        
        except KeyError:
            print(f"\n\t{Style.BRIGHT}'{title}' does not exist.")
 
        more_important = input("\tMark another task as important? (Y/N): ").strip().lower()
        if more_important != 'y':
            print("\n")
            break

menu_options = [1, 2, 3, 4, 5, 6]
welcome_menu = [
    "Welcome to the To-Do List App!\n",
    "Menu:",
    "1. Add a task",
    "2. View tasks",
    "3. Mark a task as complete",
    "4. Delete a task",
    "5. Mark a task as important",
    "6. Quit"
]

while True:
    for string in welcome_menu:
        if "List" in string:
            print(f"\tWelcome to the To-Do {Fore.RED}List{Fore.RESET} App!\n")

        elif string in welcome_menu[2:]:    
            if " as " in string:
                bold = string.replace(" as ", Style.BRIGHT + " as " + Style.NORMAL)
                print(f"\t{Fore.RED}{bold[:2]}{Fore.RESET}{bold[2:]}")
            else:
                print(f"\t{Fore.RED}{string[:2]}{Fore.RESET}{string[2:]}")
    
        else:
            print(f"\t{string}")

    try:
        
        user_selection = input((f"\n\tSelect a {Fore.RED}number{Fore.RESET}: ") ) 
        selection = int(user_selection)

        if selection == 1:
            add()
        elif selection == 2:
            view()
        elif selection == 3:
            complete()
        elif selection == 4:
            delete()
        elif selection == 5:
            important()
        elif selection == 6:
            print("\n\tThank you for using My TO-DO List App! <3\n")
            break
        elif selection < 1 or selection > 6:
            raise ValueError
    except ValueError:
        print(f"\n\t{Style.BRIGHT}{Fore.YELLOW}Invalid option listed. Enter a number from the menu.\n")


