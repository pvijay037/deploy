# School Project

![School Project Logo](/path/to/your/logo.png)

This Django-based application manages mentor-student relationships, user authentication, and basic CRUD functionalities for students. It also includes features for video uploads and display on user profiles.

## Task-1 

1. **Account App**
    ```bash
    http://127.0.0.1:8000/api/register/
    ```
    ![School Project Logo](/School/images/Screenshot%202023-12-09%20014321.png)

    ```bash
    http://127.0.0.1:8000/api/login/
    ```
    ![School Project Logo](/School/images/Screenshot%202023-12-09%20014638.png)


    ```bash
    http://127.0.0.1:8000/api/user/
    ```
    ![School Project Logo](/School/images/Screenshot%202023-12-09%20015750.png)


    ```bash
    http://127.0.0.1:8000/api/logout/
    ```
    ![School Project Logo](/School/images/Screenshot%202023-12-09%20020014.png)

2. **Mentor App:**
    ```bash
    http://127.0.0.1:8000/mentor/mentors/
    ```
    ![School Project Logo](/School/images/Screenshot%202023-12-09%20020655.png)

    ```bash
    http://127.0.0.1:8000/mentor/mentors/1/add_student/
    ```
    ![School Project Logo](/School/images/Screenshot%202023-12-09%20021030.png)

    ```bash
    http://127.0.0.1:8000/mentor/students/
    ```
    ![School Project Logo](/School/images/Screenshot%202023-12-09%20021218.png)


3. **Student App:**
    ```bash
    http://127.0.0.1:8000/student/students/
        http://127.0.0.1:8000/student/students/create/

    http://127.0.0.1:8000/student/students/1/

    http://127.0.0.1:8000/student/students/1/update/

    http://127.0.0.1:8000/student/students/1/delete/
    ```

## Usage

1. **Run the Django server:**
    ```bash
    python manage.py runserver
    ```

2. **Access the application at:** `http://localhost:8000`

## Features

- **User Management:**
  - Registration
  - Login with token-based authentication
  - Get user details

- **Mentor and Student Interaction:**
  - Mentor-specific routes for adding students
  - Student CRUD operations (Edit, Update, Delete)

- **Frontend UI:**
  - Basic HTML/CSS/Bootstrap interface for demonstration
  ![Sample UI](/path/to/your/sample_ui.png)

- **Video Upload and Display:**
  - Upload videos and view them on user profiles

## API Endpoints

- `/api/register/`: User registration
- `/api/login/`: User login
- `/api/user-details/`: Get user details
- `/mentor/api/...`: Mentor-specific routes
- `/student/api/...`: Student-specific routes
- ...

## Database Models

- `Mentor`: Fields include (list fields).
- `Student`: Fields include (list fields).
- ...

## Deployment

The project is deployed at [Hosting Platform](https://your-hosted-url.com).

## Contributing

Contributions are welcomed! Feel free to open issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the [License Name]. See the [LICENSE](LICENSE) file for details.
