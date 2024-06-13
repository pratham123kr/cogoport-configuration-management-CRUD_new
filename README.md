Here we are using postgres database and its connection URL is set in .env file
Its default format is - DATABASE_URL=postgresql://username:password@localhost:5432/dbname
User needs to make this database on their postgres account

# Configuration API

This repository contains a FastAPI application for managing configurations for different countries. Each configuration includes details such as country code, business name, tax ID requirements, and additional requirements. The API supports CRUD operations (Create, Read, Update, Delete) for these configurations.

## Features

- Create a new configuration
- Read an existing configuration by country code
- Update an existing configuration
- Delete a configuration by country code

## Requirements

- Python 3.0+
- FastAPI
- SQLAlchemy
- Pydantic
- uvicorn
- python-dotenv

## Installation

1. Clone the repository and navigate to the project directory.

2. Create a virtual environment and activate it.

3. Install the required dependencies using pip.

## Environment Variables

Create a `.env` file in the root directory of the project and add your database URL as follows:
- DATABASE_URL=sqlite:///./test.db (Replace with your actual database URL)

## Running the Application

1. Initialize the database.

2. Start the FastAPI application using uvicorn.

   The application will be available at http://127.0.0.1:8000.

## API Endpoints

### Create Configuration

- **Endpoint**: `/create_configuration`
- **Method**: `POST`
- **Request Body**:
  - country_code: "IND"
  - business_name: "My Business"
  - tax_id_type: "GST"
  - tax_id_required: true
  - additional_requirements: {
      "requirement1": "value1",
      "requirement2": "value2"
    }
- **Response**:
  - id: 1
  - country_code: "IND"
  - business_name: "My Business"
  - tax_id_type: "GST"
  - tax_id_required: true
  - additional_requirements: {
      "requirement1": "value1",
      "requirement2": "value2"
    }

### Get Configuration

- **Endpoint**: `/get_configuration/{country_code}`
- **Method**: `GET`
- **Response**:
  - id: 1
  - country_code: "IND"
  - business_name: "My Business"
  - tax_id_type: "GST"
  - tax_id_required: true
  - additional_requirements: {
      "requirement1": "value1",
      "requirement2": "value2"
    }

### Update Configuration

- **Endpoint**: `/update_configuration`
- **Method**: `POST`
- **Request Body**:
  - country_code: "IND"
  - business_name: "Updated Business"
  - tax_id_type: "PAN"
  - tax_id_required: false
  - additional_requirements: {
      "requirement1": "newValue1"
    }
- **Response**:
  - id: 1
  - country_code: "IND"
  - business_name: "Updated Business"
  - tax_id_type: "PAN"
  - tax_id_required: false
  - additional_requirements: {
      "requirement1": "newValue1"
    }

### Delete Configuration

- **Endpoint**: `/delete_configuration/{country_code}`
- **Method**: `DELETE`
- **Response**:
  - id: 1
  - country_code: "IND"
  - business_name: "My Business"
  - tax_id_type: "GST"
  - tax_id_required: true
  - additional_requirements: {
      "requirement1": "value1",
      "requirement2": "value2"
    }

## Database Models

### Configuration

- id: Integer, Primary Key
- country_code: String, unique, non-nullable
- business_name: String, non-nullable
- tax_id_type: String, nullable
- tax_id_required: Boolean, non-nullable
- additional_requirements: JSON, nullable

## Schemas

### ConfigurationBase

- country_code: str
- business_name: str
- tax_id_type: Optional[str]
- tax_id_required: bool
- additional_requirements: Optional[Dict[str, Any]]
