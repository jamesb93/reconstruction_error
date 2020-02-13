# How to run these scripts | 29 July 2019

## Understanding how the scripts are grouped

Each of these scripts performs a specific function. In some cases there are minor overlaps between them as they have been duplicated in order to analyse a different set of data, or work with a different format of inputs and inputs. This document will hopefully keep tabs on how they all work together so that this knowledge isn't lost somewhere down the line.

### Some things first...

- Any script marked with the prefix ```^``` are scripts that are meant for some creative rather than analytical purpose.

- Numbered scripts initially had a sense of order to them. This ordering was somewhat disrupted after essentia was included as the primary method of analysis.

### Explanation of the scripts.

1. 1_scrape.py is the script that converts any data file to audio using SoX.
2. 2_slice_and_explode.py is the script that performs novelty slicing on each of the audio files produced i 1_scrape.py
3. 3-6.py are analysis scripts using the FluCoMa CLI as the backend. These are largely made redundant by essentia
4. 7_nmf.py computes nmf in 3 components on each of the slices made by 2_slice_and_explode.py
5. 8_classification.py uses a classifier from sklearn to discern between 'bad' and 'good' samples. THe data used initially comes from the FluCoMA analysis. The classifier is set by commenting out and uncommenting the appropriate code.
6. 9_reduction.py is a breakpoint of sorts in the code base. This starts to represent where some meta-analysis occurs in looking for patterns in the overall data produced in previous scripts. This script performs a data reduction of the overall data set. Right now its not generic and there some duplications of the code that deal with different input sources (essentia vs flucoma) as well as intermediate forms (essentia post_processing) and outputs (wav and json)
