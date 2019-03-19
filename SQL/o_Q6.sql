--1. Does a higher GDP mean more gold medals?
USE olympic;

DROP TABLE IF EXISTS q6;

CREATE TABLE q6
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/cloudera/olympicOutput/q6'
AS
select country, count(medal) as medals
from countries join athlete
on (country = team and medal != "NA")
group by country
order by medals desc limit 1;
