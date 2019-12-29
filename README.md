# FCW model

Python library and Julia script to simulate the Flexible Chain Walker (FCW) model.

The python library can be useful to perform simulations for a single density and plot animations. To reproduce the results in reference <sup>1</sup>, which involve simulations for several densities, python is not efficient. For this purpose the model has been implemented also in Julia, which is a fast compiled programming language.

# Overview

The flexible chainlike walker (FCW) model was presented in 2008 by Takashi Mashiko, from the department of Mechanical Engineering of Shizuoka University. The model is proposed as a minimal model of a deformable moving object and as an extension of the regular random-walk model. For more information about the model see reference. <sup>1</sup>

Table of contents
=================

<!--ts-->
   * [Overview](#overview)
   * [Table of contents](#table-of-contents)
   * [Requeriments](#requeriments)
   * [Documentation](#documentation)
       - [Python class](#python-class)
            - [Initialisation](#initialisation)
            - [Running simulations](#running-simulations)
       - [Julia script](#julia-script)
   * [Examples](#examples)

   * [Authors](#authors)
   * [License](#license)
<!--te-->

# Requeriments

Python 3 installed with the following libraries
- NumPy
- Matplotlib

Julia 1.0.4 installed with the following libraries
- Statistics
- Plots

# Documentation

## Python class

### Initialisation

To initialise the available Python class (`FCW_model`) the following parameters must be passed in:

- `L` (int) - Lattice length.
- `l` (int) - FCW length (nº of particles that conform a FCW)
- `rho` (float) - Density of FCW's

### Running simulations

There are 2 ways to run simulations for each of the classes previously mentioned: `simulate(t, folder)`, `animate(t, save_anim)`

- `t` (int) - Number of time steps to simulate.
- `folder` : (string, optional) - Folder name to save output files. Default: None.
- `save_anim` : (boolean, optional) - Save the animation instead of displaying it. Default: False.

## Julia script

Two simulation functions have been implemented: `single_density(L, N, l, t, folder="Data")` and `several_densities(L, l, t, eq_t, times, densities, folder="Data")`

- `L` (int) - Lattice length.
- `N` (int) - Number of FCW's.
- `l` (int) - FCW length (nº of particles that conform a FCW).
- `t` (int) - Number of time steps to simulate.

- `eq_t` (int) - Number of time steps to equilibrate and start computing average mobility.
- `times` (int) - Number of times to simulate for each density point.
- `densities` (array) - Density points to simulate.

- `folder` (string, optional) - Folder name to save output files. Default: "Data".

Just execute the self.assembling_chains.jl file or the Jupyter notebook with the desired function activated.

# Examples

## Python simulation

```python
from self_assembling import FCW_model

L = 100
l = 8
rho = 0.5

t = 10**4

foldername = 'l_%i' % l

model = FCW_model(L, l, rho)

model.simulate(t, folder=foldername)
```

## Python animation

```python
from self_assembling import FCW_model

L = 100
l = 8
rho = 0.5

t = 10**4

model = FCW_model(L, l, rho)

model.animate(t)
```

## Julia simulation

To perform a simulation with Julia the Jupyter-Notebook file or the .jl script file can be used. The Julia script can be run in background so that multiple simulations can be thrown at once.

To run the Julia script in background just type the following command in the bash

```bash
nohup self_assembling_chains.jl > outfile.out &
```

this will run the script in the background writting the print outputs in the outfile.out file. The "&" command will let the cmd window free.

# Authors
* **A. Giménez-Romero**

# License
This project is licensed under the GNU General Public License - see the [LICENSE.md](https://github.com/agimenezromero/FCW-model/blob/master/LICENSE) file for details

# References
1. [Takashi Mashiko. “Irreversible aggregation of flexible chainlike walkers without adherence”.In:Phys. Rev. E78 (1 July 2008), p. 011106.](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.78.011106)
