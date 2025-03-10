#!/usr/bin/env python

import json
import argparse

PROP_KEY = "properties"
INE_KEY = "inE"
OUTV_KEY = "outV"
LABEL_KEY = "label"
VALUE_KEY = "value"
ATVALUE_KEY = "@value"
ATTYPE_KEY = "@type"

def parse_value(val):
    #print("val", val)
    if ATVALUE_KEY in val:
        v = val[ATVALUE_KEY]
        if ATTYPE_KEY in val:
            t = val[ATTYPE_KEY]
            if t == "g:Int64":
                v = int(v)
        return v
    if VALUE_KEY in val:
        if isinstance(val[VALUE_KEY], bool):
            return val[VALUE_KEY]
        #print(val)
        if ATVALUE_KEY in val[VALUE_KEY]:
            return val[VALUE_KEY][ATVALUE_KEY]
        return val[VALUE_KEY]
    return val

def parse_properties(data):
    out = {}
    if PROP_KEY in data:
        #print(data)
        for key, val in data[PROP_KEY].items():
            if isinstance(val, list):
                o = []
                if len(val) > 1:
                    print(data)
                for i in val:
                    o.append(parse_value(i))
                if len(o) == 1: # I'm not sure if I misunderstanding the GraphSON format, but there seems to be a lot of single item arrays
                    out[key] = o[0]
                else:
                    out[key] = o
            else:
                #print(val)
                out[key] = parse_value(val)
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--output", default="graph")
    parser.add_argument("--new-format", default=False, action="store_true")

    args = parser.parse_args()

    vertex_out = open(args.output + ".vertex", "wt")
    edge_out = open(args.output + ".edge", "wt")
    with open(args.file, encoding="UTF8") as handle:
        for line in handle:
            data = json.loads(line)

            vid = data['id'][ATVALUE_KEY]
            label = data[LABEL_KEY]
            props = parse_properties(data)
            #print("vertex", vid, label, props)
            #print(data)
            if args.new_format:
                vertex_out.write(json.dumps({
                    "_id" : str(vid),
                    "_label" : label
                } | props) + "\n")
            else:
                vertex_out.write(json.dumps({
                    "gid" : str(vid),
                    "label" : label,
                    "data" : props}) + "\n"
                )


            if 'inE' in data:
                for label, nodes in data['inE'].items():
                    for n in nodes:
                        eid = n['id']['@value']
                        dest = parse_value(n['outV'])
                        eprops = parse_properties(n)
                        #print("edge", vid, label, eid, dest, eprops)
                        if args.new_format:
                            edge_out.write(json.dumps({
                                "_id" : str(eid),
                                "_label" : label,
                                "_to" : str(dest),
                                "_from" : str(vid)
                            } | eprops) + "\n")
                        else:
                            edge_out.write(json.dumps({
                                "gid" : str(eid),
                                "label" : label,
                                "to" : str(dest),
                                "from" : str(vid),
                                "data" : eprops}) + "\n")

    vertex_out.close()
    edge_out.close()
