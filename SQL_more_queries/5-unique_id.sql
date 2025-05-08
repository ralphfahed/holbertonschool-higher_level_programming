-- This script creates the table 'unique_id' if it does not exist
-- The 'id' column is INT, has a default value of 1, and is UNIQUE
-- The 'name' column is a variable character string (max 256 chars)

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
