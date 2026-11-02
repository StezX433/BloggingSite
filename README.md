# Moh Blog – Full Stack Blogging Application

A full-stack blogging application built using **React.js** for the frontend and **FastAPI** for the backend. Users can create accounts, log in, publish blog posts, edit their own posts, and manage their content through a simple web interface.

## Features

### User Authentication
- User registration (Signup).
- User login.
- JWT-based authentication.
- Token storage using browser localStorage.

### Blog Management
- View all published posts.
- Create new blog posts.
- Edit existing posts.
- Delete your own posts.
- Display post titles, content, and author information.

### User Management
- View registered users.
- Store user information after authentication.

### Frontend
- React.js component-based architecture.
- React Router for navigation.
- Bootstrap for styling.
- Dynamic forms using React Hooks.

### Backend
- FastAPI REST API.
- JSON-based API communication.
- Authentication using Bearer tokens.

## Tech Stack

| Technology | Purpose |
|---|---|
| React.js | Frontend |
| JavaScript | Frontend programming |
| Bootstrap 5 | UI styling |
| React Router DOM | Client-side routing |
| FastAPI | Backend framework |
| Python | Backend programming |
| JWT | Authentication |
| REST API | Frontend-backend communication |

## Project Structure

```text
BloggingSite/
│
├── main.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   └── Navbar.js
│   │   │
│   │   ├── pages/
│   │   │   ├── Login.js
│   │   │   ├── Signup.js
│   │   │   ├── Posts.js
│   │   │   ├── CreatePost.js
│   │   │   ├── EditPost.js
│   │   │   └── AllUsers.js
│   │   │
│   │   ├── App.js
│   │   └── index.js
│   │
│   └── package.json
│
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd BloggingSite
```

### 2. Backend Setup

Create and activate a Python virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### 3. Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm start
```

Frontend runs at:

```text
http://localhost:3000
```

## API Integration

The React frontend communicates with the FastAPI backend using HTTP requests.

Base API URL:

```javascript
const API_URL = "http://127.0.0.1:8000";
```

The application uses the following API paths:

| Endpoint | Method | Purpose |
|---|---|---|
| `/signup/` | POST | Register a new user |
| `/login/` | POST | Authenticate a user |
| `/posts/` | GET | Retrieve blog posts |
| `/posts/` | POST | Create a post |
| `/posts/{id}/` | GET | Retrieve a specific post |
| `/posts/{id}/` | PUT | Update a post |
| `/posts/{id}/` | DELETE | Delete a post |

*Endpoint methods should be verified against the backend implementation.*

## Authentication Flow

1. Users register using their username, email, and password.
2. Users log in using their email and password.
3. The backend returns an authentication token.
4. The frontend stores the token in localStorage.
5. Authenticated requests include the token in the Authorization header.

Example:

```javascript
headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`
}
```

## Running the Application

Start the backend and frontend in separate terminals.

**Terminal 1 – Backend**

```bash
uvicorn main:app --reload
```

**Terminal 2 – Frontend**

```bash
cd frontend
npm start
```

Open your browser:

```text
http://localhost:3000
```

## Learning Outcomes

This project demonstrates practical implementation of:

- Full-stack web application development.
- REST API development using FastAPI.
- React functional components and Hooks.
- Client-side routing.
- JWT-based authentication.
- CRUD operations.
- Frontend and backend integration.
- Asynchronous API requests using Fetch.

## Author

**Moh Technology**

Full Stack Development Project
