# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .sandbox_input import SandboxInput
from .sandbox_metric_input_params import SandboxMetricInputParams


class SandboxScenario(pydantic.BaseModel):
    label: typing.Optional[str]
    inputs: typing.List[SandboxInput] = pydantic.Field(description=("The inputs for the scenario\n"))
    metric_input_params: typing.Optional[SandboxMetricInputParams]
    id: str = pydantic.Field(description=("The id of the scenario\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
