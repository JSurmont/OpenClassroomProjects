from ForumProject.src.GifImageFile import GifImageFile
from ForumProject.src.Moderator import Moderator
from ForumProject.src.User import User

if __name__ == '__main__':
    user1 = User("user1", "pwdUser1")

    moderator1 = Moderator("moderator1", "pwdModerator1")

    thread1 = user1.make_thread("Hello World !", "Hey je débute sur ce forum :)")

    thread1.display()

    post1 = moderator1.post(thread1, "Bienvenue, pense à lire les règles du forum :D")

    thread1.display()

    post2 = user1.post(thread1, "Einstein avait-il raison sur E = MC² ?")

    thread1.display()

    post3 = moderator1.post(thread1, "Hello, attention tu es hors sujet ! je supprime ce post :'(")

    thread1.display()

    moderator1.delete(thread1, post2)

    thread1.display()

    moderator1.delete(thread1, post3)

    thread1.display()

    post4 = user1.post(thread1, "Je ne t'aime pas braucoup toi ! :')", GifImageFile("gif1", "300"))

    thread1.display()
