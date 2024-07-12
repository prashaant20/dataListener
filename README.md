# DataListener:

# Overview:

This Python script monitors a specified folder (`upload_directory`) for new file creations using the `watchdog` library. When a new file is detected, it reads the file's name and content, then stores this information in an SQLite database (`files.db`). The database table (`uploaded_files`) records each file's metadata including filename, content, and upload time. Users can easily set up and run the script to automate the storage of file uploads into a structured database format.

# File Upload Monitoring and Database Storage:

This Python script monitors a specified directory for newly created files and stores their filenames and contents into an SQLite database.

# Requirements:

1. Python 3.x  
2. watchdog library (pip install watchdog)  
   
# Dependencies:

1. os (Standard library for interacting with the operating system)  
2. sqlite3 (Standard library for SQLite database operations)  
3. time (Standard library for time-related functions)  
4. watchdog (Third-party library for monitoring filesystem events)  
   
# Problem Faced:

The main challenge encountered was handling file creation events and efficiently storing file contents into a database. Additionally, ensuring robust error handling to manage database operations safely was crucial.

# Working Model:

# Functionality:

1. Initialization: The script initializes an SQLite database (files.db) and creates a table (uploaded_files) if it doesn't already exist. The table stores metadata about uploaded files, including id (auto-        
   incrementing primary key), filename, content, and upload_time (timestamp of insertion).
2. File Event Handling: It uses the watchdog library to monitor a specified upload_directory for file creation events. When a new file is created, its filename and content are extracted.
3. Database Interaction: The extracted filename and content are then inserted into the uploaded_files table of the SQLite database using SQL INSERT statements.
4. Execution: The script runs indefinitely, continuously monitoring the directory for new file creations. It pauses for 1 second between checks (time.sleep(1)) to minimize resource consumption.
