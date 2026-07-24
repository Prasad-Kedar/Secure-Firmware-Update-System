from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database.db import SessionLocal
from models.models import Device

router = APIRouter(
    prefix="/devices",
    tags=["Device Management"]
)


class DeviceRegisterRequest(BaseModel):
    device_name: str
    serial_number: str
    model: str
    firmware_version: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register_device(
    request: DeviceRegisterRequest,
    db: Session = Depends(get_db)
):
    # Check duplicate serial number
    existing_device = (
        db.query(Device)
        .filter(Device.serial_number == request.serial_number)
        .first()
    )

    if existing_device:
        raise HTTPException(
            status_code=400,
            detail="Device with this serial number already exists"
        )

    # Create new device
    new_device = Device(
        device_name=request.device_name,
        serial_number=request.serial_number,
        model=request.model,
        firmware_version=request.firmware_version,
        assigned_firmware=None,
        status="Pending"
    )

    db.add(new_device)
    db.commit()
    db.refresh(new_device)

    return {
        "message": "Device registered successfully",
        "device_id": new_device.id,
        "device_name": new_device.device_name,
        "serial_number": new_device.serial_number,
        "model": new_device.model,
        "firmware_version": new_device.firmware_version,
        "status": new_device.status
    }