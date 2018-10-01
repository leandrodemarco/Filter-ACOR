#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 23:11:32 2018

@author: leandrodemarcovedelago

Corre la versión discreta pura del algoritmo
"""

import ACOR
import Utils

use_log = False # Change this flag to use logarithmic version
a = ACOR.Acor('DiscretoPuro', use_log)
u = Utils.Utils()

iterations_per_rval = 50
best_r1 = [11000., 3600., 36000., 12000., 3300.]
for R1 in best_r1:
    done = False
    for i in range(0, iterations_per_rval):
        if done:
            break
        print "Running iter %i for R1=%i" % (i, R1)
        best_sol = a.mainLoop(R1)
        r2, r3, c4, c5 = best_sol[0], best_sol[1], best_sol[2], best_sol[3]
        sens = u.get_sol_info(R1, r2, r3, c4, c5)[0]
        isSol = u.is_sol(R1, r2, r3, c4, c5)
        isSoftSol = u.is_soft_sol(R1,r2,r3,c4,c5)
        if (isSol):
            done = True
            print R1, r2, r3, c4, c5