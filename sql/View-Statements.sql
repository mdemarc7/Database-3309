-- Create View #1
CREATE VIEW Expensive_Pets AS SELECT * FROM Pet WHERE price > 500;


-- Create View #2
CREATE VIEW User_With_Location AS
SELECT user_id, name, phone_number, email, password,
u.location_id, province, city, street, address_number,
postal_code
FROM User u LEFT JOIN Location l ON u.location_id = l.location_id;


-- Create View #3
CREATE VIEW Breed_Inventory AS SELECT COUNT(pet_id), b.breed_name
FROM Pet p
LEFT JOIN Litter l ON p.litter_id = l.litter_id
LEFT JOIN Breed b ON l.breed_id = b.breed_id
GROUP BY l.breed_id
ORDER BY COUNT(pet_id) DESC;