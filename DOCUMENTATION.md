# Harvesting Brilliance: Detailed Project Documentation

## 1. Project Background
"Harvesting Brilliance" is an advanced analytical project aimed at the taxonomic classification of pumpkin seeds. Pumpkin seeds are not only a popular snack but also a vital agricultural product. Distinguishing between varieties like **Çerçevelik** and **Ürgüp Sivrisi** is crucial for quality control in the food industry and seed selection in agriculture.

## 2. Dataset Specification
- **Source**: `Pumpkin_Seeds_Dataset.xlsx`
- **Total Records**: 2500 entries.
- **Target Classes**: 
  - `Çerçevelik` (Encoded as 0)
  - `Ürgüp Sivrisi` (Encoded as 1)
- **Features (Morphological Measurements)**:
  1. **Area**: Primary size measurement in pixels.
  2. **Perimeter**: Boundary length.
  3. **Major Axis Length**: Primary diameter.
  4. **Solidity**: Ratio of area to convex area (measures "fullness").
  5. **Extent**: Ratio of area to bounding box.
  6. **Roundness**: Shape circularity.
  7. **Aspect Ratio**: Shape elongation.
  8. **Compactness**: Proximity to a perfect circle.

## 3. Machine Learning Pipeline

### Data Preprocessing
- **Cleaning**: Outlier detection using the IQR method was explored in initial notebooks.
- **Encoding**: Label Encoding was used to convert target classes (`Çerçevelik`, `Ürgüp Sivrisi`) into numerical values (0, 1).
- **Feature Selection**: From the original 13 features, 8 key morphological features were selected for the final production model to ensure optimal performance and simpler user input.

### Model Training & Comparison
We evaluated several algorithms during the development phase:
- **Gradient Boosting (Best Performance)**: ~86.8% Accuracy
- **Random Forest**: ~86.4% Accuracy
- **Logistic Regression**: ~83.8% Accuracy
- **Decision Tree**: ~83.2% Accuracy
- **Naive Bayes**: ~71.8% Accuracy

**Final Model**: The system effectively utilizes the **Gradient Boosting Classifier** (serialized as `model.pkl`) for its superior balance of precision and recall.

## 4. Web Application Architecture

### Backend (Flask)
The application is built on a modular Flask architecture:
- **`app.py`**: Handles incoming requests, processes form data, and interfaces with the ML model.
- **Routes**:
  - `/` (Home): Renders the landing page.
  - `/predict` (GET): Displays the diagnostic form.
  - `/predict` (POST): Processes the 8 morphological features through the ML model and returns the classification result.

### Frontend (HTML5/CSS3)
- **`index.html`**: A high-impact landing page featuring a hero banner, transparent call-to-action buttons, and a clean harvest-themed design.
- **`predict.html`**: A functional dashboard for seed analysis. It features a responsive grid layout for data entry and a side-by-side result display.
- **`style.css`**: A centralized stylesheet that manages the "Minimalist Premium" design system, ensuring consistency across all pages.

## 5. Visual Design Philosophy
The project transitioned through two main design phases:
1. **Premium Modern**: Characterized by glassmorphism, deep shadows, and complex animations.
2. **Minimalist Professional (Current)**: Refined based on user feedback to match a clean, high-contrast aesthetic (Black headers, white cards, and clear typography).

## 6. How to Run the Project

### Prerequisites
- Python 3.8+
- Essential Libraries: `flask`, `numpy`, `pandas`, `scikit-learn`, `openpyxl`

### Execution
1. Open your terminal in the `flask` directory.
2. Run the environment setup:
   ```bash
   pip install -r requirements.txt  # If available, else install manually
   ```
3. Launch the server:
   ```bash
   python app.py
   ```
4. Access the portal at `http://127.0.0.1:5000`.

## 7. Future Enhancements
- **Batch Processing**: Implementing CSV/Excel upload for multiple seed classifications.
- **Image Recognition**: Direct classification from seed photographs using Computer Vision (CNNs).
- **Export Analytics**: Ability to download prediction histories as PDF reports.

---
*Documentation Version: 2.0*
*Created for: Harvesting Brilliance - UnitaryTech*
