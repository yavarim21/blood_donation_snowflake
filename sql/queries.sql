-- 1. Total donors per blood type
SELECT blood_type, COUNT(*) AS total_donors
FROM donors
GROUP BY blood_type
ORDER BY total_donors DESC;

-- 2. Average units donated per donor
SELECT donor_id, AVG(units) AS avg_units
FROM donors
GROUP BY donor_id
ORDER BY avg_units DESC;

-- 3. Donations over time (daily)
SELECT donation_date, SUM(units) AS total_units
FROM donors
GROUP BY donation_date
ORDER BY donation_date;

-- 4. Total transfusions per hospital
SELECT hospital_name, SUM(units) AS total_units
FROM transfusions
GROUP BY hospital_name
ORDER BY total_units DESC;

-- 5. Blood type demand vs supply
SELECT d.blood_type,
       SUM(d.units) AS total_donated,
       SUM(t.units) AS total_transfused
FROM donors d
LEFT JOIN transfusions t
  ON d.blood_type = t.blood_type
GROUP BY d.blood_type;
