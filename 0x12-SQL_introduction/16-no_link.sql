-- display the content of second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY name ASC;
