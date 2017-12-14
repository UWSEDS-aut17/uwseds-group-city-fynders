# Component Design

## 1. Data Processing:

- What it does. This component will import all four categories of city information into panda frame and get the longitude and latitude of the cities. After that, it do all the city ranking based on our ranking method to create a totally new rank file, which only contains the ranking information.
- Name: Data Processing
- Inputs: four csv file
- Outputs: `rank_file.csv` file that contains all the ranking information
- How it works
    + import panda to create new data frame
    + use rank(ascending) to rank cities based on different factor
    + use geopy to find the exact latitude and longitude for each city
    + save to csv file


## 2. User Interface:

- What it does: An off line webpage to provide some introduction about our design and also provides some buttons to help users to see our default results. They can also do their choice about what factors they care about.
- Name: User Interface
- Inputs: a matrix with two columns, first column is the name showed in the drop down setting, the other one is the name of the columns in the panda frame.
- Outputs: an off line webpage with the information we want.
- How it works:
    + use html.Div to classify divisions for each component
    + set up callbacks between buttons and their relative graphs


## 3. Plot on US map
- What it does: After user making choice, the webpage generates the graph based on the choice.
- Name: Plot on map
- Inputs: The button user choose and also rank csv file.
- Outputs: The relative US graph based on what user choose
- How it works:
	  + create a specific ranking panda data frame based on what users choose
    + use plotly to set up to dict, one is a list of cities and the other one is the layout of the US graph

## The whole process are shown below
  <img width="588" alt="component" src="https://user-images.githubusercontent.com/32401811/33976735-e2bb007e-e04b-11e7-82eb-7dbfc2037c51.PNG">
