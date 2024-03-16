
Registering as a new user will be asked by the website to confirm his email by clicking on the link
If he tries to log in without confirmation, he will receive a message asking him to confirm the email
Then he can enter
Only the user can edit or delete the post
Any user can see posts
The rest is as required in the following


                        Task: Create a simple blog application
Requirements:
1. Create a Django Rest API called "blog" and integrate it into a new Django
project.
2. Define a user model called "User" That extends Django AbstractUser Model
and use this custom user model as your AUTH_USER_MODEL.
3. Use Token Authentication system for you authenticated your API.
4. Define a model called "Post" with the following fields:

- title (CharField)
- content (TextField) - This field should be required.
- author (ForeignKey to User)
- Created at (DateTimeField, auto-populated with the current timestamp)
- Updated at (DateTimeField, auto-populated with the update timestamp)

5. Create appropriate views to perform the following tasks:
- Register, Login, and logout for user.
- Publish post by specific user as Author.
- List Published posts with data about Author.
- Update and Delete Published posts by Author only.

6. Implement serializers to convert the User and Post model instances into JSON
format and vice versa.


7. Write unit tests to ensure the correct functioning of the views and models.
Preferable to use MongoDB instead of the default database (SQLite) using two ways:

First ORM and you can use djongo package:
Install the djongo package: pip install djongo.
Configure Django to use MongoDB as the database backend in the project's settings.py
file.


Second ODM and you can the mongoengine package:
- Install the mongoengine package: pip install mongoengine
- you won’t need to configure Django settings for database or migrate anything to db.


valuation Criteria:

- Correctness and functionality of the implemented models, views, and serializers.
- Proper usage of Django's best practices and conventions.
- Error handling and validation of user input.
- All should be pushed to a github repository.
- Optional: write unite tests for all implemented views.
- Optional and preferable: Ability to use MongoDB as the database backend (nice to use it).
                            
                            
                                        Good Luck!
