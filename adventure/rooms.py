from pydantic import BaseModel


class Room(BaseModel):
    # fields
    name: str
    description: str
    items = []  # : list
    exits = []  #: list

    def show(self):
        """
        Shows the current room.
        """
        print(self.description)
        if self.items != []:  # len(current_room.items) > 0
            print('Vidíš:')
            for item in self.items:
                print(f'  {item}')
        else:
            print('Nevidíš tu nič zvláštne.')
