from jinja2 import Template
import pdfkit

def rebuild_to_structured_array(flat_array): 
    result = []
    current_block = None
    current_section = None
    current_row = None
    current_column = None
 
    for item in reversed(flat_array):
        description = item.get("description")
 
        if description == "Block Break":
            # Push current section, row, and block if they exist
            if current_row:
                current_section["rows"].insert(0, current_row)
                current_row = None
 
            if current_section:
                current_block["sections"].insert(0, current_section)
                current_section = None
 
            if current_block:
                result.insert(0, current_block)
 
            current_block = {
                "fieldtype": item.get("fieldtype"),
                "fieldname": item.get("fieldname"),
                "label": item.get("label") if item.get("label") else "",
                "parent": item.get("parent"),
                "sections": []
            }
 
        elif description == "Section Break":
            # Push current row and section if they exist
            if current_row:
                current_section["rows"].insert(0, current_row)
                current_row = None
 
            if current_section:
                current_block["sections"].insert(0, current_section)
 
            current_section = {
                "fieldtype": item.get("fieldtype"),
                "fieldname": item.get("fieldname"),
                "label": item.get("label") if item.get("label") else "",
                "parent": item.get("parent"),
                "rows": []
            }
 
        elif description == "Row Break":
            # Push current row if it exists
            if current_row:
                current_section["rows"].insert(0, current_row)
 
            current_row = {
                "fieldtype": item.get("fieldtype"),
                "fieldname": item.get("fieldname"),
                "label": item.get("label") if item.get("label") and not item.get("label").lower().startswith("row_") else "",
                "parent": item.get("parent"),
                "columns": []
            }
 
        elif description == "Column Break":
            # Add the column to the current row
            current_column = {
                "fieldtype": item.get("fieldtype"),
                "fieldname": item.get("fieldname"),
                "label": item.get("label") if item.get("label") else "",
                "parent": item.get("parent"),
                "fields": []
            }
            current_row["columns"].insert(0, current_column)
 
        else:  # Regular field
            # Add field to the current column
            if current_column:
                updated_field = {
                    "fieldname": item.get("fieldname"),
                    "fieldtype": item.get("fieldtype"),
                    "parent": item.get("parent"),
                    "label": item.get("label"),
                    "reqd": item.get("reqd"),
                    "options": item.get("options"),
                    "values": item.get("values")
                    }
                current_column["fields"].insert(0, updated_field)
 
    # Push the last row, section, and block (if any exist)
    if current_row:
        current_section["rows"].insert(0, current_row)
 
    if current_section:
        current_block["sections"].insert(0, current_section)
 
    if current_block:
        result.insert(0, current_block)
    return result

from jinja2 import Template
 
