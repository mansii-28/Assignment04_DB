<<<<<<< HEAD
# Bank & Loan Search Performance Using PostgreSQL Indexes

## Project Description
This application demonstrates the impact of PostgreSQL indexing on query performance. It provides a web-based dashboard to search through bank and loan data, allowing users to compare execution times for various search options with and without indexes.

## Technologies Used
- **Backend:** Flask (Python)
- **Database:** PostgreSQL, pgAdmin
- **Library:** psycopg2
- **Frontend:** HTML, CSS

## Setup Instructions

### 1. Database Setup
1. Open pgAdmin or any PostgreSQL client.
2. Create a new database named `Assignment04_DB`.
3. Open a Query Tool and execute the contents of `schema.sql` to create the necessary tables (`banks`, `loans`) and sequences.

### 2. Configure Environment
Create a `.env` file in the project root or set the `DB_PASSWORD` environment variable with your PostgreSQL password:
```bash
export DB_PASSWORD="your_postgres_password"
```

### 3. Data Generation
Run the following command to populate the database with at least 10,000 rows for both banks and loans:
```bash
python data_generation.py
```

### 4. Running the Application
Start the Flask development server:
```bash
python app.py
```
The application will be available at: [http://127.0.0.1:5001](http://127.0.0.1:5001)

## Search Demonstrations
The application features four primary search modes to demonstrate indexing benefits:
1. **Without Indexing - Single Table:** Searches the `loans` table using a sequential scan.
2. **Without Indexing - Join:** Joins `loans` and `banks` tables using a sequential scan.
3. **With Indexing - Single Table:** Uses an index on `loan_type` for faster retrieval.
4. **With Indexing - Join:** Uses indexes on join keys and filter columns for optimized performance.

## Security Note
**Do not commit database passwords or secrets to GitHub.** The application is configured to read the database password from an environment variable (`DB_PASSWORD`) or use a placeholder if not set.
=======
# Assignment04_DB
>>>>>>> fa88f949d9456094fff567988efd629210623916
