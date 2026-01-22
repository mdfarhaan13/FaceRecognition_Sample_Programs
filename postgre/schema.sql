CREATE TABLE missing_persons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    last_seen_location TEXT
);

INSERT INTO missing_persons (name, age, last_seen_location)
VALUES ('John Doe', 35, 'Chennai');