json_object = [{'description': 'Field', 'fieldname': 'guest_name', 'fieldtype': 'Data', 'idx': 0, 'label': 'Guest name', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': '', 'fieldtype': 'Column Break', 'idx': 1, 'label': ''}, {'description': 'Field', 'fieldname': 'company_name', 'fieldtype': 'Data', 'idx': 2, 'label': 'Company name', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': '', 'fieldtype': 'Column Break', 'idx': 3, 'label': ''}, {'description': 'Field', 'fieldname': 'position', 'fieldtype': 'Data', 'idx': 4, 'label': 'Position', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': '', 'fieldtype': 'Column Break', 'idx': 5, 'label': ''}, {'description': 'Row Break', 'fieldname': 'row_0_0_0', 'fieldtype': 'Column Break', 'idx': 6, 'label': 'row_0_0_0'}, {'description': 'Section Break', 'fieldname': 'guest_details', 'fieldtype': 'Section Break', 'label': 'guest details', 'idx': 7}, {'description': 'Field', 'fieldname': 'arrival_date', 'fieldtype': 'Data', 'idx': 8, 'label': 'Arrival date', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': '', 'fieldtype': 'Column Break', 'idx': 9, 'label': ''}, {'description': 'Field', 'fieldname': 'departure_date', 'fieldtype': 'Data', 'idx': 10, 'label': 'Departure date', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': '', 'fieldtype': 'Column Break', 'idx': 11, 'label': ''}, {'description': 'Row Break', 'fieldname': 'row_0_1_0', 'fieldtype': 'Column Break', 'idx': 12, 'label': 'row_0_1_0'}, {'description': 'Section Break', 'fieldname': 'stay_details', 'fieldtype': 'Section Break', 'label': 'stay details', 'idx': 13}, {'description': 'Field', 'fieldname': 'number_of_persons', 'fieldtype': 'Data', 'idx': 14, 'label': 'Number of persons', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': '', 'fieldtype': 'Column Break', 'idx': 15, 'label': ''}, {'description': 'Field', 'fieldname': 'number_of_nights', 'fieldtype': 'Data', 'idx': 16, 'label': 'Number of nights', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': '', 'fieldtype': 'Column Break', 'idx': 17, 'label': ''}, {'description': 'Field', 'fieldname': 'number_of_rooms', 'fieldtype': 'Data', 'idx': 18, 'label': 'Number of rooms', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': '', 'fieldtype': 'Column Break', 'idx': 19, 'label': ''}, {'description': 'Row Break', 'fieldname': 'row_0_2_0', 'fieldtype': 'Column Break', 'idx': 20, 'label': 'row_0_2_0'}, {'description': 'Section Break', 'fieldname': '', 'fieldtype': 'Section Break', 'label': '', 'idx': 21}, {'description': 'Field', 'fieldname': 'allocated_rooms_in_standard', 'fieldtype': 'Data', 'idx': 22, 'label': 'Allocated rooms in standard', 'reqd': 0, 'value': ''}, {'description': 'Field', 'fieldname': 'total_persons_stayed_in_standard', 'fieldtype': 'Data', 'idx': 23, 'label': 'Total persons stayed in standard', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': 'standard_room', 'fieldtype': 'Column Break', 'idx': 24, 'label': 'Standard room'}, {'description': 'Field', 'fieldname': 'allocated_rooms_in_premier', 'fieldtype': 'Data', 'idx': 25, 'label': 'Allocated rooms in premier', 'reqd': 0, 'value': ''}, {'description': 'Field', 'fieldname': 'total_persons_stayed_in_premier', 'fieldtype': 'Data', 'idx': 26, 'label': 'Total persons stayed in premier', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': 'premier_room', 'fieldtype': 'Column Break', 'idx': 27, 'label': 'Premier room'}, {'description': 'Field', 'fieldname': 'allocated_room_in_suite', 'fieldtype': 'Data', 'idx': 28, 'label': 'Allocated room in suite', 'reqd': 0, 'value': ''}, {'description': 'Field', 'fieldname': 'total_persons_stayed_in_suite', 'fieldtype': 'Data', 'idx': 29, 'label': 'Total persons stayed in suite', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': 'suite_room', 'fieldtype': 'Column Break', 'idx': 30, 'label': 'Suite room'}, {'description': 'Row Break', 'fieldname': 'row_0_3_0', 'fieldtype': 'Column Break', 'idx': 31, 'label': 'row_0_3_0'}, {'description': 'Section Break', 'fieldname': 'room_details', 'fieldtype': 'Section Break', 'label': 'Room details', 'idx': 32}, {'description': 'Block Break', 'fieldname': 'requestor', 'fieldtype': 'Section Break ', 'label': 'Requestor', 'idx': 33}, {'description': 'Field', 'fieldname': 'reservation_number', 'fieldtype': 'Data', 'idx': 34, 'label': 'Reservation number', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': '', 'fieldtype': 'Column Break', 'idx': 35, 'label': ''}, {'description': 'Field', 'fieldname': 'reservation_made_by', 'fieldtype': 'Data', 'idx': 36, 'label': 'Reservation made by', 'reqd': 0, 'value': ''}, {'description': 'Column Break', 'fieldname': '', 'fieldtype': 'Column Break', 'idx': 37, 'label': ''}, {'description': 'Row Break', 'fieldname': 'row_0_0_1', 'fieldtype': 'Column Break', 'idx': 38, 'label': 'row_0_0_1'}, {'description': 'Section Break', 'fieldname': 'reservtaion_details', 'fieldtype': 'Section Break', 'label': 'Reservtaion details', 'idx': 39}, {'description': 'Block Break', 'fieldname': 'approver1', 'fieldtype': 'Section Break ', 'label': 'Approver-1', 'idx': 40}]
# Sample nested data structure
data = rebuild_to_structured_array(flat_array=json_object)

