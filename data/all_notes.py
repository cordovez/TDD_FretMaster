# Key of C


class Fretboard:
    def __init__(self):
        self.complete = [
            [{'E1': 'F'}, {'A1': 'Bb'}, {'D1': 'Eb'}, {'G1': 'Ab'}, {'B1': 'C'},
             {'e1': 'F'}],
            [{'E2': 'Gb'}, {'A2': 'B'}, {'D2': 'E'}, {'G2': 'A'}, {'B2': 'Db'},
             {'e2': 'Gb'}],
            [{'E3': 'G'}, {'A3': 'C'}, {'D3': 'F'}, {'G3': 'Bb'}, {'B3': 'D'},
             {'e3': 'G'}],
            [{'E4': 'Ab'}, {'A4': 'Db'}, {'D4': 'Gb'}, {'G4': 'B'}, {'B4': 'Eb'},
             {'e4': 'Ab'}],
            [{'E5': 'A'}, {'A5': 'D'}, {'D5': 'G'}, {'G5': 'C'}, {'B5': 'E'},
             {'e5': 'A'}],
            [{'E6': 'Bb'}, {'A6': 'Eb'}, {'D6': 'Ab'}, {'G6': 'Db'}, {'B6': 'F'},
             {'e6': 'Bb'}],
            [{'E7': 'B'}, {'A7': 'E'}, {'D7': 'A'}, {'G7': 'D'}, {'B7': 'Gb'},
             {'e7': 'B'}],
            [{'E8': 'C'}, {'A8': 'F'}, {'D8': 'Bb'}, {'G8': 'Eb'}, {'B8': 'G'},
             {'e8': 'C'}],
            [{'E9': 'Db'}, {'A9': 'Gb'}, {'D9': 'B'}, {'G9': 'E'}, {'B9': 'Ab'},
             {'e9': 'Db'}],
            [{'E10': 'D'}, {'A10': 'G'}, {'D10': 'C'}, {'G10': 'F'}, {'B10': 'A'},
             {'e10': 'D'}],
            [{'E11': 'Eb'}, {'A11': 'Ab'}, {'D11': 'Db'}, {'G11': 'Gb'}, {'B11': 'Bb'},
             {'e11': 'Eb'}],
            [{'E12': 'E'}, {'A12': 'A'}, {'D12': 'D'}, {'G12': 'G'}, {'B12': 'B'},
             {'e12': 'E'}],
            [{'E13': 'F'}, {'A13': 'Bb'}, {'D13': 'Eb'}, {'G13': 'Ab'}, {'B13': 'C'},
             {'e13': 'F'}],
            [{'E14': 'Gb'}, {'A14': 'B'}, {'D14': 'E'}, {'G14': 'A'}, {'B14': 'Db'},
             {'e14': 'Gb'}],
            [{'E15': 'G'}, {'A15': 'C'}, {'D15': 'F'}, {'G15': 'Bb'}, {'B15': 'D'},
             {'e15': 'G'}],
            ]

    @staticmethod
    def filter_out_flats(notes_on_fret):
        """Filter out notes containing flats."""
        fret = []
        for note in notes_on_fret:
            for k, v in note.items():
                if "b" not in v:
                    fret.append(note)
        return fret

    @staticmethod
    def key_of_c(fret_range: list) -> list:
        """Apply the filter to each fret in the specified range to get only natural notes."""
        return [Fretboard.filter_out_flats(string_group) for string_group in fret_range]

    def get_fret_group(self, start: int, end: int) -> list[list[dict[str, str]]]:
        """Retrieve a range of frets from the complete fretboard."""
        # dealing in fret numbers, not list index, thus the '-1'
        return self.complete[start - 1:end]

    def position_1(self) -> list[list[dict[str, str]]]:
        return self.key_of_c(self.get_fret_group(8, 12))

    def position_2(self) -> list[list[dict[str, str]]]:
        return self.key_of_c(self.get_fret_group(10, 14))

    def position_3(self) -> list[list[dict[str, str]]]:
        return self.key_of_c(self.get_fret_group(13, 15))

    def position_4(self) -> list[list[dict[str, str]]]:
        return self.key_of_c(self.get_fret_group(1, 5))

    def position_5(self) -> list[list[dict[str, str]]]:
        return self.key_of_c(self.get_fret_group(3, 7))

    def position_6(self) -> list[list[dict[str, str]]]:
        return self.key_of_c(self.get_fret_group(5, 9))

    def position_7(self) -> list[list[dict[str, str]]]:
        return self.key_of_c(self.get_fret_group(7, 10))
