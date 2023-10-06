# Improving Models for Health-Related Social Media Text Classification

This was developed as part of a team project working together with Daniel Song.

Our goal was to see if we could improve text classification for health data retrieved from social media. For this project, we focused on improving the classification of the NPMU dataset. For our benchmark, we used the score F1 score of 64.9 which was the highest score for this dataset in recent research (Guo, Y.; Ge, Y.; Yang, Y.-C.; Al-Garadi, M.A.; Sarker, A. Comparison of Pretraining Models and Strategies for Health-Related Social Media Text Classification. Healthcare 2022, 10, 1478. https://doi.org/10.3390/healthcare10081478). 

We were able to consistently obtain an F1 score above 95, with 96.1 being our highest score. To obtain this improvement, we used different data-cleaning methods that the authors and custom learning rates and epochs. We used multiple pre-trained models and found the most success with Bert, though all models performed better than or equivalent to that from the research paper.

To run the models, simply run the associated ipynb file. Be aware that the models will try to take more than 12 GB of RAM if you are running them in colab it may crash.
