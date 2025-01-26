import sys
import os
from dotenv import load_dotenv

# Add your project directory to Python path
path = '/home/Issaerium/abdize'
if path not in sys.path:
    sys.path.append(path)

# Load environment variables
load_dotenv(os.path.join(path, '.env'))

# Import your Flask app
from app import app as application

# No changes required if this file is not used by PythonAnywhere.
