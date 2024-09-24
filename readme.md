# Author Identification in Persian Literature using Language Models

## Project Overview

This project focuses on identifying the authors of Persian literary texts using large language models, specifically BERT-based architectures. The dataset consists of works from 10 Persian poets, and the models are fine-tuned to classify the author of a given text.

The project consists of two main parts:

1. **Dataset Creation**: Web scraping Persian literary texts to create a balanced dataset.
2. **Author Identification**: Fine-tuning BERT models for the task of author classification.

## Dataset

- **Genre**: Persian Poetry
- **Authors**: 10 Persian poets
- **Documents per Author**: 30
- **Document Length**: 500 words
- **Tools**: `BeautifulSoup`, `Pandas`

### Dataset Details

For dataset creation, I scraped literary texts from online sources, ensuring that each document is representative of the poet's style. Metadata such as author name and text content is included.

## Models and Training

Three pre-trained models were fine-tuned using the `transformers` library:

1. `bert-base-multilingual-cased`
   - **Train Loss**: 0.0087
   - **Validation Loss**: 1.8457
   - **Train Accuracy**: 100%
   - **Validation Accuracy**: 70.14%

2. `xlm-roberta-base`
   - **Train Loss**: 0.3915
   - **Validation Loss**: 1.0959
   - **Train Accuracy**: 96.4%
   - **Validation Accuracy**: 67.01%

3. `distilbert-base-multilingual-cased`
   - **Train Loss**: 0.5000
   - **Validation Loss**: 1.5666
   - **Train Accuracy**: 95.51%
   - **Validation Accuracy**: 44.10%

All models were trained for 50 epochs.

## Experiments

The experiments were conducted with:

- 5-Fold Cross-Validation
- Performance Metrics: Accuracy, F1 Score, Precision, Recall
- Confusion Matrix for each model
- Hyperparameter tuning for learning rate, document length, and stopwords.

## Results

- The `bert-base-multilingual-cased` model outperformed the others with a validation accuracy of 70.14%.
- Fine-tuning parameters like learning rate had a significant impact on model performance.
- Longer document lengths and proper handling of stopwords also improved accuracy.

## Traditional Machine Learning Comparison

Traditional machine learning approaches (e.g., Naive Bayes, SVM) were explored, showing limitations in comparison to the language models.

## Conclusion

The BERT-based models proved effective for the author identification task. Future work could explore larger datasets and more complex language models to improve accuracy further.

## Libraries Used

- `pandas`
- `sklearn`
- `transformers`
- `torch`
- `matplotlib`
- `seaborn`
- `hazm`

## Acknowledgements

Special thanks to the open-source contributors of `transformers` and `BeautifulSoup` for the tools that made this project possible.
