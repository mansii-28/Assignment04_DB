import psycopg2
from faker import Faker
import random
import os

fake = Faker()

DB_NAME = "Assignment04_DB"
USER = "postgres"
PASSWORD = os.getenv("DB_PASSWORD", "your_postgres_password")
HOST = "localhost"
PORT = "5432"

BANK_TYPES = ["Commercial", "Credit Union", "Investment", "Retail", "Savings"]
LOAN_TYPES = ["Home Loan", "Auto Loan", "Personal Loan", "Business Loan", "Education Loan"]
LOAN_STATUS = ["Approved", "Pending", "Rejected", "Closed"]

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

def clear_data(cur):
    cur.execute("DELETE FROM loans;")
    cur.execute("DELETE FROM banks;")
    cur.execute("ALTER SEQUENCE loans_loan_id_seq RESTART WITH 1;")
    cur.execute("ALTER SEQUENCE banks_bank_id_seq RESTART WITH 1;")

def insert_banks(cur, count=10000):
    print("Inserting banks...")

    for _ in range(count):
        cur.execute("""
            INSERT INTO banks (
                bank_name, branch_name, city, state, zip_code,
                phone, manager_name, established_year, bank_type, total_assets
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            fake.company() + " Bank",
            fake.city() + " Branch",
            fake.city(),
            fake.state(),
            fake.zipcode(),
            fake.phone_number()[:20],
            fake.name(),
            random.randint(1950, 2024),
            random.choice(BANK_TYPES),
            round(random.uniform(1000000, 900000000), 2)
        ))

def insert_loans(cur, count=10000):
    print("Inserting loans...")
    
    email_domains = ["yahoo.com", "hotmail.com", "gmail.com", "outlook.com", "asu.cse412assignment04.edu"]

    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        borrower_name = f"{first_name} {last_name}"
        domain = random.choice(email_domains)
        random_num = random.randint(10, 99)
        
        email_format = random.choice([
            f"{first_name.lower()}.{last_name.lower()}{random_num}@{domain}",
            f"{first_name.lower()}{last_name.lower()}{random_num}@{domain}",
            f"{last_name.lower()}{first_name.lower()[:2]}{random_num}@{domain}"
        ])

        cur.execute("""
            INSERT INTO loans (
                bank_id, borrower_name, borrower_email, loan_type,
                loan_amount, interest_rate, loan_term_months,
                issue_date, status, credit_score
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            random.randint(1, 10000),
            borrower_name,
            email_format,
            random.choice(LOAN_TYPES),
            round(random.uniform(5000, 1000000), 2),
            round(random.uniform(3.0, 18.0), 2),
            random.choice([12, 24, 36, 48, 60, 120, 180, 240, 360]),
            fake.date_between(start_date="-10y", end_date="today"),
            random.choice(LOAN_STATUS),
            random.randint(300, 850)
        ))

def main():
    conn = get_connection()
    cur = conn.cursor()

    clear_data(cur)
    insert_banks(cur)
    insert_loans(cur)

    conn.commit()
    cur.close()
    conn.close()

    print("Data generation completed successfully.")

if __name__ == "__main__":
    main()