from config import settings

def execute(args: dict) -> dict:
    url = args.get("url")
    if not url and "brand_similarity" != "pdf_generator":
        raise ValueError("URL is required")

    # Deterministic mock fallback
    return {"status": "mock_success", "tool": "brand_similarity", "target": args.get("url")}
