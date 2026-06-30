from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

STORAGE = os.path.join(
    os.path.dirname(__file__),
    "storage"
)

@app.route("/")
def home():

    folders = []

    for folder in os.listdir(STORAGE):

        folder_path = os.path.join(STORAGE, folder)

        if os.path.isdir(folder_path):
            folders.append(folder)

    return render_template(
        "home.html",
        folders=folders
    )

@app.route("/folder/<folder_name>")
def folder(folder_name):

    folder_path = os.path.join(
        STORAGE,
        folder_name
    )

    files = []

    if os.path.exists(folder_path):

        for file in os.listdir(folder_path):

            if file.lower().endswith(".pdf"):
                files.append(file)

    custom_order = {

        "Chemistry": [
            "chem1.pdf",
            "chem2.pdf",
            "chem3.pdf",
            "chem4.pdf",
            "chem5.pdf",
            "chem6.pdf",
            "chem7.pdf",
            "chem8.pdf",
            "chem9.pdf",
            "chem10.pdf",
            "chem11.pdf",
            "QuantumMechanicalModelLecture12.pdf",
            "ElectronicConfigurationLecture13.pdf"
        ]

        "Maths": [
            "mathlecture1and2.pdf",
            "mathlecture3.pdf",
            "mathlecture4.pdf",
            "mathlecture5.pdf",
            "mathlecture6.pdf",
            "mathlecture7.pdf",
            "mathlecture8.pdf",
            "mathlecture9.pdf",
            "QuadraticEquationsLecture10.pdf",
            "InequalityLecture11.pdf"
        ]

        "Physics": [
            "lecture 1.pdf",
            "lecture 2.pdf",
            "lecture 3.pdf",
            "lecture 4.pdf",
            "lecture 5 kinematics 1.pdf",
            "lecture 6 kinematics 2.pdf",
            "lecture 7 friction 1.pdf",
            "lecture 8 friction 2.pdf",
            "lecture 9 friction and calculus 3 (online class).pdf",
            "lecture 10 calculus 4.pdf",
            "lecture 11 calculus 5.pdf",
            "lecture 12 calculus 6.pdf"
        ]
    }

    if folder_name in custom_order:

        files.sort(
            key=lambda x: custom_order[folder_name].index(x)
            if x in custom_order[folder_name]
            else 999
        )

    return render_template(
        "folder.html",
        folder=folder_name,
        files=files
    )

@app.route("/file/<path:filepath>")
def file(filepath):

    folder = os.path.dirname(filepath)

    filename = os.path.basename(filepath)

    return send_from_directory(
        os.path.join(STORAGE, folder),
        filename
    )
    
@app.route("/weekly")
def weekly():

    weekly_path = os.path.join(
        STORAGE,
        "WeeklyTests"
    )

    weeks = []

    if os.path.exists(weekly_path):

        for folder in os.listdir(weekly_path):

            folder_path = os.path.join(
                weekly_path,
                folder
            )

            if os.path.isdir(folder_path):
                weeks.append(folder)

        weeks.sort(
            key=lambda x: int(x.replace("Week ", ""))
        )
    
    return render_template(
        "weekly.html",
        weeks=weeks
    )

@app.route("/weekly/<week>")
def weekly_folder(week):

    week_path = os.path.join(
        STORAGE,
        "WeeklyTests",
        week
    )

    files = []

    if os.path.exists(week_path):

        for file in os.listdir(week_path):

            if file.lower().endswith(".pdf"):
                files.append(file)

    custom_order = [
        "Physics Test.pdf",
        "Chemistry Test.pdf",
        "Mathematics Test.pdf"
    ]

    files.sort(
        key=lambda x: custom_order.index(x)
        if x in custom_order
        else 999
    )

    return render_template(
        "weekly_files.html",
        week=week,
        files=files
    )

if __name__ == "__main__":
    app.run(debug=True)
