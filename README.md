# Bank & Loan Search Performance Using PostgreSQL Indexes

## Project Description

This project is for CSE 412 Assignment 04. It shows how PostgreSQL indexes make searches faster. I built a Flask app that lets you search through banks and loans and compare how long it takes with and without indexes.

## Technologies Used

- Flask (Python)
- PostgreSQL & pgAdmin
- psycopg2
- HTML & CSS

## Setup Instructions

### 1. Database Setup

1. Open pgAdmin.
2. Create a new database called `Assignment04_DB`.
3. Open a Query Tool and run the code in `schema.sql`. This will create the `banks` and `loans` tables.

### 2. Set Password

You need to set your database password. You can create a `.env` file or just set the `DB_PASSWORD` environment variable:

```bash
export DB_PASSWORD="[PASSWORD]"
```

### 3. Generate Data

Run this script to add 10,000 banks and 10,000 loans to the database:

```bash
python data_generation.py
```

### 4. Run the App

Start the Flask app:

```bash
python app.py
```

Open your browser to: [http://127.0.0.1:5001](http://127.0.0.1:5001)

## Search Options

There are four types of searches you can test:

1. **Without Indexing - Single Table:** Searches just the loans table.
2. **Without Indexing - Join:** Joins loans and banks together.
3. **With Indexing - Single Table:** Uses an index on the loan type.
4. **With Indexing - Join:** Uses indexes on the IDs and city names to speed up the join.

