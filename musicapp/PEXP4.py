#Libraries
import random
import time
import ast #This library is new to me its a safer version of eval() and I'll use it for str(dict) to dict transformations

#Variables
LoggedIn = False
CurrentUser = None #For when a user logs in, we need the user
SongLibrary = { #Stores all major song genres and artists + examples for creating a song library
    #Example

    # 'Rock': {
    #     'AC/DC': [
    #         'SONG1',
    #         'SONG2',
    #         'SONG3',
    #         'SONG4'
    #     ]
    # },
    'Rock': {
        'AC/DC': {
            'Highway To Hell': '3:26',
            'Ride On': '5:53',
            'Shoot To Thrill': '5:17',
            'Hells Bells': '5:12',
            'Thunderstruck': '4:52',
            },
        'The Rolling Stones': {
            "Jumpin' Jack Flash": '3:42',
            'Gimme Shelter': '4:37',
            'Satisfaction': '3:45',
            'Time Is On My Side': '3:05',
            'Ruby Tuesday': '3:12',
        },
        'Led Zeppelin': {
            'Heartbreaker': '4:15',
            'Good Times Bad Times': '2:43',
            'Ten Years Gone': '6:55',
            'Dazed And Confused': '3:46',
            'Gallows Pole': '4:50',
        },
    },
    'Pop': {
        'The Beatles': {
            'While My Guitar Gently Weeps': '',
            'A Day In The Life': '5:35',
            'I Want To Hold Your Hand': '2:24',
            'Strawberry Fields Forever': '4:07',
            'Yesterday': '2:03',
        },
        'Elvis Presley': {
            'Mystery Train': '2:30',
            'Kentucky Rain': '3:20',
            'An American Trilogy': '4:26',
            'Heartbreak Hotel': '2:08',
            'Love Me Tender': '2:41',
        },
        'Rihanna': {
            'Disturbia': '3:59',
            'S&M': '4:03',
            "Don't Stop the Music": '4:27',
            'Diamonds': '3:45',
            'Stay': '4:00',
        },
        
    },
    'Rap': {

    },
    'R&B': {

    },
    'Country': {

    },

}

#Notes/Explanations
#The user’s playlist is separate and a collection of 1 or more songs taken from the song library
#A song library is just like a book library where there are details of all songs
#Where it says no songs have the same title means that you can’t have the same song twice in the library with the same title
#Library analogy - all books are in the library, people can take out a copy of their favourite books but the original book is still there

#Examples

#AccountDetails
# AccountDetails = {
#    'joe': { #Name
#        'Password': '...', #Password
#        'DateOfBirth': '...', #Date Of Birth
#        'FavArtist': '...', #Favourite Artist
#        'FavGenre': '...', #Favourite Genre
#        'Playlists': '...', #Playlists Of Songs (At least 1)
#        }
#    }

#Playlists
# 'Playlist': {
#     'EXAMPLELIST1': [
#         'SONGNAME1', #Playlists have to be comprised of atleast one song
#         'SONGNAME2', #I can store just song names here to prevent even more confusion with more nested dictionaries
#         'SONGNAME3', #I'll just call a fetchvalue function to grab data such as song lengths etc from the song library itself
#     ]
# }

AccountDetails = {}

#File handling
AccountsFile = open('Accounts.txt', 'a+')
AccountsFile.seek(0)
RAccountsFile = AccountsFile.read()
Accounts = RAccountsFile.splitlines()

#Functions & Procedures

def ValidSong(SongName): #If the songname is in song library
    for MusicGenre in SongLibrary:
        for MusicArtist in SongLibrary[MusicGenre]:
            if SongName in SongLibrary[MusicGenre][MusicArtist]:
                return True
    return False

def UpdateData():
    AccountsFile.truncate(0) #Clear everything in file
    AccountsFile.seek(0) #Go to start of file (necessary for truncated files)
    for Account in AccountDetails: #Add updated data
        AccountInfo = AccountDetails[Account]
        AccountsFile.write(f'Username: {Account},Password: {AccountInfo["Password"]},DateOfBirth: {AccountInfo["DateOfBirth"]},FavouriteArtist: {AccountInfo["FavouriteArtist"]},FavouriteGenre: {AccountInfo["FavouriteGenre"]},')
        AccountsFile.write(f'Playlists: {str(AccountInfo["Playlists"])}\n')
        AccountsFile.flush() #Save the file

