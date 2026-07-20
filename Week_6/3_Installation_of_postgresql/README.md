# 🐘 PostgreSQL & SQL Complete Beginner Guide

> A complete beginner-friendly guide to Databases, SQL, PostgreSQL, DBeaver, SQL Commands, Examples, and Interview Questions.

---

# 📑 Table of Contents

1. What is Database?
2. Types of Databases
3. SQL vs NoSQL
4. What is RDBMS?
5. Features of SQL
6. SQL Syntax
7. SQL Categories
8. PostgreSQL
9. Installing PostgreSQL
10. Installing DBeaver
11. Database Terminology
12. SQL Examples
13. SQL Functions
14. SQL Joins
15. SQL Execution Order
16. Best Practices
17. Summary
18. Interview Questions

---

# 📚 What is Database?

## Definition

A **Database** is an organized collection of information stored electronically inside a computer system.

It helps users:

- Store data
- Retrieve data
- Update data
- Delete data
- Manage large amounts of information efficiently

Instead of storing everything inside Excel files, companies use databases.

Examples

- Amazon
- Flipkart
- Facebook
- Instagram
- Banking Systems
- Hospital Management
- College Management

All of them use databases.

---

# 🗂 Example Database

Employee Database

| Employee ID | Name | Department | Salary |
|-------------|------|------------|--------|
|101|Ramesh|HR|35000|
|102|Rahul|IT|50000|
|103|Priya|Sales|45000|

This table is stored inside a database.

---

# 🏛 Database Hierarchy

```
Database
    │
    ├── Tables
    │      │
    │      ├── Rows (Records)
    │      └── Columns (Fields)
```

---

# 📦 Table

A table stores related information.

Example

Employees Table

| ID | Name | Salary |
|----|------|---------|
|1|John|50000|
|2|David|70000|

---

# 📄 Row

Each horizontal entry is called a Row.

```
1 John 50000
```

This entire record is one row.

---

# 📑 Column

Vertical information is called Column.

Example

```
ID
Name
Salary
```

---

# 💡 SQL

## SQL

**Structured Query Language**

SQL is used to communicate with Relational Databases.

Using SQL we can

- Create tables
- Insert records
- Update records
- Delete records
- Search records

---

# SQL Databases

Examples

- PostgreSQL
- MySQL
- Microsoft SQL Server
- Oracle Database
- MariaDB
- SQLite

---

# 📘 NoSQL

NoSQL means

**Not Only SQL**

Stores data differently.

Instead of Tables,

Uses

- JSON
- Collections
- Documents

Examples

- MongoDB
- DynamoDB
- Cassandra
- Redis
- Elasticsearch

---

# SQL vs NoSQL

| SQL | NoSQL |
|------|--------|
|Tables|Collections|
|Rows|Documents|
|Columns|Fields|
|Structured Data|Semi Structured|
|Schema Required|Flexible Schema|
|PostgreSQL|MongoDB|

---

# 🏢 What is RDBMS?

## RDBMS

**Relational Database Management System**

Software that stores, manages and understands SQL language.

Responsibilities

- Store Data
- Manage Data
- Relationships
- Security
- Backup
- Recovery

Examples

- PostgreSQL
- MySQL
- Oracle
- SQL Server

---

# ⭐ Features of SQL

## 1️⃣ Data Retrieval

Retrieve information from tables.

Example

```sql
SELECT * FROM employees;
```

---

## 2️⃣ Data Manipulation

Modify data.

```sql
INSERT

UPDATE

DELETE
```

---

## 3️⃣ Data Definition

Create database objects.

```sql
CREATE

ALTER

DROP
```

---

## 4️⃣ Filtering

Retrieve specific rows.

```sql
SELECT *
FROM employees
WHERE department='HR';
```

---

## 5️⃣ Sorting

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

---

## 6️⃣ Joins

Combine multiple tables.

```sql
SELECT *
FROM employees
JOIN departments
ON employees.department_id = departments.id;
```

---

## 7️⃣ Aggregate Functions

```sql
SUM()

AVG()

COUNT()

MIN()

MAX()
```

Example

```sql
SELECT AVG(salary)
FROM employees;
```

---

## 8️⃣ Security

SQL supports

- Users
- Roles
- Permissions

Example

```sql
GRANT SELECT
ON employees
TO user1;
```

---

# SQL Syntax

General Syntax

```sql
SELECT column_name
FROM table_name
WHERE condition;
```

Example

```sql
SELECT name,salary
FROM employees
WHERE department='HR';
```

---

# SQL Categories

---

## 1️⃣ DDL

Data Definition Language

Used for

- Create
- Modify
- Delete Structure

Commands

```
CREATE

ALTER

DROP

TRUNCATE

RENAME
```

Example

```sql
CREATE TABLE employees
(
id INT,
name VARCHAR(50)
);
```

---

## 2️⃣ DML

Data Manipulation Language

Used for data modification.

Commands

```
INSERT

UPDATE

DELETE
```

Example

```sql
INSERT INTO employees
VALUES(1,'John');
```

---

## 3️⃣ DQL

Data Query Language

Command

```
SELECT
```

Example

```sql
SELECT *
FROM employees;
```

---

## 4️⃣ DCL

Data Control Language

Commands

```
GRANT

REVOKE
```

Example

```sql
GRANT SELECT
ON employees
TO admin;
```

---

## 5️⃣ TCL (Bonus)

Transaction Control Language

Commands

```
COMMIT

ROLLBACK

SAVEPOINT
```

---

