# I. Setup Guide — How It Works

This section explains step by step how to run the project locally, including the **LanguageTool server**, the **FastAPI backend**, and the **web interface**.

## I. Running LanguageTool as a Local Server

### STEP 1 — Install Java (Required)

This project **requires Java 17** to run the LanguageTool server.

Verify your Java installation:

```bash
java -version
```

Expected output should indicate **Java 17**.

### STEP 2 — Download LanguageTool Manually

From your browser, download LanguageTool from the official website:

👉 [https://languagetool.org/download/](https://languagetool.org/download/)

Download the following archive:

```
LanguageTool-6.6.zip
```

Then extract and navigate into the directory:

```bash
unzip LanguageTool-6.6.zip
cd LanguageTool-6.6
```

### STEP 3 — Start the LanguageTool Server

Run the following command to start LanguageTool in HTTP server mode:

```bash
java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081
```

✅ Expected output:

```text
Starting LanguageTool HTTP server on port 8081
```

This means the LanguageTool server is now running locally and ready to accept requests.

---

## II. Running the FastAPI Backend

### Backend Configuration

Navigate to the backend directory and set up a Python virtual environment:

```bash
# Go to the backend directory
cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Start the FastAPI Server

Launch the API using Uvicorn:

```bash
uvicorn app.main:app --reload
```

Once started, the API will be available at:

```
http://localhost:8000
```

Swagger API documentation:

```
http://localhost:8000/docs
```

## III. Launching the Web Interface

To run the frontend, simply navigate to the `frontend` directory and open the HTML file.

You can either run:

```bash
firefox index.html
```

or **double-click** on the `index.html` file.

✔️ No build step required
✔️ No bundler needed
✔️ React runs via CDN

## API Endpoint

### POST `/correct`

#### Request

```json
{
  "text": "bonjourr madamw"
}
```

#### Response

```json
{
  "original_text": "bonjourr madamw",
  "corrected_text": "Bonjour madame",
  "errors": [
    {
      "id": 1,
      "error": "bonjourr",
      "message": "Faute de frappe possible trouvée.",
      "category": "Orthographe",
      "suggestions": ["Bonjour"]
    }
  ],
  "statistics": {
    "word_count": 2,
    "error_count": 1
  }
}
```

---

## Summary

1. Start **LanguageTool** (Java 17, port 8081)
2. Start **FastAPI backend** (port 8000)
3. Open **index.html** in your browser
