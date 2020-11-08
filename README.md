# PhysicsHackathon_2020
CFHT Challenge, Hackathon 2020
Sneha Nair, Félix St-Denis, Patrick Horlaville


In order to generate the output asked, our idea was to make use of a scipy function that is able to find peaks in signals.
We used two parameters of that function:
  1) the minimum value required for a point to be considered a maximum ("height")
  2) the minimum amount of data points between each peak ("distance")
  
For the emission lines, we consider the appropriate array of 213,542 entries for the various intensities corresponding to wavelengths roughly between 400nm and 1000nm.
We let the function run on that array with a "height" of 20 and a "distance" of 10,000
(Note that these values were selected after testing for a few other values. They were selected for they strictly outputed the most obvious peaks and hence represented a reasonable set of parameters for this situation. For example, if we noticed too much noise points were selected as peaks, we would increase the "height" parameter. If we noticed that two very close points on the graph were selected for a peak, we would increase the "distance" parameter).
The function computes the needed peaks' intensity values corresponding to some specific wavelength. Each couple (wavelength, intensity) is denoted.

We repeat the same for the absorbtion lines, except for this: we do not consider this time the intensities themselves, but minus the intensities. Indeed, for the absorbtion lines, we are looking for the minimums. Visually, we are flipping the graph (symmetry with respect to the y=0 axis) so now all the absorbtion lines are the maximum of this new distribution. So looking for the maximums of the distribution (wavelengths, -intensities) will output the absorbtion lines.

The procedure is the same, we apply our function, and we are able to retrieve the needed peaks coupled to their wavelength.

We display at the end the graphs of the distribution for both objects PN M1-46 & gam CrA A with the peaks for emission & absorbtion lines displayed.
We also display the values of each emission & absorbtion line (each couple (wavelength, intensity)).

