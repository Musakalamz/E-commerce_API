# Demo Video

**Submission:** [Insert Demo Video Link Here]

## Demo Video Script / Checklist

Record a video (max 5 minutes) covering the following points:

### 1. Introduction (0:00 - 0:30)
*   Introduce yourself and the project (E-commerce API).
*   Briefly mention the tech stack (Django, DRF, SQLite/PostgreSQL).

### 2. API Walkthrough via Swagger UI (0:30 - 3:00)
*   Open the Swagger UI (`http://localhost:8000/swagger/`).
*   **Authentication:**
    *   Show getting a token via `/api/token/`.
    *   Authorize in Swagger using the token (`Bearer <token>`).
*   **Categories:**
    *   Show listing categories (`GET /api/categories/`).
    *   Create a new category (`POST`).
*   **Products:**
    *   Create a new product (`POST`) linked to the category.
    *   List products (`GET`).
    *   Show filtering or detail view.

### 3. Code & Best Practices (3:00 - 4:30)
*   Briefly show the code structure in VS Code.
*   Highlight **Models** (relationships).
*   Highlight **Serializers** (validation).
*   Mention **Permissions** (security).

### 4. Conclusion (4:30 - 5:00)
*   Summarize what was achieved.
*   Wrap up.
