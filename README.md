# FCW model

Python library and Julia script to simulate the Flexible Chain Walker (FCW) model.

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
- `folder` : (string, optional) - Folder name to save output files. Default: None
- `save_anim` : (boolean, optional) - Save the displayed animation. Default: False

## Julia script

Two simulation functions have been implemented: `single_density(L, N, l, t, folder="Data")` and `several_densities(L, l, t, eq_t, times, densities, folder="Data")`

Just execute the self.assembling_chains.jl file or the Jupyter notebook with the desired function activated

# Examples

## Python simulation

## Python animation

## Julia simulation

# Authors
* **A. Giménez-Romero**

# License
This project is licensed under the GNU General Public License - see the [LICENSE.md](https://github.com/agimenezromero/FCW-model/blob/master/LICENSE) file for details

# References
1. [Takashi Mashiko. “Irreversible aggregation of flexible chainlike walkers without adherence”.In:Phys. Rev. E78 (1 July 2008), p. 011106.](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.78.011106)
