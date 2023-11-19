# Employee Management System

## Introduction

Welcome to the Employee Management System, a comprehensive project designed for efficient employee management. This system streamlines various aspects, including attendance tracking, appointment scheduling, user profile management, and project/task administration.

## Features

### 1. Attendance Tracking System

- Users can mark open attendances created by administrators.
- Streamlined attendance management for easy tracking.

### 2. Appointment System

- Schedule appointments with a notification system (non-realtime).
- Users receive timely notifications for their scheduled appointments.

### 3. User Profile Management

- Users can edit their basic information.
- Change password functionality for enhanced security.

### 4. Project and Task Management

- Efficiently manage projects and tasks associated with them.
- Built-in CRUD functionality for easy project and task administration.

### 5. Admin Panel

- Utilizes Django for a robust admin panel.
- Jazzmin template for a modern and user-friendly admin interface.
- Good safeguard measures in place for the assignment of projects and tasks.

![Admin Panel](screenshots/admin_panel.png)

*Caption: The modern and user-friendly admin panel powered by Django and Jazzmin.*

## History of Civil Engineering

Civil engineering has a rich history that spans centuries. From the construction of ancient structures to the modern infrastructure developments, civil engineering has played a crucial role in shaping societies. Explore the milestones, influential figures, and major developments in the field.

## Installation

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/zeus/employee-management-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd employee-management-system
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up MySQL database in XAMPP and update database configurations in `settings.py`.

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application at [http://localhost:8000](http://localhost:8000).

## Features

### 1. Attendance Tracking System

- Users can mark open attendances created by administrators.
- Streamlined attendance management for easy tracking.

### 2. Appointment System

- Schedule appointments with a notification system (non-realtime).
- Users receive timely notifications for their scheduled appointments.

### 3. User Profile Management

- Users can edit their basic information.
- Change password functionality for enhanced security.

### 4. Project and Task Management

- Efficiently manage projects and tasks associated with them.
- Built-in CRUD functionality for easy project and task administration.

#### Admin Panel

- Utilizes Django for a robust admin panel.
- Jazzmin template for a modern and user-friendly admin interface.
- Good safeguard measures in place for the assignment of projects and tasks.
*Caption: The modern and user-friendly admin panel powered by Django and Jazzmin.*

![Admin Panel](screenshots/admin_panel.png)

#### Login Screen

![Login Screen](screenshots/login_screen.png)

*Caption: The login screen for users to access the system.*

#### User Panel

![User Panel](screenshots/user_panel.png)

*Caption: The user panel displaying key functionalities for individual users.*

### History of Civil Engineering in User Dashboard

[Watch the History of Civil Engineering](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDhnMG8xYXRwcjRmM3p2aWp0emVxdzAyeDQwZmpzZWowNnV5Y28yMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zZBqKmLLhQepXvgfPJ/giphy.gif)

*Caption: A section in the user dashboard providing insights into the history of civil engineering.*

## Contributing

If you'd like to contribute to the project, please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to [Django](https://www.djangoproject.com/) for providing a powerful web framework.
- The [Jazzmin](https://github.com/farridav/django-jazzmin) template for enhancing the admin interface.

Feel free to explore and enhance the system as needed for your specific use case. If you encounter any issues or have suggestions, don't hesitate to contribute or reach out for support. Happy coding!
