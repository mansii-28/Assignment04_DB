from flask import Flask, render_template, request
import psycopg2
import time
import os

app = Flask(__name__)

DB_NAME = "Assignment04_DB"
USER = "postgres"
PASSWORD = os.getenv("DB_PASSWORD", "your_postgres_password")
HOST = "localhost"
PORT = "5432"

COLUMN_MAP = {
    'loan_id': 'Loan ID',
    'borrower_name': 'Borrower Name',
    'borrower_email': 'Borrower Email',
    'loan_type': 'Loan Type',
    'loan_amount': 'Loan Amount ($)',
    'interest_rate': 'Interest Rate (%)',
    'loan_term_months': 'Loan Term (Months)',
    'status': 'Status',
    'credit_score': 'Credit Score',
    'bank_name': 'Bank Name',
    'branch_name': 'Branch Name',
    'city': 'City',
    'state': 'State'
}

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

def run_query(query, params=None):
    connection = get_connection()
    cursor = connection.cursor()

    start_time = time.time()
    cursor.execute(query, params)
    results = cursor.fetchall()
    end_time = time.time()

    columns = [desc[0] for desc in cursor.description]

    cursor.close()
    connection.close()

    execution_time = round((end_time - start_time) * 1000, 4)

    return columns, results, execution_time

def drop_indexes():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DROP INDEX IF EXISTS idx_loans_loan_type;")
    cursor.execute("DROP INDEX IF EXISTS idx_loans_bank_id;")
    cursor.execute("DROP INDEX IF EXISTS idx_banks_city;")

    connection.commit()
    cursor.close()
    connection.close()

def create_indexes():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_loans_loan_type ON loans(loan_type);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_loans_bank_id ON loans(bank_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_banks_city ON banks(city);")

    connection.commit()
    cursor.close()
    connection.close()

@app.route("/", methods=["GET", "POST"])
def index():
    result_data = None

    if request.method == "POST":
        search_value = request.form.get("search_value")
        mode = request.form.get("mode")
        option = request.form.get("option")

        if search_value:
            if mode == "without_index":
                drop_indexes()
                mode_title = "Search Without Indexing"
            else:
                create_indexes()
                mode_title = "Search With Indexing"

            if option == "single":
                query = """
                    SELECT loan_id, borrower_name, borrower_email, loan_type,
                           loan_amount, interest_rate, loan_term_months,
                           status, credit_score
                    FROM loans
                    WHERE loan_type = %s
                    LIMIT 5;
                """
                option_title = "Search Option 01 - Single Table Search"
            else:
                query = """
                    SELECT l.loan_id, b.bank_name, b.branch_name, b.city, b.state,
                           l.borrower_name, l.loan_type, l.loan_amount, l.status
                    FROM loans l
                    JOIN banks b ON l.bank_id = b.bank_id
                    WHERE l.loan_type = %s
                    LIMIT 5;
                """
                option_title = "Search Option 02 - Join Search Using Both Tables"

            columns, results, execution_time = run_query(query, (search_value,))

            formatted_columns = [COLUMN_MAP.get(col, col.replace('_', ' ').title()) for col in columns]

            formatted_results = []
            for row in results:
                formatted_row = []
                for col_name, value in zip(columns, row):
                    if col_name == 'loan_amount' and value is not None:
                        formatted_row.append(f"{float(value):,.2f}")
                    else:
                        formatted_row.append(value)
                formatted_results.append(formatted_row)

            result_data = {
                "mode_title": mode_title,
                "option_title": option_title,
                "search_value": search_value,
                "columns": formatted_columns,
                "results": formatted_results,
                "execution_time": execution_time
            }

    return render_template("index.html", result_data=result_data)

if __name__ == "__main__":
    app.run(debug=True)