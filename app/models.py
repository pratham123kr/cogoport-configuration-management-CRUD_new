from sqlalchemy import Column, Integer, String, JSON, Boolean
from .database import Base

# Here we are creating tables that we want to be saved
# in our database.

# Below is the structure of our table
# (1) We will give unique id to each entry
# (2) Country_code- This will take a string input like IND for India, US for USA
# (3) Business_name- it will take string input and name of the business/company
# (4) Tax_id_type: this will take string as an input to give tax types like- GST for India 
# (5) Tax_id_required: a bool type to to show if the tax_id for given country required
# (6) additional_requirements: this will take JSON value of format Dict['string':Any] so we can add any type of
#  additional information unique to that country in a dict/json format
class Configuration(Base):
    # name of table
    __tablename__ = 'configurations'

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, unique=True, index=True, nullable=False)
    business_name = Column(String, nullable=False)
    tax_id_type = Column(String, nullable=True)
    tax_id_required = Column(Boolean, nullable=False)
    additional_requirements = Column(JSON, nullable=True)
