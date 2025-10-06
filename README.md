# EPS Sizing Tool

A Python tool for sizing the Electrical Power System (EPS) components of a spacecraft mission to Mercury.

## Overview

This tool calculates the required specifications for:

- **Solar Array**: Size, mass, and optimal incidence angle
- **Battery System**: Capacity, mass, and volume requirements
- **Power Control and Distribution Unit (PCDU)**: Mass and volume specifications

## Files

- [`main.py`](main.py) - Main script that runs the sizing calculations and displays results
- [`utils.py`](utils.py) - Core calculation functions for solar arrays and batteries
- [`constants.py`](constants.py) - Mission parameters, component specifications, and subsystem power requirements

## Usage

Run the sizing tool:

```bash
python main.py
```

The tool will output the complete EPS specifications including total mass and volume requirements.

## Mission Parameters

- **Target**: Mercury orbit mission
- **Duration**: 8.5 years (7.5 years + 1 year transfer)
- **Orbital Period**: ~2.1 hours around Mercury
- **Eclipse Fraction**: 28% of orbit in shadow

The tool accounts for solar flux differences between Earth and Mercury, solar array degradation over mission lifetime, and a combination of both batteries and supercapacitors. Furthermore, a different power consumption is assumed for the transfer flight in some of the subsystems.
