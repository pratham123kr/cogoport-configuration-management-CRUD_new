from pydantic import BaseModel
from typing import Dict, Any, Optional

# Here we provide schemas for all types of requests
# These schemas define the structure and validation for the data used in our API

# Base schema that all configurations inherit from
class ConfigurationBase(BaseModel):
    country_code: str
    business_name: str
    tax_id_type: Optional[str] = None
    tax_id_required: bool
    additional_requirements: Optional[Dict[str, Any]] = None

# Schema for creating a new configuration
class ConfigurationCreate(ConfigurationBase):
    pass  # Inherits all fields from ConfigurationBase without modification

# Schema for updating an existing configuration
class ConfigurationUpdate(ConfigurationBase):
    pass  # Inherits all fields from ConfigurationBase without modification

# Schema for returning a configuration, includes an ID field
class Configuration(ConfigurationBase):
    # Unique identifier for the configuration entry
    id: int

    # Configuration class that enables the ORM mode in Pydantic models
    # This allows the model to work seamlessly with ORM objects (e.g., SQLAlchemy)
    class Config:
        orm_mode = True
