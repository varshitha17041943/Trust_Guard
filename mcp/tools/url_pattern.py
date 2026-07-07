from config import settings

def execute(args: dict) -> dict:
    url = args.get("url")
    if not url and "url_pattern" != "pdf_generator":
        raise ValueError("URL is required")

    # Deterministic mock fallback
    return {"status": "mock_success", "tool": "url_pattern", "target": args.get("url")}