def PrintGeneralCmds():
    print("""
Actions:
- EDIT [arg]
- VIEW [arg]
- EXIT
    """)

def PrintPlistCmds():
    print("""
Actions:
- CREATE [plist name]
- VIEW [plist name]
- EDIT [plist name]
- DELETE [plist name]
- GENERATE [plist name]
- BACK
    """)
def FetchSongData(SongName): #Fetch all the data from song library for previewing e.g name, duration, artist and genre
    SongInfoTable = {} #Creating a table to store all the information for that one song

    for MusicGenre in SongLibrary: #Genre
        for MusicArtist in SongLibrary[MusicGenre]: #Artist
            if SongName in SongLibrary[MusicGenre][MusicArtist]: #Name
                SongInfoTable['Name'] = SongName
                SongInfoTable['Duration'] = SongLibrary[MusicGenre][MusicArtist][SongName]
                SongInfoTable['Artist'] = MusicArtist
                SongInfoTable['Genre'] = MusicGenre
    return SongInfoTable
    

#Main
for Account in Accounts: #Storing existing accounts into a dictionary
    Details = Account.split(',', 5) #Splitting of data for each user. Note: put 5 as maxsplit so tat the rest of the data in playlists can be interpreted by AST library
    Detail1 = Details[0] #Username
    try: #Preventing error from index nil if there are no accounts at all
        Detail2 = Details[1] #Password
    except:
        print('There are no accounts yet')
        break
    Detail3 = Details[2] #DateOfBirth
    Detail4 = Details[3] #FavouriteArtist
    Detail5 = Details[4] #FavouriteGenre
    Detail6 = Details[5] #Playlists

    #Getting second part of data
    Username = Detail1.split(' ', 1)[1]
    Password = Detail2.split(' ', 1)[1]
    DateOfBirth = Detail3.split(' ', 1)[1]
    FavouriteArtist = Detail4.split(' ', 1)[1]
    FavouriteGenre = Detail5.split(' ', 1)[1]
    Playlists = ast.literal_eval(Detail6.split(' ', 1)[1]) #AST library turning playlist into an actual dictionary

    AccountDetails[Username] = {
        'Password': Password,
        'DateOfBirth': DateOfBirth,
        'FavouriteArtist': FavouriteArtist,
        'FavouriteGenre': FavouriteGenre,
        'Playlists': Playlists,
        }

print('Login or Signup')
AccountAction = input('> ') #Action
if AccountAction == 'Login': #Login
    #Ask for details
    IUsername = input('Username: ')
    IPassword = input('Password: ')

    #Loop through accounts for each accounts' details
    for Account in AccountDetails:
        AccountInfo = AccountDetails[Account] #The passwords + fav genre, music etc..
        if Account == IUsername and AccountInfo['Password'] == IPassword: #Check if IDetails are valid
            print('Logged in')
            CurrentUser = Account
            LoggedIn = True
elif AccountAction == 'Signup': #Signup
    #Create username, password + details
    IUsername = input('Username: ')
    IPassword = input('Password: ')

    IDateOfBirth = input('Date Of Birth (MM/DD/YYYY): ')
    IFavouriteArtist = input('Favourite Artist: ')
    IFavouriteGenre = input('Favourite Genre: ')

    if IUsername in AccountDetails: #Username already taken
        print('Username taken already!')
    else:
        AccountDetails[IUsername] = { #Create the data
            'Password': IPassword,
            'DateOfBirth': IDateOfBirth,
            'FavouriteArtist': IFavouriteArtist,
            'FavouriteGenre': IFavouriteGenre,
            'Playlists': {}, #Unable to ask for playlist info this early yet, so we will keep it empty for now
            }

        print(AccountDetails) #Debug check
        AccountsFile.truncate(0) #Clear everything in file
        AccountsFile.seek(0) #Go to start of file (necessary for truncated files)

        for Account in AccountDetails: #Add updated data
            AccountInfo = AccountDetails[Account]
            AccountsFile.write(f'Username: {Account},Password: {AccountInfo["Password"]},DateOfBirth: {AccountInfo["DateOfBirth"]},FavouriteArtist: {AccountInfo["FavouriteArtist"]},FavouriteGenre: {AccountInfo["FavouriteGenre"]},Playlists: {{}}\n')
        AccountsFile.flush() #Save the file
#Make sure they are logged in to continue
if LoggedIn == False: exit()

