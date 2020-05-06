# General Info
This API generates the relative importance of words in a text snippet. The
algorithm represents the input text as an undirected graph and computes
 the normalized centrality measure of each word.

# Setup
In order to run this toy API follow the steps outlined below. 

1. Clone the repository: 
   ```
   https://github.com/FyzHsn/graph-tools-api.git
   ```

2. Build & run docker image in the `graph-tools-api` folder via.
   ```
   docker build -t graph_api:latest .
   docker run -p 5000:5000 graph_api:latest
   ```
3. Type in `http://0.0.0.0:5000/api/v1/centrality?text=[Your Document]` in
 the browser to find the results. 


# Code Example
`http://0.0.0.0:5000/api/v1/centrality?text=""Physics is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force. Newton's laws connect force, space and time and motion."` 
 
The request above will lead return the following json object:
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
 
