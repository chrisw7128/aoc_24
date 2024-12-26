from pprint import pprint
from pydantic import BaseModel
import re

def load_data():
    with open('data_14.txt') as fin:
        myfile = fin.read()
        pattern = re.compile(
            r"p=(\d+),(\d+) v=(\d+),(\d+)"
        )
        matches = pattern.findall(myfile)
        structured_data = []
        for match in matches:
            match_structured = {
                "Position": (match[0], match[1]),
                "Velocity": (match[2], match[3])
            }
            structured_data.append(match_structured)
        pydantic_list = []
        for guard in structured_data:
            security_guard = Security_Guard(**guard)
            pydantic_list.append(security_guard)
    return pydantic_list

class Security_Guard(BaseModel):
    Position: tuple[int, int]
    Velocity: tuple[int, int]

data = load_data()

pprint(data)
print(f'len of data: {len(data)}')
pprint(type(data[42]))
pprint(data[42])
pprint(type(data[42].Velocity))
pprint(data[42].Velocity)
pprint(type(data[42].Velocity[0]))
pprint(data[42].Velocity[0])