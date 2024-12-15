Abstract: Table Detection and Content Extraction Pipeline

This repository provides a comprehensive pipeline for table detection and content extraction from images and PDFs, leveraging the provided scripts and pre-trained models. The workflow comprises the following steps:

1. Image Deskewing
	•	Purpose: Ensures that input images with skewed tables are properly aligned for accurate detection.
	•	Process:
	•	The deskewImage function detects the rotation angle of the table or text content.
	•	Skew correction is applied by rotating the image to align the content horizontally.

2. Table Detection
	•	Purpose: Identifies the boundaries of tables within the image.
	•	Process:
	•	Functions plot_prediction and make_prediction utilize a pre-trained object detection model (predictor).
	•	Bounding boxes for tables are detected and visually highlighted with rectangles.
	•	Detected tables are cropped from the image for further processing.

3. Table Structure Recognition
	•	Purpose: Reconstructs the grid structure of the detected tables.
	•	Process:
	•	The recognize_structure function detects vertical and horizontal lines using morphological operations to map the table’s grid layout.
	•	Contours are identified within the grid, and bounding rectangles are drawn around individual cells.
	•	Rows and columns are organized by analyzing the spatial relationships of the detected cells.
	•	The result is a structured table format preserving the original layout.

4. Text Extraction
	•	Purpose: Extracts textual content from each detected cell.
	•	Process:
	•	OCR is applied to individual cells using Tesseract (via pytesseract) to extract text.
	•	Extracted text is organized in a structured format, aligning with the table’s original layout.

5. Output Generation
	•	Purpose: Provides the extracted table content in a reusable format.
	•	Process:
	•	Outputs the structured table content as CSV files or pandas DataFrames, preserving the original format for analysis or integration.

Key Features
	•	Handles complex tables, even those without headers.
	•	Converts PDF pages to images and processes them seamlessly.
	•	Outputs XML format with bounding box details for each detected table and cell.
	•	Converts XML to text files for simplified integration into workflows.

This repository provides an end-to-end solution for automating table detection and content extraction, integrating deskewing, structure recognition, and OCR to handle complex table layouts.
