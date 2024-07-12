import os
import sqlite3
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
upload_directory = 'C:/Users/prash/OneDrive/Desktop/assign/python/upload'  # Replace with your directory path
database_file = 'files.db'  # SQLite database file name

# Function to initialize database and table if not exists
def initialize_database():
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uploaded_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            content TEXT NOT NULL,
            upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Function to handle file events
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        filepath = event.src_path
        filename = os.path.basename(filepath)
        
        # Read file content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Upload content to database
        upload_to_database(filename, content)

# Function to upload file content to database
def upload_to_database(filename, content):
    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO uploaded_files (filename, content) VALUES (?, ?)
        ''', (filename, content))
        conn.commit()
        print(f"Uploaded '{filename}' to database.")
    except sqlite3.Error as e:
        print(f"Error uploading '{filename}' to database: {e}")
    finally:
        if conn:
            conn.close()

# Main function to start file monitoring
def main():
    initialize_database()
    
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, upload_directory, recursive=False)
    observer.start()
    print(f"File listener started, monitoring directory '{upload_directory}'...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
