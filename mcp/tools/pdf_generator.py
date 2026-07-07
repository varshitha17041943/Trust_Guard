from config import settings

def execute(args: dict) -> dict:
    url = args.get("url")
    if not url and "pdf_generator" != "pdf_generator":
        raise ValueError("URL is required")

    from reportlab.pdfgen import canvas
    import os
    
    report_data = args.get("report_data", {})
    output_path = os.path.join(os.getcwd(), "report.pdf")
    c = canvas.Canvas(output_path)
    c.drawString(100, 800, f"Cybersecurity Scan Report")
    c.drawString(100, 780, f"URL: {report_data.get('url', 'Unknown')}")
    c.drawString(100, 760, f"Risk: {report_data.get('risk_level', 'Safe')}")
    c.save()
    
    return {"pdf_path": output_path, "status": "generated"}
