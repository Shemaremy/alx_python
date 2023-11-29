def validate_password(password):
 
     if any(i.isalpha()==False for i in password) and any(i.isspace()!=True for i in password) and len(password)>=8:

         if any(char.isupper() for char in password) and any(char.islower() for char in password):              
              m="True"
         else:                                
              m="False"

     else:
             m="False"


     return m            
        

