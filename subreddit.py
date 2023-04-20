posts_dict = {"Title": [], "Post Text": [],
            "ID": [], "Score": [], "Upvote Ratio": [],
            "Total Comments": [],"Created On":[], "Post URL": [],
            "Original Content": []
            }
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
        self.title = dict['Title']
        self.posttext = dict['Post Text']
        self.id = dict['id']
        self.score = dict['Score']
        self.upvoteratio = round(dict['Upvote Ratio'],1)
        self.totalcomment = dict['Total Comments']
        self.createtime = dict['Created On']
        self.orignialcontent = dict['Original Content']

    def info(self):
        return str(self.name) + " about " + str(self.categories) + " (rating: " + str(self.rating) + ")" + " (distance: " + str(self.distance) + "m)"