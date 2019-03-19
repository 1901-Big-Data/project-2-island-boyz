--1. Does a higher GDP mean more gold medals?
USE olympic;

DROP TABLE IF EXISTS q7;

CREATE TABLE q7
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/cloudera/olympicOutput/q7'
AS
select country, count(medal) as medals
from countries join athlete
on (country = team and medal != "NA")
group by country
order by medals limit 1;
