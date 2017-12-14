# Which city would you like to live in ?
----
## How to install and run cityfynders:
1. For mac, navigate (`cd`) to the location you would like to copy the `cityfynders`
package; for Windows, we recommend you to install [Anaconda]
(https://www.anaconda.com/download/#macos) `cd` through the terminal in the conda.

2. Clone the `cityfynders` by typing the following code in terminal:

~~~
git clone https://github.com/UWSEDS-aut17/uwseds-group-city-fynders.git
~~~

3. In the `uwseds-group-city-fynders` directory, initiate the setup
(it will automatically install the packages if you do not have them):

~~~
python setup.py develop --user
~~~

4. Run the script to generate webpage-based UI server:

~~~
python ./scripts/city_script.py
~~~

5. Copy the following url in the browser:

~~~
http://127.0.0.1:8050/
~~~

If your terminal shows the different url, copy that one.

## Successfully installed? Now let's explore and have fun!

<p align="center">
  <img src="https://user-images.githubusercontent.com/32367015/33974699-ad81a730-e03e-11e7-810e-852879c37093.PNG">
</p>

----

## What you can do from the interface of cityfynders?

1. Check some default ranking:

   Click the any of the 5 buttons to have an exploration.

   <p align="center">
     <img src="https://user-images.githubusercontent.com/32367015/33974958-5a345ed6-e040-11e7-8c79-9e69f9dfea09.png">
   </p>

   The expecting outputs will be (Don't forget to try the multiple functions!):

   If you try 'Total Rank' (you can hover to check the detailed ranking information
   for each city)

   <p align="center">
     <img src="https://user-images.githubusercontent.com/32367015/33975693-10723b2e-e045-11e7-9d47-72350b9d3b53.png">
   </p>

2. DIY the ranking yourself:

   Select your first, second...fifth care factors, let's try 'Fewer Crime', 'Air Quality',
   'Water Quality', 'Employment Rate', 'Restaurants':

   <p align="center">
     <img src="https://user-images.githubusercontent.com/32367015/33975535-05f5a24a-e044-11e7-980c-940e768a74bf.png">
   </p>

   Now here's the DIY results:

   <p align="center">
     <img src="https://user-images.githubusercontent.com/32367015/33975703-2552063c-e045-11e7-9ae4-f24d7256bbd3.png">
   </p>

   If you can choose the same care factors if you just care some of them also

3. See the correlation graph


   If you want to know the correlation between the chosen factors, we also draw
   the correlation matrix:

   <p align="center">
     <img src="https://user-images.githubusercontent.com/32367015/33975811-f1e32898-e045-11e7-94aa-ae79af32b164.png">
   </p>
