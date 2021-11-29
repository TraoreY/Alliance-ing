run api.py for start api

#requests syntax

METHOD GET

http://127.0.0.1:5000/sectionname?namepost=namepost --> Get one post (post and sectionname=actualites or formations)

http://127.0.0.1:5000/sectionname --> Get all posts (post and sectionname=actualites or formations)

METHOD PUT

http://127.0.0.1:5000/sectionname?namepost=newnamepost&uriimg=newuriimg&descriptionpost=newdescriptionpost --> Update one post (post and sectionname=actualites or formations)


METHOD DELETE

http://127.0.0.1:5000/sectionname?namepost=namepost --> Delete one post (post and sectionname=actualites or formations)


METHOD POST 

http://127.0.0.1:5000/sectionname?namepost=namepost&uriimg=uriimg&descriptionpost=descriptionpost --> add new post(sectionname=actualites or formations)