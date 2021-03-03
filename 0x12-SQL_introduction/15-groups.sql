-- group by score!
SELECT score, COUNT(*)
FROM second_table AS score, number
GROUP BY score
ORDER BY score DESC;
