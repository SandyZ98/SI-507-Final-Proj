class Post:
    '''
    This class defines the attributes and methods about restaurants
    Parameters:
    ----------
    dict: dict
        a dictionary that contains all the information about a restaurant
    Returns
    -------
    name, categories, phoneNumber, location, rating, url: string
        the information about the restaurant
    info: function
        will print the information about this restaurant
    '''

    def __init__(self, dict):
        self.subreddit = dict['Subreddit']
        self.title = dict['Title']
        self.posttext = dict['Post Text']
        self.id = dict['ID']
        self.score = dict['Score']
        self.upvoteratio = dict['Upvote Ratio']
        self.totalcomment = dict['Total Comments']
        self.createtime = dict['Created On']
        self.orignialcontent = dict['Original Content']

    def info(self):
        return str(self.subreddit) + " about " + str(self.title) + " (rating: " + str(self.posttext) + ")" + " (distance: " + str(self.score) + "m)"

