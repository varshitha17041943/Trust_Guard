from fpdf import FPDF
from app.models.scan import Scan
import json
import tempfile
import os

class ReportService:
    @staticmethod
    def generate_json(scan: Scan) -> dict:
        return {
            "id": scan.id,
            "target": scan.target,
            "scan_type": scan.scan_type,
            "risk_score": scan.risk_score,
            "risk_level": scan.risk_level,
            "confidence_score": scan.confidence_score,
            "threat_intel": [t.description for t in scan.threat_results],
            "recommendations": [r.text for r in scan.recommendations],
            "official_url": scan.official_websites[0].official_url if scan.official_websites else None,
            "created_at": str(scan.created_at)
        }

    @staticmethod
    def generate_markdown(scan: Scan) -> str:
        data = ReportService.generate_json(scan)
        md = f"# TrustGuardAI Security Report\n\n"
        md += f"**Target:** {data['target']} ({data['scan_type']})\n"
        md += f"**Risk Score:** {data['risk_score']}/100 | **Risk Level:** {data['risk_level']}\n\n"
        
        md += f"## Threat Intel Findings\n"
        for flag in data['threat_intel']:
            md += f"- {flag}\n"
            
        md += f"\n## Recommendations\n"
        for rec in data['recommendations']:
            md += f"- {rec}\n"
            
        if data['official_url']:
            md += f"\n**Official Website:** {data['official_url']}\n"
            
        return md

    @staticmethod
    def generate_pdf(scan: Scan) -> str:
        data = ReportService.generate_json(scan)
        pdf = FPDF()
        pdf.add_page()
        
        # 1. Header
        pdf.set_font("helvetica", 'B', 24)
        pdf.cell(0, 15, "TrustGuardAI Security Report", ln=True, align="C")
        pdf.set_font("helvetica", '', 12)
        pdf.cell(0, 10, f"Scan Date: {data['created_at']}", ln=True, align="C")
        pdf.ln(10)
        
        # 2. Core Details
        pdf.set_font("helvetica", 'B', 14)
        pdf.set_text_color(59, 130, 246) # Blue header
        pdf.cell(0, 10, "Overview", ln=True)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("helvetica", '', 12)
        pdf.cell(0, 8, f"Target: {data['target']} ({data['scan_type']})", ln=True)
        
        # Risk Scoring with Color
        pdf.set_font("helvetica", 'B', 12)
        if data['risk_level'] == "Critical":
            pdf.set_text_color(220, 53, 69) # Red
        elif data['risk_level'] == "High":
            pdf.set_text_color(255, 152, 0) # Orange
        else:
            pdf.set_text_color(40, 167, 69) # Green
        pdf.cell(0, 8, f"Risk Score: {data['risk_score']} / 100 ({data['risk_level']})", ln=True)
        pdf.set_text_color(0, 0, 0)
        pdf.ln(5)
        
        # 3. Generate Pie Chart with Matplotlib
        import matplotlib.pyplot as plt
        import uuid
        
        score = data['risk_score']
        safe_margin = max(0, 100 - score)
        
        fig, ax = plt.subplots(figsize=(4, 4))
        colors = ['#ef4444', '#22c55e'] if score > 50 else ['#f97316', '#22c55e'] if score > 20 else ['#22c55e', '#e5e7eb']
        ax.pie([score, safe_margin], labels=['Risk', 'Safe'], colors=colors, autopct='%1.1f%%', startangle=90, textprops={'color':"black", 'weight':'bold'})
        ax.axis('equal') 
        fig.patch.set_facecolor('white') 
        
        chart_path = tempfile.mktemp(suffix=".png")
        plt.savefig(chart_path, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
        plt.close(fig)
        
        # Embed Pie Chart cleanly
        pdf.image(chart_path, x=130, y=pdf.get_y() - 25, w=50)
        pdf.ln(25)
        
        # 4. Findings
        pdf.set_font("helvetica", 'B', 14)
        pdf.set_text_color(59, 130, 246)
        pdf.cell(0, 10, "Technical Findings", ln=True)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("helvetica", '', 12)
        if not data['threat_intel']:
            pdf.cell(0, 8, "- No critical threats detected.", ln=True)
        for flag in data['threat_intel']:
            pdf.cell(0, 8, f"- {flag}", ln=True)
        pdf.ln(5)
        
        # 5. Recommendations
        pdf.set_font("helvetica", 'B', 14)
        pdf.set_text_color(59, 130, 246)
        pdf.cell(0, 10, "AI Recommendations", ln=True)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("helvetica", '', 12)
        if not data['recommendations']:
            pdf.cell(0, 8, "- Proceed with standard caution.", ln=True)
        for rec in data['recommendations']:
            pdf.cell(0, 8, f"- {rec}", ln=True)
            
        if data['official_url']:
            pdf.ln(5)
            pdf.set_font("helvetica", 'B', 12)
            pdf.cell(0, 10, f"Verified Official Website: {data['official_url']}", ln=True)
            
        # Clean up chart
        try:
            os.remove(chart_path)
        except:
            pass
        
        # Save to temp file
        tmp_path = tempfile.mktemp(suffix=".pdf")
        pdf.output(tmp_path)
        return tmp_path
