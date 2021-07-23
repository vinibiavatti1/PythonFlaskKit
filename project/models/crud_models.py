from abc import ABC, abstractmethod
from copy import copy


###############################################################################
# Form
###############################################################################


class CrudForm:
    """
    Dynamic form data structure
    """
    def __init__(self):
        self.fields = []

    def with_field(self, field):
        self.fields.append(field)
        return self

    def add_field(self, field):
        self.fields.append(field)

    def set_fields(self, fields):
        self.fields = fields

    def build(self):
        fields = []
        input_types = []
        for field in self.fields:
            field_data = copy(field.__dict__)
            input_type = field_data.pop('input_type')
            input_types.append(input_type)
            fields.append(field_data)
        return dict(
            fields=fields,
            input_types=input_types
        )


###############################################################################
# Form fields
###############################################################################


class Field(ABC):
    """
    Base class for form inputs
    """
    def __init__(self, *, name, input_type, label, placeholder='',
                 required=True, css_class='', disabled=False, default=''):
        self.name = name
        self.input_type = input_type
        self.label = label
        self.placeholder = placeholder
        self.required = required
        self.css_class = css_class
        self.disabled = disabled
        self.default = default


class TextField(Field):
    """
    Text input class
    """
    def __init__(self, *, name, label, placeholder='', required=True,
                 css_class='', disabled=False, default=''):
        super().__init__(
            name=name,
            input_type='text',
            label=label,
            placeholder=placeholder,
            required=required,
            css_class=css_class,
            disabled=disabled,
            default=default
        )


class NumericField(Field):
    """
    Numeric input class
    """
    def __init__(self, *, name, label, placeholder='', required=True,
                 css_class='', disabled=False, default='', min_value=0,
                 max_value=100, step_value=1):
        super().__init__(
            name=name,
            input_type='numeric',
            label=label,
            placeholder=placeholder,
            required=required,
            css_class=css_class,
            disabled=disabled,
            default=default
        )
        self.min_value = min_value
        self.max_value = max_value
        self.step_value = step_value


class TextareaField(Field):
    """
    Textarea input class
    """
    def __init__(self, *, name, label, placeholder='', required=True,
                 css_class='', disabled=False, default=''):
        super().__init__(
            name=name,
            input_type='textarea',
            label=label,
            placeholder=placeholder,
            required=required,
            css_class=css_class,
            disabled=disabled,
            default=default
        )


class DateField(Field):
    """
    Date input class
    """
    def __init__(self, *, name, label, placeholder='', required=True,
                 css_class='', disabled=False, default=''):
        super().__init__(
            name=name,
            input_type='date',
            label=label,
            placeholder=placeholder,
            required=required,
            css_class=css_class,
            disabled=disabled,
            default=default
        )


class DatetimeField(Field):
    """
    Datetime input class
    """
    def __init__(self, *, name, label, placeholder='', required=True,
                 css_class='', disabled=False, default=''):
        super().__init__(
            name=name,
            input_type='datetime',
            label=label,
            placeholder=placeholder,
            required=required,
            css_class=css_class,
            disabled=disabled,
            default=default
        )


class SelectField(Field):
    """
    Select input class
    """
    def __init__(self, *, name, label, placeholder='', required=True,
                 css_class='', disabled=False, default='', options={}):
        super().__init__(
            name=name,
            input_type='select',
            label=label,
            placeholder=placeholder,
            required=required,
            css_class=css_class,
            disabled=disabled,
            default=default,
        )
        self.options = options


###############################################################################
# Crud
###############################################################################


class Crud(ABC):
    """
    Crud definition ABC class to be registered in application and render
    dynamic cruds
    """

    def __init__(self, db_table: str) -> None:
        self.db_table = db_table

    @abstractmethod
    def build_form(self, update: bool = False) -> CrudForm:
        pass

    @abstractmethod
    def build_list(self):
        pass
