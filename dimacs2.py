# -*- coding: utf-8 -*-

import sys

#
#
def ParseCNF(fname, outformat=frozenset):

    num_vars = 0
    litclauses = None
    clauses = set()

    cnf_file = open(fname, 'r')    
    
    try:
        for nline, line in enumerate(cnf_file):
            lvalues = line.strip().split()
            
            if not lvalues or lvalues[0] == 'c':
                continue
            
            elif    lvalues[0] == 'p':
                if lvalues[1] != 'cnf':
                    raise SyntaxError('Invalid format identifier "%s".'
                                % (lvalues[1]) )
                            
                num_vars = int(lvalues[2])
                #num_clauses = int(lvalues[3])                
                litclauses = [set() for i in xrange(num_vars+1)] #range [1, num_vars]

            # Parse clause
            else:
                values = map(int, lvalues)
                clause = set()

                for lit in values:
                    if lit == 0:
                        if clause not in clauses:
                            
                            if outformat != set:
                                clause = outformat(clause)

                            clauses.add( clause )
                            for l in clause:
                                alit = abs(l)
                                litclauses[alit].add(clause)
                        else:
                            print 'Repeated'
                        clause = None # Check line ends with 0

                    else:
                        clause.add(lit)

                        if lit < -num_vars or lit > num_vars:
                            raise SyntaxError('Invalid literal %d '
                                ', it must be in range [1, %d].'
                                % (lit, num_vars) )

                if clause:
                    raise SyntaxError('Error not found the trailing 0')

    except SyntaxError, e:
        sys.stderr.write('Error parsing file "%s" (%d): %s\n' % 
                                    (fname, nline, str(e)) )

        raise e

    if outformat != set:
        clauses = outformat(clauses)
    litclauses = tuple(litclauses)
    return num_vars,clauses, litclauses

                