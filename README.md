# Project



This Django-based application manages mentor-student relationships, user authentication, and basic CRUD functionalities for students. It also includes features for video uploads and display on user profiles.

## Task-1 

1. **Account App**
    ```bash
    http://127.0.0.1:8000/api/register/
    ```
    <img width="636" alt="Screenshot321" src="https://github.com/pvijay037/deploy/assets/95902517/d7e4f7da-a615-4a7b-9e39-6a2ad90cd90b">
    ```bash
    http://127.0.0.1:8000/api/login/
    ```
    <img width="640" alt="Screenshot 2023-12-09 014638" src="https://github.com/pvijay037/deploy/assets/95902517/443dd3b9-d5b8-44b6-94d3-50d4d621207f">
    ```bash
    http://127.0.0.1:8000/api/user/
    ```
    <img width="647" alt="Screenshot 2023-12-09 015750" src="https://github.com/pvijay037/deploy/assets/95902517/9799e685-e25d-45d1-aff5-63e012e1f367">
    ```bash
    http://127.0.0.1:8000/api/logout/
    ```
    <img width="653" alt="Screenshot 2023-12-09 020014" src="https://github.com/pvijay037/deploy/assets/95902517/84062991-952e-48bf-8f4b-404ea609a598">

2. **Mentor App:**
    ```bash
    http://127.0.0.1:8000/mentor/mentors/
    ```
    <img width="947" alt="Screenshot 2023-12-09 020655" src="https://github.com/pvijay037/deploy/assets/95902517/a8192b00-b01f-43bc-b15c-45b1bebf04f2">
    
    ```bash
    http://127.0.0.1:8000/mentor/mentors/1/add_student/
    ```
    <img width="647" alt="Screenshot 2023-12-09 021030" src="https://github.com/pvijay037/deploy/assets/95902517/a1d12023-1ed5-4c2c-b217-4add24cc6dcb">
    
    ```bash
    http://127.0.0.1:8000/mentor/students/
    ```
    <img width="955" alt="Screenshot 2023-12-09 021218" src="https://github.com/pvijay037/deploy/assets/95902517/b66b0805-32cf-4658-89a7-b80d7a574754">


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
