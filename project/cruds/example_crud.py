from project.utils.translation_utils import translate
from project.models.crud_models import (
    Crud,
    CrudForm,
    TextField,
    TextareaField,
    NumericField,
    DateField,
    DatetimeField,
    SelectField
)


class ExampleCrud(Crud):

    def __init__(self) -> None:
        super().__init__('example')

    def build_form(self, update: bool = False) -> CrudForm:
        return CrudForm() \
            .with_field(TextField(
                name='f1',
                label=translate('cruds.example.f1.label'),
                required=True,
                placeholder=translate('cruds.example.f1.placeholder'),
                disabled=update,
                css_class='blue-text'
            )) \
            .with_field(NumericField(
                name='f2',
                label=translate('cruds.example.f2.label'),
                required=False,
                placeholder=translate('cruds.example.f2.placeholder'),
                min_value=0,
                step_value=1,
                max_value=100
            )) \
            .with_field(TextareaField(
                name='f3',
                label=translate('cruds.example.f3.label'),
                required=False,
                placeholder=translate('cruds.example.f3.placeholder'),
            )) \
            .with_field(DateField(
                name='f4',
                label=translate('cruds.example.f4.label'),
                required=False,
            )) \
            .with_field(DatetimeField(
                name='f5',
                label=translate('cruds.example.f5.label'),
                required=False,
            )) \
            .with_field(SelectField(
                name='f6',
                label=translate('cruds.example.f6.label'),
                required=False,
                options={
                    1: 'Yes',
                    2: 'No'
                }
            ))

    def build_list(self):
        pass
