# -*- coding: utf-8 -*-

from random import randint
import satutil
#import copy

#
#
def Solve(num_vars, clauses, max_flips):
	"""
	Solve(): [boolean, boolean, ...]

	Tries to find a solution to the given formula using GSAT algorithm
	"""	
	checkSat = satutil.Satisfies
	incrementUnsatWeights = satutil.IncrementUnsatWeights
	var_range = xrange(1, num_vars+1)
	num_clauses = len(clauses)

	# Weight structure
	weights = { c: 1 for c in clauses }
	loops = 0
	while True:
		loops += 1
		rintp = satutil.RandomInterpretation(num_vars)
		if checkSat(clauses, rintp):
			return rintp

		#weights = copy.copy(bweights)

		# Flip some variables
		for j in xrange(max_flips):
			num_sat_clauses = FlipVar(var_range, clauses, rintp, weights)
			# print 'Best sat value:', num_sat_clauses
			if num_clauses == num_sat_clauses:
				print loops
				return rintp
			incrementUnsatWeights(clauses, rintp, weights)

#
#
def FlipVar(var_range, clauses, interpretation, weights):
	chosed_variable = 0
	best_result = -1
	checkNumWSat = satutil.NumSatisfiedWeightedClauses

	for i in var_range:
		interpretation[i] = not interpretation[i]
		result = checkNumWSat(clauses, interpretation, weights)
		interpretation[i] = not interpretation[i]

		if result > best_result:
			best_result = result
			chosed_variable = i

	interpretation[chosed_variable] = not interpretation[chosed_variable]

	return satutil.NumSatisfiedClauses(clauses, interpretation)