import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def export_sar_csv(account, mule_info, path):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Account", "MuleScore", "Scenarios", "GeneratedAt"])
        writer.writerow([
            account,
            mule_info["mule_score"],
            ",".join(mule_info["scenarios"]),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])


def export_sar_pdf(account, mule_info, path):
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Suspicious Activity Report (SAR)")

    y -= 40
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Account: {account}")
    y -= 20
    c.drawString(50, y, f"Mule Score: {mule_info['mule_score']}")
    y -= 20
    c.drawString(50, y, f"Generated At: {datetime.now()}")

    y -= 30
    c.drawString(50, y, "Triggered Scenarios:")
    y -= 20

    for s in mule_info["scenarios"]:
        c.drawString(70, y, f"- {s}")
        y -= 15

    c.showPage()
    c.save()