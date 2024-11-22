import PySimpleGUI as sg
import os.path

# First, the window layout in 2 columns

# Column for the folder selection and file list
file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# Column for displaying image
image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

# Create the window
window = sg.Window("Image Viewer", layout)

# Event loop to handle events and update the interface
while True:
    event, values = window.read()

    # Exit condition
    if event == sg.WINDOW_CLOSED:
        break

    # Handle folder selection
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        if os.path.isdir(folder):
            # Update file list with image files from the selected folder
            file_list = [
                f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))
            ]
            window["-FILE LIST-"].update(file_list)

    # Handle file selection
    if event == "-FILE LIST-":
        try:
            # Get selected file and display it
            filename = values["-FILE LIST-"][0]
            filepath = os.path.join(values["-FOLDER-"], filename)
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filepath)
        except IndexError:
            pass

# Close the window
window.close()