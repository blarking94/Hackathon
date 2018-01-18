def convert_buying(value):
  return {
    'vhigh': 1,
    'high': 2,
    'med': 3,
    'low': 4
  }[value]

def convert_maint(value):
  return {
    'vhigh': 1,
    'high': 2,
    'med': 3,
    'low': 4
  }[value]

def convert_doors(value):
  return {
    '2': 1,
    '3': 2,
    '4': 3,
    '5more': 4
  }[value]

def convert_persons(value):
  return {
    '2': 1,
    '4': 2,
    'more': 3
  }[value]

def convert_lug_boot(value):
  return {
    'small': 1,
    'med': 2,
    'big': 3
  }[value]

def convert_safety(value):
  return {
    'low': 1,
    'med': 2,
    'high': 3
  }[value]

def convert_acceptability(value):
    return{
      'unacc' : 1,
      'acc' : 2,
      'good' : 3,
      'vgood' : 4
    }[value]
