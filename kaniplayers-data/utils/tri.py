from typing import List


def tri(datas: any, item: str) -> List[list]:
  """
  Custom sorting function based on the buble sorting

  Args:
      datas (any): The datas where we choose to sort the thingies
      item (str): The sort of data we wanna sort

  Returns:
      List[list]
      ["Joueur", "item"][]
  """
  names = list(datas['Joueur'])
  numbers = list(datas[item])
  n = len(names)
  for i in range(n-1):
    for j in range(n-1):
      if numbers[j] < numbers[j+1]:
        temp_name = names[j+1]
        temp_number = numbers[j+1]
        names[j+1] = names[j]
        numbers[j+1] = numbers[j]
        names[j] = temp_name
        numbers[j] = temp_number
  return [[names[i], numbers[i]] for i in range(n)]