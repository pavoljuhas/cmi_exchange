#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from diffpy.Structure import loadStructure
from diffpy.srreal.pdfcalculator import PDFCalculator
from matplotlib.pyplot import plot, draw, show

UISO = 0.0005

# load BaTiO3 structure and set all ADPs to the same isotropic value
batio3 = loadStructure('BaTiO3.cif')
batio3.anisotropy = False
batio3.Uisoequiv = UISO

# calculate FWHM of a Gaussian profile for independent ADPS at UISO
FWHM = 2 * np.sqrt(2 * np.log(2)) * (2 * UISO)
# the closest square pulse to Gaussian profile seems at the following width
PWIDTH = 2 * FWHM

# standard PDF calculator
pdfc0 = PDFCalculator(qmax=25, rstep=FWHM)
r0, g0 = pdfc0(batio3)

# PDF calculator configured for pulse profile function
from pulseprofile import PulseProfile
pdfc1 = PDFCalculator(qmax=25, rstep=FWHM)
pdfc1.peakprofile = PulseProfile()
pdfc1.pulsewidth = PWIDTH
r1, g1 = pdfc1(batio3)

plot(r0, g0, r1, g1, hold=False)
draw()
show()
