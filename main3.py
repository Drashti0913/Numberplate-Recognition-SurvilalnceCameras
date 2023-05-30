import cv2
import pytesseract
import tensorflow as tf

# Load pre-trained TensorFlow model for object detection
model = tf.keras.models.load_model(r"C:\Users\drash\OneDrive\Documents\Extra\Cyber\saved_model.pb")



# Define a function to detect license plates
def detect_license_plate(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filtering to remove noise while preserving edges
    filtered = cv2.bilateralFilter(gray, 11, 17, 17)

    # Detect edges using Canny edge detection
    edges = cv2.Canny(filtered, 30, 200)

    # Find contours of regions with high edge density
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over contours to find license plates
    for contour in contours:
        # Get the perimeter of the contour
        perimeter = cv2.arcLength(contour, True)

        # Use perimeter to approximate polygonal shape of contour
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        # If the contour has four vertices, it may be a license plate
        if len(approx) == 4:
            # Get the bounding box of the contour
            x, y, w, h = cv2.boundingRect(contour)

            # Crop the license plate from the image
            plate_image = image[y:y+h, x:x+w]

            # Use TensorFlow to detect characters in license plate
            characters = model.predict(plate_image)

            # Convert character predictions to text using PyTesseract
            text = pytesseract.image_to_string(characters)

            # If the text matches a license plate pattern, return the plate number
            if text_matches_pattern(text):
                return text

    # If no license plate is found, return None
    return None

# Define a function to match text to a license plate pattern
def text_matches_pattern(text):
    # TODO: Implement text matching algorithm
    pass

# Load video file
cap = cv2.VideoCapture(r"C:\Users\drash\OneDrive\Documents\Extra\Cyber\video.mp4")

# Iterate over frames in the video
while True:
    # Read the next frame
    ret, frame = cap.read()

    # If no frame is read, break out of the loop
    if not ret:
        break

    # Detect license plates in the frame
    plate = detect_license_plate(frame)

    # If a license plate is detected, display it on the frame
    if plate:
        cv2.putText(frame, plate, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('frame', frame)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
