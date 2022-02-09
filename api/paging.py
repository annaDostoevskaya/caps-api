class Page:
    ## TODO(annad): Documentation!
    ## TODO(annad): Refactoring!
    def __init__(self, number, size, string_repr_template):

        self.number = number
        self.size = size
        '''
        Example:

        page = 2. pg_size = 3. => pointer_id = 4 <----+------------------------------------------------+
                                                      +                                                +
            pointer_id = ((page - 1) * pg_size) + 1 <-+                                                +
                                                      +                                                +
            (page - 1) -------------------------------+------------------------------------+           +
                                                      +                                    +           +
    +------ (page - 1) * pg_size                      +                                    +           +
    +                                                 +                                    +           +
    +       (page - 1) * pg_size + 1------------------+                                    +           +
    +                                                                                      +           +
    +               +-1. =DATA=========================================== -+               +           +
    +   pg_size = 3 + 2. =DATA===========================================  + page = 1  <---+           +
    +----------->   +-3. =DATA=========================================== -+                           +
                                                                                                       +
                      4. =DATA=========================================== -+ <-------------------------+
                      5. =DATA===========================================  + page = 2
                      6. =DATA=========================================== -+

                      7. =DATA=========================================== -+
                      8. =DATA===========================================  + page = 3
                      9. =DATA=========================================== -+

                      10.=DATA=========================================== -+
                      .....................................................+ page = 4

        '''
        self.dbid_pointer = ((number - 1) * size) + 1
        self.string_repr_template = string_repr_template
        self.string_format = string_repr_template.format(self.number, self.size)

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, nb):
        if nb <= 0:
            raise ValueError('Page below 1 is not possible.')
        self._number = nb

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, sz):
        if sz <= 0:
            raise ValueError('Size of Page below 1 is not possible.')
        self._size = sz

    def next(self):
        return Page(self.number + 1, self.size, self.string_repr_template)

    def previous(self):
        return Page(self.number - 1, self.size, self.string_repr_template)

    def start_id(self):
        return self.dbid_pointer

    def end_id(self):
        return self.dbid_pointer + self.size