# Python User Management CLI

Modular CLI user management system built in Python with JSON-based file persistence.

---

## Overview

This project implements a simple user management system following CRUD principles (Create, Read, Update, Delete).

Data is stored locally using a JSON file to simulate basic backend persistence.
The project follows a modular architecture to separate responsibilities and improve maintainability.

---

## Features

- Create user
- List users
- Update user
- Delete user
- JSON file persistence (`users.json`)
- Input validation and error handling
- Modular structure

---

## Project Structure

app.py # Application entry point
menu.py # CLI interface
users.py # CRUD logic
storage.py # JSON persistence layer


---

## Requirements

- Python 3.10+

---

## Notes

 - The users.json file is generated locally.

 - It is excluded from version control via .gitignore.

 - This project demonstrates basic backend principles using file-based persistence.

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/devbykauan/python-user-management-cli.git
cd python-user-management-cli
