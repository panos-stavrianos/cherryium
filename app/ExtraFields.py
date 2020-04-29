import enum
from typing import Union, Callable

from markupsafe import escape
from wtforms import SelectField


class EnumField(SelectField):
    def coerce(enum_type: enum.Enum) -> Callable[[Union[enum.Enum, str]], enum.Enum]:
        def coerce(name: Union[enum.Enum, str]) -> enum.Enum:
            if isinstance(name, enum_type):
                return name
            try:
                return enum_type[name]
            except KeyError:
                raise ValueError(name)

        return coerce

    def __init__(self, enum_type: enum.Enum, *args, **kwargs):
        def attach_functions(enum_type: enum.Enum) -> enum.Enum:
            enum_type.__str__ = lambda self: self.name
            enum_type.__html__ = lambda self: self.name
            return enum_type

        _enum_type = attach_functions(enum_type)
        super().__init__(_enum_type.__name__,
                         choices=[(v, escape(v)) for v in _enum_type],
                         coerce=EnumField.coerce(_enum_type), *args, **kwargs)
