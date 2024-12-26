import re
from pprint import pprint
from pydantic import BaseModel

def load_data():
    with open('data_13.txt') as fin:
        myfile = fin.read()
        pattern = re.compile(
            r"Button A: X\+(\d+), Y\+(\d+)\n"
            r"Button B: X\+(\d+), Y\+(\d+)\n"
            r"Prize: X=(\d+), Y=(\d+)"
        )
        matches = pattern.findall(myfile)
        structured_data = []
        for match in matches:
            match_structured = {
                    "Button_A": {"X": int(match[0]), "Y": int(match[1])},
                    "Button_B": {"X": int(match[2]), "Y": int(match[3])},
                    "Prize": {"X": int(match[4]), "Y": int(match[5])}
                }
            structured_data.append(match_structured)
        # Transform structured data into a list of Pydantic objects
        pydantic_list = []
        for claw_example in structured_data:
            pydantic_claw = Claw_Machine(**claw_example)
            pydantic_list.append(pydantic_claw)
    return pydantic_list

class Claw_Machine(BaseModel):
    Button_A: dict[str, int]
    Button_B: dict[str, int]
    Prize: dict[str, int]

data = load_data()

pprint(data)
print(f'len of data: {len(data)}')
print(f'pydantic data type: {type(data[107])}')
print(data[107])
print(f'button b type: {type(data[107].Button_B)}')
print(data[107].Button_B)
print(f"button b location y type: {type(data[107].Button_B['Y'])}")
print(data[107].Button_B['Y'])