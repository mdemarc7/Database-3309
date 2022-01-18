-- Select #1
SELECT * FROM User WHERE phone_number LIKE “%3496”;


-- Select #2
SELECT litter_id, SUM(price)
FROM Pet
GROUP BY litter_id
HAVING SUM(price) > 1000;


-- Select #3
SELECT COUNT(pet_id), breed_id
FROM Pet p
LEFT JOIN Litter l ON l.litter_id = p.litter_id
LEFT JOIN Breed b ON b.breed_id = l.breed_id
GROUP BY breed_id
ORDER BY COUNT(pet_id) DESC;


-- Select #4
SELECT COUNT(l.breed_id), b.breed_name FROM Litter l
LEFT JOIN Breed b on l.breed_id=b.breed_id
WHERE parent_1_id IN (
SELECT parent_id FROM pawprint.Parent
WHERE description LIKE ‘%good with kids%’)
GROUP BY b.breed_name
ORDER BY b.breed_name
ORDER BY COUNT(l.breed_id) DESC;


-- Select #5
SELECT COUNT(litter_id), b.breeder_id, b.name as breeder_name
FROM Litter l
LEFT JOIN Breeder b on l.breeder_id=b.breeder_id
GROUP BY b.breeder_id
ORDER BY COUNT(litter_id) DESC;


-- Select #6
USE pawprint;
SELECT litter_id, parent_1_id, parent_2_id
FROM Litter
WHERE parent_1_id IN (
SELECT parent_id
FROM pawprint.Parent
WHERE FLOOR(DATEDIFF(CURRENT_TIMESTAMP, birth_date)/365)<=3
) AND parent_2_id IN (
SELECT parent_id
FROM pawprint.Parent
WHERE FLOOR(DATEDIFF(CURRENT_TIMESTAMP, birth_date)/365)<=3);