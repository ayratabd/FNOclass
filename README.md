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

![FNO model architecture](docs/fno_model_figure.png)

**Figure:** Overview of the proposed Fourier Neural Operator (FNO) architecture for three-component seismic waveform classification. The input waveform is projected into a higher-dimensional feature space, processed by stacked 1-D FNO blocks, and mapped to a binary probability indicating seismic signal presence.

Input:

* 3-component waveform (E, N, Z)
* Fixed-length time window (e.g., 60 seconds)

Output:

* Probability of seismic event presence (binary classification)

## Repository Structure

```text
FNOclass/
│── FNOclass.ipynb      # Main notebook for preprocessing, training, evaluation, and inference
│── environment.yml     # Conda environment specification
│── docs/               # Figures and documentation assets
│── data/               # Data access instructions or lightweight metadata only
│── README.md
│── LICENSE
```

## Installation

Clone the repository:

```bash
git clone https://github.com/ayratabd/FNOclass.git
cd FNOclass
```

Create the conda environment:

```bash
conda env create -f environment.yml
conda activate fnoclass
```

This repository uses an `environment.yml` file because it is the most convenient way to reproduce the exact software stack for notebook-based scientific workflows, especially when PyTorch and scientific Python packages are involved.

If needed, a pip-based `requirements.txt` can be added later as a lightweight alternative, but `environment.yml` should be the primary installation path.

## Usage

Open the main notebook:

```bash
jupyter notebook FNOclass.ipynb
```

The notebook contains the full workflow, including:

* data loading and preprocessing
* model definition
* training
* validation and testing
* inference on waveform windows
* figure generation and result inspection

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

Figures included in this repository should be limited to material you are authorized to share. If you add the model figure from the paper, place the exported PNG in `docs/fno_model_figure.png` and include an appropriate citation or caption in this README.

## Contact

For questions, suggestions, or collaboration inquiries:

**Ayrat Abdullin**<br>
Department of Geosciences<br>
King Fahd University of Petroleum and Minerals<br>
Dhahran, Saudi Arabia<br>
Email: [g202203180@kfupm.edu.sa](mailto:g202203180@kfupm.edu.sa)

---

## Acknowledgements

* STEAD dataset
* SeisBench
* Open-source ML ecosystem (PyTorch, NumPy, etc.)



