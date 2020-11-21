# Target language independent Wikipedia Article Generation for Schools and Hospitals
#### IRE Major Project

This repository contains the code to generate articles for popular schools and hospitals in indian languages like Hindi, Marathi and Telugu.

The Final_report.pdf file explains the architecture in detail and contans all the relevant links. (in order to access the links please use some other document viewer and not Github's default) <br>

The 'Hospital' directory contains the code to generate articles for hospitals and the schools directory contains the same for schools. 
These directories also contain the templates that the script uses to generate the final articles


## Generating templates 

In order to generate a new template or to expand an old one the user just needs to edit the file named 'language'\_Template.txt, where 'language' is the name of the language in which the template is writte. <br>
The format of the template is keyname followed by any number of variations of writing that sentence. _$key_ is used as the place holder for the values fetched from the data  <br>


## Running the script 
In order to change the language of the output articles, just make change the  <b> lanaguage </b>, the <b> script </b> and the <b> language code </b> in the notebook to the desired language. Make sure that a template file corresponding to that language exists in the execution folder. <br>
Just run all cells of the python notebook to generate the required articles. The user can generate articles for a given id, district, state and so on. 

## Contributing 
You can contribute by adding templates in other languages apart from hindi. Marathi and Telugu. In order to do that you can simply have a look at any of the existing templates for school or hospital and translate the template sentences in your own language, or find new ways of conveying the same information in your own language. <br>
You can also contribute by adding to the data of hospitals by adding relevant fields to the csv file, or filling up the sparse fields. <br>
The project can also be expanded by finding data for other domains like relegious places etc and generating those articles. 


