-- PostgreSQL Schema for Assignment 04 Bank & Loan Search Performance

-- Create Banks table
CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) NOT NULL,
    branch_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    phone VARCHAR(20),
    manager_name VARCHAR(100),
    established_year INTEGER,
    bank_type VARCHAR(50),
    total_assets NUMERIC(15, 2)
);

-- Create Loans table
CREATE TABLE IF NOT EXISTS loans (
    loan_id SERIAL PRIMARY KEY,
    bank_id INTEGER REFERENCES banks(bank_id),
    borrower_name VARCHAR(100) NOT NULL,
    borrower_email VARCHAR(100) NOT NULL,
    loan_type VARCHAR(50) NOT NULL,
    loan_amount NUMERIC(15, 2) NOT NULL,
    interest_rate NUMERIC(5, 2) NOT NULL,
    loan_term_months INTEGER NOT NULL,
    issue_date DATE,
    status VARCHAR(20) NOT NULL,
    credit_score INTEGER
);

-- Note: Indexes are created and dropped dynamically by the Flask application
-- to demonstrate performance differences.
