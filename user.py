class user:
    
    user_list = []
    
    
   def __init__(self,first_name,last_name,name,password):
     


        self.first_name = first_name
        self.last_name = last_name
        self.username = name
        self.password = password
        
    def save_user(self):
    
        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)  
        


    def delete_user(self):
    
        User.user_list.remove(self)

    
    