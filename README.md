
# HNG12 Stage 0 Backend Task

## Project Description
This is a simple public API built using FastAPI for the HNG12 Stage 0 task. The API provides basic information such as the registered email address, the current datetime in ISO 8601 format, and the GitHub repository URL.

## Technology Stack
- Programming Language: Python
- Framework: FastAPI
- Deployment: Hosted on vercel
- CORS Handling: Configured to allow all origins


## How to Run Locally
1. Clone the repository:
   ```bash
   git clone hhttps://github.com/iganya/hng_task0.git
   cd your-repo
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the FastAPI application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
5. Access the API at `http://127.0.0.1:8000/`

## Deployment
The API is deployed to a publicly accessible endpoint.
### **Deploy to Render**
1. Sign up for a free account at Render.
2. Create a new Web Service.
3. Connect your GitHub repository.
4. Set the following configuration:
5. Build Command: pip install -r requirements.txt
6. Start Command: fastapi run main.py
7. Deploy the service.


## API Documentation
### Endpoint
- **URL**: `GET /`
- **Description**: Returns basic information in JSON format.
- **Response Format**: (200 OK)
```json
{
    "email": "matthewiganga@gail.com",
    "current_datetime": "2025-01-31T03:59:54.504837Z",
    "github_url": "https://github.com/Iganya/hng_task-0"
}
```
## **Example Usage**

1. **Make a GET request to the API**:
   ```bash
   curl -X GET https://hng-task-0-w5i6.onrender.com/
    ```
2. **Example Response**:
```json
{
    "email": "matthewiganga@gail.com",
    "current_datetime": "2025-01-31T03:59:54.504837Z",
    "github_url": "https://github.com/Iganya/hng_task-0"
}
```


## Useful Links
- [Hire Python Developers](https://hng.tech/hire/python-developers)
- [Project GitHub Repository](https://github.com/Iganya/hng_task-0)

## License
This project is open-source and available under the MIT License.
