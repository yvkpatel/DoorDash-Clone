# -------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Item Class -------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------

# @intializes  
#           Type: String
#           Description: item id 
#           Type: String
#           Description: item name
#           Type: String
#           Description: item category
#           Type: double
#           Description: cost of item
#           Type: String
#           Description: estimated preparation time for item
#           Type: double
#           Description: number of calories in item
class Item:
  
    def __init__(self, id, name, category, cost, prepTime, calories, description, imageLink):
        self.__id = id
        self.__name = name
        self.__category = category
        self.__cost = cost
        self.__prepTime = prepTime
        self.__calories = calories
        self.__description = description
        self.__imageLink = imageLink

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getCategory(self):
        return self.__category

    def getCost(self):
        return self.__cost

    def getPrepTime(self):
        return self.__prepTime

    def getCalories(self):
        return self.__calories

    def getDescription(self):
        return self.__description

    def getImageLink(self):
        return self.__imageLink
