"""
Simple script to start the Streamlit app
Run this file: python start_app.py
"""

import subprocess
import sys
import os

def main():
    print("=" * 60)
    print("Course Recommendation System")
    print("=" * 60)
    print("\nStarting Streamlit app...")
    print("The app will open in your browser automatically.")
    print("If it doesn't, go to: http://localhost:8501")
    print("\nPress Ctrl+C to stop the server\n")
    
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Try to run streamlit
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n\nServer stopped by user.")
    except FileNotFoundError:
        print("\nError: Streamlit not found!")
        print("Please install dependencies: pip install -r requirements.txt")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTrying alternative method...")
        # Try with 'streamlit' command directly
        try:
            subprocess.run(["streamlit", "run", "app.py"], check=True)
        except:
            print("Please install streamlit: pip install streamlit")

if __name__ == "__main__":
    main()

