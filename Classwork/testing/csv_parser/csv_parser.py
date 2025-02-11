class InputError(Exception):
    def __init__(self, data):
        self.message = f"failed to parse {data}"

def parse_csv(content: str, separator:str = ",") -> list[dict[str, str]]:
    result = list()
    if not content:
        return result
    
    lines = content.split("\n")

    if len(lines) == 1:
        return None
    
    header = lines[0].split(separator)
    header = [col.strip() for col in header]

    for line in lines[1:]:
        if line.count(separator) == len(header):
            if line.strip()[-1] == separator:
                line = line.strip()[:-1]

        values = line.split(separator)
        values = [val.strip() for val in values]

        if len(values) != len(header):
            raise InputError(line)
        
        line_dict = {}
        for col, val in zip(header, values):

            line_dict[col] = val.strip('"')
            line_dict[col] = val.replace ('"', '')

        result.append(line_dict)
    return result