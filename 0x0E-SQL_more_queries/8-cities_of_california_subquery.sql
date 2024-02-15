-- script lists all the cities of California that can be
--	found in the database hbtn_0d_usa

-- Results must be sorted in ascending order by cities.id
SELECT * FROM cities
WHERE state_id = (
	SELECT DISTINCT id FROM states
	WHERE name = 'California')
ORDER BY cities.id;

