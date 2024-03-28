from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from database import Base


class AddressBase(BaseModel):
    street: str
    city: str
    latitude: float
    longitude: float


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True


# SQLAlchemy model
class DBAddress(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, index=True)
    city = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
