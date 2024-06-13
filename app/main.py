from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

# Create the database tables
# Initializing our FastAPI application
# I have also used HTTPException for error handling using custom status codes
models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

# Endpoint to create a new configuration
@app.post("/create_configuration", response_model=schemas.Configuration)
def create_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(database.get_db)):
    # Check if configuration for the given country_code already exists
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config:
        # If it exists, raise an HTTP 400 Bad Request exception
        raise HTTPException(status_code=400, detail="Configuration already exists")
    # Create and return the new configuration
    return crud.create_configuration(db, config=config)

# Endpoint to get the configuration for a specific country_code
@app.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(database.get_db)):
    # Retrieve the configuration from the database
    db_config = crud.get_configuration(db, country_code=country_code)
    if db_config is None:
        # If the configuration is not found, raise an HTTP 404 Not Found exception
        raise HTTPException(status_code=404, detail="Configuration not found")
    # Return the configuration
    return db_config

# Endpoint to update an existing configuration
@app.post("/update_configuration", response_model=schemas.Configuration)
def update_configuration(config: schemas.ConfigurationUpdate, db: Session = Depends(database.get_db)):
    # Retrieve the existing configuration from the database
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config is None:
        # If the configuration is not found, raise an HTTP 404 Not Found exception
        raise HTTPException(status_code=404, detail="Configuration not found")
    # Update and return the configuration
    return crud.update_configuration(db, config=config)

# Endpoint to delete a configuration by country_code
@app.delete("/delete_configuration/{country_code}", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(database.get_db)):
    # Retrieve the configuration to be deleted from the database
    db_config = crud.get_configuration(db, country_code=country_code)
    if db_config is None:
        # If the configuration is not found, raise an HTTP 404 Not Found exception
        raise HTTPException(status_code=404, detail="Configuration not found")
    # Delete and return the deleted configuration
    return crud.delete_configuration(db, country_code=country_code)
