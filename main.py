from datetime import datetime as dt
import json as js

def main():
    isNameSet = False
    isDescSet = False
    tasks = [[0]]
    while (True):
        name = input(str('Welcome to this to-do list. Please start by entering the name of the task: '))
        desc = input(str('Next, please enter a description of the task: '))
        while (True):
            dueDateInput = input(str('Additionally, please enter a due date and time (if applicable) in this format: MM-DD-YYYY HH:MM. If there is no due date, please enter "none" without the quotation marks: '))
            dueDateFormat = '%m-%d-%Y %H:%M'
            if dueDateInput.lower == 'none':
                break
            else:
                try:
                    dt.strptime(dueDateInput, dueDateFormat)
                except ValueError:
                    print('Invalid format. Please try again.')
                    continue
                else:
                    dueDate = dt.strptime(dueDateInput, dueDateFormat)
                    break
        while (True):
            tmp = False
            step = input(str('Lastly, please input the name of the step to complete the task (if applicable). If there are no steps associated with this task, or you do not wish to enter any more steps, please enter "none" without the quotation marks: '))
            if step.lower == 'none':
                break
            else:
                while (True):
                    isCompleted = input(str('Has this step been completed? Enter "y" for yes or "n" for no: '))
                    if isCompleted.lower == 'y':
                        tmp = True
                        break
                    elif isCompleted.lower == 'n':
                        tmp = False
                        break
                    else:
                        print('Please enter y or n only.')
                        continue
                tasks[0].append
                        


class ToDoList:
    # name of task
    name = None
    # id number for the task
    idNum = None
    # description of the task
    desc = None
    # the task's due date
    dueDate = None
    # steps involved if any to complete the task
    steps = None

    def __init__(self):
        pass

    def setIdNum():
        pass


if __name__ == '__main__':
    main()