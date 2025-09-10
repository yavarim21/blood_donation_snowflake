-- Create donors table
CREATE OR REPLACE TABLE donors (
    donor_id INT,
    donor_name STRING,
    age INT,
    blood_type STRING,
    donation_date DATE,
    units INT
);

-- Create transfusions table
CREATE OR REPLACE TABLE transfusions (
    transfusion_id INT,
    hospital_name STRING,
    blood_type STRING,
    units INT,
    transfusion_date DATE
);
