import random

class User():
    def __init__(self, id: int, nickname: str, mark: int):
        self.id = id
        self.nickname = nickname
        self.mark = mark

    def __str__(self):
        return f"{self.id} {self.nickname} {self.mark}"

id = int(input('enter id:'))
nickname = input('enter nickname:')
mark = int(input('enter mark:'))

new_user = User(id, nickname, mark)
with open("database.txt", 'a', encoding="utf-8") as file:
    file.write(new_user.__str__())