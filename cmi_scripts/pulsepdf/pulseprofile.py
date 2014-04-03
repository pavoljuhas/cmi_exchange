#!/usr/bin/env python

from diffpy.srreal.peakprofile import PeakProfile


class PulseProfile(PeakProfile):
    '''PDF profile function for a Dirac-like square profile.

    pulsewidth   -- width of the pulse function
    '''

    _pulsewidth = 0.05

    def __init__(self, *args, **kwargs):
        PeakProfile.__init__(self, *args, **kwargs)
        self._registerDoubleAttribute('pulsewidth')
        return

    @property
    def pulsewidth(self):
        return self._pulsewidth

    @pulsewidth.setter
    def pulsewidth(self, value):
        if value != self._pulsewidth:
            self.ticker().click()
        self._pulsewidth = value

    # overloads from the base class

    def __call__(self, x, fwhm):
        halfpulse = 0.5 * self.pulsewidth
        if -halfpulse < x <= +halfpulse:
            return 1.0 / self.pulsewidth
        return 0.0

    def clone(self):
        import copy
        return copy.copy(self)

    def create(self):
        return PulseProfile()

    def type(self):
        return 'pulseprofile'

    def xboundhi(self, fwhm):
        return +0.5 * self.pulsewidth

    def xboundlo(self, fwhm):
        return -0.5 * self.pulsewidth

PulseProfile()._registerThisType()
