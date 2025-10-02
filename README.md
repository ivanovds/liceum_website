# Liceum  website
Simple social network Django website

### Contributors:
- ivanovds: Daniil Ivanov
- kiriatop: Kyryl Okhrimenko
- Sacvartello: Heorhii Dvorskyi
- WreckedHustle: Illia Kolesnikov
- W1ngr1l: Harazha Makar
- Roxy2010: Roksana Kazarova

### Project setup:

- **Install required software:** Python 3, pip, git, Postgresql
- Python: https://www.python.org/downloads/
- Pip: https://pip.pypa.io/en/stable/installation/
- Git: https://git-scm.com/downloads
- Postgresql: https://www.postgresql.org/download/

- **Clone the repository**
   ```bash
   git clone <repository-url>
   cd liceum_website
   ```

- **Create and activate virtual environment**
   ```bash
   python -m virtualenv .venv
   
   # On Windows:
   .venv\Scripts\activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

- **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

- **Configure environment variables**
   ```bash
   # Copy the example environment file
   cp .env.local.example .env
   
   # Edit .env file and add your configuration
   # If you do not wanna install and use Postgresql, simply change the DATABASE_URL to sqlite database:
   DATABASE_URL=sqlite:///db.sqlite3
   ```

- **Run database migrations**
   ```bash
   python manage.py migrate
   ```

- **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

- **Run the development server**
   ```bash
   python manage.py runserver
   ```

- **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`