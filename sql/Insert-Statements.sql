-- Insert #1
INSERT INTO User (name, phone_number, email, password, location_id)
VALUES ('Caleb Test', 5193351020, 'ccaldw2@uwo.ca', 'pwd', 1013);


-- Insert #2
INSERT INTO User (name, email, password, location_id)
VALUES ('Mariah Test', 'mdmarc3@uwo.ca', 'pwd2', 4200),
('Arya Test,', 'avatanab@uwo.ca', 'pw3', 1898),
('Rando User', 'rando@gmail.com', 'pwrandom', 224);


-- Insert #3
SELECT phone_number, email, password, location_id
INTO @phone, @email, @pwd, @loc_id
FROM (SELECT phone_number, email
FROM User WHERE user_id = 1)
as merge1
CROSS JOIN
(SELECT password, location_id
FROM User WHERE user_id = 2)
as merge2;
INSERT INTO User (name, phone_number, email, password, location_id)
Values('Franken Tuple', @phone, @email, @pwd, @loc_id);
SELECT * FROM User;