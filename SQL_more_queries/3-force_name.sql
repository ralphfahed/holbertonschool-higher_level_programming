-- This script creates the table 'force_name' if it does not exist
-- The table will have two columns: id (INT) and name (VARCHAR, NOT NULL)

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
