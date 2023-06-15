#   Question one
class Story:

     def __init__(self,story_name,story_length,age_group,origin_language,african_community):
         self.storyName = story_name
         self.storyLength = story_length
         self.ageGroup = age_group
         self.originlanguage = origin_language
         self.africanCommunity = african_community
     

    def display_details:
        return f"This {self.story_name} is a story from the {self.african_community} who speak the {self.origin_language}.\n It is {self.story_length} long and is meant for children who are {self.age_group} years."
 


class Story_teller(Story):

    def __init__(self,story_name,story_length,age_group,origin_language,african_community):
    super .__init__():


    def display_details(self,story_teller_name,number_of_moralLessons):
         return f"This {self.story_name} is narrated by {story_teller_name} in {self.origin_language}, for children who are {self.age_group }. It is from the {self.african_community} community and has {number_of_moral_lessons} moral lessons."
    
 

class Translator(Story):


    def __init__(self,story_name,story_length,age_group,origin_language,african_community):
    super .__init__():

    def translateStory(self,origin_language,new_language):
        return f"This {self.story_name} that was originally narrated in {self.origin_language} from the {self.african_community} community has now been translated to {new_language}."


#  Question two
class African_Cuisine:

     def __init__(self,unique_ingredients,prep_time,cooking_method,nutritional_value):
         self.unique_ingredients = s
         self.prep_time= prep_time
         self.cooking_method = cooking_method
         self.nutritional_value = nutritional_value
         