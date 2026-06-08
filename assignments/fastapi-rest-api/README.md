# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework. This assignment teaches API route creation, request validation, response models, and interactive API documentation.

## 📝 Tasks

### 🛠️ Create a basic FastAPI service

#### Description
Build a FastAPI app that exposes endpoints for managing a simple collection of items.

#### Requirements
Completed program should:

- Define a FastAPI application object named `app`
- Expose at least three endpoints: `GET /items`, `GET /items/{item_id}`, and `POST /items`
- Use path parameters and request bodies appropriately
- Return JSON responses for all routes
- Include a minimal in-memory store for item data

### 🛠️ Add request validation and response models

#### Description
Use Pydantic models to validate incoming requests and format outgoing responses consistently.

#### Requirements
Completed program should:

- Define a Pydantic model for item creation and an output model for item responses
- Validate `POST /items` request data using the input model
- Return validated Pydantic model instances from the API routes
- Handle invalid input gracefully by relying on FastAPI validation errors

### 🛠️ Enable API documentation and test the endpoints

#### Description
Use FastAPI's built-in interactive docs and verify that the routes work as expected.

#### Requirements
Completed program should:

- Run the app with Uvicorn on a local port
- Allow API exploration via `/docs` or `/redoc`
- Demonstrate at least one successful request for each endpoint in the assignment notes or comments

## 📁 Starter files

- `starter-code.py` — skeleton FastAPI app with route placeholders and model definitions

## ▶️ How to run

Install dependencies and start the server:

```bash
python3 -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Then open `http://127.0.0.1:8000/docs` to explore the API documentation.

## ✅ Submission

Submit your completed `starter-code.py` (or rename it to `main.py`) and update this `README.md` with any design decisions or extra features you implemented.
