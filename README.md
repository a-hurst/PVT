# PVT

The Psychomotor Vigilance Task (PVT) is a paradigm for measuring vigilence and fatigue, first developed by [Dinges and Powell (1985)](https://link.springer.com/article/10.3758/BF03200977). This experiment program is an implementation of this task using the KLibs framework, based on the methods section of [Drummond el al. (2005)](https://academic.oup.com/sleep/article/28/9/1059/2708157).

![PVT_animation](klibs_pvt.gif)


## Requirements

This version of the PVT is programmed in Python 2.7 (3.3+ compatible) using the [KLibs framework](https://github.com/a-hurst/klibs). It has been developed and tested on macOS (10.9 through 10.13), but should also work with minimal hassle on computers running [Ubuntu](https://www.ubuntu.com/download/desktop) or [Debian](https://www.debian.org/distrib/) Linux, as well as on computers running Windows 7 or newer with [a bit more effort](https://github.com/a-hurst/klibs/wiki/Installation-on-Windows).

## Getting Started

### Installation

First, you will need to install the KLibs framework by following the instructions [here](https://github.com/a-hurst/klibs).

Then, you can then download and install the experiment program with the following commands (replacing `~/Downloads` with the path to the folder where you would like to put the program folder):

```
cd ~/Downloads
git clone https://github.com/a-hurst/PVT.git
```

### Running the Experiment

This version of the PVT is a KLibs experiment, meaning that it is run using the `klibs` command at the terminal (running the 'experiment.py' file using python directly will not work).

To run the experiment, navigate to the PVT folder in Terminal and run `klibs run [screensize]`,
replacing `[screensize]` with the diagonal size of your display in inches (e.g. `klibs run 24` for a 24-inch monitor).

If you just want to test the program out for yourself and skip demographics collection, you can add the `-d` flag to the end of the command to launch the experiment in development mode.

### Exporting Data

To export data from the PVT task, simply run

```
klibs export
```
while in the root of the PVT directory. This will export the trial data for each participant into individual tab-separated text files in the project's `ExpAssets/Data` subfolder.
