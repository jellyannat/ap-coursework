Detecting a seizure from EEG data using entropy

The idea for the project was to produce a program that estimates entropy of signal amplitude
distribution. The function "histogram" aims to estimate a histogram of the signals, which is 
used by the "entropy" function to calculate the entropy of the histogram. The idea for this 
project can be found at this link: http://www.cs.rug.nl/~rudy/matlab/doc/entropy.html.

I was unable to produce a function that calculates the entropy of a histogram of signals,
although I have kept the attempted entropy function commented out within the script.


Prerequisites:
You will need to install these things in order to run the code successfully:
import numpy as np

Example of use:
The example used in my code contains EEG recordings at 6 electrodes from a patient with focal
epilepsy, recorded during an invasive pre-surgical epileptic episode with a 256 Hz sampling rate.
Running the code will output the result a result vector of the first trace and the descriptor.


Aims for future work:
I would aim to have fixed the entropy function to be able to output the calculated entropy for each 
histogram. I would then use a moving-window technique in order to estimate entropy over specified 
window sizes. I also wanted to produce figures of the traces for visualisation, as well as visualise the
entropy of the EEG traces in a single figure.


Versioning
GitHub was used for versioning. To see available versions and a copy of this README file, the
repository can be found at https://github.com/jellyannat/ap-coursework

