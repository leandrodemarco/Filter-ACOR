#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 19:36:16 2018

@author: leandrodemarcovedelago
"""
import re

regex=r"[-+]?[0-9]+\.?[0-9]*(?:[eE][-+]?[0-9]+)?"

input_file = open('ContinuoFijo/Logaritmico/results_full.txt', 'r')
output_file = open('ContinuoFijo/Logaritmico/latex_parsed.txt', 'w+')

for line in input_file.readlines():
    if (not 'X' in line):
        continue
    l = re.findall(regex, line)
    i = 0
    for string_number in l:
        latex_parsed_line = ""
        if (i == 0):
            # R1
            latex_parsed_line += (str(int(float(string_number))) + ' & ')
        elif (i < 3):
            # R2, R3
            latex_parsed_line += (str(round(float(string_number), 2)) + ' & ')
        elif (i == 3 or i == 4):
            # C4, C5
            parsed_num = ("%.3g" % float(string_number))
            base, exp = parsed_num.split('e')
            exp = str(int(exp)) # Remove preceding zeros
            latex_expr = '\\expnumber{%s}{%s}' % (base, exp)
            latex_parsed_line += (latex_expr + ' & ')
        elif (i < len(l)-1):
            # Errors
            latex_parsed_line += (str(round(float(string_number), 3)) + '\\% & ')
        else:
            # Sens
            latex_parsed_line += (str(round(float(string_number), 3)) + ' \\\\\n')
        i += 1
        output_file.write(latex_parsed_line)
        
input_file.close()
output_file.close()