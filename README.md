1. Registered as a new user and confirmed my email by clicking on the link provided by the website.
2. If attempting to log in without email confirmation, I received a prompt to confirm my email before gaining access.
3. Only the user who authored a post can edit or delete it.
4. All users can view posts.
5. Implemented the following tasks as required:
    *Created a Django Rest API named "blog" and integrated it into a new Django project.
    *Defined a custom user model called "User" extending the Django AbstractUser Model and set it as the AUTH_USER_MODEL.
    *Utilized Token Authentication for API authentication.
    *Defined a model named "Post" with the specified fields (title, content, author, Created at, Updated at).
    *Developed views for user registration, login, logout, publishing posts by authors, listing published posts with author data, updating, and deleting published posts by the author.
    *Implemented serializers for converting User and Post model instances into JSON format and vice versa.
6. Conducted unit tests to ensure the correct functioning of views and models.
7. Configured Django to use MongoDB as the database backend in the project's settings.py file using the Djongo package.
