
WITH CTE AS (
    SELECT *, ROW_NUMBER() OVER (ORDER BY visit_date) AS row_id
    FROM (SELECT * FROM stadium WHERE people > 100) t
)

SELECT id, visit_date, people
FROM
    stadium, (SELECT min(id) m, max(id) n FROM cte GROUP BY (id - row_id) HAVING COUNT(id - row_id) >= 3) t
WHERE id BETWEEN m and n
