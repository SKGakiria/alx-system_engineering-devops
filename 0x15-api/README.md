# 0x15. API
#### `Python` `Scripting` `Back-end` `API`

## Resources
**Read or watch:**

* [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
* [What is an API](https://www.webopedia.com/definitions/api/)
* [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
* [What is a REST API](https://www.sitepoint.com/rest-api/)
* [What are microservices](https://smartbear.com/learn/api-design/microservices/)
* [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://peps.python.org/pep-0008/)

## Tasks
0. Gather data from an API
Write a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.

Requirements:

* You must use `urllib` or `requests` module
* The script must accept an integer as a parameter, which is the employee ID
* The script must display on the standard output the employee TODO list progress in this exact format:
	* First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
		* `EMPLOYEE_NAME`: name of the employee
		* `NUMBER_OF_DONE_TASKS`: number of completed tasks
		* `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
	* Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`)

1. Export to CSV
Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

* Records all tasks that are owned by this employee
* Format must be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
* File name must be: `USER_ID.csv`

2. Export to JSON
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

* Records all tasks that are owned by this employee
* Format must be: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
* File name must be: `USER_ID.json`

3. Dictionary of list of dictionaries
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

* Records all tasks from all employees
* Format must be: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
* File name must be: `todo_all_employees.json`
