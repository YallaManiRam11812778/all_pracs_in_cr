from jinja2 import Template
import pdfkit

template_str = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Authorization Form</title>
<style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        td, th {
            border: 1px solid #000;
            padding: 8px;
        }
        .logo-section {
            text-align: center;
        }
        .form-section {
            margin-top: 20px;
        }
        .checkbox-group {
            margin-top: 10px;
        }
</style>
</head>
<body>
<div class="logo-section">
<img src="{{ novotel_logo_url }}" alt="Novotel Logo" style="height: 50px;">
<img src="{{ ibis_logo_url }}" alt="Ibis Logo" style="height: 50px;">
</div>
 
    <div class="form-section">
<form method="post" action="{{ form_action }}">
<table>
<tr>
<td>Authorization No.</td>
<td><input type="text" name="authorization_no" value="{{ authorization_no }}"></td>
<td>
<label><input type="checkbox" name="complimentary" {% if complimentary %}checked{% endif %}> Complimentary</label>
<label><input type="checkbox" name="house_use" {% if house_use %}checked{% endif %}> House Use</label>
</td>
</tr>
<tr>
<td>Guest Name:</td>
<td colspan="2"><input type="text" name="guest_name" value="{{ guest_name }}"></td>
</tr>
<tr>
<td>Company/Agent:</td>
<td colspan="2"><input type="text" name="company_agent" value="{{ company_agent }}"></td>
</tr>
<tr>
<td>Position:</td>
<td colspan="2"><input type="text" name="position" value="{{ position }}"></td>
</tr>
<tr>
<td>Arrival Date:</td>
<td><input type="date" name="arrival_date" value="{{ arrival_date }}"></td>
<td>Departure Date: <input type="date" name="departure_date" value="{{ departure_date }}"></td>
</tr>
<tr>
<td>Persons:</td>
<td><input type="number" name="persons" value="{{ persons }}"></td>
<td>No. of Rooms: <input type="number" name="no_of_rooms" value="{{ no_of_rooms }}"></td>
</tr>
<tr>
<td>Room Type:</td>
<td colspan="2">
<label><input type="radio" name="room_type" value="Superior/Standard" {% if room_type == "Superior/Standard" %}checked{% endif %}> Superior/Standard</label>
<label><input type="radio" name="room_type" value="Premier" {% if room_type == "Premier" %}checked{% endif %}> Premier</label>
<label><input type="radio" name="room_type" value="Suite" {% if room_type == "Suite" %}checked{% endif %}> Suite</label>
</td>
</tr>
<tr>
<td>Reason for Complimentary:</td>
<td colspan="2">
<label><input type="checkbox" name="reasons" value="Inbound Contract" {% if 'Inbound Contract' in reasons %}checked{% endif %}> Inbound Contract</label>
<label><input type="checkbox" name="reasons" value="Group Contract" {% if 'Group Contract' in reasons %}checked{% endif %}> Group Contract</label>
<label><input type="checkbox" name="reasons" value="Guest Complaint" {% if 'Guest Complaint' in reasons %}checked{% endif %}> Guest Complaint</label>
<label><input type="checkbox" name="reasons" value="Prize Winner" {% if 'Prize Winner' in reasons %}checked{% endif %}> Prize Winner</label>
<label><input type="checkbox" name="reasons" value="Site Inspection" {% if 'Site Inspection' in reasons %}checked{% endif %}> Site Inspection/Fam. Trip</label>
<br>
                        Other (specify): <input type="text" name="other_reason" value="{{ other_reason }}">
</td>
</tr>
<tr>
<td>Inclusions:</td>
<td colspan="2">
<label><input type="checkbox" name="inclusions" value="Rooms" {% if 'Rooms' in inclusions %}checked{% endif %}> Rooms</label>
<label><input type="checkbox" name="inclusions" value="Food" {% if 'Food' in inclusions %}checked{% endif %}> Food</label>
<label><input type="checkbox" name="inclusions" value="Telephone" {% if 'Telephone' in inclusions %}checked{% endif %}> Telephone</label>
<label><input type="checkbox" name="inclusions" value="Internet" {% if 'Internet' in inclusions %}checked{% endif %}> Internet</label>
<label><input type="checkbox" name="inclusions" value="Laundry" {% if 'Laundry' in inclusions %}checked{% endif %}> Laundry</label>
<label><input type="checkbox" name="inclusions" value="Minibar" {% if 'Minibar' in inclusions %}checked{% endif %}> Minibar</label>
<br>
                        Other Remarks: <input type="text" name="remarks" value="{{ remarks }}">
</td>
</tr>
<tr>
<td>Requested By:</td>
<td><input type="text" name="requested_by" value="{{ requested_by }}"></td>
<td>Sign: <input type="text" name="sign" value="{{ sign }}"></td>
</tr>
<tr>
<td>Authorized By:</td>
<td><input type="text" name="authorized_by" value="{{ authorized_by }}"></td>
<td>Reservation No.: <input type="text" name="reservation_no" value="{{ reservation_no }}"></td>
</tr>
</table>
<button type="submit">Submit</button>
</form>
</div>
</body>
</html>
"""
# Sample data for rendering
data = {
    "novotel_logo_url": "https://example.com/novotel_logo.png",
    "ibis_logo_url": "https://example.com/ibis_logo.png",
    "form_action": "/submit-authorization",
    "authorization_no": "AUTH12345",
    "complimentary": True,
    "house_use": False,
    "guest_name": "John Doe",
    "company_agent": "Acme Corporation",
    "position": "Manager",
    "arrival_date": "2025-01-24",
    "departure_date": "2025-01-30",
    "persons": 2,
    "no_of_rooms": 1,
    "room_type": "Suite",
    "reasons": ["Inbound Contract", "Prize Winner"],
    "other_reason": "Special Event",
    "inclusions": ["Rooms", "Food", "Internet"],
    "remarks": "Special dietary requirements",
    "requested_by": "Alice Johnson",
    "sign": "A. Johnson",
    "authorized_by": "Bob Smith",
    "reservation_no": "RES67890"
}
# Create the template
template = Template(template_str)

# Render the template with the sample data
rendered_html = template.render(data)

def convert_html_to_pdf(html_content, pdf_path):
    try:
        pdfkit.from_string(html_content, pdf_path)
        print(f"PDF generated and saved at {pdf_path}")
    except Exception as e:
        print(f"PDF generation failed: {e}")
# PDF path to save
pdf_path = '/home/caratred/Documents/ram/test/jinja_python/example_from_html.pdf'

# Generate PDF
convert_html_to_pdf(rendered_html, pdf_path)