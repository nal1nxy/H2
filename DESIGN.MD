- **Developer**: Nalin

## Design of `constructor()`

- Define a constructor `init` with `self` being the current instance of the class.
- The constructor `init` has one parameter `scrabble_file` of datatype `file`.
- Initialize the instance variable `self.scrabble_letter` with an empty dictionary.
- Define a local variable `letters_file` of the datatype `file`.
- Use the local variable `letters_file` to open the file given as the parameter `scrabble_file` in read mode by encoding it.
- Define a local variable `list_of_lines` hwose datatype is a `list`.
- Use the `readlines` method on `letters_file` and assign it to the variable `list_of_lines`.
- Use `for` loop to iterate through `list_of_lines` with `line` as the iterator variable whose datatype is `string`
    - Skip the first element in the list as it is "letter,count,points" by using.
    - Inside the `for` loop define three more variables `letter`, `frequency`, `points` of datatype `stinrg`.
    - Use split method on each `line` with `,` as the separator and assign it to the three variables `letter`, `frequency`, `points`.
    - If `letter` is the string `"balnk"` then
        - Assign an string with a blank space to `letter`.
    - Assign the list of `frequency` and `count`, where their datatypes ae typecasted to `int`, to the key `letter` in the  dictionary `self.scribble_letters`.