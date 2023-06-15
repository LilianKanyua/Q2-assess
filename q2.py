class Story:

     def __init__(self,story_name,story_length,age_group,origin_language,african_community):
         self.storyName = storyName
         self.storyLength = storyLength
         self.ageGroup = ageGroup
         self.originlanguage = originlanguage
         self.africanCommunity = africanCommunity
     

    def display_details:
        return f"This {self.storyName} is a story from the {self.africanCommunity} who speak the {self.originLanguage}.\n It is {self.storyLength} long and is meant for children who are {self.agegroup} years."
 


class StoryTeller(Story):

    def __init__(self,story_name,story_length,age_group,origin_language,african_community):
    super .__init__():


    def display_details(self,storyTellerName,numberOfMoralLessons):
         return f"This {self.storyName} is narrated by {storyTellerName} in {self.originLanguage}, for children who are {self.ageGroup }. It is from the {self.africanCommunity community} and has {numberOfMoralLessons} moral lessons."
    
 

class Translator(Story):


    def __init__(self,story_name,story_length,age_group,origin_language,african_community):
    super .__init__():

    def translateStory(self,origin_language,newLanguage):
        return f"This {self.storyName} that was originally narrated in {self.originLanguage} from the {self.africanCommunity} community has now been translated to {newLanguage}."


 