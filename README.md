# 📺 Late Show API

This is a RESTful API for managing **Late Show episodes**, **guests**, and their **appearances** using **Flask** and **SQLAlchemy**.  
It allows clients to retrieve episodes and guests, and create new guest appearances on specific episodes.

---

## 🚀 Features

- View all Late Show episodes
- View a single episode with full guest appearance data
- View all guests
- Add a new guest appearance with validation

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (local database)
- Postman (for testing)

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/lateshow-firstname-lastname.git
cd lateshow-firstname-lastname

2. Create a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# OR
venv\Scripts\activate  # On Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Initialize the Database
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
5. Seed the Database
Make sure you have the lateshow.csv file in your root directory.
Then run:

bash
Copy
Edit
python seed.py
▶️ Running the Server
bash
Copy
Edit
python app.py
The API will run on:

arduino
Copy
Edit
http://localhost:5555
🔌 API Endpoints
GET /episodes
Returns a list of all episodes.

json
Copy
Edit
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  }
]
GET /episodes/<id>
Returns details of a specific episode including appearances.

json
Copy
Edit
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "guest_id": 1,
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}
Returns 404 if episode is not found.

GET /guests
Returns a list of all guests.

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  }
]
POST /appearances
Creates a new appearance.

Request JSON:

json
Copy
Edit
{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}
Response JSON (201):

json
Copy
Edit
{
  "id": 162,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
Error Response (422):

json
Copy
Edit
{
  "errors": ["Invalid episode_id or guest_id"]
}
✅ Validations
Appearance.rating must be between 1 and 5 (inclusive).

Appearance must reference a valid Guest and Episode.

✍️ Author
Name: Wamae Presbury

Moringa School, Phase 4 Project

🗂️ License
This project is for educational purposes only.

yaml
Copy
Edit

---

## 📥 Final Steps

### 1. Save the README
Create a file called `README.md` and paste the content.

### 2. Add + Commit + Push

```bash
git add README.md
git commit -m "Add README documentation for Late Show API"
git push origin main
