word_lib = {'fruit': ['apple',
                      'banana',
                      'cantaloupe',
                      'dragon fruit',
                      'elderberry',
                      'finger lime',
                      'guava',
                      'honeydew',
                      'jackfruit',
                      'kumquat',
                      'lychee',
                      'mango',
                      'nectarine',
                      'olive',
                      'persimmon',
                      'quince',
                      'rambutan',
                      'star fruit',
                      'tangerine',
                      'watermelon'],
            'vegetable': ['artichoke',
                          'brussel sprout',
                          'cassava',
                          'daikon raddish',
                          'eggplant',
                          'fennel',
                          'ginger',
                          'horse raddish',
                          'jicama',
                          'kale',
                          'leek',
                          'mustard green',
                          'Nasturtium',
                          'onion',
                          'potato',
                          'quinoa',
                          'raddish',
                          'spinach',
                          'taro root',
                          'watercress',
                          'yam',
                          'zucchini']}


def draw_hangman(tries):
    stages = [
        r"""
    ________
   |/      |
   |      (_)
   |      \|/
   |       |
   |      / \
   |
___|___
  """,
        r"""
    ________
   |/      |
   |      (_)
   |      \|/
   |       |
   |      /
   |
___|___
  """,
        r"""
    ________
   |/      |
   |      (_)
   |      \|/
   |       |
   |      
   |
___|___
  """,
        r"""
    ________
   |/      |
   |      (_)
   |      \|
   |       |
   |      
   |
___|___
  """,
        r"""
    ________
   |/      |
   |      (_)
   |       |
   |       |
   |      
   |
___|___
  """,
        r"""
    ________
   |/      |
   |      (_)
   |      
   |       
   |      
   |
___|___
  """,
        r"""
    ________
   |/      |
   |      
   |      
   |      
   |      
   |
___|___
  """
    ]
    return stages[tries]
