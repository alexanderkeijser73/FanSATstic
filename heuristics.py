# -*- coding: utf-8 -*-


#
#
def mostOftenVariable(var_range, litclauses):
    """
    mostOftenVariable(var_range, litclauses) -> variable

        - var_range: An Iterable that which returns all the possible variables
        
        - litclauses: A dictionary with all the clauses per literal in var_range
    
    Returns the variable that apears more times on the formula
    """
    
    best = -1
    var = 0
    
    for v in var_range:
        times = 0
        
        try:
            times += len(litclauses[v])
        except KeyError:
            pass
        
        try:
            times += len(litclauses[-v])
        except KeyError:
            pass
        
        if times > best:
            best = times            
            var = v
            
    return var
        

#
#
def mom(var_range, litclauses):
    """
    mom(var_range, litclauses) -> variable

        - var_range: An Iterable that which returns all the possible variables
        
        - litclauses: A dictionary with all the clauses per literal in var_range
    
    Returns the variable that appears most often in the smallest clauses, and favours 
    balanced variables
    """
    
    k = 10	#tuneable parameter

    var = 0
    best = -1
    
    for v in var_range:
        pvlen = nvlen = 0
    
        try:
            pvlen = len(litclauses[v]) 
        except KeyError:
            pass
        
        try:
            nvlen = len(litclauses[-v])
        except KeyError:
            pass

        mom_value = pvlen * nvlen + 2**k * (pvlen + nvlen)
            
        if eq_value > best:
            best = eq_value         
            var = v
            
    return var

#
#
def jwOS(var_range, litclauses):
    """
    jwOS(var_range, litclauses) -> variable

        - var_range: An Iterable that which returns all the possible variables
        
        - litclauses: A dictionary with all the clauses per literal in var_range
    
    Returns the variable with the highest One sided Jeroslow-Wang factor
    """
    

    var = 0
    best = -1
    
    for v in var_range:
        j_value = 0
    
        try:
            v_clauses = litclauses[v]
            for clause in v_clauses:
            	j_value += 2**(-len(clause)) 
        except KeyError:
            pass
            
        if j_value > best:
            best = j_value           
            var = v
            
    return var

#
#
def jwTS(var_range, litclauses):
    """
    jwTS(var_range, litclauses) -> variable

        - var_range: An Iterable that which returns all the possible variables
        
        - litclauses: A dictionary with all the clauses per literal in var_range
    
    Returns the variable with the highest Two sided Jeroslow-Wang factor
    """
    

    var = 0
    best = -1
    
    for v in var_range:
        jpos_value, jneg_value = 0
    
        try:
            vpos_clauses = litclauses[v]
            for pos_clause in vpos_clauses:
            	jpos_value += 2**(-len(pos_clause)) 
        except KeyError:
            pass
            
        try:
            vneg_clauses = litclauses[-v]
            for neg_clause in vneg_clauses:
            	jneg_value += 2**(-len(neg_clause)) 
        except KeyError:
            pass
      	
      	j_value = jpos_value + jneg_value

        if j_value > best:
            best = j_value           
            if jneg_value > jpos_value:
            	var = -v	#MAYBE ERROR FOR v=0
            else:
            	var = v
            
    return var

#
#
def dlcs(var_range, litclauses):
    """
    dlcs(var_range, litclauses) -> variable

        - var_range: An Iterable that which returns all the possible variables
        
        - litclauses: A dictionary with all the clauses per literal in var_range
    
    Returns the variable that apears most often in both polarities and chooses the 
    polarity that occurs most
    """
    
    best = -1
    var = 0
    
    for v in var_range:
        times, vp, vn = 0

        
        try:
            vp = len(litclauses[v])
            times += vp
        except KeyError:
            pass
        
        try:
            vn = len(litclauses[-v])
            times += vn
        except KeyError:
            pass
        
        if times > best:
            best = times            
            if vn > vp:
            	var = -v #MAYBE ERROR FOR v=0
            else:
            	var = v
            
    return var

#
#
def dlis(var_range, litclauses):
    """
    dlis(var_range, litclauses) -> variable

        - var_range: An Iterable that which returns all the possible variables
        
        - litclauses: A dictionary with all the clauses per literal in var_range
    
    Returns the literal that occurs most
    """
    
    best = -1
    var = 0
    
    for v in var_range:
        times = 0

        try:
        	times = len(litclauses[v])
	        if times > best:
        	   var = v #MAYBE ERROR FOR v=0 
        except KeyError:
            pass
            
    return var

#
#
def mostEqulibratedVariable(var_range, litclauses):
    """
    mostEqulibratedVariable(var_range, litclauses) -> variable

        - var_range: An Iterable that which returns all the possible variables
        
        - litclauses: A dictionary with all the clauses per literal in var_range
    
    Returns the most equilibrated variable [ (len(var) * len(-var)) ]
    """
    
    var = 0
    best = -1
    
    for v in var_range:
        pvlen = nvlen = 0
    
        try:
            pvlen = len(litclauses[v]) 
        except KeyError:
            pass
        
        try:
            nvlen = len(litclauses[-v])
        except KeyError:
            pass

        eq_value = pvlen * nvlen * 1024 + pvlen + nvlen
            
        if eq_value > best:
            best = eq_value
            var = v

    return var        