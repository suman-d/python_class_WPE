import sys

def myrange2(*args):
    
    if len(args) == 1:
        start = 0 
        stop = args[0]
        step = 1
    
    elif len(args) == 2:
        start, stop = args
        if stop is None:
            stop = start
            start = 0
        step = 1
    
    elif len(args) == 3:
        start, stop, step = args
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1
    
    elif len(args) == 0 or len(args) > 3:
        print("Invalid Arguments")
        sys.exit(0)
    
    result = []
    while True:
        
        if start > stop-1:
            break
            
        result.append(start)
        start += step 
    
    return result

def myrange3(*args):
    
    if len(args) == 1:
        start = 0 
        stop = args[0]
        step = 1
    
    elif len(args) == 2:
        start, stop = args
        if stop is None:
            stop = start
            start = 0
        step = 1
    
    elif len(args) == 3:
        start, stop, step = args
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1
    
    elif len(args) == 0 or len(args) > 3:
        print("Invalid Arguments")
        sys.exit(0)
    
    while True:
        
        if start > stop-1:
            break
            
        yield start
        start += step 
