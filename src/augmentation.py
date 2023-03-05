# Importing necessary library 
import Augmentor 
# Passing the path of the image directory 
p = Augmentor.Pipeline("Augmented_image") 
  
# Defining augmentation parameters and generating 5 samples 
p.flip_left_right(0.5) 
p.black_and_white(0.1) 
p.rotate(0.3, 10, 10) 
p.skew(0.4, 0.5) 
p.sample(8) 