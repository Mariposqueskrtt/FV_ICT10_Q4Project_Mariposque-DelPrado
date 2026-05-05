from pyscript import display, document
import matplotlib.pyplot as plt
import logging

logging.getLogger('matplotlib').setLevel(logging.ERROR)

#classmates
class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.subject}."


classmates = [
    Classmate("Alexandra Vargas", "Emerald", "Social Studies"),
    Classmate("Xylee Goyenechea", "Emerald", "Science"),
    Classmate("KC Del Prado", "Emerald", "Social Studies"),
    Classmate("Rycob Pagtalunan", "Emerald", "Math"),
    Classmate("Miguel Buo", "Emerald", "English")
]


def get(id):
    return document.getElementById(id).value


def clear_inputs():
    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""


def show_list(event=None):
    output = "<h3>Classmates:</h3>"

    for c in classmates:
        output += f"<p>{c.introduce()}</p>"

    document.getElementById("list").innerHTML = output


def add_classmate(event=None):
    name = get("name")
    section = get("section")
    subject = get("subject")

    if not name or not section or not subject:
        document.getElementById("list").innerHTML = "Kindly please answer all the questions"
        return

    classmates.append(Classmate(name, section, subject))
    clear_inputs()

    document.getElementById("list").innerHTML = "You have been added successfully!"



#attendance
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
absences = [1, 2, 3, 4, 5]


def submit_graph(e):
    selected_day = document.getElementById("class_day").value
    new_value = document.getElementById("absence_input").value

    try:
        day_index = [d.lower() for d in days].index(selected_day.lower())
        absences[day_index] = float(new_value)
    except:
        pass

    plt.clf()
    plt.plot(days, absences)
    plt.title('Days of the Week')

    display(plt, target="output", append=False)