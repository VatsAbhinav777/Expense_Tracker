# Problem statement
In daily life, individuals often make numerous small financial transactions that go untracked. Relying on
memory or physical notes (pen and paper) is inefficient, prone to error, and lacks the ability to instantly
sum up totals. Existing financial apps can be overly complex, requiring accounts, internet access, or
subscriptions. There is a need for a simple, immediate, and offline tool that allows users to log
expenses on the fly without any setup friction.

# Scope of the project
The scope of this project is limited to a Single-Session Expense Tracker.
1) Current Scope: The application runs in the console, accepts user input for amounts and
descriptions, stores them in a temporary list structure, and calculates totals. Data persists only as
long as the script is running.
2) Future Scope: Future iterations may include file handling (CSV/JSON) for permanent data storage,
graphical data visualization, and category-based filtering.

# Target users
1) Students: To track pocket money and daily spending on food/stationary.
Budget-Conscious Individuals: People who want a quick, no-frills way to see where their money
went during the day.
2) Python Beginners: Developers looking for a reference implementation of basic CRUD (Create,
Read) operations in a CLI environment.

# High-level features
1) Data Entry Interface: A streamlined prompt to capture financial data (Cost + Context).
2) Dynamic List Management: The system dynamically grows the storage list as new entries are
added.
3) Aggregation Logic: An internal calculator that traverses the data structure to sum up costs
automatically.
4) User Control: A loop-based menu system that puts the user in control of the application flow
(Add vs. View vs. Exit).
