# Assignment 04 Report Guide

Follow these steps to generate the data and screenshots required for your final report.

## Screenshots Instructions

### Screenshot 1: Sequential Scan (Single Table)
1. Refresh the home page.
2. Locate the **"Search Without Indexing"** card.
3. In **"Option 01: Single Table Search"**, select a loan type from the dropdown.
4. Click **"Search Loans"**.
5. Capture a full-page screenshot showing the **Execution Time** and the **Top 5 Rows** of the results.

### Screenshot 2: Sequential Scan (Join)
1. Refresh the home page.
2. Locate the **"Search Without Indexing"** card.
3. In **"Option 02: Two Tables Join"**, select a loan type from the dropdown.
4. Click **"Search Joined Data"**.
5. Capture a full-page screenshot showing the **Execution Time** and the **Top 5 Rows** of the results.

### Screenshot 3: Index Scan (Single Table)
1. Refresh the home page.
2. Locate the **"Search With Indexing"** card.
3. In **"Option 01: Single Table Search"**, select a loan type from the dropdown.
4. Click **"Search Loans"**.
5. Capture a full-page screenshot showing the **Execution Time** and the **Top 5 Rows** of the results.

### Screenshot 4: Index Scan (Join)
1. Refresh the home page.
2. Locate the **"Search With Indexing"** card.
3. In **"Option 02: Two Tables Join"**, select a loan type from the dropdown.
4. Click **"Search Joined Data"**.
5. Capture a full-page screenshot showing the **Execution Time** and the **Top 5 Rows** of the results.

---

## Report Structure
Use the following structure for your final document:

**Title:** Assignment 04 - Demonstrating the Effect of Indexes on Search Performance

1. **Introduction:** Briefly describe the purpose of the experiment.
2. **Database Design:** Mention the tables used and the number of records (10,000+).
3. **Flask Web Application:** Describe the features of the dashboard.
4. **Search Without Indexing:**
   - [Paste Screenshot 1]
   - [Paste Screenshot 2]
5. **Search With Indexing:**
   - [Paste Screenshot 3]
   - [Paste Screenshot 4]
6. **Performance Comparison:** Discuss the differences in execution times.
7. **Conclusion:** Summarize your findings.

---

## Key Performance Explanations
Include these points in your conclusion:
- **Sequential Scan:** Without indexing, PostgreSQL may need to scan every row in the table to find matches, leading to slower performance as the dataset grows.
- **Index Scan:** With indexing, PostgreSQL creates a separate data structure that allows it to jump directly to the relevant records, significantly reducing disk I/O and execution time.
- **Join Optimization:** Indexing is particularly effective for join operations, as it allows the database to quickly find matching keys across multiple tables.