# PostgreSQL

PostgreSQL is one of the world's most powerful open-source relational databases.

Features

- Open Source
- ACID Compliant
- High Performance
- Secure
- Supports JSON
- Supports Stored Procedures
- Supports Functions
- Supports Indexes

Official Website

https://www.postgresql.org/

---

# DBeaver

DBeaver is a GUI Tool.

It allows us to

- Connect databases
- Execute SQL
- View Tables
- Export Data
- Import Data

Official Website

https://dbeaver.io/

---

# Installing PostgreSQL

Download

https://www.postgresql.org/download/

Steps

1. Download Installer

2. Install

3. Set Password

4. Install pgAdmin

5. Open PostgreSQL

6. Create Database

---

# Installing DBeaver

Download

https://dbeaver.io/download/

Steps

1. Install

2. Open

3. Create Connection

4. Select PostgreSQL

5. Enter

- Host
- Username
- Password
- Database

6. Finish

---

# Creating Database

```sql
CREATE DATABASE company;
```

---

# Creating Table

```sql
CREATE TABLE employees
(
id INT PRIMARY KEY,
name VARCHAR(50),
department VARCHAR(50),
salary INT
);
```

---

# Insert Data

```sql
INSERT INTO employees
VALUES
(1,'John','HR',30000),
(2,'David','IT',50000),
(3,'Priya','Sales',45000);
```

---

# View Data

```sql
SELECT *
FROM employees;
```

---

# WHERE

```sql
SELECT *
FROM employees
WHERE department='HR';
```

---

# ORDER BY

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

---

# UPDATE

```sql
UPDATE employees
SET salary=60000
WHERE id=2;
```

---

# DELETE

```sql
DELETE
FROM employees
WHERE id=3;
```

---

# Aggregate Functions

## COUNT

```sql
SELECT COUNT(*)
FROM employees;
```

---

## SUM

```sql
SELECT SUM(salary)
FROM employees;
```

---

## AVG

```sql
SELECT AVG(salary)
FROM employees;
```

---

## MAX

```sql
SELECT MAX(salary)
FROM employees;
```

---

## MIN

```sql
SELECT MIN(salary)
FROM employees;
```

---

# SQL Joins

## INNER JOIN

Returns matching rows.

```sql
SELECT *
FROM employees
INNER JOIN departments
ON employees.department_id=departments.id;
```

---

## LEFT JOIN

Returns all left table rows.

---

## RIGHT JOIN

Returns all right table rows.

---

## FULL JOIN

Returns all records.

---

# SQL Execution Order

```
FROM

WHERE

GROUP BY

HAVING

SELECT

ORDER BY

LIMIT
```

---

# Best Practices

✅ Use Primary Keys

✅ Normalize Data

✅ Use Indexes

✅ Avoid SELECT *

✅ Backup Database

✅ Use Transactions

✅ Secure Passwords

✅ Use Meaningful Table Names

---

# Final Summary

Database stores information in an organized way.

SQL is used to communicate with relational databases.

PostgreSQL is one of the most popular SQL databases.

RDBMS manages relational databases.

DBeaver is a graphical interface used to connect and manage databases.

SQL consists of:

- DDL
- DML
- DQL
- DCL
- TCL

Common SQL Commands

```
CREATE

ALTER

DROP

INSERT

UPDATE

DELETE

SELECT

GRANT

REVOKE

COMMIT

ROLLBACK
```

---

# Frequently Asked Interview Questions

## Q1. What is a Database?

Answer:

A database is an organized collection of data stored electronically that allows efficient storage, retrieval, updating, and management of information.

---

## Q2. What is SQL?

Answer:

SQL stands for Structured Query Language. It is used to communicate with relational databases.

---

## Q3. What is PostgreSQL?

Answer:

PostgreSQL is an open-source relational database management system that supports SQL and advanced database features.

---

## Q4. Difference between SQL and NoSQL?

Answer:

| SQL | NoSQL |
|------|--------|
|Tables|Collections|
|Fixed Schema|Flexible Schema|
|Relational|Non-Relational|
|PostgreSQL|MongoDB|

---

## Q5. What is RDBMS?

Answer:

RDBMS stands for Relational Database Management System. It stores data in tables and manages relationships between them.

---

## Q6. What are SQL Categories?

Answer

DDL

DML

DQL

DCL

TCL

---

## Q7. Difference between DELETE, DROP and TRUNCATE?

| DELETE | TRUNCATE | DROP |
|---------|-----------|------|
|Deletes Rows|Removes All Rows|Deletes Entire Table|
|Can Use WHERE|No WHERE|Table Removed|

---

## Q8. What is Primary Key?

Answer:

A Primary Key uniquely identifies every row in a table.

---

## Q9. What is Foreign Key?

Answer:

A Foreign Key creates a relationship between two tables.

---

## Q10. What are Joins?

Answer:

Joins combine records from two or more tables based on a common column.

---

# Congratulations 🎉

You have learned:

✅ Database Basics

✅ SQL

✅ PostgreSQL

✅ RDBMS

✅ DBeaver

✅ SQL Commands

✅ SQL Categories

✅ SQL Functions

✅ SQL Joins

✅ CRUD Operations

✅ Interview Questions

🚀 You are now ready to start writing SQL queries and building PostgreSQL database applications.

---
![Image] (https://chatgpt.com/s/m_6a5e41b16abc8191af29817acdada3c1)

![Image] (https://chatgpt.com/s/m_6a5e4393db9c819186dda6a9507e7a57)