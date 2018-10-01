#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:23:12 2018

@author: leandrodemarcovedelago
"""

import ACOR
import Utils

use_log = True # Change this flag to use logarithmic version
a = ACOR.Acor('ContinuoLibre', use_log)
u = Utils.Utils()
final_results = a.mainLoop()
best_sol = final_results[:-1]
cost = final_results[-1]

if (use_log):
    best_sol = Utils.exp_list(best_sol)
    
print best_sol, cost
r1, r2, r3, c4, c5 = best_sol[:5]
sens, g, q, wp = u.get_sol_info(r1, r2, r3, c4, c5)
print('Sensibilidad: ' + str(sens) + '\n')
print('G: ' + str(g) + '\n')
print('Error G: ' + str(u.err_g(g)) + '%\n')
print('Omega: ' + str(wp) + '\n')
print('Error Omega: ' + str(u.err_wp(wp)) + '%\n')
print('Q: ' + str(q) + '\n')
print('Error Q: ' + str(u.err_q(q)) + '%\n')

plot = True
if (plot):
    best_r1 = Utils.exp_list(a.best_r1) if use_log else a.best_r1
    best_r2 = Utils.exp_list(a.best_r2) if use_log else a.best_r2
    best_r3 = Utils.exp_list(a.best_r3) if use_log else a.best_r3
    best_c4 = Utils.exp_list(a.best_c4) if use_log else a.best_c4
    best_c5 = Utils.exp_list(a.best_c5) if use_log else a.best_c5
    best_cost = a.best_cost
    plot_utils = Utils.PlotingUtils([best_r1, best_r2, best_r3, best_c4,
                                     best_c5, best_cost])
    plot_utils.plot_cost_and_vars()
    plot_utils.generate_png_files()
    