# Search Engine Usage
  As mentioned in Setup the search page can be accessed by http://127.0.0.1:5000/ url.

  Search provides two sort opetions
  1. Search by Relevance - User enters Question in the text box and select Search by Relevance and submits
     As seen below Answer titles with the relevant SO user scores mentioned in lables are displayed. Answers are sorted out by Relevance as determined by OkapiBM25 algorithm.
     Clicking any of the Answer title reveals full answer text

    [logo]: ''

  2. Search by Answer Score - User enters Question and select Search by Answer Score checkbox and submits. All answered are displayed as mentioned above, however they are sorted by SO answer scores. OkapiBM25 is used to first search the most relevant answers and then they are sorted by answer scores  
    [logo]: ''
