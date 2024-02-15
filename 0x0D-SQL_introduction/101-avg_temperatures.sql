-- script displays the average temperature 
-- 	(Fahrenheit) by city ordered by temperature

-- Data imported from temperature.sql dump
SELECT city, 
	avg(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
