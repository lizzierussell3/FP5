# Customer Data Entry and Storage GUI

This repository contains a simple Python application with a Graphical User Interface (GUI) for customers to enter their information, which is then stored in a local SQLite database file.

## 📁 Repository Contents

| File Name | Description |
| :--- | :--- |
| **`fp5.py`** | The main application file. This script runs the GUI (likely built with Tkinter, PyQt, or a similar library) and handles the logic for connecting to the database and saving customer information upon submission. |
| **`view_data.py`** | **(Assuming you created this file)** A utility script to connect to the database and print the stored customer records to the console. This is for quick internal viewing of the data. |
| **`customer.db`** | The SQLite database file. This is where all the customer information entered via the GUI is permanently stored. |
| **`README.md`** | This file, providing an overview and instructions for the project. |

---

## 🚀 How to Run the Application

### Prerequisites

You need **Python 3.x** installed on your system.

### 1. Run the GUI Application

To start the customer data entry form, execute the main script:

```bash
python fp5.py