-- Script that prints the description of the first_table in the given database
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table' AND TABLE_SCHEMA = 'hbtn_test_db_5'
ORDER BY ORDINAL_POSITION;
