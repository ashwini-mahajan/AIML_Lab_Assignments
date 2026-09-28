import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Create workbook
wb = openpyxl.Workbook()

# Sheet setup
ws = wb.active
ws.title = "Collabs Tracker"
ws.views.sheetView[0].showGridLines = True

# Premium aesthetic color palette (Rose / Slate / Clean Neutral)
PRIMARY_DARK = "1E293B"     # Slate 800
HEADER_BG = "0F172A"        # Deep Navy / Slate 900
ZEBRA_BG = "F8FAFC"         # Light clean grey
BORDER_COLOR = "CBD5E1"     # Slate 300

PAID_TAG_BG = "DCFCE7"      # Soft emerald green
PAID_TAG_TXT = "166534"
BARTER_TAG_BG = "F1F5F9"    # Neutral soft slate
BARTER_TAG_TXT = "475569"

STATUS_REC_BG = "DCFCE7"    # Green
STATUS_REC_TXT = "166534"
STATUS_PEND_BG = "FEF3C7"   # Amber/Yellow
STATUS_PEND_TXT = "92400E"
STATUS_BARTER_BG = "E0E7FF" # Soft Indigo
STATUS_BARTER_TXT = "3730A3"

thin_border = Border(
    left=Side(style='thin', color=BORDER_COLOR),
    right=Side(style='thin', color=BORDER_COLOR),
    top=Side(style='thin', color=BORDER_COLOR),
    bottom=Side(style='thin', color=BORDER_COLOR)
)

# Header styling
header_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
header_fill = PatternFill(start_color=HEADER_BG, end_color=HEADER_BG, fill_type="solid")

# Title Block
ws['B2'] = "CREATOR BRAND COLLABORATIONS MASTER TRACKER"
ws['B2'].font = Font(name="Segoe UI", size=15, bold=True, color=PRIMARY_DARK)
ws['B3'] = "Complete record of Paid & Barter campaigns, deliverables, payment statuses & POCs"
ws['B3'].font = Font(name="Segoe UI", size=10, italic=True, color="64748B")

# Summary KPI Cards (Top Bar)
kpi_data = [
    (2, "Total Tracked Collabs", "=COUNTA(B8:B35)", "0"),
    (4, "Total Paid Revenue", "=SUMIF(E8:E35, \"Paid\", F8:F35)", "₹ #,##0"),
    (6, "Total Cash Received", "=SUMIFS(F8:F35, E8:E35, \"Paid\", J8:J35, \"Received\")", "₹ #,##0"),
    (8, "Pending Receivables", "=SUMIFS(F8:F35, E8:E35, \"Paid\", J8:J35, \"Pending\")", "₹ #,##0"),
    (10, "Total Barter Collabs", "=COUNTIF(E8:E35, \"Barter\")", "0")
]

for col, title, formula, num_fmt in kpi_data:
    c_t = ws.cell(row=5, column=col, value=title)
    c_t.font = Font(name="Segoe UI", size=9, bold=True, color="475569")
    c_t.alignment = Alignment(horizontal="center", vertical="center")
    c_t.fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    
    c_v = ws.cell(row=6, column=col, value=formula)
    c_v.font = Font(name="Segoe UI", size=13, bold=True, color=PRIMARY_DARK)
    c_v.alignment = Alignment(horizontal="center", vertical="center")
    c_v.number_format = num_fmt
    c_v.fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
    
    for r in [5, 6]:
        ws.cell(row=r, column=col).border = thin_border

# Columns required for full professional creator workflow
headers = [
    "S.No",
    "Month",
    "Brand Name",
    "Deliverables / Scope",
    "Collab Type\n(Paid / Barter)",
    "Commercial\nAmount (₹)",
    "Deliverable Status\n(Live / In Progress)",
    "Deliverable Link\n(Reel / Video URL)",
    "Invoice Status\n(Sent / Pending / NA)",
    "Payment Status\n(Received / Pending / NA)",
    "Agency / POC Name",
    "Notes & Requirements"
]

header_row = 8
ws.row_dimensions[header_row].height = 28

