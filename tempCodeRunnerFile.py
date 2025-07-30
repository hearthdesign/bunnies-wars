    # place carrots for pc randomly.
    def place_carrots(self, row, col):
        if (
            (row, col) not in self.carrots and
                len(self.carrots) < self.num_carrots
        ):
            self.carrots.add((row, col))
            return True
        return False