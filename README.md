## Number Plate Detection and Recognition System

This project implements a robust system for detecting and recognizing vehicle number plates using surveillance camera footage. Leveraging the power of OpenCV and Tesseract OCR, the system processes video input to accurately identify and extract number plate information in various environmental conditions.

### Project Overview

The system uses the YOLOv5 object detection model combined with image processing techniques to locate and decipher number plates from real-time or recorded video feeds. The core functionality is built on Python, utilizing libraries such as OpenCV for image operations and Tesseract OCR for text extraction.

### Features

- Real-time number plate detection from surveillance video streams.
- High accuracy in diverse lighting and weather conditions.
- Extraction and recognition of alphanumeric characters from plates.
- State identification from number plate characters.

### Technologies Used

- Python 3.8+
- OpenCV (cv2)
- Numpy
- Pytesseract
- Haar Cascades for object detection

### Installation

Ensure you have Python 3.8 or higher installed on your system. Follow the steps below to set up the project environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/Drashti0913/Object-Detection
   cd Object-Detection
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Tesseract-OCR:
   - Download and install Tesseract from [this link](https://github.com/tesseract-ocr/tesseract).
   - Ensure the Tesseract executable is in your system’s path, or modify the `pytesseract.pytesseract.tesseract_cmd` path in the script.

### Usage

To run the number plate detection on an image file:

```bash
python detect.py --source <path_to_your_image>
```

Replace `<path_to_your_image>` with the path to the image you want to process.

### Results

The system outputs images with detected number plates highlighted by bounding boxes. Detected text from the number plates is displayed above the bounding boxes. Results are saved as image files and can also be viewed in a window during processing.

### Contributing

Contributions to this project are welcome. To contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.

### Acknowledgements

- Thanks to the YOLOv5 team for their state-of-the-art object detection model.
- Thanks to the developers of Tesseract OCR for providing a powerful tool for text recognition tasks.

### Contact

For any inquiries or issues, please open an issue on the repository, or contact [drashtibhavsar09@gmail.com](mailto:drashtibhavsar09@gmail.com).
