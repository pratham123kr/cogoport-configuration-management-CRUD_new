from sqlalchemy.orm import Session
from .models import Configuration
from .schemas import ConfigurationCreate, ConfigurationUpdate

# making CRUD operations
# GET to fetch data
def get_configuration(db: Session, country_code: str):
    return db.query(Configuration).filter(Configuration.country_code == country_code).first()

# POST operation for making new elements
# Here we pass country_code i.e. IND for India, US for USA etc
# Business_name to have name of businesses
# tax_id if required
# additional_requirement- A JSON field to store any additional onboarding requirements specific to the country. 
#                         This allows for flexibility to accommodate variations without altering the table structure.
def create_configuration(db: Session, config: ConfigurationCreate):
    db_config = Configuration(
        country_code=config.country_code,
        business_name=config.business_name,
        tax_id_type=config.tax_id_type,
        tax_id_required=config.tax_id_required,
        additional_requirements=config.additional_requirements
    )
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

# POST operation to update any field
def update_configuration(db: Session, config: ConfigurationUpdate):
    db_config = get_configuration(db, config.country_code)
    if db_config:
        db_config.business_name = config.business_name
        db_config.tax_id_type = config.tax_id_type
        db_config.tax_id_required = config.tax_id_required
        db_config.additional_requirements = config.additional_requirements
        db.commit()
        db.refresh(db_config)
    return db_config

# DELETE operation
def delete_configuration(db: Session, country_code: str):
    db_config = get_configuration(db, country_code)
    if db_config:
        db.delete(db_config)
        db.commit()
    return db_config
