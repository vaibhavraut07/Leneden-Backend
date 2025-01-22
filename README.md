# Leneden-Backend

# Tic-Tac-Toe Backend Project

This is a backend system for a Tic-Tac-Toe game built using Django and Django REST Framework. It supports user registration, login, game creation, move tracking, and game history.

---

## **Features**
- User registration and login with JWT authentication.
- Create a new game between two players.
- Make moves in the game and track the game state.
- Automatically assign `X` or `O` to players based on their role in the game.
- Fetch game details and history for a user.
- Declare a winner or draw when the game is over.

---

## **API Documentation**

### **Base URL**
All API endpoints are prefixed with `/api/`.

---

### **1. User Registration**
Register a new user.

- **URL**: `/api/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "player1",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "username": "player1"
  }
  ```

---

### **2. User Login**
Log in a user and get an access token.

- **URL**: `/api/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "player1",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
  }
  ```

---

### **3. Create a Game**
Create a new game between two players.

- **URL**: `/api/games/`
- **Method**: `POST`
- **Headers**:
  - `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
      "player2": 2  // ID of the second player
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "player1": 1,
      "player2": 2,
      "winner": null,
      "is_draw": false,
      "created_at": "2023-10-10T12:34:56Z",
      "moves": [],
      "game_board": "   |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
  }
  ```

---

### **4. Make a Move**
Make a move in the game. The `symbol` (`X` or `O`) is automatically assigned based on the player's role in the game.

- **URL**: `/api/moves/`
- **Method**: `POST`
- **Headers**:
  - `Authorization: Bearer <access_token>`
- **Request Body**:
  ```json
  {
      "game": 1,   // ID of the game
      "position": 0  // Position on the board (0-8)
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "game": 1,
      "player": 1,
      "position": 0,
      "symbol": "X",  // Automatically assigned based on the player
      "created_at": "2023-10-10T12:35:00Z"
  }
  ```

---

### **5. Fetch Game Details**
Fetch the details of a specific game, including the current state of the game board.

- **URL**: `/api/games/<game_id>/`
- **Method**: `GET`
- **Headers**:
  - `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  {
      "id": 1,
      "player1": 1,
      "player2": 2,
      "winner": null,
      "is_draw": false,
      "created_at": "2023-10-10T12:34:56Z",
      "moves": [
          {
              "id": 1,
              "game": 1,
              "player": 1,
              "position": 0,
              "symbol": "X",
              "created_at": "2023-10-10T12:35:00Z"
          }
      ],
      "game_board": "X |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
  }
  ```

---

### **6. Fetch Game History**
Fetch the game history for a user.

- **URL**: `/api/history/`
- **Method**: `GET`
- **Headers**:
  - `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  [
      {
          "id": 1,
          "player1": 1,
          "player2": 2,
          "winner": null,
          "is_draw": false,
          "created_at": "2023-10-10T12:34:56Z",
          "moves": [
              {
                  "id": 1,
                  "game": 1,
                  "player": 1,
                  "position": 0,
                  "symbol": "X",
                  "created_at": "2023-10-10T12:35:00Z"
              }
          ],
          "game_board": "X |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
      }
  ]
  ```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/tic-tac-toe-backend.git
cd tic-tac-toe-backend
```

### **2. Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**
```bash
python manage.py migrate
```

### **5. Run the Server**
```bash
python manage.py runserver
```

The server will run at `http://127.0.0.1:8000/`.

---

## **Testing the APIs**
You can test the APIs using tools like **Postman** or **cURL**. Here’s an example workflow:

1. **Register two users**:
   - Register `player1` and `player2` using the `/api/register/` endpoint.

2. **Log in as `player1`**:
   - Use the `/api/login/` endpoint to get an access token.

3. **Create a game**:
   - Use the `/api/games/` endpoint to create a game between `player1` and `player2`.

4. **Make moves**:
   - Use the `/api/moves/` endpoint to make moves alternately for `player1` and `player2`. The `symbol` (`X` or `O`) will be automatically assigned.

5. **Fetch game details**:
   - Use the `/api/games/<game_id>/` endpoint to check the current state of the game, including the game board.

6. **Fetch game history**:
   - Use the `/api/history/` endpoint to see all games played by a user.

---

## **Technologies Used**
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default), can be replaced with PostgreSQL or MySQL
- **Authentication**: JWT (JSON Web Tokens)
- **API Testing**: Postman

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**
If you have any questions or need further assistance, feel free to reach out:
- **Email**: work.vaibhavraut@gmail.com
- **GitHub**: vaibhavraut07
```
