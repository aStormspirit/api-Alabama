from pydantic import BaseModel
from enum import Enum
from typing import List, Optional

class StateEnum(str, Enum):
    Nevada = 'NV'
    Kansas = 'KS'
    Wyoming = 'WY'
    Florida = 'FL' 

class Address(BaseModel):
    street: str
    extra: str
    city: str
    state: str
    zipCode: str

class Company(BaseModel):
    name: str
    designator: str
    address: Address

class Contact(BaseModel):
    firstName: str
    lastName: str
    email: str
    mobile: str

class Member(BaseModel):
    isIndividual: bool
    firstName: str
    lastName: str
    companyName: str
    percentOfOwnership: int
    address: Address

class Agent(BaseModel):
    isIndividual: bool
    firstName: str
    lastName: str
    companyName: str
    address: Address

class Data(BaseModel):
    entityType: str
    entityState: str
    activityType: str
    company: Company
    contact: Contact
    members: List[Member]
    agent: Agent

class Credentials(BaseModel):
    login: str
    password: str

class RootModel(BaseModel):
    credentials: Credentials
    state: StateEnum
    data: Data
    class Config:
        use_enum_values = True