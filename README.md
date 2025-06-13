# Pastel To-Do List

This is a simple yet elegant To-Do List web application built with Flask, designed to help users manage their tasks efficiently with a delightful pastel-themed interface. The application allows users to add, complete, and delete tasks, as well as filter them by status (all, completed, or pending). It also includes a theme toggle for a personalized user experience.

## Features

*   **Add Tasks:** Easily add new tasks with customizable priority levels (low, medium, high).
*   **Mark as Complete:** Mark tasks as completed to keep track of your progress.
*   **Delete Tasks:** Remove tasks that are no longer needed.
*   **Filter Tasks:** View tasks based on their status: all, completed, or pending.
*   **Priority Indication:** Tasks are visually distinguished by priority levels using color-coded borders.
*   **Theme Toggle:** Switch between a light pastel theme and a dark theme for comfortable viewing.
*   **Responsive Design:** The interface is designed to be user-friendly across various devices.

## Project Structure

The project is organized into a standard Flask application structure:

```
pastel-todo-list/
├── app.py
├── static/
│   └── css/
│       └── style.css
└── templates/
    └── index.html
```

*   `app.py`: The main Flask application file, handling routes, logic, and data management.
*   `static/`: Contains static files such as CSS stylesheets.
    *   `css/style.css`: Defines the visual styles and pastel theme for the application.
*   `templates/`: Stores HTML templates rendered by the Flask application.
    *   `index.html`: The main HTML file for the To-Do List interface.

## Technologies Used

*   **Flask:** A micro web framework for Python, used for building the web application backend.
*   **HTML5:** Standard markup language for creating web pages.
*   **CSS3:** Stylesheet language used for describing the presentation of a document written in HTML.
*   **JavaScript:** Used for interactive elements, specifically the theme toggle functionality.

## Setup and Installation

To get this project up and running on your local machine, follow these steps:

### Prerequisites

Make sure you have Python installed on your system. This project was developed with Python 3.x.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pastel-todo-list.git
cd pastel-todo-list
```

(Note: Replace `YOUR_USERNAME` with your actual GitHub username and `pastel-todo-list` with your repository name if you fork it.)

### 2. Create a Virtual Environment (Recommended)

It's good practice to use a virtual environment to manage project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install Flask
```

### 4. Run the Application

Once the dependencies are installed, you can run the Flask application:

```bash
python app.py
```

### 5. Access the Application

Open your web browser and navigate to `http://127.0.0.1:5000/` (or `http://localhost:5000/`).

## Usage

1.  **Adding a Task:** Type your task in the input field, select a priority from the dropdown, and click the "Add" button.
2.  **Completing a Task:** Click the "✔" icon next to a task to mark it as completed. Completed tasks will have a strikethrough and reduced opacity.
3.  **Deleting a Task:** Click the "🗑" icon next to a task to remove it from the list.
4.  **Filtering Tasks:** Use the "All", "Completed", and "Pending" links above the task list to filter tasks based on their status.
5.  **Toggling Theme:** Click the "🌙 Toggle Theme" button at the top right corner to switch between the light and dark themes.

## Code Overview

### `app.py`

This file contains the core logic of the Flask application. It defines the routes and their corresponding functions to handle HTTP requests.

*   **`app = Flask(__name__)`**: Initializes the Flask application.
*   **`tasks = []`**: An in-memory list used to store tasks. Each task is a dictionary with `name`, `priority`, and `done` keys.
*   **`@app.route('/')`**: The main route that renders the `index.html` template. It also handles task filtering based on the `filter` query parameter.
*   **`@app.route('/add', methods=['POST'])`**: Handles the addition of new tasks. It retrieves the task name and priority from the form submission and appends it to the `tasks` list.
*   **`@app.route('/complete/<int:task_id>')`**: Marks a task as complete based on its `task_id`.
*   **`@app.route('/delete/<int:task_id>')`**: Deletes a task based on its `task_id`.
*   **`if __name__ == '__main__': app.run(debug=True)`**: Runs the Flask development server. `debug=True` enables debug mode, which provides detailed error messages and automatically reloads the server on code changes.

### `templates/index.html`

This is the main HTML template that defines the user interface of the To-Do List. It uses Jinja2 templating engine (default for Flask) to dynamically render content.

*   **`<!DOCTYPE html>`**: Standard HTML5 declaration.
*   **`<head>`**: Contains metadata, title, and links to external resources like `style.css` and Google Fonts.
*   **`<div class="theme-toggle">`**: Contains the theme toggle button that calls the `toggleTheme()` JavaScript function.
*   **`<div class="container">`**: The main container for the To-Do List elements.
*   **`<form method="POST" action="/add">`**: Form for adding new tasks, including an input field for the task name, a select dropdown for priority, and an add button.
*   **`<div class="filters">`**: Contains links to filter tasks (`All`, `Completed`, `Pending`). These links modify the URL query parameters to trigger filtering in `app.py`.
*   **`{% if tasks|length == 0 %}` / `{% else %}`**: Jinja2 conditional rendering to display a message if no tasks exist or to display the task list.
*   **`<ul class="task-list">`**: Unordered list to display individual tasks.
*   **`{% for task in tasks %}`**: Jinja2 loop to iterate over the `tasks` list and render each task as a list item (`<li>`).
*   **`<li class="{{ 'completed' if task.done else '' }} priority-{{ task.priority }}">`**: Each list item dynamically applies CSS classes based on task status (`completed`) and priority (`priority-low`, `priority-medium`, `priority-high`).
*   **`<span class="actions">`**: Contains links for completing ("✔") and deleting ("🗑") tasks. `loop.index0` is used to get the 0-based index of the current task in the loop.
*   **`<script>`**: Contains the `toggleTheme()` JavaScript function that adds or removes the `dark` class from the `body` element to switch themes.

### `static/css/style.css`

This stylesheet provides the visual styling for the application, implementing the pastel theme and responsive design.

*   **`/* General Styles */`**: Basic styling for `body`, `container`, and `h1`.
*   **`.dark`**: Defines styles for the dark theme, which are applied when the `dark` class is added to the `body`.
*   **`form`**: Styles for the task input form elements.
*   **`.filters`**: Styles for the task filter links.
*   **`.task-list`**: Styles for the unordered list of tasks.
*   **`.task-list li`**: Styles for individual task items, including hover effects and transitions.
*   **`.task-list li.completed`**: Styles for completed tasks (strikethrough and opacity change).
*   **`.priority-low`, `.priority-medium`, `.priority-high`**: Defines left border colors to visually indicate task priority.
*   **`.actions a`**: Styles for the complete and delete action icons.
*   **`.empty`**: Styles for the message displayed when no tasks are present.
*   **`.theme-toggle`**: Styles for the theme toggle button.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

## License

This project is open source and available under the MIT License.

## Contact

If you have any questions or suggestions, feel free to open an issue on the GitHub repository.

