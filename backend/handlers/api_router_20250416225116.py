from fastapi import APIRouter
from .upload import router as upload_router
from .export import router as export_router

router = APIRouter()
router.include_router(upload_router, prefix="/upload", tags=["Upload"])
router.include_router(export_router, prefix="/export", tags=["Export"])
