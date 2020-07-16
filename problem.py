hockey_games = [
    {'home': {'name': 'San Jose Sharks', 'goals': 3},
     'away': {'name': 'Los Angeles Kings', 'goals': 2},
     'final_period': '3'},
    {'home': {'name': 'Los Angeles Kings', 'goals': 3},
     'away': {'name': 'San Jose Sharks', 'goals': 4},
     'final_period': '3'},
    {'home': {'name': 'Edmonton Oilers', 'goals': 4},
     'away': {'name': 'San Jose Sharks', 'goals': 2},
     'final_period': 'OT'},
    {'home': {'name': 'Vancouver Canucks', 'goals': 3},
     'away': {'name': 'Edmonton Oilers', 'goals': 5},
     'final_period': '3'},
    {'home': {'name': 'Arizona Coyotes', 'goals': 3},
    'away': {'name': 'Vancouver Canucks', 'goals': 2},
    'final_period': 'SO'},
    {'home': {'name': 'Arizona Coyotes', 'goals': 30},
    'away': {'name': 'Vancouver Canucks', 'goals': 20},
    'final_period': '3'}
]
##################################################################################################
# OT is overtime, SO is shoot-out which happens after overtime expires
def calculate_statistics(game_dict):

    home_team = game_dict['home']
    away_team = game_dict['away']
    final_period = game_dict['final_period']

# Check which team won
    if home_team['goals'] > away_team['goals']:
        winning_team_name = game_dict['home']['name']
        losing_team_name = game_dict['away']['name']

    elif home_team['goals'] < away_team['goals']:
        winning_team_name = game_dict['away']['name']
        losing_team_name = game_dict['home']['name']

    else:
        return  {'winner':{'name':winning_team_name, 'score': 1, "ROW": 0}, 'loser':{'name': losing_team_name, 'score': 1, 'ROW':0}}  # tie (pre 2000-2001)
                  

        # Handle overtime vs regulation win
    
    thisItem={}
    if final_period =='OT':
        thisItem= {'winner':{'name':winning_team_name, 'score': 2, "ROW": 1}, 'loser':{'name': losing_team_name, 'score': 1, 'ROW':0}}  # Overtime win/loss
    elif final_period =='SO':
        thisItem= {'winner':{'name':winning_team_name, 'score': 2, "ROW": 0}, 'loser':{'name': losing_team_name, 'score': 1, 'ROW':0}}  # shootout win/loss
    else:
        thisItem= {'winner':{'name':winning_team_name, 'score': 2, "ROW": 1}, 'loser':{'name': losing_team_name, 'score': 0, 'ROW':0}}  # regulation win/loss
        

    return thisItem    

#############################################################################################################

def sort_list(list_to_sort):
    #reorder in descending order of score
    # print("######starting the sort function!  now sorting this list: ", list_to_sort)
    new_list=[]                     #the new sorted copy of list_to_sort
    sub_list=[]                     #the portion of list_to_sort that excludes the largest value
    highest_score=0
    highest_team={}

    if len(list_to_sort)==1:
        return list_to_sort         #exit condition
    else:
        for this_team in list_to_sort:
            if this_team['score']>highest_score:
                highest_score=this_team['score']
                highest_team=this_team

        #remove the highest, the manual way:

        for this_team in list_to_sort:
            if this_team['name']==highest_team['name']:
               pass    # do nothing
            else:
                sub_list.append(this_team)          #restore all the non-highest teams for further sorting.

       
        new_list.append(highest_team)               # the first entry is the highest
        temp_list=[]
        temp_list=sort_list(sub_list)                 # now add the rest of the list, sorted with recursive calls
        for this_item in temp_list:
            new_list.append(this_item)      
        
        return new_list

##############################################################################################################



def ordered_standings():
    
    # traverse the list of games and sum up the points:
    team_list=[]            #keeps track of teams so we don't add a team twice
    result_list=[]          # list of dictionaries
    for this_game in hockey_games:
        this_name=this_game['home']['name']
        if this_name not in team_list:
            result_list.append({'name':this_name,'score':0})
            team_list.append(this_name)

    for this_game in hockey_games:
        result=calculate_statistics(this_game)
        #print("this result is", result)

        #traverse the list of team names and match up to this game's results:
        winner_name=result['winner']['name']
        loser_name=result['loser']['name']

        for team in result_list:
            if team['name']==winner_name:
                team['score']+=result['winner']['score']
            elif team['name']==loser_name:
                team['score']+=result['loser']['score']
            
    #now reorder the list:
    final_list=sort_list(result_list)


    return final_list

##################################################################################
def downformat(thisList):
# change to the desired format
    newList=[]

    for thisTeam in thisList:
        newTeam={}
        newTeam={thisTeam['name']:thisTeam['score']}
        newList.append(newTeam)


    return newList
##################################################################################


my_list=ordered_standings()

print ("the final result list of dictionaries is:")
print (my_list)

my_list=downformat(my_list)

print ("the final result list is")
print (my_list)

