CREATE TABLE IF NOT EXISTS CUSTOMER (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FIRST_NAME TEXT,
    LAST_NAME TEXT,
    COUNTRY TEXT,
    CREDIT_LIMIT FLOAT
);
INSERT INTO CUSTOMER (FIRST_NAME, LAST_NAME, COUNTRY, CREDIT_LIMIT)
VALUES ('Alex', 'White', 'USA', 200350.54),
('Tyler', 'Hanson', 'UK', 15354.23),
('Jordan', 'Fernandez', 'France', 359200.67),
('Drew', 'Bradley', 'Albania', 1060.57),
('Blake', 'Fuller', 'USA', 14789.00),
('Spencer', 'Johnston', 'China', 100243.35),
('Ellis', 'Gutierrez', 'USA', 998999.20),
('Morgan', 'Thomas', 'Canada', 500500.23),
('Riley', 'Garza', 'UK', 18782.44),
('Peyton', 'Harris', 'USA', 158367.00);

SELECT id, first_name, last_name
FROM CUSTOMER
WHERE LENGTH(first_name || last_name) < 12
ORDER BY LENGTH(first_name || last_name) ASC, 
         LOWER(first_name || last_name) ASC, 
         id ASC;
