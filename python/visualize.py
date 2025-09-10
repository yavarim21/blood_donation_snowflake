import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# 1. Connect to Snowflake
# --------------------------
conn = snowflake.connector.connect(
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT',
    warehouse='YOUR_WAREHOUSE',
    database='BLOOD_DB',
    schema='BLOOD_SCHEMA'
)

# --------------------------
# 2. Run a query
# --------------------------
query = """
SELECT blood_type, COUNT(*) AS total_donors
FROM donors
GROUP BY blood_type
ORDER BY total_donors DESC
"""

df = pd.read_sql(query, conn)

# --------------------------
# 3. Visualization: Donors per Blood Type
# --------------------------
plt.figure(figsize=(8,6))
sns.barplot(data=df, x='blood_type', y='total_donors', palette='Reds')
plt.title("Total Donors per Blood Type")
plt.xlabel("Blood Type")
plt.ylabel("Number of Donors")
plt.savefig("../images/donors_per_blood_type.png")
plt.show()

# --------------------------
# 4. Optional: Donations Over Time
# --------------------------
query2 = """
SELECT donation_date, SUM(units) AS total_units
FROM donors
GROUP BY donation_date
ORDER BY donation_date
"""
df2 = pd.read_sql(query2, conn)

plt.figure(figsize=(10,6))
sns.lineplot(data=df2, x='donation_date', y='total_units', marker='o')
plt.title("Donations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Units Donated")
plt.savefig("../images/donations_over_time.png")
plt.show()

# Close connection
conn.close()
