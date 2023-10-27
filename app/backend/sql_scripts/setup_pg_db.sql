--####################################################--
------------------ Creating Schemas --------------------
--####################################################--

CREATE SCHEMA IF NOT EXISTS test_schema;

--###############################################--
------------------ Test Database ------------------
--###############################################--

CREATE TABLE IF NOT EXISTS test_schema.test_table (
    column_name_1 INT NOT NULL,
    column_name_2 VARCHAR(200),
    column_name_3 FLOAT
	);

DELETE FROM test_schema.test_table;
INSERT INTO test_schema.test_table values (1, '1968', 2.1);
INSERT INTO test_schema.test_table values (2, '1969', 2.1);