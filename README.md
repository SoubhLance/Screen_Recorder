# Screen Recorder with GUI

This project is a Python-based screen recording tool with a graphical user interface (GUI) built using Tkinter. The application allows users to record their screen activity in real time and save it as a video file in `.avi` format.

## Features
- **Record Screen Activity**: Records the entire screen and saves the recording as a video.
- **Real-time Preview**: Displays the recording preview in a window.
- **GUI Interface**: Start and stop recording using an intuitive GUI.
- **Multithreading**: Ensures smooth recording and GUI operation using threads.
- **Save Path Management**: Saves recorded videos to a defined directory without overwriting existing files.

## Dependencies

To run this project, the following Python packages are required:
- `opencv-python`
- `numpy`
- `pyautogui`
- `tkinter`

You can install these dependencies by running:

```bash
pip install opencv-python numpy pyautogui
```
## Installation

1. Clone this repository or download the source code.
   ```bash
     git clone <repository_url>
     cd <repository_folder>

2. Install the required dependencies as mentioned above.
3. Create a directory to save the recorded videos:

```bash
    mkdir D:/ScreenRecord/
```

##Usage

1. Run the script using Python:
  ```bash
      python screen_recorder.py
```
2. The GUI will appear with two buttons:

    - Start Recording: Begins recording your screen.
    - Stop Recording: Stops the recording and saves the video to the defined directory.

3. The recorded video will be saved as `screen_record_<timestamp>.avi` in `D:/ScreenRecord/`.

##File Structure
```bash
      .
    ├── screen_recorder.py      # Main Python script for the screen recorder
    ├── README.md               # Documentation for the project
```

##Troubleshooting

  - Recording stops unexpectedly: Make sure there are no issues with system resources (CPU, memory) while running the application.
  - Incorrect screen dimensions: If the screen resolution is incorrect, check the screen resolution obtained by `pyautogui.size()` and adjust if necessary.
  
  
##Future Improvements

- Add support for customizable video file formats.
- Allow users to choose the save directory via the GUI.
- Add an option to record specific regions of the screen.
- Implement a pause/resume functionality.

##License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

```vbnet 
    You can copy and paste this directly into your `README.md` file. Let me know if you need further changes!
```






