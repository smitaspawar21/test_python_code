# Flask Project

This is a simple Flask project that contains two APIs: one for login authentication and another for user interaction.

## Project Structure

```
flask-project
├── app
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── user
│   │   ├── __init__.py
│   │   └── routes.py
│   └── models.py
├── run.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## API Endpoints

### Login Authentication

- **Endpoint:** `/auth/login`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response:** 
  - Success: Returns a success message and user token.
  - Failure: Returns an error message.

### User Interaction

- **Endpoint:** `/user/data`
- **Method:** GET
- **Response:**
  ```json
  {
    "name": "User Name",
    "email": "user@example.com",
    "mobile": "1234567890"
  }
  ```

## Running the Application

To run the application, execute the following command:

```
python run.py
```

The application will start on `http://127.0.0.1:5000/`. You can use tools like Postman or curl to interact with the APIs.