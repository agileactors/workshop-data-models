-- Drop table if exists
DROP TABLE IF EXISTS ecommerce_schema.users;

-- Remove rows from users table based on user_id
DELETE FROM ecommerce_schema.users WHERE user_id = 1;

-- Add a column
ALTER TABLE ecommerce_schema.users ADD COLUMN phone VARCHAR(15);

-- Modify a column
ALTER TABLE ecommerce_schema.users ALTER COLUMN email TYPE VARCHAR(100);

-- Drop a column
ALTER TABLE ecommerce_schema.users DROP COLUMN phone;

-- Rename a column
ALTER TABLE ecommerce_schema.users RENAME COLUMN email TO user_email;

-- Add a new constraint
ALTER TABLE ecommerce_schema.users ALTER COLUMN username SET NOT NULL;

-- Drop a constraint
ALTER TABLE ecommerce_schema.users DROP CONSTRAINT some_constraint_name;
