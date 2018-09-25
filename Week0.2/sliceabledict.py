import collections

class SliceableDict(dict):
    
    def __getitem__(self, key):
        
        if not isinstance(key, collections.Iterable):
            val = dict.__getitem__(self, key)
                
        else:
            val = []
            for k in key:
                try: 
                    val.append(dict.__getitem__(self, k))
                except KeyError:
                    print("No key {}".format(k))
                    
        
        return val