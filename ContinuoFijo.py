#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:32:46 2018

@author: leandrodemarcovedelago
"""

import ACOR
import Utils

use_log = True # Change this flag to use logarithmic version
a = ACOR.Acor('DiscretoPuro', use_log)
u = Utils.Utils()

best_r1 = u.best_r1_sens
for R1 in best_r1:
    final_results = a.mainLoop(R1)
    best_sol = final_results[:-1]
    cost = final_results[-1]
    if (use_log):
        best_sol = Utils.exp_list(best_sol)
    r2, r3, c4, c5 = best_sol[0], best_sol[1], best_sol[2], best_sol[3]
    sens = u.get_sol_info(R1, r2, r3, c4, c5)[0]
    isSol = u.is_sol(R1, r2, r3, c4, c5)
    print R1, r2, r3, c4, c5
    print ('Es solucion' if isSol else 'No es solucion')
    