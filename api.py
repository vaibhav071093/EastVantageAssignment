from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from geopy.distance import geodesic

from database import SessionLocal
from models import AddressCreate, Address, DBAddress
from crud import create_address, get_address, get_addresses_within_distance, update_address, delete_address

router = APIRouter()


@router.post("/addresses/", response_model=Address)
def create_new_address(address: AddressCreate, db: Session = Depends(SessionLocal)):
    return create_address(db, address)


@router.put("/addresses/{address_id}", response_model=Address)
def update_existing_address(address_id: int, updated_address: AddressCreate, db: Session = Depends(SessionLocal)):
    db_address = update_address(db, address_id, updated_address)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


@router.delete("/addresses/{address_id}")
def delete_existing_address(address_id: int, db: Session = Depends(SessionLocal)):
    if not delete_address(db, address_id):
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Address deleted successfully"}


@router.get("/addresses/{address_id}", response_model=Address)
def read_address(address_id: int, db: Session = Depends(SessionLocal)):
    address = get_address(db, address_id)
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@router.get("/addresses/")
def read_addresses_within_distance(latitude: float, longitude: float, distance: float, db: Session = Depends(SessionLocal)):
    addresses = get_addresses_within_distance(db, latitude, longitude, distance)
    return addresses
