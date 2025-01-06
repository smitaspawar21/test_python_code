# Simple Node.js Project

This project is a simple Node.js application that provides two APIs: one for user login and another for retrieving user data.

## Project Structure

```
simple-nodejs-project
├── src
│   ├── app.js
│   ├── controllers
│   │   ├── authController.js
│   │   └── userController.js
│   ├── routes
│   │   ├── authRoutes.js
│   │   └── userRoutes.js
│   └── models
│       └── userModel.js
├── package.json
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd simple-nodejs-project
   ```

3. Install the dependencies:
   ```
   npm install
   ```

4. Start the application:
   ```
   npm start
   ```

## API Endpoints

### User Login

- **Endpoint:** `/api/login`
- **Method:** POST
- **Parameters:**
  - `username`: The username of the user.
  - `password`: The password of the user.

### Retrieve User Data

- **Endpoint:** `/api/user`
- **Method:** GET
- **Response:**
  - `name`: The name of the user.
  - `email`: The email of the user.
  - `mobile`: The mobile number of the user.

## License

This project is licensed under the MIT License.