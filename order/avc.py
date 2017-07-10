###############################################################################
# -*- coding: utf-8 -*-
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT License
###############################################################################

from __future__ import division, print_function
from six.moves import range

import numpy as np

class VoronoiCell(object):
    """asphericity of the Voronoi cell"""
    def __init__(self):
        pass
    
    def compute_vc(self, planes):
        """compute the Voronoi cell"""
        #total area of all planes
        S = 0.0

        #total volume of Voronoi polyhedron
        V = 0.0

        #compute S and V
        for plane in planes:
           
            outter_p = 0.0
            for i in range(1, len(plane)-1):
                outter_p += np.linalg.norm(np.outter((plane[i] - plane[0]),
                                                     (plane[i+1] - plane[0])))

            vol = 0.0
            for i in range(1, len(plane)-1):
                vol += np.linalg.norm(np.dot(np.outter(plane[0], plane[i]),
                                             plane[i+1]))    
            outter_p *= 0.5
            vol *= 1 / 6
            S += outter_p
            V += vol

        #voronoi cell
        eta = S ** 3 / (36 * np.pi * V ** 2)

        return eta