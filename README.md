# Login System with Face Recognition

Welcome to the Login System with Face Recognition project. This project provides a secure login system using face recognition for employee access. It includes an admin panel for employee registration and login management.

## Details

This project is implemented in Python and uses various libraries and modules. Before getting started, make sure to install the required dependencies:

### Modules to Install

- `cv2`: OpenCV for video capture.
- `pymysql`: To connect to a MySQL database.
- `numpy`: For numerical operations.
- `tkinter`: GUI library for the user interface.
- `face_recognition`: For face recognition functionality.
- `playsound`: For playing voice notifications.
- `multiprocessing`: For handling audio processes in parallel.

## Features

- Employee login via face recognition.
- Admin panel for employee registration.
- Secure database storage of employee information.
- Voice notifications for successful logins.

## Getting Started

1. Clone this repository to your local machine.
2. Install the required modules as mentioned in the "Modules to Install" section.
3. Set up a MySQL database with the appropriate credentials and update them in `credentials.py`.
4. Prepare employee face data and store it using `encode_faces()` from `videoStream.py`.
5. Run the project by executing `login_system.py`.

## How to Use

- Start the application by running `login_system.py`.
- Click on the "Login" button to log in using face recognition.
- Click on the "Register" button to access the admin panel.
- In the admin panel, register new employees with their details.
- The system will recognize registered employees and allow access.


## Contributions

We welcome contributions! If you'd like to enhance or fix issues in this project, please follow these steps:

1. Fork this repository.
2. Create a branch with your feature or bug fix: `git checkout -b your-feature`.
3. Commit changes: `git commit -m 'Added new feature'`.
4. Push to the branch: `git push origin your-feature`.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgment

- Thanks to the python Open source developers for providing  modules making developing in python easy.
