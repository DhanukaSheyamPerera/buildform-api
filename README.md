# Form Data Management API

## Introduction
This API is designed to manage form data submissions, retrievals, updates, and deletions. Built with FastAPI, it provides a robust set of endpoints that interact with a MongoDB database asynchronously.

## API Endpoints

### Submit Form
- **POST** `/forms`
- Description: Submit a new form data entry.
- Request Body: `FormData`
- Response: `FormDataResponse`

### Get Form Data by ID
- **GET** `/forms/{id}`
- Description: Retrieve form data by its unique identifier.
- Path Parameter: `id` (string)
- Response: `FormData`

### Get All Forms
- **GET** `/forms/`
- Description: Retrieve all form data entries with an optional limit.
- Query Parameter: `limit` (int, optional)
- Response: List of `FormDataResponse`

### Delete Form Data by ID
- **DELETE** `/forms/{id}`
- Description: Delete form data by its unique identifier.
- Path Parameter: `id` (string)
- Security: Basic Authentication
- Response: Message indicating successful deletion

### Update Form Data by ID
- **PUT** `/update-forms/{id}`
- Description: Update an existing form data entry by its unique identifier.
- Path Parameter: `id` (string)
- Request Body: `FormData`
- Security: Basic Authentication
- Response: Updated `FormData`

### Get Forms Count
- **GET** `/forms-count`
- Description: Get the count of all form data records.
- Response: Dictionary with the count of records

## Setup and Installation
To set up this API locally, follow these steps:

1. Clone the repository: git clone [https://github.com/DhanukaSheyamPerera/buildform-api.git]
2. Navigate to the project directory: cd [app]
3. Install the required dependencies: pip install -r requirements.txt
4. Set up your `.env` file with the necessary environment variables.
5. Run the API: uvicorn app.main:app --reload

## Public Demo
The project also hosted on render: [https://buildform-api.onrender.com/docs]


## Environment Variables
To run this project, you will need to add the following environment variables to your `.env` file:

- `MONGODB_USERNAME`: Your MongoDB username.
- `MONGODB_PASSWORD`: Your MongoDB password.
- `MONGODB_CLUSTER_URL`: Your MongoDB cluster URL.
- `AUTHENTICATION_PASSWORD`: The password for HTTP Basic authentication.

## Dependencies
This project uses several external libraries which can be found in the `requirements.txt` file. Some of the key dependencies include:

- FastAPI: For creating the API endpoints.
- Motor: As an async MongoDB driver.
- Pydantic: For data validation and settings management.
- Uvicorn: As an ASGI server for running the application.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
