from pydantic import BaseModel
from typing import List, Optional

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

class RootModel(BaseModel):
    State: str
    data: Data