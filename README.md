# The-Whether

In this program :

> We import and open a file
> Appends additional data to the file
> reads from the file to displays each city name and month average high temperature in Celsius


# Output: The output should resemble the following

  * City of Beijing month ave: highest high is 30.9 Celsius
  * City of Cairo month ave: highest high is 34.7 Celsius
  * City of London month ave: highest high is 23.5 Celsius
  * City of Nairobi month ave: highest high is 26.3 Celsius
  * City of New York City month ave: highest high is 28.9 Celsius
  * City of Sydney month ave: highest high is 26.5 Celsius
  * City of Tokyo month ave: highest high is 30.8 Celsius
  * City of Rio De Janeiro month ave: highest high is 30.0 Celsius


## There are two ways to doing this program

* import the file into the Jupyter Notebook environment
  - (use !curl to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv as mean_temp.txt)
  - Open the file in a+ mode, then do require changes
   ```
    file=open('mean_temp.txt','a+')
   ```

* Or we can create the file manually
  - Create the file
  - Write data into the file
  - And then format those data as require Output
  - In this case we can do it without using jupyter Notebook  
