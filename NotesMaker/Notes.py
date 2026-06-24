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

    print("FILES FOUND:", files)

    return render_template(
        "folder.html",
        folder=folder_name,
        files=files
    )

@app.route("/file/<folder>/<filename>")
def file(folder, filename):

    return send_from_directory(
        os.path.join(STORAGE, folder),
        filename
    )

if __name__ == "__main__":
    app.run(debug=True)