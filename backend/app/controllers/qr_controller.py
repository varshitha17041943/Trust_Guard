from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.exceptions.custom import DomainException
from app.models.scan import Scan
import re
import mimetypes

router = APIRouter()

MAX_FILE_SIZE = 5 * 1024 * 1024 # 5 MB
ALLOWED_MIMES = ['image/jpeg', 'image/png', 'image/webp']

@router.post("/api/scan/qr")
async def scan_qr(
    extracted_url: str = Form(...),
    file: UploadFile = File(None),
    db: AsyncSession = Depends(get_db)
):
    # 1. Validate File if provided
    if file:
        if file.content_type not in ALLOWED_MIMES:
            raise DomainException("Invalid file type. Only JPEG, PNG, and WebP are allowed.", 400)
        # Read to check size (in memory for now)
        content = await file.read()
        if len(content) > MAX_FILE_SIZE:
            raise DomainException("File exceeds 5MB limit.", 400)
            
    # 2. Sanitize and Validate URL
    if not extracted_url:
        raise DomainException("Extracted URL is empty", 400)
        
    # Reject bad protocols strictly
    bad_protocols = ['javascript:', 'data:', 'ftp:', 'file:', 'vbscript:']
    lower_url = extracted_url.lower()
    for bad in bad_protocols:
        if lower_url.startswith(bad):
            raise DomainException(f"Unsafe protocol detected: {bad}", 403)
            
    if not lower_url.startswith('http://') and not lower_url.startswith('https://'):
        raise DomainException("Invalid protocol. Only HTTP and HTTPS are supported.", 400)
        
    # 3. Store in History (Mock logic for now, real logic connects to DB)
    scan = Scan(target=extracted_url, scan_type="QR", status="pending")
    db.add(scan)
    await db.commit()
    await db.refresh(scan)
    
    return {
        "scan_id": scan.id,
        "target": extracted_url,
        "status": "success",
        "message": "QR Code validated and analysis started."
    }
