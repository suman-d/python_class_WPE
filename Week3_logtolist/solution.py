from collections import OrderedDict

def logtolist2(filename):
    result = []

    with open(filename) as fh:

        fh_list = fh.readlines()
        for l in fh_list:
            data_broken = l.split("- - [")
            d_ip = data_broken[0].strip()
            d_time = data_broken[1].split("]")[0]
            d_rest = data_broken[-1].strip().split('"')[1]

            final_data = OrderedDict({"ip_address": d_ip,
                          "timestamp" : d_time,
                          "request" : d_rest})


            result.append(final_data)

    return result

def logtolist(filename):
    
    return [ line_to_dict(line) for line in open(filename)]

def line_to_dict(line):
    
    ip_add = line.split()[0]
    
    timestamp_start = line.index("[") + 1
    timestamp_end = line.index("]")
    timestamp = line[timestamp_start:timestamp_end]
    
    rest_start = line.index('"') + 1
    rest_end = rest_start + line[rest_start:].index('"')
    rest = line[rest_start:rest_end]
    
    final_data = OrderedDict({"ip_address": ip_add,
                              "timestamp" : timestamp,
                              "request" : rest})
    
    return final_data