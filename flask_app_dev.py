from app.engine import create_app


app = create_app(__name__, './envs/dev.env')
print(f'Running in {app.env} environment!')
app.run(debug=True)
