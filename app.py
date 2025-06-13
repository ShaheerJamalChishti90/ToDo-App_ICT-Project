from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route('/')
def index():
    # Get the filter parameter from the URL
    filter_type = request.args.get('filter', 'all')  # Default to 'all'
    
    # Filter tasks based on the filter type
    filtered_tasks = []
    if filter_type == 'all':
        filtered_tasks = tasks
    elif filter_type == 'completed':
        filtered_tasks = [task for task in tasks if task['done']]
    elif filter_type == 'pending':
        filtered_tasks = [task for task in tasks if not task['done']]
    
    return render_template('index.html', tasks=filtered_tasks, filter=filter_type)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    priority = request.form.get('priority', 'low')  # default to low
    if task_name:
        tasks.append({
            "name": task_name,
            "priority": priority,
            "done": False
        })
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)