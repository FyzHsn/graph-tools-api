# General Info
This API generates the relative importance scores of words in a given
document. The algorithm represents the input text as an undirected graph
and computes the normalized centrality measure of each word.
 
The normalized centrality score is computed by aggregating the number of
incoming edges to each word and normalizing the score by the remaining
number of nodes. Note that the stopwords and irrelevant parts of speech are
removed from the computation.

A document is comprised of a series of sentences punctuated by a period of
 question mark. For example,
```buildoutcfg
Physics is the natural science that studies matter, its motion and behavior 
through space and time, and the related entities of energy and force. Newton's
laws connect force, space and time and motion.
```

# Setup
In order to run this toy API, follow the steps below. 

1. Clone the repository: 
   ```
   https://github.com/FyzHsn/graph-tools-api.git
   ```

2. Build & run the docker image in the `graph-tools-api` folder via (Note
 that `pytest` is automatically run during the build process): 
   ```
   docker build -t graph_api:latest .
   docker run -p 5000:5000 graph_api:latest
   ```
3. Type in `http://0.0.0.0:5000/api/v1/centrality?text=[Your Document]` in
 the browser to see the importance score of each word in the document. 


# Code Example
`http://0.0.0.0:5000/api/v1/centrality?text=Physics is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force. Newton's laws connect force, space and time and motion.` 
 
The request above will return the following json object:
```buildoutcfg
[
  [
    "space", 
    0.31
  ], 
  [
    "time", 
    0.31
  ], 
  [
    "motion", 
    0.23
  ], 
  [
    "forc", 
    0.23
  ], 
  [
    "natur", 
    0.15
  ], 
  [
    "scienc", 
    0.15
  ], 
  [
    "studi", 
    0.15
  ], 
  [
    "behavior", 
    0.15
  ], 
  [
    "relat", 
    0.15
  ], 
  [
    "entiti", 
    0.15
  ], 
  [
    "energi", 
    0.15
  ], 
  [
    "law", 
    0.15
  ], 
  [
    "physic", 
    0.08
  ], 
  [
    "newton", 
    0.08
  ]
]
```
 
# References
1.  [Graph based text representations](http://www.lix.polytechnique.fr/~mvazirg/gow_tutorial_webconf_2018.pdf) 
 
