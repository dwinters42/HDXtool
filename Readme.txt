            HDXtool.py: peak extraction from Mass Spectra
            =============================================

This little program semi-automatically fits the exact position and
abundance of peaks belonging to the same fragment in e.g. top-down MS
spectra of proteins and can be used for a variety of other purposes,
like extracting exact centroid masses for Hydrogen-Deuterium-Exchange
(HDX) experiments.

For questions or in case of problems please contact me at
daniel@tydirium.org.

1 Downloads 
~~~~~~~~~~~~

The latest version 1.0 can be downloaded from [here].


[here]: http://www.tydirium.org/daniel/downloads/HDXtool/HDXtool-1.0.zip

2 Installation 
~~~~~~~~~~~~~~~

Prerequisites: You will need the [Python interpreter] and the following
Python modules: 

- [py-yaml]
- [wxPython]
- [matplotlib]
- [SciPy]

After having these installed, just run the HDXtool.py script.


[Python interpreter]: http://www.python.org
[py-yaml]: http://pyyaml.org/
[wxPython]: www.wxpython.org
[matplotlib]: http://matplotlib.sourceforge.net/
[SciPy]: http://www.scipy.org

3 Usage 
~~~~~~~~

The workflow is like this:

1. Load a datafile containing comma separated XY mass spectrum,
   e.g. like the included "test.dat" (which is an oversimplified
   example). This loads the file and pops up a window showing the
   spectrum.
2. Next, press the "Region Of Interest" (ROI) button and click on
   three points in the spectrum plot to define the baseline
   (everything over the baseline will be searched for peaks), the left
   boundary for the search and finally the right boundary of the
   fragment you want to work on. You will get three lines in the
   spectrum plot.
3. Press "Suggest" and then click on the highest peak in the fragment
   series, which will be fitted and the fit will show in a new window.
4. Click on the next peak to the right or left of the main peak, which
   will be fitted again.
5. The program will now try to find all peaks belonging to the
   fragment, fit them and mark the position in the spectrum
   plot. Finally, it will show the fitted curves in a new window.
6. If you like the fit, press "Accept" and the peaks will be memorized
   by the program. A line in the main window shows the centroid mass
   and position and charge state.
7. By right-clicking on a line you can delete a fragment, add a
   comment or copy the selection to the clipboard for e.g. pasting
   into Excel.
8. Finally, pressing the "Save button" will generate a text file in
   YAML format with all the fitdata. The next time the data file is
   openend, the fitdata is imported as well.

4 Data format 
~~~~~~~~~~~~~~

The fitdata is saved in a special text format called YAML that is
human-friendly and contains the fitted data for all fragements:

- lower boundary ("low")
- high boundary ("high")
- Baseline ("thres") 
- Centroid mass ("centroid")
- Charge state ("charge state")
- the actual peak fitdata ("peaks")
