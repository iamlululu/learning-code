from app import train_sprider
from app.conf import tconf


if __name__ == '__main__':
    conf = tconf()
    train_sprider(conf)
