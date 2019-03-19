--1. Does a higher GDP mean more gold medals?


--INSERT OVERWRITE DIRECTORY 'home/cloudera/oozieOutput'
--SELECT country, gdp, count(medal) 
--from countries join athlete on (country = team and medal = "Gold")
--order by country group by gdp;


INSERT OVERWRITE DIRECTORY 'home/cloudera/oozieOutput'
SELECT c.country, count(a.medal)
FROM countries c JOIN athlete a ON (c.country = a.team)
GROUP BY c.country;
