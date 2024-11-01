# Image Captioning with BLIP

This project is a Streamlit application that allows users to upload an image and generate a descriptive caption using the BLIP (Bootstrapped Language-Image Pretraining) model from Hugging Face's Transformers library. The application provides an intuitive interface for generating captions, making it useful for a variety of applications, including accessibility and content creation.

## Features

- **Image Upload**: Users can upload images in JPG, JPEG, or PNG formats.
- **Caption Generation**: The application generates a descriptive caption for the uploaded image using the BLIP model.
- **Visual Feedback**: Displays the uploaded image alongside the generated caption.

## Requirements

To run this application, you need the following:

- Python 3.7 or higher
- Streamlit
- Transformers
- Pillow

You can install the required packages using pip:

```bash
pip install streamlit transformers Pillow
```

## Getting Started

1. **Clone the repository** or download the files:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

   Replace `app.py` with the name of your Python file containing the Streamlit code.

3. **Open your browser** and navigate to the URL provided in the terminal (usually `http://localhost:8501`).

4. **Upload an image** using the upload button and wait for the generated caption to appear below the image.

## Application Structure

- **app.py**: The main application file that contains the Streamlit code for image uploading and caption generation.
- **Images/**: Directory to store uploaded images.

## Usage

1. Launch the application as described in the "Getting Started" section.
2. Click on "Choose an image..." to upload an image file.
3. After uploading, the application will validate the image and generate a caption using the BLIP model.
4. The uploaded image and its generated caption will be displayed on the page.

## Notes

- Ensure you have a stable internet connection as the BLIP model is downloaded from Hugging Face the first time you run the application.
- The application is designed to handle basic image formats (JPG, JPEG, PNG) only. Please ensure that the uploaded images are in one of these formats.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/) for providing the BLIP model.
- [Streamlit](https://streamlit.io/) for the framework that makes it easy to build web apps for machine learning.
