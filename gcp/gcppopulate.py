from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from gcp_migrations import Patient, MedicalRecord
import random
from datetime import timedelta
import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")

engine = create_engine(
        connection_string,
        connect_args=connect_args)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker instance
fake = Faker()

# Function to generate fake patient data
def create_fake_patient():
    return Patient(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        date_of_birth=fake.date_of_birth(),
        gender=random.choice(['Male', 'Female']),
        contact_number=fake.phone_number()
    )

# Function to generate fake medical record data
def create_fake_medical_record(patient):
    admission_date = fake.date_between(start_date='-30d', end_date='today')
    discharge_date = admission_date + timedelta(days=random.randint(1, 15))
    return MedicalRecord(
        patient=patient,
        diagnosis=fake.sentence(nb_words=5),
        treatment=fake.paragraph(),
        admission_date=admission_date,
        discharge_date=discharge_date if random.choice([True, False]) else None
    )

# Generate and insert fake data
for _ in range(100):  # Adjust the number of records you want to generate
    fake_patient = create_fake_patient()
    session.add(fake_patient)
    session.commit()
    
    fake_medical_record = create_fake_medical_record(fake_patient)
    session.add(fake_medical_record)
    session.commit()

# Close the session
session.close()

print("Done")