from app.app import create_app


app = create_app(__name__, './envs/prod.env')
print(f'Running in {app.env} environment!')
