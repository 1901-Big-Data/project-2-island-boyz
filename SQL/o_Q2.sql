--1. Does a higher GDP mean more gold medals?
USE olympic;

DROP TABLE IF EXISTS q2;

CREATE TABLE q2
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/cloudera/olympicOutput/q2'
AS
select country, gdp, count(medal) as medals
from countries join athlete
on (country = team and medal != "NA")
group by country, gdp;
