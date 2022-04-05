import json

class Zpk:
    zpk_binary: bytes
    zpk_json: dict

    def __init__(self, path):
        with open(path, 'rb') as f:
            self.zpk_binary = f.read()
            self.zpk_binary = self.zpk_binary[128:]
            self.__get_json__()

    def __get_json__(self):
        bracket_match_count = 0
        last_bracket_index = 0
        for index in range(len(self.zpk_binary)):
            if self.zpk_binary[index] == ord('{'):
                bracket_match_count = bracket_match_count + 1
            if self.zpk_binary[index] == ord('}'):
                bracket_match_count = bracket_match_count - 1
                last_bracket_index = index
            if bracket_match_count == 0:
                break
        self.zpk_json = json.loads(self.zpk_binary[:last_bracket_index + 1].decode(encoding='utf-8'))

    def get_json(self):
        return self.zpk_json
