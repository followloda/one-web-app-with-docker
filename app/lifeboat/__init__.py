# -*- endcoding=UTF-8 -*-
from flask import Flask
app=Flask(__name__)

from app.lifeboat import views,models