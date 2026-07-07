from config import settings

def execute(args: dict) -> dict:
    url = args.get("url")
    if not url and "dns_lookup" != "pdf_generator":
        raise ValueError("URL is required")

    # Deterministic mock fallback
    return {"status": "mock_success", "tool": "dns_lookup", "target": args.get("url")}
