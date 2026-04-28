DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS banks;

CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100),
    branch_name VARCHAR(100),
    city VARCHAR(80),
    state VARCHAR(50),
    zip_code VARCHAR(15),
    phone VARCHAR(20),
    manager_name VARCHAR(100),
    established_year INT,
    bank_type VARCHAR(50),
    total_assets NUMERIC(15,2)
);

CREATE TABLE loans (
    loan_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    borrower_name VARCHAR(100),
    borrower_email VARCHAR(120),
    loan_type VARCHAR(60),
    loan_amount NUMERIC(12,2),
    interest_rate NUMERIC(5,2),
    loan_term_months INT,
    issue_date DATE,
    status VARCHAR(40),
    credit_score INT
);
