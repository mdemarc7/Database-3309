-- Data Modification #1
UPDATE Listing
SET date_closed=DATE_ADD(date_closed, INTERVAL 14 DAY)
WHERE date_closed = ‘2019-11-23’;


-- Data Modification #2
DELETE FROM Listing WHERE litter_id IN
(SELECT litter_id, FROM Litter WHERE breeder_id = ‘49’);


-- Data Modification #3
UPDATE Pet SET price=price-200 WHERE price > 259
AND litter_id in (SELECT litter_id FROM Litter WHERE description not like
‘%updated vaccinations%’);