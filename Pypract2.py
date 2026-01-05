import pdfplumber
import re
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def convert_time(ms):
    return datetime.fromtimestamp(int(ms) / 1000).strftime("%d-%m-%Y %H:%M:%S")

def call_type(t):
    return {"1": "Incoming", "2": "Outgoing", "3": "Missed"}.get(t, "Unknown")

text = ""

with pdfplumber.open(r"C:\Users\sudar\Downloads\à¤_à¥_à¤²_1767532624567.xml.pdf") as pdf:
    for page in pdf.pages:
        text += page.extract_text() + "\n"

blocks = re.findall(
    r"<phoneNumber>\s*(.*?)</phoneNumber>.*?"
    r"<dateTime>\s*(.*?)</dateTime>.*?"
    r"<callDuration>\s*(.*?)</callDuration>.*?"
    r"<logType>\s*(.*?)</logType>",
    text,
    re.S
)

c = canvas.Canvas("call_logs_dur.pdf", pagesize=A4)
w, h = A4
y = h - 40

for p, d, dur, t in blocks:
    if call_type(t) == "Outgoing" and dur > "0":
        lines = [
            f"Phone Number : {p}",
            f"Date & Time  : {convert_time(d)}",
            f"Duration     : {dur} seconds",
            f"Call Type    : {call_type(t)}",
            "-" * 40
        ]

        for line in lines:
            c.drawString(40, y, line)
            y -= 15
            if y < 40:
                c.showPage()
                y = h - 40

c.save()
