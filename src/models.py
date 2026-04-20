class Course:
    def __init__(self, title, description, instructor, duration, topics=None):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.topics = topics or []

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"

class Video:
    def __init__(self, title, description, video_id):
        self.title = title
        self.description = description
        self.video_id = video_id

videos = [
    Video("Python for Beginners - Full Course", "Learn Python programming from scratch in this comprehensive tutorial.", "rfscVS0vtbw"),
    Video("Flask Web Development Tutorial", "Build a complete web application with Flask, covering routing, templates, and more.", "Z1RJmh_OqeA"),
    Video("Data Science Full Course", "Master data science fundamentals including NumPy, Pandas, and Matplotlib.", "ua-CiDNNj30"),
    Video("Git & GitHub Crash Course", "Learn the essentials of version control with Git and GitHub.", "RGOj5yH7evk"),
]

contact_info = {
    "org_name": "CodeLearn Academy",
    "email": "hello@codelearnacademy.com",
    "address": "123 Dev Street, San Francisco, CA 94105",
    "socials": [
        {"platform": "Twitter", "handle": "@codelearnacademy", "url": "https://twitter.com/codelearnacademy"},
        {"platform": "GitHub", "handle": "github.com/codelearnacademy", "url": "https://github.com/codelearnacademy"},
        {"platform": "LinkedIn", "handle": "linkedin.com/company/codelearnacademy", "url": "https://linkedin.com/company/codelearnacademy"},
    ]
}

courses = [
    Course("Introduction to Python", "Learn the basics of Python programming.", "John Doe", "4 weeks",
           topics=["Variables and Data Types", "Control Flow", "Functions", "Modules"]),
    Course("Web Development with Flask", "Build web applications using Flask.", "Jane Smith", "6 weeks",
           topics=["Routing", "Templates", "Forms", "Databases"]),
    Course("Data Science Fundamentals", "An introduction to data science concepts and tools.", "Alice Johnson", "8 weeks",
           topics=["NumPy", "Pandas", "Matplotlib", "Machine Learning Basics"]),
    Course("Go Programming Language", "Learn Go from the ground up, covering concurrency and web services.", "Bob Lee", "5 weeks",
           topics=["Syntax and Types", "Goroutines", "Channels", "HTTP Services"]),
]