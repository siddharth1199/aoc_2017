import re

def possible_changes():
    changes = [{"Al": "ThF"},
               {"Al": "ThRnFAr"},
               {"B": "BCa"},
               {"B": "TiB"},
               {"B": "TiRnFAr"},
               {"Ca": "CaCa"},
               {"Ca": "PB"},
               {"Ca": "PRnFAr"},
               {"Ca": "SiRnFYFAr"},
               {"Ca": "SiRnMgAr"},
               {"Ca": "SiTh"},
               {"F": "CaF"},
               {"F": "PMg"},
               {"F": "SiAl"},
               {"H": "CRnAlAr"},
               {"H": "CRnFYFYFAr"},
               {"H": "CRnFYMgAr"},
               {"H": "CRnMgYFAr"},
               {"H": "HCa"},
               {"H": "NRnFYFAr"},
               {"H": "NRnMgAr"},
               {"H": "NTh"},
               {"H": "OB"},
               {"H": "ORnFAr"},
               {"Mg": "BF"},
               {"Mg": "TiMg"},
               {"N": "CRnFAr"},
               {"N": "HSi"},
               {"O": "CRnFYFAr"},
               {"O": "CRnMgAr"},
               {"O": "HP"},
               {"O": "NRnFAr"},
               {"O": "OTi"},
               {"P": "CaP"},
               {"P": "PTi"},
               {"P": "SiRnFAr"},
               {"Si": "CaSi"},
               {"Th": "ThCa"},
               {"Ti": "BP"},
               {"Ti": "TiTi"},
               {"e": "HF"},
               {"e": "NAl"},
               {"e": "OMg"}]

    possible_changes = {}

    for item in changes:
        for key, value in item.items():
            possible_changes.setdefault(key, []).append(value)

    return possible_changes


def calculate_changes(input):
    outcomes = {}
    changes = possible_changes()

    for original, replacements in changes.items():
        for replacement in replacements:
            for occ in re.finditer(original, input):
                new = input[:occ.start()] + replacement + input[occ.end():]
                outcomes.setdefault(new, True)

    return len(outcomes.keys())


if __name__ == "__main__":
    input = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
    print(calculate_changes(input))