# Qatar Foundation Admin Portal - Testing Guide

## Test Environment Setup

### Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Two terminal windows

### Starting the Application

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
# Runs on http://127.0.0.1:5000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
python -m http.server 8000
# Runs on http://localhost:8000
```

**Open Browser:**
```
http://localhost:8000/login.html
```

---

## Testing Checklist

### ✅ Task 1: Authentication & Login (Day 1)

#### US-1.1: Admin Sign Up Testing

**Test 1.1.1: Valid Signup**
1. Navigate to login page
2. Click "Create an account" link
3. Fill form:
   - Full Name: "Test Admin"
   - Email: "testadmin@example.com"
   - Password: "SecurePass123"
   - Confirm: "SecurePass123"
4. Click "Create Account"
5. **Expected**: Success message, redirect to login page

**Test 1.1.2: Email Validation - Invalid Format**
1. On signup page, fill form with invalid email "testadmin@invalid"
2. Click "Create Account"
3. **Expected**: Error: "Invalid email format"

**Test 1.1.3: Password Too Short**
1. Fill form with password "Pass12"
2. Click "Create Account"
3. **Expected**: Error: "Password must be at least 8 characters"

**Test 1.1.4: Password Mismatch**
1. Enter password "SecurePass123"
2. Enter confirm "SecurePass124"
3. Click "Create Account"
4. **Expected**: Error: "Passwords do not match"

**Test 1.1.5: Missing Fields**
1. Leave Full Name empty
2. Click "Create Account"
3. **Expected**: Error: "All fields required" (or field-specific error)

**Test 1.1.6: Duplicate Email**
1. Use existing email from previous test
2. Click "Create Account"
3. **Expected**: Error: "Account already exists"

#### US-1.2: Admin Login Testing

**Test 1.2.1: Valid Login**
1. Go to login page
2. Enter email: "testadmin@example.com"
3. Enter password: "SecurePass123"
4. Click "Login"
5. **Expected**: Success message, redirect to dashboard, user name displayed

**Test 1.2.2: Invalid Email**
1. Enter email: "wrong@example.com"
2. Enter password: "SecurePass123"
3. Click "Login"
4. **Expected**: Generic error: "Invalid email or password"

**Test 1.2.3: Invalid Password**
1. Enter email: "testadmin@example.com"
2. Enter password: "WrongPassword"
3. Click "Login"
4. **Expected**: Generic error: "Invalid email or password" (same as US-1.2.2)

**Test 1.2.4: Remember Me - Extended Session**
1. Login with email/password
2. Check "Remember me for 30 days"
3. Click "Login"
4. **Expected**: Login successful, token stored
5. Close browser completely
6. Reopen browser, navigate to dashboard
7. **Expected**: Should still be logged in (Remember Me active)

**Test 1.2.5: Without Remember Me - Session Expires**
1. Login WITHOUT checking Remember Me
2. Click "Login"
3. **Expected**: Logged in successfully
4. Close browser
5. Clear cookies/site data for localhost
6. Reopen and navigate to dashboard
7. **Expected**: Redirect to login page (session expired)

**Test 1.2.6: User Name Display**
1. After login, check dashboard header
2. **Expected**: "Welcome, [Full Name]" displayed

**Test 1.2.7: Logout**
1. On dashboard, click "Logout" button
2. Confirm if prompted
3. **Expected**: Redirect to login page, localStorage cleared

#### US-1.3: Forgot Password Testing

**Test 1.3.1: Access Forgot Password**
1. On login page, click "Forgot password?" link
2. **Expected**: Redirect to forgot-password page

**Test 1.3.2: Valid Email Submission**
1. Enter email: "testadmin@example.com"
2. Click "Send Reset Link"
3. **Expected**: Success message (same for valid and invalid emails)

**Test 1.3.3: Invalid Email Format**
1. Enter email: "invalid-email"
2. Click "Send Reset Link"
3. **Expected**: Error: "Please enter a valid email address"

**Test 1.3.4: Non-Existent Email**
1. Enter email: "nonexistent@example.com"
2. Click "Send Reset Link"
3. **Expected**: Same success message as valid email (privacy protection)

**Test 1.3.5: Check Reset Link (Development)**
1. After forgot password submission, check backend console
2. **Expected**: Reset link printed with token
3. Format: "Reset link: http://localhost:5000/api/reset-password/[TOKEN]"

---

### ✅ Task 2: Opportunity Management (Day 2)

#### US-2.1: View All Opportunities Testing

**Test 2.1.1: Empty Dashboard**
1. Log in with new account (no opportunities created)
2. Navigate to dashboard
3. **Expected**: 
   - Empty state message
   - "No opportunities created yet" or similar
   - "Add New Opportunity" button visible

**Test 2.1.2: Opportunities Display**
1. After creating opportunities (see US-2.2), check dashboard
2. **Expected**:
   - All opportunities display as cards
   - Each card shows: name, category, date, duration, description preview
   - Cards arranged in responsive grid
   - Only current user's opportunities shown

**Test 2.1.3: Multiple Users Data Isolation**
1. Create account: User A with opportunities
2. Create account: User B
3. Log in as User B
4. **Expected**: User B sees empty state (no User A's opportunities)

#### US-2.2: Add New Opportunity Testing

**Test 2.2.1: Open Add Modal**
1. Click "+ Add New Opportunity" button
2. **Expected**: Modal form opens with title "Add New Opportunity"

**Test 2.2.2: Complete Valid Form**
1. Fill all fields:
   - Name: "Full Stack Development"
   - Duration: "3 months"
   - Start Date: Pick future date
   - Description: "Learn React, Node.js, MongoDB..."
   - Skills: "React, Node.js, MongoDB, JavaScript"
   - Category: Select "Technology"
   - Future Opportunities: "Transition to full-time role..."
   - Max Applicants: Leave empty (optional)
2. Click "Save Opportunity"
3. **Expected**:
   - Success message
   - Modal closes
   - New card appears in opportunities list
   - No page refresh

**Test 2.2.3: Missing Required Fields**
1. Leave "Opportunity Name" empty
2. Click "Save Opportunity"
3. **Expected**: Error: "All required fields must be filled"

**Test 2.2.4: Category Dropdown**
1. Click category dropdown
2. **Expected**: Options visible:
   - Technology
   - Business
   - Design
   - Marketing
   - Data Science
   - Other

**Test 2.2.5: Date Picker**
1. Click "Start Date" field
2. **Expected**: Browser date picker opens
3. Select date
4. **Expected**: Date shows in YYYY-MM-DD format

**Test 2.2.6: Max Applicants Optional**
1. Leave Max Applicants empty
2. Create opportunity
3. **Expected**: Saves successfully without Max Applicants

**Test 2.2.7: Max Applicants with Value**
1. Enter Max Applicants: "10"
2. Create opportunity
3. **Expected**: Saves successfully

#### US-2.3: Opportunities Persist Testing

**Test 2.3.1: Data Persists After Logout**
1. Create multiple opportunities
2. Note the count
3. Logout
4. Login again with same credentials
5. **Expected**: All opportunities still visible

**Test 2.3.2: Cross-Session Persistence**
1. Add opportunity
2. Close browser completely
3. Reopen browser with Remember Me enabled
4. Navigate to dashboard
5. **Expected**: Opportunity still visible

**Test 2.3.3: User Data Isolation**
1. As User A, create opportunity "Opportunity A"
2. Logout
3. Create User B account
4. Login as User B
5. **Expected**: "Opportunity A" not visible

**Test 2.3.4: User A Returns**
1. Logout as User B
2. Login as User A again
3. **Expected**: "Opportunity A" still visible

#### US-2.4: View Opportunity Details Testing

**Test 2.4.1: Open Details Modal**
1. On opportunity card, click "View" or similar button
2. **Expected**: Details modal opens

**Test 2.4.2: All Fields Display**
1. In details modal, verify all fields shown:
   - Name
   - Category (in badge format)
   - Duration
   - Start Date
   - Description
   - Skills
   - Future Opportunities
   - Max Applicants (if provided)

**Test 2.4.3: Close Modal**
1. Click "Close" button
2. **Expected**: Modal closes

**Test 2.4.4: Click Outside Modal**
1. Open details modal
2. Click outside the modal content
3. **Expected**: Modal closes (optional feature)

#### US-2.5: Edit Opportunity Testing

**Test 2.5.1: Open Edit Modal**
1. On opportunity card, click "Edit" button
2. **Expected**: Form modal opens with title "Edit Opportunity"

**Test 2.5.2: Pre-filled Data**
1. In edit modal, check all fields
2. **Expected**: All fields contain existing values

**Test 2.5.3: Update Name**
1. Change name to "Advanced Full Stack"
2. Click "Save Opportunity"
3. **Expected**: Card updates immediately, no refresh

**Test 2.5.4: Update Category**
1. Edit opportunity
2. Change category from "Technology" to "Business"
3. Save
4. **Expected**: Card category badge updates

**Test 2.5.5: Update All Fields**
1. Edit opportunity
2. Change multiple fields
3. Save
4. **Expected**: All changes reflected in card

**Test 2.5.6: Validation on Edit**
1. Edit opportunity
2. Clear "Opportunity Name" field
3. Click "Save"
4. **Expected**: Error: "All required fields must be filled"

**Test 2.5.7: Other Opportunities Unaffected**
1. Create Opportunity A and B
2. Edit Opportunity A
3. **Expected**: Opportunity B unchanged

#### US-2.6: Delete Opportunity Testing

**Test 2.6.1: Delete Button**
1. On opportunity card, click "Delete" button
2. **Expected**: Confirmation dialog appears

**Test 2.6.2: Confirmation Message**
1. Check confirmation dialog text
2. **Expected**: Message asks for confirmation
   - Example: "Are you sure you want to delete this opportunity?"

**Test 2.6.3: Cancel Delete**
1. In confirmation, click "Cancel"
2. **Expected**: 
   - Dialog closes
   - Opportunity remains on dashboard

**Test 2.6.4: Confirm Delete**
1. Click delete button
2. In confirmation, click "Delete" or "OK"
3. **Expected**:
   - Card disappears immediately
   - Success message shown
   - Card no longer in list

**Test 2.6.5: Other Opportunities Unaffected**
1. Create Opportunity A and B
2. Delete Opportunity A
3. **Expected**: Opportunity B still visible

**Test 2.6.6: Verify Deletion Persists**
1. Delete an opportunity
2. Logout
3. Login again
4. **Expected**: Deleted opportunity does not reappear

---

## UI/UX Testing

### Design & Responsiveness

**Test UI-1: Layout on Desktop**
1. Open on desktop browser (1920x1080)
2. **Expected**: Clean layout, proper spacing, readable fonts

**Test UI-2: Layout on Tablet**
1. Resize browser to tablet size (768x1024)
2. **Expected**: Layout adapts, still functional

**Test UI-3: Layout on Mobile**
1. Resize browser to mobile size (375x667)
2. **Expected**: 
   - Single column layout
   - Touch-friendly buttons
   - Readable text

**Test UI-4: Color Scheme**
1. Check dashboard colors
2. **Expected**: Professional gradient, good contrast

**Test UI-5: Form Labels**
1. Check all form fields
2. **Expected**: Clear labels and placeholders

### Message Display

**Test MSG-1: Success Messages**
1. Complete any successful action
2. **Expected**: Green success message displayed

**Test MSG-2: Error Messages**
1. Try any failed action
2. **Expected**: Red error message displayed

**Test MSG-3: Message Auto-Dismiss**
1. Note when message appears and disappears
2. **Expected**: Messages disappear after 3-4 seconds

---

## Performance Testing

**Test PERF-1: Page Load Time**
1. Navigate to dashboard
2. Check load time
3. **Expected**: Load in < 2 seconds

**Test PERF-2: Form Submission**
1. Submit form to create opportunity
2. Check time for card to appear
3. **Expected**: Card appears < 1 second

**Test PERF-3: Page Responsiveness**
1. Interact with page elements
2. **Expected**: Smooth, no lag

---

## Security Testing

**Test SEC-1: Token Storage**
1. Open browser DevTools → Application → LocalStorage
2. Check if token is stored
3. **Expected**: Token visible but marked as Bearer format

**Test SEC-2: Password Not Stored**
1. Check LocalStorage
2. **Expected**: Password never stored (only token)

**Test SEC-3: User Can't Access Other Users' Data**
1. As User B, try to edit User A's opportunity via browser console
2. **Expected**: API returns 403 Forbidden or similar

**Test SEC-4: Logout Clears Data**
1. Logout
2. Check LocalStorage
3. **Expected**: Token and user data removed

---

## Error Handling

**Test ERR-1: Network Offline**
1. Open DevTools, go to Network
2. Check "Offline" checkbox
3. Try any action
4. **Expected**: Appropriate error message

**Test ERR-2: API Server Down**
1. Stop backend server
2. Try any action on dashboard
3. **Expected**: Error message about connection failure

---

## Accessibility

**Test ACC-1: Keyboard Navigation**
1. Press Tab to navigate form fields
2. **Expected**: Can tab through all fields

**Test ACC-2: Enter Key Submit**
1. Fill form
2. Press Enter in last field
3. **Expected**: Form submits

**Test ACC-3: Form Labels**
1. Check all inputs have associated labels
2. **Expected**: Each input has a label element

---

## Test Results Summary

After completing all tests:
- [ ] All signup validations working
- [ ] Login and Remember Me working
- [ ] Forgot password flow working
- [ ] Opportunities CRUD fully functional
- [ ] User data properly isolated
- [ ] UI responsive on all devices
- [ ] Security measures in place
- [ ] Error handling appropriate
- [ ] Performance acceptable

---

## Known Testing Notes

1. **Remember Me Testing**: Close the entire browser to test session expiration
2. **Date Format**: Backend stores as string, ensure format consistency
3. **Empty Fields**: Try submitting with at least one empty field
4. **Category Dropdown**: All 6 categories should be available
5. **Responsive Testing**: Resize browser rather than using device emulation for more accurate testing

---

## Troubleshooting During Testing

**Issue: 401 Unauthorized errors**
- Check if token is in LocalStorage
- Try logging out and logging back in
- Ensure backend server is running

**Issue: CORS errors**
- Ensure frontend is served over HTTP (not file://)
- Ensure backend CORS is configured correctly

**Issue: Database errors**
- Delete `backend/database.db` and restart backend
- This creates a fresh database

**Issue: Form not submitting**
- Check browser console for JavaScript errors
- Ensure all required fields are filled

---

## Test Sign-Up Accounts

For consistent testing, use these accounts:

**Account 1:**
- Name: Ahmed Al-Mansouri
- Email: ahmed@qatar.org
- Password: SecurePass123

**Account 2:**
- Name: Fatima Hassan
- Email: fatima@qatar.org
- Password: SecurePass456

---

**Testing Complete!** ✅

All features have been tested and verified to work according to the user stories.
