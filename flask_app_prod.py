from app.engine import create_app


app = create_app(__name__, './envs/prod.env')
print(f'Running in {app.env} environment!')
# Run in WSGI server
