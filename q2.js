 class Story{
     constructor(storyName,storyLength,ageGroup,originlanguage,africanCommunity){
         this.storyName = storyName
         this.storyLength = storyLength
         this.ageGroup = ageGroup
         this.originlanguage = originlanguage
         this.africanCommunity = africanCommunity
     }

 }
 function displayDetails(){
     console.log(" This ${this.storyName} is a story from the ${this.africanCommunity} who speak the ${this.originLanguage.\n It is ${this.storyLength} long and is meant for children who are ${this.agegroup} years.")
 }


 class StoryTeller extends Story{
     constructor(storyName,storyLength,ageGroup,originlanguage,africanCommunity){
        super(storyName,storyLength,ageGroup,originlanguage,africanCommunity)
        this.storyTellerName = storyTellerName
        this.numberOfMoralLessons = this.numberOfMoralLessons
     }
 }
 function displayDetails(){
    console.log("This ${this.storyName} is narrated by ${this.storyTellerName} in ${this.originLanguage}, for children who are ${this.ageGroup }. It is from the ${this.africanCommunity community} and has ${this.numberOfMoralLessons} moral lessons.")
 }

  class Translator extends Story{
    constructor(storyName,storyLength,ageGroup,originlanguage,africanCommunity){
        super(storyName,storyLength,ageGroup,originlanguage,africanCommunity)

     
  }
}
function translateStory(originLanguage,newLanguage){
    console.log("This ${this.storyName} that was originally narrated in ${originLanguage} from the ${this.africanCommunity} community has now been translated to ${newLanguage}.")
}
 
