--1. Does a higher GDP mean more gold medals?
USE olympic;

DROP TABLE IF EXISTS q1;

CREATE TABLE q1
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/cloudera/olympicOutput/q1'
AS
SELECT country, gdp, count(medal) AS gold_medals
FROM countries JOIN athlete
ON (country = team AND medal = "Gold")
GROUP BY country, gdp;
