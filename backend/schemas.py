from pydantic import BaseModel

class DeviceCreate(BaseModel):
    device_name: str
    serial_number: str
    model: str