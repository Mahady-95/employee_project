## Git Actions CI with CRUD
- Runs Django tests on every push & PR
- Uses MySQL service for production parity
- Enforces minimum 70% test coverage
## Daily Work flow

📝 Docker + Django + MySQL Daily Cheat Sheet

1️⃣ Start / Stop Docker
  docker-compose up -d        # Start containers
  docker ps                   # Check running containers
  docker-compose down         # Stop all containers
  docker-compose stop web     # Stop only web
  docker-compose start web    # Start only web

2️⃣ Access Django container
  docker-compose exec web bash   # Enter container shell (/app)

3️⃣ Database workflow
  python manage.py makemigrations   # Create migration files
  python manage.py migrate          # Apply migrations
  python manage.py dbshell          # Access DB shell
  python manage.py createsuperuser  # Create admin user

4️⃣ Run Django server
  python manage.py runserver 0.0.0.0:8000
  Browser: http://localhost:8000/ | Admin: /admin/

5️⃣ Static / Media (optional)
  python manage.py collectstatic

6️⃣ Git workflow
  git status
  git checkout -b feature/<name>
  git add .
  git commit -m "Message"
  git push origin feature/<name>

7️⃣ Logs / Debug
  docker-compose logs -f           # All logs
  docker-compose logs -f web       # Web logs only
  docker-compose logs -f db        # DB logs only

8️⃣ Reset DB (if needed)
  docker-compose down -v
  docker-compose up --build -d

💡 Daily Flow:
  1. up -d → 2. exec web → 3. makemigrations → 4. migrate → 5. runserver → 6. test/code/git → 7. down
