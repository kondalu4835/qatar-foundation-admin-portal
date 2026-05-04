# Qatar Foundation Admin Portal

A modern, responsive admin portal built with Flask and vanilla JavaScript for managing opportunities and admin accounts.

## Project Overview

This project implements a complete admin portal system with the following features:

### Task 1: Authentication (Day 1)
- **US-1.1**: Admin Sign Up with validation
  - Form validation for required fields
  - Email format validation
  - Password minimum 8 characters
  - Password confirmation matching
  - Duplicate account prevention
  - Redirect to login on success

- **US-1.2**: Admin Login with Remember Me
  - Email and password authentication
  - Generic error messages for security
  - Remember Me checkbox (30-day token)
  - Secure password hashing with bcrypt
  - Session management

- **US-1.3**: Forgot Password
  - Email-based password reset
  - Privacy-protecting generic success message
  - Token-based reset links (1-hour expiration)
  - Expired token handling

### Task 2: Opportunity Management (Day 2)
- **US-2.1**: View All Opportunities
  - Load opportunities from database for logged-in admin
  - Display opportunity cards with key information
  - Empty state when no opportunities exist
  - User-specific data isolation

- **US-2.2**: Add New Opportunity
  - Modal form for creating opportunities
  - Required fields validation
  - Category dropdown (Technology, Business, Design, Marketing, Data Science, Other)
  - Skills as comma-separated list
  - Max applicants as optional field
  - Real-time card display after creation

- **US-2.3**: Opportunities Persist After Login
  - Database persistence across sessions
  - User account isolation
  - Data integrity on logout/login

- **US-2.4**: View Opportunity Details
  - Modal dialog with full opportunity information
  - All saved fields displayed
  - Close functionality

- **US-2.5**: Edit Opportunity
  - Pre-filled form modal with existing data
  - Field validation on update
  - Real-time UI update after save
  - User-specific update validation

- **US-2.6**: Delete Opportunity
  - Confirmation dialog to prevent accidental deletion
  - Permanent database removal
  - Real-time UI removal
  - User-specific deletion validation

## Tech Stack

**Backend:**
- Flask (Python web framework)
- Flask-SQLAlchemy (Database ORM)
- Flask-JWT-Extended (JWT authentication)
- Flask-CORS (Cross-origin resource sharing)
- bcrypt (Password hashing)
- itsdangerous (Token generation)
- SQLite (Database)

**Frontend:**
- HTML5
- CSS3 (Modern gradient design)
- Vanilla JavaScript (No dependencies)
- Fetch API (for API calls)
- LocalStorage (for token management)

## Project Structure

```
.
├── backend/
│   ├── app.py              # Flask application entry point
│   ├── config.py           # Configuration settings
│   ├── extensions.py       # Flask extensions (SQLAlchemy, JWT)
│   ├── models.py           # Database models (User, Opportunity)
│   ├── requirements.txt    # Python dependencies
│   ├── database.db         # SQLite database (auto-created)
│   ├── routes/
│   │   ├── auth.py        # Authentication endpoints
│   │   └── opportunities.py # Opportunity CRUD endpoints
│   └── utils/
│       └── token.py        # Token generation and verification
│
└── frontend/
    ├── index.html          # Main page (redirects based on auth)
    ├── login.html          # Login page
    ├── signup.html         # Signup page
    ├── dashboard.html      # Main dashboard with opportunities
    ├── forgot-password.html # Password reset page
    ├── js/
    │   └── app.js          # Main JavaScript application logic
    └── css/
        └── style.css       # Modern responsive styling
```

## API Endpoints

### Authentication Endpoints

**POST /api/signup**
- Create new admin account
- Request: `{ full_name, email, password, confirm_password }`
- Response: `{ message: "Signup successful" }`
- Status: 201 Created

**POST /api/login**
- Login with credentials
- Request: `{ email, password, remember_me }`
- Response: `{ token, user: { id, name, email } }`
- Status: 200 OK

**POST /api/forgot-password**
- Request password reset
- Request: `{ email }`
- Response: `{ message: "..." }`
- Status: 200 OK

**POST /api/reset-password/<token>**
- Reset password with token
- Request: `{ password }`
- Response: `{ message: "Password reset successful" }`
- Status: 200 OK

### Opportunity Endpoints (All require JWT)

**GET /api/opportunities**
- Get all opportunities for logged-in user
- Response: Array of opportunities
- Status: 200 OK

**POST /api/opportunities**
- Create new opportunity
- Request: Opportunity object with all fields
- Response: `{ message: "Opportunity created" }`
- Status: 201 Created

**GET /api/opportunities/<id>**
- Get single opportunity details
- Response: Opportunity object
- Status: 200 OK

**PUT /api/opportunities/<id>**
- Update opportunity
- Request: Updated opportunity fields
- Response: `{ message: "Updated successfully" }`
- Status: 200 OK

