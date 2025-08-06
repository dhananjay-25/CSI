📜 Hindi Digit Classification, ML model & App
=========================================

This is a simple yet interactive **Streamlit application** where users can draw **Hindi digits (0-9)** using their mouse or finger, and the app will predict the digit using a pre-trained **SVM** or **KNN** model trained on **HOG (Histogram of Oriented Gradients)** features.

* * * * *

📍 Demo Video
-------------

👉 [Click here to watch the demo video](https://youtu.be/L-h9DBNvb5E)


* * * * *

📁 Project Structure
--------------------

```
digit_recognition_app/
├── hindi-digit-classification.ipynb  # Jupyter Notebook for training models
├── app.py                    # Main Streamlit App
├── models/
│   ├── svm_model.joblib      # Trained SVM model
│   └── knn_model.joblib      # Trained KNN model
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

```

* * * * *

⚖️ Features
-----------

-   Draw digits (0--9) in a canvas with finger/mouse

-   Select between **SVM** or **KNN** classifier

-   Extracts **HOG features** from drawings

-   Predicts the digit in real-time

-   Easy to use and fully local app

* * * * *

📦 Requirements
---------------

-   Python 3.7+

-   Streamlit

-   OpenCV

-   scikit-learn

-   scikit-image

-   streamlit-drawable-canvas

-   joblib

-   numpy

* * * * *

⚙️ Installation & Setup
-----------------------

### Step 1: Clone the Repository

```
git clone https://github.com/yourusername/digit_recognition_app.git
cd digit_recognition_app

```

### Step 2: Create and Activate Virtual Environment (recommended)

#### For Windows:

```
python -m venv venv
venv\Scripts\activate

```

#### For macOS/Linux:

```
python3 -m venv venv
source venv/bin/activate

```

### Step 3: Install Requirements

```
pip install -r requirements.txt

```

* * * * *

🧠 Add Trained Models
---------------------

Ensure the following trained models are saved in the `models/` folder:

```
from joblib import dump

# After training
dump(svm_model, 'models/svm_model.joblib')
dump(knn_model, 'models/knn_model.joblib')

```

* * * * *

🚀 Run the App
--------------

```
streamlit run app.py

```

The app will launch in your browser. You can draw Hindi digits and see the prediction in real-time.

* * * * *



📌 Example Output
-----------------

![Canvas Example](https://i.imgur.com/sOMEImage.png)\
*Drawn digit with prediction using HOG + SVM*

* * * * *

🧑‍💻 Author
------------

-   👨‍🎓 Dhananjay Chandel

-   🔗 [LinkedIn](https://www.linkedin.com/in/your-profile/)

-   💼 Project for academic/portfolio usage

* * * * *

