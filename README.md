<h1 align="center">
  <img src="Assets/Image README.jpg" alt="Heading photo">
</h1>
<h2 align="center">Color Palette Classifier </h2>

  <p align="center">
    Find dominant colors from given image using Unsupervised Learning Algorithm.
    <br />
    <br />
    <a href="https://github.com/BeholdenArt/Color-Palette-Classifier/issues">Report Bug</a>
    ·
    <a href="https://github.com/BeholdenArt/Color-Palette-Classifier/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<br />
<details open="open">
  <summary><h2 style="display: inline-block">TABLE OF CONTENTS</h2></summary>
  <ol>
    <li>
      <a href="#ABOUT-THE-PROJECT">ABOUT THE PROJECT</a>
      <ul>
        <li><a href="#Demo">Demo</a></li>
        <li><a href="#Built-with">Built With</a></li>
      </ul>
    </li>
      <a href="#GETTING-STARTED">GETTING STARTED</a>
      <ul>
        <li><a href="#Prerequisite">Prerequisite</a></li>
        <li><a href="#Installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#USAGE">USAGE</a></li>
    <li><a href="#CONTRIBUTION">CONTRIBUTION</a></li>
    <li><a href="#CONTACT-ME">CONTACT ME</a></li>
  </ol>
</details>


<br><br><br>
<!-- ABOUT THE PROJECT -->
## ABOUT THE PROJECT

<p align="center">
     <h4>  
       We uses K-Means Clustering to classify dominant colors from an image based on k value given by the user and represent those dominant colors into piechart. 
       This project has 2 files (addons.py and "palette extractor.py"). Addon contains all the functions required to run the algorithm and "Palette Extractor" contains all the           streamlit web client stuffs along side with classification model and exception handling. 
    </h4>
<br>
<h4>
      K Means Clustering algorithm is used in this project to cluster out dominant colors from a image.
      The K-means algorithm in data mining starts with a first group of randomly selected centroids, which are used as the beginning points for every cluster, and then performs         iterative (repetitive) calculations to optimize the positions of the centroids
 </h4>
 <br>
 <h4>
      It halts creating and optimizing clusters when either:
  <ul>
        <li>The centroids have stabilized — there is no change in their values because the clustering has been successful.</li>
    <li>The defined number of iterations has been achieved.</li>
  </ul> 
 </h4>
</p>
<br />

## Demo 

https://user-images.githubusercontent.com/50458157/138034031-fdce342c-be61-45d1-a18a-c5a65c8aafe8.mp4





<!-- BUILT WITH -->
## Built-with
<ol>
  <li> <a href="https://streamlit.io/" target="_blank">Streamlit</a> - For creating web application. </li> 
  <li> <a href="https://scikit-learn.org/" target="_blank">Sklearn</a> - For Unsupervised Learning Algorithm. </li> 
  <li> <a href="https://matplotlib.org/" target="_blank">Matplotlib</a> - Used to plot pie chart of dominant colors. </li>
  <li> <a href="https://numpy.org/" target="_blank">Numpy</a></li> 
  <li> <a href="https://webcolors.readthedocs.io/en/1.11.1/" target="_blank">Webcolors</a> - Used to convert RGB to HEX CODE and COLOR NAME. </li> 
  <li> <a href="https://www.scipy.org/" target="_blank">Scipy</a> - For KDTree </li> 
  <li> <a href="https://python-pillow.org/" target="_blank">Pillow</a> - To get the image from the user. </li> 
</ol>
  <br>



<br><br><br>
<!-- GETTING STARTED -->
## GETTING STARTED

<!-- PREREQUISITE -->
## Prerequisite 
<p align="left" > 
    &emsp;
   <a href="https://www.python.org" target="_blank"><img alt="Python" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreene">
  </a>
  &emsp; 
    <a href="https://www.scipy.org/" target="_blank"><img alt="Scipy" src="https://img.shields.io/badge/SciPy-654FF0?style=for-the-badge&logo=SciPy&logoColor=white"></a>
  &emsp;
  </a> 
    <a href="https://numpy.org/" target="_blank"><img alt="Numpy" src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white"></a>
  </a> 
  &emsp;
  <a href="https://streamlit.io/" target="_blank"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"></a>
  &emsp;
  </a>
  <a href="https://scikit-learn.org/" target="_blank"><img alt="Scikit Learn" src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"></a>
  &emsp;
  </a>
</p>

<br>


<!--INSTALLATION -->
## Installation
<ol>
  <li> Clone the repo </li>
  
   ```sh
   git clone https://github.com/BeholdenArt/Color-Palette-Classifier.git
   ```
  
  <li> Install requirements </li> 
  
  ```sh
   pip3 install -r requirenments.txt
   ```
  
</ol>



<br><br><br>
<!-- USAGE -->
## USAGE

To use this project.
*  Complete the getting started part. </li>
*  To run the web application
    ```
    streamlit run "palette extractor.py"
    ```


<br><br><br>
<!-- CONTRIBUTING -->
## CONTRIBUTION
Please refer to each project's style and contribution guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!



<br><br><br>
## CONTACT ME

<p align="center">
	<a href="mailto:priyanshub5645@gmail.com"><img src="https://img.icons8.com/bubbles/50/000000/gmail.png" alt="Gmail"/></a>
	<a href="https://github.com/BeholdenArt"><img src="https://img.icons8.com/bubbles/50/000000/github.png" alt="GitHub"/></a>
	<a href="https://linkedin.com/in/priyanshu-bairwa-827432190"><img src="https://img.icons8.com/bubbles/50/000000/linkedin.png" alt="LinkedIn"/></a>
	<a href="https://www.facebook.com/priyanshu.bairwa.129794"><img src="https://img.icons8.com/bubbles/50/000000/facebook-new.png" alt="Facebook"/></a>
	<a href="https://instagram.com/theblockedguy"><img src="https://img.icons8.com/bubbles/50/000000/instagram.png" alt="Instagram"/></a>
	
</p>
