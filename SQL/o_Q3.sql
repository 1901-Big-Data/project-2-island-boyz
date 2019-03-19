--1. Does a higher GDP mean more gold medals?
USE olympic;

DROP TABLE IF EXISTS q3;

CREATE TABLE q3
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/cloudera/olympicOutput/q3'
AS
select country, population, count(medal) as medals
from countries join athlete
on (country = team and medal = "Gold")
group by country, population;
