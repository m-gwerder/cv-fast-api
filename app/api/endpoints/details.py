from fastapi import APIRouter
from app.mockup.details import details

router = APIRouter()

@router.get("/")
async def get_details():
    return details

@router.get("/contact/")
async def get_details():
    return details["contact"]

@router.get("/address/")
async def get_details():
    return details["address"]

@router.get("/dob/")
async def get_details():
    return details["dob"]

@router.get("/maritial_status/")
async def get_details():
    return details["maritial_status"]

@router.get("/languages/")
async def get_details():
    return details["languages"]

@router.get("/about/")
async def get_details():
    return details["about"]