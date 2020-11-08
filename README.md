# PhysicsHackathon_2020
CFHT Challenge, Hackathon 2020
Sneha Nair, Félix St-Denis, Patrick Horlaville

* Please note, the code referred in this text is CFHT_Hackathon2020 *

In order to generate the output asked, our idea was to make use of a scipy function that is able to find peaks in signals (scipy.signal.find_peaks).
We used two parameters of that function:
  1) the minimum value required for a point to be considered a maximum ("height")
  2) the minimum amount of data points between each peak ("distance")

For the context of the challenge, we consider the two objects PN M1-46 & gam CrA A, whose spectra are given at https://www.cfht.hawaii.edu/~manset/Hackathon2020/

For the emission lines, we consider the appropriate array of 213,542 & 214,823 entries (for the two objects) for the various intensities of corresponding wavelengths roughly between 400nm and 1000nm.
We let the function run on that array with a "height" of 20 and a "distance" of 10,000.

* (Notice that these values were selected after testing for a few other values. They were selected for they strictly outputed the most obvious peaks and hence represented a reasonable set of parameters for this situation. For example, if we noticed too much noise points were selected as peaks, we would increase the "height" parameter. If we noticed that two very close points on the graph were selected for a peak, we would increase the "distance" parameter).
* (Notice also that you can change these parameters at line 34 of our code by entering the values you want)
* (Notice also that we have worked the solution for both objects with the same parameters for it would work well that way, but we could have chosen to use different parameters for both)

The function computes the needed peaks' intensity values corresponding to some specific wavelength. Each couple (wavelength, intensity) is denoted.

We repeat the same for the absorbtion lines, except for this: we do not consider this time the intensities themselves, but minus the intensities. Indeed, for the absorbtion lines, we are looking for the minimums. Visually, we are flipping the graph (symmetry with respect to the y=0 axis) so now all the absorbtion lines are the maximum of this new distribution. So looking for the maximums of the distribution (wavelengths, -intensities) will output the absorbtion lines.

The procedure is the same, we apply our function, and we are able to retrieve the needed peaks coupled to their wavelength.

The whole process is appliable to any similar set of data. The input of the data itself can be modified at lines 38 to 44

We display at the end the graphs of the distribution for both objects PN M1-46 & gam CrA A with the peaks for emission & absorbtion lines displayed.
We also display the values of each emission & absorbtion line (all couples (wavelength, intensity)).

