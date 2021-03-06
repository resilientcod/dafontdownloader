<img src="https://camo.githubusercontent.com/debb4136883d8a3585f83971f342da038183f627/68747470733a2f2f7777772e6461666f6e742e636f6d2f696d672f6461666f6e742e706e67" align="right">


dafontdownloader 0.5
=================

A python script to download fonts directly from [dafont](https://www.dafont.com/) site.

## What's new in 0.5

* Windows compatible

## Install

  

### First way

To avoid using `sudo`, installation requires these steps:

  

1. Use `pip` to install the package with all dependencies required:

  

* `pip install dafontdownloader --user`


*Obs: if you are on windows you don't need to perform the following steps*
  

2. Use `export` to persistent use of dafontdownloader script:

  

* `echo "export PATH=${PATH}:"$HOME"/.local/bin" >> "$HOME"/.bashrc`

  

3. Use `source` to start using script in command line:

  

* `source .bashrc`

  

### Second Way

1. Download this repository, or use `git clone https://github.com/resilientcod/dafontdownloader.git`

2. Open repository directory.

3. Use `python3 setup.py install`

4. Follow the steps 2 and 3, to persistent use of dafontdownloader script.



### Third Way (with `sudo`)

**Attention:** use at your own risk!



`sudo pip install dafontdownloader`



This allow install in `bin` directory, making it unnecessary to use steps 2 and 3 in the first way.

## Usage
After installation, type `dafontdownloader` in the terminal to verify that everything is correct,
as in the image:
![image](https://i.imgur.com/VRY4gNZ.png)

Then use: `dafontdownloader <name-font>` to download and install fonts from dafont site.

Example:

`dafontdownloader Nemesis Grant`

**Attention:** Make sure you type the name correctly!

## More info

The fonts are installed in the user's local `.fonts` directory

Enjoy!
