import torch; 

if torch.cuda.is_available():
    print('GPU is available')
    print('Available GPU memory:', torch.cuda.get_device_properties(0).total_memory / 1024**2, 'MB')
else:
    print('GPU is not available')
