fun main(){

}
//The class story has  several attributes which are the story name, the story length, the age group range , the origin language  the
//  story is written in and the African language. The function displayDetails displays all the information about the story from the attributes given.
 open class Story(var storyName:Story,var storyLength:String,var ageGroup:IntRange, var originLanguage:String,var africanCommunity:String){
    open fun displayDetails(){
        println("This $storyName is a story from the $africanCommunity community who speak the $originLanguage language,it iss $storyLength long and is meant for children who are $ageGroup years old")
    }


}
//I  created a new class for the storyteller which inherits the attributes from the story class and added a some unique attributes for this class, the story
//tellers  name  and the number of moral lessons he shares from the story
class StoryTeller(storyName: Story,storyLength: String,ageGroup: IntRange,originLanguage: String,africanCommunity: String,var storyTellerName:String,var numberOfMoralLessons:Int):Story(storyName,storyLength,ageGroup,originLanguage,africanCommunity){
     override fun displayDetails(){
         println("This $storyName is narrated by $storyTellerName in $originLanguage, for children who are $ageGroup years. It is from the $africanCommunity community and has $numberOfMoralLessons moral lessons.")
     }
}
class Translator(storyName: Story,storyLength: String,ageGroup: IntRange,originLanguage: String,africanCommunity: String):Story(storyName,storyLength,ageGroup,originLanguage,africanCommunity){
 fun translateStory( originLanguage: String, newLanguage:String){
     println("This $storyName that was originally narrated in $originLanguage from the $africanCommunity community has now been translated to $newLanguage.")

 }

}
