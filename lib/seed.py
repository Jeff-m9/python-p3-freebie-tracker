#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Company, Dev, Freebie

engine = create_engine("sqlite:///freebies.db")

Base.metadata.create_all(engine)


with Session(engine) as session:


    company1 = Company(name="TechCorp", founding_year=1999)
    company2 = Company(name="InnoSoft", founding_year=2010)
    session.add_all([company1, company2])
    session.commit()


    dev1 = Dev(name="Alice")
    dev2 = Dev(name="Bob")
    session.add_all([dev1, dev2])
    session.commit()

    
    freebie1 = Freebie(item_name="Sticker Pack", value=5, dev=dev1, company=company1)
    freebie2 = Freebie(item_name="Coffee Mug", value=15, dev=dev1, company=company2)
    freebie3 = Freebie(item_name="T-Shirt", value=20, dev=dev2, company=company1)
    session.add_all([freebie1, freebie2, freebie3])
    session.commit()

    print("data created successfully.")
