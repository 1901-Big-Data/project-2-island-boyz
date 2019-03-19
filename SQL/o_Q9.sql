--1. Does a higher GDP mean more gold medals?
USE olympic;

DROP TABLE IF EXISTS q9;

CREATE TABLE q9
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/cloudera/olympicOutput/q9'
AS
select country, agriculture, count(medal) as gold_medals 
from countries join athlete 
on (country = team and medal = "Gold" and year >= 1980) 
group by country, agriculture;
