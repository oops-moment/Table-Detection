import cv2
import pytesseract
import xml.etree.ElementTree as ET

def parse_xml(xml_path):
    """
    Parse the XML file and extract bounding boxes and structure.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    tables = []
    for table in root.findall(".//table"):
        cells = []
        for cell in table.findall(".//cell"):
            bounding_box = cell.find(".//boundingbox")
            row = int(cell.get("row"))
            column = int(cell.get("column"))
            x, y, w, h = [int(bounding_box.get(attr)) for attr in ["x", "y", "w", "h"]]
            cells.append({"row": row, "column": column, "bbox": (x, y, x + w, y + h)})
        tables.append(cells)
    return tables

def extract_text_from_bbox(image, bbox):
    """
    Extract text from the specified bounding box in the image.
    """
    x1, y1, x2, y2 = bbox
    cropped_img = image[y1:y2, x1:x2]
    text = pytesseract.image_to_string(cropped_img, config="--psm 6")
    return text.strip()

def process_image_and_xml(image_path, xml_path, output_path):
    """
    Process the image and XML file, extract text from bounding boxes,
    and save it to a text file in a formatted manner.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not load image. Check the image path.")

    # Parse the XML file
    tables = parse_xml(xml_path)

    # Open the output file
    with open(output_path, "w") as output_file:
        table_index = 1

        for cells in tables:
            # Organize cells by rows and columns
            table = {}
            for cell in cells:
                row, column, bbox = cell["row"], cell["column"], cell["bbox"]
                if row not in table:
                    table[row] = {}
                table[row][column] = bbox

            # Sort rows and columns
            sorted_rows = sorted(table.keys())
            output_file.write(f"Table {table_index}:\n")

            for row in sorted_rows:
                sorted_columns = sorted(table[row].keys())
                row_text = []

                for column in sorted_columns:
                    bbox = table[row][column]
                    text = extract_text_from_bbox(image, bbox)
                    row_text.append(text)

                output_file.write("\t".join(row_text) + "\n")
            output_file.write("\n")
            table_index += 1

    print(f"Extraction complete. Output saved to {output_path}")

# Example Usage
image_path = "page_5.jpg"  # Path to input image
xml_path = "xml2text.xml"    # Path to input XML file
output_path = "output_text.txt" # Path to save extracted text

process_image_and_xml(image_path, xml_path, output_path)