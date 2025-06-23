# 📘 Simple MySQL CRUD Guide

This is a simple guide to using MySQL for basic database operations.

---

## 🔹 Step 1: Create a Table

```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100),
  age INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Insert
```sql

INSERT INTO users (name, email, age) VALUES
('Alice', 'alice@example.com', 25),
('Bob', 'bob@example.com', 30),
('Charlie', 'charlie@example.com', 22),
('David', 'david@example.com', 28);
```

## View Data (READ)
Show all users:
```python
SELECT * FROM users;
Show user with ID = 2:
```
```python
SELECT * FROM users WHERE id = 2;

```
## Add New User (CREATE)
```python
INSERT INTO users (name, email, age)
VALUES ('Eve', 'eve@example.com', 27);
```

## UPDATE users
```python
SET age = 31
WHERE name = 'Bob';
```
## DELETE
```python
DELETE FROM users WHERE name = 'Charlie';
```
## Extra: Filter, Sort, Count
 ### Show users over age 25:
 ```python
SELECT * FROM users WHERE age > 25;

```

```python
SELECT * FROM users ORDER BY age ASC;

```

### Count how many users:
```python
SELECT COUNT(*) FROM users;
```
