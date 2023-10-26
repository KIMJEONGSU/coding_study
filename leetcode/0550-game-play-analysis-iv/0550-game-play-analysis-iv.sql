SELECT ROUND(SUM(tmp)/COUNT(DISTINCT player_id),2) as fraction
FROM (SELECT player_id,
       DATEDIFF(event_date, MIN(event_date) OVER(PARTITION BY player_id))=1 AS tmp
       FROM Activity) A