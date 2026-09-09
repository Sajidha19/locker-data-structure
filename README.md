# 🔐 Paid Locker Data Structure System

A Python-based **paid locker system** using a **list of dictionaries** to manage locker IDs, occupancy status, mobile numbers, passcodes, and storage time.

## 📌 Project Overview

This project demonstrates how a locker management system can be represented and manipulated using Python data structures.

The system contains **7 locker records**, with each locker represented as a dictionary and all locker records stored inside a list.

The program demonstrates how locker information can be:

* Created
* Displayed
* Searched
* Updated
* Filtered
* Counted
* Reset
* Managed based on occupancy status

---

```

### Locker Attributes

| Attribute  | Description                              |
| ---------- | ---------------------------------------- |
| `id`       | Unique locker identifier                 |
| `occupied` | Indicates whether the locker is occupied |
| `mobile`   | Customer mobile number                   |
| `passcode` | Customer passcode                        |
| `time`     | Locker storage time in hours             |

Using a list of dictionaries makes it possible to store multiple locker records together while allowing individual records and values to be accessed and modified.


## 🧠 Programming Concepts Demonstrated

This project demonstrates practical use of:

* **Lists**
* **Dictionaries**
* Dictionary key-value pairs
* `append()`
* `for` loops
* `if` and `else` statements
* Boolean values
* Conditional filtering
* Searching through collections
* Updating dictionary values
* `len()`
* Counters
* String formatting
* Data manipulation
* Basic record management

---

## 🔄 System Operations

The main operations demonstrated by the program are:

```text
              ┌──────────────────────┐
              │ Create Locker List   │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Add Locker Records   │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Display Locker Data  │
              └──────────┬───────────┘
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Search      Filter       Update
          Locker      Lockers      Records
             │           │           │
             └───────────┼───────────┘
                         ▼
              ┌──────────────────────┐
              │ Generate Status      │
              │ Report               │
              └──────────────────────┘
```

## 🧪 Demonstrated Operations

The program demonstrates the following scenarios:

* Creating an empty list
* Adding locker dictionaries using `append()`
* Displaying all locker records
* Displaying occupied lockers
* Displaying available lockers
* Changing an available locker to occupied
* Freeing an occupied locker
* Updating storage time
* Searching for a locker by ID
* Counting total lockers
* Counting occupied lockers
* Counting available lockers
* Updating multiple locker attributes
* Changing a customer's passcode
* Updating a customer's mobile number
* Displaying customer mobile numbers for occupied lockers

---

## 🛠️ Technologies Used

* **Python**
* **Visual Studio Code**
* **Python Console / Terminal**

---

## ▶️ How to Run

### 1. Clone or Download the Repository

Clone the repository or download the project files.

### 2. Open the Python File

Open the Python file in any Python-compatible development environment.

### 3. Run the Program

Run the Python file using a Python interpreter.

```bash
python locker_data_structure.py
```

> **Note:** If you keep the current filename in the repository, use the exact filename shown in your GitHub repository.

The program automatically creates the locker records and demonstrates the different data structure operations through the console.

---

## 📁 Repository Structure

```text
locker-data-structure/
│
├── locker_data_structure.py
│
├── README.md
│
└── .gitignore
```

---

## 🎯 Learning Outcomes

Through this project, I developed practical experience in:

* Using lists and dictionaries to represent structured data
* Managing multiple records within a collection
* Accessing dictionary values using keys
* Updating existing records
* Searching records using unique identifiers
* Filtering records using conditional statements
* Counting records dynamically
* Resetting stored information
* Using loops to process collections
* Applying Python data structures to a practical system



## 👩‍💻 Project Author

**Sajidha**
**BSc (Hons) Computing Student**

This project was developed for academic and portfolio purposes as part of my university programming coursework.

---
