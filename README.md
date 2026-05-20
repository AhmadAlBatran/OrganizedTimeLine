# OrganizedTimeLine

A calendar app where you can create, edit, and manage events. Built with Flask and FullCalendar.

a full version is currently deployed using render services.

**🚀 Try it live**: https://organizedtimeline.onrender.com

to run it locally follow the following steps :
## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your database connection:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/calendar_db
   ```

3. Run the app:
   ```bash
   python app.py
   ```

Open `http://localhost:5000` in your browser.

## Features

- Sign up and login with user accounts
- password hashing
- Create events by clicking on calendar dates
- Edit event details (title, description, time)
- Drag and drop events to change dates/times
- Resize events to adjust duration
- Delete events
- Multiple calendar views (day, week, month)
- All events saved to database

## How to Use

1. **Sign Up**: Create a new account with username and password
2. **Login**: Log in with your credentials
3. **Create Event**: Click on any date/time slot, enter event title
4. **Edit Event**: Click an event to modify title, description, or time
5. **Move Event**: Drag events to different dates or times
6. **Delete Event**: Click event → select "Delete Event"
7. **Logout**: Click logout button when done

## Tech Stack

- **Backend**: Flask, SQLAlchemy, PostgreSQL
- **Frontend**: HTML, JavaScript, Bootstrap, FullCalendar

## Project Files

- `app.py` - Flask backend with all API routes
- `index.html` - Login/sign-up page
- `calendar.html` - Main calendar interface
- `requirements.txt` - Python dependencies

## Requirements

- Python 3.8+
- PostgreSQL database
- pip

## Database

- **Users Table**: Stores usernames and passwords and  
- **Events Table**: Stores event details linked to users
- 
## Database
 
- **Users Table**: Stores usernames and passwords
- **Events Table**: Stores event details linked to users
![Database Schema](DB_Schema.png)

provided by SupaBase Schema Visualizer 

## Future Features

- Email notifications for upcoming events
- Event categories and color coding
- Calendar sharing between users
- Recurring events
- Dark mode