#Actions
EDITVars = ['FavouriteArtist', 'FavouriteGenre'] #Variables the user is allowed to edit

PrintGeneralCmds()
Action = input('> ')

while Action != 'EXIT': #Main loop
    #Action: EDIT
    if Action[:4] == 'EDIT':
        SAction = Action.split(' ', 1) #Getting the argument from EDIT [arg]
        try: #Just in case the user does not enter an argument at all
            Argument = SAction[1]
        except:
            print('Invalid argument, please try again')
            PrintGeneralCmds()
            Action = input('> ')
            continue
        if Argument in EDITVars: #If variable is one of the allowed edit variables
            NewValue = input('NewValue: ') #Now asking for the new value
            AccountInfo = AccountDetails[CurrentUser]
            AccountInfo[Argument] = NewValue #Edit variable to 'NewValue'

            UpdateData() #Update everything
        elif Argument == 'Playlists': #Playlists is a special case as the user can edit current playlists, delete playlists and create new playlists
            #Playlist Commands
            PrintPlistCmds()
            Action = input('> ')

            while Action != 'BACK':
                #PlaylistAction: CREATE
                if Action[:6] == 'CREATE':
                    SAction = Action.split(' ', 1) #Getting the argument from EDIT [arg]
                    try: #Just in case the user does not enter an argument at all
                        PlaylistName = SAction[1] #Playlist name
                    except:
                        print('Invalid argument, please try again')
                        PrintPlistCmds()
                        Action = input('> ')
                        continue

                    AccountInfo = AccountDetails[CurrentUser] #Get user data
                    if not PlaylistName in AccountInfo['Playlists']: #To make sure there are no two playlists with the same name
                        AccountInfo['Playlists'][PlaylistName] = [] #Create a new playlist with the playlist name

                        #Start song loop
                        print(f'Enter song for playlist: {PlaylistName} [END to stop]')
                        SongName = input('> ')
                        while SongName != 'END': #Perform song adding loop until end is called
                            if ValidSong(SongName): #Check if song is a valid song in song library
                                AccountInfo['Playlists'][PlaylistName].append(SongName) #Add the song to the playlist
                                print(f'{SongName} added to {PlaylistName}')
                            else: #Invalid song
                                print('Could not find song in song library, please try again')
                            print(f'Enter song for playlist: {PlaylistName} [END to stop]')
                            SongName = input('> ')
                        if AccountInfo['Playlists'][PlaylistName] == []:
                            print(f'{PlaylistName} not created as a playlist requires at least one song!')
                            AccountInfo['Playlists'].pop(PlaylistName)
                        UpdateData() #Update everything
                    else:
                        print('There is already a saved playlist under that name, please try again')
                #PlaylistAction: VIEW
                elif Action[:4] == 'VIEW':
                    SAction = Action.split(' ', 1) #Getting the argument from EDIT [arg]
                    try: #Just in case the user does not enter an argument at all
                        PlaylistName = SAction[1] #Playlist name
                    except:
                        print('Invalid argument, please try again')
                        PrintPlistCmds()
                        Action = input('> ')
                        continue
                    AccountInfo = AccountDetails[CurrentUser] #Get user data
                    print()
                    for Song in AccountInfo['Playlists'][PlaylistName]:
                        SongInfoTable = FetchSongData(Song)
                        for SongDetail in SongInfoTable:
                            print(f'{SongDetail}: {SongInfoTable[SongDetail]}')
                        print()
                    time.sleep(3) #Delay it for the user to read
                    
                #PlaylistAction: Invalid command
                else:
                    print('Invalid command, please try again')
                    
                PrintPlistCmds()
                Action = input('> ')
        #Action: Invalid argument
        else:
            print('Invalid argument, please try again')
    #Action: VIEW
    elif Action[:4] == 'VIEW':
        SAction = Action.split(' ', 1) #Getting the argument from EDIT [arg]
        try: #Just in case the user does not enter an argument at all
            Argument = SAction[1]
        except:
            print('Invalid argument, please try again')
            PrintGeneralCmds()
            Action = input('> ')
            continue
        if Argument in EDITVars: #If variable is one of the allowed edit variables
            print(f'{Argument}: {AccountInfo[Argument]}') #Print it out
    #Action: Invalid command
    else:
        print('Invalid command, please try again')
    PrintGeneralCmds()
    Action = input('> ')

AccountsFile.close()