for col_idx, h in enumerate(headers, start=1):
    cell = ws.cell(row=header_row, column=col_idx, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border

# Master data from May, June, July, September + Campaign logs
data = [
    # May 2026
    (1, "May 2026", "Flipkart Content Central", "120 Short-form UGC Videos", "Paid", 14400, "Live", "", "Sent", "Received", "Flipkart Team", "Full ₹14.4k payment received"),
    (2, "May 2026", "Parachute", "1 Dedicated Brand Reel", "Paid", 2500, "Live", "", "Sent", "Received", "Agency POC", "Bank transfer completed"),
    (3, "May 2026", "Elle 18", "Campus Ambassador (Month 4 Retainer)", "Paid", 2500, "Live", "", "Sent", "Received", "Elle 18 Team", "Monthly CA Retainer"),
    (4, "May 2026", "Nykaa - Moi Perfume", "Perfume PR Review / Story", "Barter", 0, "Live", "", "N/A", "Product Received", "Nykaa PR", "Barter PR Gifting"),
    (5, "May 2026", "Beauty Fred", "Skincare Review Deliverable", "Barter", 0, "Live", "", "N/A", "Product Received", "Beauty Fred POC", "Barter PR Gifting"),
    (6, "May 2026", "Dalba Sunscreen", "Sunscreen Product Reel / Review", "Barter", 0, "Live", "", "N/A", "Product Received", "Dalba Team", "Barter PR Gifting"),
    
    # June 2026
    (7, "June 2026", "WishCare", "Dedicated Campaign Reel", "Paid", 800, "Live", "", "Sent", "Received", "WishCare POC", "Agency transfer received"),
    (8, "June 2026", "VF - Lenskart", "Story & Task Deliverable", "Paid", 300, "Live", "", "Sent", "Received", "Viral Fission POC", "Task payout received"),
    (9, "June 2026", "Dot & Key", "Product Seeding / Review", "Barter", 0, "Live", "", "N/A", "Product Received", "Dot & Key Team", "PR Gifting"),
    (10, "June 2026", "Fiama Soap", "Product Integration / Reel", "Barter", 0, "Live", "", "N/A", "Product Received", "Fiama PR", "PR Gifting"),

    # July 2026
    (11, "July 2026", "Pantene", "Bond Repair Reel", "Paid", 750, "Live", "", "Sent", "Received", "Agency POC", "Reimbursement + Fee"),
    (12, "July 2026", "Taco Bell", "Food Campaign Video", "Paid", 1200, "Live", "", "Sent", "Received", "Agency POC", "Direct bank transfer"),
    (13, "July 2026", "Rapido", "Brand Promotion Video", "Paid", 1800, "Live", "", "Sent", "Received", "Agency POC", "Agency transfer"),
    (14, "July 2026", "Elle 18", "Campus Ambassador (Month 5 Retainer)", "Paid", 2500, "Live", "", "Sent", "Received", "Elle 18 Team", "Monthly CA Retainer"),
    (15, "July 2026", "Moana Disney", "Campaign Deliverable", "Paid", 500, "Live", "", "Sent", "Received", "Agency POC", "Campaign payout"),
    (16, "July 2026", "NNOW", "Fashion Integration", "Paid", 800, "Live", "", "Sent", "Received", "NNOW Team", "Platform payout"),
    (17, "July 2026", "Elaganz", "Product Promotional Video", "Paid", 1000, "Live", "", "Sent", "Received", "Elaganz POC", "Brand transfer"),
    (18, "July 2026", "Stringz Toothpaste", "Reel Integration", "Paid", 1600, "Live", "", "Sent", "Received", "Agency POC", "Agency transfer"),
    (19, "July 2026", "Buddup Network", "Network Campaign Deliverable", "Paid", 1300, "Live", "", "Sent", "Received", "Buddup POC", "Network payout"),
    (20, "July 2026", "Taj Perfume", "Dedicated Fragrance Reel", "Paid", 2300, "Live", "", "Sent", "Received", "Brand POC", "Direct transfer"),
    (21, "July 2026", "Pantene", "Bond Repair Task 2", "Paid", 700, "Live", "", "Sent", "Received", "Agency POC", "Reimbursement + Fee"),

    # September 2026 (Active & Upcoming)
    (22, "September 2026", "Pantene", "Bond Repair Reel (White Outfit Mandate)", "Paid", 700, "In Progress", "", "Pending", "Pending", "Ayushi (VuduCom)", "White outfit only; clean minimalist corner; ProV B5"),
    (23, "September 2026", "L'Oréal Paris", "Collagen Lifter Range (Pastel Outfit Mandate)", "Paid", 900, "In Progress", "", "Pending", "Pending", "Agency POC", "Solid pastel only (no white/black); volume keywords"),
    (24, "September 2026", "Biotique", "Fresh Neem Anti-Dandruff Reel (< ₹200)", "Paid", 1500, "In Progress", "", "Pending", "Pending", "Brand POC", "Cross-posting deliverable (IG & YouTube Shorts)")
]

start_row = 9
for i, row_data in enumerate(data):
    current_row = start_row + i
    ws.row_dimensions[current_row].height = 22
    is_zebra = (i % 2 == 1)
    
    for col_idx, val in enumerate(row_data, start=1):
        cell = ws.cell(row=current_row, column=col_idx, value=val)
        cell.font = Font(name="Segoe UI", size=9.5)
        cell.border = thin_border
        
        # Zebra striping background
        if is_zebra:
            cell.fill = PatternFill(start_color=ZEBRA_BG, end_color=ZEBRA_BG, fill_type="solid")
            
        # Alignments & formatting
        if col_idx in (1, 2, 7, 9):
            cell.alignment = Alignment(horizontal="center", vertical="center")
        elif col_idx == 5: # Paid / Barter
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if val == "Paid":
                cell.fill = PatternFill(start_color=PAID_TAG_BG, end_color=PAID_TAG_BG, fill_type="solid")
                cell.font = Font(name="Segoe UI", size=9.5, bold=True, color=PAID_TAG_TXT)
            else:
                cell.fill = PatternFill(start_color=BARTER_TAG_BG, end_color=BARTER_TAG_BG, fill_type="solid")
                cell.font = Font(name="Segoe UI", size=9.5, bold=True, color=BARTER_TAG_TXT)
        elif col_idx == 6: # Commercial Amount
            cell.number_format = "₹ #,##0"
            cell.alignment = Alignment(horizontal="right", vertical="center")
            cell.font = Font(name="Segoe UI", size=9.5, bold=(val > 0))
        elif col_idx == 10: # Payment Status
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if val == "Received":
                cell.fill = PatternFill(start_color=STATUS_REC_BG, end_color=STATUS_REC_BG, fill_type="solid")
                cell.font = Font(name="Segoe UI", size=9.5, bold=True, color=STATUS_REC_TXT)
            elif val == "Pending":
                cell.fill = PatternFill(start_color=STATUS_PEND_BG, end_color=STATUS_PEND_BG, fill_type="solid")
                cell.font = Font(name="Segoe UI", size=9.5, bold=True, color=STATUS_PEND_TXT)
            else:
                cell.fill = PatternFill(start_color=STATUS_BARTER_BG, end_color=STATUS_BARTER_BG, fill_type="solid")
                cell.font = Font(name="Segoe UI", size=9.5, color=STATUS_BARTER_TXT)
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center")

# Total Row at the bottom
end_data_row = start_row + len(data) - 1
total_row = end_data_row + 1
ws.row_dimensions[total_row].height = 24

ws.cell(row=total_row, column=4, value="TOTAL COMMERCIAL VALUE").font = Font(name="Segoe UI", size=10, bold=True, color=PRIMARY_DARK)
ws.cell(row=total_row, column=4).alignment = Alignment(horizontal="right", vertical="center")

total_cell = ws.cell(row=total_row, column=6, value=f"=SUM(F{start_row}:F{end_data_row})")
total_cell.font = Font(name="Segoe UI", size=10, bold=True, color=PRIMARY_DARK)
total_cell.number_format = "₹ #,##0"
total_cell.alignment = Alignment(horizontal="right", vertical="center")

for c in range(1, len(headers) + 1):
    ws.cell(row=total_row, column=c).border = thin_border
    ws.cell(row=total_row, column=c).fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")

# Auto-adjust column widths
col_widths = {
    1: 6,    # S.No
    2: 15,   # Month
    3: 24,   # Brand Name
    4: 34,   # Deliverables / Scope
    5: 16,   # Collab Type
    6: 18,   # Commercial Amount
    7: 18,   # Deliverable Status
    8: 24,   # Deliverable Link
    9: 16,   # Invoice Status
    10: 18,  # Payment Status
    11: 20,  # Agency / POC
    12: 40   # Notes
}

for col_idx, width in col_widths.items():
    col_letter = get_column_letter(col_idx)
    ws.column_dimensions[col_letter].width = width

output_path = "Master_Brand_Collabs_Tracker.xlsx"
wb.save(output_path)
print(f"File created successfully: {output_path}")