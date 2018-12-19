#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 23:11:32 2018

@author: leandrodemarcovedelago

Corre la versión discreta pura del algoritmo
"""

import ACOR
import Utils

use_log = True # Change this flag to use logarithmic version

output_dir = ('DiscretoPuro/Logaritmico/' if use_log 
              else 'DiscretoPuro/Comun/')
f = open(output_dir + 'results.txt', 'w+')

a = ACOR.Acor('DiscretoPuro', use_log)
u = Utils.Utils()

iterations_per_rval = 100
r1_vals = u.r1_with_sols
for R1 in r1_vals:
    found_sols = []
    iterations_with_sol = 0
    for i in range(0, iterations_per_rval):
        print 'Running iter %i for R1: %i' % (i+1, R1)
        best_sol = a.main_loop(R1)[:-1]
        if (use_log):
            best_sol = Utils.exp_list(best_sol)
        r2, r3, c4, c5 = best_sol[0], best_sol[1], best_sol[2], best_sol[3]
        sol = [R1, r2, r3, c4, c5]
        sens = u.get_sol_info_grouped(sol)[0]
        isSol = u.is_sol_grouped(sol)
        if (isSol):
            iterations_with_sol += 1
            if (not sol in found_sols):
                found_sols.append(sol)
    if iterations_with_sol == 0:
        f.write('No hallo soluciones para R1: ' + str(R1) + '\n')
    else:
        f.write('Hallo %i (%i) soluciones: %s\n' % (len(found_sols), \
                                                   iterations_with_sol, \
                                                   str(found_sols)))
            
f.close()