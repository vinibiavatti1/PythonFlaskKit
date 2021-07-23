from project.models.crud_models import Crud
from project.cruds.example_crud import ExampleCrud


# Register cruds
records: dict[Crud] = {
    'example': ExampleCrud()
}
