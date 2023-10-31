# cloud_db_mgmt_pooling_migrations

[Assignment](https://github.com/hantswilliams/HHA_504_2023/blob/main/WK4/assignment4c-migrations-pools.md):
Gain practical experience in managing a cloud-based MySQL database with a focus on implementing connection pooling and performing database migrations. You will work with both Azure and Google Cloud Platform (GCP) for this assignment.


# Connection Pooling Setup:

## Azure: 
1. Log in Azure with credentials
2. Search `Azure Database for MySQL` and press create under flexible server
3. Choose a Resource Group or create new one
4. Create a server name and under `configurate server` change the compute size to `Standard_B1s (1 vCore, 1 GiB memory, 400 max iops)`
5. Create username and password
6. Under `networking` click, `public access (allowed IP addresses) and private endpoint`
7. Under `Firewall rules` click, `+ Add 0.0.0.0 - 255.255.255.255 and + Add current client IP address (xx.xxx.xxx.xxx)` and create instance
8. Go `server paramters` and set `max_connections` to `20` and `connect_timeout` to `3`

## GCP
1. Log in with Google Cloud credentials
2. Find `sql` then `create instance` and click `choose MySQL`
3. Create an instance ID and password
4. Under `Choose a Cloud SQL edition` click `enterprise`, scroll down and change `preset` to `Sandbox`
5. Under `Customize your instance` click `shared core` and `1 vCPU, 0.164GB option`
6. Under `Connections` and  `Add a Network` put it as `Allow-All` and set it as `0.0.0.0/0`

# 2a. Database Schema and Data
I created a database with 2 tables named: `patients` and `medical_records` in both [GCP](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/blob/main/gcp/gcp_migrations.py) and [Azure](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/blob/main/azure/azure_migrations.py). The tables were populated with random data with a function to generate fake medical record data and fake patient data from faker in [GCP](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/blob/main/gcp/gcppopulate.py) and [Azure](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/blob/main/azure/azurepopulate.py). 

# 2b. Using MySQL Workbench to Generate ERD:
Opening MySQL workbench, using the `+` next to `MySQL Connections`, putting in the hostname, username, and password for both GCP and Azure, this is what the [ERDs](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/tree/main/mysql%20connections) looks like.

# 3. SQLAlchemy and Flask Integration:
To create the application, I reused the [templates](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/tree/main/templates) from previous assignments. The templates folder includes `base.html`, `medical_records.html`, and `patients.html`. An [app.py file](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/blob/main/app.py) was also created for flask integration. I also created a `.env` with my credentials for both GCP and Azure along with a `.gitignore` file to protect the credentials. Screenshots of the flask application can be seen [here](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/tree/main/flaskapp)

# 4. Database Migrations with Alembic:
For database migrations with Alembic, I followed the steps in `Running migrations` shown under `Part 3 - create the tables using sqlalchemy models, with no raw SQL required:`  in the [gcp_migrations.py](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/blob/main/gcp/gcp_migrations.py) and [azure_migrations.py](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/blob/main/azure/azure_migrations.py) file. 
1. In the google shell terminal, type `alembic init migrations`
2. Under the file `alembic.ini` in the shell, edit the section that shows `sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name` with individuals credentials.
3. put `alembic.ini` in the `.gitignore` file
4. Under `env.py` in the shell, change `from db_schema import Base` and `target_metadata = Base.metadata `. In this example, I changed the db_schema to azure_migrations.
5. Make sure to add a comment (#) next to `target_metadata = None`
6. In the shell, type `alembic revision --autogenerate -m "create tables"` to create a migration
7. Run the migration with `alembic upgrade head`
8. To save the migration, type in `alembic upgrade head --sql > migration.sql` in the shell. This will create a `migration.sql` file 
9. Go into GCP and Azure to add another column in either table. For example, I added `discharge_time = Column(String(100))` under the `medical_records` table in both [Azure](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/blob/main/azure/azure_migrations.py) and [GCP](https://github.com/EugeneHsiung/cloud_db_mgmt_pooling_migrations/blob/main/gcp/gcp_migrations.py)
