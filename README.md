# FNOclass

Seismic event classification with a lightweight Fourier Neural Operator model (FNO).

## Overview

This repository contains the implementation of a lightweight deep learning model for seismic event classification based on the Fourier Neural Operator (FNO). The method is designed for efficient and accurate classification of seismic waveforms, particularly in resource-constrained and real-time monitoring environments.

The model achieves competitive performance with significantly fewer parameters compared to conventional deep learning architectures, making it suitable for deployment in microseismic monitoring workflows.

## Related Publication

**Ayrat Abdullin, Umair Bin Waheed, Leo Eisner, Abdullatif Al-Shuhail**
*Seismic event classification with a lightweight Fourier Neural Operator model*
Geophysical Prospecting (EAGE)

[Link to paper (to be added)]

If you use this repository, please cite the paper.

## Key Features

* Lightweight architecture (~34k parameters)
* High classification accuracy (F1 ≈ 0.95–0.98 depending on dataset)
* Efficient training and inference
* Suitable for real-time and edge deployment
* Robust performance under limited training data

## Method Summary

The model uses Fourier Neural Operator layers to process seismic waveforms in the frequency domain. Unlike standard CNNs, which rely on local convolutions, FNO performs global spectral convolutions, enabling efficient capture of long-range temporal dependencies.

Input:

* 3-component waveform (E, N, Z)
* Fixed-length time window (e.g., 60 seconds)

Output:

* Probability of seismic event presence (binary classification)

## Repository Structure

```
FNOclass/
│── models/           # Model architecture and layers
│── training/         # Training scripts
│── inference/        # Inference / prediction scripts
│── data/             # Data handling utilities
│── notebooks/        # Example notebooks
│── utils/            # Helper functions
│── README.md
│── LICENSE
```

## Installation

Clone the repository:

```bash
git clone https://github.com/ayratabd/FNOclass.git
cd FNOclass
```

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Training

```bash
python training/train.py --config configs/default.yaml
```

### Inference

```bash
python inference/predict.py --input path/to/waveform
```

## Data

### Public Dataset

This work uses the **STEAD dataset**, a large-scale global dataset of seismic waveforms.

### Microseismic Dataset

The field microseismic dataset used in the study is **not publicly available** due to licensing restrictions but may be obtained from the data provider upon request.

## Results

| Dataset      | F1 Score |
| ------------ | -------- |
| STEAD        | ~0.95    |
| Microseismic | ~0.98    |

The model demonstrates strong generalization and maintains high performance even with limited training data.

## Reproducibility

* Training details and hyperparameters are provided in the paper
* Example configs are included in `configs/`
* Random seeds can be fixed for deterministic results

## Citation

```bibtex
@article{abdullin2026fno,
  title={Seismic event classification with a lightweight Fourier Neural Operator model},
  author={Abdullin, Ayrat and Waheed, Umair Bin and Eisner, Leo and Al-Shuhail, Abdullatif},
  journal={Geophysical Prospecting},
  year={2026}
}
```

## License

This repository is licensed under the MIT License.

## Notes on Paper Usage

The published journal article is subject to copyright by the publisher. Please refer to the official publication for the final version. Do not redistribute the publisher PDF unless permitted.

## Contact

Ayrat Abdullin
King Fahd University of Petroleum and Minerals
Email: [g202203180@kfupm.edu.sa](mailto:g202203180@kfupm.edu.sa)

---

## Acknowledgements

* STEAD dataset
* SeisBench
* Open-source ML ecosystem (PyTorch, NumPy, etc.)