# Jinja2 template string
template_str = """
<!DOCTYPE html>
<html>
<head>
<title>Dynamic Form</title>
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        background-color: #f9fafb;
    }
    .main-block {
        border-bottom: 1px solid #dfe3e8;
    }
    /* Block Styling */
    .block-container {
        border-bottom: 2px solid #dfe3e8;
        border: 1px solid #dfe3e8;
        background-color: #ffffff;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 40px; 
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04); 
    }
    .block-container h2 {
        font-size: 15px;
        font-weight: 700;
        color: #202223;
        margin-bottom: 10px;
        # border-bottom: 1px solid #dfe3e8;
        padding-bottom: 10px;
    }
    /* Section Styling */
    .section-container {
        border-radius: 6px;
        background-color: #f9fafc;
        padding: 20px; 
        margin-bottom: 30px; 
    }
    .section-container h3 {
        font-size: 13px;
        font-weight: 600 !important;
        color: #202223;
        margin-bottom: 15px;
        padding-bottom: 5px;
        
    }
    .sectionLabel {
        font-weight: 450;
    }
    /* Flexbox for Columns */
    .flex-container {
        display: flex;
        gap: 20px;
        margin-bottom: 15px;
    }
    .column {
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 15px;
        width: 100%;
        # max-width: 48%;
        border: 1px solid #dfe3e8;
        padding: 0px 15px 15px 15px;
        border-radius: 10px;
        margin: 5px;
        background-color: #FFFFFF;
    }
    .column h4 {
        font-size: 13px;
        font-weight: 500;
        margin-top: 15px;
    }
    /* Label Styling */
    label {
        font-size: 13px;
        font-weight: 500;
        color: #202223;
        margin-bottom: 5px;
        margin-left: 3px;
        display: block;
    }
    /* Input Styling */
    input {
        padding: 7px 16px;
        margin-bottom: 10px;
        font-size: 13px;
        border: 1px solid #dfe3e8;
        border-radius: 6px;
        background-color: #ffffff;
        box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.05); 
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    input:focus {
        border-color: #5c6ac4;
        outline: none;
        box-shadow: 0 0 0 2px rgba(92, 106, 196, 0.3); 
    }
    input::placeholder {
        color: #a8a8a8;
        font-style: italic;
    }
    .column input:last-child {
        margin-bottom: 0;
    }
    .section-container h3:first-of-type {
        margin-top: 0;
    }
    .flex-container:last-of-type {
        margin-bottom: 0;
    }
</style>
</head>
<body>
<div class="main-block">
    {% for block in data %}
        <div class="block-container">
            <h2>{{ block.label }}</h2>
            {% for section in block.sections %}
                <div class="section-container">
                    <h3 class="sectionLabel">{{ section.label }}</h3>
                    {% for row in section.rows %}
                        <div class="flex-container">
                            {% for column in row.columns %}
                                <div class="column">
                                    <h4>{{ column.label }}</h4>
                                    {% for field in column.fields %}
                                        <label>{{ field.label }}</label>
                                        <input type="text" value="{{ field['values'] }}" />
                                    {% endfor %}
                                </div>
                            {% endfor %}
                        </div>
                    {% endfor %}
                </div>
            {% endfor %}
        </div>
    {% endfor %}
</div>
</body>
</html>

"""

html_output = Template(template_str).render(data=data)

def convert_html_to_pdf(html_content, pdf_path):
    try:
        pdfkit.from_string(html_content, pdf_path)
        print(f"PDF generated and saved at {pdf_path}")
    except Exception as e:
        print(f"PDF generation failed: {e}")
# PDF path to save
pdf_path = '/home/caratred/jinja_to_form.pdf'

# Generate PDF
convert_html_to_pdf(html_output, pdf_path)