**DELETE /api/opportunities/<id>**
- Delete opportunity
- Response: `{ message: "Deleted successfully" }`
- Status: 200 OK

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser with JavaScript enabled

### 1. Environment Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (if not already done)
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Initialization

The database is automatically created on first run. The SQLite database file (`database.db`) will be created in the `backend/` directory.

### 3. Running the Application

**Terminal 1: Start Backend (Flask Server)**
```bash
cd backend
python app.py
# Server runs on http://127.0.0.1:5000
```

**Terminal 2: Start Frontend (HTTP Server)**
```bash
cd frontend
python -m http.server 8000
# Frontend runs on http://localhost:8000
```

### 4. Access the Application

Open your browser and navigate to:
```
http://localhost:8000
```

The application will redirect to the login page if not authenticated.

## User Flow

1. **New User**: Click "Create an account" → Fill signup form → Auto-redirect to login
2. **Existing User**: Enter credentials → Optional "Remember Me" → Dashboard loads
3. **Dashboard**: Create, view, edit, or delete opportunities
4. **Logout**: Click "Logout" button → Redirect to login page

## Security Features

- **Password Hashing**: bcrypt with salt rounds
- **JWT Authentication**: Secure token-based authentication
- **CORS Protection**: Configured for proper cross-origin requests
- **Token Expiration**: 1 hour default, 30 days with Remember Me
- **User Isolation**: Users can only see/modify their own opportunities
- **Input Validation**: Both client and server-side validation
- **Email Validation**: RFC-compliant email format checking
- **Generic Error Messages**: Security-conscious error responses

## Frontend Features

### Modern UI Design
- Responsive grid layout for opportunity cards
- Modal dialogs for forms and details
- Smooth animations and transitions
- Professional gradient color scheme
- Mobile-friendly responsive design

### Form Validation
- Required field checking
- Email format validation
- Password strength enforcement
- Confirm password matching
- Category dropdown selection
- Empty field error messages

### Real-time Updates
- Opportunities load immediately after creation
- Edit modal pre-fills existing data
- Delete confirmation before removal
- Success/error message notifications

## Database Schema

### Users Table
- id (Primary Key)
- full_name (String, Required)
- email (String, Unique, Required)
- password (String, Hashed, Required)
- created_at (DateTime)

### Opportunities Table
- id (Primary Key)
- user_id (Foreign Key, Required)
- name (String, Required)
- duration (String, Required)
- start_date (String, Required)
- description (Text, Required)
- skills (Text, Required, Comma-separated)
- category (String, Required)
- future_opportunities (Text, Required)
- max_applicants (Integer, Optional)
- created_at (DateTime)

## Testing the Application

### Test Signup
1. Navigate to signup page
2. Enter: Name, Email, 8+ char password, matching confirm
3. Click Create Account
4. Should redirect to login with success message

### Test Login
1. Enter credentials from signup
2. Check "Remember Me" (optional)
3. Click Login
4. Should redirect to dashboard

### Test Opportunities CRUD
1. Click "+ Add New Opportunity"
2. Fill all required fields
3. Click "Save Opportunity"
4. Card should appear in list
5. Click "Edit" to modify
6. Click "Delete" with confirmation

### Test Data Persistence
1. Add opportunities
2. Logout
3. Login with same credentials
4. Verify all opportunities still appear

## Troubleshooting

### Issue: 401 Unauthorized on API calls
**Solution**: Ensure token is being sent in Authorization header. Check browser console for errors. Token should be stored in localStorage after successful login.

### Issue: CORS errors
**Solution**: Ensure frontend is served over HTTP (not file://). Use the provided HTTP server on port 8000.

### Issue: Database locked
**Solution**: Remove the `database.db` file to start fresh, then restart the application.

### Issue: "ModuleNotFoundError" when running backend
**Solution**: Ensure virtual environment is activated and dependencies are installed with `pip install -r requirements.txt`

## Future Enhancements

- Email notifications for password reset links
- Applicant tracking for opportunities
- Advanced filtering and search
- Opportunity templates
- Bulk operations
- Analytics dashboard
- File upload for opportunity materials
- Multi-language support
- Two-factor authentication
- User role management

## Development Notes

- The application uses SQLite for simplicity. For production, consider PostgreSQL or MySQL.
- JWT tokens are stored in localStorage for simplicity. Consider using HttpOnly cookies for enhanced security.
- The frontend uses vanilla JavaScript. For larger applications, consider React or Vue.js.
- All API responses include appropriate HTTP status codes for error handling.
- Password reset links are logged to console (not actually emailed) for development.

## License

This project is part of the Qatar Foundation Admin Portal initiative.

## Support

For issues or questions, please refer to the user stories documentation or contact the development team.

---

**Version**: 1.0.0  
**Last Updated**: May 2026  
**Framework Versions**: Flask 2.3.3, Python 3.8+
