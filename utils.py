import numpy as np
from scipy.signal import detrend

def process_traces(trace_list, h5_file, start_idx, output_array):
    
    """Helper to process and scale traces into the preallocated array."""
    
    for i, evi in enumerate(trace_list):
        
        # 1. Fetch data
        data = h5_file.get(f'data/{evi}')[()]
        
        # 2. Detrend (scipy.signal.detrend removes the linear trend and mean by default)
        # axis=0 processes each channel (E, N, Z) independently
        detrended = detrend(data, axis=0)
        
        # 3. Standard Scaling (Z-score)
        # Formula: (x - mean) / std
        mu = np.mean(detrended, axis=0)
        sigma = np.std(detrended, axis=0)
        
        # Update output_array in place
        output_array[start_idx + i] = (detrended - mu) / (sigma + 1e-10)
        
def create_labels(eq_list, noise_list):
    
    """
    Creates a label vector: 1 for earthquakes, 0 for noise.
    Matches the order of the data processing (EQs first, then Noise).
    """
    
    return np.concatenate((
        np.ones(len(eq_list), dtype=int),   # Label 1 for EQ
        np.zeros(len(noise_list), dtype=int) # Label 0 for Noise
    ))