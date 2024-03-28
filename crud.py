from sqlalchemy.orm import Session
from models import AddressCreate, Address, DBAddress


def create_address(db: Session, address: AddressCreate):
    db_address = DBAddress(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def get_address(db: Session, address_id: int):
    return db.query(DBAddress).filter(DBAddress.id == address_id).first()


def get_addresses_within_distance(db: Session, latitude: float, longitude: float, distance: float):
    addresses = db.query(DBAddress).all()
    valid_addresses = []
    for address in addresses:
        coord_a = (latitude, longitude)
        coord_b = (address.latitude, address.longitude)
        if geodesic(coord_a, coord_b).kilometers <= distance:
            valid_addresses.append(address)
    return valid_addresses


def update_address(db: Session, address_id: int, updated_address: AddressCreate):
    db_address = db.query(DBAddress).filter(DBAddress.id == address_id).first()
    if db_address:
        for attr, value in updated_address.dict().items():
            setattr(db_address, attr, value)
        db.commit()
        db.refresh(db_address)
        return db_address
    else:
        return None


def delete_address(db: Session, address_id: int):
    db_address = db.query(DBAddress).filter(DBAddress.id == address_id).first()
    if db_address:
        db.delete(db_address)
        db.commit()
        return True
    else:
        return False
