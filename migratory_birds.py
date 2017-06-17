from collections import Counter


class InvalidData(Exception):
    pass


class BirdCounter():

    def migratory_birds(self, n, ar):
        error_check = self.validate_data(n, ar)
        if error_check == 'validated':
            count = dict(Counter(ar))
            max_bird_number = max([x for x in count.values()])
            lowest_type = min([x for x, j in count.items() if j == max_bird_number])
            return lowest_type
        return 'invalid data'

    def validate_data(self, n, ar):
        try:
            self.checks(n, ar)
            return 'validated'
        except InvalidData as e:
            print(e)
            return e

    def checks(self, n, ar):
        if len(ar) > 0:
            ar_check = [x for x in ar if x <= 0 or x > 5]
            print(ar)
            if n <= 0 or n > 1e15:
                raise InvalidData('Invalid integer n')
            elif len(ar_check) > 0:
                raise InvalidData('Invalid type in array arr')
        else:
            raise InvalidData('No values in ar')
