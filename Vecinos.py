#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:14:32 2018

@author: leandrodemarcovedelago
"""

import ACOR
import Utils

use_log = True # Change this flag to use logarithmic version
a = ACOR.Acor('Vecinos', use_log)
u = Utils.Utils()

best_r1 = u.best_r1_sens
for R1 in best_r1:
    final_results = a.mainLoop(R1)
    best_sol = final_results[:-1]
    cost = final_results[-1]
    if (use_log):
        best_sol = Utils.exp_list(best_sol)
    r2, r3, c4, c5 = best_sol[0], best_sol[1], best_sol[2], best_sol[3]
    solutions = u.fetch_neighbour_solutions(R1, r2, r3, c4, c5)
    for sol in solutions:
        sens = u.get_sol_info_grouped(sol)[0]
        print sol, sens

