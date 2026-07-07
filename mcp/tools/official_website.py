from config import settings

def execute(args: dict) -> dict:
    url = args.get("url")
    if not url and "official_website" != "pdf_generator":
        raise ValueError("URL is required")

    # Deterministic mock fallback
    return {"status": "mock_success", "tool": "official_website", "target": args.get("url")}
