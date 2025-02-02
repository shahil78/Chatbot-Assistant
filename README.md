# Chat Assistant with SQLite Database Interaction

## Objective
This project aims to design, implement, and deploy a Python-based chat assistant that interacts with an SQLite database to answer user queries. The chat assistant accepts natural language queries, converts them into SQL queries, fetches data from the database, and responds with clear, formatted answers.

## Scope and Requirements

### Database
The SQLite database contains two tables:

#### Table 1: Employees
| ID  | Name    | Department   | Salary | Hire_Date  |
|-----|---------|--------------|--------|------------|
| 1   | Alice   | Sales        | 50000  | 2021-01-15 |
| 2   | Bob     | Engineering  | 70000  | 2020-06-10 |
| 3   | Charlie | Marketing    | 60000  | 2022-03-20 |

#### Table 2: Departments
| ID  | Name         | Manager |
|-----|--------------|---------|
| 1   | Sales        | Alice   |
| 2   | Engineering  | Bob     |
| 3   | Marketing    | Charlie |

You are free to add more data and columns to the database as needed.

### Functionality
The chat assistant supports the following types of queries:
- “Show me all employees in the [department] department.”
- “Who is the manager of the [department] department?”
- “List all employees hired after [date].”
- “What is the total salary expense for the [department] department?”
- And more…

### Error Handling
The chat assistant is designed to:
- Gracefully handle invalid queries.
- Return meaningful messages when no results are found.
- Handle incorrect department names or invalid input formats.

## Deliverables
1. **Hosted Link**: A public URL to access and test the deployed chat assistant.
2. **Code Repository**: A GitHub repository containing:
   - The source code for the assistant.
   - The SQLite database file.
   - A `README.md` file with:
     - An explanation of how the assistant works.
     - Steps to run the project locally.
     - Known limitations or suggestions for improvement.

## Evaluation Criteria
- **Correctness**: Does the assistant correctly answer the supported queries?
- **Deployment**: Is the application hosted properly and accessible without issues?
- **Code Quality**: Is the code modular, readable, and well-documented?
- **Error Handling**: Does the assistant gracefully handle edge cases and invalid inputs?
- **User Experience**: Is the hosted application intuitive and user-friendly?

## How the Assistant Works
The chat assistant is built using Python and interacts with an SQLite database. It uses natural language processing (NLP) techniques to interpret user queries and convert them into SQL queries. The assistant then executes these SQL queries on the database and returns the results in a user-friendly format.

### Steps to Run the Project Locally
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/chat-assistant.git
   cd chat-assistant
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Chat Assistant**:
   Open your web browser and navigate to `http://127.0.0.1:5000` to interact with the chat assistant.

## Known Limitations
- The assistant currently supports a limited set of queries. More complex queries may not be handled correctly.
- The natural language processing capabilities are basic and may not understand all variations of user input.
- The assistant does not support multi-table joins or advanced SQL operations.

## Suggestions for Improvement
- Expand the range of supported queries.
- Enhance the NLP capabilities to better understand user input.
- Implement multi-table join support for more complex queries.
- Add a user interface for a more interactive experience.

## Notes for Candidates
- Use Python and any framework or libraries of your choice (e.g., Flask, FastAPI).
- Ensure that your deployed version is functional and provides a seamless user experience.
- Focus on simplicity, clarity, and robustness in your solution.
- This solution needs to work without any third-party API. You may download and use open-source models/libraries.

---

Feel free to contribute to the project by submitting issues or pull requests. Your feedback and contributions are highly appreciated!
