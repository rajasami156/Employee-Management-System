import psycopg2
import tkinter as tk
from tkinter import PhotoImage

# Function to verify credentials
def verify_credentials():
    # Get the input values
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            dbname='employees',
            user='postgres',
            password='Samiullah17+',
            host='localhost',
            port=5432
        )

        # Create a cursor
        cursor = conn.cursor()

        # Execute a SQL query to check if the username and password are correct
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()

        if result:
            result_label.config(text="Authentication successful")
            # Enable additional functionality after successful authentication
            view_profile_button.config(state=tk.NORMAL)
            view_salary_button.config(state=tk.NORMAL)
        else:
            result_label.config(text="Authentication failed")

    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)
        result_label.config(text="Database connection error")

    finally:
        # Close the cursor and the database connection
        if conn:
            cursor.close()
            conn.close()

# Function to view employee profile
img1 = None
def view_profile():
    global img1  # Use the global img1

# Create a new window for displaying salary information
    employee_window = tk.Toplevel(root)
    employee_window.title("Employee Information")
    employee_window.geometry("800x600")  # Set the size of the new window

# Load the employee profile image
    img1 = PhotoImage(file='C:/Users/pc/Desktop/Python_Final_Project/employee_profile.png')

# Create a label to display the image in the profile_window
    background_label = tk.Label(employee_window, image=img1, bg='white')
    background_label.place(x=50, y=50)

# Example label for displaying employee information
    salary_label = tk.Label(employee_window, text="Employee Information of SAMIULLAH", font=('Arial', 15))
    salary_label.pack(pady=20)



    View_leaves_button = tk.Button(employee_window, text="View Leaves", command= View_leaves)
    View_leaves_button.pack()

# Function for the additional button on the employee profile page
img2= None
def View_leaves():
    global img2
    leaves_window = tk.Toplevel(root)
    leaves_window.title("Employee Information")
    leaves_window.geometry("800x400")
    img2 = PhotoImage(file='C:/Users/pc/Desktop/Python_Final_Project/leaves.PNG')

    img2 = img2.subsample(1, 1)  # Adjust the factors to achieve the desired aspect ratio
    background_label = tk.Label(leaves_window, image=img2, bg='white')
    background_label.place(x=50, y=50)

    leaves_label = tk.Label(leaves_window, text="Remaining Leaves for SAMIULLAH", font=('Arial', 15))
    leaves_label.pack(pady=20)


img0 = None

# Function to view salary information
def view_salary():
    global img0  # Use the global img0

    # Create a new window for displaying salary information
    salary_window = tk.Toplevel(root)
    salary_window.title("Salary Information")
    salary_window.geometry("800x600")  # Set the size of the new window

    # Load the salary image
    img0 = PhotoImage(file='C:/Users/pc/Desktop/Python_Final_Project/salaryslip.PNG')

    # Create a label to display the image in the salary_window
    background_label = tk.Label(salary_window, image=img0, bg='white')
    background_label.place(x=50, y=50)

    # Example label for displaying salary information
    salary_label = tk.Label(salary_window, text="Salary Information for SAMIULLAH", font=('Arial', 15))
    salary_label.pack(pady=20)


# Create the main window
root = tk.Tk()
root.title("EMPLOYEE MANAGEMENT SYSTEM")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

# Load the background image
img = PhotoImage(file='C:/Users/pc/Desktop/Python_Final_Project/login.png')

# Create a label to display the image
background_label = tk.Label(root, image=img, bg='white')
background_label.place(x=50, y=50)

# Create and place widgets
frame = tk.Frame(root, width=300, height=300, bg='white')
frame.place(x=480, y=70)

heading = tk.Label(frame, text='Sign In', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI light', 23, 'bold'))
heading.place(x=100, y=5)

# Adjust the coordinates for username and password widgets
username_label = tk.Label(frame, width=25, text="Username:", fg='black', bg='white', font=('Microsoft YaHei UI light', 11, 'bold'))
username_label.place(x=30, y=60)

username_entry = tk.Entry(frame, width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI light', 11, 'bold'))
username_entry.place(x=30, y=90)

password_label = tk.Label(frame, text="Password:", fg='black', bg='white', font=('Microsoft YaHei UI light', 11, 'bold'))
password_label.place(x=30, y=120)

password_entry = tk.Entry(frame, show="*", width=25, fg='black', border=1, bg='white', font=('Microsoft YaHei UI light', 11, 'bold'))
password_entry.place(x=30, y=150)

login_button = tk.Button(frame, text="Login", command=verify_credentials)
login_button.place(x=30, y=180)

result_label = tk.Label(root, text="", bg='white')
result_label.place(x=350, y=340)


# Button to view profile information

view_profile_button = tk.Button(root, text="View Employee Profile", command=view_profile, state=tk.DISABLED)
view_profile_button.place(x=50, y=400)

# Button to view salary information
view_salary_button = tk.Button(root, text="View Salary Information", command=view_salary, state=tk.DISABLED)
view_salary_button.place(x=250, y=400)





# Start the main loop
root.mainloop()
