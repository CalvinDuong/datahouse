# datahouse
Input: Json file that is passed in as the input data in the main function ; could also ask user for json file input using input() command 
Output: Json file as well 

## Schema to generate output 
We assume that all attributes are weighted equally when trying to compute a compability score (eg: intelligence and strength both have the same weight)
For each person on the team, we compuet the average attribute score for all the attributes they have. This value will be the average score for the team 

For each applicant, we want to rate those with similar attribute scores with higher compatability, as a result, we compare the average team score for each attribute, and compare it with the repsective attribute for the applicant for all the attributes. This is done by finding the percent similarity. Since similarity goes both ways, we divide the smaller attribute rating with the higher attribute rating giving us the percent of the average (this also ensure our values are between 0 and 1). We sum all the different attributes and divide it by the length of attributes to compute the overall compatability. 