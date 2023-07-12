# Ruphoria NLP Suite

This repository is an advanced suite of text preprocessing and cleaning algorithms, suitable for complex NLP analysis and modeling work. The architecture is versatile and allows easy configuration using config files, for instance, [`configs/cleaning/default.yml`](configs/cleaning/default.yml).

# Modules

### Document preprocessing and cleaning

Our primary data sources are PDF and text documents. We have crafted a suite of preprocessing and cleaning modules to convert these documents into forms that can be efficiently used by our models. The operations performed by our pipeline are as follows:
- Convert pdf to text
- Parse the text document and perform sentence tokenization.
- Lemmatize the tokens and remove stop words.
- Drop all non-alphabetical tokens.
- Apply spell check and try to recover misspelled words.
- Normalize tokens by converting to lowercase.

### Phrase detection

The preprocessing stage also includes phrase detection in the documents. Phrases are logical groupings of tokens signifying a distinct meaning. Primarily, we use the [Gensim](https://radimrehurek.com/gensim/) NLP toolkit and Spacy to develop the phrase detection algorithms.

### Acronym detection

Acronyms are prevalent in documents from development organizations and multilateral development banks. Therefore, our pipeline includes an acronym detector and expander which detects acronyms in a document and replaces them with the appropriate expansion.

Moreover, we maintain a log of multiple instances of an acronym and generate prototypes for each instance that encode the acronym information, for example, PPP -> private-public partnership or purchasing power parity.