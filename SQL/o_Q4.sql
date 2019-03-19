--1. Does a higher GDP mean more gold medals?
USE olympic;

DROP TABLE IF EXISTS q4;

CREATE TABLE q4
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/cloudera/olympicOutput/q4'
AS
select country, population, count(medal) as medals
from countries join athlete
on (country = team and medal != "NA")
group by country, population;
