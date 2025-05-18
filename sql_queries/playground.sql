SELECT * FROM my_table;

INSERT INTO my_table (id, name) VALUES (4, 'John Doe');

UPDATE my_table SET value = 500 WHERE id = 4;

SELECT * FROM my_table WHERE value <= 500 AND value > 450;

INSERT INTO my_table (id,name,value) VALUES (5, 'Jane Doe', 600);

SELECT * FROM my_table WHERE name = 'Jane Doe';

COPY my_table TO '/Users/gomte/Desktop/ml_pipeline_project/data/test.csv' DELIMITER ',' CSV HEADER;

SELECT datname FROM pg_catalog.pg_database WHERE datname = 'smiles_db';

SELECT * from information_schema.tables WHERE table_name = 'my_table';

SELECT * FROM smiles_table;