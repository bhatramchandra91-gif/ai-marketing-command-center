from fpdf import FPDF

def create_proposal(client, service, price):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    text = f"""
    Proposal for {client}

    Service: {service}
    Price: {price}

    We will handle complete digital marketing including:
    - Social media
    - Ads
    - Content
    - Lead generation
    """

    for line in text.split("\n"):
        pdf.cell(200, 8, txt=line, ln=True)

    filename = f"{client}_proposal.pdf"
    pdf.output(filename)
    return filename
