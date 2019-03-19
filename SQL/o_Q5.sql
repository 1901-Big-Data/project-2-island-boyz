--1. Does a higher GDP mean more gold medals?
USE olympic;

DROP TABLE IF EXISTS q5;

CREATE TABLE q5
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/cloudera/olympicOutput/q5'
AS
select country, literacy, count(medal) as medals
from countries join athlete
on (country = team and medal != "NA")
group by country, literacy;
