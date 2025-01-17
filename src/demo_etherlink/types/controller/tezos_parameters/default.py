# generated by datamodel-codegen:
#   filename:  default.json

from __future__ import annotations

from pydantic import BaseModel
from pydantic import Extra


class DefaultParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    dictator_signature: str
    payload_hash: str
    target: str
